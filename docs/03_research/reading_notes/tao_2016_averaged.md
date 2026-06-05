# Reading notes: Tao (2016), finite-time blow-up for an averaged 3D Navier-Stokes

Terence Tao, "Finite time blowup for an averaged three-dimensional Navier-Stokes equation," Journal of the American Mathematical Society 29:3 (2016), 601-674. DOI 10.1090/jams/838. (arXiv:1402.0290, 2014.)

> This is the single most orienting *negative* result on the regularity side, and it is a barrier, not a result about the true equation. Tao constructs an averaged version of 3D Navier-Stokes whose nonlinearity is an average of the genuine bilinear term over Fourier multipliers and rotations, engineered so it keeps the three soft structural features people lean on: the energy identity $\langle\tilde B(u,u),u\rangle=0$, the exact scaling symmetry $u_\lambda(x,t)=\lambda u(\lambda x,\lambda^2 t)$, and the dimensional (frequency-locality) structure. That averaged system has a smooth finite-energy solution that blows up in finite time. The consequence is sharp and structural: any proof of global regularity for true Navier-Stokes must use a feature of the *exact* nonlinearity that averaging destroys, because energy-plus-scaling alone provably does not prevent blow-up. This is Architecture 4 (blow-up and barriers) and it is the ground truth behind Control (B), the supercriticality ceiling, and behind the criticality bookkeeper's `INSUFFICIENT_BY_ITSELF` verdict on any purely energy-controlled estimate. It disciplines Direction 03: a candidate critical coercive quantity that would also be monotone for the averaged system is automatically insufficient.

## What it proves

### Statement

Work on $\mathbb{R}^3$ (the same construction adapts to $\mathbb{T}^3$). The true Navier-Stokes system in Leray-projected form is
$$\partial_t u = \Delta u + B(u,u), \qquad \nabla\cdot u = 0,$$
with the bilinear nonlinearity
$$B(u,u) = -\mathbb{P}\,(u\cdot\nabla)u,$$
where $\mathbb{P}$ is the Leray projection onto divergence-free fields (the pressure has been eliminated by $\mathbb{P}$). Set the viscosity $\nu=1$ by rescaling; the construction keeps the genuine Laplacian $\Delta$, so this is *not* a hyperdissipative caricature.

**Theorem (Tao 2016).** There is an averaged bilinear operator $\tilde B$, of the same algebraic type as $B$, such that:

1. **(Same energy identity.)** $\tilde B$ is bounded, bilinear, divergence-free valued, and antisymmetric in the energy pairing,
   $$\langle \tilde B(u,u),\,u\rangle_{L^2} = 0 \qquad \text{for all divergence-free } u,$$
   so the averaged flow $\partial_t u = \Delta u + \tilde B(u,u)$ obeys the *exact same* energy identity as true NS:
   $$\tfrac12\frac{d}{dt}\|u\|_{L^2}^2 = -\|\nabla u\|_{L^2}^2 \le 0.$$
2. **(Same scaling and dimension.)** $\tilde B$ commutes with the Navier-Stokes scaling and translation symmetries and respects the dimensional structure: $\tilde B$ has the same order (it maps roughly $H^s \times H^s \to H^{s-1}$ in the right range) and frequency support locality as $B$, so the averaged system has the identical scaling $u_\lambda(x,t)=\lambda u(\lambda x,\lambda^2 t)$ and the identical local well-posedness theory in the critical and subcritical spaces.
3. **(Finite-time blow-up.)** There exists smooth, compactly-supported-in-frequency, finite-energy, divergence-free initial data $u_0$ for which the unique smooth solution of the averaged system $\partial_t u=\Delta u+\tilde B(u,u)$ develops a singularity in finite time: there is $T_\ast<\infty$ with
   $$\limsup_{t\uparrow T_\ast}\|u(\cdot,t)\|_{H^s(\mathbb{R}^3)}=+\infty \qquad \text{for every } s>s_c,$$
   while the energy $\|u(t)\|_{L^2}$ stays bounded (indeed non-increasing) all the way to $T_\ast$.

Here $s_c$ is the critical Sobolev regularity. The blow-up is invisible to the energy: it happens only in the high regularity norms, exactly the small-scale information the supercritical $L^2$ does not see.

### Form of the averaged operator

