# Reading notes: an annotated map of the standard graduate references

> This note is not a single-result dossier. It is a *map*: a coordinate placement of the eight canonical graduate textbooks and monographs onto the project's spine (five architectures) and its three structural controls (2D smoothness, supercriticality, viscosity). Each entry says what the book is the best reference *for*, its level, which architecture and direction it serves, and where its central machinery sits on the criticality scale. The aim is so a BUILDER, ADVERSARY, or VERIFIER can pick the right book in one lookup, and so a reader knows in advance which control each book engages and which it is silent on. Because a textbook collects results rather than proving one, the criticality placement here is of the *machinery* the book is built around, not of a single theorem. The single-paper dossiers (BKM, ESS, CKN, Fujita-Kato, Leray, Hopf, Tao 2016/2019, ...) carry the sharp theorem statements; this note tells you which book to open to find each one with full proofs.

The eight references mapped here:

| # | Reference | Year | Best for | Architecture | Control engaged |
|---|---|---|---|---|---|
| 1 | Constantin-Foias | 1988 | dynamical-systems / attractor view; functional theory | 1, 2 | B (energy, dimension) |
| 2 | Temam | 1977 / 2001 | functional-analytic weak-solution framework + numerics | 1 | B (energy) |
| 3 | Doering-Gibbon | 1995 | energy methods, length scales, the ladder of norms | 1 | B (energy, explicitly) |
| 4 | Majda-Bertozzi | 2002 | vorticity, BKM, vortex stretching, 2D vs 3D | 2, 4 | A and C (best single source) |
| 5 | Bahouri-Chemin-Danchin | 2011 | Littlewood-Paley / Besov critical-space technique | 3 | B and edge of C |
| 6 | Robinson-Rodrigo-Sadowski | 2016 | cleanest modern self-contained 3D classical theory | 1, 2 | A, B (with full proofs) |
| 7 | Galdi | 1994 / 2011 | the steady (stationary) problem | (steady; 1) | B (no time, so no blow-up) |
| 8 | Sohr | 2001 | the $L^p$ / Stokes-semigroup theory | 1, 2, 3 | B (the $L^p$ substrate) |

The criticality convention is the bookkeeper's (`experiments/_shared/criticality.py`): a spatial norm $\|u\|_{L^q(\mathbb{R}^3)}$ has scaling exponent $a = 1 - 3/q$, with $a>0$ subcritical, $a=0$ critical, $a<0$ supercritical, under $u_\lambda(x,t)=\lambda\,u(\lambda x,\lambda^2 t)$. The energy norms $L^\infty_t L^2_x$ ($a=-1/2$) and $L^2_t \dot H^1_x$ ($a=0$ spatially but driven by the supercritical $L^2$ mass) are the supercritical pair that every book in the functional-analytic tradition is ultimately built on.

---

## 1. Constantin and Foias, "Navier-Stokes Equations" (1988)

P. Constantin, C. Foias, *Navier-Stokes Equations*, Chicago Lectures in Mathematics, University of Chicago Press (1988). ISBN 0-226-11548-8.

> The standard graduate reference for the *functional-analytic and dynamical-systems* view. Where Temam builds the weak-solution machinery, Constantin-Foias is the book that reads Navier-Stokes as an infinite-dimensional dynamical system: it carries the theory of the global attractor and its finite Hausdorff and fractal dimension, the Lyapunov-exponent / volume-contraction (Constantin-Foias-Temam) estimates, and the link to turbulence degrees of freedom. It serves Architectures 1 and 2 and engages control (B): everything is built on the energy and enstrophy, which is exactly why the 3D regularity question stays open inside it (the attractor theory for the *strong* 3D flow is conditional on regularity).

### What it is the best reference for

- The **Stokes operator** $A = -P\Delta$ (with $P$ the Leray projector) as a self-adjoint, positive, unbounded operator with compact inverse and discrete spectrum $0<\lambda_1\le\lambda_2\le\dots$, and the fractional powers $A^\alpha$ that index the natural scale of spaces $D(A^{\alpha})$. This is the cleanest place to learn the $A^{1/2}\sim\dot H^1$, $A^{1/4}\sim\dot H^{1/2}$ dictionary.
- The **global attractor** $\mathcal{A}$ for 2D Navier-Stokes: existence, and the bound on its Hausdorff and fractal dimension by the generalized Grashof number, $\dim_H \mathcal{A} \lesssim G^{2/3}(1+\log G)^{1/3}$ (the Constantin-Foias-Temam dimension estimate). This is the rigorous form of "number of degrees of freedom in 2D turbulence."
- The **enstrophy invariance** and the 2D vorticity structure stated in operator form.

### Level and method

Graduate, functional-analytic, terse. The mechanism is: project with $P$, pose $u' + \nu A u + B(u,u) = f$ as an abstract evolution equation on a Hilbert space $H = \{u \in L^2: \nabla\cdot u=0\}$, with $B(u,v)=P[(u\cdot\nabla)v]$ the bilinear term, and run Galerkin plus compactness. Dimension bounds come from the trace formula for the volume-contraction rate of the linearized flow (Lyapunov exponents), bounded via the Lieb-Thirring inequality.

### Criticality placement

