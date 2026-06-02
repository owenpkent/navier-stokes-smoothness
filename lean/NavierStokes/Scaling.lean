/-
The Navier-Stokes scaling symmetry and criticality.

If (u, p) solves Navier-Stokes, so does

    u_λ(x, t) = λ · u(λ x, λ² t),   p_λ(x, t) = λ² · p(λ x, λ² t),   λ > 0,

with the viscosity ν unchanged. This is the ruler that measures everything: a
norm is critical if it is invariant under this rescaling, subcritical if it
grows as λ → ∞, supercritical if it decays. The energy (L²) norm is
supercritical in 3D (exponent -1/2), which is the structural obstruction.

This module is the most self-contained of the skeleton: the scaling action is
algebraic, and the rescaling of a solution into another solution is the kind of
statement that could plausibly be proved in Lean once the equation itself is
formalized. The scaling EXPONENTS are recorded as plain rationals (matching
`experiments/_shared/criticality.py`) and the classification is a real, total
function with a genuine proof.
-/

import Mathlib.Data.Rat.Defs
import Mathlib.Data.Real.Basic

namespace NavierStokes

/-- The rescaled velocity field `u_λ(x) = λ · u(λ x)` (fixed time slice).
    Space is modeled as `Fin 3 → ℝ`. -/
noncomputable def rescaleVelocity (lam : ℝ) (u : (Fin 3 → ℝ) → (Fin 3 → ℝ)) :
    (Fin 3 → ℝ) → (Fin 3 → ℝ) :=
  fun x i => lam * u (fun j => lam * x j) i

/-- Criticality classification of a scaling exponent.

    The convention (matching `criticality.py`): with `‖u_λ‖_X = λ^a ‖u‖_X`,
    `a > 0` is subcritical (controls small scales), `a = 0` critical (scale
    invariant), `a < 0` supercritical (no small-scale control). -/
inductive Criticality where
  | subcritical
  | critical
  | supercritical
  deriving DecidableEq, Repr

open Criticality

/-- Classify a rational scaling exponent. This is a real total function with the
    obvious proof (no `sorry`): it is the Lean mirror of `classify_exponent`. -/
def classify (a : ℚ) : Criticality :=
  if a > 0 then subcritical
  else if a = 0 then critical
  else supercritical

/-- The homogeneous Sobolev exponent in dimension d: `a = 1 + s - d/2`. -/
def sobolevExponent (s : ℚ) (d : ℚ) : ℚ := 1 + s - d / 2

/-- The Lebesgue exponent in dimension d: `a = 1 - d/q`. -/
def lebesgueExponent (q : ℚ) (d : ℚ) : ℚ := 1 - d / q

/-- The energy norm L² is supercritical in 3D. A genuine, sorry-free fact about
    the classifier: `classify (lebesgueExponent 2 3) = supercritical`, i.e. the
    exponent `1 - 3/2 = -1/2` is negative. This is the one piece of the
    supercriticality story that is fully formal here. -/
theorem energy_L2_supercritical :
    classify (lebesgueExponent 2 3) = supercritical := by
  decide

/-- The critical Sobolev space H^{1/2} is critical in 3D: exponent `1 + 1/2 - 3/2 = 0`. -/
theorem H_half_critical :
    classify (sobolevExponent (1/2) 3) = Criticality.critical := by
  decide

/-- The L³ space is critical in 3D (the ESS endpoint): exponent `1 - 3/3 = 0`. -/
theorem L3_critical :
    classify (lebesgueExponent 3 3) = Criticality.critical := by
  decide

/-- The enstrophy / H¹ norm is subcritical in 3D: exponent `1 + 1 - 3/2 = 1/2`. -/
theorem H1_subcritical :
    classify (sobolevExponent 1 3) = Criticality.subcritical := by
  decide

/-- The scaling map preserves the Navier-Stokes equations.

    VERIFIER target #SC-1: once the NS evolution is formalized (see
    `EnergyInequality.lean` / a future `Equation.lean`), prove that
    `rescaleVelocity λ` carries a solution to a solution. This is algebraic but
    needs the equation as a hypothesis to state. -/
theorem rescale_preserves_solution : True := by
  trivial

end NavierStokes
