# Reading guide: books and resources for Navier-Stokes existence and smoothness

A curated, annotated path through the literature for someone seriously studying the
Navier-Stokes existence-and-smoothness problem. This is the "what to read, and in what
order" companion to the bibliography in [`README.md`](README.md). It is organized so a
newcomer can start from a freely available statement of the problem and walk all the way
to the research frontier, with every item tagged by what it is best for.

Style note: this guide uses the project's coordinate system throughout. Every result is
placed on the sub/critical/super criticality scale and checked against the three
controls (2D stays smooth; energy is supercritical; viscosity and the exact 3D structure
matter). See [`../CLAUDE.md`](../CLAUDE.md) for those conventions and
[`../docs/research_atlas/README.md`](../docs/research_atlas/README.md) for the master
obstruction map.

A surveyor's honesty caveat: the freely available URLs below were checked at the time of
writing. Links marked "(verify)" were not directly confirmed live and should be
re-checked. Some reading-note dossiers linked in Section 4 are seeded and some are
forthcoming; the index in [`../docs/03_research/reading_notes/README.md`](../docs/03_research/reading_notes/README.md)
records which is which.

---

## 1. Orientation

The 3D incompressible Navier-Stokes equations on $\mathbb{R}^3$ or $\mathbb{T}^3$,

$$\partial_t u + (u\cdot\nabla)u = -\nabla p + \nu\,\Delta u, \qquad \nabla\cdot u = 0, \qquad u(\cdot,0)=u_0,$$

describe a viscous incompressible fluid. The Millennium Problem asks: given smooth,
divergence-free, suitably decaying initial data $u_0$ with finite energy, does a smooth
solution exist for all time, or can it break down in finite time? Global weak solutions
exist (Leray 1934, Hopf 1951) and short-time smooth solutions exist, but whether the
smooth solution persists globally in three dimensions is open.

The single most important structural fact, and the spine of this whole project: the
energy inequality

$$\tfrac12\,\|u(t)\|_{L^2}^2 + \nu\int_0^t \|\nabla u\|_{L^2}^2\,ds \le \tfrac12\,\|u_0\|_{L^2}^2$$

is the only coercive globally-in-time a priori bound we have, and it is **supercritical**
with respect to the natural scaling $u_\lambda(x,t) = \lambda\,u(\lambda x, \lambda^2 t)$.
Under that scaling the energy goes to zero at small scales, so an energy bound is
compatible with worlds where the solution concentrates and blows up. The critical
quantities (those scale-invariant, like $\|u\|_{L^3}$, $\|u\|_{\dot H^{1/2}}$,
$\|u\|_{\mathrm{BMO}^{-1}}$) sit exactly at the threshold the energy cannot reach. The
proof, if it exists, must add genuinely critical control that engages the exact 3D
vortex-stretching nonlinearity, because any purely energy-level argument would equally
"apply" to 2D, where solutions are known to stay smooth forever.

---

## 2. Start here: freely available primary sources

Read these first. They are free, authoritative, and they install the coordinate system.

- **The official problem statement (Fefferman, Clay 2000).** The contract: what
  "solution" means, the finite-energy class, and the four acceptable answers (A/B
  regularity on $\mathbb{R}^3$/$\mathbb{T}^3$, C/D breakdown). The canonical target is
  global existence-and-smoothness with no forcing. Free PDF:
  https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf
  Problem page: https://www.claymath.org/millennium/navier-stokes-equation/
  Dossier: [`../docs/03_research/reading_notes/fefferman_problem_statement.md`](../docs/03_research/reading_notes/fefferman_problem_statement.md)

- **Tao, "Why global regularity for Navier-Stokes is hard" (blog, 2007).** The single
  best plain-language explanation of the supercriticality barrier: why weakening the
  nonlinearity, strengthening dissipation, or discretizing all give global solutions to
  an approximate equation, and why none of that reaches the true equation. This is the
  prose form of the project's central thesis.
  https://terrytao.wordpress.com/2007/03/18/why-global-regularity-for-navier-stokes-is-hard/

