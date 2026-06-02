/-
The global regularity goal.

This module states the Clay Millennium target itself: for the 3D incompressible
Navier-Stokes equations with viscosity ν > 0, every smooth divergence-free
finite-energy initial datum gives rise to a global-in-time smooth solution.

It also records the two acceptable Clay outcomes (regularity OR blow-up) and the
disciplined relationship to the controls: a proof must use the 3D vortex-
stretching structure (so it does NOT apply in 2D, where regularity is already
known) and must use viscosity (the inviscid relatives blow up).

Status: skeleton. This is the apex `sorry`: the whole program aims at proving
(or disproving) `GlobalRegularity`. Documented as the top VERIFIER target.
-/

import NavierStokes.DivergenceFree
import NavierStokes.EnergyInequality
import NavierStokes.BealeKatoMajda

namespace NavierStokes

/-- Smooth, divergence-free, finite-energy initial data (the admissible class in
    Fefferman's statement).

    VERIFIER target #GR-1: replace by the genuine smoothness + decay + finite
    energy conditions once the regularity classes are available. -/
def AdmissibleInitialData (u₀ : VelocityField) : Prop :=
  IsDivergenceFree u₀ ∧ (∃ E : ℝ, kineticEnergy u₀ ≤ E)

/-- A time-dependent field is a global smooth solution of NS with viscosity ν
    and initial datum u₀.

    VERIFIER target #GR-2: requires the formalized equation and the global (all
    `t ≥ 0`) smoothness. Currently a typed placeholder using the BKM-style
    smooth-solution predicate at every horizon. -/
def IsGlobalSmoothSolution (u : TimeVelocity) (ν : ℝ) (u₀ : VelocityField) : Prop :=
  u 0 = u₀ ∧ ∀ T : ℝ, 0 < T → IsSmoothSolutionOn u ν T

/-- THE GOAL. Global existence and smoothness: for every viscosity ν > 0 and
    every admissible initial datum, a global smooth solution exists.

    This is the Clay Millennium statement (existence-and-smoothness form, (A)/(B)
    in Fefferman). VERIFIER target #GR-3 (the apex): prove it, or prove its
    negation via an explicit blow-up (target #GR-4). Everything else in the
    project is a sub-target of this. -/
def GlobalRegularity : Prop :=
  ∀ (ν : ℝ) (u₀ : VelocityField), 0 < ν → AdmissibleInitialData u₀ →
    ∃ u : TimeVelocity, IsGlobalSmoothSolution u ν u₀

/-- The blow-up alternative (the other acceptable Clay outcome): there exist a
    viscosity and admissible data with no global smooth solution.

    VERIFIER target #GR-4: the disproof side. The two outcomes
    `GlobalRegularity` and `FiniteTimeBlowup` are exclusive; proving either wins
    the prize. -/
def FiniteTimeBlowup : Prop :=
  ∃ (ν : ℝ) (u₀ : VelocityField), 0 < ν ∧ AdmissibleInitialData u₀ ∧
    ¬ ∃ u : TimeVelocity, IsGlobalSmoothSolution u ν u₀

/-- The Clay dichotomy is genuinely a dichotomy in the unforced setting:
    exactly one of global regularity / blow-up holds for the family.

    VERIFIER target #GR-5: `GlobalRegularity ↔ ¬ FiniteTimeBlowup`. With the
    definitions above this is a logical manipulation (a `∀ ... ∃` versus its
    negation), so it should be provable once the placeholders are real; recorded
    here as the structural target. -/
theorem regularity_iff_not_blowup :
    GlobalRegularity ↔ ¬ FiniteTimeBlowup := by
  sorry

end NavierStokes
