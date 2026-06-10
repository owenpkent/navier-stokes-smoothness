# Cross-architecture findings

The synthesis surface. Each finding is a structural insight that cuts across the experimental thread, written so a future session can pick up the narrative. Numbered for stable reference.

The dominant meta-finding is **the supercriticality of the energy estimate**: the only all-time a priori bound is supercritical with respect to the scaling, so it cannot reach a regularity statement on its own. Everything below either sharpens this or maps a consequence of it.

---

## #1 The energy estimate is supercritical (the central finding)

Source: `scaling_criticality/criticality_table.py`, `_shared/criticality.py`.

The energy inequality

$$\tfrac12\|u(t)\|_{L^2}^2 + \nu\int_0^t \|\nabla u\|_{L^2}^2\,ds \le \tfrac12\|u_0\|_{L^2}^2$$

is the only coercive a priori bound that holds for all time in 3D. The norm it controls, $\|u\|_{L^2}$, has scaling exponent $-1/2$ under $u_\lambda(x,t)=\lambda u(\lambda x,\lambda^2 t)$: it is **supercritical**. Supercritical means the norm carries no information at the small scales where a singularity would form. Regularity is a critical-or-subcritical statement (every regularity criterion sits at exponent $0$). So energy methods, by themselves, cannot close regularity. This is not a heuristic: it is the scaling arithmetic, verified in the bookkeeper and reproduced in the smoke test. It is the compass for the whole project.

## #2 The regularity criteria all sit exactly at critical

Source: `scaling_criticality/`, literature (Prodi-Serrin-Ladyzhenskaya, Beale-Kato-Majda, Escauriaza-Seregin-Sverak).

$\dot H^{1/2}$, $L^3$, $\mathrm{BMO}^{-1}$, and the BKM vorticity integral all have scaling exponent $0$ (critical). This is not a coincidence: a regularity criterion has to be scale invariant, because regularity is preserved by the scaling. The consequence is sharp: the gap between the supercritical bound we have (energy) and the critical control we need (any of these) is a gap in scaling weight, not just in technique. Closing it requires a genuinely new, scaling-critical a priori bound. No such bound is known.

## #3 2D closes because the enstrophy bound is available there

Source: `_shared/flow.py` (`Flow2D`), smoke test Test 5, literature (Ladyzhenskaya 1959).

In 2D the vorticity is a scalar transported with diffusion and **no stretching term**, so $\tfrac{d}{dt}\int\omega^2 \le 0$: the enstrophy is non-increasing. That is a subcritical ($H^1$) a priori bound, and it closes regularity in 2D. The smoke test confirms the enstrophy decreasing on a random 2D field. The 3D obstruction is exactly the stretching term $\omega\cdot\nabla u$ in the vorticity equation, which has no 2D analog. CONSEQUENCE (the 2D control): any 3D regularity mechanism that does not genuinely engage vortex stretching would apply in 2D too, where it is unnecessary, which marks it as not the real mechanism.

## #4 Viscosity is what prevents gradient blow-up

Source: `burgers_shock/burgers_blowup.py`.

The 1D Burgers equation carries the same quadratic transport nonlinearity as NS. Inviscid Burgers from $u_0=\sin x$ forms a shock at $t^*=1$ (gradient diverges; the experiment reaches $\max|u_x|\sim$ hundreds), while viscous Burgers stays smooth ($\max|u_x|$ saturates near $8$). CONSEQUENCE (the viscosity control): a regularity argument blind to the viscous term cannot be right, because the inviscid relative is singular. This is reinforced by the fact that 3D Euler (the true inviscid relative of NS) admits finite-time singularities (Elgindi 2021) and is numerically supported in others (Hou-Luo, Chen-Hou). The NS regularity question is precisely a question about what $\nu\Delta u$ buys.

## #5 The non-singular baseline is consistent and the solver respects the structure

Source: `taylor_green/taylor_green_dns.py`.