The attractor-dimension theory is a **2D** theory: it closes because 2D enstrophy is an a priori bound (the 2D control A, but used positively, not as a detector). The 2D enstrophy $\|\omega\|_{L^2}^2$ is *critical* in 2D and *non-increasing*, which is exactly why the 2D attractor is finite-dimensional. In 3D the same constructions are **conditional on regularity**: the global attractor for the strong 3D flow exists only on the (open) hypothesis that solutions are smooth, because the supercritical 3D energy does not give the needed compactness uniformly. So the book is a precise illustration of control (B): the dynamical-systems picture is complete in 2D (subcritical-enough enstrophy) and stalls in 3D at exactly the supercriticality gap.

### Against the three controls

- (A) 2D: the book's headline successes (attractor, dimension) are 2D and rest on the absence of vortex stretching. It does not pretend the 3D strong-flow attractor is unconditional. It passes A by being honest about the 2D/3D divide at the level of the dynamical system.
- (B) Supercriticality: engaged throughout. The 3D theory in the book is the conditional theory; the unconditional theory is the energy/enstrophy theory, which is supercritical in 3D.
- (C) Viscosity: $\nu A$ is the dissipation and the whole attractor theory needs $\nu>0$ (the inviscid Euler flow has no compact attractor in this sense). Engaged but not foregrounded as a control.

### What it gives / does not give

Gives: the cleanest operator-theoretic substrate ($A$, $A^\alpha$, $B$), the complete 2D attractor and dimension theory, the turbulence degrees-of-freedom heuristics made rigorous in 2D. Does not give: any 3D regularity result; the 3D attractor here is conditional. It is background for Architectures 1 and 2, not a source of new critical control.

---

## 2. Temam, "Navier-Stokes Equations: Theory and Numerical Analysis" (1977 / 2001)

R. Temam, *Navier-Stokes Equations: Theory and Numerical Analysis*, North-Holland (1977); AMS Chelsea reprint (2001). (Companion: R. Temam, *Navier-Stokes Equations and Nonlinear Functional Analysis*, CBMS-NSF 66, SIAM, 2nd ed. 1995.)

> The canonical reference for the **Galerkin / weak-solution machinery** of Architecture 1, plus the finite-element and spectral numerical analysis that pairs with it. If you need the existence of Leray-Hopf weak solutions on a bounded domain done carefully, with the function spaces $H$ and $V$ defined and the compactness (Aubin-Lions) lemma stated and used, this is the book. It engages control (B): the only global bound it produces is the energy, and it states plainly that 3D uniqueness/regularity is open.

### What it is the best reference for

