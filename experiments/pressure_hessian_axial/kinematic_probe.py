"""Kinematic probe for the axial-pressure-concavity-depletion conjecture.

The conjecture (BUILDER, pressure-nonlocality lens): for divergence-free u on T^3,
at rotation-dominated points (|omega|^2 >= 4 |S|^2), the negative axial pressure
curvature is controlled by the local strain plus a scale-integrated (Dini) maximal
function of the axial inhomogeneity:

    (-what . Hess p . what)_+  <=  C0 |S|^2
        + C0 * sum_dyadic_r  avg_{B_r(x)} |(what . grad) u| |grad u|

where what = omega/|omega|. Key kinematic facts probed here:
  1. tr(A^2) = d_i d_j (u_i u_j) for div-free u (so Hess p = R_i R_j applied to it).
  2. Laplacian p = |omega|^2/2 - |S|^2.
  3. R_z^2 annihilates z-independent sources: a perfectly columnar (2.5D) flow has
     ZERO axial pressure curvature. Axial concavity requires axial inhomogeneity.
  4. The sup-over-scales majorant fails on multi-scale coaxial telescopes (the
     contributions add over scales), but the Dini (sum over scales) majorant is
     expected to stay O(1). This script measures both ratios on three fields:
       A: pure column (null test: LHS should be ~ 0),
       B: axially modulated column (single-scale test),
       C: coaxial telescope of modulated columns at dyadic scales (adversarial).

Everything is kinematic: no time stepping. u is built as curl(psi), hence exactly
divergence-free up to spectral precision.
"""

import numpy as np

N = 64
L = 2 * np.pi
x1 = np.arange(N) * L / N
X, Y, Z = np.meshgrid(x1, x1, x1, indexing="ij")
k1 = np.fft.fftfreq(N, d=1.0 / N)
KX, KY, KZ = np.meshgrid(k1, k1, k1, indexing="ij")
K2 = KX**2 + KY**2 + KZ**2
K2_safe = np.where(K2 == 0, 1.0, K2)

fft, ifft = np.fft.fftn, np.fft.ifftn


def deriv(f_hat, K):
    return np.real(ifft(1j * K * f_hat))


def grad_phys(f):
    fh = fft(f)
    return deriv(fh, KX), deriv(fh, KY), deriv(fh, KZ)


def curl_of_psi(psi):
    """u = curl psi, exactly divergence-free."""
    px, py, pz = (fft(c) for c in psi)
    ux = deriv(pz, KY) - deriv(py, KZ)
    uy = deriv(px, KZ) - deriv(pz, KX)
    uz = deriv(py, KX) - deriv(px, KY)
    return ux, uy, uz


def velocity_gradients(u):
    A = np.empty((3, 3, N, N, N))
    for j, comp in enumerate(u):
        gx, gy, gz = grad_phys(comp)
        A[0, j], A[1, j], A[2, j] = gx, gy, gz   # A[i,j] = d_i u_j
    return A


