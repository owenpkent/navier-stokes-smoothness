# Reading notes: Fefferman, the official Clay problem statement (2000)

Charles L. Fefferman, "Existence and smoothness of the Navier-Stokes equation," official problem description for the Clay Mathematics Institute Millennium Prize Problems, 2000 (PDF revised circa 2006). Collected in J. Carlson, A. Jaffe, A. Wiles (eds.), *The Millennium Prize Problems*, Clay Mathematics Institute / American Mathematical Society, 2006.

> This is not a theorem; it is the contract. Fefferman's note is the precise legal-mathematical specification of the target the whole project aims at: what counts as the equation, what counts as initial data, what counts as a solution, and what counts as a proof. It is load-bearing because every result in the repo is graded against it. The note fixes the function-space setting (finite-energy, Schwartz-class data, smooth solutions), it names the two acceptable verdicts (global smoothness or finite-time breakdown), and it offers the choice of domain ($\mathbb{R}^3$ with rapid decay, or the torus $\mathbb{T}^3$). It engages all three structural controls at once, because it is the document that draws the line the controls are calibrated against: 2D is solved, 3D sits between short-time smoothness and global weak existence, and the only all-time a priori bound (energy) is supercritical. This note is the spec for Architectures 1 through 4; it deliberately does not require uniqueness, which is where Architecture 5 (convex integration) lives just outside the frame.

## Statement

The note fixes the 3D incompressible Navier-Stokes system with constant kinematic viscosity $\nu > 0$ on the time interval $t \ge 0$:

$$\partial_t u_i + \sum_{j=1}^{3} u_j\,\partial_{x_j} u_i \;=\; \nu\,\Delta u_i \;-\; \partial_{x_i} p \;+\; f_i(x,t), \qquad i = 1,2,3,$$

$$\nabla\cdot u \;=\; \sum_{i=1}^{3} \partial_{x_i} u_i \;=\; 0, \qquad u(x,0) = u^{\circ}(x),$$

where $u(x,t) = (u_1,u_2,u_3)$ is the velocity, $p(x,t)$ the pressure, $f(x,t)$ an externally applied force, and $u^{\circ}$ a given divergence-free initial velocity. The unknowns are $u$ and $p$; $\nu$ and $f$ are data. The convective term $(u\cdot\nabla)u$ and the pressure gradient $\nabla p$ are the nonlinearity; $\nu\Delta u$ is the dissipation. The pressure is not independent: taking the divergence of the momentum equation and using $\nabla\cdot u = 0$ gives $-\Delta p = \sum_{i,j}\partial_{x_i}\partial_{x_j}(u_i u_j) - \nabla\cdot f$, so $p$ is recovered from $u$ (and $f$) by a nonlocal elliptic solve. This is the analytic content of the Leray projector $\mathbb{P}$ onto divergence-free fields: the genuine evolution is $\partial_t u = \mathbb{P}(\nu\Delta u - (u\cdot\nabla)u + f)$, with the pressure absorbed.

**Hypotheses on the data (the whole-space case).** The initial velocity $u^{\circ}$ is $C^\infty$, divergence-free, and rapidly decreasing in the Schwartz sense: for every multi-index $\alpha$ and every $K \ge 0$ there is a constant $C_{\alpha,K}$ with

$$\big|\partial_x^\alpha\, u^{\circ}(x)\big| \;\le\; C_{\alpha,K}\,(1+|x|)^{-K}, \qquad x\in\mathbb{R}^3.$$

The force is either absent ($f \equiv 0$, the canonical case) or itself smooth and rapidly decreasing, with a joint bound $|\partial_x^\alpha \partial_t^m f(x,t)| \le C_{\alpha,m,K}(1+|x|+t)^{-K}$. This decay is exactly enough to make the energy finite and the elliptic pressure solve well posed, and it removes any contribution from spatial infinity.

**Definition of an acceptable (physically reasonable) solution.** A pair $(p,u)$ is acceptable if

