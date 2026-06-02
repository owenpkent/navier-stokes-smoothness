# Operations Guide: running the Navier-Stokes research program

> How to run this repo as the operational substrate for an AI-augmented (and, speculatively, AI-only) research program on the Navier-Stokes existence and smoothness problem.
>
> **Scope of this guide**: how to launch sessions, deploy agents, maintain state, escalate to human review. Not the mathematical content (that lives in `experiments/`, `docs/03_research/`, `lean/`).

## 1. The repo as substrate

This repository is structured as the operational substrate for AI-augmented execution:

| Component | Path | Role |
|---|---|---|
| Agent role specifications | [`.claude/agents/`](.claude/agents/) | Six specialized agents: surveyor, builder, verifier, adversary, synthesizer, orchestrator. Each is a subagent that can be deployed via the `Agent` tool. |
| Phase state | [`PHASE_STATE.md`](PHASE_STATE.md) | Current phase, current sub-task, last verification, next steps. Read by ORCHESTRATOR at start of every session. |
| Project narrative | [`experiments/LEARNINGS.md`](experiments/LEARNINGS.md) | Cross-architecture findings. Updated by SYNTHESIZER. |
| Status table | [`experiments/PLAN.md`](experiments/PLAN.md) | Per-experiment status. Updated as work lands. |
| Strategic snapshot | [`STATE_OF_THE_PROGRAM.md`](STATE_OF_THE_PROGRAM.md) | One-page where-every-architecture-stands. |
| Research directions | [`docs/03_research/research_directions/`](docs/03_research/research_directions/) | Per-direction execution roadmaps. |
| Formal verification | [`lean/`](lean/) | Lean 4 / Mathlib project. Every structural claim verified here is canonical. |
| Persistent memory | [`memory/MEMORY.md`](memory/) | Cross-session context. Read at session start. |

## 2. The session loop

Each session follows this pattern:

### 2.1 Session start

1. ORCHESTRATOR reads [`PHASE_STATE.md`](PHASE_STATE.md) and [`experiments/LEARNINGS.md`](experiments/LEARNINGS.md).
2. ORCHESTRATOR decides the session goal based on the prior session's recommended next steps.
3. ORCHESTRATOR deploys agents via the `Agent` tool with `subagent_type` matching the role (e.g., `subagent_type: surveyor`).

### 2.2 Agent deployment (parallel where possible)

For mapping work:
- Deploy 1-3 SURVEYORs on the relevant sub-corpus (e.g., partial-regularity papers post-CKN, convex-integration papers post-2018).
- Deploy 3-5 BUILDERs on the same research direction with different attack angles.
- Deploy 1-2 VERIFIERs to formalize BUILDER outputs.
- Deploy 1-2 ADVERSARYs to stress-test outputs against the three controls (2D, criticality, viscosity).

The `Agent` tool supports multiple parallel agents via separate tool calls in a single message.

### 2.3 Synthesis

After agent outputs land:
- Deploy SYNTHESIZER to integrate the verified outputs.
- SYNTHESIZER updates [`experiments/LEARNINGS.md`](experiments/LEARNINGS.md), [`experiments/PLAN.md`](experiments/PLAN.md), [`PHASE_STATE.md`](PHASE_STATE.md).

### 2.4 Session end

ORCHESTRATOR writes to [`PHASE_STATE.md`](PHASE_STATE.md):
- Current phase + sub-task.
- Sessions used / budgeted.
- Pending agent outputs.
- Recommended next agent deployments.
- Falsifiability triggers approaching or hit.

### 2.5 Commit

The session's work is committed to git with a clear message: "Direction X: BUILDER outputs + VERIFIER results + ADVERSARY findings". Each commit is reproducible.

## 3. Scheduled / continuous execution

For sustained compute, the session loop runs on a schedule:

- `/loop`: AI self-paces iterations. Useful for tight feedback loops within a direction.
- `/schedule`: cron-driven scheduled agent runs. Useful for a long horizon.

## 4. Verification stack

Every claim must pass through a layered verification stack before becoming canonical:

1. **Mechanical computation**: a numerical experiment in `experiments/` that runs and reports diagnostics. For DNS claims, at least a resolution-doubling check (does the diagnostic converge as the grid refines?).
2. **Symbolic verification**: symbolic algebra (`sympy`) where applicable (e.g., verifying a scaling exponent or an energy identity by hand-checked algebra).
3. **The three controls**: every proposed method is run against the 2D control, the criticality bookkeeper, and the viscosity/Burgers control. A method that fails any control is structurally wrong.
4. **Formal proof in Lean 4**: structural claims (the energy inequality, the Beale-Kato-Majda criterion statement, the scaling identity) are formalized in [`lean/NavierStokes/`](lean/NavierStokes/).

