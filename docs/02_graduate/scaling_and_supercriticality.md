# Scaling and supercriticality

Prerequisites: Sobolev spaces, the heat semigroup, basic harmonic analysis.

This is the structural core of the whole problem. The claim is precise: the only globally-in-time a priori bound for 3D Navier-Stokes is supercritical with respect to the scaling symmetry, and supercritical bounds cannot, by themselves, close a regularity statement.

## The scaling symmetry

If $(u, p)$ solves Navier-Stokes on $\mathbb{R}^3$, so does

$$u_\lambda(x, t) = \lambda\, u(\lambda x, \lambda^2 t), \qquad p_\lambda(x, t) = \lambda^2\, p(\lambda x, \lambda^2 t), \qquad \lambda > 0.$$

The initial data rescales as $u_{0,\lambda}(x) = \lambda u_0(\lambda x)$. A function space $X$ for the initial data is called **critical** if its norm is invariant under this rescaling, $\|u_{0,\lambda}\|_X = \|u_0\|_X$ for all $\lambda$. It is **subcritical** if the norm of $u_{0,\lambda}$ grows as $\lambda \to \infty$ (zooming into small scales), and **supercritical** if it decays.

The heuristic, made rigorous in many cases: in a subcritical or critical space, small data gives global smooth solutions, because the rescaling does not let small scales escape the norm's control. In a supercritical space the norm sees nothing at small scales, so it cannot prevent concentration.

## Computing the exponents

For the spatial velocity rescaling $v_\lambda(x) = \lambda\, u(\lambda x)$ (fixed time), a change of variables gives the homogeneous norms:

$$\|v_\lambda\|_{\dot H^s} = \lambda^{\,1 + s - d/2}\, \|u\|_{\dot H^s}, \qquad \|v_\lambda\|_{L^q} = \lambda^{\,1 - d/q}\, \|u\|_{L^q}.$$

In dimension $d = 3$:

| Space | Exponent | Class | Significance |
|---|---|---|---|
| $L^2$ (energy) | $1 - 3/2 = -1/2$ | supercritical | the only all-time a priori bound |
| $\dot H^{1/2}$ | $1 + 1/2 - 3/2 = 0$ | critical | Fujita-Kato (1964) small-data space |
| $L^3$ | $1 - 3/3 = 0$ | critical | ESS endpoint (2003) |
| $\mathrm{BMO}^{-1}$ | $0$ | critical | Koch-Tataru (2001), the largest known small-data space |
| $\dot H^1$ (enstrophy) | $1 + 1 - 3/2 = +1/2$ | subcritical | bounded for all time in 2D, not in 3D |

The chain of critical spaces is $\dot H^{1/2} \hookrightarrow L^3 \hookrightarrow \mathrm{BMO}^{-1}$, each scale invariant, each progressively larger. Small data in any of them gives a global smooth solution. The open problem is **large** data. These exponents are exactly what `experiments/_shared/criticality.py` computes; the table is reproduced by `experiments/scaling_criticality/criticality_table.py`.

## Why the energy is supercritical, and why that is the whole problem

The energy identity gives, for all time,

$$\frac12 \|u(t)\|_{L^2}^2 + \nu \int_0^t \|\nabla u\|_{L^2}^2\, ds \le \frac12 \|u_0\|_{L^2}^2.$$

So we control $u \in L^\infty_t L^2_x \cap L^2_t \dot H^1_x$. The Ladyzhenskaya-Prodi-Serrin interpolation between these gives $u \in L^p_t L^q_x$ with $2/p + 3/q = 3/2$ in 3D. Compare this to the regularity threshold $2/p + 3/q = 1$ (see [regularity criteria](regularity_criteria.md)): the energy gives $3/2$, the threshold needs $1$. The deficit is exactly $1/2$, which is the supercriticality. In two dimensions the same interpolation gives $2/p + 2/q = 1$, which is precisely the 2D regularity threshold: the energy is **critical** in 2D, and that is the analytic reason 2D is solved.

So the supercriticality gap is a deficit of $1/2$ in a scaling exponent, present in 3D, absent in 2D. A proof of 3D regularity must make up that $1/2$ with a genuinely new, scaling-critical (or subcritical) a priori bound. Decades of work have not produced one.

## What supercriticality rules out

The supercriticality is a sharp filter, the analog of a saturated ceiling. It tells us what cannot work, which is how the search narrows:

1. **No purely energy-based argument can close regularity.** Anything controlled by $L^\infty_t L^2 \cap L^2_t \dot H^1$ alone is supercritical. The criticality bookkeeper (`experiments/_shared/criticality.py`) audits any proposed estimate and fires INSUFFICIENT_BY_ITSELF on supercritical controlling norms.
2. **No argument that ignores vortex stretching can be the real one.** The same energy chain in 2D is critical and closes; the difference is the stretching term $(\omega \cdot \nabla) u$. A 3D argument that does not engage it would apply in 2D, where it is unnecessary.
3. **No argument that uses only the energy identity and the scaling can work.** Tao (2016) constructed finite-time blow-up for an averaged Navier-Stokes that preserves both. So the missing control must use the exact structure of the nonlinearity (the precise transport-and-pressure coupling), not its soft consequences.

## Where critical control might come from

The compass points at genuinely critical structure. The most-studied candidates:

- **Critical norms as continuation criteria.** ESS (2003) proves that if $\|u(t)\|_{L^3}$ stays bounded then the solution is smooth. This converts regularity into controlling a critical norm. The control is what is missing.
- **Geometric / direction-of-vorticity conditions.** Constantin-Fefferman (1993) show that if the vorticity direction stays Lipschitz where the vorticity is large, the flow is regular. This is a scale-aware structural condition, the closest thing to a critical control that uses the geometry of stretching. It is the most promising survey target (see the research directions).
- **Anisotropic and one-component criteria.** Regularity can follow from controlling fewer components or fewer derivatives than naively expected, exploiting the divergence-free structure. These probe how much of the full critical norm is actually needed.

None of these is yet an unconditional bound. They map the boundary of the gap with increasing precision. Closing it is the open problem.
