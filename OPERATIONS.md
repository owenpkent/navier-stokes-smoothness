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

## 10. The conjecture-forge protocol (a fan-out session pattern)

A reusable session pattern for generating new candidate attacks when a direction stalls and the next move is "think of something genuinely new." It is a structured fan-out, not a one-shot prompt. It exists because the missing object (a coercive, scaling-critical a priori bound) is unlikely to come from incremental work on a single known criterion; the bet is that breadth of first-principles angles, each immediately stress-tested, surfaces a live lead faster than depth on one.

### 10.1 Shape

1. **Forge** (BUILDER per lens). Deploy one BUILDER for each first-principles *lens* below. Each returns a small number of precise, falsifiable conjectures (not restatements of known theorems). Every conjecture carries: a formal statement with quantifiers, a from-the-physics heuristic, the 3D mechanism it engages, the scaling arithmetic, the role of viscosity, the cheapest falsification test (ideally runnable in `experiments/`), and the author's own best guess at how it dies.
2. **Attack** (ADVERSARY per conjecture). Each conjecture is run against four gates (see 10.3) and assigned `alive` / `wounded` / `dead`.
3. **Precedent** (SURVEYOR per survivor). Every non-dead conjecture gets a literature-precedent check (`known` / `partially_known` / `open_new`) with the closest prior work named, so the genuinely new part is isolated from its ancestors.

Dead conjectures are kept, not discarded: each is a coordinate that narrows the search, in keeping with [`docs/researcher_mindset.md`](docs/researcher_mindset.md).

### 10.2 The ten lenses

These extend the five [research directions](docs/03_research/research_directions/) with sharper attack angles. They are deliberately diverse so the failure modes do not correlate.

| Lens | The angle |
|---|---|
| Geometric depletion | Push past Constantin-Fefferman: curvature/torsion of vortex lines, alignment with the strain eigenframe, direction-field functionals that could be a priori bounded. |
| Topological helicity | Helicity is scale-invariant (critical) but signed and non-coercive; build coercive critical quantities from linking, knottedness, helical decomposition. |
| Monotone entropy | The Perelman move: hunt unexpected monotone or almost-monotone functionals (backward self-similar weights, localized entropies, optimal-transport reformulations) that are critical and fail for the averaged caricature. |
| Cascade capacity | The nonlinear flux through Littlewood-Paley shells as a channel with finite capacity; self-improving flux inequalities, minimum-time-per-shell taxes on any blow-up trajectory. |
| Probabilistic genericity | Singularity as an infinitely fine-tuned event: infinite codimension of blow-up data, instability of every collapse profile, almost-sure global well-posedness under forcing. |
| Renormalization / spectral | Liouville theorems for the rescaled equation; computer-assisted instability certificates for would-be self-similar profiles (Chen-Hou machinery aimed at *nonexistence*). |
| Quantitative almost-critical | Erode the gap logarithmically: induction-on-scales with telescoping log loss, regularity under bounds supercritical by only a log factor. |
| Pressure nonlocality | The nonlocal pressure as the hero (restricted Euler blows up; averaging destroys pressure nonlocality): quantitative "pressure defeats local alignment" bounds. |
| ML functional search | Search the low-description-length space of critical functionals with the discriminators built in as hard constraints; symbolic regression / neural conjecturing on DNS trajectories. |
| Anti-lens (blow-up) | Build the singularity to learn from what kills it: Hou-Luo-style scenarios at increasing Reynolds, asymptotically self-similar collapse evading NRS/Tsai. The obstruction map is the skeleton of the regularity proof. |

### 10.3 The four vetting gates

The [three controls](#4-verification-stack) plus the averaged-NS barrier. A conjecture is `dead` if any gate fails outright.

1. **2D control.** Does the mechanism genuinely require vortex stretching, or would it run verbatim in 2D (where the problem is already solved without it)?
2. **Criticality control.** Redo the scaling arithmetic independently. Is every claimed-critical quantity exponent 0, and is the controlled quantity actually coercive (does bounding it bound a BKM/Prodi-Serrin quantity)? Watch the two traps: critical-but-non-coercive (helicity) and coercive-but-secretly-supercritical (anything controlled by energy alone).
3. **Viscosity control.** Does it use $\nu\Delta u$ essentially, or would it equally "prove" regularity for Euler (Elgindi) or Burgers (shocks)?
4. **Tao barrier.** Would the argument apply verbatim to the averaged Navier-Stokes (energy identity and scaling preserved, yet finite-time blow-up)? If yes, it uses only soft structure and is dead. See finding #7 in [`experiments/LEARNINGS.md`](experiments/LEARNINGS.md).

### 10.4 Implementation note

The pattern is realizable as a single background workflow: a `pipeline` over the lenses (Forge stage), each feeding a `parallel` fan of ADVERSARY attacks, with SURVEYOR precedent checks gated on survival. Structured-output schemas force each stage to return validated objects so survivors can be tabulated mechanically. The output is a vetted dossier (statement, kill-reason or survival, precedent status, first experiment) that SYNTHESIZER folds into the relevant research direction. A run was designed and scaffolded in this repo's session history; the protocol is recorded here as a repeatable move, independent of any single run.

## 11. Cross-references

- [`STATE_OF_THE_PROGRAM.md`](STATE_OF_THE_PROGRAM.md): one-page strategic snapshot.
- [`docs/03_research/research_directions/`](docs/03_research/research_directions/): the research directions.
- [`experiments/PLAN.md`](experiments/PLAN.md): test plan.
- [`experiments/LEARNINGS.md`](experiments/LEARNINGS.md): cross-architecture findings.
- [`lean/README.md`](lean/README.md): Lean 4 formalization status.
- [`PHASE_STATE.md`](PHASE_STATE.md): current operational state.
