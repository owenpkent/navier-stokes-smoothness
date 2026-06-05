# Reading notes: Isett (2018), a proof of Onsager's conjecture

Philip Isett, "A proof of Onsager's conjecture," Annals of Mathematics (2) 188 (2018), 871-963. Context throughout: T. Buckmaster, C. De Lellis, L. Szekelyhidi Jr., V. Vicol, "Onsager's conjecture for admissible weak solutions," Comm. Pure Appl. Math. 72 (2019), 229-274.

> Isett (2018) settles the flexible (constructive) half of Onsager's 1949 conjecture for the incompressible Euler equations: for every exponent $\beta < 1/3$ there exist nontrivial weak solutions $u \in C^\beta_x(\mathbb{T}^3 \times \mathbb{R})$ (Holder, spatially) that do not conserve kinetic energy. The companion Buckmaster-De Lellis-Szekelyhidi-Vicol (2019) makes these solutions admissible, i.e. they strictly dissipate (anomalous dissipation), matching the physical sign of turbulent energy loss. Paired with the rigid half (Constantin-E-Titi 1994: above $1/3$ energy is exactly conserved), this proves the Onsager threshold $\beta = 1/3$ is sharp. This is an Architecture 5 (convex integration) result and it sits deliberately OUTSIDE the project's regularity discipline: it is about the inviscid Euler equation, about rough weak solutions below any energy-coercivity class, and about anomalous dissipation rather than viscous smoothing. Its load-bearing role here is threefold. (1) It is the Euler template whose convex-integration machinery (Mikado flows, the iteration, the geometric lemma) Buckmaster-Vicol (2019) then carried to Navier-Stokes to prove non-uniqueness below Leray-Hopf. (2) It pins the exact regularity floor where "weak solution of the inviscid problem" stops constraining the energy, which is exactly the kind of threshold that disciplines the energy-equality-versus-inequality question that Leray's theory leaves open for NS. (3) It is a clean exhibit of why a purely energy-based argument cannot decide regularity: it builds explicit objects that have finite energy, satisfy the equation weakly, and still leak energy at small scales, so finite energy plus weak form is structurally compatible with small-scale pathology.

## What it proves / Statement

Setting: incompressible Euler on the torus $\mathbb{T}^3 = (\mathbb{R}/2\pi\mathbb{Z})^3$ (or $\mathbb{R}^3$ with decay),
$$\partial_t u + \nabla\cdot(u\otimes u) + \nabla p = 0, \qquad \nabla\cdot u = 0,$$
where $u\otimes u$ is the tensor with entries $u_i u_j$. A weak solution is $u \in C_t L^2_x$ satisfying the equation in the distributional sense against divergence-free test fields, with the pressure recovered from $-\Delta p = \nabla\cdot\nabla\cdot(u\otimes u)$.

**Theorem (Isett 2018, flexible side of Onsager).** For every $\beta < 1/3$ there exists a nonzero weak solution $u \in C^\beta(\mathbb{T}^3 \times \mathbb{R})$ of the incompressible Euler equations, compactly supported in time, hence with kinetic energy $e(t) = \tfrac12\int_{\mathbb{T}^3} |u(x,t)|^2\,dx$ not constant in $t$ (it is $0$ outside the support and positive inside, so energy is created and destroyed). More flexibly, one can prescribe the energy profile: for any smooth target $e:\mathbb{R}\to\mathbb{R}_{>0}$ on a time interval there is a $C^\beta$ Euler flow whose energy equals $e(t)$ there. In particular the solutions are non-unique and dissipate energy on suitable intervals.

Here $C^\beta$ means Holder continuity of exponent $\beta$ in the spatial variables (and at least continuity in time); $\beta < 1/3$ is the full subcritical Holder range. The threshold $\tfrac13$ is the Onsager exponent.

