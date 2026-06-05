# Reading notes: Bourgain-Pavlovic (2008)

J. Bourgain, N. Pavlovic, "Ill-posedness of the Navier-Stokes equations in a critical space in 3D," Journal of Functional Analysis 255 (2008), no. 9, 2233-2247.

> This is the upper-boundary marker for Architecture 3 (critical spaces and scaling). Koch-Tataru (2001) proved small-data global well-posedness in $\mathrm{BMO}^{-1}$, the largest critical space then known to be well-posed. Bourgain-Pavlovic show that one notch larger, in the critical Besov space $\dot B^{-1}_{\infty,\infty}$, the flow is *ill-posed*: arbitrarily small data produce solutions that become arbitrarily large in arbitrarily short time (norm inflation), so the solution map is not even continuous at $0$. Together these two results pin the critical-space frontier from both sides. The note ties directly into structural control (B): a critical norm is necessary but a critical space can be too rough to support a continuous flow, so "find a critical estimate" is not by itself a recipe, the *space* matters. This is a barrier result, not a regularity result; it tells the project where the well-posedness theory has to stop, and therefore where any regularity-closing estimate cannot simply be a norm bound.

## What it proves

The setting is the incompressible Navier-Stokes Cauchy problem on $\mathbb{R}^3$,
$$\partial_t u - \Delta u + (u\cdot\nabla)u + \nabla p = 0,\qquad \nabla\cdot u = 0,\qquad u(0)=u_0,$$
written through the Leray projector $\mathbb{P}$ and the Duhamel (mild) formulation
$$u(t) = e^{t\Delta}u_0 - \int_0^t e^{(t-s)\Delta}\,\mathbb{P}\,\nabla\cdot\big(u(s)\otimes u(s)\big)\,ds.$$

The critical space in play is the homogeneous Besov space $\dot B^{-1}_{\infty,\infty}(\mathbb{R}^3)$ (the paper writes it $\dot B^{-1,\infty}_{\infty}$), with norm
$$\|f\|_{\dot B^{-1}_{\infty,\infty}} \;=\; \sup_{t>0}\, t^{1/2}\,\big\|e^{t\Delta} f\big\|_{L^\infty(\mathbb{R}^3)}.$$
This is the largest classical critical space for 3D Navier-Stokes: there is a chain of continuous embeddings
$$\dot H^{1/2}\hookrightarrow L^3 \hookrightarrow \dot B^{-1+3/p}_{p,\infty}\ (p<\infty)\hookrightarrow \mathrm{BMO}^{-1}\hookrightarrow \dot B^{-1}_{\infty,\infty},$$
and every space in the chain has the same scaling. So $\dot B^{-1}_{\infty,\infty}$ is the roughest critical space, sitting just beyond $\mathrm{BMO}^{-1}$.

**Main theorem (norm inflation, informal).** For every $\delta>0$ and every $N>0$ there exist a Schwartz initial datum $u_0$ (smooth, divergence free) and a time $0<T<\delta$ such that
$$\|u_0\|_{\dot B^{-1}_{\infty,\infty}} \;\le\; \delta,\qquad\text{but}\qquad \|u(T)\|_{\dot B^{-1}_{\infty,\infty}} \;\ge\; N,$$
where $u$ is the (locally smooth, since $u_0$ is Schwartz) solution. Consequently the data-to-solution map
$$u_0 \longmapsto u(t), \qquad \dot B^{-1}_{\infty,\infty}\to \dot B^{-1}_{\infty,\infty},$$
fails to be continuous at the origin: it is discontinuous as a map at $0$, and in particular not bounded and not Lipschitz on any neighborhood of $0$. The data are genuinely smooth, so this is *not* a low-regularity artifact; the failure is purely about the topology of the critical norm $\dot B^{-1}_{\infty,\infty}$.

The point of "Schwartz data" is sharpness: the solution exists and is smooth, there is no question of what "solution" means. The pathology is that smallness in $\dot B^{-1}_{\infty,\infty}$ does not survive the flow even for an instant, which is the negation of the well-posedness one has in $\mathrm{BMO}^{-1}$.

