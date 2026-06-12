# Experimental plan: proof architectures and controls

The computational thread. It is organized around the five candidate proof architectures for the Navier-Stokes existence and smoothness problem, with three structural wrong-approach detectors applied throughout.

## Methodology

Each experiment is a runnable Python module under `experiments/<topic>/`, with a short `.md` writeup. Shared infrastructure lives in `experiments/_shared/`:

- The **criticality bookkeeper** (`criticality.py`): the CONTROL that classifies any norm sub/critical/super under the NS scaling and audits proposed estimates.
- The **pseudo-spectral solvers** (`flow.py`): `Flow3D` (Navier-Stokes on $\mathbb{T}^3$) and `Flow2D` (the 2D control).

The AI-centric methodology: a BUILDER proposes a candidate estimate or mechanism; an ADVERSARY runs it against the three controls; a VERIFIER attempts a Lean statement; a SYNTHESIZER records the finding in [`LEARNINGS.md`](LEARNINGS.md). See [`../OPERATIONS.md`](../OPERATIONS.md).

## The three wrong-approach detectors

1. **2D control**: 2D Navier-Stokes is globally smooth (no vortex stretching, enstrophy non-increasing). A candidate that applies verbatim in 2D and would predict 2D blow-up is wrong. Implemented as `Flow2D` in `_shared/flow.py`.
2. **Criticality control**: the energy is supercritical; any energy-controlled estimate is INSUFFICIENT_BY_ITSELF. Implemented as `criticality.py`.
3. **Viscosity control**: inviscid Burgers shocks, 3D Euler blows up; a method blind to $\nu \Delta u$ is suspect. Implemented as `burgers_shock/`.

## The five architectures and their experiments

### Architecture 1: energy methods and weak solutions

Leray-Hopf weak solutions exist globally (Leray 1934, Hopf 1951); uniqueness/regularity in 3D is open. Partial regularity: Caffarelli-Kohn-Nirenberg (1982), $\mathcal{P}^1(\text{singular set}) = 0$.

- **Taylor-Green DNS** (`taylor_green/`): RUNS. Confirms energy dissipation (energy inequality, numerically), finite BKM integral at low Reynolds, incompressibility at machine precision. The non-singular baseline.

### Architecture 2: conditional regularity criteria

Beale-Kato-Majda ($\int_0^T\|\omega\|_\infty\,dt < \infty$), Prodi-Serrin-Ladyzhenskaya ($2/p+3/q\le1$), Escauriaza-Seregin-Sverak ($L^\infty_t L^3_x$ endpoint).

- The BKM integral is tracked in the Taylor-Green DNS.
- **Vortex stretching anatomy** (`vortex_stretching/`): RUNS. Measures the enstrophy budget $dZ/dt = P - D$ (verified to $<1\%$ in the resolved window), strain-eigenvector alignment, the stretching depletion factor ($\approx 0.53$ of pointwise-maximal), and the Constantin-Fefferman direction coherence $|\nabla\xi|$ in the intense region. The 2D control runs alongside ($P$ structurally zero, enstrophy non-increasing). This is the experimental face of the CF lead.
- Mapping every criterion onto the criticality coordinate is done: see the [conditional-criteria criticality dossier](../docs/research_atlas/conditional_criteria_dossier.md). The vorticity-direction (Constantin-Fefferman) geometric criterion is the lead; the dossier sharpens this to the open $\beta = 0$ endpoint of the coherence ladder.
- **The $\beta$-dial and sparseness probe** (`vortex_stretching/beta_dial.py`): RUNS. Dossier handoffs 11.3.1-2. Holder-$\beta$ seminorms of $\xi$ on the intense set at $\beta \in \{1, 1/2, 1/4\}$: bounded at every rung, local exponent $\alpha \approx 1.2$ to $1.4$ at peak resolved production (the CF Lipschitz rung is sustained; the staircase has not begun to descend in laminar flow). 2D control: every seminorm exactly zero through the same code path. Sparseness: clean negative (TG is not filamentary; depletion $\approx 0.55$ flat across thresholds), so depletion is not sparseness-driven here. LEARNINGS #14.

### Architecture 3: critical spaces and scaling

The scaling symmetry; small-data global existence in $\dot H^{1/2}$ (Fujita-Kato), $L^3$, $\mathrm{BMO}^{-1}$ (Koch-Tataru). The supercriticality gap.

- **Criticality table** (`scaling_criticality/`): RUNS. Classifies the standard norms; energy supercritical, the regularity criteria critical. The headline control.
- **Energy spectrum** (`energy_spectrum/`): RUNS. The spectral picture of where energy lives (large scales) vs where a singularity would form (small scales).

### Architecture 4: blow-up and self-similar solutions

Leray's self-similar ansatz, ruled out in $L^3$ (Necas-Ruzicka-Sverak 1996; Tsai 1998). Tao (2016): finite-time blow-up for an averaged Navier-Stokes (a barrier). Euler blow-up: Elgindi (2021); Hou-Luo and Chen-Hou numerics.

