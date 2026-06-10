# Phase State (operational)

> Read by ORCHESTRATOR at the start of every session. Maintained by SYNTHESIZER. Living document.

## Current state (scaffold)

**Active mode**: AI-augmented (with human owner in critical path). Transition to AI-only execution requires infrastructure and an expert PDE collaborator not yet engaged (see [`OPERATIONS.md`](OPERATIONS.md) §7).

**Current spine.** The program is organized around the **supercriticality gap**: the energy is the only coercive all-time a priori bound and it is supercritical under the scaling, while every regularity criterion (PSL, BKM, ESS) is critical or above. The open problem is to supply a coercive critical (or subcritical) bound that uses 3D vortex stretching and respects that 2D is smooth and that viscosity is essential. Operating philosophy in [`docs/researcher_mindset.md`](docs/researcher_mindset.md).

**Current phase**: Phase 0 (Foundation). Scaffolding, controls, and coarse experiments in place. Analytic core not started (it is the open problem).

## Phase 0 deliverables done

- Repo structure mirrored from the companion analysis repo, adapted to Navier-Stokes.
- Layered docs: intuitive, undergraduate, graduate (scaling + supercriticality + regularity criteria), research overview, implications, solutions catalog, research atlas.
- Five numbered research directions in [`docs/03_research/research_directions/`](docs/03_research/research_directions/).
- Shared experiment infrastructure: the `Flow3D` solver interface, the criticality bookkeeper CONTROL, the 2D control, and the smoke test.
- Four experiments, at least two runnable end-to-end on a laptop:
  - `scaling_criticality/criticality_table.py` (runs, classifies norms).
  - `burgers_shock/burgers_blowup.py` (runs, inviscid gradient blow-up vs smooth viscous solution).
  - `taylor_green/taylor_green_dns.py` (runs at 32^3; tracks energy, enstrophy, max vorticity, BKM integral).
  - `energy_spectrum/energy_spectrum.py` (runs; reads TG output or a synthetic field).
- Lean 4 skeleton with documented `sorry`s: divergence-free fields, Leray projector, energy inequality, BKM criterion, scaling, global-regularity goal.
- Agent role specifications in [`.claude/agents/`](.claude/agents/).
- Operations guide ([`OPERATIONS.md`](OPERATIONS.md)) and strategic snapshot ([`STATE_OF_THE_PROGRAM.md`](STATE_OF_THE_PROGRAM.md)).

## Phase 0 deliverables remaining

- Independent expert verification (HUMAN: requires a PDE-analyst correspondent).
- Lean 4 / Mathlib expansion: the skeleton is documented `sorry`. Mathlib lacks Sobolev-spaces-of-vector-fields and Leray-projection infrastructure; a clean statement of even the energy inequality needs upstream work. Build is not expected to be green yet.
- Research-resolution DNS (current experiments are deliberately coarse).

## Architecture status

- **Arch 1 (energy / weak solutions)**: foundational and mapped. Leray-Hopf existence and CKN partial regularity are the baseline; the energy is supercritical (criticality bookkeeper confirms).
- **Arch 2 (conditional criteria)**: mapped. PSL, BKM, ESS all at critical scaling. The vorticity-direction (Constantin-Fefferman) geometric criterion is flagged as the most promising critical-control survey target.
- **Arch 3 (critical spaces)**: mapped. Small-data global existence in $\dot H^{1/2}$, $L^3$, $\mathrm{BMO}^{-1}$; large data open; the supercriticality gap is the obstruction.
- **Arch 4 (blow-up / self-similar)**: mapped. No NS example; Leray self-similar ruled out in $L^3$; Tao's averaged-NS blow-up is the barrier; Euler blow-up (Elgindi) and Hou-Luo numerics inform where to look.
- **Arch 5 (convex integration)**: mapped. Buckmaster-Vicol non-uniqueness below energy class; sharpens the solution concept, outside the regularity discipline.

## Compute budget

| Item | Used | Budgeted | Remaining |
|---|---|---|---|
| Project sessions to date | 1 (scaffold) | unbounded (project-level) | n/a |
| Lean proofs landed | 0 (skeleton only) | per-direction | substantial |
| DNS at research resolution | 0 | as needed | substantial |

