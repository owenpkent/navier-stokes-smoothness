# CLAUDE.md

Project-specific instructions for Claude Code. Read on every session start. This file carries both the project's technical context (architectures, conventions, the solver interface) and the human-side context (owner, tech stack, agent infrastructure).

## What this repo is

A research-and-study project on the Navier-Stokes existence and smoothness problem (Clay Millennium Problem). It contains:
- Layered docs (intuitive, undergraduate, graduate, research) on the 3D incompressible Navier-Stokes equations
- A strategic landscape document (`docs/research_atlas/`) cataloging every known proof approach with its obstructions
- A computational experimental thread (`experiments/`) organized around the candidate proof architectures and the wrong-approach detectors
- A Lean 4 / Mathlib formalization skeleton (`lean/`)

It is **not** a tool or product. It is a research codebase. Output is markdown documents, numerical experiments, visualizations, and Lean proofs.

## Stance (read this before writing any framing)

The posture of this project is that we are trying to solve the problem. It is hard and the odds are long, but it is a target, not a monument, and nothing here should be written as if the problem were impossible.

When you document a negative result, frame it as progress. A method that fails (an energy-controlled estimate that is supercritical, a candidate that does not use 3D vortex stretching and would equally "apply" to predict 2D blow-up, a self-similar ansatz ruled out in $L^3$) has removed a dead branch and sharpened where the real proof must live. Each "this won't work" is a coordinate that narrows the search.

Specifically, avoid fatalistic phrasing ("stuck," "hopeless," "can never"). Prefer the directional reading: the supercriticality finding is a **compass** that says the proof must add genuinely critical control engaging the exact 3D structure, not a wall. Keep the math exactly as rigorous as it is (a supercritical estimate really is supercritical; 2D really is globally smooth). Change the tone, not the theorems.

## About the owner

The owner is Owen, a wheelchair user with muscular dystrophy.

- **Typing is hard.** Be proactive. Make decisions. Don't ask for confirmation on small things.
- **Offer A/B/C choices** when input is needed. One letter is faster than a sentence.
- **PowerShell on Windows.** Use PowerShell syntax. Prefer single-line commands.
- **Accessibility matters.** Many of Owen's projects are tools he actually uses.

## START HERE

- **Mindset and philosophy**: [`docs/researcher_mindset.md`](docs/researcher_mindset.md). How this project works: the problem is a target not a monument, we advance a front, negative results are coordinates, honesty is the engine. Read this first; it defines what counts as progress.
- **Research strategy**: [`docs/research_atlas/README.md`](docs/research_atlas/README.md). Comprehensive catalog of all approaches, what failed, what's missing.
- **Experiments**: [`experiments/PLAN.md`](experiments/PLAN.md). The test plan with current status per architecture.
- **Proof program state**: [`PHASE_STATE.md`](PHASE_STATE.md) (current operational state), [`OPERATIONS.md`](OPERATIONS.md) (how to drive the agent loop).
- **Lean 4 substrate**: [`lean/README.md`](lean/README.md). VERIFIER target table.

## Core conceptual framework

The project is organized around **five candidate proof architectures** (from `docs/solutions/README.md` and `experiments/PLAN.md`):

1. **Energy methods and weak solutions**: Leray-Hopf weak solutions (1934, 1951) exist globally; uniqueness/regularity in 3D is open. Partial regularity: Caffarelli-Kohn-Nirenberg (1982), the 1D parabolic Hausdorff measure of the singular set is zero.
2. **Conditional regularity criteria**: Beale-Kato-Majda (control of $\int_0^T \|\omega(t)\|_{L^\infty}\, dt$ prevents blow-up), Prodi-Serrin-Ladyzhenskaya ($u \in L^p_t L^q_x$ with $2/p + 3/q \le 1$), Escauriaza-Seregin-Sverak (the borderline $L^\infty_t L^3_x$ case).
3. **Critical spaces and scaling**: the scaling $u_\lambda(x, t) = \lambda\, u(\lambda x, \lambda^2 t)$; small-data global existence in critical spaces (Fujita-Kato $\dot H^{1/2}$, Koch-Tataru $\mathrm{BMO}^{-1}$); the **supercriticality gap**: energy is supercritical relative to the scaling, so energy bounds alone cannot close regularity.
4. **Blow-up and self-similar solutions**: Leray's self-similar ansatz, ruled out in $L^3$ (Necas-Ruzicka-Sverak; Tsai); Tao (2016) finite-time blow-up for an averaged Navier-Stokes (a barrier result); modern numerically-supported Euler blow-up (Elgindi; Chen-Hou).
5. **Non-uniqueness via convex integration**: Buckmaster-Vicol (2019), non-uniqueness of weak solutions below the Leray-Hopf class; Isett/Onsager context for Euler.