def analyze(u, label):
    A = velocity_gradients(u)
    S = 0.5 * (A + A.transpose(1, 0, 2, 3, 4))
    wx = A[1, 2] - A[2, 1]
    wy = A[2, 0] - A[0, 2]
    wz = A[0, 1] - A[1, 0]
    w2 = wx**2 + wy**2 + wz**2
    S2 = np.einsum("ij...,ij...->...", S, S)

    # identity check 1: tr(A^2) = d_i d_j (u_i u_j)
    trA2 = np.einsum("ij...,ji...->...", A, A)
    ddu = np.zeros((N, N, N))
    Ks = (KX, KY, KZ)
    for i in range(3):
        for j in range(3):
            ddu += np.real(ifft(-Ks[i] * Ks[j] * fft(u[i] * u[j])))
    id1 = np.max(np.abs(trA2 - ddu)) / max(np.max(np.abs(trA2)), 1e-30)

    # pressure and its Hessian: p = (-Lap)^{-1} tr(A^2)
    p_hat = fft(trA2) / K2_safe
    p_hat[0, 0, 0] = 0.0
    lap_p = np.real(ifft(-K2 * p_hat))
    id2 = np.max(np.abs(lap_p - (0.5 * w2 - S2))) / max(np.max(np.abs(lap_p)), 1e-30)

    H = np.empty((3, 3, N, N, N))
    for i in range(3):
        for j in range(3):
            H[i, j] = np.real(ifft(-Ks[i] * Ks[j] * p_hat))

    wmag = np.sqrt(w2) + 1e-30
    what = np.stack([wx, wy, wz]) / wmag
    axial = np.einsum("i...,ij...,j...->...", what, H, what)
    lhs = np.maximum(-axial, 0.0)

    # axial-inhomogeneity density g = |(what.grad)u| |grad u| (local direction)
    g = np.zeros((N, N, N))
    for j in range(3):
        dz_u_j = np.einsum("i...,i...->...", what, A[:, j])
        g += dz_u_j**2
    g = np.sqrt(g) * np.sqrt(np.einsum("ij...,ij...->...", A, A))

    # dyadic Gaussian averages of g: Dini = sum over scales, Sup = max over scales
    radii = [(2.0**k) * (L / N) * 1.5 for k in range(6)]
    filtered = []
    gh = fft(g)
    for r in radii:
        filtered.append(np.real(ifft(gh * np.exp(-0.5 * K2 * r**2))))
    D_dini = np.sum(filtered, axis=0)
    D_sup = np.max(filtered, axis=0)

    mask = (w2 >= 4.0 * S2) & (wmag >= 0.25 * wmag.max())
    npts = int(mask.sum())
    eps = 1e-12 * max(S2.max(), 1.0)
    r_dini = (lhs / (S2 + D_dini + eps))[mask]
    r_sup = (lhs / (S2 + D_sup + eps))[mask]
    r_loc = (lhs / (S2 + eps))[mask]

    print(f"[{label}] identity tr(A^2)=dd(uu): rel err {id1:.2e} | "
          f"Lap p = w^2/2 - |S|^2: rel err {id2:.2e}")
    print(f"[{label}] rotation-dominated pts: {npts}, max LHS {lhs[mask].max():.4e}"
          if npts else f"[{label}] no rotation-dominated points")
    if npts:
        print(f"[{label}] ratio LHS/(|S|^2 + Dini): max {r_dini.max():.3f} "
              f"median {np.median(r_dini):.3f}")
        print(f"[{label}] ratio LHS/(|S|^2 + Sup) : max {r_sup.max():.3f}")
        print(f"[{label}] ratio LHS/|S|^2 (no nonlocal term): max {r_loc.max():.3f}")
    print()


def column(a, amp, m=0, eps_mod=0.0, x0=np.pi, y0=np.pi):
    """Vector potential for a Gaussian vortex column along z, optionally
    axially modulated with wavenumber m and relative amplitude eps_mod."""
    r2 = (X - x0)**2 + (Y - y0)**2
    phi = amp * np.exp(-r2 / (2 * a**2))
    if m:
        phi = phi * (1.0 + eps_mod * np.cos(m * Z))
    return phi


# Field A: pure column (2.5D): LHS should vanish identically.
psiA = (np.zeros((N, N, N)), np.zeros((N, N, N)), column(0.5, 1.0))
analyze(curl_of_psi(psiA), "A column")

# Field B: single axially modulated column.
psiB = (np.zeros((N, N, N)), np.zeros((N, N, N)), column(0.5, 1.0, m=4, eps_mod=0.5))
analyze(curl_of_psi(psiB), "B modulated")

# Field C: coaxial telescope, equal |grad u| per dyadic scale, coherent modulation.
pz = np.zeros((N, N, N))
for j in range(4):
    a_j = 0.5 / 2**j
    pz += column(a_j, a_j**2 * 4.0, m=min(4 * 2**j, N // 3), eps_mod=0.5)
psiC = (np.zeros((N, N, N)), np.zeros((N, N, N)), pz)
analyze(curl_of_psi(psiC), "C telescope")