$$p,\;u \;\in\; C^\infty(\mathbb{R}^3\times[0,\infty)),$$

the equations and the divergence-free constraint hold pointwise everywhere on $\mathbb{R}^3\times[0,\infty)$, and the energy is bounded uniformly in time:

$$\sup_{t\ge 0}\;\int_{\mathbb{R}^3} |u(x,t)|^2 \,dx \;<\; \infty. \tag{bounded energy}$$

The bounded-energy clause is structurally important. Without it the note remarks that uninteresting nonphysical solutions can be manufactured by adding a spatially uniform $t$-dependent drift; the finite-energy requirement excludes those and pins the problem to the physically meaningful class. Smoothness ($u\in C^\infty$) and bounded energy together are the definition of "no blow-up."

**The four targets.** A prize is awarded for a complete proof of any one of:

- **(A) Existence and smoothness on $\mathbb{R}^3$.** Take $\nu > 0$, $f \equiv 0$, and any Schwartz-class divergence-free $u^{\circ}$. Prove there exist $p,u\in C^\infty(\mathbb{R}^3\times[0,\infty))$ solving the system with bounded energy.
- **(B) Existence and smoothness on $\mathbb{T}^3$.** The periodic analog. Data $u^{\circ}$ and force $f$ are $C^\infty$ and $\mathbb{Z}^3$-periodic in $x$ (no decay condition needed, the torus is compact); prove a global smooth solution exists. Bounded energy is automatic on the torus since $\int_{\mathbb{T}^3}|u|^2$ is finite for any continuous $u$.
- **(C) Breakdown on $\mathbb{R}^3$.** Exhibit $\nu>0$ and a smooth, divergence-free, Schwartz-class $u^{\circ}$ (and a smooth rapidly-decreasing $f$ is permitted) for which there is no solution of class (A): no global-in-time smooth finite-energy solution exists.
- **(D) Breakdown on $\mathbb{T}^3$.** The periodic analog of (C).

The canonical regularity targets are (A) and (B): global existence and smoothness with no forcing. A proof of (C) or (D) would resolve the problem by exhibiting a genuine finite-time singularity. Note the deliberate asymmetry: the breakdown targets (C), (D) explicitly allow a forcing $f$, whereas the cleanest reading of the existence targets is the unforced one. The note's wording ("Take $\nu > 0$ and $f \equiv 0$") makes the unforced case the headline for (A)/(B), while admitting forced breakdown for (C)/(D).

**Scaling of every object in the statement.** Under the Navier-Stokes scaling symmetry $u_\lambda(x,t)=\lambda\,u(\lambda x,\lambda^2 t)$, $p_\lambda(x,t)=\lambda^2\,p(\lambda x,\lambda^2 t)$ (with $f$ rescaling as $f_\lambda = \lambda^3 f(\lambda x,\lambda^2 t)$), the system is invariant. The energy norm in the bounded-energy clause scales as $\|u_\lambda(t)\|_{L^2(\mathbb{R}^3)} = \lambda^{-1/2}\|u\|_{L^2}$: exponent $a = 1 - d/q = 1 - 3/2 = -1/2 < 0$, **supercritical**. That the problem's own definition of "no blow-up" is phrased through a supercritical quantity is the single most important structural fact in the note, and it is the reason the energy method alone cannot reach the target. See the criticality placement below.

## Method / structure

There is no proof here; the note's "method" is the careful framing, and three framing choices carry the mathematical weight.

