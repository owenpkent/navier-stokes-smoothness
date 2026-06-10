"""Kinematic probe for the local-induction-depletion conjecture.

Conjecture (BUILDER, pressure-nonlocality lens): the enstrophy production carried
by the strain that vorticity induces within its own dissipative-scale neighborhood
r_nu = sqrt(nu/|omega|) is dominated by viscous dissipation:

    integral omega . S_loc omega dx  <=  (nu/2) ||grad omega||_2^2
                                          + C0 nu ||omega||_2^2 / L0^2 .

Probe uses the Littlewood-Paley variant: S_loc = strain of the high-pass velocity
P_{k > k_c} u with k_c = sqrt(max|omega| / nu) (the global proxy for 1/r_nu).
Two fields:
  R: random divergence-free multiscale field, E(k) ~ k^{-5/3}, 1 <= k <= 20.
  P: antiparallel vortex pair (Crow geometry), separation tuned near r_nu,
     the classical mutual-stretching configuration.
Reported: P_loc, the viscous budget D = (nu/2)||grad omega||^2, ratio P_loc/D,
across a sweep of nu. Kill condition for the conjecture: ratio > 1 robustly,
growing under resolution refinement, in a dynamically sustained configuration.

RESOLUTION CAVEAT: at N=64 the dissipative cutoff k_c = sqrt(max|omega|/nu) lands
near 70-100, far above the resolved kmax = N/3 = 21, so the high-pass projector
P_{k>k_c} captures nothing and P_loc collapses to ~0. The probe is therefore a
null placeholder at this resolution and only becomes informative at N >= ~256 (or
a fixed moderate k_c decoupled from nu). Kept as a scaffold, not yet a verdict.
"""

import numpy as np

N = 64
L = 2 * np.pi
x1 = np.arange(N) * L / N
X, Y, Z = np.meshgrid(x1, x1, x1, indexing="ij")
k1 = np.fft.fftfreq(N, d=1.0 / N)
KX, KY, KZ = np.meshgrid(k1, k1, k1, indexing="ij")
K2 = KX**2 + KY**2 + KZ**2
Kmag = np.sqrt(K2)
fft, ifft = np.fft.fftn, np.fft.ifftn
dV = (L / N) ** 3
Ks = (KX, KY, KZ)


def gradients(u_hats):
    A = np.empty((3, 3, N, N, N))
    for j in range(3):
        for i in range(3):
            A[i, j] = np.real(ifft(1j * Ks[i] * u_hats[j]))
    return A


def vorticity(A):
    return np.stack([A[1, 2] - A[2, 1], A[2, 0] - A[0, 2], A[0, 1] - A[1, 0]])


def production_split(u_hats, nu, label):
    A = gradients(u_hats)
    w = vorticity(A)
    wmax = np.sqrt((w**2).sum(0)).max()
    k_c = np.sqrt(wmax / nu)
    hp = (Kmag > k_c).astype(float)
    A_loc = gradients([uh * hp for uh in u_hats])
    S_loc = 0.5 * (A_loc + A_loc.transpose(1, 0, 2, 3, 4))
    S_full = 0.5 * (A + A.transpose(1, 0, 2, 3, 4))

    P_loc = np.einsum("i...,ij...,j...->...", w, S_loc, w).sum() * dV
    P_tot = np.einsum("i...,ij...,j...->...", w, S_full, w).sum() * dV
    grad_w2 = 0.0
    for c in w:
        ch = fft(c)
        grad_w2 += sum(np.abs(np.real(ifft(1j * Kq * ch))) ** 2 for Kq in Ks).sum() * dV
    D = 0.5 * nu * grad_w2
    ens = (w**2).sum() * dV
    print(f"[{label}] nu={nu:.3g} k_c={k_c:6.1f} (kmax_resolved={N//3}) | "
          f"P_tot={P_tot:9.3e} P_loc={P_loc:9.3e} D={D:9.3e} | "
          f"P_loc/D={P_loc/D:7.3f} | nu*ens={nu*ens:8.3e}")


def project_divfree(u_hats):
    div = sum(1j * Ks[i] * u_hats[i] for i in range(3))
    K2s = np.where(K2 == 0, 1.0, K2)
    return [u_hats[i] - (-1j * Ks[i]) * (-div) / K2s for i in range(3)]
    # u - k (k.u)/|k|^2 in Fourier form


# Field R: random multiscale divergence-free, E(k) ~ k^{-5/3}
rng = np.random.default_rng(7)
u_hats = []
Kmag_safe = np.where(Kmag > 0, Kmag, 1.0)
amp = np.where((Kmag >= 1) & (Kmag <= 20), Kmag_safe**(-5.0 / 6.0 - 1.0), 0.0)
for _ in range(3):
    phase = rng.uniform(0, 2 * np.pi, (N, N, N))
    u_hats.append(amp * np.exp(1j * phase) * N**3)
u_hats = project_divfree(u_hats)
# enforce real field
u_phys = [np.real(ifft(uh)) for uh in u_hats]
scale = 3.0 / max(np.abs(c).max() for c in u_phys)
u_hats = [fft(c * scale) for c in u_phys]

print("Field R: random multiscale (E ~ k^-5/3), nu sweep")
for nu in (0.002, 0.005, 0.01, 0.02, 0.05):
    production_split(u_hats, nu, "R random")
print()

# Field P: antiparallel pair, separation d, cores of width a
a, d = 0.35, 0.5
psi_z = (np.exp(-(((X - np.pi)**2 + (Y - np.pi - d / 2)**2)) / (2 * a**2))
         - np.exp(-(((X - np.pi)**2 + (Y - np.pi + d / 2)**2)) / (2 * a**2)))
# slight sinusoidal displacement along z to seed Crow-type axial variation
psi_z = psi_z * (1.0 + 0.2 * np.cos(2 * Z))
pz_hat = fft(psi_z)
u_hats_P = [1j * KY * pz_hat, -1j * KX * pz_hat, np.zeros_like(pz_hat)]
u_hats_P = project_divfree(u_hats_P)

print(f"Field P: antiparallel pair, separation d={d}, core a={a}")
for nu in (0.002, 0.005, 0.01, 0.02, 0.05, 0.125):
    production_split(u_hats_P, nu, "P pair  ")