A precise note on what "ill-posed" means here. Hadamard well-posedness asks for existence, uniqueness, and *continuous dependence on data*. Existence and uniqueness of a local smooth solution for Schwartz data are not in question. It is the third clause, continuous dependence in the $\dot B^{-1}_{\infty,\infty}$ topology, that fails, and it fails maximally: not merely non-Lipschitz, but discontinuous, at the single most benign point (the origin, $u_0\to 0$). So the failure cannot be repaired by shrinking the data; it is a defect of the *norm*, not of the size of the data.

## Method / structure

The proof is a quantitative Picard-iteration analysis. Write the mild solution as the Picard series
$$u = \sum_{k\ge1} u^{(k)},\qquad u^{(1)} = e^{t\Delta}u_0,\qquad u^{(2)} = -\int_0^t e^{(t-s)\Delta}\,\mathbb{P}\,\nabla\cdot\big(u^{(1)}\otimes u^{(1)}\big)\,ds,$$
and $u^{(k)}$ defined by the bilinear recursion $B(u^{(i)},u^{(j)})$, $i+j=k$, where
$$B(u,v)(t) = -\int_0^t e^{(t-s)\Delta}\,\mathbb{P}\,\nabla\cdot\big(u(s)\otimes v(s)\big)\,ds.$$

The mechanism, lemma by lemma:

- **Designed data.** Choose $u_0$ as a sum of high-frequency oscillatory packets at a large frequency $\kappa$, of the schematic form
$$u_0 \;\sim\; \frac{r}{\sqrt{\log r}}\,\kappa\,\sum_{\text{finite}} \big(\cos(\kappa\, e\cdot x)\big)\,v,$$
with a large frequency $\kappa$, a slowly growing prefactor, and polarization vectors $v$ chosen orthogonal to the wavevector so $\nabla\cdot u_0=0$. The logarithm and the precise number of packets are tuned so that the *linear* part stays small in $\dot B^{-1}_{\infty,\infty}$: by construction $\|u_0\|_{\dot B^{-1}_{\infty,\infty}}\le \delta$. The Besov norm at level $-1$ exactly tolerates one factor of $\kappa$ together with the $L^\infty$ amplitude, which is why the construction lives in this space and not in $L^3$ or $\mathrm{BMO}^{-1}$ (those finer norms would already see the packet as large).

- **The second iterate dominates.** The heart of the proof is that the *first Picard correction* $u^{(2)} = B(u^{(1)},u^{(1)})$ is already large in $\dot B^{-1}_{\infty,\infty}$ at a short time $T\sim \kappa^{-2}$ (the natural viscous time of frequency $\kappa$), while the linear term $u^{(1)}$ and the higher iterates $u^{(k)}$, $k\ge3$, remain small. The product $u^{(1)}\otimes u^{(1)}$ contains a *resonant low-frequency beat*: two packets at frequencies $\kappa e_1$ and $\kappa e_2$ generate a difference frequency $\kappa(e_1-e_2)$ of size $O(1)$ (or any chosen low frequency). At that low frequency the heat semigroup does *not* dissipate on the time scale $\kappa^{-2}$, the prefactor $\nabla\cdot$ contributes only an $O(1)$ factor, and the time integral over $[0,T]$ of two amplitude-$\kappa$ packets produces a coefficient that beats the $-1$ Besov weight. The outcome is a clean lower bound
$$\big\|u^{(2)}(T)\big\|_{\dot B^{-1}_{\infty,\infty}} \;\gtrsim\; (\log\kappa)\cdot(\text{controllable}) \;\ge\; N,$$
arbitrarily large as $\kappa\to\infty$, achieved at $T\to0$.

- **Controlling the tail.** The remaining work is to show the series tail $\sum_{k\ge3}u^{(k)}$ does not cancel or swamp $u^{(2)}$. Bourgain-Pavlovic bound the trilinear and higher terms in an auxiliary norm (a space adapted to the iteration, finer than $\dot B^{-1}_{\infty,\infty}$, where the bilinear estimate of Koch-Tataru-type *does* close) and show those terms are $o(\|u^{(2)}\|)$ on $[0,T]$. So the solution is well defined and smooth on $[0,T]$ (the data are Schwartz), yet its $\dot B^{-1}_{\infty,\infty}$ norm at time $T$ is dominated by the inflated second iterate.