- **Why finite energy is the natural class.** The only a priori bound that survives for all time is the energy inequality. Multiplying the momentum equation by $u$ and integrating (the energy identity) gives, formally,
  $$\tfrac12\frac{d}{dt}\int |u|^2 \,dx \;+\; \nu\int |\nabla u|^2\,dx \;=\; \int f\cdot u\,dx,$$
  because the convective term $\int (u\cdot\nabla)u\cdot u = \tfrac12\int u\cdot\nabla|u|^2 = 0$ by $\nabla\cdot u = 0$, and $\int \nabla p\cdot u = -\int p\,\nabla\cdot u = 0$. With $f\equiv 0$ this yields the global bound $\tfrac12\|u(t)\|_2^2 + \nu\int_0^t\|\nabla u\|_2^2 \le \tfrac12\|u^{\circ}\|_2^2$. The note's bounded-energy clause is exactly the quantity this identity controls, which is why the definition of "acceptable solution" is built around it. The pressure and the divergence-free constraint are what make the two structural cancellations (transport conserves energy, pressure does no work) hold.

- **Why smoothness is the right notion of regularity.** The note asks for $C^\infty$, but by parabolic smoothing for the Navier-Stokes system this is equivalent to far weaker conditions: a solution that stays bounded in any subcritical norm, or in a critical norm by the deeper continuation theorems, is automatically $C^\infty$ in the interior. So "$u\in C^\infty$" is a clean stand-in for "the solution does not lose regularity," and the real question is whether any norm strong enough to force smoothness can blow up in finite time. This is where Architecture 2 (continuation criteria: Beale-Kato-Majda, Prodi-Serrin-Ladyzhenskaya, Escauriaza-Seregin-Sverak) enters: each gives a specific norm whose finiteness implies smoothness.

- **Why both $\mathbb{R}^3$ and $\mathbb{T}^3$ are offered.** The two domains isolate different difficulties, and the note offers either so that a solver may pick the cleaner setting. On $\mathbb{T}^3$ there is no decay bookkeeping, no behavior at spatial infinity, the energy is automatically finite, and Fourier-series / pseudo-spectral analysis is exact; the cost is that the zero mode (mean flow) must be handled (the note typically also normalizes $\int_{\mathbb{T}^3} u^{\circ} = 0$). On $\mathbb{R}^3$ the Schwartz decay makes the Leray projector and the heat semigroup act cleanly via the Fourier transform and the Oseen kernel, the scaling symmetry acts without a length scale, and self-similar analysis (Architecture 4) is natural; the cost is decay bookkeeping. Crucially, the regularity question is believed to be domain-independent in its essence: blow-up is a small-scale, local phenomenon (the singular set is expected to be a point in space-time), so whether the far field is periodic or decaying does not change whether a singularity can form. Offering both is a convenience, not two genuinely different problems. The repo's experiments run on $\mathbb{T}^3$ for exactly the spectral-exactness reason.

## Criticality placement

The note's definition of an acceptable solution is anchored to the bounded-energy quantity $\sup_t \int_{\mathbb{R}^3}|u|^2\,dx$. Run this and the other norms named across the four targets through the criticality bookkeeper (`experiments/_shared/criticality.py`), which reports the exponent $a$ in $\|u_\lambda\|_X = \lambda^a\|u\|_X$ and classifies $a>0$ subcritical, $a=0$ critical, $a<0$ supercritical:

| Quantity in the note | Where it appears | Exponent $a$ ($d=3$) | Class |
|---|---|---|---|
| $\|u(t)\|_{L^2}$ (bounded energy) | definition of acceptable solution | $1 - 3/2 = -1/2$ | supercritical |
| $\|\nabla u\|_{L^2}$ (enstrophy$^{1/2}$, from energy identity) | the dissipation term | $1 + 1 - 3/2 = +1/2$ | subcritical |
| $\|u\|_{\dot H^{1/2}}$ (Fujita-Kato) | not in the note, but the scale of "smallness" | $1 + 1/2 - 3/2 = 0$ | critical |
| $\|u\|_{L^3}$ (ESS endpoint) | not in the note; the sharp continuation norm | $1 - 3/3 = 0$ | critical |
| $\int_0^T\|\omega(t)\|_{L^\infty}\,dt$ (BKM) | not in the note; the sharp blow-up criterion | $0$ | critical |

