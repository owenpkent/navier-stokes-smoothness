"""Pseudo-spectral incompressible-flow solvers on the periodic torus.

Provides the shared computational substrate for the experimental thread:

  - Flow3D: a 3D incompressible Navier-Stokes solver on T^3 = [0, 2pi)^3, using
    a Fourier collocation (pseudo-spectral) method with explicit RK time
    stepping and projection onto divergence-free fields at every step.
  - Flow2D: the 2D vorticity-streamfunction solver, used as the CONTROL. In 2D
    there is no vortex-stretching term, the enstrophy is non-increasing, and the
    solution stays smooth for all time (Ladyzhenskaya). Any 3D method that would
    "apply" equally in 2D and predict 2D blow-up is structurally wrong.

WHY pseudo-spectral: incompressibility (div u = 0) is a projection in Fourier
space (the Leray projector is algebraic on each wavenumber), and derivatives are
multiplications by i*k. This makes the divergence-free constraint exact to
machine precision and the diagnostics (energy, enstrophy, vorticity) cheap.

These solvers are deliberately small-grid (32^3 by default). They are a teaching
and control substrate, not research-resolution DNS.
"""

from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np


def _wavenumbers(n: int):
    """FFT-ordered integer wavenumbers for an n-point periodic grid on [0, 2pi)."""
    return np.fft.fftfreq(n, d=1.0 / n).astype(np.float64)


@dataclass
class Diagnostics3D:
    """Time series of scalar diagnostics from a Flow3D run."""

    t: list = field(default_factory=list)
    energy: list = field(default_factory=list)            # (1/2) mean |u|^2
    enstrophy: list = field(default_factory=list)          # (1/2) mean |omega|^2
    max_vorticity: list = field(default_factory=list)      # ||omega||_Linfty
    bkm_integral: list = field(default_factory=list)        # running int_0^t ||omega||_inf ds


class Flow3D:
    """3D incompressible Navier-Stokes on T^3 via a pseudo-spectral method.

    State is the three velocity components in Fourier space. The Leray
    projection (incompressibility) is applied to the nonlinear term every
    substep, so div u = 0 holds spectrally. Time stepping is an explicit
    low-storage RK2 (Heun) on the projected right-hand side, with the viscous
    term treated explicitly. Stable for the small grids and viscosities used
    here.
    """

    def __init__(self, n: int = 32, nu: float = 0.02):
        self.n = n
        self.nu = float(nu)

        k1 = _wavenumbers(n)
        self.kx, self.ky, self.kz = np.meshgrid(k1, k1, k1, indexing="ij")
        self.k2 = self.kx**2 + self.ky**2 + self.kz**2
        self.k2_nozero = self.k2.copy()
        self.k2_nozero[0, 0, 0] = 1.0  # avoid division by zero at the mean mode

        self.uh = np.zeros((3, n, n, n), dtype=np.complex128)

    # --- field setup -----------------------------------------------------

    def set_velocity(self, u_phys):
        """Set the (real) physical-space velocity field, then project."""
        for i in range(3):
            self.uh[i] = np.fft.fftn(u_phys[i])
        self._project()

    def grid(self):
        """Return the three coordinate arrays (each shape n^3) on [0, 2pi)."""
        x1 = np.linspace(0.0, 2.0 * np.pi, self.n, endpoint=False)
        return np.meshgrid(x1, x1, x1, indexing="ij")

    # --- core operators --------------------------------------------------

    def _project(self):
        """Apply the Leray projector P = I - grad div^{-1} div in Fourier space.

        On each wavenumber k, P removes the component of u_hat along k, leaving
        the divergence-free part. This is the algebraic content of
        incompressibility.
        """
        kdotu = self.kx * self.uh[0] + self.ky * self.uh[1] + self.kz * self.uh[2]
        self.uh[0] -= self.kx * kdotu / self.k2_nozero
        self.uh[1] -= self.ky * kdotu / self.k2_nozero
        self.uh[2] -= self.kz * kdotu / self.k2_nozero

    def _rhs(self, uh):
        """Projected right-hand side d(uh)/dt = P[ -(u.grad)u ] - nu k^2 uh.

        The nonlinear term is computed in physical space (the "pseudo" in
        pseudo-spectral) and projected. The viscous term is diagonal in Fourier
        space.
        """
        u = np.array([np.fft.ifftn(uh[i]).real for i in range(3)])
        # velocity gradients du_i/dx_j in physical space
        rhs = np.zeros_like(uh)
        adv = np.zeros((3, self.n, self.n, self.n), dtype=np.float64)
        for i in range(3):
            dui_dx = np.fft.ifftn(1j * self.kx * uh[i]).real
            dui_dy = np.fft.ifftn(1j * self.ky * uh[i]).real
            dui_dz = np.fft.ifftn(1j * self.kz * uh[i]).real
            adv[i] = u[0] * dui_dx + u[1] * dui_dy + u[2] * dui_dz
        for i in range(3):
            rhs[i] = -np.fft.fftn(adv[i])
        # project nonlinear term, then add viscosity
        kdotr = self.kx * rhs[0] + self.ky * rhs[1] + self.kz * rhs[2]
        rhs[0] -= self.kx * kdotr / self.k2_nozero
        rhs[1] -= self.ky * kdotr / self.k2_nozero
        rhs[2] -= self.kz * kdotr / self.k2_nozero
        for i in range(3):
            rhs[i] -= self.nu * self.k2 * uh[i]
        return rhs

    def step(self, dt: float):
        """Advance one step with explicit RK2 (Heun's method)."""
        k1 = self._rhs(self.uh)
        u1 = self.uh + dt * k1
        k2 = self._rhs(u1)
        self.uh = self.uh + 0.5 * dt * (k1 + k2)
        self._project()

    # --- diagnostics -----------------------------------------------------

    def velocity(self):
        return np.array([np.fft.ifftn(self.uh[i]).real for i in range(3)])

    def vorticity(self):
        """omega = curl u, computed spectrally."""
        wx = np.fft.ifftn(1j * (self.ky * self.uh[2] - self.kz * self.uh[1])).real
        wy = np.fft.ifftn(1j * (self.kz * self.uh[0] - self.kx * self.uh[2])).real
        wz = np.fft.ifftn(1j * (self.kx * self.uh[1] - self.ky * self.uh[0])).real
        return np.array([wx, wy, wz])

    def energy(self):
        u = self.velocity()
        return 0.5 * np.mean(u[0] ** 2 + u[1] ** 2 + u[2] ** 2)

    def enstrophy(self):
        w = self.vorticity()
        return 0.5 * np.mean(w[0] ** 2 + w[1] ** 2 + w[2] ** 2)

    def max_vorticity(self):
        w = self.vorticity()
        return float(np.sqrt(w[0] ** 2 + w[1] ** 2 + w[2] ** 2).max())

    def divergence_Linfty(self):
        """Max |div u| in physical space; should be ~machine epsilon after projection."""
        div = np.fft.ifftn(
            1j * (self.kx * self.uh[0] + self.ky * self.uh[1] + self.kz * self.uh[2])
        ).real
        return float(np.abs(div).max())