The structural reading: the bilinear map $B$ is *bounded* on $\mathrm{BMO}^{-1}$ (this is exactly the Koch-Tataru fixed-point estimate), but it is *unbounded* on $\dot B^{-1}_{\infty,\infty}$. The construction is precisely a witness that $B:\dot B^{-1}_{\infty,\infty}\times \dot B^{-1}_{\infty,\infty}\to \dot B^{-1}_{\infty,\infty}$ fails the estimate that drives the contraction. No vortex stretching, no energy identity, no viscosity-vs-inviscid dichotomy enters; the result is a statement about the harmonic analysis of the Duhamel bilinear term in the roughest critical norm.

Why this is a $\dot B^{-1}_{\infty,\infty}$ phenomenon and not a finer-space one:

- In $L^3$ or $\dot H^{1/2}$ or $\mathrm{BMO}^{-1}$ the high-frequency packet would already register as *large* (these norms weight high frequencies more strongly), so the construction could not keep the data small there. The pathology requires a norm rough enough to declare the inflating packet "small" at the start.
- $\dot B^{-1}_{\infty,\infty}$ is the unique-up-to-the-scale roughest space with the right ($-1$) scaling, defined by a single $\sup_t$ of the heat-extension $L^\infty$ norm. The third Besov index $\infty$ (versus $q<\infty$ in $\mathrm{BMO}^{-1}$-adjacent spaces) is what removes the summability that the contraction needs. Wang (2015) later showed the third index being finite does not save you (see lineage), so the obstruction is really the $\dot B^{-1}_{\infty,\cdot}$ scale, not the $q=\infty$ endpoint alone.
- The mechanism is frequency-local and translation-structured, so it is robust: it survives passage to the torus $\mathbb{T}^3$ and to fractional-dissipation variants, which is why the same template reappears across related systems (see lineage).

## Criticality placement

Every space in this note has scaling exponent $0$ under $u_\lambda(x,t)=\lambda\,u(\lambda x,\lambda^2 t)$, $u_{0,\lambda}(x)=\lambda u_0(\lambda x)$. A homogeneous norm $\dot B^{s}_{p,q}$ on the *initial datum* is scale invariant for the velocity exactly when $s = -1 + 3/p$. For $p=\infty$ this gives $s=-1$, so $\dot B^{-1}_{\infty,\infty}$ and $\dot B^{-1}_{\infty,q}$ for any $q$ are all critical, as is $\mathrm{BMO}^{-1}$ and $\dot H^{1/2}$ (here $s=1/2$, $p=2$, $-1+3/2=1/2$). Run any of these through the criticality bookkeeper `experiments/_shared/criticality.py` and the scaling exponent returns $0$: critical, not sub, not super.

This is the subtle and important content for the project. *Criticality of the norm is not enough.* Bourgain-Pavlovic is a critical-space result on both sides:

- The norm $\dot B^{-1}_{\infty,\infty}$ is critical (exponent $0$), so it is exactly the kind of quantity Architecture 3 wants to control.
- Yet the flow is ill-posed there. So a critical norm can be too weak (too rough, too far down the embedding chain) for any continuous solution theory, let alone a regularity theory.

The lesson sits beside the supercriticality gap, not on top of it. The supercriticality gap (control B) says: energy is supercritical, so an energy-level bound cannot reach a critical regularity statement, the proof must add critical control. Bourgain-Pavlovic adds a second constraint from the *other* direction: not every critical control is admissible, because below $\mathrm{BMO}^{-1}$ the critical norm does not even generate a continuous flow. The viable window for a critical well-posedness norm is bounded above (by $\dot B^{-1}_{\infty,\infty}$, excluded) and the project's regularity target must live at or below $\mathrm{BMO}^{-1}$ in roughness. The energy norm $L^\infty_t L^2_x$ (scaling exponent $-1/2$ on the datum side, supercritical) is on the far *other* end and does not embed into any of these critical spaces; the two facts are independent walls bracketing the search.