The reading: the problem's own "no blow-up" clause lives at $a=-1/2$, **supercritical**. Calling `audit_estimate` on the energy norm returns the verdict `INSUFFICIENT_BY_ITSELF`: a supercritical controlling norm gives no control at the small scales where a singularity would form, so the bound the note hands us for free cannot, by itself, certify smoothness. Meanwhile the dissipation $\int\|\nabla u\|_2^2$ that the energy identity controls in time is subcritical pointwise in $t$ but is only an $L^2$-in-time bound (it can be exhausted in finite time), so it does not upgrade to an all-time pointwise enstrophy bound in 3D. The continuation norms that *would* certify smoothness ($\dot H^{1/2}$, $L^3$, the BKM integral) all sit at $a=0$, **critical**, and no all-time a priori bound at that level is known. This exact gap, from the supercritical bound we have to the critical bound we need, is the supercriticality gap the project is organized around. See [`../research_directions/03_supercriticality_gap.md`](../research_directions/03_supercriticality_gap.md).

A short way to say it: the Clay note defines success as a critical-or-subcritical regularity statement, but the only currency it grants for free is supercritical. The whole problem is the change of currency.

## Against the three controls

The note is the document that *defines* the controls' calibration, so the audit here reads slightly differently from a typical result: instead of asking whether a method passes, we record what the note says about each control.

- **Control A (2D must stay smooth).** The note explicitly observes that the analogous 2D problem was solved affirmatively long ago (global regularity; Ladyzhenskaya 1959, building on Leray). This is not a footnote; it is the sharpest available constraint on any proof of (A)/(B). The 2D and 3D equations differ only in the vortex-stretching term $\omega\cdot\nabla u$, which vanishes identically in 2D (vorticity is a transported-with-diffusion scalar, $\partial_t\omega + u\cdot\nabla\omega = \nu\Delta\omega$, and enstrophy is non-increasing). So any argument for (A)/(B) that does not genuinely use 3D structure would, by the same steps, prove the 2D case false where it is true, or would prove a false 3D analog of a true 2D fact. The note's mention of 2D is the project's must-stay-smooth control in its original source.

- **Control B (supercriticality is the ceiling).** As computed above, the note's bounded-energy clause is supercritical ($a=-1/2$). The note itself flags the structural situation: global weak solutions (Leray) exist and short-time smooth solutions exist, but the two have never been bridged. The analytic name for that bridge failing is precisely that the global bound is supercritical and the smoothness-forcing bounds are critical. The note does not use this vocabulary, but it states the symptom (the gap between weak existence and smooth existence) of which supercriticality is the diagnosis.

- **Control C (viscosity and the exact NS structure are essential).** The note keeps $\nu > 0$ fixed and never sends it to zero; the target is the viscous equation. This matters because the inviscid limit is genuinely different: inviscid Burgers shocks in finite time, and 3D Euler has finite-time-singularity results and evidence (Elgindi 2021; Chen-Hou). The viscous regularizing term $\nu\Delta u$ is exactly what is in question, and a candidate proof that would work verbatim for Euler (no use of $\nu$) is suspect, because Euler blows up. The note's insistence on $\nu>0$ and on the exact NS nonlinearity (not an averaged or modified one) is the source of the viscosity control. Tao (2016) sharpens the warning from the other side: an *averaged* Navier-Stokes that respects the energy identity blows up in finite time, so the proof must use structure beyond the energy identity that the averaging destroys.

- **Architecture 5 boundary.** The note's definition of "solution" requires $C^\infty$ regularity and pointwise satisfaction of the equations; it does not require, and does not even mention, uniqueness in the weak class. Convex integration (Buckmaster-Vicol 2019; and for forced Leray-Hopf solutions, Albritton-Brue-Colombo 2022) produces non-unique non-smooth weak solutions below the energy class. These objects are not solutions in Fefferman's sense (they are not $C^\infty$), so they neither prove nor disprove (A) through (D) directly. They live just outside the note's frame, sharpening what "solution" can mean rather than answering the regularity question. The note's silence on uniqueness is precisely the gap convex integration occupies. See [`../research_directions/05_convex_integration_boundary.md`](../research_directions/05_convex_integration_boundary.md).

