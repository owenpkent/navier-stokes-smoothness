# Reading notes: Buckmaster-Vicol (2019), non-uniqueness via convex integration

Tristan Buckmaster, Vladimir Vicol, "Nonuniqueness of weak solutions to the Navier-Stokes equations," Annals of Mathematics (2) 189:1 (2019), 101-144. DOI 10.4007/annals.2019.189.1.3. (Preprint: arXiv:1709.10033, 2017.)

> This is the headline result of Architecture 5. It proves that the notion "weak solution of 3D Navier-Stokes with finite kinetic energy" is, by itself, too loose to single out a unique flow: distinct such solutions can share the same initial data, and one can even prescribe an arbitrary smooth (non-monotone, energy-increasing) kinetic energy profile. The mechanism is intermittent convex integration, a viscous adaptation of the Nash-Kuiper / De Lellis-Szekelyhidi-Isett scheme that settled the flexible side of the Onsager conjecture for Euler. The load-bearing point for this project is a delimiting one, not a regularity one. The solutions produced live in $C_t H^\beta$ with $\beta>0$ small, below the Leray-Hopf regularity, and they do not satisfy the energy inequality. So they do not contradict the smooth-flow regularity program at all. What they do is pin the exact class in which any future uniqueness theorem could hold: uniqueness is false in $C_t L^2$, so the Leray-Hopf class (with the energy inequality, $L^\infty_t L^2_x \cap L^2_t \dot H^1_x$) is not an arbitrary convenience but the correct floor. This is why CLAUDE.md places Architecture 5 partly OUTSIDE the three structural controls: it is about the boundary of what "solution" means, not about whether the smooth flow stays smooth.

## What it proves

Work on the periodic torus $\mathbb{T}^3 = \mathbb{R}^3 / (2\pi\mathbb{Z})^3$, with viscosity normalized to $\nu=1$, for the incompressible Navier-Stokes system
$$\partial_t v + \operatorname{div}(v\otimes v) - \Delta v + \nabla p = 0, \qquad \nabla\cdot v = 0.$$
A weak solution here means a divergence-free $v \in C([0,T]; L^2(\mathbb{T}^3))$ that solves the system in the sense of distributions (tested against divergence-free test fields, so the pressure is recovered by the Leray projection and need not appear). This is strictly weaker than the Leray-Hopf class: no energy inequality is imposed, and no $L^2_t \dot H^1_x$ dissipation bound is required.

**Theorem 1.2 (prescribed energy profile).** There exists $\beta > 0$ such that the following holds. Let $e:[0,T]\to (0,\infty)$ be any smooth, strictly positive function. Then there exists a weak solution
$$v \in C\big([0,T]; H^\beta(\mathbb{T}^3)\big), \qquad \nabla\cdot v = 0,$$
of the Navier-Stokes equations whose kinetic energy realizes the prescribed profile exactly:
$$\int_{\mathbb{T}^3} |v(x,t)|^2 \, dx = e(t) \qquad \text{for all } t\in[0,T].$$

**Theorem 1.1 (non-uniqueness corollary).** Weak solutions of 3D Navier-Stokes in the class $C([0,T]; L^2(\mathbb{T}^3))$ are not unique. Concretely, there exist two weak solutions $v_1 \neq v_2$ with the same initial datum $v_1(\cdot,0) = v_2(\cdot,0)$. (Take two distinct energy profiles agreeing at $t=0$, or compare a convex-integration solution against the zero solution by choosing $e$ with $e(0)=0$ small; the constructed $v$ is not identically the Leray-Hopf solution issuing from its own data.)

Two structural consequences recorded in the paper:

- The constructed $v$ does **not** satisfy the energy inequality. Indeed for a profile $e(t)$ that is increasing somewhere, $\tfrac12 e(t)$ exceeds $\tfrac12 e(0)$, which is impossible for a Leray-Hopf solution (whose energy is non-increasing for the unforced equation). So these are genuinely **non-Leray-Hopf** objects.
- (Vanishing-viscosity link.) The scheme produces, in the inviscid limit, dissipative Holder-continuous weak solutions of 3D Euler as a strong $L^2$ limit of finite-energy Navier-Stokes weak solutions, tying the construction to the Onsager flexibility results.

### What "small $\beta$" means and why it is not improvable to Leray-Hopf here