def taylor_green_initial(n: int):
    """The Taylor-Green vortex initial velocity on T^3.

    u = ( sin x cos y cos z, -cos x sin y cos z, 0 ).

    This is the canonical smooth, divergence-free, finite-energy initial datum
    used to study the transition to small scales. At low Reynolds number it
    relaxes smoothly; the BKM integral stays finite.
    """
    x1 = np.linspace(0.0, 2.0 * np.pi, n, endpoint=False)
    x, y, z = np.meshgrid(x1, x1, x1, indexing="ij")
    u = np.zeros((3, n, n, n))
    u[0] = np.sin(x) * np.cos(y) * np.cos(z)
    u[1] = -np.cos(x) * np.sin(y) * np.cos(z)
    u[2] = 0.0
    return u


class Flow2D:
    """2D incompressible Navier-Stokes (vorticity form) on T^2. The CONTROL.

    In 2D the vorticity is a scalar transported with diffusion,

        d_t w + (u . grad) w = nu * laplacian w,

    with NO vortex-stretching term. The enstrophy integral of w^2 is therefore
    non-increasing, which gives an all-time H^1 bound on u and global
    smoothness (Ladyzhenskaya 1959). This class exists so experiments can
    demonstrate the structural 2D-vs-3D difference directly: any candidate 3D
    regularity mechanism that does not use the stretching term would apply here
    too, where it is not needed, which is the signature of a wrong approach.
    """

    def __init__(self, n: int = 64, nu: float = 0.01):
        self.n = n
        self.nu = float(nu)
        k1 = _wavenumbers(n)
        self.kx, self.ky = np.meshgrid(k1, k1, indexing="ij")
        self.k2 = self.kx**2 + self.ky**2
        self.k2_nozero = self.k2.copy()
        self.k2_nozero[0, 0] = 1.0
        self.wh = np.zeros((n, n), dtype=np.complex128)

    def set_vorticity(self, w_phys):
        self.wh = np.fft.fftn(w_phys)

    def _velocity_from_vorticity(self, wh):
        """u = (d_y psi, -d_x psi) where laplacian psi = -w (Biot-Savart in 2D)."""
        psih = wh / self.k2_nozero
        uh = 1j * self.ky * psih
        vh = -1j * self.kx * psih
        return np.fft.ifftn(uh).real, np.fft.ifftn(vh).real

    def _rhs(self, wh):
        u, v = self._velocity_from_vorticity(wh)
        wx = np.fft.ifftn(1j * self.kx * wh).real
        wy = np.fft.ifftn(1j * self.ky * wh).real
        adv = u * wx + v * wy
        return -np.fft.fftn(adv) - self.nu * self.k2 * wh

    def step(self, dt: float):
        k1 = self._rhs(self.wh)
        w1 = self.wh + dt * k1
        k2 = self._rhs(w1)
        self.wh = self.wh + 0.5 * dt * (k1 + k2)

    def enstrophy(self):
        w = np.fft.ifftn(self.wh).real
        return 0.5 * np.mean(w**2)

    def max_vorticity(self):
        w = np.fft.ifftn(self.wh).real
        return float(np.abs(w).max())