## What it gives / what it does not give

**What it gives.** A precise, gradeable target. Specifically: (i) the equation, with $\nu>0$ and a clean choice of $f\equiv 0$ for the existence targets; (ii) the data class (Schwartz, divergence-free, smooth), chosen to remove every nuisance about decay and infinity; (iii) the solution class ($C^\infty$ with bounded energy), chosen so that "smooth" means "no blow-up" and bounded energy excludes nonphysical drifts; (iv) two acceptable verdicts (global smoothness or finite-time breakdown) and two domains ($\mathbb{R}^3$, $\mathbb{T}^3$). It also gives an honest map of the partial results: Leray-Hopf weak solutions exist globally, short-time smooth solutions exist, 2D is solved, and the 3D global-smoothness question sits in between, unresolved.

**What it does not give, and the gap to closing regularity.**

- It does not require uniqueness, so a proof of existence-and-smoothness need not settle uniqueness, and conversely the non-uniqueness results (Architecture 5) do not bear directly on (A)/(B).
- It does not award anything for partial regularity. Caffarelli-Kohn-Nirenberg (1982) proved the singular set of a suitable weak solution has one-dimensional parabolic Hausdorff measure zero (informally, no singular curves in space-time; the singular set is at most a discrete set of points in space at each time). This is the strongest known unconditional statement toward (A), and it is still infinitely far from (A): "the singular set is very small" is not "the singular set is empty." The note's all-or-nothing $C^\infty$ requirement is what makes CKN partial rather than complete.
- It does not award anything for conditional regularity. Beale-Kato-Majda, Prodi-Serrin-Ladyzhenskaya, and Escauriaza-Seregin-Sverak each say "if a certain critical or subcritical norm stays finite, the solution is smooth." None of these norms is known to stay finite for general data, because the only unconditional all-time bound (energy) is supercritical and does not control them. The conditional results convert (A) into the equivalent problem "show this critical norm cannot blow up," which is the supercriticality gap restated, not crossed.
- It does not award anything for solving a modified equation. Tao (2016) built an averaged Navier-Stokes that obeys the same energy identity and yet blows up in finite time. This proves no energy-only argument can settle (A), and it tells a candidate proof exactly which structure (the precise nonlinear cancellations the averaging breaks) it must use. It is a barrier and a compass, not a counterexample to NS.

The single most important sentence for the project: the note grants us a supercritical bound and asks for a critical-or-subcritical conclusion, with the 2D control forbidding any shortcut that ignores vortex stretching and the viscosity control forbidding any shortcut that ignores $\nu$. That triangulation is the search region for the real proof.

## Lineage and sharpest known form

**What it builds on.** The note distills the classical theory: Leray (1934) global weak solutions and the energy inequality; Hopf (1951) on bounded domains; the short-time smooth existence theory (Kato, Fujita-Kato $\dot H^{1/2}$); Ladyzhenskaya's 2D global regularity (1959). It states these as the known background against which (A) through (D) are open.

**What built on it.** Everything in the repo is downstream of the note's framing. The partial-regularity line (CKN 1982) sharpens "how big can the singular set be." The conditional line (BKM 1984; Prodi 1959, Serrin 1962, Ladyzhenskaya; ESS 2003) sharpens "which norm staying finite forces smoothness." The critical-space line (Fujita-Kato 1964; Koch-Tataru 2001, $\mathrm{BMO}^{-1}$) sharpens "how small must the data be for global smoothness." The barrier line (Necas-Ruzicka-Sverak 1996 and Tsai 1998 ruling out $L^3$ self-similar blow-up; Tao 2016 averaged blow-up) sharpens "what a singularity cannot look like, and what a proof must use."