- **Tao, Navier-Stokes tag on "What's New" (blog index).** The running collection of
  Tao's NS posts, including the logarithmically supercritical hyperdissipation result
  (how far you can push a critical argument into the supercritical regime) and the
  averaged-equation blow-up program.
  https://terrytao.wordpress.com/tag/navier-stokes-equations/

- **Constantin, "Some open problems and research directions in the mathematical study of
  fluid dynamics" (in Mathematics Unlimited: 2001 and Beyond, Springer).** A short
  survey that frames existence, uniqueness, regularity, and the statistical/turbulence
  questions together. The author's preprint copy is reachable from his Princeton papers
  page: https://web.math.princeton.edu/~const/papers.html (verify the specific entry).

- **Sverak, lecture notes on fluid mechanics / PDE (University of Minnesota).** Graduate
  course notes that build the Navier-Stokes theory carefully from the function-space
  setup through regularity; in the St. Petersburg style, very readable.
  https://www-users.cse.umn.edu/~sverak/course-notes2011.pdf
  (Older mirror sometimes cited as math.umn.edu/~sverak/course-notes2011.pdf (verify).)

- **Seregin, Lecture Notes on Regularity Theory for the Navier-Stokes Equations.** Based
  on Oxford TCC courses; the cleanest self-contained route to the
  Caffarelli-Kohn-Nirenberg partial-regularity machinery and the $\varepsilon$-regularity
  method. The published book is not free, but the lecture-note versions circulate; see
  the publisher page https://www.worldscientific.com/worldscibooks/10.1142/9314 and check
  the author's Oxford page for a preprint (verify).

- **Kukavica, lecture notes / survey on regularity of Navier-Stokes.** Kukavica has
  several expository surveys on partial regularity and conditional regularity criteria
  that are widely circulated as PDFs; search his USC faculty page for the current copy
  (verify). Good complement to Seregin on the partial-regularity side.

---

## 3. Textbooks, with "best for" and a suggested order

Work down this list. The first four form a spine; the rest are targeted references you
pull from when a specific technique or domain comes up.

1. **Robinson, Rodrigo, Sadowski, The Three-Dimensional Navier-Stokes Equations:
   Classical Theory (Cambridge, 2016).** Best for: the cleanest modern presentation of
   the classical theory (weak and strong solutions, local existence, the regularity
   criteria, partial regularity) with full proofs and no prerequisites beyond a solid
   PDE course. Start here.

2. **Lemarie-Rieusset, The Navier-Stokes Problem in the 21st Century (CRC, 2nd ed.
   2018).** Best for: the encyclopedic reference on critical spaces, mild solutions, and
   the harmonic-analysis machinery (including Koch-Tataru $\mathrm{BMO}^{-1}$). This is
   where the criticality story lives in book form. Dense; use it as a reference, not a
   first read.

3. **Majda, Bertozzi, Vorticity and Incompressible Flow (Cambridge, 2002).** Best for:
   the vorticity formulation, vortex stretching, and the Euler equations, including the
   Beale-Kato-Majda criterion in its native setting. Read this to understand the exact
   3D structure (the $\omega\cdot\nabla u$ term) that any regularity proof must engage.

4. **Bahouri, Chemin, Danchin, Fourier Analysis and Nonlinear Partial Differential
   Equations (Springer, 2011).** Best for: the Littlewood-Paley and paradifferential
   technique used in modern critical-space well-posedness. Read it when the harmonic
   analysis in Lemarie-Rieusset starts to feel like a black box.

Targeted references (pull as needed):

- **Constantin, Foias, Navier-Stokes Equations (Chicago, 1988).** Best for: the compact
  classic graduate treatment of the functional-analytic framework and the
  Galerkin/energy approach; concise and authoritative.
- **Temam, Navier-Stokes Equations: Theory and Numerical Analysis.** Best for: the
  rigorous weak-solution functional setting and the bridge to numerical analysis.
- **Doering, Gibbon, Applied Analysis of the Navier-Stokes Equations (Cambridge, 1995).**
  Best for: a short, physically motivated energy-method introduction; good for the
  turbulence and dissipation intuition.
- **Galdi, An Introduction to the Mathematical Theory of the Navier-Stokes Equations
  (Springer, 2nd ed. 2011).** Best for: the steady-state theory and the deep
  function-space (and pressure) analysis; the definitive reference on those.
