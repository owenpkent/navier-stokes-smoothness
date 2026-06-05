# Reference library

Annotated index of the key references for the Navier-Stokes existence and smoothness problem. PDFs are gitignored (copyrighted); this tracked index records the bibliography, the role each source plays, and which research direction, architecture, or wrong-approach control it informs. Reading notes for the load-bearing sources are in [`../docs/03_research/reading_notes/`](../docs/03_research/reading_notes/).

## How to read this index

Sources are grouped by the project's five candidate proof architectures plus cross-cutting categories. For each source: full citation (authors, exact title, journal/venue, volume, year) and a one-to-two sentence ROLE. The ROLE names what the source contributes and which architecture (1 through 5), research direction, or structural control (2D smoothness, criticality, viscosity) it informs.

The three structural controls referenced below:
- **2D control**: 2D NS is globally smooth, so any method must genuinely use 3D vortex stretching $\omega \cdot \nabla u$.
- **Criticality control**: the energy norm is supercritical under the scaling $u_\lambda(x,t) = \lambda\, u(\lambda x, \lambda^2 t)$; a regularity proof must add genuinely critical control.
- **Viscosity control**: inviscid models (Burgers, Euler) blow up, so the viscous structure is essential and a method blind to it is suspect.

Items marked "(verify)" have a citation detail (volume, page, year) not yet cross-checked against the published version.

## The problem statement

| Source | Role |
|---|---|
| C. L. Fefferman, "Existence and smoothness of the Navier-Stokes equation," Clay Mathematics Institute Millennium Prize Problem description (2000; revised 2006) | The official problem statement. Defines the target (existence-and-smoothness on $\mathbb{R}^3$ or $\mathbb{T}^3$) and the four acceptable statements (A, B existence/smoothness; C, D breakdown). Fixes the rules of the game for every architecture. |
| O. A. Ladyzhenskaya, "The sixth millennium problem: Navier-Stokes equations, existence and smoothness," Russian Math. Surveys 58 (2003), 251-286 | An expository framing of the Clay problem by a founder of the rigorous theory. Useful orientation on what is and is not known and on the 2D vs 3D divide (2D control). |

## Foundational existence and partial regularity (Architecture 1: energy methods and weak solutions)

| Source | Role |
|---|---|
| J. Leray, "Sur le mouvement d'un liquide visqueux emplissant l'espace," Acta Math. 63 (1934), 193-248 | Global weak ("turbulent") solutions exist on $\mathbb{R}^3$; the energy inequality; the first self-similar blow-up ansatz. The origin of Architecture 1 and the energy that the criticality control flags as supercritical. |
| E. Hopf, "Uber die Anfangswertaufgabe fur die hydrodynamischen Grundgleichungen," Math. Nachr. 4 (1951), 213-231 | Global weak solutions on bounded and general domains via Galerkin approximation; the Leray-Hopf class is named jointly for this and Leray 1934. The functional-analytic backbone of Architecture 1. |
| L. Caffarelli, R. Kohn, L. Nirenberg, "Partial regularity of suitable weak solutions of the Navier-Stokes equations," Comm. Pure Appl. Math. 35 (1982), 771-831 | The singular set of a suitable weak solution has parabolic Hausdorff measure $\mathcal{P}^1 = 0$; the $\varepsilon$-regularity method via the local energy inequality. The strongest unconditional partial-regularity result; stops exactly where supercriticality stops it (small singular set, not empty). |
| V. Scheffer, "Partial regularity of solutions to the Navier-Stokes equations," Pacific J. Math. 66 (1976), 535-552 | The pre-CKN partial-regularity program (Hausdorff dimension bounds on the singular set). The historical predecessor that CKN sharpened. Informs Architecture 1. |
| F.-H. Lin, "A new proof of the Caffarelli-Kohn-Nirenberg theorem," Comm. Pure Appl. Math. 51 (1998), 241-257 | A streamlined compactness proof of the CKN partial-regularity bound. The standard modern reference for the $\varepsilon$-regularity machinery used across Architectures 1 and 2. |

## Conditional regularity criteria (Architecture 2)