**Theorem (Buckmaster-De Lellis-Szekelyhidi-Vicol 2019, admissible refinement).** For every $\beta < 1/3$ and any strictly decreasing smooth $e(t)$ there exists a weak solution $u\in C^\beta(\mathbb{T}^3\times[0,T])$ of Euler with $\tfrac12\int|u(x,t)|^2\,dx = e(t)$, so the solution is *admissible*: its energy is non-increasing, matching the dissipative sign demanded by physics (a Leray-type energy inequality holds, with strict inequality where $e$ decreases). This removes the artificiality of energy that goes up and down: there exist genuinely dissipative $C^{1/3-}$ Euler flows.

**The rigid counterpart (Constantin-E-Titi 1994), for orientation.** If $u\in L^3_t B^{\beta}_{3,\infty,x}$ (in particular if $u\in C^\beta_x$) is a weak Euler solution with $\beta > 1/3$, then the energy is exactly conserved: $e(t) \equiv e(0)$. The mechanism is a commutator estimate on a mollified equation; the energy flux through scale $\ell$ is bounded by $\ell^{3\beta - 1}\to 0$ as $\ell\to 0$ precisely when $3\beta - 1 > 0$, i.e. $\beta > 1/3$. Onsager (1949) had conjectured exactly this dichotomy. Isett supplies the matching flexibility at and below the threshold, so

$$\boxed{\ \beta = \tfrac13 \ \text{is the sharp regularity threshold for energy conservation in inviscid Euler.}\ }$$

Earlier convex-integration constructions climbed toward $1/3$: De Lellis-Szekelyhidi reached $C^{0}$ and then $C^{1/10-}$; Buckmaster-De Lellis-Szekelyhidi reached $C^{1/5-}$ and an a.e.-in-time $C^{1/3-}$ statement; Isett (2018) is the first to reach the full $C^{1/3-}$ for all times with the energy under control. Numbers in this paragraph are the standard chronology (verify exact intermediate exponents against the cited papers if a precise quotation is needed).

## Method / structure

The proof is a *convex integration* iteration adapted from the differential-inclusion / $h$-principle tradition (Nash-Kuiper isometric embeddings; De Lellis-Szekelyhidi 2009 for Euler). The object iterated is not the Euler equation itself but the **Euler-Reynolds system**.

### 1. The Euler-Reynolds system and the iteration target

A pair $(u_q, p_q, R_q)$ solves the Euler-Reynolds system if
$$\partial_t u_q + \nabla\cdot(u_q\otimes u_q) + \nabla p_q = \nabla\cdot R_q, \qquad \nabla\cdot u_q = 0,$$
with $R_q$ a symmetric trace-free $3\times 3$ tensor (the Reynolds stress) measuring the failure of $u_q$ to solve Euler exactly. The iteration produces a sequence $q = 0,1,2,\dots$ with stresses $\|R_q\|_{C^0} \to 0$ and velocities $u_q \to u$ in $C^\beta$. The limit $u$ has $R_\infty = 0$, hence solves Euler weakly. The whole game is to add a fast oscillation $w_{q+1} = u_{q+1} - u_q$ that cancels the current stress $R_q$ at the cost of a much smaller new stress $R_{q+1}$, while keeping the $C^\beta$ growth of the velocity bounded.

### 2. Two scale parameters and the gain

At step $q$ one fixes a frequency $\lambda_q$ and an amplitude $\delta_q^{1/2}$ with
$$\lambda_q \sim \lambda_0^{(b^q)}, \qquad \delta_q \sim \lambda_q^{-2\beta},$$
for a base frequency $\lambda_0$ and a growth rate $b>1$. The perturbation oscillates at frequency $\lambda_{q+1}$ with amplitude $\delta_{q+1}^{1/2}$. The two governing constraints are: the velocity increment must be Holder-$\beta$-bounded, which forces $\delta_{q+1}^{1/2}\lambda_{q+1}^\beta \lesssim 1$; and the new stress must be smaller than the old, which forces a balance among $\delta_q$, $\delta_{q+1}$, $\lambda_q$, $\lambda_{q+1}$. Working the inequalities out, the construction closes for every $\beta < 1/3$, and the value $1/3$ is exactly where the amplitude-versus-stress budget saturates. The Holder exponent of the limit is therefore not incidental: $1/3$ falls out of the same flux balance that Constantin-E-Titi see from the rigid side.