- **Sohr, The Navier-Stokes Equations: An Elementary Functional Analytic Approach
  (Birkhauser, 2001).** Best for: a careful, self-contained functional-analytic
  development of weak and strong solution theory.

---

## 4. Landmark papers by architecture

Each item points to its dossier in the project's reading notes (relative links below).
The dossiers carry the structural read: what is actually proved at the lemma level, and
where it sits on the criticality scale. A few dossiers are seeded now; the rest are
forthcoming as the surveyor program works through the corpus (see the
[reading-notes index](../docs/03_research/reading_notes/README.md)).

### The problem

- Fefferman, official statement (Clay 2000): [`../docs/03_research/reading_notes/fefferman_problem_statement.md`](../docs/03_research/reading_notes/fefferman_problem_statement.md)

### Architecture 1: energy methods, weak solutions, partial regularity

These are unconditional, and each stops exactly where supercriticality stops it
(existence but not regularity; small singular set but not empty).

- Leray 1934, global weak solutions and the energy inequality: [`../docs/03_research/reading_notes/leray_1934.md`](../docs/03_research/reading_notes/leray_1934.md)
- Hopf 1951, Leray-Hopf weak solutions on domains: [`../docs/03_research/reading_notes/hopf_1951.md`](../docs/03_research/reading_notes/hopf_1951.md)
- Caffarelli-Kohn-Nirenberg 1982, $\mathcal{P}^1 = 0$ singular set, $\varepsilon$-regularity: [`../docs/03_research/reading_notes/caffarelli_kohn_nirenberg_1982.md`](../docs/03_research/reading_notes/caffarelli_kohn_nirenberg_1982.md)
- Lin (1998) / Vasseur, streamlined partial-regularity proofs: [`../docs/03_research/reading_notes/lin_vasseur_partial_regularity.md`](../docs/03_research/reading_notes/lin_vasseur_partial_regularity.md)

### Architecture 2: conditional regularity criteria

Sharp and critical, but unreachable from the supercritical energy alone. These tell you
what control would suffice; the program's job is to find where that control comes from.

- Prodi-Serrin-Ladyzhenskaya, $L^p_t L^q_x$ with $2/p + 3/q \le 1$: [`../docs/03_research/reading_notes/prodi_serrin_ladyzhenskaya.md`](../docs/03_research/reading_notes/prodi_serrin_ladyzhenskaya.md)
- Beale-Kato-Majda 1984, $\int_0^T \|\omega\|_{L^\infty}\,dt$ blow-up criterion: [`../docs/03_research/reading_notes/beale_kato_majda_1984.md`](../docs/03_research/reading_notes/beale_kato_majda_1984.md)
- Constantin-Fefferman 1993, the geometric (vorticity-direction) criterion: [`../docs/03_research/reading_notes/constantin_fefferman_1993.md`](../docs/03_research/reading_notes/constantin_fefferman_1993.md)
- Escauriaza-Seregin-Sverak 2003, the endpoint $L^\infty_t L^3_x$, backward uniqueness: [`../docs/03_research/reading_notes/escauriaza_seregin_sverak_2003.md`](../docs/03_research/reading_notes/escauriaza_seregin_sverak_2003.md)
- Tao 2019, quantitative ESS, triple-log lower bound on $\|u\|_{L^3}$: [`../docs/03_research/reading_notes/tao_2019_quantitative.md`](../docs/03_research/reading_notes/tao_2019_quantitative.md)

### Architecture 3: critical spaces and scaling

Small-data global existence at the scaling threshold; the boundary of what is known.

- Fujita-Kato 1964, small data in $\dot H^{1/2}$: [`../docs/03_research/reading_notes/fujita_kato_1964.md`](../docs/03_research/reading_notes/fujita_kato_1964.md)
- Koch-Tataru 2001, small data in $\mathrm{BMO}^{-1}$ (largest known critical space): [`../docs/03_research/reading_notes/koch_tataru_2001.md`](../docs/03_research/reading_notes/koch_tataru_2001.md)
- Bourgain-Pavlovic 2008, norm inflation / ill-posedness in $\dot B^{-1}_{\infty,\infty}$ (the boundary): [`../docs/03_research/reading_notes/bourgain_pavlovic_2008.md`](../docs/03_research/reading_notes/bourgain_pavlovic_2008.md)

