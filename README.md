# Navier-Stokes Existence and Smoothness: Deep Study Repo

A multi-level exploration of the 3D incompressible Navier-Stokes equations and the Clay Millennium problem of global existence and smoothness: from intuitive visual understanding through graduate-level PDE analysis to the frontier of current research. Includes a computational experimental thread organized around the candidate proof architectures and the structural obstructions that any proof must overcome.

**Operational substrate**: this repo is also structured as the substrate for an AI-augmented (and, speculatively, AI-only) research program on the problem. See [`STATE_OF_THE_PROGRAM.md`](STATE_OF_THE_PROGRAM.md) for a one-page repo-wide strategic snapshot (where every architecture stands and the single most-leveraged next move), [`OPERATIONS.md`](OPERATIONS.md) for how to operate it, [`PHASE_STATE.md`](PHASE_STATE.md) for current state, and [`docs/03_research/research_directions/`](docs/03_research/research_directions/) for the numbered direction specs. The repo is a handoff artifact: the scaffolding and the experimental controls are in place; the deep analytic work requires expert collaborators and sustained effort.

## What's Here

This repo is structured so you can enter at any level and go as deep as you want.

```
navier-stokes-smoothness/
├── docs/                        # All written explanations
│   ├── 00_intuitive/            # No math required: visual, conceptual
│   ├── 01_undergraduate/        # Vector calculus, ODEs, basic PDEs
│   ├── 02_graduate/             # Sobolev spaces, weak solutions, scaling,
│   │                            #   the supercriticality of the energy estimate
│   ├── 03_research/             # Current approaches, RESEARCH DIRECTIONS
│   │   ├── research_directions/ # Numbered research-grade direction specs
│   │   └── reading_notes/       # Notes on the key reference sources
│   ├── implications/            # Why it matters (turbulence, engineering, math)
│   ├── solutions/               # Known approaches and their obstructions
│   ├── research_atlas/          # Master research map: attempts, failures, ML directions
│   └── researcher_mindset.md    # Operating philosophy (target not monument)
├── experiments/                 # Computational thread; control + architecture tests
│   ├── PLAN.md                  # Test plan + AI-centric methodology
│   ├── LEARNINGS.md             # Cross-cutting findings
│   ├── _shared/                 # Solver interface, criticality bookkeeper (CONTROL), 2D control
│   ├── taylor_green/            # Pseudo-spectral DNS of the Taylor-Green vortex (RUNNABLE)
│   ├── burgers_shock/           # Inviscid vs viscous Burgers blow-up (RUNNABLE)
│   ├── energy_spectrum/         # Energy spectrum and dissipation from the TG run
│   └── scaling_criticality/     # Sub/critical/super classification of norms (RUNNABLE)
├── references/                  # Reference library index (gitignored PDFs) + tracked index
├── lean/                        # Lean 4 / Mathlib formal verification (skeleton)
│   ├── lakefile.lean
│   ├── NavierStokes.lean        # Main module
│   └── NavierStokes/            # DivergenceFree, LerayProjector, EnergyInequality, BKM, ...
├── .claude/agents/              # AI agent role specifications
├── sources/                     # Original PDFs and converted text
├── visualizations/              # manim animation scripts
├── memory/                      # Cross-session persistent memory
├── OPERATIONS.md                # How to operate this repo as the research substrate
├── PHASE_STATE.md               # Current operational state (read by ORCHESTRATOR)
└── CLAUDE.md                    # Project + owner context for AI assistants
```

## The Question

The **Navier-Stokes existence and smoothness problem** asks, for the 3D incompressible Navier-Stokes equations on $\mathbb{R}^3$ (or the torus $\mathbb{T}^3$) with viscosity $\nu > 0$:

> Given smooth, divergence-free initial velocity of finite energy, prove EITHER global-in-time existence of a smooth (finite-energy) solution, OR exhibit smooth initial data that leads to finite-time blow-up.

The equations are

$$\partial_t u + (u \cdot \nabla) u = -\nabla p + \nu \Delta u, \qquad \nabla \cdot u = 0,$$

with $u : \mathbb{R}^3 \times [0, \infty) \to \mathbb{R}^3$ the velocity field and $p$ the pressure. It is one of the seven Clay Millennium Prize Problems (worth \$1,000,000). The official problem statement is Charles Fefferman's. Weak solutions have been known to exist globally since Leray (1934), but whether they are unique and smooth in three dimensions is open.

## Stance

We are trying to solve this. That is the posture of the whole repo.

It is hard. The odds against any single program are long, and the honest baseline is ninety years of effort by the best analysts alive. But "hard" is not "impossible," and this project treats global regularity (or its failure) as a target, not a monument.