| Source | Role |
|---|---|
| G. Prodi, "Un teorema di unicita per le equazioni di Navier-Stokes," Ann. Mat. Pura Appl. 48 (1959), 173-182 | The uniqueness half of the Prodi-Serrin condition $u \in L^p_t L^q_x$, $2/p + 3/q \le 1$. A foundational conditional criterion at the critical scaling line (criticality control). |
| J. Serrin, "On the interior regularity of weak solutions of the Navier-Stokes equations," Arch. Rational Mech. Anal. 9 (1962), 187-195 | The interior-regularity half of the Prodi-Serrin condition. Establishes that subcritical $L^p_t L^q_x$ control ($2/p + 3/q < 1$) forces smoothness; the subcritical boundary of Architecture 2. |
| O. A. Ladyzhenskaya, "The Mathematical Theory of Viscous Incompressible Flow," 2nd ed., Gordon and Breach (1969) | The rigorous 2D global-regularity theory and the 3D conditional criteria in book form. The canonical statement of the 2D control (no vortex stretching, enstrophy non-increasing). |
| J. T. Beale, T. Kato, A. Majda, "Remarks on the breakdown of smooth solutions for the 3-D Euler equations," Comm. Math. Phys. 94 (1984), 61-66 | The vorticity blow-up criterion: smoothness persists on $[0,T]$ iff $\int_0^T \|\omega(t)\|_{L^\infty}\, dt < \infty$. The sharpest qualitative continuation criterion; central to Architectures 2 and 4 and to the viscosity control via the Euler connection. |
| H. Kozono, Y. Taniuchi, "Limiting case of the Sobolev inequality in BMO, with application to the Euler equations," Comm. Math. Phys. 214 (2000), 191-200 | Sharpens BKM by replacing $\|\omega\|_{L^\infty}$ with the weaker $\|\omega\|_{\mathrm{BMO}}$, using a log-type endpoint Sobolev inequality. The BMO endpoint of the BKM criterion; informs Architecture 2 and the geometric/vorticity direction. |
| L. Escauriaza, G. Seregin, V. Sverak, "$L_{3,\infty}$-solutions of Navier-Stokes equations and backward uniqueness," Russian Math. Surveys 58 (2003), 211-250 | The endpoint criterion: $u \in L^\infty_t L^3_x$ implies regularity, proved via backward uniqueness for the heat operator and unique continuation. Closes the critical $q=3$ endpoint of Prodi-Serrin (criticality control); the deepest conditional result. |
| G. Seregin, "A certain necessary condition of potential blow up for Navier-Stokes equations," Comm. Math. Phys. 312 (2012), 833-845 | If $T$ is a singular time then $\|u(t)\|_{L^3}$ does not stay bounded as $t \to T$ (an $L^3$ blow-up of the critical norm). The bridge from ESS to the quantitative-regularity program (Architecture 2/4). |

## Critical spaces and scaling (Architecture 3)

| Source | Role |
|---|---|
| H. Fujita, T. Kato, "On the Navier-Stokes initial value problem. I," Arch. Rational Mech. Anal. 16 (1964), 269-315 | Small-data global existence and local well-posedness of mild solutions in the critical space $\dot H^{1/2}(\mathbb{R}^3)$. The origin of the critical-space program (Architecture 3). |
| T. Kato, "Strong $L^p$-solutions of the Navier-Stokes equation in $\mathbb{R}^m$, with applications to weak solutions," Math. Z. 187 (1984), 471-480 | Mild solutions in the critical Lebesgue space $L^3(\mathbb{R}^3)$ via the semigroup/fixed-point method; local well-posedness and small-data global existence. The $L^3$ critical-space pillar of Architecture 3. |
| M. Cannone, Y. Meyer, F. Planchon, "Solutions auto-similaires des equations de Navier-Stokes," Seminaire EDP, Ecole Polytechnique (1993-1994), Expose VIII | Forward self-similar and small-data global solutions in critical Besov spaces $\dot B^{-1+3/q}_{q,\infty}$, larger than $L^3$. Extends Architecture 3 to Besov-scale critical data; the bridge to forward self-similar solutions. |
| H. Koch, D. Tataru, "Well-posedness for the Navier-Stokes equations," Adv. Math. 157 (2001), 22-35 | Small-data global existence in $\mathrm{BMO}^{-1}$, the largest known critical space (it contains all the others). The upper boundary of the critical-space program; informs Architecture 3 and the boundary against ill-posedness. |
| J. Bourgain, N. Pavlovic, "Ill-posedness of the Navier-Stokes equations in a critical space in 3D," J. Funct. Anal. 255 (2008), 2233-2247 | Norm inflation: NS is ill-posed in $\dot B^{-1}_{\infty,\infty}$, the scaling-critical space just above $\mathrm{BMO}^{-1}$. Marks the outer edge of the critical-space program; a negative result that pins down how far Architecture 3 can reach (criticality control). |
| J. Bogdan, T. Tao (context: critical-space scaling) and the project note on supercriticality | See `docs/02_graduate/` and `experiments/scaling_criticality/`. The in-repo criticality bookkeeper that classifies any norm as sub/critical/super. The operational form of the criticality control. (verify: internal cross-reference, not an external paper) |