### Architecture 4: blow-up, self-similarity, and the Euler companion

The barriers and the singularity evidence. These enforce the viscosity control and the
"engage the exact nonlinearity" discipline.

- Necas-Ruzicka-Sverak 1996, Leray self-similar blow-up ruled out in $L^3$: [`../docs/03_research/reading_notes/necas_ruzicka_sverak_1996.md`](../docs/03_research/reading_notes/necas_ruzicka_sverak_1996.md)
- Tao 2016, finite-time blow-up for an averaged Navier-Stokes (the barrier result): [`../docs/03_research/reading_notes/tao_2016_averaged.md`](../docs/03_research/reading_notes/tao_2016_averaged.md)
- Luo-Hou 2014, numerically-supported axisymmetric Euler near-singularity at a boundary: [`../docs/03_research/reading_notes/luo_hou_2014.md`](../docs/03_research/reading_notes/luo_hou_2014.md)
- Elgindi 2021, finite-time singularity for $C^{1,\alpha}$ axisymmetric Euler: [`../docs/03_research/reading_notes/elgindi_2021.md`](../docs/03_research/reading_notes/elgindi_2021.md)

### Architecture 5: non-uniqueness via convex integration

About the boundary of what "solution" means below the energy class, more than about
smooth-flow regularity. Read these to understand why the smooth/weak distinction is sharp.

- Isett 2018, the Onsager conjecture for Euler ($C^{1/3}$ threshold): [`../docs/03_research/reading_notes/isett_2018.md`](../docs/03_research/reading_notes/isett_2018.md)
- Buckmaster-Vicol 2019, non-uniqueness of weak NS below Leray-Hopf: [`../docs/03_research/reading_notes/buckmaster_vicol_2019.md`](../docs/03_research/reading_notes/buckmaster_vicol_2019.md)
- Albritton-Brue-Colombo 2022, non-uniqueness of Leray-Hopf solutions for forced NS: [`../docs/03_research/reading_notes/albritton_brue_colombo_2022.md`](../docs/03_research/reading_notes/albritton_brue_colombo_2022.md)

---

## 5. Online resources

- **Clay problem page.** Statement, official PDF, and pointers:
  https://www.claymath.org/millennium/navier-stokes-equation/

- **Tao, "What's New" Navier-Stokes tag.** Expository posts on the supercriticality
  barrier, hyperdissipation, and the averaged-equation blow-up program:
  https://terrytao.wordpress.com/tag/navier-stokes-equations/

- **Tao 2016 averaged-NS paper (open AMS PDF).** The finite-time blow-up barrier result
  in full: https://www.ams.org/jams/2016-29-03/S0894-0347-2015-00838-4/S0894-0347-2015-00838-4.pdf

- **Sverak course notes (UMN).** Graduate fluid-mechanics lecture notes:
  https://www-users.cse.umn.edu/~sverak/course-notes2011.pdf

- **Constantin papers page (Princeton).** Preprints of his surveys and research papers:
  https://web.math.princeton.edu/~const/papers.html

- **arXiv math.AP feed.** The live frontier; the convex-integration and Euler-blow-up
  threads move fast here. Search the recent listings under math.AP (verify current URL).

- **Rigorous numerics for the Euler blow-up thread.** The Chen-Hou program on
  computer-assisted proofs of self-similar Euler/Boussinesq blow-up is the place to
  watch on the singularity side; track the authors' arXiv preprints (Chen and Hou,
  2022 onward) and the surrounding rigorous-numerics literature (interval arithmetic,
  computer-assisted fixed-point proofs). See the atlas Architecture 4 section in
  [`../docs/research_atlas/README.md`](../docs/research_atlas/README.md) (verify the
  specific preprint URLs as they are revised).

---

## 6. A suggested four-stage learning path

Each stage lists concrete items from above. Do not skip Stage 1 even if you have a PDE
background; it sets the coordinate system that the rest of the program runs on.

### Stage 1: intuitive (what the problem is and why it is hard)