At $32^3$, $\nu=0.025$ (Re ~ 40) the Taylor-Green vortex relaxes smoothly: energy dissipates monotonically (the energy inequality holds numerically), the BKM integral stays finite ($\approx 4.4$ to $t=3$), and incompressibility is held at machine precision ($\max|\nabla\cdot u|\sim 10^{-17}$). This validates the solver against the analytic a priori structure and provides the baseline for resolution studies. It is NOT evidence for global regularity. Numerics can suggest where to look, never decide the problem, and the criticality control (#1) applies regardless: the energy bound that holds here is supercritical.

## #6 The dissipation lives at small scales, where control is absent

Source: `energy_spectrum/energy_spectrum.py`.

The energy spectrum $E(k)$ peaks at low $k$ (large scales, where the a priori bound holds), but the dissipation integrand $k^2 E(k)$ is weighted toward high $k$ (small scales, where a singularity would form and where finite resolution bites first). This is the spectral face of the supercriticality gap (#1): the conserved quantity and the dangerous scales live at opposite ends of the spectrum. The wavenumber where $E(k)$ drops below grid resolution is the numerical boundary of what a DNS can see, which is the computational shadow of the analytic gap.

## #7 The blow-up side has barriers, not examples (and one caricature does blow up)

Source: literature (Leray; Necas-Ruzicka-Sverak; Tsai; Tao 2016), mapped in `docs/research_atlas/`.

No finite-time singularity is known for 3D Navier-Stokes. Leray's self-similar ansatz is ruled out in $L^3$ (Necas-Ruzicka-Sverak 1996; Tsai 1998). But Tao (2016) built finite-time blow-up for an **averaged** Navier-Stokes that preserves the energy identity and the scaling. CONSEQUENCE: a regularity proof cannot rely only on the energy identity and scaling, because the averaged caricature has both and still blows up. The proof must use a structural feature of the true nonlinearity that the averaged version destroys. This sharpens #1: the missing control must be specific to the exact 3D transport-and-pressure structure, not a soft consequence of energy plus scaling.

## #8 Non-uniqueness below the energy class fixes the solution concept

Source: literature (Buckmaster-Vicol 2019; Isett 2018; Onsager), mapped in `docs/research_atlas/`.

Convex integration produces non-unique weak solutions below the Leray-Hopf class. This does not bear directly on smoothness of the strong flow, but it is a coordinate: it says the Leray-Hopf class (finite energy, energy inequality) is the right class in which to ask the regularity question, and that dropping below it loses uniqueness. The regularity problem and the non-uniqueness phenomena live at different regularity levels, separated by the Onsager-type threshold. Keeping them distinct prevents a category error.

## #9 The criticality arithmetic predicts dynamics (dyadic shell scan)

Source: `dyadic_shell/criticality_scan.py`.

In the dyadic cascade $\dot a_n = \lambda^n a_{n-1}^2 - \lambda^{n+1} a_n a_{n+1} - \nu \lambda^{2\alpha n} a_n$ (energy-conserving nonlinearity, the Katz-Pavlovic / Cheskidov model family), flux balance on the constant-flux profile $a_n \sim \lambda^{-n/3}$ predicts a sharp boundary at $\alpha_c = 1/3$: dissipation outruns the cascade above it, the cascade outruns dissipation below it. The scan confirms it dynamically: finite-time blow-up (geometrically converging shell-arrival times, ratio $0.638$ vs the predicted $\lambda^{-2/3} = 0.630$) for $\alpha \le 1/3$, front stall for $\alpha \ge 0.36$, at fixed $\nu = 0.1$ over 40 shells. CONSEQUENCE: the bookkeeper's sub/critical/super classification is not metaphor; in a system where the dial is explicit, the classification **is** the boundary between singular and regular dynamics. This is also #7 in miniature, watchable: the model keeps the energy identity and still blows up on the supercritical side, so whatever saves NS must come from structure the caricature destroys (transport, pressure, phase cancellation, geometry).

## #10 Stretching is geometrically depleted and the vorticity direction is coherent (observed, not forced)

Source: `vortex_stretching/alignment_depletion.py`.

Along a Taylor-Green run ($32^3$, $\nu = 0.01$) the enstrophy budget $dZ/dt = \int \omega \cdot S\omega - \nu\int|\nabla\omega|^2$ verifies to $<1\%$ in the resolved window, with production exceeding dissipation for an extended interval while the flow stays smooth. Two geometric facts accompany this: the realized stretching is only $\approx 0.53$ of the pointwise-maximal $\int \lambda_3|\omega|^2$ (depletion), and the direction field $\xi = \omega/|\omega|$ has $|\nabla\xi|$ far below the Nyquist scale in the high-vorticity region (Constantin-Fefferman coherence). One honest nuance: the classical turbulence statistic is alignment with the intermediate strain eigenvector $e_2$, but this laminar symmetric flow aligns with the extensional $e_3$ at mid-run and is depleted anyway, so depletion is not reducible to the $e_2$ story. CONSEQUENCE: the CF criterion conditionalizes exactly what is observed here; the open problem in these coordinates is to prove the depletion is **forced** by the equation a priori. The 2D control ran alongside (production structurally zero, enstrophy non-increasing), so the experiment engages only the genuinely 3D term. A second use: the budget residual grows ($0.65\% \to 36\%$) precisely when the grid stops resolving the cascade, giving a built-in resolution alarm (the dynamical face of #6).

## #11 The BKM integral converges under refinement at laptop parameters (the instrument is calibrated)

Source: `resolution_study/bkm_refinement.py`.

Grid refinement $16^3 \to 24^3 \to 32^3$ at $\nu \in \{0.025, 0.01\}$: the BKM integral $\int_0^3 \|\omega\|_\infty\,dt$ converges (successive change below tolerance at the finest pair), and the critical norms $\|u\|_{L^3}$, $\|u\|_{\dot H^{1/2}}$ stay bounded along every run, consistent with ESS. This is calibration, not evidence about the supercritical regime: it fixes the signature a real candidate singularity must show (BKM growth that **survives** refinement) and confirms the instrument reads CONVERGED in the known-smooth regime. CONSEQUENCE: future near-singular scenarios (Hou-Luo-type data) have a well-defined pass/fail readout.

---

## Reading of the findings together

The findings converge on one statement: a proof of 3D Navier-Stokes global regularity must supply a **coercive, scaling-critical a priori bound** that (i) is derived from the data and the equation, (ii) controls a BKM/PSL quantity for all time, (iii) genuinely uses 3D vortex stretching (so it has no 2D analog, #3), (iv) uses the viscous term (#4), and (v) survives the averaged caricature (#7), i.e. uses the exact structure of the nonlinearity rather than energy-plus-scaling alone. No such bound is known. That is the open problem, stated as sharply as the experiments can state it. The supercriticality gap (#1) is the compass; the controls (#3, #4, #7) are the fences that keep a candidate honest.