## Blow-up, self-similar solutions, and Euler (Architecture 4)

| Source | Role |
|---|---|
| J. Necas, M. Ruzicka, V. Sverak, "On Leray's self-similar solutions of the Navier-Stokes equations," Acta Math. 176 (1996), 283-294 | Leray's backward self-similar blow-up profiles are ruled out in $L^3(\mathbb{R}^3)$. Closes the classical self-similar route in the critical space; a foundational negative result for Architecture 4. |
| T.-P. Tsai, "On Leray's self-similar solutions of the Navier-Stokes equations satisfying local energy estimates," Arch. Rational Mech. Anal. 143 (1998), 29-51 | Extends Necas-Ruzicka-Sverak under local energy bounds, ruling out a wider class of self-similar blow-up. Strengthens the self-similar exclusion of Architecture 4. |
| H. Jia, V. Sverak, "Local-in-space estimates near initial time for weak solutions of the Navier-Stokes equations and forward self-similar solutions," Invent. Math. 196 (2014), 233-265 | Constructs global forward self-similar solutions from $(-1)$-homogeneous data via local-in-space regularity; the scenario underlying a proposed self-similar non-uniqueness mechanism. Reframes Architecture 4 around forward (not backward) self-similar profiles and links to non-uniqueness. |
| T. Tao, "Finite time blowup for an averaged three-dimensional Navier-Stokes equation," J. Amer. Math. Soc. 29 (2016), 601-674 | Finite-time blow-up for an averaged NS that retains the energy identity and the exact scaling. The barrier result: any regularity proof must use the precise nonlinearity, not energy-plus-scaling alone. The single most orienting negative result for Architecture 4 and the criticality control. |
| T. Tao, "Quantitative bounds for critically bounded solutions to the Navier-Stokes equations," in Nine Mathematical Challenges (Proc. Sympos. Pure Math. 104), AMS (2021), 149-193 (arXiv:1908.04958, 2019) | Quantitative ESS: a triple-exponential lower bound on $\|u\|_{L^3}$ growth approaching a putative singularity. Makes the $L^3$ criterion effective and seeds the quantitative-regularity program (Architectures 2/4). |
| S. Barker, C. Prange, "Quantitative regularity for the Navier-Stokes equations via spatial concentration," Comm. Math. Phys. 385 (2021), 717-792 | Quantitative regularity and forced concentration of the critical $L^3$ norm at scale $\sim \sqrt{T_* - t}$ near a putative Type I singularity. Refines Tao's quantitative bounds; central to the modern concentration/quantitative-regularity direction. |
| T. Buckmaster, C. Prange (eds.) survey context; D. Albritton, S. Barker, C. Prange, "Localized smoothing and concentration for the Navier-Stokes equations in the half space," arXiv:2112.10705 (2021) | Localized smoothing and critical-norm concentration in the half-space setting. Extends the concentration program to boundaries. (verify: final journal placement) |
| T. M. Elgindi, "Finite-time singularity formation for $C^{1,\alpha}$ solutions to the incompressible Euler equations on $\mathbb{R}^3$," Ann. of Math. (2) 194 (2021), 647-727 | Rigorous finite-time singularity for axisymmetric $C^{1,\alpha}$ Euler. The viscosity control made precise: inviscid 3D really does blow up, so viscosity is essential to any smoothness claim. |
| G. Luo, T. Y. Hou, "Potentially singular solutions of the 3D axisymmetric Euler equations," Proc. Natl. Acad. Sci. USA 111 (2014), 12968-12973 | High-resolution numerics showing potential boundary-driven axisymmetric Euler singularity (the Hou-Luo scenario). The numerical precursor to the Chen-Hou rigorous program; informs Architecture 4 and the viscosity control. |
| J. Chen, T. Y. Hou, "Stable nearly self-similar blowup of the 2D Boussinesq and 3D Euler equations with smooth data I: Analysis," arXiv:2210.07191 (2022); "... II: Rigorous Numerics," Multiscale Model. Simul. (SIAM) (2025), arXiv:2305.05660 | Computer-assisted proof of finite-time blow-up for 2D Boussinesq and 3D axisymmetric Euler with smooth data and boundary, via nonlinear stability of an approximate self-similar profile. The state of the art on rigorous Euler blow-up; sharpens the viscosity control. (verify: II journal volume/pages) |
| Y. Wang, C.-Y. Lai, J. Gomez-Serrano, T. Buckmaster, "Asymptotic self-similar blow-up profile for three-dimensional axisymmetric Euler equations using neural networks," Phys. Rev. Lett. 130 (2023), 244002 | Physics-informed neural networks discover smooth self-similar blow-up profiles for 2D Boussinesq and 3D Euler, including unstable ones. The ML-assisted route to candidate blow-up profiles; informs Architecture 4 and the research_atlas ML directions. |
| P. Constantin, "Geometric statistics in turbulence," SIAM Rev. 36 (1994), 73-98 | Surveys the geometric depletion of nonlinearity and vorticity-alignment structure relevant to whether 3D stretching can produce singularities. Context for the geometric/vorticity criteria and Architecture 4. |