## Against the three controls

- **(A) 2D control.** The construction is dimension-agnostic at its core: the resonant-beat mechanism in the bilinear Duhamel term exists in 2D as well, and indeed analogous norm-inflation statements hold for 2D Navier-Stokes in the corresponding critical Besov space (scaling $s=-1+2/p$, so $\dot B^{-1}_{\infty,\infty}$ is critical in 2D too, since the velocity scaling $\lambda u(\lambda x,\lambda^2 t)$ is the same in any dimension). This does *not* violate control (A), because control (A) concerns *blow-up of smooth solutions*, and this result is about *discontinuity of the flow map in a rough critical norm*, not about loss of smoothness. The 2D solutions here are still globally smooth (2D NS is globally regular); they merely have a discontinuous data-to-solution map in $\dot B^{-1}_{\infty,\infty}$. So Bourgain-Pavlovic is correctly *outside* the regularity dichotomy that control (A) polices: it is a well-posedness statement, not a regularity statement. Worth flagging explicitly: a reader could mistake "ill-posed" for "blows up". It does not. Smooth data here stay smooth; the norm inflates but the solution is fine.

- **(B) Supercriticality / critical-space frontier.** This is the primary tie-in and it is structural-control adjacent rather than an instance of the gap. The energy supercriticality ceiling says energy cannot reach critical regularity. Bourgain-Pavlovic marks the *upper* edge of the critical regime: the roughest critical space is already ill-posed. The two together carve the admissible band. The result does not engage the energy identity at all, and it does not claim any energy-level estimate; it is purely about the harmonic-analytic size of the bilinear term in a critical norm.

- **(C) Viscosity / Burgers control.** Viscosity is present and is in fact *used*: the proof works on the viscous time scale $T\sim\kappa^{-2}$, and the heat semigroup's failure to dissipate the low-frequency beat is what lets $u^{(2)}$ inflate. The result is therefore *not* blind to viscosity, but neither does it exploit the precise nonlinear structure in the way a regularity proof must. It is the opposite kind of statement from a regularity criterion: it shows that even *with* viscosity, the critical norm $\dot B^{-1}_{\infty,\infty}$ cannot tame the bilinear term. So control (C) is satisfied trivially (viscosity is in the picture) and is not the operative constraint here.

Net: this is an Architecture-3 *barrier* result. It uses no genuine 3D structure (the vortex-stretching term $\omega\cdot\nabla u$ never appears), it is not an energy estimate, and it does not predict any blow-up. It maps a boundary of the well-posedness theory, which is exactly what a barrier should do.

## What it gives / what it does not give

What it gives:

- A hard ceiling on critical-space well-posedness. $\mathrm{BMO}^{-1}$ (Koch-Tataru) is essentially the top of the well-posed critical tower; one step rougher, in $\dot B^{-1}_{\infty,\infty}$, continuity of the flow already fails. This sharpens "regularity is a critical-scaling statement" into "regularity is a critical-scaling statement *in a sufficiently fine critical norm*; the roughest critical norm is too weak even for continuity."
- A concrete, explicit mechanism (resonant low-frequency beat in the second Picard iterate, large at the viscous time) that the project can reuse as a stress test: any proposed critical a priori quantity should be checked against whether the Bourgain-Pavlovic data inflate it. If the candidate quantity also inflates for these smooth small data, it cannot underlie a continuous theory.
- Negative information that is genuinely a coordinate: it tells BUILDER not to chase a fixed-point / contraction scheme in $\dot B^{-1}_{\infty,\infty}$ or any space containing it, because the bilinear estimate provably fails there.

What it does not give (the gap to regularity):