The structural commitment of the project: **regularity is a critical-scaling statement**, and the energy is subcritical-in-the-wrong-direction (supercritical). A method that lives only at the energy level cannot close regularity, because energy is compatible with worlds where the solution concentrates at small scales. Knowing that tells us where the proof must live (genuinely critical control), so we spend effort there. Ruling a level out is how the search narrows.

## The wrong-approach discipline

Three structural detectors play the role that the Davenport-Heilbronn L-function plays in the companion zeta repo. Any candidate method must pass all three.

1. **2D Navier-Stokes is globally well-posed and smooth** (Ladyzhenskaya, Leray). In 2D the vorticity is transported with diffusion ($\partial_t \omega + u \cdot \nabla \omega = \nu \Delta \omega$, scalar, no stretching term) and the enstrophy $\int |\omega|^2$ is non-increasing. Any method that does not genuinely use 3D structure (vortex stretching, $\omega \cdot \nabla u$) and would equally "apply" to predict 2D blow-up is wrong. **2D is the must-stay-smooth control.**
2. **Supercriticality is the structural ceiling** (the analog of the Vinogradov-Korobov $2/3$ exponent in the zeta repo). Any a priori bound controlled by the energy norm is supercritical with respect to the scaling, so it cannot by itself reach a critical or subcritical regularity statement. A proof must add genuinely critical control. Implemented as `experiments/_shared/criticality.py` (the criticality bookkeeper).
3. **Controls that DO blow up or break**: inviscid Burgers forms shocks in finite time; 3D Euler has modern finite-time singularity evidence and results (Elgindi). These show viscosity and the precise NS structure are essential; a method blind to viscosity is suspect. Implemented as `experiments/burgers_shock/`.

Architecture 5 (convex integration) sits partly outside this discipline: it deliberately produces non-smooth, non-unique weak solutions below the energy class, so it is about the boundary of what "solution" means rather than about regularity of the smooth flow.

## Repository structure

```
navier-stokes-smoothness/
├── docs/
│   ├── 00_intuitive/            intuitive-level explanations
│   ├── 01_undergraduate/        undergrad-level explanations
│   ├── 02_graduate/             graduate-level (scaling, supercriticality, regularity criteria)
│   ├── 03_research/             research-level overviews; numbered directions; reading notes
│   ├── implications/            why the problem matters
│   ├── solutions/               known proof attempts/approaches
│   ├── research_atlas/          master research map; all approaches, failures, ML directions
│   └── researcher_mindset.md    operating philosophy
├── experiments/
│   ├── PLAN.md                  the test plan with per-architecture status
│   ├── LEARNINGS.md             cross-cutting findings synthesis
│   ├── _shared/                 solver interface, criticality bookkeeper (CONTROL), 2D control, smoke test
│   ├── taylor_green/            pseudo-spectral DNS of the Taylor-Green vortex
│   ├── burgers_shock/           inviscid vs viscous Burgers (viscosity control)
│   ├── energy_spectrum/         energy spectrum + dissipation from the TG run
│   └── scaling_criticality/     sub/critical/super classification of norms
├── lean/                        Lean 4 / Mathlib formal verification (skeleton)
│   ├── NavierStokes.lean
│   └── NavierStokes/{DivergenceFree,LerayProjector,EnergyInequality,
│                     BealeKatoMajda,GlobalRegularity,Scaling}.lean
├── .claude/agents/              Six agent role specs (surveyor/builder/verifier/adversary/synthesizer/orchestrator)
├── sources/                     source PDFs and their text conversions
├── visualizations/              manim scenes
├── memory/                      cross-session persistent memory
├── CLAUDE.md                    this file
├── README.md                    project overview, status, structure map
├── TODO.md                      task tracking (- [ ] checkbox format)
├── OPERATIONS.md                how to operate this repo as the research-program substrate
├── STATE_OF_THE_PROGRAM.md      one-page strategic snapshot
└── PHASE_STATE.md               current phase, sub-task, falsifiability triggers, next-session plan
```

## Tech stack

- **Language**: Python (primary). Lean 4 (formal verification).
- **Python libraries**: `numpy`, `scipy` (FFT-based pseudo-spectral solvers, ODE integration), `matplotlib`. Optional: `mpmath`, `sympy`, `manim`.
- **Visualization**: manim (3Blue1Brown style). `pip install manim`.
- **Formal verification**: Lean 4 + Mathlib (`lean/` directory, requires `elan` to build).
- **Docs**: Markdown with LaTeX math (`$...$` inline, `$$...$$` block in files; plain Unicode in chat).

## Conventions