**Sharpest known forms as of 2025.** The note itself is the fixed problem statement and is not "improved," but the frontier of the partial results it lists has moved:
- *Critical endpoint (ESS).* Escauriaza-Seregin-Sverak (2003) closed the $L^\infty_t L^3_x$ endpoint. Tao (2019/2020) made it quantitative: at a hypothetical first singularity, $\|u(t)\|_{L^3}$ must blow up at least at a triple-logarithmic rate, a self-improving critical bound. Barker-Prange and others have localized and refined the quantitative ESS estimates.
- *Vorticity criterion (BKM).* The Beale-Kato-Majda integral $\int_0^T\|\omega\|_{L^\infty}\,dt$ was sharpened by Kozono-Taniuchi (2000) to the weaker $\mathrm{BMO}$ norm $\int_0^T\|\omega\|_{\mathrm{BMO}}\,dt$, a genuine refinement since $L^\infty\subset\mathrm{BMO}$.
- *Self-similar exclusion.* The $L^3$ exclusion of Leray self-similar blow-up (Necas-Ruzicka-Sverak; Tsai) was extended by Jia-Sverak (2014) to a local-in-space / minimal regularity setting, and their program produced candidate non-uniqueness scenarios that fed Albritton-Brue-Colombo (2022).
- *Convex integration.* Buckmaster-Vicol (2019) non-uniqueness of weak solutions below Leray-Hopf, then Albritton-Brue-Colombo (2022) non-uniqueness of *Leray-Hopf* solutions for a forced equation, mark how far the boundary of "solution" has been pushed, all of it outside the $C^\infty$ class the note requires.

None of these has changed the status of (A) through (D): all four remain open as of 2025. What has changed is the resolution of the map of where the proof cannot live.

## References

- C. L. Fefferman, "Existence and smoothness of the Navier-Stokes equation," Clay Mathematics Institute Millennium Prize Problem description, 2000 (revised circa 2006); in J. Carlson, A. Jaffe, A. Wiles (eds.), *The Millennium Prize Problems*, CMI/AMS, 2006.
- J. Leray, "Sur le mouvement d'un liquide visqueux emplissant l'espace," *Acta Math.* 63 (1934), 193-248.
- E. Hopf, "Uber die Anfangswertaufgabe fur die hydrodynamischen Grundgleichungen," *Math. Nachr.* 4 (1951), 213-231.
- O. A. Ladyzhenskaya, *The Mathematical Theory of Viscous Incompressible Flow* (2D global regularity, 1959; English ed. Gordon and Breach, 1969).
- L. Caffarelli, R. Kohn, L. Nirenberg, "Partial regularity of suitable weak solutions of the Navier-Stokes equations," *Comm. Pure Appl. Math.* 35 (1982), 771-831.
- J. T. Beale, T. Kato, A. Majda, "Remarks on the breakdown of smooth solutions for the 3-D Euler equations," *Comm. Math. Phys.* 94 (1984), 61-66.
- G. Prodi (1959); J. Serrin (1962); O. Ladyzhenskaya: the $L^p_t L^q_x$, $2/p+3/q\le 1$ criterion.
- L. Escauriaza, G. Seregin, V. Sverak, "$L_{3,\infty}$-solutions of Navier-Stokes equations and backward uniqueness," *Russian Math. Surveys* 58 (2003), 211-250.
- H. Fujita, T. Kato, "On the Navier-Stokes initial value problem I," *Arch. Rational Mech. Anal.* 16 (1964), 269-315.
- H. Koch, D. Tataru, "Well-posedness for the Navier-Stokes equations," *Adv. Math.* 157 (2001), 22-35.
- H. Kozono, Y. Taniuchi, "Bilinear estimates in BMO and the Navier-Stokes equations," *Math. Z.* 235 (2000), 173-194.
- J. Necas, M. Ruzicka, V. Sverak, "On Leray's self-similar solutions of the Navier-Stokes equations," *Acta Math.* 176 (1996), 283-294; T.-P. Tsai (1998).
- H. Jia, V. Sverak, "Local-in-space estimates near initial time for weak solutions of the Navier-Stokes equations and forward self-similar solutions," *Invent. Math.* 196 (2014), 233-265.
- T. Tao, "Finite time blowup for an averaged three-dimensional Navier-Stokes equation," *J. Amer. Math. Soc.* 29 (2016), 601-674.
- T. Tao, "Quantitative bounds for critically bounded solutions to the Navier-Stokes equations," (2019/2020).
- T. Buckmaster, V. Vicol, "Nonuniqueness of weak solutions to the Navier-Stokes equation," *Ann. of Math.* 189 (2019), 101-144.
- D. Albritton, E. Brue, M. Colombo, "Non-uniqueness of Leray solutions of the forced Navier-Stokes equations," *Ann. of Math.* 196 (2022), 415-455.
- T. Elgindi, "Finite-time singularity formation for $C^{1,\alpha}$ solutions to the incompressible Euler equations on $\mathbb{R}^3$," *Ann. of Math.* 194 (2021), 647-727.