- It says nothing about blow-up of smooth solutions. A discontinuous flow map in a rough norm is compatible with global smoothness (2D is the proof of that). So this result does not touch the Clay problem's regularity question directly; it constrains the *space*, not the *fate of the solution*.
- It does not show $\mathrm{BMO}^{-1}$ is *optimal* for well-posedness, only that $\dot B^{-1}_{\infty,\infty}$ is too big. The exact boundary between well-posed and ill-posed critical spaces is finer than this single result resolves (see lineage: Germain, Yoneda, Wang push the boundary down to $\dot B^{-1}_{\infty,q}$ for *all* finite $q$).
- It gives no coercive quantity and no monotonicity. It is the wrong *type* of result to close regularity; it is a frontier-marker. The project should read it as "here is where the critical-space architecture's well-posedness theory ends," not as a step toward an estimate.

The single most useful takeaway for the program: a critical norm being scale-invariant (exponent $0$ in the bookkeeper) is *necessary but not sufficient* to be a useful control. Direction 03's catalog of candidate critical quantities must add a continuity/admissibility check, not only a scaling check.

A reusable stress test for BUILDER and ADVERSARY:

1. Take any proposed critical control quantity $Q[u]$ (a candidate norm or functional at scaling exponent $0$).
2. Feed it the Bourgain-Pavlovic family: smooth data small in $\dot B^{-1}_{\infty,\infty}$ whose second Picard iterate inflates at time $T\sim\kappa^{-2}$.
3. If $Q$ inflates on this family (i.e. small initial $Q$, large $Q$ at time $T$), then $Q$ cannot underlie a *continuous* small-data theory, and any contraction/fixed-point scheme built on $Q$ in a space that sees $\dot B^{-1}_{\infty,\infty}$ is doomed. This does not by itself rule $Q$ out as an a priori bound for *already-smooth* solutions, but it flags that $Q$ is not a well-posedness norm.
4. If $Q$ stays controlled on this family (like the $\mathrm{BMO}^{-1}$ norm of these same small data, which Koch-Tataru keeps controlled), $Q$ passes this particular test.

Common misreadings to avoid (flagged for SYNTHESIZER):

- "Ill-posed" does not mean "blows up". The solutions here are globally smooth in 2D and locally smooth in 3D; the flow map is what misbehaves.
- This does not contradict Koch-Tataru. Koch-Tataru is small-data well-posedness in the $\mathrm{BMO}^{-1}$ topology; the inflation is in the strictly rougher $\dot B^{-1}_{\infty,\infty}$ topology.
- This is not a supercriticality result. Every norm here is critical (exponent $0$); the obstruction is roughness within the critical class, a distinct axis from the sub/critical/super axis.

## Lineage and sharpest known form

Builds on:

- **H. Koch, D. Tataru (2001).** Small-data global well-posedness in $\mathrm{BMO}^{-1}$, via a bilinear estimate in an adapted (Koch-Tataru) function space. Bourgain-Pavlovic is the exact complement: the bilinear estimate that closes in $\mathrm{BMO}^{-1}$ fails one step up in $\dot B^{-1}_{\infty,\infty}$, and the construction is the explicit witness.
- **H. Fujita, T. Kato (1964).** Small-data well-posedness in $\dot H^{1/2}$, the original critical-space result, at the bottom (finest) end of the embedding chain.
- The general technology of Picard-iterate norm inflation, which became a template for ill-posedness across dispersive and parabolic equations after this paper.

Built on it / sharpest known refinements (the critical-space frontier, pushed down):

