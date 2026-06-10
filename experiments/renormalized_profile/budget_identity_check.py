"""Numerical check of the renormalized (similarity-variable) enstrophy budget.

In backward self-similar variables y = x/sqrt(T-t), s = -log(T-t), with
u(x,t) = (T-t)^{-1/2} U(y,s), the vorticity Omega = curl U obeys

    d_s Omega + Omega + (1/2)(y . grad)Omega + (U . grad)Omega
        = (Omega . grad)U + Lap Omega.

Dotting with Omega and integrating over R^3 (decaying fields) gives the budget

    d/ds (1/2)\int|Omega|^2 = -\int|grad Omega|^2 - (1/4)\int|Omega|^2
                              + \int Omega . S . Omega,

so a STEADY profile must satisfy

    \int Omega . S . Omega = (1/4)\int|Omega|^2 + \int|grad Omega|^2,

hence ||S||_inf > 1/4 (the strain-quarter quantization). The 1/4 comes from
two integration-by-parts facts checked here on random decaying div-free fields:

  (A)  \int Omega . ((1/2) y . grad) Omega dy = -(3/4) \int |Omega|^2 dy
  (B)  \int Omega . ((U . grad) Omega) dy     = 0          (div U = 0)
  (C)  \int Omega . ((Omega . grad) U) dy     = \int Omega_i S_ij Omega_j dy

Spectral derivatives on a large periodic box; fields are curl of a
Gaussian-enveloped random potential so they are exactly divergence-free and
decay fast enough that periodic wrap error is below the reported tolerance.
"""

import numpy as np

N = 64
L = 16.0          # box [-8, 8)^3; envelope sigma = 2 puts wrap error ~ e^{-8}
SIGMA = 2.0
KMAX = 3          # low-mode random potential
SEED = 7


def spectral_grad(f, K):
    fh = np.fft.fftn(f)
    return [np.real(np.fft.ifftn(1j * K[a] * fh)) for a in range(3)]


def main():
    rng = np.random.default_rng(SEED)
    h = L / N
    coords = np.arange(N) * h - L / 2.0
    y = np.meshgrid(coords, coords, coords, indexing="ij")
    k1 = 2.0 * np.pi * np.fft.fftfreq(N, d=h)
    K = np.meshgrid(k1, k1, k1, indexing="ij")

    # random low-mode vector potential, Gaussian envelope, then U = curl A
    env = np.exp(-(y[0] ** 2 + y[1] ** 2 + y[2] ** 2) / (2.0 * SIGMA ** 2))
    A = []
    for _ in range(3):
        fh = np.zeros((N, N, N), dtype=complex)
        idx = np.arange(-KMAX, KMAX + 1)
        for a in idx:
            for b in idx:
                for c in idx:
                    fh[a, b, c] = rng.normal() + 1j * rng.normal()
        f = np.real(np.fft.ifftn(fh))
        f /= np.max(np.abs(f))
        A.append(f * env)

    gA = [spectral_grad(A[a], K) for a in range(3)]
    U = [gA[2][1] - gA[1][2], gA[0][2] - gA[2][0], gA[1][0] - gA[0][1]]
    gU = [spectral_grad(U[a], K) for a in range(3)]
    W = [gU[2][1] - gU[1][2], gU[0][2] - gU[2][0], gU[1][0] - gU[0][1]]
    gW = [spectral_grad(W[a], K) for a in range(3)]

    dV = h ** 3
    ens = sum(np.sum(W[a] ** 2) for a in range(3)) * dV

    # (A) drift dilution coefficient
    drift = sum(
        np.sum(W[i] * 0.5 * (y[0] * gW[i][0] + y[1] * gW[i][1] + y[2] * gW[i][2]))
        for i in range(3)
    ) * dV
    # (B) transport orthogonality
    transp = sum(
        np.sum(W[i] * (U[0] * gW[i][0] + U[1] * gW[i][1] + U[2] * gW[i][2]))
        for i in range(3)
    ) * dV
    # (C) stretching = strain quadratic form
    stretch = sum(
        np.sum(W[i] * (W[0] * gU[i][0] + W[1] * gU[i][1] + W[2] * gU[i][2]))
        for i in range(3)
    ) * dV
    strainq = sum(
        np.sum(W[i] * 0.5 * (gU[j][i] + gU[i][j]) * W[j])
        for i in range(3) for j in range(3)
    ) * dV

    div_check = max(
        np.max(np.abs(gU[0][0] + gU[1][1] + gU[2][2])),
        0.0,
    )

    print(f"grid N={N}, box L={L}, envelope sigma={SIGMA}, seed={SEED}")
    print(f"max |div U|                 : {div_check:.3e}")
    print(f"enstrophy  int|Omega|^2     : {ens:.6e}")
    print(f"(A) drift integral          : {drift:.6e}")
    print(f"    -(3/4) enstrophy        : {-0.75 * ens:.6e}")
    print(f"    relative error          : {abs(drift + 0.75 * ens) / ens:.3e}")
    print(f"(B) transport integral      : {transp:.6e}")
    print(f"    relative to enstrophy   : {abs(transp) / ens:.3e}")
    print(f"(C) stretching integral     : {stretch:.6e}")
    print(f"    strain quadratic form   : {strainq:.6e}")
    print(f"    relative error          : {abs(stretch - strainq) / max(abs(stretch), 1e-30):.3e}")

    # (A) is limited by periodic wrap error of the envelope tail: |A| ~ e^{-8}
    # at |y| = L/2, so the |y|-weighted enstrophy-relative residual is ~ 1e-6.
    # (B) and (C) are exact integration-by-parts identities on the torus and
    # hold to machine precision regardless of the envelope.
    ok = (
        abs(drift + 0.75 * ens) / ens < 1e-4
        and abs(transp) / ens < 1e-9
        and abs(stretch - strainq) / max(abs(stretch), 1e-30) < 1e-9
    )
    print("BUDGET IDENTITY COEFFICIENTS:", "CONFIRMED" if ok else "FAILED")


if __name__ == "__main__":
    main()