## Non-uniqueness via convex integration (Architecture 5)

| Source | Role |
|---|---|
| P. Isett, "A proof of Onsager's conjecture," Ann. of Math. (2) 188 (2018), 871-963 | Constructs $C^{1/3 - \varepsilon}$ Euler flows dissipating energy, settling the flexible side of the Onsager conjecture. The Euler template for the convex-integration machinery used on NS (Architecture 5). |
| T. Buckmaster, C. De Lellis, L. Szekelyhidi Jr., V. Vicol, "Onsager's conjecture for admissible weak solutions," Comm. Pure Appl. Math. 72 (2019), 229-274 | Onsager-critical Euler solutions that are admissible (dissipate energy) below $C^{1/3}$. The refined Onsager construction; the methodological bridge from Euler to the NS non-uniqueness results. |
| T. Buckmaster, V. Vicol, "Nonuniqueness of weak solutions to the Navier-Stokes equations," Ann. of Math. (2) 189 (2019), 101-144 | Non-uniqueness of weak solutions of 3D NS with bounded kinetic energy, below the Leray-Hopf class, via intermittent convex integration. The headline Architecture 5 result; shows "weak solution" alone is too loose, sharpening why the Leray-Hopf energy class matters. |
| D. Albritton, E. Brue, M. Colombo, "Non-uniqueness of Leray solutions of the forced Navier-Stokes equations," Ann. of Math. (2) 196 (2022), 415-455 | Two distinct Leray-Hopf solutions for the same forced initial data, via an instability/self-similar mechanism (not convex integration). Pushes non-uniqueness into the Leray-Hopf class itself for forced NS; complements Architecture 5 and links to Jia-Sverak. |
| C. De Lellis, L. Szekelyhidi Jr., "The Euler equations as a differential inclusion," Ann. of Math. (2) 170 (2009), 1417-1436 | Originates the convex-integration / differential-inclusion method for incompressible Euler. The conceptual root of Architecture 5. |

## Geometric and vorticity-direction criteria

