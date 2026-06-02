# Weak solutions and regularity criteria

Prerequisites: Sobolev spaces, distributions, the Galerkin method, parabolic regularity.

A map of what is actually known: global weak solutions exist, their singular set is small, and a family of conditional criteria say "if this critical quantity is bounded, the solution is smooth." Each criterion sits at the critical scaling level, which is exactly why the supercritical energy bound cannot reach them.

## Leray-Hopf weak solutions (existence)

Leray (1934) and Hopf (1951) constructed **weak solutions** for any divergence-free $u_0 \in L^2$, global in time, satisfying the equations in the distributional sense and obeying the energy inequality

$$\frac12 \|u(t)\|_{L^2}^2 + \nu \int_0^t \|\nabla u\|_{L^2}^2\, ds \le \frac12 \|u_0\|_{L^2}^2.$$

A Leray-Hopf solution lies in $L^\infty_t L^2_x \cap L^2_t \dot H^1_x$. Existence is settled. What is open in 3D:

- **Uniqueness**: not known. Leray-Hopf solutions might not be unique.
- **Regularity**: not known to be smooth. They might develop singularities.

In two dimensions the Leray-Hopf solution is unique and smooth (the enstrophy bound). The 3D gap is the subject of the whole problem.

## Caffarelli-Kohn-Nirenberg (partial regularity)

CKN (1982), building on Scheffer, proved a partial regularity theorem for **suitable** weak solutions (those satisfying a local energy inequality): the **singular set** $S$ (the set of spacetime points where $u$ is not locally bounded) has **one-dimensional parabolic Hausdorff measure zero**, $\mathcal{P}^1(S) = 0$.

This is the strongest unconditional regularity result known. It does not exclude singularities; it bounds how big the singular set can be. In particular a singularity cannot occur along a curve in spacetime, but a single point in time at a single point in space is not excluded. The scaling reason CKN reaches exactly $\mathcal{P}^1$ is again the supercriticality: the local energy is supercritical, and the dimension count of the bound reflects exactly the $1/2$ deficit.

## The conditional regularity criteria

These are statements of the form: a Leray-Hopf solution that is a priori known to control a certain critical quantity on $[0, T]$ is in fact smooth on $[0, T]$. They all sit at critical scaling, which is what makes them sharp and what makes them unreachable from the energy alone.

### Prodi-Serrin-Ladyzhenskaya (PSL)

If $u \in L^p_t L^q_x$ with

$$\frac{2}{p} + \frac{3}{q} \le 1, \qquad 3 < q \le \infty,$$

then $u$ is smooth. The borderline $2/p + 3/q = 1$ is scale invariant (critical). Compare with what the energy gives, $2/p + 3/q = 3/2$: the deficit of $1/2$ is the supercriticality, made concrete in the same exponent arithmetic.

### Escauriaza-Seregin-Sverak (ESS), the $L^3$ endpoint

The PSL family excludes the endpoint $q = 3$, $p = \infty$. ESS (2003) proved exactly this borderline case: if $u \in L^\infty_t L^3_x$ on $[0, T]$ (the critical Lebesgue norm stays bounded), then $u$ is smooth on $[0, T]$. This is the deepest of the critical continuation criteria. Its proof uses backward uniqueness and unique continuation for the heat operator, genuinely new machinery beyond energy estimates.

### Beale-Kato-Majda (BKM)

Originally for Euler, central for Navier-Stokes: a smooth solution on $[0, T)$ can be continued past $T$ if and only if

$$\int_0^T \|\omega(t)\|_{L^\infty}\, dt < \infty.$$

The integral is scale invariant (critical): the spatial sup of the vorticity scales like $\lambda^2$ and the time integral contributes $\lambda^{-2}$ (see `experiments/_shared/criticality.py`). BKM converts blow-up into the divergence of a single critical integral, which is why the Taylor-Green DNS tracks exactly that integral (`experiments/taylor_green/`).

### Geometric and anisotropic refinements

- **Constantin-Fefferman (1993)**: if the direction $\xi = \omega / |\omega|$ of the vorticity is Lipschitz in space wherever $|\omega|$ is large, the solution is regular. This replaces a magnitude bound with a coherence-of-direction condition, a scale-aware structural criterion. It is the closest thing to a critical control that uses the geometry of stretching, and the most promising target for sharpening.
- **One-component / anisotropic criteria** (Neustupa-Penel; Kukavica-Ziane; Chemin-Zhang and others): regularity can follow from controlling a single velocity component, or one component of the vorticity, or anisotropic norms, exploiting the divergence-free constraint. These probe how much of the critical norm is actually needed.

## The unifying picture

| Criterion | Controlled quantity | Scaling | Status |
|---|---|---|---|
| Energy inequality | $L^\infty_t L^2 \cap L^2_t \dot H^1$ | supercritical | holds for all time (the only one that does) |
| PSL | $L^p_t L^q_x$, $2/p+3/q\le1$ | critical | conditional |
| ESS | $L^\infty_t L^3_x$ | critical | conditional (deepest) |
| BKM | $\int\|\omega\|_\infty\,dt$ | critical | conditional (the sharp blow-up criterion) |
| Constantin-Fefferman | vorticity direction Lipschitz | scale-aware geometric | conditional |
| CKN | local energy / singular set | supercritical | unconditional (singular set $\mathcal{P}^1 = 0$) |

Every conditional criterion is at the critical level, every unconditional result is at the supercritical level, and the gap between them is the problem. A proof closes the gap by upgrading some critical quantity from "conditional" to "controlled by the data for all time," using the 3D vortex-stretching structure that 2D lacks and the viscosity that the inviscid relatives lack.