The regularity is $v \in C_t H^\beta_x$ for some explicit but small $\beta > 0$ (the paper does not optimize $\beta$; it is a fixed small number coming from the iteration parameters). This is far below the Leray-Hopf regularity $L^\infty_t L^2_x \cap L^2_t \dot H^1_x$, i.e. below $\dot H^1$ in space on average in time. The gap between $H^\beta$ ($\beta$ small) and $\dot H^1$ is exactly the room in which convex integration operates. Closing that gap (reaching the energy class) is not possible with this construction and is the subject of the lineage discussion below (Onsager-type thresholds for NS).

## Method / structure

The proof is an iteration: a **convex-integration scheme** adapted from Euler (De Lellis-Szekelyhidi, Isett) to the viscous setting by making the building blocks **intermittent**. The object iterated is not the velocity alone but a velocity-stress pair.

### The Reynolds-stress relaxation

One solves the Navier-Stokes-Reynolds system at each stage $q\in\mathbb{N}$:
$$\partial_t v_q + \operatorname{div}(v_q\otimes v_q) - \Delta v_q + \nabla p_q = \operatorname{div}\, \mathring R_q, \qquad \nabla\cdot v_q = 0,$$
where $\mathring R_q$ is a symmetric traceless "Reynolds stress" measuring the failure of $v_q$ to solve NS. The goal is to drive $\mathring R_q \to 0$ in $L^1$ while keeping $v_q$ convergent in $C_t H^\beta$. If $\mathring R_q \to 0$ then the limit $v = \lim_q v_q$ is an exact weak solution.

### The inductive estimates

The iteration is controlled by two scalar parameters per stage: a frequency $\lambda_q$ (growing super-exponentially, $\lambda_{q+1}\approx \lambda_q^{b}$ with $b>1$) and an amplitude $\delta_q$ (decaying). The inductive hypotheses are, schematically,
$$\|v_q\|_{L^2} \ \text{tracks } e(t)^{1/2}, \qquad \|v_q\|_{C^1_{x,t}} \lesssim \lambda_q^{\,?}, \qquad \|\mathring R_q\|_{L^1} \lesssim \delta_{q+1}.$$
One adds a perturbation $w_{q+1} = v_{q+1}-v_q$, highly oscillatory at frequency $\sim \lambda_{q+1}$, designed so that its self-interaction $w_{q+1}\otimes w_{q+1}$ cancels the old stress $\mathring R_q$ to leading order (a low-frequency / high-frequency split), leaving a new, smaller stress $\mathring R_{q+1}$.

### Intermittent Beltrami flows (the building blocks)

For Euler/Onsager the perturbations are **Beltrami flows**: eigenfunctions of curl, $\nabla\times W = \lambda W$, which are stationary Euler solutions and supply the algebraic identity needed to cancel a prescribed symmetric stress via the geometric lemma (any positive-definite symmetric matrix is a convex combination of squared Beltrami modes). These are space-filling (every Fourier mode has $|\hat W|\sim 1$), so they have $\|W\|_{L^p}\sim 1$ uniformly in $p$, i.e. **no intermittency**.

The viscous obstruction is the dissipation term $-\Delta w_{q+1}$, which costs $\lambda_{q+1}^2 \delta_{q+1}^{1/2}$ in $L^2$. A space-filling Beltrami perturbation cannot pay this cost while keeping amplitudes small. The Buckmaster-Vicol innovation is the **intermittent Beltrami flow**: take a Beltrami flow, then concentrate it onto a sparse set in space (a periodic lattice of small thickened tubes/cubes), so that the building block has
$$\|W\|_{L^2}\sim 1, \qquad \|W\|_{L^p}\ \text{growing in } p \ (\text{large } L^p / L^2 \text{ ratio}),$$
which is exactly **intermittency** (a few high spots rather than uniform filling). Concentrating onto a fraction of the volume lets the high derivative cost of $-\Delta$ be absorbed at the price of large but localized $L^p$ norms, while $L^2$ (the energy) stays $O(1)$. The intermittency dimension is tuned so the viscous term is subordinate to the nonlinear cancellation in the relevant norms.

### The energy-profile control

Because the perturbation's $L^2$ mass is set by the chosen amplitudes, one feeds the target profile $e(t)$ into the amplitude schedule at each stage. The leading-order $L^2$ of $v_q$ is forced to track $e(t)^{1/2}$, and the convergence is arranged so the limit hits $\int|v|^2 = e(t)$ exactly. The freedom to prescribe $e$, including making it increase, is what produces a non-Leray-Hopf solution and hence non-uniqueness against the (energy-non-increasing) Leray-Hopf solution.

### Where the Leray projector and divergence-free structure enter