| Source | Role |
|---|---|
| P. Constantin, C. Fefferman, "Direction of vorticity and the problem of global regularity for the Navier-Stokes equations," Indiana Univ. Math. J. 42 (1993), 775-789 | If the vorticity direction is Lipschitz in regions of high vorticity, the solution stays smooth. The geometric regularity criterion: alignment, not just magnitude, controls blow-up. Engages 3D vortex stretching directly (passes the 2D control). |
| P. Constantin, C. Fefferman, A. J. Majda, "Geometric constraints on potentially singular solutions for the 3-D Euler equations," Comm. Partial Differential Equations 21 (1996), 559-571 | Geometric (vorticity-direction smoothness) constraints that obstruct Euler singularity formation. The Euler analog of Constantin-Fefferman 1993; informs the geometric direction and the viscosity control. |
| J. D. Gibbon, "The three-dimensional Euler equations: Where do we stand?," Phys. D 237 (2008), 1894-1904 | Surveys vorticity-stretching and geometric criteria for Euler and NS blow-up. A compact orientation to the geometric/vorticity literature. |
| L. C. Berselli, G. P. Galdi, "Regularity criteria involving the pressure for the weak solutions to the Navier-Stokes equations," Proc. Amer. Math. Soc. 130 (2002), 3585-3595 | Pressure-based conditional regularity criteria. A complementary family to the velocity and vorticity criteria of Architecture 2. (verify) |

## Textbooks and encyclopedic references

| Source | Role |
|---|---|
| P. Constantin, C. Foias, "Navier-Stokes Equations," Chicago Lectures in Mathematics, Univ. of Chicago Press (1988) | The standard graduate reference for the rigorous functional-analytic theory: weak solutions, regularity, dimension of attractors. Background for Architectures 1 and 2. |
| R. Temam, "Navier-Stokes Equations: Theory and Numerical Analysis," AMS Chelsea reprint (2001; orig. North-Holland 1977) | Functional-analytic framework, weak solutions, and numerical analysis. The canonical reference for the Galerkin/weak-solution machinery (Architecture 1). |
| C. R. Doering, J. D. Gibbon, "Applied Analysis of the Navier-Stokes Equations," Cambridge Texts in Applied Mathematics (1995) | Applied, energy-method-oriented introduction with explicit a priori estimates and the ladder of higher norms. Accessible entry to Architecture 1 and the energy bookkeeping behind the criticality control. |
| P.-L. Lions, "Mathematical Topics in Fluid Mechanics, Vol. 1: Incompressible Models," Oxford Lecture Series in Mathematics and its Applications 3 (1996) | Compactness methods and the incompressible weak-solution theory. Reference for Architecture 1 and the renormalized/weak-solution boundary. |
| A. J. Majda, A. L. Bertozzi, "Vorticity and Incompressible Flow," Cambridge Texts in Applied Mathematics 27 (2002) | The vorticity-formulation textbook: BKM, vortex stretching, energy methods, weak solutions, and 2D vs 3D. The single best reference tying the 2D control and 3D stretching together. |
| P. G. Lemarie-Rieusset, "The Navier-Stokes Problem in the 21st Century," CRC Press / Chapman and Hall (2016; 2nd ed. 2024) | The modern encyclopedic monograph: critical spaces, mild solutions, partial regularity, ESS, and the state of the conditional criteria. The most comprehensive single reference across Architectures 1 through 4. |
| H. Bahouri, J.-Y. Chemin, R. Danchin, "Fourier Analysis and Nonlinear Partial Differential Equations," Grundlehren der mathematischen Wissenschaften 343, Springer (2011) | Littlewood-Paley and Besov-space technology with NS well-posedness applications. The toolbox reference for the critical-space program (Architecture 3). |
| J. C. Robinson, J. L. Rodrigo, W. Sadowski, "The Three-Dimensional Navier-Stokes Equations: Classical Theory," Cambridge Studies in Advanced Mathematics 157 (2016) | A modern, self-contained graduate text: weak and strong solutions, local existence, partial regularity, and conditional criteria with full proofs. A clean entry point to Architectures 1 and 2. |
| C. Foias, O. Manley, R. Rosa, R. Temam, "Navier-Stokes Equations and Turbulence," Encyclopedia of Mathematics and its Applications 83, Cambridge (2001) | Connects the rigorous theory to turbulence (energy cascade, attractors, statistical solutions). Background for the energy-spectrum experiments and the supercriticality framing. |

## Surveys and lecture notes

