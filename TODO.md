# TODO: Navier-Stokes Existence and Smoothness Study Repo

## Done

### Repo and docs

- [x] Set up repo structure
- [x] Write README.md
- [x] **CLAUDE.md** project context for AI assistants
- [x] **OPERATIONS.md** how to operate the research-program substrate
- [x] **STATE_OF_THE_PROGRAM.md** one-page strategic snapshot
- [x] **PHASE_STATE.md** current operational state
- [x] **docs/researcher_mindset.md** operating philosophy
- [x] **docs/solutions/** known approaches and obstructions per architecture
- [x] **docs/research_atlas/** master research map, all approaches and obstructions
- [x] **docs/00_intuitive/** intuitive-level explanation
- [x] **docs/01_undergraduate/** undergraduate-level explanation
- [x] **docs/02_graduate/** scaling, supercriticality, the regularity criteria
- [x] **docs/03_research/** research overview + five research directions + reading notes
- [x] **docs/implications/** why the problem matters

### Experimental thread (see `experiments/PLAN.md`)

- [x] Phase 0: shared infrastructure (Flow3D solver interface, criticality bookkeeper CONTROL, 2D control, smoke test)
- [x] Scaling/criticality classifier: classify energy L^2, H^1, L^3, BMO^{-1}, H^{1/2}, vorticity-L^infinity-in-time as sub/critical/super under NS scaling (runs)
- [x] Burgers shock: inviscid Burgers forms a shock (gradient blow-up) in finite time, viscous Burgers stays smooth (runs)
- [x] Taylor-Green DNS: pseudo-spectral 32^3, low Reynolds, track energy/enstrophy/max vorticity + BKM integral, observe BKM integral stays finite (runs)
- [x] Energy spectrum: from a TG-style field, plot E(k) and the dissipation rate, show the cascade and where resolution bites (runs)

### Lean 4 / Mathlib skeleton

- [x] lakefile.lean + lean-toolchain (matched to the companion repo: Lean 4.13.0 + Mathlib v4.13.0)
- [x] NavierStokes.lean main module
- [x] DivergenceFree.lean (divergence-free vector fields)
- [x] LerayProjector.lean (the Leray projection onto divergence-free fields)
- [x] EnergyInequality.lean (the energy inequality statement)
- [x] BealeKatoMajda.lean (the BKM criterion statement)
- [x] Scaling.lean (the scaling symmetry and criticality)
- [x] GlobalRegularity.lean (the global-regularity goal statement)

### Agents and references

- [x] Six agent role specs in .claude/agents/ (surveyor/builder/verifier/adversary/synthesizer/orchestrator)
- [x] references/README.md (key reference library index)
- [x] sources/README.md
- [x] visualizations/README.md + one manim scene
- [x] memory/MEMORY.md

## Open: experimental

- [ ] Resolution study: run the Taylor-Green DNS at 48^3, 64^3 and increasing Reynolds; track whether the BKM integral shows any sign of divergence (with the explicit caveat that numerics cannot prove blow-up)
- [ ] Add 2/3-rule dealiasing to the Taylor-Green solver and confirm energy/enstrophy diagnostics are stable under it
- [ ] Set up the Hou-Luo axisymmetric near-singular scenario at coarse resolution (the most-studied candidate near-blow-up flow)
- [ ] Quantitative criticality dossier: classify the one-component, vorticity-direction (Constantin-Fefferman), and anisotropic criteria onto the sub/critical/super coordinate (Constantin-Fefferman done in docs/03_research/reading_notes/constantin_fefferman_1993.md and the criticality-placement table; one-component and anisotropic criteria remain)
- [ ] Energy spectrum from an actual Taylor-Green run rather than the synthetic fallback; compare the -5/3 inertial range expectation at higher Reynolds
- [ ] 2D control experiment: run a 2D Navier-Stokes DNS showing enstrophy non-increasing and no stretching, side by side with the 3D run, to make the must-stay-smooth control concrete in code

## Open: analytic (the open problem)

- [ ] Survey: map every known regularity criterion onto the sub/critical/super coordinate and identify which are genuinely scale-invariant geometric conditions (landmark criteria mapped in docs/03_research/reading_notes/README.md criticality-placement table; remaining: one-component, anisotropic, and Ladyzhenskaya-Prodi-Serrin variants)
- [x] Survey: the convex-integration non-uniqueness literature (Buckmaster-Vicol and after) and exactly what it does and does not say about the smooth flow (dossiers: buckmaster_vicol_2019, isett_2018, albritton_brue_colombo_2022, plus the spine narrative in reading_notes/README.md)
- [x] Survey: the Tao averaged-NS barrier and what structural feature any regularity proof must use to exclude the averaged caricature (dossier: docs/03_research/reading_notes/tao_2016_averaged.md)
- [ ] Identify the smallest open conditional improvement worth targeting (e.g., a logarithmic improvement of a Prodi-Serrin endpoint, or a vorticity-direction condition weakened toward criticality)

## Open: Lean / formalization

- [ ] State the energy inequality in a Mathlib-faithful way; identify the exact gap (vector-valued Sobolev spaces, the Leray projector)
- [ ] State the scaling identity and prove it preserves the NS equations (algebraic, may be reachable)
- [ ] State the BKM criterion and the global-regularity goal; keep as documented `sorry` until the analytic infrastructure exists
- [ ] Track which Mathlib analysis pieces (Bochner integral, Sobolev spaces, Helmholtz/Leray decomposition) would need to land upstream

## Open: docs and visualizations

- [ ] Convert any source PDFs to Markdown (text conversions in sources/)
- [ ] manim scene: TaylorGreenVortex (the canonical visualization of the test flow)
- [ ] manim scene: VortexStretching (the 3D-vs-2D structural difference)
- [ ] manim scene: ScalingZoom (how the scaling symmetry rescales space and time, and why energy is supercritical)
- [ ] manim scene: BurgersShock (gradient steepening into a shock; viscosity regularizing)
- [ ] manim scene: SingularSetCKN (the CKN partial-regularity picture)
- [ ] Add a glossary of terms (mild solution, suitable weak solution, criticality, enstrophy)

## ML / data backlog

- [ ] Set up a DNS data pipeline (the Johns Hopkins Turbulence Database is a candidate source)
- [ ] ML experiment framework for detecting near-singular structures in DNS fields
- [ ] Learned closure / Lyapunov-functional search (a candidate critical quantity discovered numerically, then checked analytically)
- [ ] Link visualizations to corresponding doc sections
- [ ] Add Jupyter notebooks for interactive exploration