- The function-space setup: $H = $ closure of divergence-free test fields in $L^2$, $V = $ closure in $H^1$, with $V \hookrightarrow H \hookrightarrow V'$ a Gelfand triple. The Leray projector $P: L^2 \to H$ and the Stokes operator $A=-P\Delta: V \to V'$.
- **Existence of Leray-Hopf weak solutions** on bounded $\Omega \subset \mathbb{R}^3$ with no-slip boundary, via Galerkin truncation in the eigenbasis of $A$, energy a priori bounds, and Aubin-Lions compactness to pass to the limit in the nonlinear term. The standard reference proof.
- The **energy inequality** $\tfrac12\|u(t)\|_{L^2}^2 + \nu\int_0^t\|\nabla u\|_{L^2}^2 \le \tfrac12\|u_0\|_{L^2}^2$ derived as a property of the constructed solution (weak solutions satisfy the inequality, not necessarily equality).
- **2D uniqueness and regularity** (the Ladyzhenskaya theorem) with the Ladyzhenskaya inequality $\|u\|_{L^4(\mathbb{R}^2)}^2 \le C\|u\|_{L^2}\|\nabla u\|_{L^2}$ as the key 2D-only interpolation.
- The numerical half: finite-element and spectral Galerkin convergence, the basis for why pseudo-spectral DNS (the project's `taylor_green/` thread) is a legitimate approximation.

### Criticality placement

Pure Architecture 1. The a priori bounds are the energy bounds, $u \in L^\infty_t L^2_x \cap L^2_t \dot H^1_x$, both **supercritical** in 3D ($a=-1/2$ for the $L^2$ mass). In 2D the same Galerkin scheme closes to uniqueness and regularity because the Ladyzhenskaya inequality upgrades the energy bound to control the nonlinearity; in 3D the analogous inequality $\|u\|_{L^4(\mathbb{R}^3)}^2 \le C\|u\|_{L^2}^{1/2}\|\nabla u\|_{L^2}^{3/2}$ has the wrong exponents and the estimate does not close. That exponent gap *is* the supercriticality gap in its most elementary form.

### Against the three controls

- (A) 2D: the book proves the 2D positive result (control A's content) and shows precisely where the 3D analog fails (the $L^4$ exponent). Passes A.
- (B) Supercriticality: engaged; the energy is the only global bound, stated as such.
- (C) Viscosity: $\nu>0$ is used throughout (the Stokes operator is the dissipation); the book does not treat the inviscid limit centrally.

### What it gives / does not give

Gives: the definitive weak-solution existence proof on bounded domains, the function-space substrate, the 2D regularity theorem, and the numerical-analysis backing. Does not give: 3D regularity or uniqueness, or any critical-scale control. The natural pairing for the Hopf 1934/1951 dossier and the `_shared` solver interface.

---

## 3. Doering and Gibbon, "Applied Analysis of the Navier-Stokes Equations" (1995)

C. R. Doering, J. D. Gibbon, *Applied Analysis of the Navier-Stokes Equations*, Cambridge Texts in Applied Mathematics, Cambridge University Press (1995). ISBN 0-521-44557-7.

> The most accessible entry to **energy methods, length scales, and the ladder of higher norms**, written for applied mathematicians and physicists. It is the book that makes the supercriticality bookkeeping concrete: it computes the a priori estimates explicitly, tracks the dissipation length scale and the attractor-dimension / degrees-of-freedom counts in physical (Reynolds / Grashof) variables, and builds the "ladder" of $H^n$ estimates that show exactly where the 3D nonlinear term refuses to close. It serves Architecture 1 and is the most direct textbook companion to control (B).

### What it is the best reference for

- The **ladder of norms**: differential inequalities for $H_n = \int |\nabla^n u|^2$ (or the rescaled $F_n$), showing how the nonlinearity couples each rung to higher rungs and where the 3D ladder fails to close while the 2D ladder does. This is the cleanest textbook statement of "the 3D estimate is supercritical."
- **Length scales and the energy cascade**: the Kolmogorov dissipation length, the number of degrees of freedom $N \sim (L/\ell_d)^3 \sim Re^{9/4}$, all derived from the energy/enstrophy budget. Directly relevant to the `energy_spectrum/` experiment.
- Explicit, low-prerequisite derivations of the **energy inequality**, the 2D enstrophy bound, and the Grashof-number attractor-dimension estimates (the applied face of Constantin-Foias).
- Leray's weak-solution theory presented with minimal functional analysis.

### Criticality placement

This book *is* the criticality control in textbook form. Its ladder of $H_n$ inequalities, schematically $\dot H_n \le -\nu \lambda_1 H_n + c\,\|\nabla u\|_{L^\infty} H_n + \dots$, shows the nonlinear feedback is controlled in 2D (enstrophy is an a priori bound, every rung closes) and uncontrolled in 3D (the rung-coupling needs $\|\nabla u\|_{L^\infty}$, which the supercritical energy does not supply, the same gap BKM later names exactly). The dissipation length scale $\ell_d \sim \nu^{3/4}\varepsilon^{-1/4}$ and the count $Re^{9/4}$ are the physical-variable image of the same supercritical scaling.

### Against the three controls

- (A) 2D: the 2D ladder closes in the book; the 3D one does not, on the same page, which is the textbook crystallization of control A.
- (B) Supercriticality: this is the book to cite when you want the supercriticality gap derived from first principles in applied variables.
- (C) Viscosity: the dissipation length and the $\nu$-dependence of every estimate are foregrounded; the inviscid singular limit ($\nu\to0$) is discussed as the hard limit.

### What it gives / does not give

Gives: the most transparent derivation of why energy methods stall in 3D, in language that pairs directly with the `scaling_criticality/` and `energy_spectrum/` experiments. Does not give: critical-space technology or partial regularity (it stays at the energy/enstrophy level by design). The recommended first read for the supercriticality direction.

---

## 4. Majda and Bertozzi, "Vorticity and Incompressible Flow" (2002)

A. J. Majda, A. L. Bertozzi, *Vorticity and Incompressible Flow*, Cambridge Texts in Applied Mathematics 27, Cambridge University Press (2002). ISBN 0-521-63948-7.

> The single best reference tying together the **vorticity formulation, vortex stretching, BKM, and the 2D-vs-3D divide**. If a question is about $\omega$, this is the book. It develops the vorticity equation, the Biot-Savart law, the 3D stretching term $\omega\cdot\nabla u$, the Beale-Kato-Majda breakdown criterion (with full proof of the log-Sobolev inequality), the 2D global theory (Yudovich), and vortex-patch / vortex-sheet weak solutions. It serves Architectures 2 (conditional criteria) and 4 (blow-up / Euler) and is the textbook that most directly engages controls (A) and (C).

### What it is the best reference for

- The **vorticity equation** in both forms,
$$\partial_t\omega + (u\cdot\nabla)\omega = (\omega\cdot\nabla)u + \nu\Delta\omega \quad(\text{3D}), \qquad \partial_t\omega + (u\cdot\nabla)\omega = \nu\Delta\omega \quad(\text{2D, scalar}),$$
with the **stretching term** $(\omega\cdot\nabla)u$ isolated as the sole source of 3D growth. This is the cleanest textbook treatment of *why* 2D is smooth (no stretching, $\omega$ transported with diffusion, $\|\omega\|_{L^p}$ controlled) and why 3D is open.
- The **Beale-Kato-Majda theorem** with full proof, including the logarithmic Sobolev inequality $\|\nabla u\|_{L^\infty} \le C(1 + \|\omega\|_{L^\infty}(1+\log^+\|u\|_{H^s}) + \|\omega\|_{L^2})$. The authoritative source.
- **Local existence in $H^s$** for Euler and Navier-Stokes via the vorticity formulation and the particle-trajectory (Lagrangian) method.
- **2D global existence**: Yudovich's theorem for $\omega_0 \in L^\infty$, and the $L^p$ vorticity theory.
- Weak solutions with **vortex-sheet / vortex-patch** initial data, concentration-cancellation (DiPerna-Majda), and the boundary of the weak Euler theory (context for Architecture 5).

### Criticality placement

The book lives on the vorticity equation, where the criticality story is sharpest. $\|\omega\|_{L^\infty}$ scales like $\lambda^2$ (pointwise in rescaled time) but the BKM integral $\int_0^T \|\omega\|_{L^\infty}\,dt$ is **scale invariant (critical)**, exactly the placement worked out in the BKM dossier. The 2D conserved quantities ($\|\omega\|_{L^p}$ for all $p$, from transport along a measure-preserving flow) are why the 2D ladder closes; the 3D stretching term is the supercritical obstruction. The book is the structural argument that regularity is a statement about the *critical* vorticity integral, not the supercritical energy.

### Against the three controls

- (A) 2D: this is *the* reference for control A. It proves the 2D positive result via the absence of stretching and isolates $\omega\cdot\nabla u$ as the exact 3D-only term. Any method that would predict 2D blow-up contradicts the theory in this book.
- (B) Supercriticality: BKM names the critical target; the book is honest that the energy does not reach it.
- (C) Viscosity: the book treats Euler ($\nu=0$) and Navier-Stokes ($\nu>0$) side by side, so the role of viscosity is visible in every estimate. The Euler local theory and the breakdown question (the modern Elgindi / Chen-Hou singularities) sit here. Best textbook engagement of control C alongside Galdi's steady contrast.

### What it gives / does not give

Gives: the complete vorticity toolkit, BKM with proof, the 2D global theory, and the Euler/NS comparison that makes controls A and C concrete. Does not give: critical-space (Besov/$\mathrm{BMO}^{-1}$) technology or partial regularity (those are Bahouri-Chemin-Danchin and Robinson-Rodrigo-Sadowski respectively). The home reference for Directions 02 (vorticity geometry) and 04 (blow-up and barriers).

---

## 5. Bahouri, Chemin, and Danchin, "Fourier Analysis and Nonlinear Partial Differential Equations" (2011)

H. Bahouri, J.-Y. Chemin, R. Danchin, *Fourier Analysis and Nonlinear Partial Differential Equations*, Grundlehren der mathematischen Wissenschaften 343, Springer (2011). ISBN 978-3-642-16829-1.

> The toolbox reference for the **critical-space program (Architecture 3)**: Littlewood-Paley decomposition, Besov spaces $\dot B^s_{p,q}$, paraproducts and Bony decomposition, and the well-posedness theory of Navier-Stokes built on them. If you need to know what $\dot B^{-1+3/p}_{p,\infty}$ is, why $\mathrm{BMO}^{-1}$ is the largest critical space, and how the bilinear estimate closes the fixed point, this is the book. It engages control (B) from the critical side: it shows where regularity *can* be closed (small critical data) and is silent on large data, which is the supercriticality gap restated.

### What it is the best reference for

- **Littlewood-Paley theory**: dyadic blocks $\Delta_j$, the characterization of homogeneous Besov spaces $\dot B^s_{p,q}$ via $\|2^{js}\|\Delta_j u\|_{L^p}\|_{\ell^q}$, and Bernstein's inequalities. The substrate for every critical-space estimate.
- **Paraproducts and the Bony decomposition** $uv = T_u v + T_v u + R(u,v)$, the tool that tames the Navier-Stokes nonlinearity at low regularity.
- **Critical well-posedness of Navier-Stokes**: local well-posedness and small-data global existence in critical Besov spaces $\dot B^{-1+3/p}_{p,r}(\mathbb{R}^3)$, the Fujita-Kato ($\dot H^{1/2}$) and Kato ($L^3$) results recovered and generalized, up to the neighborhood of $\mathrm{BMO}^{-1}$ (Koch-Tataru).
- The **heat-semigroup smoothing** estimates $\|e^{t\Delta}\Delta_j f\|_{L^p} \lesssim e^{-ct2^{2j}}\|\Delta_j f\|_{L^p}$ that drive the mild-solution fixed point.

### Criticality placement

This is the book of the **critical line $a=0$**. Every space it features for Navier-Stokes, $\dot H^{1/2}$, $L^3$, $\dot B^{-1+3/p}_{p,\infty}$, $\mathrm{BMO}^{-1}$, $\dot B^{-1}_{\infty,\infty}$ (the ill-posed edge, Bourgain-Pavlovic), has scaling exponent exactly $0$ under $u_\lambda(x,t)=\lambda u(\lambda x,\lambda^2 t)$. The criticality bookkeeper returns `CRITICAL` for all of them. The book's reach is the positive half of the supercriticality story: at criticality the fixed point closes for *small* data, and the technology says nothing about large data, which is the gap.

### Against the three controls

- (A) 2D: the Littlewood-Paley machinery is dimension-agnostic; the book does not foreground the 2D control, though the critical exponents shift with dimension. Neutral on A.
- (B) Supercriticality: engaged from the critical side. The book is where you see that criticality is reachable only for small data, which is the precise boundary the energy cannot cross for large data.
- (C) Viscosity: the heat semigroup $e^{t\Delta}$ is the engine; the smoothing is exactly the viscous parabolic gain. The inviscid Euler critical theory (transport estimates, $\log$-loss) is also developed, so the contrast with $\nu>0$ is visible. Touches the edge of C.

### What it gives / does not give

Gives: the full critical-space / paradifferential toolkit and the small-data global theory at every critical scale up to $\mathrm{BMO}^{-1}$. Does not give: large-data regularity (smallness is essential to the fixed point), partial regularity, or the vorticity-geometry criteria. The home reference for Directions 01 (critical continuation) and the critical-space half of 03 (supercriticality gap). Pairs with the Fujita-Kato, Koch-Tataru, and Bourgain-Pavlovic dossiers.

---

## 6. Robinson, Rodrigo, and Sadowski, "The Three-Dimensional Navier-Stokes Equations: Classical Theory" (2016)

J. C. Robinson, J. L. Rodrigo, W. Sadowski, *The Three-Dimensional Navier-Stokes Equations: Classical Theory*, Cambridge Studies in Advanced Mathematics 157, Cambridge University Press (2016). ISBN 978-1-107-01966-9.

> The cleanest **modern, self-contained, proof-complete** graduate text on 3D classical theory. It is the book to put in a student's hands: weak solutions, local existence of strong solutions, weak-strong uniqueness, the Prodi-Serrin conditional criteria, the Leray structure theorem on the singular set, and a full account of partial regularity (CKN), all with proofs and consistent notation. It serves Architectures 1 and 2 and engages controls (A) and (B) with full rigor. It is the natural backbone for the VERIFIER's Lean targets because the proofs are stated at a level a formalization can track.

### What it is the best reference for

- **Weak (Leray-Hopf) solutions** existence with full proof, and the energy inequality, on $\mathbb{T}^3$ and $\mathbb{R}^3$.
- **Local existence and uniqueness of strong solutions** in $H^1$ (and $\dot H^{1/2}$), the maximal-existence-time theory, and the blow-up rate $\|\nabla u(t)\|_{L^2} \gtrsim (T^*-t)^{-1/4}$ at a putative singularity.
- **Weak-strong uniqueness**: a weak solution coincides with a strong solution as long as the strong one exists (the Serrin / Prodi argument), proved cleanly.
- The **Prodi-Serrin-Ladyzhenskaya conditional regularity criteria** $u\in L^p_t L^q_x$, $2/p+3/q\le 1$, $q>3$, with proof, and discussion of the $q=3$ endpoint (ESS, stated).
- **Leray's structure theorem**: the set of singular times has $\tfrac12$-dimensional Lebesgue measure zero, and eventual regularity.
- **Partial regularity (CKN)**: a full, modern account of the local energy inequality, suitable weak solutions, and the $\varepsilon$-regularity theorem giving $\mathcal{P}^1(S)=0$.

### Criticality placement

The book is organized so the reader sees the criticality scale directly. The unconditional results (weak existence, partial regularity) run on the **supercritical** energy ($a=-1/2$); the conditional criteria (Prodi-Serrin) and the strong-solution local theory live at or above **critical** ($\dot H^{1/2}$ is $a=0$; $L^p_tL^q_x$ on the line $2/p+3/q=1$ is critical). The blow-up rate $(T^*-t)^{-1/4}$ for $\|\nabla u\|_{L^2}$ is the scaling-consistent rate, and the book derives it from the supercritical-to-critical mismatch. It is the most explicit textbook walk from supercritical (what we have) to critical (what we need).

### Against the three controls

- (A) 2D: the 3D theory is presented against the 2D backdrop; the strong-solution theory is exactly where 3D and 2D part. Passes A.
- (B) Supercriticality: foregrounded. The book's structure is the supercriticality gap made into a curriculum: unconditional results are supercritical, conditional results are critical, and the gap between them is the open problem.
- (C) Viscosity: $\nu>0$ throughout; the parabolic smoothing is used in the strong-solution and partial-regularity theory. Not centrally contrasted with Euler (see Majda-Bertozzi for that).

### What it gives / does not give

Gives: the complete modern classical theory with proofs, in one consistent notation, including partial regularity. The best single book for Directions 01 and the partial-regularity strand, and the best source text for VERIFIER (Lean) targets. Does not give: critical-space Besov technology (Bahouri-Chemin-Danchin) or the vorticity-geometry criteria (Majda-Bertozzi, Constantin-Fefferman). Pairs with the Leray, Hopf, Prodi-Serrin, ESS, and CKN dossiers.

---

## 7. Galdi, "An Introduction to the Mathematical Theory of the Navier-Stokes Equations: Steady-State Problems" (1994 / 2011)

G. P. Galdi, *An Introduction to the Mathematical Theory of the Navier-Stokes Equations: Steady-State Problems*, Springer Monographs in Mathematics, 2nd ed., Springer (2011); originally two volumes, Springer Tracts in Natural Philosophy 38, 39 (1994). ISBN 978-0-387-09619-3.

> The definitive reference for the **steady (stationary) Navier-Stokes problem**, $-\nu\Delta u + (u\cdot\nabla)u + \nabla p = f$, $\nabla\cdot u = 0$, with no time derivative. It is the place for existence, uniqueness (for small data / small Reynolds number), regularity, and the delicate asymptotic / exterior-domain theory (the Stokes and Oseen fundamental solutions, the Stokes paradox in 2D, leading-order wake structure). It is a different control regime: with no time evolution there is no finite-time blow-up to fear, so the steady problem is *well-posed and regular* under broad hypotheses, and it serves as the elliptic backbone (the Stokes problem) that the time-dependent theory is built on.

### What it is the best reference for

- The **Stokes problem** $-\Delta u + \nabla p = f$, $\nabla\cdot u = 0$: existence, uniqueness, and the full $L^q$ and Schauder regularity theory, including the **Helmholtz-Weyl / Leray decomposition** $L^q = L^q_\sigma \oplus G^q$ (solenoidal plus gradient) on general domains, which is the rigorous foundation of the Leray projector $P$.
- **Steady Navier-Stokes** existence (Leray's method, via the Leray-Schauder degree / fixed point) and uniqueness for small force or small Reynolds number.
- **Exterior-domain asymptotics**: the Oseen fundamental tensor, the structure of the wake, summability and pointwise decay of $u$, the 2D **Stokes paradox** (no bounded solution to the 2D exterior Stokes problem with prescribed velocity at infinity) and its Navier-Stokes resolution.
- The **$L^q$ theory of the Stokes operator** in its stationary form, the elliptic regularity that feeds Sohr's parabolic $L^p$ theory.

### Criticality placement

The steady problem removes the time-scaling axis. Under the spatial scaling $u(x)\mapsto \lambda u(\lambda x)$, steady Navier-Stokes is invariant, and the natural energy space is $\dot H^1$ (Dirichlet integral), which is the *critical* space for the steady problem in 3D. There is no supercriticality gap of the time-dependent kind: the steady estimates close because there is no time to integrate a supercritical bound over. This makes Galdi the contrast case for control (B): it shows that the obstruction in the evolutionary problem is genuinely the *time* axis (accumulation toward a singular time), not the spatial nonlinearity in isolation.

### Against the three controls

- (A) 2D: the 2D steady theory (Stokes paradox, and the subtle existence theory for the 2D exterior Navier-Stokes problem) is a major theme; the 2D/3D contrast is sharp but in the steady setting. Engages A in a distinct register.
- (B) Supercriticality: the steady problem has no finite-time blow-up, so the supercriticality gap as the project means it does not arise. Galdi is the reference that isolates *which* difficulty is time-dependent.
- (C) Viscosity: $\nu>0$ is essential (the Stokes/Oseen fundamental solutions are viscous objects; the inviscid steady problem is a different, ill-conditioned object). Engaged.

### What it gives / does not give

Gives: the complete steady-state and Stokes/Oseen elliptic theory, the Helmholtz decomposition and Leray-projector foundations, and the exterior-domain asymptotics. Does not give: any time-dependent regularity result, hence nothing directly about the Clay problem's blow-up question. Its role is foundational (the elliptic substrate) and contrastive (it shows the blow-up risk is an evolutionary phenomenon). Background for Architecture 1 and the function-space foundations.

---

## 8. Sohr, "The Navier-Stokes Equations: An Elementary Functional Analytic Approach" (2001)

H. Sohr, *The Navier-Stokes Equations: An Elementary Functional Analytic Approach*, Birkhauser Advanced Texts (2001); Modern Birkhauser Classics reprint (2013). ISBN 978-3-0348-0550-6 (reprint).

> The reference for the **$L^q$ / Stokes-semigroup theory**: the Helmholtz decomposition in $L^q$, the Stokes operator $A_q$ as the generator of a bounded analytic semigroup $e^{-tA_q}$ on $L^q_\sigma$, the maximal $L^p$-$L^q$ regularity estimates, and the construction of weak and strong solutions in the $L^q$ framework on general (including unbounded) domains. It is the bridge between the Hilbert-space ($L^2$) theory of Temam / Constantin-Foias and the critical-space ($L^3$, Besov) theory of Bahouri-Chemin-Danchin: the $L^q$ smoothing estimates are what make $L^3$ and the Serrin exponents work. Serves Architectures 1, 2, and 3.

### What it is the best reference for

- The **Helmholtz decomposition $L^q(\Omega) = L^q_\sigma(\Omega) \oplus G^q(\Omega)$** for $1<q<\infty$ on a wide class of domains, and the boundedness of the Leray projector $P_q$ on $L^q$ (a Calderon-Zygmund / Mikhlin-multiplier result), with the precise hypotheses on the domain.
- The **Stokes operator $A_q = -P_q\Delta$** on $L^q_\sigma$ as the generator of a bounded analytic semigroup, with the smoothing estimates $\|A_q^\alpha e^{-tA_q} f\|_{L^q} \lesssim t^{-\alpha}\|f\|_{L^q}$ and the $L^p$-$L^q$ decay $\|e^{-tA_q}f\|_{L^r} \lesssim t^{-\frac{3}{2}(\frac1q-\frac1r)}\|f\|_{L^q}$. These are the engine behind every mild-solution construction.
- **Maximal $L^p$-$L^q$ regularity** for the nonstationary Stokes system: $\|u_t\|_{L^p_tL^q_x} + \|A_q u\|_{L^p_tL^q_x} \lesssim \|f\|_{L^p_tL^q_x}$, the parabolic estimate that controls the linear part at the Serrin scaling.
- Construction of **weak solutions** (the energy class) and **strong / mild solutions** in $L^q$, and the Serrin-type regularity and uniqueness in the $L^q$ framework, all from the semigroup estimates.

### Criticality placement

Sohr supplies the *machinery* at every scaling level rather than living at one. The $L^p$-$L^q$ smoothing estimates are scaling-covariant: the decay exponent $\tfrac{3}{2}(\tfrac1q-\tfrac1r)$ is exactly what the scaling $u_\lambda$ predicts, which is why these estimates make the **critical** Serrin line $2/p+3/q=1$ and the **critical** space $L^3$ work in the mild-solution theory. The weak-solution side runs on the **supercritical** energy. So the book is the toolbox that connects the supercritical energy theory to the critical mild-solution theory through quantitative semigroup decay. It is where the criticality bookkeeper's exponents are realized as actual estimates.

### Against the three controls

- (A) 2D: the $L^q$ framework is dimension-general; Sohr is not primarily a 2D-vs-3D book. Neutral on A.
- (B) Supercriticality: engaged as the bridge. The semigroup estimates are how one *attempts* to upgrade supercritical energy control to critical control; they succeed for small data (matching Bahouri-Chemin-Danchin) and stall for large data.
- (C) Viscosity: the analytic semigroup $e^{-tA_q}$ *is* the viscous smoothing; the entire book is a quantitative account of what $\nu>0$ buys. The strongest implicit engagement of C among the functional-analytic texts (inviscid has no analytic Stokes semigroup).

### What it gives / does not give

Gives: the definitive $L^q$ / Stokes-semigroup / maximal-regularity toolkit and the mild-solution construction at the Serrin scaling, on general domains. Does not give: large-data 3D regularity, or the vorticity-geometry and convex-integration material. The home reference for the linear-estimate substrate underneath Architectures 2 and 3, and the technical companion to the Fujita-Kato, Kato, and ESS dossiers.

---

## Cross-cutting summary: which book for which job

| If you need ... | Open ... |
|---|---|
| Leray-Hopf weak-solution existence with proof | Temam (bounded domain), Robinson-Rodrigo-Sadowski ($\mathbb{T}^3,\mathbb{R}^3$) |
| The Stokes operator $A$, fractional powers, Helmholtz decomposition | Constantin-Foias ($L^2$), Sohr ($L^q$), Galdi (steady/elliptic) |
| The supercriticality gap derived in applied variables | Doering-Gibbon |
| BKM, vortex stretching, the 2D-vs-3D mechanism | Majda-Bertozzi |
| Critical-space (Besov, $\mathrm{BMO}^{-1}$) well-posedness | Bahouri-Chemin-Danchin |
| Partial regularity (CKN), Prodi-Serrin, with full proofs | Robinson-Rodrigo-Sadowski (and Seregin's 2014 lecture notes) |
| The steady problem, exterior domains, Stokes/Oseen asymptotics | Galdi |
| $L^p$-$L^q$ semigroup smoothing, maximal regularity, mild solutions | Sohr |
| 2D attractor and turbulence degrees of freedom (rigorous) | Constantin-Foias, Doering-Gibbon |
| Numerical-analysis backing for the DNS thread | Temam |

Two recurring readings tie the map to the project spine:

1. **Every functional-analytic textbook (Constantin-Foias, Temam, Robinson-Rodrigo-Sadowski, Sohr) closes the 2D theory and stalls in 3D at the same place**: the only global a priori bound is the energy ($a=-1/2$, supercritical), and the 2D-only interpolation (Ladyzhenskaya's $L^4$ inequality, or equivalently the absence of vortex stretching) is what lets 2D close. This is control (B), control (A), and the supercriticality gap, all reading the same boundary from inside three different toolkits.
2. **The critical-side books (Bahouri-Chemin-Danchin, Sohr's mild-solution chapters) close the small-data theory at $a=0$ and say nothing about large data.** This is the positive half of the supercriticality story: criticality is reachable, but only when smallness substitutes for the missing large-data a priori bound. Galdi is the contrast that isolates the time axis as the true seat of the blow-up risk.

## What this enables / what remains open

**Enables.**
- A one-lookup routing table so BUILDER can find the sharpest available form of a needed estimate (semigroup decay in Sohr, the ladder in Doering-Gibbon, BKM in Majda-Bertozzi) without re-deriving it.
- A source-text recommendation for the VERIFIER: Robinson-Rodrigo-Sadowski states the classical-theory proofs at the granularity a Lean formalization can track, and Temam / Sohr supply the function-space lemmas (Helmholtz decomposition, Stokes operator) those proofs depend on.
- A confirmation, from four independent functional-analytic traditions, that the supercriticality gap is not an artifact of one method: it is where 2D-to-3D closure fails in the Galerkin theory (Temam), the attractor theory (Constantin-Foias), the ladder-of-norms theory (Doering-Gibbon), and the classical strong-solution theory (Robinson-Rodrigo-Sadowski) alike.

**Remains open (and is each book's silence).**
- No book here closes 3D large-data regularity; each is a complete account of one *side* of the gap (supercritical unconditional, or critical small-data).
- The vorticity-geometry criteria (Constantin-Fefferman) and the quantitative-regularity / concentration program (Tao 2019, Barker-Prange) are newer than most of these texts and are not in any of them; they live in the single-paper dossiers and Directions 02 and 04.
- The convex-integration boundary (Architecture 5) is outside every textbook here; it is post-2019 and sits below the energy class these books are built on.
- A genuinely critical *large-data* a priori bound, the missing ingredient, is in none of these books because it does not yet exist. The map says exactly which book each *partial* ingredient is in; assembling them across the gap is the open problem.

## References

- P. Constantin, C. Foias, *Navier-Stokes Equations*, Chicago Lectures in Mathematics, University of Chicago Press (1988).
- R. Temam, *Navier-Stokes Equations: Theory and Numerical Analysis*, North-Holland (1977); AMS Chelsea reprint (2001). Companion: *Navier-Stokes Equations and Nonlinear Functional Analysis*, CBMS-NSF 66, SIAM (2nd ed. 1995).
- C. R. Doering, J. D. Gibbon, *Applied Analysis of the Navier-Stokes Equations*, Cambridge Texts in Applied Mathematics, Cambridge University Press (1995).
- A. J. Majda, A. L. Bertozzi, *Vorticity and Incompressible Flow*, Cambridge Texts in Applied Mathematics 27, Cambridge University Press (2002).
- H. Bahouri, J.-Y. Chemin, R. Danchin, *Fourier Analysis and Nonlinear Partial Differential Equations*, Grundlehren der mathematischen Wissenschaften 343, Springer (2011).
- J. C. Robinson, J. L. Rodrigo, W. Sadowski, *The Three-Dimensional Navier-Stokes Equations: Classical Theory*, Cambridge Studies in Advanced Mathematics 157, Cambridge University Press (2016).
- G. P. Galdi, *An Introduction to the Mathematical Theory of the Navier-Stokes Equations: Steady-State Problems*, Springer Monographs in Mathematics, 2nd ed., Springer (2011); orig. two volumes, Springer Tracts in Natural Philosophy 38, 39 (1994).
- H. Sohr, *The Navier-Stokes Equations: An Elementary Functional Analytic Approach*, Birkhauser Advanced Texts (2001); Modern Birkhauser Classics reprint (2013).
- (Adjacent, not mapped above but cited for completeness.) P.-L. Lions, *Mathematical Topics in Fluid Mechanics, Vol. 1: Incompressible Models*, Oxford Lecture Series 3 (1996); C. Foias, O. Manley, R. Rosa, R. Temam, *Navier-Stokes Equations and Turbulence*, Encyclopedia of Mathematics and its Applications 83, Cambridge (2001); P. G. Lemarie-Rieusset, *The Navier-Stokes Problem in the 21st Century*, CRC Press (2016; 2nd ed. 2024); G. Seregin, *Lecture Notes on Regularity Theory for the Navier-Stokes Equations*, World Scientific (2014).

## Cross-links

- Direction 01 (critical continuation criteria), served by Robinson-Rodrigo-Sadowski (Prodi-Serrin with proofs) and Bahouri-Chemin-Danchin (critical-space technology): [`../research_directions/01_critical_continuation_criteria.md`](../research_directions/01_critical_continuation_criteria.md).
- Direction 02 (vorticity geometry), served by Majda-Bertozzi (vorticity formulation, stretching, BKM): [`../research_directions/02_vorticity_geometry.md`](../research_directions/02_vorticity_geometry.md).
- Direction 03 (the supercriticality gap), served by Doering-Gibbon (the ladder, applied variables) and Constantin-Foias (the attractor / dimension side): [`../research_directions/03_supercriticality_gap.md`](../research_directions/03_supercriticality_gap.md).
- Direction 04 (blow-up and barriers), served by Majda-Bertozzi (Euler local theory and breakdown) and Galdi (the steady contrast that isolates the time axis): [`../research_directions/04_blowup_and_barriers.md`](../research_directions/04_blowup_and_barriers.md).
- Direction 05 (convex integration boundary), outside every textbook here (post-2019, below the energy class): [`../research_directions/05_convex_integration_boundary.md`](../research_directions/05_convex_integration_boundary.md).
- Sibling note BKM (1984), proved in full in Majda-Bertozzi: [`./beale_kato_majda_1984.md`](./beale_kato_majda_1984.md).
- Sibling note ESS (2003), whose $L^q$ semigroup substrate is Sohr and whose critical-space companions are in Bahouri-Chemin-Danchin: [`./escauriaza_seregin_sverak_2003.md`](./escauriaza_seregin_sverak_2003.md).
- Sibling notes Leray (1934) and Hopf (1951), whose Galerkin / weak-solution machinery is Temam and Robinson-Rodrigo-Sadowski: [`./leray_1934.md`](./leray_1934.md), [`./hopf_1951.md`](./hopf_1951.md).
- Sibling notes Fujita-Kato (1964) and Koch-Tataru (2001), whose critical-space toolkit is Bahouri-Chemin-Danchin and whose semigroup estimates are Sohr: [`./fujita_kato_1964.md`](./fujita_kato_1964.md), [`./koch_tataru_2001.md`](./koch_tataru_2001.md).
- Sibling note CKN (1982), with the modern partial-regularity account in Robinson-Rodrigo-Sadowski: [`./caffarelli_kohn_nirenberg_1982.md`](./caffarelli_kohn_nirenberg_1982.md).
- The full reference index: [`../../../references/README.md`](../../../references/README.md). The criticality bookkeeper: `experiments/_shared/criticality.py`.
