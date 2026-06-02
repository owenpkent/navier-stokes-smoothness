# Lean 4 / Mathlib formalization of the Navier-Stokes regularity program

> Formal verification stack for the research program. Goal: every structural claim in the project (the scaling identity, the energy inequality, the Beale-Kato-Majda criterion, the global-regularity goal statement) is translated to Lean 4 and checked against Mathlib's kernel.

## Status

**Skeleton with documented `sorry`s. Not expected to build yet.** The project infrastructure (lakefile, toolchain) matches the companion analysis repo (Lean 4.13.0 + Mathlib v4.13.0). The modules state the right objects with typed signatures and carry documented `sorry`s marking the VERIFIER targets.

The honest caveat: Mathlib (as of v4.13.0) does NOT have the analysis infrastructure to make even the energy inequality clean. Missing pieces include vector-valued Sobolev spaces, the Helmholtz-Leray decomposition, a packaged 3D `curl`, and the Bochner-integral setup for vector fields. So a green build is a multi-step VERIFIER project, not a one-pass scaffold. The skeleton's job is to record the targets precisely.

Build command (once the infrastructure exists):

```powershell
cd lean
lake build
```

First-time setup needs `lake update` (downloads the prebuilt Mathlib oleans).

## What is real (sorry-free) in the skeleton

`Scaling.lean` carries genuine, sorry-free content: the `Criticality` classifier and the proofs that the standard 3D norms classify correctly (`energy_L2_supercritical`, `H_half_critical`, `L3_critical`, `H1_subcritical`), each by `decide`. These mirror `experiments/_shared/criticality.py` and make the supercriticality of the energy a machine-checked fact about the scaling exponents. `LerayProjector.lean` proves idempotence from the projection lemmas (modulo their own `sorry`s).

Everything else is a documented `sorry` (see the target table).

## Structure

```
lean/
├── lakefile.lean                    # Lake build configuration (Mathlib v4.13.0)
├── lean-toolchain                   # Lean version pin (v4.13.0)
├── NavierStokes.lean                # Main module: imports all sub-modules
└── NavierStokes/
    ├── DivergenceFree.lean          # divergence-free velocity fields, div u = 0
    ├── LerayProjector.lean          # the Leray projection onto divergence-free fields
    ├── Scaling.lean                 # the scaling symmetry + criticality classifier (sorry-free)
    ├── EnergyInequality.lean        # the energy inequality (the supercritical a priori bound)
    ├── BealeKatoMajda.lean          # the BKM blow-up criterion statement
    └── GlobalRegularity.lean        # the Clay goal: global existence + smoothness
```

## VERIFIER target IDs

Each `sorry` carries an ID for tracking.

| ID | Module | What it asks for |
|---|---|---|
| #DF-1 | DivergenceFree | Define `divergence` as the real sum of partial derivatives (needs differentiability class pinned). |
| #DF-2 | DivergenceFree | Prove the zero field is divergence-free once `divergence` is real. |
| #LP-1 | LerayProjector | Define `lerayProjector` as the orthogonal projection onto divergence-free L² fields (Helmholtz-Leray; Mathlib gap). |
| #LP-2 | LerayProjector | Prove `lerayProjector u` is divergence-free. |
| #LP-3 | LerayProjector | Prove the projector fixes divergence-free fields. |
| #LP-4 | LerayProjector | Idempotence (PROVED from #LP-2/#LP-3, modulo their sorries). |
| #SC-1 | Scaling | Prove the rescaling carries a solution to a solution (needs the equation formalized). |
| #EI-1 | EnergyInequality | Define `kineticEnergy` via the Bochner/Lebesgue integral of `|u|²`. |
| #EI-2 | EnergyInequality | Define `dissipation` via the integral of `|∇u|²`. |
| #EI-3 | EnergyInequality | State the energy inequality faithfully (the defining Leray-Hopf bound). |
| #EI-4 | EnergyInequality | Prove energy monotonicity from the inequality plus nonnegative dissipation. |
| #BKM-1 | BealeKatoMajda | Define the 3D `curl` (vorticity) from `fderiv`. |
| #BKM-2 | BealeKatoMajda | Define the vorticity `L^∞` norm (essential sup). |
| #BKM-3 | BealeKatoMajda | Define "smooth NS solution on [0, T)". |
| #BKM-4 | BealeKatoMajda | The BKM continuation criterion (the central conditional-regularity statement; far beyond current Mathlib). |
| #GR-1 | GlobalRegularity | The admissible-initial-data class (smooth, divergence-free, finite energy). |
| #GR-2 | GlobalRegularity | "Global smooth solution" predicate (needs the formalized equation). |
| #GR-3 | GlobalRegularity | THE APEX: prove `GlobalRegularity`. |
| #GR-4 | GlobalRegularity | The blow-up alternative (the disproof side). |
| #GR-5 | GlobalRegularity | `GlobalRegularity ↔ ¬ FiniteTimeBlowup` (a logical manipulation once placeholders are real). |

## Mathlib coverage gaps

As of v4.13.0, Mathlib does NOT have:
- Vector-valued (Bochner) Sobolev spaces of the kind needed for $u \in L^\infty_t L^2_x \cap L^2_t \dot H^1_x$.
- The Helmholtz-Leray decomposition / the Leray projector.
- A packaged 3D `curl` with the vector identities.
- The local existence theory and the log-Sobolev inequality behind BKM.

For these, VERIFIER agents either (1) propose a minimal Mathlib extension to contribute upstream, or (2) reduce the claim to existing Mathlib lemmas plus clearly-flagged axioms. The scaling and criticality content (`Scaling.lean`) is the part reachable today.

## How agents use this

- **BUILDER**: writes definitions in `NavierStokes/`.
- **VERIFIER**: picks a target ID, converts the `sorry` to a real proof or a precise Mathlib-gap report.
- **ADVERSARY**: attacks proposed theorems; checks they respect the controls (a "regularity" lemma that would also prove 2D blow-up is wrong).
- **SYNTHESIZER**: maintains this README and the target table.

## Cross-references

- [`../STATE_OF_THE_PROGRAM.md`](../STATE_OF_THE_PROGRAM.md): the strategic snapshot (Lean substrate section).
- [`../experiments/PLAN.md`](../experiments/PLAN.md): the experimental thread.
- [`../docs/02_graduate/scaling_and_supercriticality.md`](../docs/02_graduate/scaling_and_supercriticality.md): the math behind `Scaling.lean`.