The incompressibility constraint $\nabla\cdot v = 0$ is maintained by building $w_{q+1}$ from divergence-free Beltrami modes and correcting with small divergence-free correctors. The pressure $p_q$ is slaved to $v_q$ and $\mathring R_q$ by the Leray projection $\mathbb{P}$ and never needs to be tracked independently. There is no use of the energy identity as a coercive control; on the contrary, the construction violates the energy inequality on purpose.

## Criticality placement

Under the Navier-Stokes scaling $u_\lambda(x,t)=\lambda\,u(\lambda x,\lambda^2 t)$:

- The energy $\|v(\cdot,t)\|_{L^2}^2$ scales as $\lambda^{-1}$, so $L^\infty_t L^2_x$ is **supercritical** (scaling exponent $-1$ on the squared norm; $-1/2$ on the norm). This is the same supercritical energy the project's criticality bookkeeper flags. The whole construction lives at and below this supercritical energy level.
- The space $\dot H^{1/2}(\mathbb{R}^3)$ is **critical** (scaling exponent $0$). The constructed solutions sit in $H^\beta$ with $\beta$ small, hence in $\dot H^\beta$ with $\beta < 1/2$: they are **below critical** (sub-critical in regularity, i.e. rougher than the critical Sobolev scale, which under the scaling makes the relevant homogeneous norm supercritical). In the project's bookkeeping a regularity index below $1/2$ corresponds to a norm that scales with a negative exponent, the same side of the line as the energy.
- The Onsager-type heuristic exponent for NS intermittent convex integration sits well under the Leray-Hopf threshold; in particular under $\dot H^{1/2}$. The construction cannot be pushed up to the critical space by this method.

The criticality reading is therefore the mirror image of a regularity theorem. A conditional criterion (ESS, Prodi-Serrin) buys regularity by controlling a **critical** norm ($L^\infty_t L^3_x$, $L^p_t L^q_x$ on the line $2/p+3/q=1$). Convex integration produces pathology precisely **below** that critical scale, where no scale-invariant norm is controlled. The two phenomena are separated by the critical line, and that separation is the structural content for this project. Run $L^2$ and $\dot H^\beta$ ($\beta<1/2$) through `experiments/_shared/criticality.py`: both return negative scaling exponents (SUPERCRITICAL / below-critical), confirming these objects live strictly below the critical regularity at which uniqueness might be recoverable. See [`../research_directions/03_supercriticality_gap.md`](../research_directions/03_supercriticality_gap.md).

## Against the three controls

Architecture 5 sits partly OUTSIDE the wrong-approach discipline by design: it is not a regularity argument, so passing or failing the controls is not the right test. Still, the audit is informative.

- **(A) 2D control (must stay smooth, genuine 3D structure).** The construction is genuinely 3D: Beltrami flows are eigenfunctions of curl, which is a 3D operator (in 2D there is no nontrivial Beltrami field of this kind), and the geometric lemma uses the full $3\times 3$ symmetric-matrix decomposition. It does **not** falsely predict 2D blow-up, because it does not predict blow-up at all; it produces bounded-energy non-unique weak solutions, not singularities. Note the contrast with the regularity discipline: the worry that a method "would equally apply in 2D" is about singularity formation, and here there is no singularity. (For completeness: 2D Euler weak solutions are also non-unique below regularity by related convex-integration work, but 2D NS smoothness of the strong flow is untouched.)
- **(B) Criticality / energy-supercritical.** The method does not even try to control a critical norm; it lives below the energy class. So it trivially "is supercritical," but as a construction of pathology that is the point, not a defect. It confirms Control (B) from the other side: at and below the supercritical energy level there is genuinely no uniqueness, so an energy-level statement cannot be a regularity statement. This is the sharpest possible illustration of the supercriticality gap.
- **(C) Viscosity / exact NS structure.** Here the result is interesting. The viscous term $-\Delta$ is precisely what forces the move from space-filling Beltrami flows (Euler) to **intermittent** ones (NS). So the construction is **not blind to viscosity**: it confronts the dissipation head-on and pays for it with intermittency. The vanishing-viscosity limit recovers dissipative Holder Euler solutions, tying viscous non-uniqueness to the inviscid Onsager picture. Viscosity changes the building blocks but does not restore uniqueness at this low regularity. This is the one control the result engages substantively, and it engages it correctly.

Net placement: this is a boundary-of-solution-concept result. It does not enter the regularity discipline; it defines the floor (the Leray-Hopf class) below which the discipline's central object (a unique smooth flow) is not even singled out.

## What it gives / what it does not give