### 3. Mikado flows: the geometric building block (the key innovation)

The central technical advance of Isett (2018), and the reason it reached the endpoint, is the use of **Mikado flows**. A Mikado flow is a stationary solution of Euler built from a periodic arrangement of straight, disjoint, oscillating *pipe* (jet) structures pointing in finitely many rational directions; "Mikado" is the pick-up-sticks image of thin straight rods. Their defining properties:

- Each Mikado flow is an *exact* stationary Euler solution (it solves $\nabla\cdot(W\otimes W) + \nabla P = 0$ on its own), so plugging it in does not generate a low-frequency error from the principal nonlinear self-interaction.
- The set of available Mikado flows realizes, through their averaged self-correlation tensors $\langle W\otimes W\rangle$, every symmetric tensor in a neighborhood of the identity. This is the *geometric lemma*: the convex-integration freedom needed to cancel an arbitrary positive-definite stress $R_q$ comes from superposing Mikado flows with tunable coefficients $a_I(R_q)$ depending smoothly on $R_q$.
- Because the pipes are disjoint and straight, distinct Mikado directions have *disjoint supports* (after a small spatial shift), so their cross interactions vanish exactly rather than approximately. This removes a whole layer of error terms that plagued the earlier Beltrami-flow constructions and is what let Isett push the exponent to the endpoint.

The perturbation is, schematically,
$$w_{q+1}(x,t) \;=\; \sum_{I} a_I\big(R_q(x,t)\big)\; W_I\!\big(\lambda_{q+1}\,\Phi(x,t)\big),$$
a sum of Mikado profiles $W_I$, oscillating at frequency $\lambda_{q+1}$, with amplitudes set by the geometric lemma to satisfy $\langle w_{q+1}\otimes w_{q+1}\rangle \approx -R_q$ (cancel the stress in average), transported along the coarse flow map $\Phi$ of $u_q$ to keep the construction consistent with advection. A divergence-free corrector restores $\nabla\cdot u_{q+1} = 0$.

### 4. The new stress and the error estimates

Inserting $u_{q+1} = u_q + w_{q+1}$ produces a new stress $R_{q+1}$ that decomposes into transport, Nash, oscillation, and corrector errors. Each is estimated in $C^0$ and in $C^1$ (and via interpolation, in fractional Holder norms) using stationary-phase / non-stationary-phase bounds: high-frequency factors gain inverse powers of $\lambda_{q+1}$, low-frequency factors cost positive powers of $\lambda_q$. The disjoint-support property of Mikado flows kills the most dangerous oscillation error exactly. The outcome is $\|R_{q+1}\|_{C^0} \ll \|R_q\|_{C^0}$ with constants uniform in $q$, and $\sum_q \|w_{q+1}\|_{C^\beta} < \infty$, giving convergence in $C^\beta$. Mollification along the flow (a regularization step, "gluing" in later refinements) controls the loss of derivatives in the transport term.

### 5. Energy control

Because $\langle w_{q+1}\otimes w_{q+1}\rangle$ adds a controllable amount of kinetic energy at each step ($\operatorname{tr}\langle w_{q+1}\otimes w_{q+1}\rangle = |w_{q+1}|^2$ in average), and the high-frequency increments are nearly orthogonal in $L^2$ to the coarse field, one can steer $\int |u_q|^2$ toward a prescribed profile $e(t)$ with errors that vanish as $q\to\infty$. This is the source of the energy-profile flexibility, and in BDSV (2019) the bookkeeping is arranged so that $e(t)$ can be taken strictly decreasing, yielding admissible dissipative solutions.

### Contrast with the NS carry-over (Buckmaster-Vicol 2019)