The genuine $B$ has, in frequency, the schematic shape
$$\widehat{B(u,u)}(\xi) = \int_{\xi=\eta+\zeta} m(\xi,\eta,\zeta)\,\hat u(\eta)\,\hat u(\zeta)\,d\eta,$$
with a symbol $m$ built from the convolution $u\cdot\nabla u$ and the projection $\mathbb{P}$. Tao replaces $m$ by an *average* over a measured family of multiplier-and-rotation symmetries,
$$\tilde m(\xi,\eta,\zeta) = \mathbb{E}_{R,\,\psi}\; \psi(\xi,\eta,\zeta)\, m_R(\xi,\eta,\zeta),$$
where $R$ ranges over rotations and $\psi$ over multipliers chosen so the average preserves antisymmetry (hence the energy identity), preserves the order and homogeneity (hence the scaling), but loses the rigid pointwise/physical-space identity $(u\cdot\nabla)u$ and the precise sign-and-cancellation pattern of the true symbol. The freedom in choosing the averaging weights is exactly what lets Tao install a chosen dynamical mechanism while keeping the soft invariants fixed.

## Method / structure

The proof has two layers: a *dyadic-model* design (a discrete ODE caricature where the mechanism is transparent) and an *embedding* of that mechanism into a genuine averaged PDE on $\mathbb{R}^3$ keeping the three invariants.

### 1. The blow-up machine (self-replicating energy cascade)

Tao engineers the averaged nonlinearity so the dynamics realizes an abstract "blow-up machine," which he frames as a self-replicating finite-state machine (a von-Neumann-style replicator) wired out of frequency-localized mode interactions. Organize the modes into dyadic frequency shells of scale $2^n$. The machine does the following, on repeat:

- A bump of energy sits, at time $T_n$, primarily in the shell at scale $2^n$ (frequencies $\sim 2^n$).
- The averaged nonlinearity is tuned so this bump *abruptly pumps its energy into the next shell* at scale $2^{n+1}$, leaving a faithful (rescaled) copy of itself one octave up, and then the next, and so on.
- Each transfer is faster than the last. The transfer times satisfy
  $$T_{n+1}-T_n \;\sim\; 2^{-\alpha n}\quad (\alpha>0),\qquad \text{so}\qquad T_n \uparrow T_\ast=\sum_n (T_{n+1}-T_n) < \infty.$$
  The geometric (summable) spacing is what makes infinitely many octave-jumps fit into finite time.

Because each generation is a rescaled replica of the previous one, the dynamics is *quasi-periodic* under the scaling group: it looks the same at every octave, just faster and smaller. As $n\to\infty$ the energy has migrated to arbitrarily high frequency at the finite time $T_\ast$, which is precisely a finite-time singularity (loss of smoothness, divergence of every $H^s$ with $s>s_c$).

### 2. Why the energy identity does not stop it

This is the load-bearing structural point for the project. The cascade *conserves* the (modulo viscous dissipation, decreases) total energy at every transfer: energy is moved from shell $2^n$ to shell $2^{n+1}$, not created. The energy budget
$$\tfrac12\|u(t)\|_{L^2}^2 + \int_0^t\|\nabla u\|_{L^2}^2\,ds = \tfrac12\|u_0\|_{L^2}^2$$
holds throughout, and $\|u(t)\|_{L^2}$ stays bounded up to $T_\ast$. The viscosity $\Delta$ does fight the cascade, because dissipation at scale $2^n$ acts at rate $\sim 2^{2n}$, but the machine is tuned so each transfer happens *faster* than the viscous time of its shell. The nonlinear transfer wins the race at every octave. So the genuine Laplacian is present and the energy inequality is satisfied, and neither stops the blow-up. The blow-up is supercritical-invisible: it lives entirely in the high-frequency, high-$H^s$ content that the energy norm cannot resolve.

### 3. Embedding into a true averaged PDE

The delicate part is realizing the abstract machine inside an operator $\tilde B$ that is genuinely of NS type (an average of $B$) rather than an ad hoc dyadic shell model. Tao does this by:

- Building the interaction coefficients of the machine out of frequency-localized, rotation-averaged multiplier symbols, so that $\tilde B$ is literally an average of the true symbol $m$ over a symmetry family.
- Enforcing antisymmetry in the energy pairing at the symbol level, which gives $\langle\tilde B(u,u),u\rangle=0$ for free and hence the exact energy identity.
- Enforcing the homogeneity/order of the true symbol, which gives the exact scaling and the standard local well-posedness (so "smooth solution that then blows up" is meaningful: the solution is genuinely smooth and unique until $T_\ast$).

