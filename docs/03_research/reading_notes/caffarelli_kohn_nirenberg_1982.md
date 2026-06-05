# Reading notes: Caffarelli-Kohn-Nirenberg (1982)

L. Caffarelli, R. Kohn, L. Nirenberg, "Partial regularity of suitable weak solutions of the Navier-Stokes equations," *Communications on Pure and Applied Mathematics* **35** (1982), 771-831.

> CKN is the best unconditional regularity theorem known for the 3D incompressible Navier-Stokes equations. It does not prove smoothness, and forty years later nothing unconditional has surpassed it. What it proves is that the singular set $S$ (the set of spacetime points where the velocity fails to be locally bounded) is small: it has parabolic one-dimensional Hausdorff measure zero, $\mathcal{P}^1(S)=0$, so in particular it can contain no spacetime curve and has parabolic Hausdorff dimension at most $1$. This is Architecture 1 (energy methods and weak solutions) pushed to its current frontier. Its engine, an $\varepsilon$-regularity theorem stating that smallness of a scale-invariant local energy on a parabolic cylinder forces local boundedness, is a *critical-scaling* statement, and the place where it stops, dimension $1$, is exactly the geometric image of the supercriticality gap (control B). CKN is the unconditional shadow of the conditional critical criteria (BKM, ESS): the same gap that keeps energy from controlling the critical norm keeps the singular set from being proven empty.

## Statement

Fix the incompressible Navier-Stokes system on an open set in $\mathbb{R}^3 \times \mathbb{R}$,
$$
\partial_t u + (u\cdot\nabla)u = -\nabla p + \nu\,\Delta u, \qquad \nabla\cdot u = 0,
$$
with viscosity $\nu>0$ (CKN normalize $\nu=1$). Write the parabolic cylinder $Q_r(z_0) = B_r(x_0)\times(t_0-r^2,\,t_0)$ centered at $z_0=(x_0,t_0)$; the use of $r^2$ in the time direction is the parabolic scaling that matches $u_\lambda(x,t)=\lambda\,u(\lambda x,\lambda^2 t)$.

**Suitable weak solutions.** A pair $(u,p)$ is a *suitable weak solution* on a spacetime domain if:

1. $u \in L^\infty_t L^2_x \cap L^2_t \dot H^1_x$ and $p \in L^{3/2}_{\mathrm{loc}}$ (CKN use $p\in L^{5/4}$ in the original; the now-standard hypothesis is $p\in L^{3/2}_{\mathrm{loc}}$, which matches the scaling of $|u|^3$);
2. $(u,p)$ solves Navier-Stokes in the sense of distributions;
3. $(u,p)$ satisfies the **local energy inequality**: for every nonnegative $\phi \in C_c^\infty$,
$$
\int |u(t)|^2\,\phi\,dx \;+\; 2\nu\!\int\!\!\int |\nabla u|^2\,\phi
\;\le\;
\int\!\!\int |u|^2\,(\partial_t\phi + \nu\,\Delta\phi)
\;+\;
\int\!\!\int \big(|u|^2 + 2p\big)\,(u\cdot\nabla\phi).
\tag{LEI}
$$

Condition (3) is the load-bearing extra hypothesis. A generic Leray-Hopf weak solution satisfies only the *global, integrated* energy inequality (test function $\phi\equiv 1$). (LEI) is the same inequality run against a *localized* test function, and the price of localization is the appearance of the pressure $p$ through the work term $\int\int (|u|^2+2p)\,(u\cdot\nabla\phi)$. The pressure is not optional here: localizing the energy balance forces the nonlocal pressure into the estimate, and controlling it (via the Calderon-Zygmund bound $p = (-\Delta)^{-1}\partial_i\partial_j(u_i u_j)$, so $\|p\|_{L^{3/2}} \lesssim \|u\|_{L^3}^2$) is half the work of the theorem.

**Existence of suitable weak solutions.** CKN prove that for any finite-energy divergence-free $u_0$ there exists at least one suitable weak solution. The construction is a retarded-mollification (Scheffer-type) regularization: regularize the transport velocity, solve, and pass to the limit while keeping (LEI) as an inequality (weak limits can only lose local energy, never create it). So suitability is not an extra assumption one must verify case by case; it is achievable, and the partial-regularity conclusion therefore applies to *some* solution for every datum. It is **not** known that *every* Leray-Hopf weak solution is suitable, which is one honest gap (see "What it does not give").

