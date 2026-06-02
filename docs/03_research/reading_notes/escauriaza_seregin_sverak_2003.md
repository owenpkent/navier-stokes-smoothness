# Reading notes: Escauriaza-Seregin-Sverak (2003)

L. Escauriaza, G. Seregin, V. Sverak, "L_{3,infty}-solutions of Navier-Stokes equations and backward uniqueness," Russian Math. Surveys 58 (2003).

## What it proves

The endpoint critical regularity criterion: if a Leray-Hopf solution satisfies

$$u \in L^\infty\big([0,T]; L^3(\mathbb{R}^3)\big),$$

i.e. the critical Lebesgue norm $\|u(t)\|_{L^3}$ stays bounded on $[0,T]$, then $u$ is smooth on $[0,T]$. Equivalently, at a first blow-up time the $L^3$ norm must become unbounded: $\limsup_{t\to T}\|u(t)\|_{L^3} = \infty$.

This is the borderline case $q=3$, $p=\infty$ excluded by the Prodi-Serrin-Ladyzhenskaya family ($2/p+3/q\le1$ requires $q>3$ in the original statement). It is the deepest of the critical continuation criteria.

## Structural content

- **Why the endpoint is hard.** For $q>3$ the criterion follows from a perturbative / bootstrap argument because the controlled norm is subcritical relative to the scaling of the iteration. At $q=3$ the norm is exactly critical and scale invariant, so there is no slack and the perturbative argument fails. A genuinely new idea is needed.
- **Backward uniqueness and unique continuation.** The new idea: rescale around a hypothetical singularity to produce an ancient (defined for all negative time) bounded "mild bounded" solution; show by **backward uniqueness** for the heat operator with a potential (a Carleman-estimate argument) and **unique continuation** that this ancient solution must vanish, contradicting the singularity. The Carleman estimates are the technical core.
- **Critical scaling is essential.** The blow-up rescaling exactly uses the scale invariance of $L^3$: the rescaled solutions stay bounded in $L^3$ precisely because $L^3$ is critical, which is what produces the ancient solution.

## How it bears on the spine

ESS is the sharpest statement of "regularity is a critical-norm statement": control the critical $L^3$ norm and you are done. The criticality bookkeeper confirms $L^3$ has scaling exponent $0$. The energy gives $L^\infty_t L^2$, supercritical, which does not embed into $L^\infty_t L^3$, so ESS is unreachable from the energy. Tao (2019) made ESS quantitative (a singularity forces $\|u\|_{L^3}$ to grow at least triple-logarithmically), which is the Direction 01 lead: a self-improving quantitative critical estimate. The backward-uniqueness machinery is genuinely beyond energy methods, which is exactly the kind of "new input" the supercriticality demands.
