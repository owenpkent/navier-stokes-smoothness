# Reading notes: Leray (1934)

Jean Leray, "Sur le mouvement d'un liquide visqueux emplissant l'espace," *Acta Mathematica* **63** (1934), 193-248.

> This is the foundational paper of the entire mathematical theory. Leray constructs global-in-time weak solutions ("solutions turbulentes") of the 3D incompressible Navier-Stokes equations for arbitrary finite-energy divergence-free data, and in doing so fixes the class in which the Clay problem is posed, the only coercive all-time a priori bound (the energy inequality), and the precise sense in which that bound fails to control small scales. It belongs to **Architecture 1** (energy methods and weak solutions). Its primary tie to the project's structural controls is **control (B), supercriticality**: the energy is the single global-in-time bound Leray produces, and it is supercritical under the Navier-Stokes scaling. Everything downstream in the regularity problem is the attempt to upgrade a Leray solution to a smooth one, and the obstruction is already legible in this paper: the energy does not see the scales where a singularity would form. The paper also seeds two of the deepest later threads (partial regularity, via the set of singular times, and the self-similar blow-up program, via Leray's own ansatz).

Notational convention used below: $\nu>0$ is the kinematic viscosity, $u:\mathbb{R}^3\times[0,\infty)\to\mathbb{R}^3$ the velocity, $p$ the pressure, $\omega=\nabla\times u$ the vorticity. The equations are
$$\partial_t u + (u\cdot\nabla)u = -\nabla p + \nu\,\Delta u,\qquad \nabla\cdot u = 0,\qquad u(\cdot,0)=u_0.$$
Leray worked on the whole space $\mathbb{R}^3$ ("emplissant l'espace"); Hopf (1951) carried the construction to bounded domains, and the modern class is named Leray-Hopf.

---

## Statement

Leray proves several distinct results in one paper. We separate them because they sit at different places on the criticality scale and feed different research directions.

### 1. Local existence and uniqueness of strong solutions