The same skeleton, with *intermittent* building blocks (concentrated, anisotropic flows with small support, replacing the spatially-spread Beltrami/Mikado profiles) absorbs the viscous term $\nu\Delta u$: intermittency makes the dissipation error of the added high-frequency field controllably small in the relevant norm. That is how the Euler template becomes the NS non-uniqueness theorem (weak solutions in $C_t L^2$, bounded kinetic energy, below Leray-Hopf). The reading note for that result is the headline Architecture 5 NS document; this note is its Euler ancestor. See [`../research_directions/05_convex_integration_boundary.md`](../research_directions/05_convex_integration_boundary.md).

## Criticality placement

The project's scaling is the *Navier-Stokes* scaling $u_\lambda(x,t) = \lambda\,u(\lambda x, \lambda^2 t)$, under which $\dot H^{1/2}(\mathbb{R}^3)$, $L^3$, and $\mathrm{BMO}^{-1}$ are critical and the energy $L^\infty_t L^2_x$ is supercritical. Isett (2018) is an *Euler* (inviscid) result, and Euler is invariant under a one-parameter family of scalings $u_\mu(x,t) = \mu^a u(\mu x, \mu^{a+1} t)$ for any $a$ (no viscosity fixes $a=1$), so the NS criticality scale is not literally the native scale of this paper. Two honest placements are nonetheless exact and load-bearing.

- **The Onsager exponent $1/3$ is a *dimensional-analysis* criticality threshold for energy flux, not for the NS continuation problem.** The energy flux through spatial scale $\ell$ of a $C^\beta$ field scales as $\ell^{3\beta-1}$ (Kolmogorov-Onsager counting: velocity increment $\sim \ell^\beta$, three of them per cubic flux term, one inverse length from the gradient). It is scale invariant exactly at $\beta = 1/3$, dissipative-compatible below, and conservative above. So $1/3$ is *critical for the energy-conservation question*, in the same dimensional sense that $L^3$ is critical for the NS regularity question. Both are the exponent where a relevant flux is exactly scale invariant. Running the criticality bookkeeper on the *energy* shows the same supercriticality moral from the other side: in NS the energy norm $L^\infty_t L^2_x$ is supercritical (negative scaling exponent under $u_\lambda$), and Isett exhibits, in the inviscid sibling, explicit finite-energy fields where that supercriticality is not a bookkeeping artifact but a real escape hatch through which energy leaves the system at small scales.
- **On the NS criticality scale, these objects sit *below* every coercive norm.** A $C^{\beta}_x$ field with $\beta < 1/3$ is not in $\dot H^{1/2}$ in general, is not a mild solution, and is not Leray-Hopf (no $L^2_t \dot H^1_x$ control). Put through `experiments/_shared/criticality.py`, the controlled quantity here is the energy, which returns SUPERCRITICAL; there is no critical-norm control on these solutions at all. They are the explicit witnesses that "supercritical control is compatible with bad small-scale behavior": exactly the worlds the criticality bookkeeper warns a regularity proof must rule out and that energy alone cannot. See [`../research_directions/03_supercriticality_gap.md`](../research_directions/03_supercriticality_gap.md).

The placement, then, is: $1/3$ is the criticality threshold *for the inviscid energy-flux problem*, and it is a structural mirror of the supercriticality gap, not a point on the NS regularity scale. The mirror is the useful object for this repo.

## Against the three controls

Architecture 5 sits *partly outside* the wrong-approach discipline by design. The controls still give a sharp reading; the reading is the point.