A claim is canonical when the relevant layers agree. Until then it is provisional and marked as such.

## 5. Escalation to human review

Certain decisions warrant human review:

- **A claimed proof of global regularity**: submit to human peer review before any announcement. The verification stack catches errors but human judgment validates the formalization.
- **A claimed finite-time blow-up construction**: even stronger requirement. Verify the numerical evidence against multiple independent code paths and resolution studies, and (if a rigorous construction) human-check the analysis.
- **A discovery that the architectural picture is wrong**: e.g., a genuinely critical a priori bound from the energy. Surface to human review before pivoting.
- **A novel mathematical object requiring expert judgment**: e.g., a candidate Lyapunov functional or a new critical norm. Expert review of mathematical taste.

ORCHESTRATOR explicitly flags such situations and pauses pending human input.

## 6. Falsifiability triggers

The program is restructured (or a direction abandoned) if:

- The criticality bookkeeper shows the proposed a priori bound is supercritical (no genuinely critical control added). This is the default failure mode and the discipline against it is constant.
- A candidate regularity argument applies verbatim to 2D AND would predict 2D blow-up (it cannot, since 2D is smooth), meaning it does not use 3D structure.
- A candidate "blow-up" mechanism is killed by viscosity in the resolution study (the diagnostic that looked divergent converges under refinement).
- A direction shows no measurable progress (no new estimate, no Lean target closed, no control passed) over N sessions.

ORCHESTRATOR tracks these triggers in [`PHASE_STATE.md`](PHASE_STATE.md).

## 7. Costs and prerequisites

To actually run this as a serious program:

| Resource | Note |
|---|---|
| Compute (DNS at research resolution, $512^3$ and up) | Large; the in-repo experiments are deliberately coarse ($32^3$) to run on a laptop. |
| Lean 4 / Mathlib expansion | Mathlib has limited PDE / Sobolev-space-for-vector-fields coverage; substantial work to formalize even the energy inequality cleanly. |
| Human oversight (expert PDE analysts) | Required for the analytic core. |

This is a major-mathematics research investment. The in-repo artifacts are the scaffolding, the controls, and the coarse experiments, not the proof.

## 8. Current state

See [`PHASE_STATE.md`](PHASE_STATE.md) for the authoritative current state. As of scaffold:
- The shared infrastructure is in place (solver interface, criticality bookkeeper control, 2D control, smoke test).
- Two experiments run end-to-end on a laptop (the scaling/criticality classifier and the Burgers shock comparison); the Taylor-Green DNS and the energy-spectrum experiment also run at coarse resolution.
- The Lean substrate is a documented `sorry` skeleton (need not build yet).
- The docs and the research-direction specs are written.

**Not yet done**: research-resolution DNS, a serious Lean/Mathlib expansion, and the analytic core (which is the open problem).

## 9. For someone picking up this repo

1. **Read** [`PHASE_STATE.md`](PHASE_STATE.md) for current state.
2. **Read** [`experiments/LEARNINGS.md`](experiments/LEARNINGS.md) for the cumulative narrative.
3. **Read** [`docs/researcher_mindset.md`](docs/researcher_mindset.md) for the operating philosophy.
4. **Read** [`.claude/agents/orchestrator.md`](.claude/agents/orchestrator.md) for how to drive sessions.
5. **Run** one session of ORCHESTRATOR to plan the next direction of work.
6. **Deploy** the agents ORCHESTRATOR recommends, via the `Agent` tool with appropriate `subagent_type`.
7. **Commit** the session's work with a clear message.
8. **Update** PHASE_STATE.md for the next session.

This is iterative. The compounding effect across many sessions is what produces the program output.

## 10. Cross-references

- [`STATE_OF_THE_PROGRAM.md`](STATE_OF_THE_PROGRAM.md): one-page strategic snapshot.
- [`docs/03_research/research_directions/`](docs/03_research/research_directions/): the research directions.
- [`experiments/PLAN.md`](experiments/PLAN.md): test plan.
- [`experiments/LEARNINGS.md`](experiments/LEARNINGS.md): cross-architecture findings.
- [`lean/README.md`](lean/README.md): Lean 4 formalization status.
- [`PHASE_STATE.md`](PHASE_STATE.md): current operational state.