**Main theorem (partial regularity).** Let $(u,p)$ be a suitable weak solution and let $S$ be its singular set (the complement of the set of points near which $u$ is essentially bounded, equivalently Holder continuous). Then
$$
\boxed{\;\mathcal{P}^1(S) = 0\;}
$$
where $\mathcal{P}^1$ is the one-dimensional Hausdorff measure built from parabolic cylinders (the gauge $r\mapsto r$ over coverings by $Q_r$). Consequences:

- $\dim_{\mathcal{P}}(S) \le 1$ (parabolic Hausdorff dimension at most $1$);
- $S$ contains no spacetime curve of positive $\mathcal{P}^1$ measure, in particular no segment $\{x_0\}\times I$ of positive-length blow-up times;
- for a.e. fixed time $t$, the time-slice $S\cap(\mathbb{R}^3\times\{t\})$ has spatial Hausdorff dimension $\le 1$ as well, and the set of *singular times* has $\tfrac12$-dimensional Hausdorff measure zero (refining Leray's count of singular times).

## Method / structure

The proof has two halves: an $\varepsilon$-regularity theorem (the analytic engine) and a covering/dimension argument (the geometric harvest).

**The two $\varepsilon$-regularity theorems.** CKN prove regularity from smallness of a *scale-invariant* local quantity. Two forms appear, and both are dimensionless under $u_\lambda(x,t)=\lambda\,u(\lambda x,\lambda^2 t)$:

- **(First / "easy" criterion, gives $\dim \le 5/3$ via Scheffer-type bound.)** There is an absolute $\varepsilon_1>0$ such that if
$$
\limsup_{r\to 0}\ \frac{1}{r}\int\!\!\int_{Q_r(z_0)} |\nabla u|^2\,dx\,dt \;<\; \varepsilon_1,
$$
then $z_0$ is a regular point. The functional $r^{-1}\int_{Q_r}|\nabla u|^2$ is exactly scale invariant: $\int|\nabla u|^2$ carries dimension $\lambda^{1}$ (one spatial dimension of deficit) and the parabolic cylinder volume carries $\lambda^{-5}$, against the $\lambda^{-1}$ from the explicit $1/r$, netting exponent $0$.

- **(Second / "hard" criterion, gives the sharp $\mathcal{P}^1(S)=0$.)** There is an absolute $\varepsilon_2>0$ such that if
$$
\frac{1}{r^2}\int\!\!\int_{Q_r(z_0)} \big(|u|^3 + |p|^{3/2}\big)\,dx\,dt \;<\; \varepsilon_2
\qquad\text{for some } r,
$$
then $u$ is bounded (Holder continuous) on $Q_{r/2}(z_0)$, with a quantitative bound on $\|u\|_{L^\infty(Q_{r/2})}$. Equivalently, in the cleanest modern packaging (Lin 1998, Ladyzhenskaya-Seregin), there is $\varepsilon_*>0$ so that
$$
\frac{1}{r^2}\int\!\!\int_{Q_r(z_0)}|u|^3\,dx\,dt < \varepsilon_* \;\Longrightarrow\; z_0 \text{ regular}.
$$
The functional $r^{-2}\int_{Q_r}|u|^3$ is scale invariant: $|u|^3$ scales as $\lambda^3$, the cylinder as $\lambda^{-5}$, and $r^{-2}$ as $\lambda^{2}$, summing to $0$. The pressure term $|p|^{3/2}$ shares this scaling because $p$ scales as $\lambda^2$.

The mechanism inside the engine is a **decay / iteration on scales**. One defines dimensionless local quantities (a local energy $A(r)$, a local dissipation, a local $L^3$ mass $\int_{Q_r}|u|^3 / r^2$, a local pressure functional), feeds (LEI) the test function $\phi$ concentrated on $Q_r$, and shows that if the relevant functional is small at one scale then it *decays geometrically* as $r\to 0$. Smallness propagating down all scales is exactly local boundedness. The pressure enters the iteration through the work term in (LEI) and is controlled by the Calderon-Zygmund estimate plus a harmonic decomposition $p = p_{\mathrm{local}} + p_{\mathrm{harmonic}}$ that separates the locally-generated pressure from the far-field part; the harmonic part is smooth and decays, the local part is bounded by local $\int|u|^3$. This is why no $\varepsilon$-regularity result for genuine Navier-Stokes can drop the pressure entirely (pressure-free one-scale variants exist but require additional structure, e.g. Guevara-Phuc, Wang-Wu).

**Where 3D structure enters, and where it does not.** The vortex-stretching term $\omega\cdot\nabla u$ never appears explicitly. CKN do not exploit the precise 3D nonlinear production of vorticity. The $\varepsilon$-regularity engine is dimension-robust: the same scheme runs in any dimension, and the threshold dimension of the singular set is set purely by the parabolic scaling arithmetic, not by 3D vortex dynamics. This is important for the controls audit below.

**The covering argument.** Singular points are, by the contrapositive of the second criterion, exactly the points where $\limsup_{r\to 0} r^{-2}\int_{Q_r}|u|^3 \ge \varepsilon_*$ (and likewise for the $|\nabla u|^2$ form). On such a point the local energy carries a fixed quantum $\varepsilon_*$. Because $u\in L^3_{\mathrm{loc}}$ (interpolating $L^\infty_t L^2_x \cap L^2_t \dot H^1_x$ gives $u\in L^{10/3}_{t,x}\subset L^3_{\mathrm{loc}}$ in spacetime) and $\nabla u \in L^2_{t,x}$, the total energy is finite, so the spacetime measure $|\nabla u|^2\,dx\,dt$ can charge only a small set with the fixed quantum. A Vitali covering of $S$ by cylinders on which the quantum lives, plus the absolute-continuity of $\int|\nabla u|^2$, bounds the parabolic $1$-measure of $S$. The sharp statement $\mathcal{P}^1(S)=0$ (not merely $\dim\le 1$) comes from the $|\nabla u|^2$ form because $\int|\nabla u|^2$ vanishes on sets of small measure (absolute continuity of the integral), which upgrades "dimension $\le 1$" to "$1$-measure $= 0$".

## Criticality placement

Run the relevant quantities through the criticality bookkeeper `experiments/_shared/criticality.py`, using the convention there that exponent $a$ in $\|u_\lambda\|_X = \lambda^a\|u\|_X$ classifies as $a>0$ subcritical, $a=0$ critical, $a<0$ supercritical.

- **The $\varepsilon$-regularity functionals are exactly critical.** Both $r^{-1}\int_{Q_r}|\nabla u|^2$ and $r^{-2}\int_{Q_r}|u|^3$ have scaling exponent $0$. CKN regularity is therefore an honest *critical-scaling* statement: regularity follows from smallness of a scale-invariant local energy, the local analog of the global critical criteria (the $L^3$ of ESS, the $\dot H^{1/2}$ of Fujita-Kato). This is the single most important structural fact about CKN for this project: the engine lives at the critical level, which is why it produces real regularity at all. Energy-level estimates (control B) cannot do this.

- **The a priori inputs are supercritical, and that is what caps the dimension at $1$.** The only globally available bounds are the Leray-Hopf energy quantities: $u\in L^\infty_t L^2_x$, with `lebesgue_exponent(2,3)` $= 1 - 3/2 = -1/2$ (supercritical), and $\nabla u\in L^2_{t,x}$, the parabolic energy. The covering argument can only spend what the energy provides. The energy provides exactly one parabolic dimension of integrability above the critical threshold ($\int|\nabla u|^2$ is one spatial derivative, i.e. a half-derivative supercritical deficit, expressed parabolically as one cylinder-dimension), so the covering caps $S$ at parabolic dimension $1$ and no lower. **The number $1$ is the supercriticality deficit made geometric.** To push the singular set below dimension $1$ (toward $S=\emptyset$) one would need a *more-than-energy*, scaling-critical global input, which is precisely the open problem and precisely what `audit_estimate` flags when handed the energy norm: `INSUFFICIENT_BY_ITSELF`.

- **Cross-check against the conditional criteria.** ESS controls the *global* critical norm $\|u(t)\|_{L^3}$ (`lebesgue_exponent(3,3)` $= 0$) and gets full regularity. CKN controls a *local* critical functional and gets local regularity off a thin set. The two are the same idea at two scopes; the difference is that ESS *assumes* the global critical bound while CKN *derives* local smallness from the supercritical energy, paying for the derivation with a nonempty (but small) singular set.

## Against the three controls

**(A) 2D control (must stay smooth).** CKN does not use vortex stretching, so as a method it would "run" in 2D. But it does not *predict 2D blow-up*: in 2D the global enstrophy bound makes the relevant local functionals small everywhere automatically, so the $\varepsilon$-regularity engine returns $S=\emptyset$, recovering global smoothness. CKN passes control A in the weak sense that it does not falsely manufacture a 2D singularity. The honest reading is sharper and is a *coordinate, not a flaw*: because CKN is dimension-robust and blind to $\omega\cdot\nabla u$, it cannot itself be the closing argument in 3D. The thing that distinguishes 3D from 2D (vortex stretching) is exactly the thing CKN does not engage, so CKN cannot see why 3D would be worse than 2D, and therefore cannot prove 3D is as good. Any closing argument must add the 3D-specific input CKN omits. This is a clean instance of control A used as a compass: it tells us where the missing structure must be.

**(B) Supercriticality (the ceiling).** CKN both *uses* and is *capped by* control B, and this is its defining relationship to the project's spine. The engine is critical (good); the inputs are supercritical (the cap). The result is the maximal regularity extractable from supercritical energy alone: a singular set of parabolic dimension $\le 1$, measure zero, but not empty. CKN is the exact unconditional witness that "energy gets you to dimension $1$ and stops." The gap from $\mathcal{P}^1(S)=0$ to $S=\emptyset$ is the supercriticality gap, the same gap as everywhere else in the program (Direction 03).

**(C) Viscosity / Burgers control.** CKN is *not* blind to viscosity. The dissipation $\nu\int|\nabla u|^2$ is the coercive term on the left of (LEI) and is what is being spent in the covering, and the parabolic cylinder geometry $B_r\times(t_0-r^2,t_0)$ is the heat scaling. Remove viscosity (Euler) and (LEI) loses its dissipative left side, the engine has nothing to spend, and the conclusion collapses: there is no Euler analog of CKN partial regularity, consistent with the modern Euler finite-time singularity evidence (Elgindi 2021; Chen-Hou). CKN passes control C: it genuinely needs $\nu>0$ and the precise parabolic (heat) structure.

Net: CKN passes all three controls in the sense of not violating any, and it is *informative against* control B in the strongest way (it is the unconditional ceiling). Its limitation against control A (no $\omega\cdot\nabla u$) is the directional reading of what a closing argument must add.

## What it gives / what it does not give

**What it gives.**

- The best unconditional regularity statement to date: $\mathcal{P}^1(S)=0$, hence $\dim_{\mathcal{P}}S\le 1$, for a class of solutions that *provably exists* for every finite-energy datum.
- A reusable analytic tool, the $\varepsilon$-regularity theorem, which is now the standard local-regularity device throughout fluid PDE and beyond (harmonic maps, mean curvature flow, Yang-Mills all have CKN-style $\varepsilon$-regularity).
- A sharp refinement of Leray's count of singular times (the set of singular times has $\tfrac12$-dimensional measure zero), and the structural statement that the velocity cannot blow up along a spacetime curve.

**What it does not give (the gap to closing regularity).**

- **It does not prove $S=\emptyset$.** Dimension $\le 1$ is *enormously* far from empty in the only sense that matters: a single point could still be singular, and one singular point is a singularity. The theorem rules out *fat* singular sets, not singularities.
- **The bound is conditional on suitability.** It applies to suitable weak solutions. Every datum has one, but it is open whether *every* Leray-Hopf solution is suitable, so CKN does not directly bound the singular set of an arbitrary weak solution.
- **The bound is at the energy ceiling.** As placed above, $1$ is the supercriticality deficit. CKN cannot be iterated or bootstrapped past dimension $1$ using only energy; the improvement to $S=\emptyset$ requires a new global critical input that the theorem does not and cannot supply from its hypotheses. This is the project's central message: CKN marks exactly where energy methods stop and where genuinely critical control must begin.
- **It is silent on uniqueness.** Partial regularity says nothing about whether the suitable solution is the only one. Architecture 5 (convex integration; Buckmaster-Vicol 2019, Albritton-Brue-Colombo 2022) lives below the suitability/energy class and is not constrained by CKN; the recent wild-solutions constructions even build solutions whose *time* singular set has Hausdorff dimension strictly below $1$, sitting just under the CKN-Scheffer ceiling rather than violating it.

The distance from CKN to a Clay-level theorem is therefore the whole problem, repackaged: close the gap between a thin singular set and an empty one, which is the gap between supercritical energy control and critical control.

## Lineage and sharpest known form

**Builds on.**

- **V. Scheffer** (1976-1980): the precursor partial-regularity program. Scheffer introduced suitable weak solutions and the local energy inequality and obtained the first partial-regularity bounds (Hausdorff dimension of the singular set $\le 5/3$ in spacetime, and related slice bounds). CKN sharpened Scheffer's dimension count to the optimal-from-energy value $\mathcal{P}^1(S)=0$ and made the $\varepsilon$-regularity theorem clean.
- **J. Leray** (1934): the count of singular *times* (the $\tfrac12$-dimensional set of singular times) is the seed; CKN's spacetime statement contains and refines it.
- The **Calderon-Zygmund** pressure estimate and parabolic regularity theory are the analytic substrate.

**Built on it.**

- **F.-H. Lin** (1998, CPAM): a dramatically shortened proof of the sharp $\varepsilon$-regularity theorem and $\mathcal{P}^1(S)=0$, using the single criterion $r^{-2}\int_{Q_r}|u|^3<\varepsilon_*$ and a compactness/blow-up argument. This is the version most textbooks teach.
- **Ladyzhenskaya-Seregin** (1999) and **Seregin**: a streamlined and generalized framework, sharper $\varepsilon$-regularity criteria, and the boundary-regularity theory.
- **Choe-Lewis**, **Robinson-Sadowski**, **Kukavica-Pei**: Minkowski / box-counting dimension refinements, which are strictly stronger than Hausdorff bounds.
- The result is the template for $\varepsilon$-regularity across geometric PDE.

**Sharpest known form (through 2025).** The Hausdorff statement $\mathcal{P}^1(S)=0$ has *not* been improved at the Hausdorff level (improving it would essentially mean closing the gap). The active frontier is the **box-counting (upper Minkowski) dimension** of the potential singular set, which is a finer, harder quantity:

- Scheffer's spacetime Hausdorff bound was $5/3$; CKN's is the sharp $\le 1$ (measure zero).
- For the *box-counting* dimension, a chain of refinements: **Robinson-Sadowski / Kukavica-Pei** $5/3$, **Koh-Yang** $95/63 \approx 1.508$, **Wang-Yang** (interior) $7/6 \approx 1.167$, **Wang-Wu** $135/104 \approx 1.298$, and further improvements **Ren-Wang-Wu** from $360/277$ to $975/758 \approx 1.286$ (verify: the exact current record and its authorship are in flux across 2018-2025 preprints). The qualitative point is stable: box dimension is provably $<5/3$ and creeping toward $1$, but no unconditional argument reaches *below* $1$, consistent with the energy ceiling.
- **Pressure-free / one-scale $\varepsilon$-regularity** (Wang-Wu, Guevara-Phuc, Chae-Wolf): criteria that avoid the pressure term or use a single scale, simplifying applications, at the cost of slightly different smallness functionals.
- **Sharpness from below.** Scheffer-type constructions of solutions to the Navier-Stokes *inequality* (not the equation) show the CKN bound cannot be improved by these methods alone: there exist suitable-inequality solutions whose singular set has Hausdorff dimension arbitrarily close to $1$. The **Buckmaster-Colombo-Vicol** (2021-2023) wild-solution constructions produce genuine weak solutions whose *time* singular set has Hausdorff dimension strictly less than $1$, populating the region just under the CKN ceiling and underlining that dimension $1$ is the right barrier for energy-based methods.

For the comprehensive modern account see W. S. Ozanski, *The Partial Regularity Theory of Caffarelli, Kohn, and Nirenberg and its Sharpness* (Birkhauser, 2019).

## References

- L. Caffarelli, R. Kohn, L. Nirenberg, "Partial regularity of suitable weak solutions of the Navier-Stokes equations," *Comm. Pure Appl. Math.* **35** (1982), 771-831.
- V. Scheffer, "Partial regularity of solutions to the Navier-Stokes equations," *Pacific J. Math.* **66** (1976), 535-552; "Hausdorff measure and the Navier-Stokes equations," *Comm. Math. Phys.* **55** (1977), 97-112.
- J. Leray, "Sur le mouvement d'un liquide visqueux emplissant l'espace," *Acta Math.* **63** (1934), 193-248.
- F.-H. Lin, "A new proof of the Caffarelli-Kohn-Nirenberg theorem," *Comm. Pure Appl. Math.* **51** (1998), 241-257.
- O. A. Ladyzhenskaya, G. A. Seregin, "On partial regularity of suitable weak solutions to the three-dimensional Navier-Stokes equations," *J. Math. Fluid Mech.* **1** (1999), 356-387.
- J. C. Robinson, W. Sadowski, "Decay of weak solutions and the singular set of the three-dimensional Navier-Stokes equations," *Nonlinearity* **20** (2007); and Kukavica-Pei box-dimension work.
- Y. Wang, G. Wu; J. Ren, Y. Wang, G. Wu; H.-K. Koh, M. Yang: box-counting dimension refinements of the singular set (2016-2024 arXiv chain; exact records cited as "(verify)" above).
- T. Buckmaster, M. Colombo, V. Vicol, "Wild solutions of the Navier-Stokes equations whose singular sets in time have Hausdorff dimension strictly less than 1," *J. Eur. Math. Soc.* (2023).
- W. S. Ozanski, *The Partial Regularity Theory of Caffarelli, Kohn, and Nirenberg and its Sharpness*, Birkhauser Advances in Mathematical Fluid Mechanics (2019).
- L. Escauriaza, G. Seregin, V. Sverak, "$L_{3,\infty}$-solutions of Navier-Stokes equations and backward uniqueness," *Russian Math. Surveys* **58** (2003), 211-250.

## Cross-links

- Direction 03, the supercriticality gap (the gap from $\mathcal{P}^1(S)=0$ to $S=\emptyset$ is exactly this): [`../research_directions/03_supercriticality_gap.md`](../research_directions/03_supercriticality_gap.md).
- Direction 01, critical continuation criteria (the conditional siblings BKM, ESS that CKN is the unconditional shadow of): [`../research_directions/01_critical_continuation_criteria.md`](../research_directions/01_critical_continuation_criteria.md).
- Direction 02, vorticity geometry (where the $\omega\cdot\nabla u$ structure CKN omits would have to enter): [`../research_directions/02_vorticity_geometry.md`](../research_directions/02_vorticity_geometry.md).
- Direction 05, the convex-integration boundary (wild solutions sitting just under the CKN ceiling): [`../research_directions/05_convex_integration_boundary.md`](../research_directions/05_convex_integration_boundary.md).
- Sibling note: Leray 1934, the weak-solution class and singular-time count CKN refines: [`leray_1934.md`](leray_1934.md).
- Sibling note: Escauriaza-Seregin-Sverak 2003, the global critical-norm criterion CKN localizes: [`escauriaza_seregin_sverak_2003.md`](escauriaza_seregin_sverak_2003.md).
- Criticality bookkeeper (confirms the $\varepsilon$-regularity functionals are exponent $0$ and the energy is $-1/2$): [`../../../experiments/_shared/criticality.py`](../../../experiments/_shared/criticality.py).

## What this enables / what remains open

**Enables.** CKN gives BUILDER a precise, scale-invariant local target: any candidate regularity estimate should reduce, locally, to forcing a critical functional like $r^{-2}\int_{Q_r}|u|^3$ below its absolute threshold, which is the local form of the closing condition. It gives ADVERSARY the exact ceiling to test against: any proposed unconditional improvement that claims $\dim_{\mathcal{P}}S < 1$ from energy-type inputs alone is, by the supercriticality bookkeeping, suspect and should be checked for a hidden critical input. It gives SYNTHESIZER the canonical statement that "energy gets you to dimension $1$ and no further," anchoring the supercriticality narrative with a concrete unconditional theorem rather than a heuristic.

**Remains open.** (i) Is every Leray-Hopf weak solution suitable? (ii) Can the box-counting dimension be pushed below $1$, or is $1$ sharp for box dimension too? (iii) The headline: is $S=\emptyset$? Closing (iii) is the Clay problem and, as placed here, requires exactly the genuinely-critical, $\omega\cdot\nabla u$-engaging global input that CKN, living on supercritical energy and blind to vortex stretching, structurally cannot provide. CKN is the most honest map of where that input must take over.