- **(A) 2D control: passes by being explicitly 3D-or-2D-agnostic in a non-threatening way.** Onsager flexibility is *not* a regularity argument and does not predict any blow-up of a smooth flow, so it cannot falsely "predict 2D NS blow-up." In fact convex-integration non-conservation exists in 2D Euler as well: there are $C^{1/3-}$ 2D Euler weak solutions that dissipate energy (Choffrut; Buckmaster-De Lellis-Szekelyhidi-Vicol-type constructions extend below 2D Euler). This does *not* contradict the 2D NS smoothness control, because (i) it concerns inviscid Euler, where 2D smooth solutions are also globally smooth but rough weak solutions need not conserve energy, and (ii) it concerns weak solutions below the energy class, not smooth flows. The control reads cleanly: a method that produces non-conservative rough solutions in both 2D and 3D is *not* a regularity method, and Onsager makes no claim that would survive being applied to the smooth 2D problem. The construction never engages vortex stretching $\omega\cdot\nabla u$ as a *mechanism for singularity of a smooth flow*; it engages the nonlinearity only as the algebraic identity to be solved approximately. So (A) is passed in the trivial-but-informative sense: this is correctly outside the regularity discipline.
- **(B) Supercriticality ceiling: this is the exhibit, not a violator.** Control (B) says energy-level information is supercritical and cannot by itself close regularity. Isett (2018) is the cleanest possible demonstration of *why*: it constructs solutions with finite energy that nevertheless lose energy through a small-scale cascade, so finite-energy-plus-weak-form is strictly weaker than energy conservation, and a fortiori than regularity. The Onsager dichotomy is the sharp statement of how much *additional* regularity above the energy class ($C^{1/3}$ Holder) you must assume before the energy is even pinned down, let alone the solution smooth. For the NS program this is the inviscid lower bound on "how far above the energy you must climb to get any rigidity," and it is consistent with the project's spine that the missing ingredient is critical, not energy-level, control.
- **(C) Viscosity / Burgers control: passes, and sharpens it.** This is an *Euler* result. There is no viscosity, and that is the whole point: anomalous dissipation here is *inviscid* dissipation, the energy leaving the resolved scales without any $\nu\Delta u$ term, the conjectural fluid-mechanical content of turbulence in the $\nu\to 0$ limit. This is precisely the regime Control (C) flags as dangerous for a *regularity* claim: a method blind to viscosity is suspect *as a smoothness argument*. Isett is not a smoothness argument, so it does not run afoul of (C); instead it shows the inviscid problem genuinely permits the pathology (energy loss, non-uniqueness) that viscosity is supposed to suppress. The Burgers and Elgindi exhibits in this repo make the same point for shock formation and 3D Euler singularity; Onsager makes it for energy. Together they say: remove or ignore viscosity and the good properties (conservation, uniqueness, smoothness) all fail. The viscous NS analog, Buckmaster-Vicol (2019), recovers non-uniqueness *with* $\nu>0$ but only *below* the Leray-Hopf class, so the viscosity still buys the energy inequality and partial regularity; it just does not buy uniqueness of *every* weak solution.

Net: this note is filed inside Architecture 5 and is, on purpose, outside the regularity discipline. Its function is to be the inviscid exhibit that calibrates Controls (B) and (C) from the boundary of "what counts as a solution," and to be the methodological source of the NS non-uniqueness result.

## What it gives / what it does not give

**Gives.**
- The sharp Onsager threshold $\beta = 1/3$ for inviscid Euler energy conservation, with the flexible side (Isett) matching the rigid side (Constantin-E-Titi). A rare instance of a fluid-mechanical dichotomy proved sharp from both directions.
- The Mikado-flow technology and the disjoint-support geometric lemma, the reusable engine that powers the modern convex-integration program (NS non-uniqueness, transport equations, MHD, SQG, and the admissibility refinements).
- A rigorous existence proof of *anomalous dissipation* solutions: explicit fields that dissipate energy with no viscosity, the long-conjectured mathematical substrate of the turbulent energy cascade and the "zeroth law" of turbulence.
- For this repo specifically: the inviscid lower bound on how much regularity above the energy class is needed for rigidity, and the explicit witnesses that supercritical (energy-level) information cannot exclude small-scale energy loss.

