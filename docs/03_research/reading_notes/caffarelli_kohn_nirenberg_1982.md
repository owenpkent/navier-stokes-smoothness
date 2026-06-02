# Reading notes: Caffarelli-Kohn-Nirenberg (1982)

L. Caffarelli, R. Kohn, L. Nirenberg, "Partial regularity of suitable weak solutions of the Navier-Stokes equations," Comm. Pure Appl. Math. 35 (1982).

## What it proves

For **suitable** weak solutions (Leray-Hopf solutions that additionally satisfy a local energy inequality), the singular set $S \subset \mathbb{R}^3 \times (0,\infty)$, the set of spacetime points where $u$ fails to be locally bounded, has **one-dimensional parabolic Hausdorff measure zero**:

$$\mathcal{P}^1(S) = 0.$$

In particular $S$ cannot contain a curve in spacetime, and its parabolic Hausdorff dimension is at most $1$.

## Structural content

- **Suitable weak solutions.** The key extra hypothesis beyond Leray-Hopf is the local energy inequality: for nonnegative test functions $\phi$,
$$\int |u|^2 \phi\,dx + 2\nu\int\int |\nabla u|^2 \phi \le \int\int |u|^2(\partial_t\phi + \nu\Delta\phi) + \int\int (|u|^2 + 2p)\, u\cdot\nabla\phi.$$
Such solutions exist (Scheffer; the construction respects the local inequality).
- **The $\varepsilon$-regularity theorem.** The technical heart: there is an absolute constant $\varepsilon > 0$ such that if the scaled local energy on a parabolic cylinder $Q_r$,
$$\frac{1}{r}\int\int_{Q_r}\big(|\nabla u|^2\big) \quad\text{(and companion quantities)} ,$$
is below $\varepsilon$, then $u$ is regular (Hölder continuous) on the smaller cylinder $Q_{r/2}$. Regularity is a local smallness condition on a scale-invariant local energy.
- **Covering argument.** The singular set is where the scale-invariant local energy fails to be small. A Vitali covering plus the $\varepsilon$-regularity theorem bounds its parabolic Hausdorff measure, giving $\mathcal{P}^1(S)=0$.

## Why it stops at dimension 1

The scale-invariant local energy is built from the supercritical energy quantities. The dimension count $\mathcal{P}^1$ is precisely the reflection of the $1/2$ supercriticality deficit: the parabolic scaling of the local energy puts the threshold at one parabolic dimension. To push the bound below dimension $1$ (toward an empty singular set) would require a more-than-energy, scaling-critical input, which is the open problem.

## How it bears on the spine

CKN is the best unconditional regularity result, and its stopping point is the supercriticality made geometric. The $\varepsilon$-regularity / local-energy-smallness mechanism is itself a critical-scaling statement (regularity from a scale-invariant smallness), so CKN is the unconditional shadow of the conditional critical criteria (BKM, ESS). Closing the gap from "$\mathcal{P}^1(S)=0$" to "$S=\emptyset$" is the same gap as everywhere else.