The output is a bona fide nonlocal but NS-shaped equation, not a toy. Earlier dyadic shell models (Katz-Pavlovic, Friedlander-Pavlovic, Cheskidov) already showed that *shell-model* caricatures can blow up; Tao's advance is to keep the average a genuine average of the true bilinear operator with all three soft invariants intact, closing the gap between "a model blows up" and "energy-plus-scaling does not forbid blow-up for an NS-type operator."

## Criticality placement

Run the relevant norms through `experiments/_shared/criticality.py`:

- **Energy $L^\infty_t L^2_x$** has spatial scaling exponent $1-d/q = 1-3/2 = -1/2 < 0$: **supercritical**. This is the only globally coercive a priori quantity the averaged system has (it has the *same* energy identity as true NS), and it is exactly the quantity that fails to stop the cascade. The bookkeeper returns `SUPERCRITICAL` / `INSUFFICIENT_BY_ITSELF`.
- **The critical Sobolev $\dot H^{1/2}$** has exponent $s-1/2 = 0$: **critical**. The averaged system blows up *above* this level (in $H^s$, $s>s_c$); small data in the critical space is fine for both systems (the local theory is shared), but the constructed data is not small, and there is no global critical a priori bound to save it.
- **The blow-up signature $\|u\|_{H^s}$, $s>s_c$**, is **subcritical** (exponent $s-1/2>0$): a global bound here *would* close regularity, and the theorem is precisely that no such bound follows from the energy identity plus scaling, because a counterexample operator with those invariants violates it.

The placement is the entire content. Tao's barrier is the rigorous statement that the chain
$$\text{energy identity} \;+\; \text{scaling} \;\not\Rightarrow\; \text{a critical or subcritical a priori bound}.$$
The supercriticality gap is not an artifact of clumsy estimates; it is a genuine obstruction, certified by an explicit NS-type operator that has every soft invariant and still blows up. This is the mathematical justification for the criticality bookkeeper's `AT_THE_MARGIN` verdict on critical norms and `INSUFFICIENT_BY_ITSELF` verdict on supercritical ones (see `../../../experiments/_shared/criticality.py`, function `audit_estimate`).

## Against the three controls

- **(A) 2D control: passes, and is the sharp diagnostic.** The averaged construction is intrinsically 3-dimensional. It exploits the 3D scaling $s_c=1/2$ and a vector nonlinearity rich enough to host a self-replicating shell cascade with vortex-stretching-like energy amplification across octaves. The true 2D Navier-Stokes nonlinearity is constrained by the absence of vortex stretching (scalar vorticity transported with diffusion, non-increasing enstrophy $\int|\omega|^2$), and an honest 2D averaging respecting the 2D conservation structure would not support the machine. The lesson aligns exactly with Control (A): the reason the *true* equation might still be regular, while this averaged caricature is not, is plausibly a structural feature (the precise transport/stretching geometry) that 2D shows is decisive. Tao's barrier does *not* falsely predict 2D blow-up; it predicts that whatever forbids 2D blow-up is a feature averaging is allowed to break.
- **(B) Supercriticality ceiling: this result *is* the ceiling, made rigorous.** The averaged system saturates Control (B). It has the energy identity and nothing critical-or-stronger that is globally coercive, and it blows up. So any a priori estimate controlled by the energy norm is `INSUFFICIENT_BY_ITSELF`: there exists an NS-type operator for which that exact estimate holds and regularity nonetheless fails. This is the strongest possible certificate that the energy method cannot, alone, close the problem. It is the analog of a sharp counterexample that removes an entire class of soft arguments at one stroke.
- **(C) Viscosity / exact-structure control: passes, with a refinement.** The construction *keeps* the genuine viscosity $\Delta$ (it is not a hyperdissipation trick), so it is not "blind to viscosity." The point is subtler than Control (C) in its Burgers/Euler form: viscosity is present and the flow still blows up, because the nonlinear cascade out-races dissipation at every scale. So the lesson is not "viscosity does not matter" but "viscosity-plus-energy-plus-scaling is not enough." What is missing is the *exact* nonlinear structure. Control (C) names viscosity and the exact NS structure together; Tao shows that for the averaged system viscosity alone is insufficient, sharpening the control to: the precise nonlinearity is what must be used, and the inviscid intuition (Burgers shocks, Euler singularity evidence, Elgindi 2021) was already telling us the nonlinearity is the dangerous object.