## Cross-links

- Research directions: [01 critical continuation criteria](../research_directions/01_critical_continuation_criteria.md) (which norm staying finite forces smoothness), [02 vorticity geometry](../research_directions/02_vorticity_geometry.md) (the $\omega\cdot\nabla u$ structure the 2D control forbids ignoring), [03 supercriticality gap](../research_directions/03_supercriticality_gap.md) (the supercritical-to-critical change of currency this note defines), [04 blow-up and barriers](../research_directions/04_blowup_and_barriers.md) (targets (C)/(D) and the Tao barrier), [05 convex integration boundary](../research_directions/05_convex_integration_boundary.md) (the uniqueness question the note leaves outside its frame).
- Sibling reading notes: [Leray 1934](leray_1934.md) (the weak-solution class the note adopts), [Caffarelli-Kohn-Nirenberg 1982](caffarelli_kohn_nirenberg_1982.md) (the sharpest partial result toward (A)), [Beale-Kato-Majda 1984](beale_kato_majda_1984.md) and [Escauriaza-Seregin-Sverak 2003](escauriaza_seregin_sverak_2003.md) (the continuation criteria that restate (A)), [Tao 2016 averaged NS](tao_2016_averaged.md) (the energy-method barrier).
- Graduate background: [`../../02_graduate/scaling_and_supercriticality.md`](../../02_graduate/scaling_and_supercriticality.md).

## What this enables / what remains open

**Enables.** A precise grading rubric for every candidate in the repo: a result counts toward the prize only if it produces a $C^\infty$, bounded-energy, global solution for all Schwartz divergence-free data (targets A/B) or a genuine finite-time singularity (targets C/D). It fixes the criticality coordinates (energy is supercritical, the smoothness-forcing norms are critical) that the whole search uses, and it pins the two structural facts (2D solved; 3D between weak existence and short-time smoothness) the controls are calibrated against. BUILDER should treat the bounded-energy supercriticality as the starting deficit any candidate estimate must overcome; ADVERSARY should treat the 2D control and the $\nu>0$ requirement as hard filters; SYNTHESIZER should grade every claimed advance against the four targets verbatim.

**Remains open.** All four targets (A), (B), (C), (D). The note does not tell us which way the answer goes; the repo's working hypothesis (regularity, targets A/B) is a bet, not a theorem. The concrete open sub-questions the note exposes: can any critical norm ($\dot H^{1/2}$, $L^3$, the BKM integral) be controlled for all time by a new a priori quantity (Direction 03), and if not, can a genuine NS singularity be constructed inside the Schwartz class while evading the $L^3$ self-similar exclusion (Direction 04). Both are restatements of the same supercriticality gap the note's bounded-energy clause makes unavoidable.