| Source | Role |
|---|---|
| C. L. Fefferman, official problem description (see "The problem statement" above) | Also serves as the canonical short survey of what counts as a solution. |
| G. Seregin, "Lecture Notes on Regularity Theory for the Navier-Stokes Equations," World Scientific (2014) | A graduate-level, proof-complete treatment of suitable weak solutions, $\varepsilon$-regularity, ESS, and backward uniqueness. The best single source for the partial-regularity and $L^3$-endpoint machinery (Architectures 1, 2). |
| T. Tao, "Lecture notes / blog posts on the Navier-Stokes regularity problem" (terrytao.wordpress.com; e.g. "Why global regularity for Navier-Stokes is hard," 2007) | The clearest informal exposition of supercriticality, the energy gap, and why energy methods cannot close regularity. The expository source for the criticality control's logic. |
| C. Prange, "From concentration to quantitative regularity: a short survey of recent developments for the Navier-Stokes equations," Vietnam J. Math. (2023), arXiv:2211.16215 | Surveys the Tao / Barker-Prange quantitative-regularity and concentration program. The orientation reference for the modern Architecture 2/4 thread. |
| V. Sverak, "PDE lecture notes (Navier-Stokes)," Univ. of Minnesota | Lecture notes covering mild solutions, critical spaces, self-similar solutions, and the ESS circle of ideas. Freely available course-level companion to Architectures 2-4. (verify: exact title/year) |
| T. Buckmaster, V. Vicol, "Convex integration and phenomenologies in turbulence," EMS Surv. Math. Sci. 6 (2019), 173-263 | A survey of the convex-integration method and its turbulence interpretation (Onsager, Nash). The orientation reference for Architecture 5. |
| L. Szekelyhidi Jr., "From isometric embeddings to turbulence," in HCDTE Lecture Notes (2012) | Traces convex integration from the Nash-Kuiper embedding theorem to fluid non-uniqueness. Conceptual background for Architecture 5. |

## Recent developments (2018-2025)

| Source | Role |
|---|---|
| P. Isett, "A proof of Onsager's conjecture," Ann. of Math. (2) 188 (2018) (also in Architecture 5) | The flexible side of Onsager settled; the Euler template that convex integration then carried to NS. |
| T. Buckmaster, V. Vicol, "Nonuniqueness of weak solutions to the Navier-Stokes equations," Ann. of Math. (2) 189 (2019) (also in Architecture 5) | The first NS non-uniqueness via convex integration; the defining recent result on the boundary of "solution." |
| T. Tao, "Quantitative bounds for critically bounded solutions ...," (2019/2021) (also in Architecture 4) | Effective ESS; launched the quantitative-regularity program. |
| S. Barker, C. Prange, "Quantitative regularity ... via spatial concentration," Comm. Math. Phys. 385 (2021) (also in Architecture 4) | Critical-norm concentration near singularities; the current frontier of conditional/quantitative regularity. |
| D. Albritton, E. Brue, M. Colombo, "Non-uniqueness of Leray solutions of the forced Navier-Stokes equations," Ann. of Math. (2) 196 (2022) (also in Architecture 5) | Non-uniqueness inside the Leray-Hopf class for forced NS; a qualitatively new instability mechanism. |
| J. Chen, T. Y. Hou, "Stable nearly self-similar blowup ... I, II," (2022; 2023/2025) (also in Architecture 4) | Computer-assisted Euler/Boussinesq blow-up with smooth data; the state of the art on rigorous inviscid singularity (viscosity control). |
| Y. Wang, C.-Y. Lai, J. Gomez-Serrano, T. Buckmaster, "Asymptotic self-similar blow-up profile ... using neural networks," Phys. Rev. Lett. 130 (2023) (also in Architecture 4) | ML-discovered self-similar profiles; the neural-network route to candidate blow-up data. |
| H. Kwon, "The role of the pressure in the regularity theory of the Navier-Stokes equations," and related 2020s quantitative-regularity papers | Representative of the active pressure/critical-norm thread feeding Architecture 2. (verify: exact citation) |

## Conventions

- PDFs go in this folder and are gitignored (`*.pdf`). Only this index and the reading notes are tracked.
- When adding a source, record it here with its full citation and a one-to-two sentence role, and link a reading note in `docs/03_research/reading_notes/` if it is load-bearing.
- Group a new source under the architecture it most informs; cross-list it in "Recent developments" if it is from 2018 or later and frontier-relevant.
- Mark any citation detail not yet checked against the published version with "(verify)".