- **Pseudo-spectral discretization**: periodic torus $\mathbb{T}^3 = [0, 2\pi)^3$, Fourier collocation via `numpy.fft`. Keep grids small (32^3 or 48^3) so experiments finish fast. 2/3-rule dealiasing where it matters.
- **Data format**: experiments save `.npz` (numpy compressed) alongside the script. Plots save as `.png`. Both are gitignored under `experiments/**/_cache/` and `experiments/**/*.png`.
- **Solver interface**: 3D solvers expose a `step()` and report diagnostics (kinetic energy, enstrophy, max vorticity). The Taylor-Green and energy-spectrum experiments share this.
- **Criticality bookkeeper**: `experiments/_shared/criticality.py` classifies any norm as sub/critical/super under the NS scaling. It is a CONTROL: it flags any proposed a priori estimate that is supercritical.

## Style

- **No em dashes** anywhere. (Global preference. Use periods, colons, parentheses, or hyphens instead.) Do not use en dashes either. Rewrite the sentence instead.
- Inline math in markdown uses `$...$` for inline, `$$...$$` for display.
- In chat output the KaTeX surface is not available; use Unicode and plain text for math.
- Code: explanatory module-level docstrings, minimal inline comments. Comments should explain WHY, not WHAT.

## Running things

```powershell
# Smoke test the shared infrastructure
python -m experiments._shared.smoke_test

# Run experiments (each is a python module)
python -m experiments.scaling_criticality.criticality_table
python -m experiments.burgers_shock.burgers_blowup
python -m experiments.taylor_green.taylor_green_dns
python -m experiments.energy_spectrum.energy_spectrum

# Build the Lean substrate (requires elan + lake)
cd lean; lake build
```

Working dir is the repo root. Scripts use `from experiments._shared import ...` style imports, which only resolve from the root.

## Git commits

```powershell
git add -A; git commit -m "docs: add intuitive explanation"
```

Conventional commits: `feat:`, `fix:`, `docs:`, `refactor:`, `chore:`. Never commit or push without per-action authorization.

## Agent infrastructure

This repo is structured as the operational substrate for an AI-augmented research program. Six agent roles in `.claude/agents/`:

- **SURVEYOR**: literature synthesis + scorecard maintenance.
- **BUILDER**: propose mathematical constructions (estimates, candidate criteria).
- **VERIFIER**: translate to Lean 4 / Mathlib and verify.
- **ADVERSARY**: 2D-control + criticality + viscosity discipline; counterexample search.
- **SYNTHESIZER**: integrate verified outputs into the project dossier.
- **ORCHESTRATOR**: schedule work; manage compute budget; decide abandonment.

See [`OPERATIONS.md`](OPERATIONS.md) for the full operational guide.

## Known landmarks

- The scaling symmetry: if $(u, p)$ solves NS, so does $u_\lambda(x, t) = \lambda\, u(\lambda x, \lambda^2 t)$, $p_\lambda(x, t) = \lambda^2 p(\lambda x, \lambda^2 t)$. The homogeneous critical Sobolev space is $\dot H^{1/2}(\mathbb{R}^3)$; $L^3(\mathbb{R}^3)$ and $\mathrm{BMO}^{-1}$ are also critical.
- Prodi-Serrin-Ladyzhenskaya: $u \in L^p_t L^q_x$ with $2/p + 3/q \le 1$, $q > 3$, implies regularity. The endpoint $q = 3$ ($p = \infty$) is Escauriaza-Seregin-Sverak (2003).
- Beale-Kato-Majda: a solution stays smooth on $[0, T]$ iff $\int_0^T \|\omega(t)\|_{L^\infty}\, dt < \infty$.
- Caffarelli-Kohn-Nirenberg (1982): the one-dimensional parabolic Hausdorff measure of the singular set of a suitable weak solution is zero.
- Energy equality / inequality: $\tfrac12 \|u(t)\|_{L^2}^2 + \nu \int_0^t \|\nabla u\|_{L^2}^2 \le \tfrac12 \|u_0\|_{L^2}^2$. This is the only coercive globally-in-time a priori bound, and it is supercritical.
- 2D is globally regular (Ladyzhenskaya 1959; the enstrophy is controlled because there is no vortex stretching).

## When in doubt

- The atlas (`docs/research_atlas/README.md`) is the master reference for what's been tried and what's stuck.
- The plan (`experiments/PLAN.md`) is the master reference for the experimental thread.
- The three wrong-approach detectors (2D control, criticality bookkeeper, viscosity/Burgers control) are the project's structural sanity checks.
- If a proposed method does not engage the supercriticality gap or the 3D vortex-stretching structure, it is probably not regularity-closing.

## Constellation

This repo is tracked by Constellation. It has `README.md` with `## Status` and `TODO.md` with checkboxes.