**Does not give.**
- **Nothing about smooth-solution regularity of Navier-Stokes.** It does not construct a singularity of a smooth flow, does not violate the NS energy inequality, and does not bear on the Clay problem's positive resolution. The category error (treating non-uniqueness of rough solutions as smoothness information) is precisely what Direction 05 exists to forbid.
- **No uniqueness or smoothness statement of any kind.** Convex integration produces *many* solutions; it is an $h$-principle (flexibility) result, the opposite of a rigidity/uniqueness theorem.
- **No viscous mechanism.** The dissipation is anomalous (inviscid). The NS carry-over needs the separate intermittency idea and still lands below Leray-Hopf, so it does not threaten the viscous regularity question for smooth data.
- **No control at or above the threshold.** At $\beta \ge 1/3$ the construction does not operate; that regime is governed by the rigid (conservation) side. The endpoint $\beta = 1/3$ itself (closed, not open) is the genuinely hard borderline; Isett gives every $\beta < 1/3$ but not $\beta = 1/3$.

For the program the load-bearing one-line summary is: *Onsager fixes the inviscid regularity floor below which energy conservation, uniqueness, and good behavior all fail, and that floor is a structural mirror of the NS supercriticality gap, not a step toward closing it.*

## Lineage and sharpest known form

**Builds on.**
- L. Onsager, "Statistical hydrodynamics," Nuovo Cimento (Suppl.) 6 (1949), 279-287: the original conjecture of the $1/3$ dichotomy.
- P. Constantin, W. E, E. S. Titi, "Onsager's conjecture on the energy conservation for solutions of Euler's equation," Comm. Math. Phys. 165 (1994), 207-209: the rigid side, energy conservation above $1/3$, via a commutator/flux estimate (also G. L. Eyink 1994 for a Fourier version).
- J. Nash (1954) and N. Kuiper (1955), the $C^1$ isometric embedding theorem and the $h$-principle: the conceptual origin of convex integration.
- C. De Lellis, L. Szekelyhidi Jr., "The Euler equations as a differential inclusion," Ann. of Math. (2) 170 (2009), 1417-1436, and "Dissipative continuous Euler flows," Invent. Math. 193 (2013), 377-407: the import of convex integration into incompressible Euler and the first continuous dissipative flows.
- T. Buckmaster, C. De Lellis, L. Szekelyhidi Jr., the $C^{1/5-}$ and a.e.-in-time $C^{1/3-}$ stages (Comm. Math. Phys. and Invent. Math., 2015-2016): the run-up to the endpoint.

**Built on it / sharpest known forms (through 2025).**
- **T. Buckmaster, C. De Lellis, L. Szekelyhidi Jr., V. Vicol (2019)**, "Onsager's conjecture for admissible weak solutions," Comm. Pure Appl. Math. 72 (2019), 229-274: upgrades Isett's flexibility to *admissible* (strictly dissipative) $C^{1/3-}$ solutions, the physically correct sign. This is the companion source for this note.
- **T. Buckmaster, V. Vicol (2019)**, "Nonuniqueness of weak solutions to the Navier-Stokes equations," Ann. of Math. (2) 189 (2019), 101-144: the Navier-Stokes carry-over via intermittent convex integration; weak solutions in $C_t L^2$ with bounded kinetic energy are non-unique, below the Leray-Hopf class. The headline Architecture 5 NS result; this note is its Euler template.
- **Gluing / sharper Onsager refinements:** P. Isett, "On the endpoint regularity in Onsager's conjecture," arXiv:1706.01549 (and subsequent work), and the De Lellis-Kwon and related programs, address the borderline $\beta = 1/3$ and Holder-with-modulus refinements; the threshold $1/3$ is sharp and the endpoint behavior is the active fine-structure question. (verify exact endpoint statements before quoting.)
- **Beyond Euler:** the Mikado-flow / intermittent machinery now yields non-uniqueness and anomalous-dissipation-type results for the transport equation (Modena-Szekelyhidi), MHD, surface quasi-geostrophic, and hypodissipative NS, and undergirds the *forced* Leray-Hopf non-uniqueness of Albritton-Brue-Colombo (2022) (which, however, uses an instability/self-similar mechanism, not convex integration). See [`necas_ruzicka_sverak_1996.md`](necas_ruzicka_sverak_1996.md) for the self-similar lineage that the Albritton-Brue-Colombo construction touches.