**Gives.**
- A rigorous proof that finite-energy weak solutions of 3D NS are non-unique, with the same initial data.
- The strongest possible form: arbitrary smooth (including increasing) energy profiles are realizable, so the failure of uniqueness is not a borderline measure-zero accident but a robust flexibility.
- A clean justification of the Leray-Hopf class: the energy inequality is the feature these pathological solutions lack, so requiring it is exactly what one must add to have any hope of uniqueness.
- A new tool (intermittent Beltrami flows) that has since organized a whole sub-field (hypodissipative NS, transport equations, MHD, SQG, the Onsager problem for higher regularity).

**Does not give.**
- It does **not** construct a singularity of a smooth NS flow. The constructed solutions are not smooth; they are $C_t H^\beta$ with $\beta$ small. Nothing here bears on whether smooth data yields a smooth solution for all time. This is the category error the project explicitly guards against.
- It does **not** establish non-uniqueness in the Leray-Hopf class for the unforced equation. These solutions are not Leray-Hopf. (Non-uniqueness inside the Leray-Hopf class is known only with a force: Albritton-Brue-Colombo 2022, by a different, non-convex-integration mechanism.)
- It does **not** reach the critical regularity $\dot H^{1/2}$ or any critical norm. There remains a gap between the regularity of the constructed solutions and the conjectured threshold at which uniqueness could be restored; locating that threshold sharply for NS is open.
- It says nothing about the smooth-flow regularity question other than "do not look here": the regularity program lives above the critical line; this construction lives below the energy line. They are kept in separate regimes.

## Lineage and sharpest known form

**Builds on.**
- C. De Lellis, L. Szekelyhidi Jr., "The Euler equations as a differential inclusion," Ann. of Math. (2) 170 (2009), 1417-1436: convex integration / differential inclusion for incompressible Euler. The conceptual root.
- The Nash-Kuiper $C^1$ isometric embedding theorem (Nash 1954, Kuiper 1955): the original "flexibility from high-frequency corrugation" template, transported to fluids by Szekelyhidi and collaborators.
- P. Isett, "A proof of Onsager's conjecture," Ann. of Math. (2) 188 (2018), 871-963; and T. Buckmaster, C. De Lellis, L. Szekelyhidi Jr., V. Vicol, "Onsager's conjecture for admissible weak solutions," Comm. Pure Appl. Math. 72 (2019), 229-274: the $C^{1/3-}$ Euler constructions whose machinery (Beltrami building blocks, the geometric lemma, Mikado-type concentration) Buckmaster-Vicol adapt. Isett's proof and the Mikado-flow refinement are the immediate methodological parents.

**Built on it.**
- T. Buckmaster, M. Colombo, V. Vicol, "Wild solutions of the Navier-Stokes equations whose singular sets in time have Hausdorff dimension strictly less than 1," J. Eur. Math. Soc. 24 (2022), 3333-3378: sharpens the non-uniqueness so the solutions are smooth off a small (Hausdorff dimension $<1$ in time) singular set, connecting to the CKN partial-regularity scale.
- D. Albritton, E. Brue, M. Colombo, "Non-uniqueness of Leray solutions of the forced Navier-Stokes equations," Ann. of Math. (2) 196 (2022), 415-455: pushes non-uniqueness into the **Leray-Hopf** class itself, but only for **forced** NS, via a self-similar instability (Jia-Sverak scenario), not convex integration. This is the natural next target the present paper leaves open for the unforced equation.
- A large family of "intermittent convex integration" results: hypodissipative NS (where the dissipation exponent is lowered and the method reaches the energy class), transport/continuity equations (Modena-Szekelyhidi), SQG, MHD, and stationary/time-discontinuous NS solutions. The intermittent Beltrami flow is the reusable engine.

**Sharpest known form as of 2025.**
- For unforced 3D NS, the strongest non-uniqueness remains at the level of finite-energy weak solutions below Leray-Hopf (this paper, refined by Buckmaster-Colombo-Vicol on the time-singular-set dimension). Non-uniqueness of unforced Leray-Hopf solutions is still open.
- For forced 3D NS, Albritton-Brue-Colombo (2022) is the sharpest: two distinct Leray-Hopf solutions for one forced datum.
- The conjectured uniqueness threshold (an NS analog of the Ladyzhenskaya-Prodi-Serrin / Onsager line) is not pinned down: there is a gap between the $H^\beta$ ($\beta$ small) regularity reached by these constructions and the critical $\dot H^{1/2}$ / $L^3$ scale where uniqueness criteria live. (verify: the precise current best $\beta$ and the sharpest hypodissipative exponent.)

## References