For divergence-free $u_0$ regular enough (Leray's hypotheses are essentially $u_0\in L^2\cap L^p$ for some $p\in(3,\infty]$, or $u_0\in H^1$ in modern language), there is a time $T_*>0$ and a unique strong solution on $[0,T_*)$ that is smooth for $t>0$. The local existence time admits a lower bound of the shape
$$T_* \ \gtrsim\ \frac{\nu^{?}}{\|u_0\|_{?}^{?}}$$
controlled by a subcritical norm of the data (the precise dependence is on $\|u_0\|_{L^p}$, $p>3$, which is a subcritical quantity; see Criticality placement). If the maximal existence time $T^*$ is finite, Leray proves a **lower bound on the blow-up rate**: for a singularity at $T^*$,
$$\|\nabla u(t)\|_{L^2} \ \gtrsim\ (T^*-t)^{-1/4},\qquad \|u(t)\|_{L^p} \ \gtrsim\ (T^*-t)^{-\frac{1}{2}\left(1-\frac{3}{p}\right)}\quad (p>3).$$
These lower bounds are the seed of every later "the critical norm must blow up" statement (Architecture 2, and Escauriaza-Seregin-Sverak at the endpoint $p=3$).

### 2. Global existence of weak ("turbulent") solutions

For *any* divergence-free $u_0\in L^2(\mathbb{R}^3)$, there exists a global weak solution $u$ on $[0,\infty)$ with

- $u\in L^\infty\big([0,\infty);L^2(\mathbb{R}^3)\big)\ \cap\ L^2\big([0,\infty);\dot H^1(\mathbb{R}^3)\big)$,
- $\nabla\cdot u=0$ in the distributional sense,
- the momentum equation satisfied in the integrated / distributional sense against divergence-free test fields (the pressure is eliminated by testing against solenoidal fields; see Method),
- the **energy inequality** (not equality):
$$\tfrac12\|u(t)\|_{L^2}^2 + \nu\int_{s}^{t}\|\nabla u(\tau)\|_{L^2}^2\,d\tau \ \le\ \tfrac12\|u(s)\|_{L^2}^2$$
for $t\ge s$, for a.e. $s$ (including $s=0$).

The pair $L^\infty_t L^2_x\cap L^2_t\dot H^1_x$ is the **Leray class**. It is exactly the regularity that the energy bound (above) makes available, no more. This is the first appearance of the function space in which the existence-and-smoothness problem is posed.

### 3. The set of singular times is small

A weak solution can fail to be strong only on a closed set $\Sigma\subset(0,\infty)$ of times (Leray's "epochs of irregularity"). Leray proves $\Sigma$ has Lebesgue measure zero, and his structural estimate (the $(T^*-t)^{-1/4}$ lower bound on $\|\nabla u\|_{L^2}$ at a singular time, combined with the integrability $\nabla u\in L^2_t$) forces $\Sigma$ to be **so sparse that its upper box-counting (Minkowski) dimension is at most $1/2$**. The clean Hausdorff-dimension reading, $\dim_{\mathcal H}\Sigma\le 1/2$, and the sharpening $\mathcal H^{1/2}(\Sigma)=0$, are due to Scheffer (1976) building directly on Leray's estimate. (verify: Leray 1934 did not phrase it as a fractal dimension, the box-counting language being later; the $1/2$ exponent is, however, exactly Leray's, read off his blow-up-rate estimate.)

This is the *temporal* partial-regularity result, and it is the direct ancestor of the *spacetime* partial regularity of Caffarelli-Kohn-Nirenberg (1982), whose singular set has parabolic Hausdorff dimension $\le 1$.

### 4. Eventual regularity (regularity for large time)

There is a time $T_0<\infty$ after which the weak solution is strong and smooth: $\Sigma\subset(0,T_0)$. Concretely, the energy dissipates, $\|u(t)\|_{L^2}^2\to$ a value small enough that the local-existence smallness condition is met, so on $[T_0,\infty)$ the solution is regular and unique. The singular epochs are confined to a bounded initial interval. This is the first instance of the principle "singularities, if any, are an early-time, finite-energy-budget phenomenon."

### 5. Weak-strong uniqueness (seed)

Leray's estimates contain the seed of what is now called weak-strong uniqueness: if a strong solution exists on $[0,T]$ with the same data, then *every* weak solution satisfying the energy inequality coincides with it on $[0,T]$. The clean modern statement and proof (a Gronwall argument on the difference, closing because the strong solution supplies a subcritical control such as $u\in L^4_tL^4_x$ or $u\in L^\infty_t L^3_x$) is usually attributed to the Prodi-Serrin-Ladyzhenskaya line, but the mechanism is already implicit here. (verify: attribution of the first explicit weak-strong statement; Leray has the local-in-time uniqueness, the global weak-strong packaging is Prodi/Serrin 1959-1963.)

### 6. The self-similar blow-up ansatz

Leray proposed, as a candidate finite-time singularity, a backward self-similar solution of the form
$$u(x,t) \ =\ \frac{1}{\sqrt{2a(T^*-t)}}\ U\!\left(\frac{x}{\sqrt{2a(T^*-t)}}\right),$$
which is exactly the profile invariant under the Navier-Stokes scaling $u_\lambda(x,t)=\lambda u(\lambda x,\lambda^2 t)$ with the blow-up time $T^*$. He could neither construct nor exclude a nontrivial profile $U$. This is the origin of **Architecture 4**. The exclusion came much later: Necas-Ruzicka-Sverak (1996) ruled out nontrivial profiles with $U\in L^3(\mathbb{R}^3)$, and Tsai (1998) extended and sharpened this. So Leray's specific mechanism is dead, but only in the $L^3$ / finite-local-energy class; discretely self-similar and more general scenarios remain open.

---

## Method / structure

The construction is the prototype of every "regularize, bound, compactness, pass to the limit" existence proof in nonlinear PDE.

### Regularization

Leray mollifies the transport velocity. Replace the nonlinearity $(u\cdot\nabla)u$ by $((J_\varepsilon u)\cdot\nabla)u$, where $J_\varepsilon$ is a spatial mollifier (a smooth retardation/averaging of the advecting field). The regularized system is semilinear and globally well-posed for each $\varepsilon>0$, because the smoothed transport coefficient is a fixed nice vector field at each instant. This is the move that buys a genuine solution to work with.

### The Leray projector and the role of the pressure

The pressure is not an independent unknown; it is the Lagrange multiplier enforcing $\nabla\cdot u=0$. Taking the divergence of the momentum equation and using $\nabla\cdot u=0$ gives the diagnostic Poisson equation
$$-\Delta p \ =\ \nabla\cdot\big((u\cdot\nabla)u\big) \ =\ \partial_i\partial_j(u_i u_j),$$
so $p=(-\Delta)^{-1}\partial_i\partial_j(u_iu_j)$ is a nonlocal, zeroth-order (Calderon-Zygmund) function of $u$. Equivalently one projects the whole equation onto divergence-free fields with the **Leray (Helmholtz) projector**
$$\mathbb{P} \ =\ \mathrm{Id} - \nabla(-\Delta)^{-1}(\nabla\cdot),$$
which annihilates gradients and so removes $\nabla p$ entirely:
$$\partial_t u \ =\ \nu\,\Delta u - \mathbb{P}\big((u\cdot\nabla)u\big).$$
This is the structural reason the pressure never needs its own a priori bound, and the reason weak solutions can be tested against solenoidal fields without ever mentioning $p$. The repo's Lean skeleton has a `LerayProjector` module for exactly this object; the project's whole spectral solver lives on the divergence-free subspace this projector defines.

### The energy bound, uniformly in the regularization

Test the regularized momentum equation against $u$ itself. The pressure term drops ($\int u\cdot\nabla p = -\int p\,(\nabla\cdot u)=0$), and the (mollified) transport term drops as well, because for divergence-free advection $\int ((J_\varepsilon u)\cdot\nabla)u\cdot u = \tfrac12\int (J_\varepsilon u)\cdot\nabla|u|^2 = 0$. What survives is
$$\tfrac{d}{dt}\,\tfrac12\|u^\varepsilon(t)\|_{L^2}^2 \ =\ -\,\nu\,\|\nabla u^\varepsilon(t)\|_{L^2}^2 \ \le\ 0.$$
Integrating gives the energy *identity* for each smooth regularized solution, and in particular a bound on $\|u^\varepsilon\|_{L^\infty_tL^2_x}$ and $\|\nabla u^\varepsilon\|_{L^2_tL^2_x}$ that is **uniform in $\varepsilon$**. This uniform bound is the entire engine of the proof: it is what survives the limit.

### Compactness and passage to the limit

The uniform energy bound gives weak-$*$ compactness in $L^\infty_tL^2_x$ and weak compactness in $L^2_t\dot H^1_x$. To pass to the limit in the nonlinear term one needs *strong* convergence of $u^\varepsilon$ in $L^2_{t,x}^{\mathrm{loc}}$, which Leray obtains by an Arzela-Ascoli-type argument controlling time-translations (the modern packaging is the **Aubin-Lions-Simon lemma**: a bound on $u^\varepsilon$ in $L^2_t\dot H^1_x$ plus a bound on $\partial_t u^\varepsilon$ in a negative-order space gives compactness in $L^2_{t,x}^{\mathrm{loc}}$). Strong $L^2_{t,x}$ convergence lets the quadratic nonlinearity pass to the limit.

### Why weak limits lose energy

The energy *identity* holds for each $u^\varepsilon$. But $\|\cdot\|_{L^2}$ is only weakly lower semicontinuous, so under weak convergence $u^\varepsilon\rightharpoonup u$ one gets
$$\|u(t)\|_{L^2}^2 \ \le\ \liminf_{\varepsilon\to 0}\|u^\varepsilon(t)\|_{L^2}^2,\qquad \int\|\nabla u\|_{L^2}^2 \ \le\ \liminf_{\varepsilon\to0}\int\|\nabla u^\varepsilon\|_{L^2}^2.$$
Energy can be *lost* in the limit but never created. This is the structural origin of the **inequality** in the energy inequality. Equality would say there is no anomalous dissipation, which is a regularity-/Onsager-type statement (energy equality is known for solutions slightly better than Leray class, e.g. $u\in L^3_tL^3_x$-type conditions; below that, convex integration of Architecture 5 produces wild solutions that dissipate anomalously). The gap between inequality and equality is therefore not a technical artifact: it is the same gap as the regularity problem, viewed energetically.

### The blow-up-rate lemma (seed of partial regularity)

For the strong solution, differentiating the higher norm and using the local existence time-estimate, Leray gets that at a finite blow-up time $T^*$ the quantity $\|\nabla u(t)\|_{L^2}$ must blow up at least like $(T^*-t)^{-1/4}$. Because $\nabla u\in L^2_t$ globally, a singular time $t_0$ contributes $\int^{t_0}(T^*-t)^{-1/2}\,dt$, and the bookkeeping of how many such times can fit inside a finite $L^2_t$ budget is exactly what forces the singular-time set to have dimension $\le 1/2$. The $1/2$ here is the same $1/2$ that appears as the critical Sobolev index $\dot H^{1/2}$ and as the CKN supercriticality deficit; it is not a coincidence but the shadow of the scaling.

---

## Criticality placement

This is the load-bearing section for the project, because Leray 1934 is *where the supercriticality enters the story*.

Under the scaling $u_\lambda(x,t)=\lambda\,u(\lambda x,\lambda^2 t)$, the criticality bookkeeper (`experiments/_shared/criticality.py`) assigns to a purely spatial norm $\|u\|_{L^q}$ the exponent $a=1-d/q$, so in $d=3$:

| Quantity | norm | scaling exponent $a$ | class |
|---|---|---|---|
| Energy | $\|u\|_{L^2}$ | $1-3/2=-\tfrac12$ | **supercritical** |
| Dissipation rate | $\|\nabla u\|_{L^2}=\|u\|_{\dot H^1}$ | $1+1-3/2=+\tfrac12$ | subcritical |
| Critical Sobolev | $\|u\|_{\dot H^{1/2}}$ | $1+\tfrac12-\tfrac32=0$ | critical |
| ESS endpoint | $\|u\|_{L^3}$ | $1-3/3=0$ | critical |

The bound Leray actually controls *for all time* is $\|u\|_{L^\infty_tL^2_x}$, and its spatial part has exponent $a=-1/2<0$: **the energy is supercritical** (`audit_estimate` returns `INSUFFICIENT_BY_ITSELF`). The companion bound $\|\nabla u\|_{L^2_tL^2_x}$ is subcritical *pointwise in space* but is only $L^2$ in time, hence not an $L^\infty_t$ bound and not a pointwise-in-time control; it cannot be promoted to a critical-norm bound by interpolation against the supercritical energy without a loss. Concretely, $L^\infty_t L^2_x\cap L^2_t\dot H^1_x$ interpolates (Ladyzhenskaya/Sobolev) to $u\in L^{10/3}_{t,x}$ in 3D, and the scaling of $L^{p}_tL^{q}_x$ is critical only on the Prodi-Serrin line $2/p+3/q=1$; the pair $(p,q)=(10/3,10/3)$ gives $2/p+3/q=6/10+9/10=3/2>1$, which is **supercritical**, i.e. short of the regularity line by a fixed margin. That margin is the supercriticality gap, and it is exactly $1/2$ wide.

So the criticality reading of Leray 1934 is: the construction is unconditional and global, but the *only* global bound it produces sits a fixed distance ($a=-1/2$ in the $L^2$ exponent, equivalently the $3/2>1$ excess on the Prodi-Serrin line) below the critical level where a singularity would have to register. This is the precise sense of "the energy does not see small scales." Any proof that closes regularity must add genuinely critical (scale-invariant) control on top of Leray's energy; the energy cannot be bootstrapped there by interpolation alone. See [Direction 03: the supercriticality gap](../research_directions/03_supercriticality_gap.md).

---

## Against the three controls

**(A) 2D Navier-Stokes is globally smooth.** Leray's *existence* construction is dimension-agnostic: the same regularize-bound-compactness argument produces weak solutions in 2D, 3D, and higher. That is correct and is *not* a violation, because the existence theorem makes no smoothness claim. The dimension sensitivity lives one level up, in the a priori bounds. In 2D the energy estimate is supplemented by the *enstrophy* estimate (the 2D vorticity equation $\partial_t\omega+u\cdot\nabla\omega=\nu\Delta\omega$ has no stretching term $\omega\cdot\nabla u$, so $\int|\omega|^2$ is non-increasing), and enstrophy control is subcritical/critical enough to force global smoothness. Leray's *3D* construction deliberately stops at the energy because the 3D vorticity equation
$$\partial_t\omega + u\cdot\nabla\omega \ =\ \omega\cdot\nabla u + \nu\Delta\omega$$
carries the stretching term $\omega\cdot\nabla u$, which has no sign and no a priori bound. So the paper is *on the correct side* of control (A): it does not pretend to a smoothness conclusion that would equally hold in 2D, and it correctly locates the 3D-specific difficulty (vortex stretching) as the reason the energy is all there is. The 2D control fires green.

**(B) Supercriticality is the ceiling.** This is the paper's primary tie-in and it fires loudly. The energy inequality is *the* global a priori bound, and it is supercritical ($a=-1/2$). Leray 1934 is the paper that installs the ceiling. Every later unconditional result (CKN partial regularity, the eventual-regularity time $T_0$, the $\dim\le 1/2$ singular-time set) inherits the $1/2$ deficit visibly. The bookkeeper's verdict on the controlling norm is `INSUFFICIENT_BY_ITSELF`, and that verdict is not a criticism of Leray, it is the discovery the paper makes.

**(C) Viscosity / Burgers control.** Leray's whole construction uses $\nu>0$ essentially: the dissipative term $\nu\Delta u$ is what makes the regularized problem globally solvable and what produces the $L^2_t\dot H^1_x$ bound (the dissipation term in the energy identity). At $\nu=0$ (Euler) the energy identity loses its negative-definite right-hand side, the $\dot H^1_t$ control disappears, and the construction does not yield the Leray class. So the method is *not* blind to viscosity; viscosity is load-bearing. This is the correct posture: the inviscid limit is genuinely more singular (Burgers shocks, Elgindi's $C^{1,\alpha}$ Euler blow-up), and Leray's solutions are viscous objects. Control (C) fires green. Caveat worth flagging for the discrepancy log: Leray's *bounds* do not quantitatively use $\nu$ in a way that survives the inviscid limit, so the paper does not by itself explain *why* viscosity prevents blow-up, only that the construction needs it.

This paper sits squarely *inside* the wrong-approach discipline (it is Architecture 1, not Architecture 5): it is about genuine solutions of the smooth flow and their a priori bounds, not about the boundary of what "solution" means.

---

## What it gives / what it does not give

**Gives:**

- A global-in-time object to study for *arbitrary* finite-energy data, with no smallness assumption. This is the only existence theorem in the unconditional global regime; everything conditional (Architectures 2, 3) is about upgrading it.
- The function class $L^\infty_tL^2_x\cap L^2_t\dot H^1_x$ in which the Clay problem is posed.
- The energy inequality, the one coercive all-time a priori bound.
- The first partial-regularity statement (singular times have dimension $\le 1/2$) and the first eventual-regularity statement (smooth after $T_0$).
- The blow-up-rate lower bounds at a hypothetical singularity, the template for all critical-norm-must-blow-up results.
- The self-similar blow-up ansatz, the origin of Architecture 4.

**Does not give (the gap to closing regularity):**

- *Uniqueness* of weak solutions in 3D. Open in the Leray class; *false* just below it (Buckmaster-Vicol 2019, Albritton-Brue-Colombo 2022 for forced NS), which is Architecture 5 territory.
- *Regularity* of the weak solution for general data. The weak solution might develop singularities; Leray cannot exclude this, only confine it (dimension $\le 1/2$ in time, finite eventual time $T_0$).
- *Energy equality.* The limit only inherits the inequality; equality is a regularity-strength statement.
- Any *critical-scale* control. The energy is supercritical; the gap to a critical bound is a fixed $1/2$ wide and cannot be interpolated shut from the energy alone. Closing it is the whole problem.

The honest one-line summary: Leray 1934 produces the patient and the only universal vital sign (energy), and proves the patient is healthy for all large time and singular on at most a dimension-$1/2$ set of times. It does not produce the critical-scale instrument that would prove the patient never gets sick. That instrument is what Architectures 2 and 3 are trying to build, and the supercriticality gap is the project's coordinate for *where* it must be built.

---

## Lineage and sharpest known form

**Builds on:** Oseen's linear theory and the heat-kernel / Oseen-tensor representation of the Stokes problem; the Helmholtz decomposition (here as the Leray projector); the variational and compactness tools of the early 1930s. The mollification idea is Leray's own.

**Built on it (direct descendants):**

- **Hopf (1951):** the construction on bounded domains via Galerkin truncation rather than mollification; the class is now "Leray-Hopf." (See [`hopf_1951.md`](hopf_1951.md) if present.)
- **Prodi (1959), Serrin (1962), Ladyzhenskaya (1967):** the conditional regularity criteria $u\in L^p_tL^q_x$, $2/p+3/q\le 1$, $q>3$, and clean weak-strong uniqueness. The endpoint $q=3$ is Escauriaza-Seregin-Sverak. See [`escauriaza_seregin_sverak_2003.md`](escauriaza_seregin_sverak_2003.md).
- **Scheffer (1976):** first systematic study of the dimension of the singular-time and singular-spacetime sets, sharpening Leray's epoch estimate to $\mathcal H^{1/2}(\Sigma)=0$ in time and initiating spacetime partial regularity.
- **Caffarelli-Kohn-Nirenberg (1982):** spacetime partial regularity, $\mathcal P^1(S)=0$ (parabolic Hausdorff dimension $\le 1$), via the $\varepsilon$-regularity theorem for *suitable* weak solutions (Leray-Hopf plus a local energy inequality). The temporal $\dim\le1/2$ of Leray is the slice of this. See [`caffarelli_kohn_nirenberg_1982.md`](caffarelli_kohn_nirenberg_1982.md).
- **Fujita-Kato (1964), Koch-Tataru (2001):** small-data global existence in the critical spaces $\dot H^{1/2}$ and $\mathrm{BMO}^{-1}$, the critical-scale counterpart to Leray's supercritical energy. See [Direction 01](../research_directions/01_critical_continuation_criteria.md) and [Direction 03](../research_directions/03_supercriticality_gap.md).
- **Necas-Ruzicka-Sverak (1996), Tsai (1998):** exclusion of Leray's self-similar profiles in $L^3$, the first killing of an explicit blow-up mechanism. See [Direction 04](../research_directions/04_blowup_and_barriers.md).

**Sharpest known refinements as of 2025:**

- *Quantitative critical-norm blow-up.* Tao (2019/2020) made the ESS endpoint quantitative: at a singularity $\|u(t)\|_{L^3}$ must grow at least like $(\log\log\log\frac{1}{T^*-t})^{c}$ (a triple-logarithm). This is the modern descendant of Leray's $(T^*-t)^{-1/4}$ rate lower bound, now at the critical exponent rather than at the subcritical $p>3$. Barker-Prange and others have pushed quantitative regularity and concentration estimates further (annuli of concentration, quantitative epochs).
- *Energy equality thresholds.* The inequality-vs-equality gap is now sharply mapped: energy equality holds under conditions slightly above the Leray class (e.g. $u\in L^4_tL^4_x$ on the torus, or $L^3_tL^3_x$-type Onsager-critical conditions), and fails below, where convex integration (Buckmaster-Vicol 2019; Albritton-Brue-Colombo 2022, the latter even within Leray-Hopf for forced NS) produces non-unique, anomalously dissipating solutions. See [Direction 05](../research_directions/05_convex_integration_boundary.md).
- *Singular-time set, dimension below $1/2$.* Recent convex-integration constructions (Buckmaster-Colombo-Vicol and successors, ~2018-2023) exhibit *wild* weak solutions whose singular-time set has Hausdorff dimension strictly below $1$, probing how far Leray's $\le1/2$ can be pushed for non-Leray-Hopf solutions. (verify: exact dimension values; the relevant constructions give explicit dimensions $<1$, not necessarily reaching $1/2$, and concern wild rather than Leray-Hopf solutions.)
- *Modern review.* Ozanski and Pooley, "Leray's fundamental work on the Navier-Stokes equations" (arXiv:1708.09787, 2017), is the definitive modern re-derivation of every theorem above with current notation; it is the recommended companion to the original French.

---

## Discrepancy log (against the project's existing analyses)

- The project's `references/README.md` summarizes Leray 1934 as "global weak solutions exist; the energy inequality; the self-similar blow-up attempt." That is correct but undersells two load-bearing items this note adds: the **temporal partial regularity** (singular times of dimension $\le 1/2$) and the **eventual regularity** ($T_0$). They should be promoted in the index because they are the direct ancestors of CKN and of the quantitative-regularity program.
- The CLAUDE.md landmark list dates Leray-Hopf as "(1934, 1951)" and attributes 2D global regularity to "Ladyzhenskaya 1959." Both are consistent with this note. No contradiction; flagging only that the 2D global-regularity *mechanism* (no vortex stretching) is already implicit in Leray's vorticity bookkeeping, so the 1959 attribution is for the bounded-domain/clean statement, not the underlying idea.
- The prior stub asserted the energy inequality "$\le$" with the loss-of-energy explanation, which this note preserves verbatim in spirit and expands with the weak-lower-semicontinuity mechanism. No correct content was discarded.

---

## What this enables / what remains open

**Enables (for BUILDER):** any candidate a priori estimate must be stated *relative to Leray's energy*, i.e. as additional control beyond $L^\infty_tL^2_x\cap L^2_t\dot H^1_x$, and must be audited by the criticality bookkeeper to confirm it reaches at least the critical level $a=0$. An estimate controlled only by the energy is `INSUFFICIENT_BY_ITSELF` by construction and should not be proposed as regularity-closing. The interpolation $u\in L^{10/3}_{t,x}$ with its $3/2>1$ Prodi-Serrin excess is the precise numerical target a closing argument must beat.

**Enables (for ADVERSARY):** the supercriticality of the energy is the cleanest single test. Any proposed method that would deliver smoothness using only energy-level inputs is wrong by control (B), and it would moreover (likely) "work" identically in 2D by control (A), since 2D global regularity needs the extra enstrophy input that 3D lacks. Leray 1934 is the reference point for both fires.

**Remains open (the gap Leray defines):**

1. Uniqueness and regularity of 3D Leray-Hopf solutions for general data.
2. Whether the energy inequality is an equality (no anomalous dissipation) for Leray-Hopf solutions.
3. Whether the singular-time set $\Sigma$ is empty (the temporal form of the regularity problem), beyond $\dim\le 1/2$.
4. Any critical-scale a priori bound that holds for all time without a smallness assumption. This is the central missing instrument; the supercriticality gap is its absence made quantitative.

---

## References

- J. Leray, "Sur le mouvement d'un liquide visqueux emplissant l'espace," *Acta Mathematica* **63** (1934), 193-248.
- E. Hopf, "Uber die Anfangswertaufgabe fur die hydrodynamischen Grundgleichungen," *Math. Nachr.* **4** (1951), 213-231.
- V. Scheffer, "Partial regularity of solutions to the Navier-Stokes equations," *Pacific J. Math.* **66** (1976), 535-552.
- L. Caffarelli, R. Kohn, L. Nirenberg, "Partial regularity of suitable weak solutions of the Navier-Stokes equations," *Comm. Pure Appl. Math.* **35** (1982), 771-831.
- G. Prodi, "Un teorema di unicita per le equazioni di Navier-Stokes," *Ann. Mat. Pura Appl.* **48** (1959), 173-182.
- J. Serrin, "On the interior regularity of weak solutions of the Navier-Stokes equations," *Arch. Rational Mech. Anal.* **9** (1962), 187-195.
- H. Fujita, T. Kato, "On the Navier-Stokes initial value problem I," *Arch. Rational Mech. Anal.* **16** (1964), 269-315.
- J. Necas, M. Ruzicka, V. Sverak, "On Leray's self-similar solutions of the Navier-Stokes equations," *Acta Math.* **176** (1996), 283-294.
- T.-P. Tsai, "On Leray's self-similar solutions of the Navier-Stokes equations satisfying local energy estimates," *Arch. Rational Mech. Anal.* **143** (1998), 29-51.
- H. Koch, D. Tataru, "Well-posedness for the Navier-Stokes equations," *Adv. Math.* **157** (2001), 22-35.
- L. Escauriaza, G. Seregin, V. Sverak, "$L_{3,\infty}$-solutions of Navier-Stokes equations and backward uniqueness," *Russian Math. Surveys* **58** (2003), 211-250.
- T. Tao, "Quantitative bounds for critically bounded solutions to the Navier-Stokes equations," (2019/2020).
- T. Buckmaster, V. Vicol, "Nonuniqueness of weak solutions to the Navier-Stokes equation," *Ann. of Math.* **189** (2019), 101-144.
- D. Albritton, E. Brue, M. Colombo, "Non-uniqueness of Leray solutions of the forced Navier-Stokes equations," *Ann. of Math.* **196** (2022), 415-455.
- W. S. Ozanski, B. C. Pooley, "Leray's fundamental work on the Navier-Stokes equations: a modern review," arXiv:1708.09787 (2017).

---

*Cross-links:* [Direction 01 (critical continuation criteria)](../research_directions/01_critical_continuation_criteria.md) | [Direction 03 (the supercriticality gap)](../research_directions/03_supercriticality_gap.md) | [Direction 04 (blow-up and barriers)](../research_directions/04_blowup_and_barriers.md) | [Direction 05 (convex integration boundary)](../research_directions/05_convex_integration_boundary.md) | sibling notes: [CKN 1982](caffarelli_kohn_nirenberg_1982.md), [ESS 2003](escauriaza_seregin_sverak_2003.md), [BKM 1984](beale_kato_majda_1984.md).