The frontier as of 2025: the inviscid Onsager dichotomy is closed and sharp; the active questions are the exact endpoint $\beta = 1/3$ behavior, the dimension/Hausdorff structure of the dissipation, and how far below Leray-Hopf the *viscous* non-uniqueness reaches (Buckmaster-Vicol is at $C_t L^2$; whether non-uniqueness can be pushed into or excluded from the Leray-Hopf class for *unforced* NS is open and is the live boundary of Architecture 5). None of this moves the smooth-data NS regularity question; it sharpens the solution concept around it.

## References

- P. Isett, "A proof of Onsager's conjecture," Ann. of Math. (2) 188 (2018), 871-963; DOI 10.4007/annals.2018.188.3.4.
- T. Buckmaster, C. De Lellis, L. Szekelyhidi Jr., V. Vicol, "Onsager's conjecture for admissible weak solutions," Comm. Pure Appl. Math. 72 (2019), 229-274.
- L. Onsager, "Statistical hydrodynamics," Nuovo Cimento (Suppl.) 6 (1949), 279-287.
- P. Constantin, W. E, E. S. Titi, "Onsager's conjecture on the energy conservation for solutions of Euler's equation," Comm. Math. Phys. 165 (1994), 207-209.
- C. De Lellis, L. Szekelyhidi Jr., "The Euler equations as a differential inclusion," Ann. of Math. (2) 170 (2009), 1417-1436.
- C. De Lellis, L. Szekelyhidi Jr., "Dissipative continuous Euler flows," Invent. Math. 193 (2013), 377-407.
- T. Buckmaster, V. Vicol, "Nonuniqueness of weak solutions to the Navier-Stokes equations," Ann. of Math. (2) 189 (2019), 101-144.
- T. Buckmaster, V. Vicol, "Convex integration and phenomenologies in turbulence," EMS Surv. Math. Sci. 6 (2019), 173-263 (survey; the orientation reference for the method).
- J. Nash, "C^1 isometric imbeddings," Ann. of Math. (2) 60 (1954), 383-396; N. H. Kuiper, "On C^1-isometric imbeddings," Indag. Math. 17 (1955), 545-556 and 683-689.
- G. L. Eyink, "Energy dissipation without viscosity in ideal hydrodynamics. I. Fourier analysis and local energy transfer," Phys. D 78 (1994), 222-240.

## Cross-links

- Research direction: [`../research_directions/05_convex_integration_boundary.md`](../research_directions/05_convex_integration_boundary.md) (primary home; this note is the Euler template that Buckmaster-Vicol carried to NS, and the exhibit that convex integration is outside the regularity discipline).
- Research direction: [`../research_directions/03_supercriticality_gap.md`](../research_directions/03_supercriticality_gap.md) (the Onsager $1/3$ flux threshold as a structural mirror of the energy supercriticality gap; finite-energy fields that still leak energy).
- Research direction: [`../research_directions/04_blowup_and_barriers.md`](../research_directions/04_blowup_and_barriers.md) (anomalous dissipation and inviscid pathology as a sibling barrier to the Euler-singularity work; the viscosity control from the inviscid side).
- Sibling notes: [`tao_2016_averaged.md`](tao_2016_averaged.md) (the contrasting NS *barrier*: an averaged NS that keeps the energy identity and scaling yet blows up; complements the Onsager exhibit that energy plus weak form is too weak), [`necas_ruzicka_sverak_1996.md`](necas_ruzicka_sverak_1996.md) (the self-similar lineage touched by the forced Leray-Hopf non-uniqueness that descends from this machinery), [`leray_1934.md`](leray_1934.md) (the energy *inequality* whose equality-versus-inequality status is exactly what the Onsager threshold governs on the inviscid side), [`escauriaza_seregin_sverak_2003.md`](escauriaza_seregin_sverak_2003.md) (the viscous, critical-norm rigidity result that is the methodological opposite of this flexible inviscid construction).