- T. Buckmaster, V. Vicol, "Nonuniqueness of weak solutions to the Navier-Stokes equations," Ann. of Math. (2) 189:1 (2019), 101-144. DOI 10.4007/annals.2019.189.1.3. Preprint arXiv:1709.10033. ([Annals page](https://annals.math.princeton.edu/2019/189-1/p03); [arXiv](https://arxiv.org/abs/1709.10033); [author PDF](https://cims.nyu.edu/~vicol/BV1.pdf))
- C. De Lellis, L. Szekelyhidi Jr., "The Euler equations as a differential inclusion," Ann. of Math. (2) 170 (2009), 1417-1436.
- P. Isett, "A proof of Onsager's conjecture," Ann. of Math. (2) 188 (2018), 871-963.
- T. Buckmaster, C. De Lellis, L. Szekelyhidi Jr., V. Vicol, "Onsager's conjecture for admissible weak solutions," Comm. Pure Appl. Math. 72 (2019), 229-274.
- T. Buckmaster, M. Colombo, V. Vicol, "Wild solutions of the Navier-Stokes equations whose singular sets in time have Hausdorff dimension strictly less than 1," J. Eur. Math. Soc. 24 (2022), 3333-3378.
- D. Albritton, E. Brue, M. Colombo, "Non-uniqueness of Leray solutions of the forced Navier-Stokes equations," Ann. of Math. (2) 196 (2022), 415-455.
- T. Buckmaster, V. Vicol, "Convex integration and phenomenologies in turbulence," EMS Surv. Math. Sci. 6 (2019), 173-263. (The survey companion. [author PDF](https://cims.nyu.edu/~vicol/BV2.pdf))

## Cross-links

- Direction file: [`../research_directions/05_convex_integration_boundary.md`](../research_directions/05_convex_integration_boundary.md). This note is the primary source reading behind that direction's "what the results say / what they do not say" split.
- The supercriticality reading: [`../research_directions/03_supercriticality_gap.md`](../research_directions/03_supercriticality_gap.md). Non-uniqueness below the energy class is the sharpest demonstration that the supercritical energy level cannot single out a unique flow.
- Sibling note on the same architecture's forced analog and the self-similar instability mechanism: [`necas_ruzicka_sverak_1996.md`](necas_ruzicka_sverak_1996.md) (self-similar exclusion in $L^3$, the regularity-side counterpart) and the Jia-Sverak forward self-similar context in the references index.
- Contrast with the regularity-side endpoint: [`escauriaza_seregin_sverak_2003.md`](escauriaza_seregin_sverak_2003.md). ESS buys regularity from control of the critical $L^\infty_t L^3_x$ norm; Buckmaster-Vicol produces non-uniqueness strictly below that critical scale. The two results bracket the critical line from opposite sides.
- The barrier-result sibling on the regularity side: [`tao_2016_averaged.md`](tao_2016_averaged.md). Tao shows energy-plus-scaling cannot rule out blow-up; Buckmaster-Vicol shows energy-class membership alone cannot rule out non-uniqueness. Both are "the energy level is not enough" results aimed at different questions.

## What this enables / what remains open

**Enables (for BUILDER, ADVERSARY, SYNTHESIZER).**
- A firm statement, citable at the lemma level, that any uniqueness theorem for unforced 3D NS must assume at least the Leray-Hopf structure (energy inequality), since $C_t L^2$ alone admits non-unique solutions (Theorem 1.1). BUILDER should not propose uniqueness or regularity criteria that would also have to hold for these $C_t H^\beta$ objects.
- A clear regime separation: ADVERSARY can use this to reject any candidate "regularity" argument that would inadvertently constrain sub-critical / below-energy weak solutions, since those are provably wild.
- The intermittency-vs-Onsager picture as a quantitative landmark: the constructed regularity $H^\beta$ ($\beta$ small) versus the critical $\dot H^{1/2}$ marks the width of the flexibility window.

**Remains open.**
- Non-uniqueness of **unforced** Leray-Hopf solutions (the construction here is non-Leray-Hopf; Albritton-Brue-Colombo needs a force).
- The sharp NS uniqueness threshold: an analog of the Onsager / Ladyzhenskaya-Prodi-Serrin line below which non-uniqueness holds and above which uniqueness holds. The gap between $H^\beta$ and $\dot H^{1/2}$ is not closed.
- Whether intermittent convex integration can be pushed to the energy class for the **full-dissipation** ($-\Delta$) equation (it reaches the energy class only in the hypodissipative regime). (verify: current best exponents.)
- Nothing here advances or obstructs the smooth-flow regularity question; that program is conducted entirely above the critical line and is untouched by this construction.