- **P. Germain (2008), "The second iterate for the Navier-Stokes equation," J. Funct. Anal. 255.** Shows the data-to-solution map fails to be $C^2$ (the second-order Taylor term, i.e. the second Picard iterate, is unbounded) in $\dot B^{-1}_{\infty,q}$ for $q>2$. This is the smooth-dependence version of the same second-iterate mechanism and isolates $q=2$ as a threshold for $C^2$ regularity of the flow.
- **T. Yoneda (2010), "Ill-posedness of the 3D Navier-Stokes equations in a generalized Besov space near $\mathrm{BMO}^{-1}$," J. Funct. Anal. 258.** Constructs ill-posedness (norm inflation) in generalized Besov spaces sitting *between* $\mathrm{BMO}^{-1}$ and $\dot B^{-1}_{\infty,\infty}$, tightening the gap just above Koch-Tataru and showing the well-posed/ill-posed boundary is delicate at the very top of the critical tower.
- **B. Wang (2015), "Ill-posedness for the Navier-Stokes equations in critical Besov spaces $\dot B^{-1}_{\infty,q}$," Adv. Math. 268.** The sharpest known statement: norm inflation (discontinuity of the solution map at the origin) holds in $\dot B^{-1}_{\infty,q}$ for *all* $1\le q\le\infty$, including $1\le q\le2$ where these spaces *embed into* $\mathrm{BMO}^{-1}$. So even though the *data* are small in $\mathrm{BMO}^{-1}$ (hence Koch-Tataru gives a global solution), the *finer* $\dot B^{-1}_{\infty,q}$ norm of that same solution inflates. This does not contradict Koch-Tataru: Koch-Tataru is well-posedness in the $\mathrm{BMO}^{-1}$ topology for small $\mathrm{BMO}^{-1}$ data, while Wang's discontinuity is in the strictly finer $\dot B^{-1}_{\infty,q}$ topology. The combined picture as of 2025: $\mathrm{BMO}^{-1}$ remains the largest critical space with small-data well-posedness, and the entire homogeneous Besov scale $\dot B^{-1}_{\infty,q}$ (every $q$) is ill-posed in its own norm.
- **Adjacent and downstream.** The same resonant-beat / second-iterate template was exported to the magneto-hydrodynamic system, the Boussinesq system, and generalized (fractional-dissipation) Navier-Stokes, and underlies the broader study of "how rough a critical space can be." On the *growth* side (distinct from ill-posedness), recent work studies arbitrarily large finite-time norm growth for genuinely strong solutions; that is a different phenomenon (growth of a real solution, not discontinuity at $0$) and should not be conflated with norm inflation (verify the precise statements before citing, recent 2024-2025 preprints).

## References

- J. Bourgain, N. Pavlovic, "Ill-posedness of the Navier-Stokes equations in a critical space in 3D," J. Funct. Anal. 255 (2008), no. 9, 2233-2247. arXiv:0807.0882.
- H. Koch, D. Tataru, "Well-posedness for the Navier-Stokes equations," Adv. Math. 157 (2001), 22-35.
- H. Fujita, T. Kato, "On the Navier-Stokes initial value problem I," Arch. Rational Mech. Anal. 16 (1964), 269-315.
- P. Germain, "The second iterate for the Navier-Stokes equation," J. Funct. Anal. 255 (2008), 2248-2264. (verify exact page range)
- T. Yoneda, "Ill-posedness of the 3D-Navier-Stokes equations in a generalized Besov space near $\mathrm{BMO}^{-1}$," J. Funct. Anal. 258 (2010), 3376-3387. (verify exact volume and pages)
- B. Wang, "Ill-posedness for the Navier-Stokes equations in critical Besov spaces $\dot B^{-1}_{\infty,q}$," Adv. Math. 268 (2015), 350-372. (verify exact pages)
- For the critical-space embedding chain and the definition of $\dot B^{-1}_{\infty,\infty}$ via the heat semigroup: P.-G. Lemarie-Rieusset, "Recent Developments in the Navier-Stokes Problem," Chapman and Hall/CRC (2002), and "The Navier-Stokes Problem in the 21st Century," CRC Press (2016).

## Cross-links

- Research direction: [Direction 01: critical continuation criteria](../research_directions/01_critical_continuation_criteria.md) (the well-posedness side of the critical tower).
- Research direction: [Direction 03: attack the supercriticality gap directly](../research_directions/03_supercriticality_gap.md) (where the "a critical norm is not automatically a useful control" caveat lands; add an admissibility/continuity check to the candidate-quantity catalog).
- Sibling note: [Escauriaza-Seregin-Sverak (2003)](escauriaza_seregin_sverak_2003.md) (the $L^3$ endpoint, the finest-norm critical continuation result, the well-posed-side complement to this barrier).
- Sibling note: [Fefferman problem statement](fefferman_problem_statement.md) (the regularity target this barrier does *not* touch directly).
