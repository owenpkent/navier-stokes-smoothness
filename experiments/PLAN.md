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
- Mapping every criterion onto the criticality coordinate is the next survey target (see TODO and the research directions). The vorticity-direction (Constantin-Fefferman) geometric criterion is the lead.

### Architecture 3: critical spaces and scaling

The scaling symmetry; small-data global existence in $\dot H^{1/2}$ (Fujita-Kato), $L^3$, $\mathrm{BMO}^{-1}$ (Koch-Tataru). The supercriticality gap.

- **Criticality table** (`scaling_criticality/`): RUNS. Classifies the standard norms; energy supercritical, the regularity criteria critical. The headline control.
- **Energy spectrum** (`energy_spectrum/`): RUNS. The spectral picture of where energy lives (large scales) vs where a singularity would form (small scales).

### Architecture 4: blow-up and self-similar solutions

Leray's self-similar ansatz, ruled out in $L^3$ (Necas-Ruzicka-Sverak 1996; Tsai 1998). Tao (2016): finite-time blow-up for an averaged Navier-Stokes (a barrier). Euler blow-up: Elgindi (2021); Hou-Luo and Chen-Hou numerics.

- **Burgers shock** (`burgers_shock/`): RUNS. The viscosity control: inviscid gradient blow-up vs viscous smoothness.
- Resolution studies on near-singular data (higher Reynolds Taylor-Green, the Hou-Luo scenario) are on the TODO; the diagnostic is whether the BKM integral diverges under grid refinement.

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
| next | 2 | criticality dossier for all conditional criteria | TODO (survey) |
| next | 4 | resolution study on near-singular data | TODO (compute) |
| next | 5 | convex-integration non-uniqueness survey | TODO (survey) |

## Cross-references

- Findings synthesis: [`LEARNINGS.md`](LEARNINGS.md)
- Research directions: [`../docs/03_research/research_directions/`](../docs/03_research/research_directions/)
- Research atlas: [`../docs/research_atlas/README.md`](../docs/research_atlas/README.md)
- Lean substrate: [`../lean/README.md`](../lean/README.md)
