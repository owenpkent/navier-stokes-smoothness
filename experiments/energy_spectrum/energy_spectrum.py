"""Experiment (c): energy spectrum and dissipation.

Computes the kinetic-energy spectrum E(k) and the dissipation rate from a 3D
velocity field. If a Taylor-Green DNS cache exists (from the taylor_green
experiment), it would be read; otherwise this builds a representative
divergence-free field with a prescribed spectrum so the experiment always runs
standalone.

WHY this matters for the problem: the spectrum shows how energy is distributed
across scales, and the dissipation rate

    epsilon = 2 nu * sum_k k^2 E(k)

is dominated by the high-wavenumber (small-scale) end. The picture makes the
supercriticality concrete: the energy lives at large scales (low k) where the
a priori bound holds, but a singularity would form at small scales (high k)
where the energy gives no control and where finite resolution always bites
first. The wavenumber where E(k) starts to fall off against the grid Nyquist
limit is exactly where a coarse DNS can no longer be trusted, which is the
numerical face of the analytic gap.

The synthetic field uses a Kolmogorov-like injection spectrum E(k) ~ k^4
exp(-2(k/k0)^2) (a standard smooth, finite-energy model). With a real DNS field
the inertial-range slope would approach -5/3 at high Reynolds number; at the low
Reynolds number of the coarse TG run the spectrum is steeper (more dissipative),
which is itself the point: at low Re there is no inertial range and no incipient
singularity.
"""

from __future__ import annotations

import os

import numpy as np


def _wavenumbers(n):
    k1 = np.fft.fftfreq(n, d=1.0 / n)
    kx, ky, kz = np.meshgrid(k1, k1, k1, indexing="ij")
    return kx, ky, kz


def synthetic_field(n=32, k0=4.0, seed=0):
    """Build a random divergence-free velocity with a smooth injection spectrum.

    The amplitude envelope sqrt(k^4 exp(-2 (k/k0)^2)) gives a peaked, smooth,
    finite-energy spectrum. Random phases make it a generic field; the Leray
    projection makes it incompressible.
    """
    rng = np.random.default_rng(seed)
    kx, ky, kz = _wavenumbers(n)
    k2 = kx**2 + ky**2 + kz**2
    k = np.sqrt(k2)
    k2_safe = k2.copy()
    k2_safe[0, 0, 0] = 1.0

    envelope = np.sqrt((k**4) * np.exp(-2.0 * (k / k0) ** 2))
    uh = np.zeros((3, n, n, n), dtype=np.complex128)
    for i in range(3):
        phase = np.exp(2j * np.pi * rng.random((n, n, n)))
        uh[i] = envelope * phase
    # Leray projection: remove the component along k
    kdotu = kx * uh[0] + ky * uh[1] + kz * uh[2]
    uh[0] -= kx * kdotu / k2_safe
    uh[1] -= ky * kdotu / k2_safe
    uh[2] -= kz * kdotu / k2_safe
    uh[:, 0, 0, 0] = 0.0  # zero mean
    return uh, (kx, ky, kz)


def load_cached_velocity():
    """Try to load a velocity field from a Taylor-Green cache; else None.

    The TG experiment caches diagnostics, not the full field, so by default this
    returns None and we use the synthetic field. Kept as a hook for when a
    field-snapshot cache is added.
    """
    return None


def energy_spectrum(uh, kgrid):
    """Shell-averaged energy spectrum E(k) and total energy.

    E(k) is the sum of (1/2)|u_hat|^2 over the spherical shell |k| in
    [k-1/2, k+1/2). Sum over k recovers the total energy (Parseval).
    """
    kx, ky, kz = kgrid
    n = uh.shape[1]
    kmag = np.sqrt(kx**2 + ky**2 + kz**2)
    # spectral energy density per mode (normalized so sums match physical mean)
    e_density = 0.5 * (np.abs(uh[0]) ** 2 + np.abs(uh[1]) ** 2 + np.abs(uh[2]) ** 2) / (n**6)
    kbins = np.arange(0, int(np.ceil(kmag.max())) + 2)
    Ek = np.zeros(len(kbins) - 1)
    kshell = np.floor(kmag + 0.5).astype(int)
    for idx in range(len(Ek)):
        Ek[idx] = e_density[kshell == idx].sum()
    kcenters = kbins[:-1]
    return kcenters, Ek


def main():
    n = int(os.environ.get("NS_SPEC_N", "32"))
    nu = float(os.environ.get("NS_SPEC_NU", "0.025"))

    print("Energy spectrum and dissipation")
    cached = load_cached_velocity()
    if cached is not None:
        uh, kgrid = cached
        source = "Taylor-Green DNS cache"
    else:
        uh, kgrid = synthetic_field(n=n, k0=4.0)
        source = "synthetic divergence-free field (E(k) ~ k^4 exp(-2(k/k0)^2))"
    print(f"field source: {source}")
    print(f"grid {n}^3, nu = {nu}")
    print()

    kc, Ek = energy_spectrum(uh, kgrid)
    total_energy = float(Ek.sum())
    kx, ky, kz = kgrid
    # dissipation rate epsilon = 2 nu sum_k k^2 E(k)
    k2c = kc.astype(float) ** 2
    epsilon = 2.0 * nu * float((k2c * Ek).sum())

    print(f"{'k':>4} {'E(k)':>14} {'k^2 E(k) (dissip. integrand)':>30}")
    print("-" * 52)
    for i in range(min(len(kc), 16)):
        print(f"{kc[i]:>4d} {Ek[i]:>14.6e} {k2c[i] * Ek[i]:>30.6e}")
    print()
    # find the peak of the dissipation integrand (where small scales dissipate)
    dissip_integrand = k2c * Ek
    k_peak_diss = int(kc[int(np.argmax(dissip_integrand))]) if len(kc) else 0
    nyquist = n // 2
    print("FINDINGS:")
    print(f"  total energy (Parseval): {total_energy:.6f}")
    print(f"  dissipation rate epsilon = 2 nu sum k^2 E(k) = {epsilon:.6e}")
    print(f"  dissipation peaks near k = {k_peak_diss} (grid Nyquist k = {nyquist})")
    print()
    print("  Reading: energy sits at low k (large scales) where the a priori bound")
    print("  holds; dissipation is weighted by k^2 toward high k (small scales),")
    print("  exactly where a singularity would form and where finite resolution")
    print("  bites first. This is the numerical face of the supercriticality gap.")

    ratio = k_peak_diss / max(nyquist, 1)
    print()
    print(f"  resolution check: dissipation peak / Nyquist = {ratio:.2f}")
    print(f"  {'(well resolved)' if ratio < 0.6 else '(marginally resolved: refine the grid)'}")

    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt

        fig, axs = plt.subplots(1, 2, figsize=(11, 4.5))
        mask = (kc > 0) & (Ek > 0)
        axs[0].loglog(kc[mask], Ek[mask], "o-")
        axs[0].set_xlabel("wavenumber k"); axs[0].set_ylabel("E(k)")
        axs[0].set_title("energy spectrum")
        axs[1].semilogy(kc[mask], (k2c * Ek)[mask], "s-")
        axs[1].set_xlabel("wavenumber k"); axs[1].set_ylabel("k^2 E(k)")
        axs[1].set_title("dissipation integrand")
        fig.tight_layout()
        out = os.path.join(os.path.dirname(__file__), "energy_spectrum.png")
        fig.savefig(out, dpi=110)
        print(f"  plot written to {out}")
    except Exception as exc:
        print(f"  (plot skipped: {exc})")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