- Fefferman official statement PDF (Section 2): read the four statements and the
  finite-energy class.
- Tao, "Why global regularity is hard" blog post (Section 2): the supercriticality
  barrier in prose.
- The project's own intuitive layer: [`../docs/00_intuitive/`](../docs/00_intuitive/)
  and the graduate scaling note [`../docs/02_graduate/scaling_and_supercriticality.md`](../docs/02_graduate/scaling_and_supercriticality.md).

### Stage 2: undergraduate weak-solution theory

- Robinson-Rodrigo-Sadowski, Classical Theory (Section 3): local existence, weak and
  strong solutions, the energy inequality.
- Doering-Gibbon, Applied Analysis (Section 3): energy methods and dissipation intuition.
- Leray 1934 dossier (Section 4): global weak existence, where the energy bound stops.
- Hopf 1951 dossier (Section 4): the Leray-Hopf class.

### Stage 3: graduate criticality and regularity criteria

- Lemarie-Rieusset, 21st Century (Section 3): critical spaces and mild solutions.
- Majda-Bertozzi, Vorticity (Section 3): vortex stretching and the 3D structure.
- Prodi-Serrin-Ladyzhenskaya and Beale-Kato-Majda dossiers (Section 4): the conditional
  criteria.
- Escauriaza-Seregin-Sverak dossier (Section 4): the critical $L^3$ endpoint.
- Fujita-Kato and Koch-Tataru dossiers (Section 4): small-data critical well-posedness.

### Stage 4: research frontier

- Caffarelli-Kohn-Nirenberg and Lin/Vasseur dossiers (Section 4): partial regularity,
  $\varepsilon$-regularity, the singular set.
- Tao 2019 quantitative ESS dossier (Section 4): the best current lower bound on
  singularity formation.
- Tao 2016 averaged-NS dossier and paper (Sections 4 and 5): the barrier that says the
  missing control must use the exact nonlinearity.
- Elgindi 2021 and Luo-Hou / Chen-Hou (Sections 4 and 5): the Euler singularity evidence
  and rigorous-numerics frontier.
- Buckmaster-Vicol 2019 and Albritton-Brue-Colombo 2022 dossiers (Section 4):
  non-uniqueness and the boundary of the solution concept.

---

## What this enables / what remains open

What this enables: a reader can move from the Clay statement to the research frontier
along a path where every stop is placed on the criticality scale and checked against the
three controls. The textbooks give the technique; the dossiers in Section 4 give the
structural read of each landmark; Sections 2 and 5 give the freely available entry
points and the live frontier feeds. For BUILDER, this map says where the critical control
would have to come from (Architectures 2 and 3) and which barriers any candidate must
clear (Architecture 4, especially Tao 2016). For ADVERSARY, it locates the controls
(2D smoothness, the supercritical energy, the viscosity/Euler boundary) against which to
test proposals.

What remains open:

- **Dossier coverage.** Several Section 4 dossiers are forthcoming, not yet written
  (Hopf, Lin-Vasseur, Prodi-Serrin-Ladyzhenskaya, Constantin-Fefferman, Tao 2019,
  Fujita-Kato, Koch-Tataru, Bourgain-Pavlovic, Necas-Ruzicka-Sverak, Elgindi, Luo-Hou,
  Isett, Buckmaster-Vicol, Albritton-Brue-Colombo). The reading-notes index marks which
  exist. Filling these is the surveyor program's standing backlog.
- **Link verification.** Items marked "(verify)" (the Constantin survey preprint, the
  Sverak math.umn.edu mirror, Seregin and Kukavica preprint copies, the Chen-Hou
  rigorous-numerics preprints, the arXiv math.AP feed URL) were not confirmed live and
  should be re-checked before they are relied on.
- **The rigorous-numerics thread.** The Chen-Hou computer-assisted Euler/Boussinesq
  blow-up work deserves its own dossier with the criticality and viscosity controls
  applied explicitly; it is currently only pointed to, not surveyed.
- **No discrepancy with the project's existing analyses was found** in assembling this
  guide. It is a pure aggregation of sources onto the existing coordinate system; it
  introduces no new claims to reconcile.