Read every negative result here in that spirit. When an experiment shows that a method fails (an energy bound is supercritical with respect to the scaling, a candidate would equally "predict" blow-up in 2D where solutions are known smooth, a self-similar ansatz is ruled out in $L^3$), that is **progress**: it removes a dead branch and sharpens where the real proof must live. Each "this won't work" is a coordinate that narrows the search, not a verdict that the search is hopeless.

The dominant structural finding (the energy estimate is **supercritical** relative to the scaling symmetry, so energy bounds alone cannot close regularity) is a compass, not a wall. It tells us exactly where new control must come from. The job is to keep digging there.

## Levels

| Level | Folder | Prerequisites |
|-------|--------|---------------|
| Intuitive | `docs/00_intuitive/` | None: curiosity only |
| Undergraduate | `docs/01_undergraduate/` | Vector calculus, ODEs |
| Graduate | `docs/02_graduate/` | Real analysis, functional analysis, PDE |
| Research | `docs/03_research/` | Graduate analysis + PDE |
| **Research Atlas** | `docs/research_atlas/` | **Start here for ML research**: full catalog of approaches, failures, obstructions, ML directions |

## Visualizations (manim)

Built with [manim](https://www.manim.community/) (3Blue1Brown's animation engine). See `visualizations/README.md` for setup and how to render each scene.

## Experimental thread

See [`experiments/PLAN.md`](experiments/PLAN.md) for the test plan. The candidate proof architectures (energy/weak solutions, conditional regularity criteria, critical-space/scaling methods, blow-up and self-similar solutions, non-uniqueness via convex integration) are tested against a set of **wrong-approach detectors**: 2D Navier-Stokes (must stay smooth), the criticality bookkeeper (any energy-controlled estimate is supercritical), and the inviscid controls (Burgers shocks, Euler blow-up) that show viscosity is essential.

Smoke test:

```powershell
python -m experiments._shared.smoke_test
```

## Cross-cutting findings

Synthesis of structural insights lives in [`experiments/LEARNINGS.md`](experiments/LEARNINGS.md). The dominant meta-finding: **the energy estimate is supercritical**. The kinetic energy $\tfrac12 \int |u|^2$ and its dissipation give the only globally-conserved-in-time a priori control in 3D, but under the scaling $u_\lambda(x, t) = \lambda\, u(\lambda x, \lambda^2 t)$ the energy norm scales with a positive power of $\lambda$, so it provides no control at small scales. Every classical regularity criterion (Prodi-Serrin-Ladyzhenskaya, Beale-Kato-Majda, the borderline $L^3$ result of Escauriaza-Seregin-Sverak) sits at or above the critical level that the energy cannot reach. This is the project's most useful piece of map: a winning proof must add genuinely **critical** (scaling-invariant) control that uses the exact structure of the 3D nonlinearity (vortex stretching), not the energy alone.

## Status

| Area | Status |
|------|--------|
| Repo structure | Complete |
| Solutions / approach catalog | `docs/solutions/` |
| Research atlas | `docs/research_atlas/` |
| Graduate docs (scaling, supercriticality, regularity criteria) | Substantial |
| Experiments: Phase 0 infrastructure | Complete (solver interface + criticality bookkeeper control + 2D control + smoke test) |
| Experiments: Taylor-Green DNS | Runnable (32^3 default; tracks energy, enstrophy, max vorticity, BKM integral) |
| Experiments: Burgers shock vs viscous | Runnable (inviscid gradient blow-up vs smooth viscous solution) |
| Experiments: scaling/criticality table | Runnable (classifies norms sub/critical/super) |
| Experiments: energy spectrum | Runnable (reads TG output; falls back to a synthetic field) |
| Lean 4 / Mathlib skeleton | Skeleton with documented `sorry`s (need not build) |
| Conjecture-forge protocol | Documented session pattern ([`OPERATIONS.md`](OPERATIONS.md) §10): ten first-principles lenses, four vetting gates |
| Intuitive / undergraduate docs | In progress |
| manim visualizations | One scene present |

## Quick Start

```powershell
# Set up environment
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt

# Smoke test the experimental framework (fast, no heavy deps)
python -m experiments._shared.smoke_test

# Run the scaling/criticality classifier (fast)
python -m experiments.scaling_criticality.criticality_table

# Run the Burgers shock experiment (fast)
python -m experiments.burgers_shock.burgers_blowup

# Run a coarse Taylor-Green DNS (a minute or two at 32^3)
python -m experiments.taylor_green.taylor_green_dns
```
