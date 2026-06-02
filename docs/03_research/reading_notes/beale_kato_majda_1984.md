# Reading notes: Beale-Kato-Majda (1984)

J. T. Beale, T. Kato, A. Majda, "Remarks on the breakdown of smooth solutions for the 3-D Euler equations," Comm. Math. Phys. 94 (1984).

## What it proves

A smooth solution on $[0, T)$ can be continued past $T$ if and only if the time integral of the sup-norm of the vorticity is finite:

$$\int_0^T \|\omega(t)\|_{L^\infty}\, dt < \infty.$$

Stated for the 3D Euler equations, the criterion is central for Navier-Stokes too: the vorticity controls the breakdown of smoothness, and the BKM integral is the sharp diagnostic.

## Structural content

- **Vorticity controls everything.** The proof shows that the higher Sobolev norms $\|u(t)\|_{H^s}$ ($s$ large) satisfy a differential inequality
$$\frac{d}{dt}\|u\|_{H^s} \le C\,\|\omega\|_{L^\infty}\,\|u\|_{H^s},$$
so by Gronwall the $H^s$ norm can blow up at $T$ only if $\int_0^T\|\omega\|_\infty\,dt = \infty$. The delicate point is replacing a naive $\|\nabla u\|_{L^\infty}$ (which does not control by Calderon-Zygmund alone) with $\|\omega\|_{L^\infty}$ using a logarithmic Sobolev inequality: $\|\nabla u\|_\infty \lesssim \|\omega\|_\infty (1 + \log^+\|u\|_{H^s}) + \|\omega\|_{L^2}$.
- **The log-Sobolev inequality** is the technical engine and is the reason it is vorticity sup, not velocity gradient sup, that appears.
- **Scaling.** The vorticity scales as $\omega_\lambda(x,t)=\lambda^2\omega(\lambda x,\lambda^2 t)$, so $\|\omega\|_{L^\infty}$ scales like $\lambda^2$; the time integral over the rescaled interval contributes $\lambda^{-2}$. Net: the BKM integral is scale invariant (critical). This is computed in `experiments/_shared/criticality.py`.

## How it bears on the spine

BKM is the canonical critical continuation criterion and the one the DNS tracks directly (`experiments/taylor_green/`). It converts "does the solution blow up?" into "does a single scale-invariant integral diverge?" The energy is supercritical and cannot bound this integral, which is the gap. The Kozono-Taniuchi BMO refinement and Besov variants (Direction 01) weaken the $L^\infty$ to a slightly larger critical norm. The viscous version of BKM holds for NS; the role of $\nu$ is to provide the parabolic smoothing absent in the Euler case (where the integral can in fact diverge, per Elgindi).