## Recommended next session actions

1. **Survey the critical/conditional regularity landscape** (SURVEYOR): produce a dossier mapping every known regularity criterion (PSL, BKM, ESS, one-component Neustupa-Penel, vorticity-direction Constantin-Fefferman, Beirao da Veiga, Cheskidov-Shvydkoy) onto the sub/critical/super coordinate, and identify which have been weakened to genuinely scale-invariant geometric conditions. The Constantin-Fefferman vorticity-coherence result is the lead.
2. **Near-singular data** (BUILDER + ADVERSARY): the Taylor-Green resolution study is DONE (`experiments/resolution_study/`, BKM converges at laptop parameters; LEARNINGS #11). Next: set up the Hou-Luo axisymmetric scenario at coarse resolution and apply the same refinement diagnostic.
3. **Lean: state the energy inequality cleanly** (VERIFIER): attempt a Mathlib-faithful statement of $\tfrac12\|u(t)\|_2^2 + \nu\int_0^t\|\nabla u\|_2^2 \le \tfrac12\|u_0\|_2^2$, identifying the exact Mathlib gap (vector-valued Sobolev spaces). Document the gap as a VERIFIER target.

## Falsifiability triggers

- A proposed a priori bound turns out supercritical under the criticality bookkeeper: this is the default outcome and the constant discipline. NOT a one-time trigger; it is the filter.
- A candidate regularity argument applies verbatim to 2D and would predict 2D blow-up: TRIGGERED means the method ignores 3D structure. Currently NOT TESTED against any candidate (no candidate yet).
- A candidate blow-up mechanism is killed by viscosity in a resolution study: the diagnostic that looked divergent converges. INSTRUMENT CALIBRATED (`experiments/resolution_study/`: BKM converges in the known-smooth regime; the trigger now has a defined readout). Not yet tested against a near-singular scenario.
- A direction shows no measurable progress over N sessions: NOT YET (one session).

## Pending agent outputs

None (scaffold session).

## Last verified state

- Git commit: 37b8c9f (the three new experiments). See README Status table.
- Experiments verified to run (2026-06-10, all end-to-end, numbers matching the committed READMEs and LEARNINGS): `scaling_criticality/criticality_table.py`, `dyadic_shell/criticality_scan.py` (boundary at alpha_c = 1/3), `vortex_stretching/alignment_depletion.py` (budget <0.65% in resolved window, depletion 0.53), `resolution_study/bkm_refinement.py` (BKM converges, last change 0.39%/0.25%). Earlier confirmed: `burgers_shock/`, `taylor_green/`, `energy_spectrum/`, smoke test.
- Lean: skeleton only, documented `sorry`, build not attempted.

## Session log (recent)

| Date | Session focus | Commits | Key outputs |
|---|---|---|---|
| scaffold | Stand up the repo: structure, docs, controls, four experiments, Lean skeleton, agents | scaffold | The supercriticality spine; criticality bookkeeper + 2D + viscosity controls; Taylor-Green DNS; Burgers shock comparison; five research directions; LEARNINGS seeded with real findings. |
| 2026-06-09 | Three new local experiments (e, f, g) | 37b8c9f | `resolution_study/` (BKM converges under refinement, instrument calibrated, LEARNINGS #11); `vortex_stretching/` (budget verified, depletion ~0.53, CF coherence measured, LEARNINGS #10); `dyadic_shell/` (criticality boundary at alpha_c = 1/3 confirmed dynamically, LEARNINGS #9). PLAN status table updated. |
| 2026-06-10 | Re-ran all five fast experiments end-to-end | pending | Reproduced committed numbers exactly (dyadic boundary, criticality table, vortex-stretching budget/depletion, BKM convergence). Last-verified state refreshed to 37b8c9f. |

## How to update this file

- ORCHESTRATOR: update "Recommended next session actions" at session end.
- SYNTHESIZER: update everything else after agent outputs land.
- Always update "Last verified state" with the latest commit hash.
- Always update "Session log" with the latest session's work.