- **Burgers shock** (`burgers_shock/`): RUNS. The viscosity control: inviscid gradient blow-up vs viscous smoothness.
- **Resolution study** (`resolution_study/`): RUNS. The BKM integral under grid refinement ($16^3 \to 24^3 \to 32^3$, two viscosities), plus the critical norms $\|u\|_{L^3}$, $\|u\|_{\dot H^{1/2}}$ along each run. Verdict at laptop parameters: CONVERGED (the smooth-regime calibration). The instrument for any future near-singular scenario: a candidate must show BKM growth that survives refinement.
- **Dyadic shell criticality scan** (`dyadic_shell/`): RUNS. The Katz-Pavlovic-type cascade with dissipation exponent $\alpha$ as an explicit criticality dial. Inviscid: finite-time blow-up (arrival ratio $0.638$ vs predicted $\lambda^{-2/3} = 0.630$). Viscous: the verdict flips from BLOWS UP to REGULAR across the flux-balance line $\alpha_c = 1/3$ (empirically between $0.333$ and $0.36$). Validates the criticality bookkeeper as a dynamical predictor and reproduces the Tao-barrier lesson (finding #7) in miniature.
- **Hou-Luo axisymmetric scenario** (`hou_luo/`): RUNS. Axisymmetric NS with swirl in the Hou-Li $(u_1, \omega_1, \psi_1)$ variables on the Luo-Hou wall geometry, with the same refinement diagnostic as `resolution_study/`. At $\nu = 0.005$ the wall-driven stretching event (peak $\|\omega\|_\infty$ x5.1) is fully resolved: the BKM integral converges under $64^2 \to 128^2 \to 256^2$ refinement (last change $0.11\%$). The no-swirl control (globally regular by Ukhovskii-Yudovich/Ladyzhenskaya) shows zero amplification at matched initial vorticity; the $\nu/4$ control triples the peak. Viscosity wins at laptop parameters, as expected; the instrument is now mounted on the one geometry whose inviscid limit provably blows up.

### Architecture 5: non-uniqueness via convex integration

Buckmaster-Vicol (2019): non-uniqueness of weak solutions below the Leray-Hopf class. Isett/Onsager context for Euler.

- This is a survey target, not a numerical experiment: it concerns the boundary of the solution concept, not the smoothness of the strong flow. See the research atlas.

## Status table

| ID | Architecture | Experiment | Status |
|---|---|---|---|
| Phase 0 | shared | criticality bookkeeper + 2D control + smoke test | Done (5/5 smoke tests pass) |
| (d) | 3 | scaling/criticality classification table | RUNS |
| (b) | 4 / control | Burgers inviscid vs viscous shock | RUNS |
| (a) | 1 / 2 | Taylor-Green DNS + BKM integral | RUNS (32^3) |
| (c) | 1 / 3 | energy spectrum + dissipation | RUNS |
| (e) | 4 / control | resolution study: BKM under grid refinement + critical norms | RUNS (16/24/32^3) |
| (f) | 2 | vortex stretching anatomy: budget, alignment, depletion, CF coherence | RUNS (32^3) |
| (g) | 3 / 4 | dyadic shell criticality scan (the bookkeeper, dynamical) | RUNS (40 shells) |
| (h) | 2 | criticality dossier for all conditional criteria | DONE (survey): [docs/research_atlas/conditional_criteria_dossier.md](../docs/research_atlas/conditional_criteria_dossier.md) |
| (i) | 4 | Hou-Luo axisymmetric NS with swirl: refinement + no-swirl + viscosity controls | RUNS (64/128/256^2) |
| (j) | 2 | beta-dial coherence ladder + intense-set sparseness (dossier handoffs 11.3.1-2) | RUNS (32^3) |
| next | 5 | convex-integration non-uniqueness survey | TODO (survey) |
| next | 2 / 4 | beta-dial mounted on Hou-Luo + nu-sweep (does coherence degrade as intensity grows?) | TODO (compute) |

## Conjecture-forge probes (unvetted)

Three falsification probes from the conjecture-forge session live alongside the vetted experiments: `renormalized_profile/` (budget identities, CLEAN), `pressure_hessian_axial/` (inconclusive at $64^3$), `local_induction_depletion/` (null placeholder, needs $N \gtrsim 256$). The underlying conjectures are NOT cleared by the controls; the scripts are reproducible scaffolds, not verdicts.

The cross-field forge run (2026-06-11, [`../docs/03_research/forge_crossfield/`](../docs/03_research/forge_crossfield/)) produced six cards (five wounded, one dead, none unconditionally alive), two audit-confirmed mathematical keepers (the exact backward-kernel vorticity identity with critical $W$; the vortex-tube halo lemma with constant $\sqrt{3}/4$), and one funded-first probe: the **octave ledger post-processor** (`octave_ledger/`, TODO) on the stored Hou-Luo and vortex-stretching outputs, with the circulation-morphology diagnostics co-mounted.

## Cross-references

- Findings synthesis: [`LEARNINGS.md`](LEARNINGS.md)
- Research directions: [`../docs/03_research/research_directions/`](../docs/03_research/research_directions/)
- Research atlas: [`../docs/research_atlas/README.md`](../docs/research_atlas/README.md)
- Lean substrate: [`../lean/README.md`](../lean/README.md)