This is an Architecture 4 result and sits fully inside the wrong-approach discipline. It is not an Architecture 5 (convex-integration) object: it produces a *genuinely smooth, unique* solution that loses regularity, not a rough non-unique weak solution below the energy class. It speaks about regularity of the smooth flow, not about the boundary of what "solution" means.

## What it gives / what it does not give

**Gives.**

- A rigorous proof that "energy identity + exact scaling + viscosity + NS-type (averaged-bilinear) nonlinearity" does *not* imply global regularity. The supercriticality gap is a theorem about a real operator, not a heuristic.
- A *requirement* on any future regularity proof, stated as a necessary condition: it must use a property of the *exact* NS nonlinearity $B(u,u)=-\mathbb{P}(u\cdot\nabla)u$ that the averaging destroys. Candidate distinguishing features, none of which $\tilde B$ retains:
  1. the precise *local / pointwise* structure of $u\cdot\nabla u$ in physical space (averaging delocalizes it; the cascade exploits that the average no longer respects physical-space transport);
  2. the *divergence-free transport* geometry (true $B$ is transport by a divergence-free field; $\tilde B$ keeps divergence-free output but loses the rigid transport identity);
  3. the *exact pressure coupling* via $\mathbb{P}$ (the true Leray projection ties the nonlinearity to an exact elliptic constraint that the averaged symbol only mimics);
  4. some *non-energy monotone quantity* of the true flow that is not monotone for the averaged flow.
- A test any candidate critical coercive quantity must pass (Direction 03): is the candidate also monotone for $\tilde B$? If yes, it is a soft consequence of the shared invariants and is killed by this barrier; it cannot close regularity. Only a quantity whose monotonicity *fails* for the averaged system can possibly work.

**Does not give.**

- **No statement about true Navier-Stokes.** It does not show NS blows up, and it does not show NS is regular. It is agnostic on the Clay problem; it constrains *methods*, not the answer.
- **No identification of which exact feature is decisive.** It proves *some* exact-structure feature must be used, but does not single out which of (1)-(4) is the operative one. Finding that feature is the open problem.
- **No quantitative critical estimate.** Unlike the quantitative-ESS line (Tao 2019), this paper produces no a priori bound for true NS; it is a pure obstruction result.
- **No 2D analog claim.** It does not assert a 2D averaged system blows up; consistency with 2D regularity is part of why the 3D-specific structure is the lesson, not a counterexample to it.

For the program this is the canonical "the soft route is provably closed" theorem. It is load-bearing as a *constraint specification*: it tells BUILDER what a candidate estimate must engage, tells ADVERSARY a concrete falsifier (run the candidate against the averaged system), and tells SYNTHESIZER why Direction 03 is the hardest and highest-value direction.

## Lineage and sharpest known form

**Builds on.**

- **Dyadic / shell models of Navier-Stokes.** N. Katz, N. Pavlovic, "Finite time blow-up for a dyadic model of the Euler equations," Trans. Amer. Math. Soc. 357 (2005), 695-708; S. Friedlander, N. Pavlovic, "Blowup in a three-dimensional vector model for the Euler equations," Comm. Pure Appl. Math. 57 (2004), 705-725; A. Cheskidov, "Blow-up in finite time for the dyadic model of the Navier-Stokes equations," Trans. Amer. Math. Soc. 362 (2010), 5101-5120. These showed shell caricatures can blow up; Tao's advance is keeping a genuine *average of the true bilinear operator* with all three soft invariants.
- **The supercriticality heuristic.** T. Tao, "Why global regularity for Navier-Stokes is hard," blog post (2007), terrytao.wordpress.com. The averaged-NS theorem is the rigorous realization of the program sketched there: build a "blow-up machine" compatible with the energy and scaling and show the soft invariants do not forbid it.
- **Leray (1934)** for the energy inequality and the blow-up rescaling idea (see `leray_1934.md`), and the critical-space local theory (Fujita-Kato $\dot H^{1/2}$, Kato $L^3$, Koch-Tataru $\mathrm{BMO}^{-1}$) that the averaged system shares (see `fujita_kato_1964.md`, `koch_tataru_2001.md`).

**Built on it / related frontier (through 2025).**

