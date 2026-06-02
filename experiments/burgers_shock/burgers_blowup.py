"""Experiment (b): inviscid vs viscous Burgers, the viscosity control.

The 1D Burgers equation

    d_t u + u d_x u = nu d_xx u

is the simplest model carrying the same quadratic transport nonlinearity as
Navier-Stokes. With nu = 0 (inviscid) a smooth decreasing initial profile
steepens until the gradient blows up in finite time (a shock forms). With nu > 0
the same data stays smooth for all time. This is the cleanest demonstration of
the role of dissipation, and it is a CONTROL for the project: a regularity
argument that is blind to the viscous term cannot be right, because its inviscid
relative is singular (and 3D Euler, the inviscid relative of NS, blows up:
Elgindi 2021).

WHY the gradient is the right diagnostic: for inviscid Burgers, characteristics
x(t) = x0 + u0(x0) t carry constant u, and they cross at the finite time

    t* = -1 / min_x u0'(x)      (when min u0' < 0).

At t* the spatial derivative u_x becomes infinite. We integrate both equations
with an accurate pseudo-spectral scheme and track max |u_x|, showing it diverges
toward t* for nu = 0 and saturates for nu > 0.
"""

from __future__ import annotations

import numpy as np


def _spectral_setup(n):
    x = np.linspace(0.0, 2.0 * np.pi, n, endpoint=False)
    k = np.fft.fftfreq(n, d=1.0 / n)
    return x, k


def _rhs(uh, k, nu):
    """d(uh)/dt for Burgers, computed pseudo-spectrally.

    Nonlinear term written in conservative form (1/2) d_x(u^2) for stability.
    """
    u = np.fft.ifft(uh).real
    flux = 0.5 * u * u
    nonlin = -1j * k * np.fft.fft(flux)
    visc = -nu * (k**2) * uh
    return nonlin + visc


def run(nu, n=512, t_end=2.0, dt=2.0e-4):
    """Integrate Burgers from u0 = sin(x). Returns time series of max|u_x|.

    u0 = sin(x) has min u0' = -1 at x = pi, so the inviscid shock time is
    t* = -1/min(u0') = 1.0.
    """
    x, k = _spectral_setup(n)
    u0 = np.sin(x)
    uh = np.fft.fft(u0)

    times = []
    max_grad = []
    nsteps = int(round(t_end / dt))
    for step in range(nsteps + 1):
        t = step * dt
        if step % 50 == 0:
            ux = np.fft.ifft(1j * k * uh).real
            times.append(t)
            max_grad.append(float(np.abs(ux).max()))
        # RK2 (Heun)
        f1 = _rhs(uh, k, nu)
        u1 = uh + dt * f1
        f2 = _rhs(u1, k, nu)
        uh = uh + 0.5 * dt * (f1 + f2)
        # stop early if the inviscid run has clearly blown up numerically
        if nu == 0.0 and np.abs(np.fft.ifft(1j * k * uh).real).max() > 1e4:
            ux = np.fft.ifft(1j * k * uh).real
            times.append(t)
            max_grad.append(float(np.abs(ux).max()))
            break
    return np.array(times), np.array(max_grad)


def main():
    shock_time = 1.0  # t* = -1/min(sin'(x)) = -1/(-1) = 1.0 for u0 = sin x
    print("1D Burgers: inviscid shock vs viscous regularization")
    print(f"initial data u0 = sin(x); predicted inviscid shock time t* = {shock_time:.3f}")
    print()

    t_inv, g_inv = run(nu=0.0, t_end=1.05, dt=1.0e-4)
    t_visc, g_visc = run(nu=0.05, t_end=2.0, dt=2.0e-4)

    print(f"{'t':>6} {'max|u_x| inviscid':>20} {'max|u_x| viscous nu=0.05':>26}")
    print("-" * 56)
    # sample a few comparable times
    for tt in [0.0, 0.25, 0.5, 0.75, 0.9, 0.95, 0.99]:
        i_inv = int(np.argmin(np.abs(t_inv - tt)))
        i_visc = int(np.argmin(np.abs(t_visc - tt)))
        gi = g_inv[i_inv] if len(g_inv) else float("nan")
        gv = g_visc[i_visc]
        print(f"{tt:>6.2f} {gi:>20.3f} {gv:>26.3f}")

    inv_peak = float(g_inv.max())
    visc_peak = float(g_visc.max())
    print()
    print(f"inviscid  max gradient over the run: {inv_peak:.2f} (diverges toward t* = {shock_time})")
    print(f"viscous   max gradient over the run: {visc_peak:.2f} (bounded for all time)")
    print()

    grew = inv_peak > 10.0 * visc_peak
    print("FINDING:")
    print("  Inviscid Burgers steepens into a shock: max|u_x| blows up as t -> t*.")
    print("  Viscous Burgers stays smooth: max|u_x| saturates at a finite value.")
    print("  CONTROL: dissipation is what prevents the gradient blow-up. A 3D")
    print("  Navier-Stokes regularity argument must use the viscous term; the")
    print("  inviscid relative (3D Euler) is known to be able to blow up (Elgindi 2021).")
    print()
    print(f"  detector: inviscid peak >> viscous peak ? {'YES (control fires)' if grew else 'NO'}")

    # optional plot if matplotlib is present (gitignored output)
    try:
        import os
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt

        fig, ax = plt.subplots(figsize=(7, 4.5))
        ax.plot(t_inv, g_inv, label="inviscid (nu = 0)", lw=2)
        ax.plot(t_visc, g_visc, label="viscous (nu = 0.05)", lw=2)
        ax.axvline(shock_time, ls="--", color="k", alpha=0.5, label="shock time t*")
        ax.set_yscale("log")
        ax.set_xlabel("time t")
        ax.set_ylabel("max |u_x|  (log scale)")
        ax.set_title("Burgers: gradient blow-up (inviscid) vs smoothness (viscous)")
        ax.legend()
        fig.tight_layout()
        out = os.path.join(os.path.dirname(__file__), "burgers_blowup.png")
        fig.savefig(out, dpi=110)
        print(f"  plot written to {out}")
    except Exception as exc:  # plotting is optional
        print(f"  (plot skipped: {exc})")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