- The averaged-NS barrier reframed the regularity program around finding the *exact-structure* input. It directly motivates the quantitative-regularity line that does engage exact structure on the *conditional* side: T. Tao, "Quantitative bounds for critically bounded solutions to the Navier-Stokes equations," arXiv:1908.04958 (2019); in *Nine Mathematical Challenges*, Proc. Sympos. Pure Math. 104, AMS (2021), 149-193. Note these are *different* Tao results: 2016 is the barrier (no NS bound), 2019 is a quantitative refinement of ESS (a genuine NS bound). See `tao_2019_quantitative.md` and do not conflate them.
- **Convex-integration non-uniqueness.** T. Buckmaster, V. Vicol, "Nonuniqueness of weak solutions to the Navier-Stokes equations," Ann. of Math. (2) 189 (2019), 101-144, attacks a different soft boundary (non-uniqueness *below* the energy class) and is partly outside the wrong-approach discipline. Tao 2016 and Buckmaster-Vicol together fence the soft region from two sides: one shows energy+scaling does not give regularity of smooth solutions, the other shows the weak-solution class is too loose to be unique. See `../research_directions/05_convex_integration_boundary.md`.
- **No averaged-NS regularity counter-construction has overturned it.** As of 2025 the barrier stands; the open work is identifying the exact-structure feature, which is precisely Direction 03's mandate and the subject of the "averaged-NS-barrier check" success criterion there.

The frontier reading: Tao 2016 is the rigorous floor under the supercriticality gap. The energy method, even with viscosity and exact scaling, is provably insufficient for an NS-type operator. The proof must add genuinely critical control that engages the exact nonlinearity. That is a compass heading, not a wall: it says where the real argument has to live.

## References

- T. Tao, "Finite time blowup for an averaged three-dimensional Navier-Stokes equation," J. Amer. Math. Soc. 29:3 (2016), 601-674; DOI 10.1090/jams/838; arXiv:1402.0290 (2014).
- T. Tao, "Why global regularity for Navier-Stokes is hard," terrytao.wordpress.com (2007).
- T. Tao, "Quantitative bounds for critically bounded solutions to the Navier-Stokes equations," arXiv:1908.04958 (2019); in *Nine Mathematical Challenges*, Proc. Sympos. Pure Math. 104, AMS (2021), 149-193.
- N. H. Katz, N. Pavlovic, "Finite time blow-up for a dyadic model of the Euler equations," Trans. Amer. Math. Soc. 357 (2005), 695-708.
- S. Friedlander, N. Pavlovic, "Blowup in a three-dimensional vector model for the Euler equations," Comm. Pure Appl. Math. 57 (2004), 705-725.
- A. Cheskidov, "Blow-up in finite time for the dyadic model of the Navier-Stokes equations," Trans. Amer. Math. Soc. 362 (2010), 5101-5120.
- L. Escauriaza, G. A. Seregin, V. Sverak, "$L_{3,\infty}$-solutions of the Navier-Stokes equations and backward uniqueness," Russian Math. Surveys 58:2 (2003), 211-250 (the conditional companion: the critical norm whose boundedness *does* force regularity).
- T. Buckmaster, V. Vicol, "Nonuniqueness of weak solutions to the Navier-Stokes equations," Ann. of Math. (2) 189 (2019), 101-144.

## Cross-links

- Research direction: [`../research_directions/03_supercriticality_gap.md`](../research_directions/03_supercriticality_gap.md) (the primary home of this barrier: any candidate critical quantity must fail to be monotone for the averaged system).
- Research direction: [`../research_directions/04_blowup_and_barriers.md`](../research_directions/04_blowup_and_barriers.md) (the barrier made into a requirement; target item 1).
- Research direction: [`../research_directions/05_convex_integration_boundary.md`](../research_directions/05_convex_integration_boundary.md) (the other soft boundary, fenced from the non-uniqueness side).
- Criticality bookkeeper (the operational form of Control (B) this result grounds): [`../../../experiments/_shared/criticality.py`](../../../experiments/_shared/criticality.py).
- Sibling notes: [`escauriaza_seregin_sverak_2003.md`](escauriaza_seregin_sverak_2003.md) (the critical norm whose control *does* close regularity, the conditional mirror of this barrier), [`tao_2019_quantitative.md`](tao_2019_quantitative.md) (the *different* Tao result: quantitative ESS, a genuine NS bound, not to be confused with this barrier), [`leray_1934.md`](leray_1934.md) (the shared energy inequality and blow-up rescaling), [`koch_tataru_2001.md`](koch_tataru_2001.md) and [`fujita_kato_1964.md`](fujita_kato_1964.md) (the critical-space local theory the averaged system shares).
