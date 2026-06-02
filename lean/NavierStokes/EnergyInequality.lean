/-
The energy inequality.

The one a priori bound that holds for all time, for any Leray-Hopf weak solution:

    (1/2) ‖u(t)‖_{L²}² + ν ∫₀ᵗ ‖∇u(s)‖_{L²}² ds ≤ (1/2) ‖u₀‖_{L²}².

The kinetic energy never increases, and the total viscous dissipation is bounded
by the initial energy. This is the coercive bound that gives existence (Leray
1934) and the bound the whole repo identifies as SUPERCRITICAL: the norm it
controls (L² of u) is at scaling exponent -1/2 in 3D, so it cannot reach a
regularity statement.

Status: skeleton. Mathlib lacks vector-valued Sobolev spaces and the Bochner
integral setup needed to state this faithfully, so the energy functional and the
inequality are typed placeholders with documented `sorry`s. The numerical face
of the inequality (energy monotonically decreasing) is exercised in the
Taylor-Green DNS smoke test, `experiments/_shared/smoke_test.py` Test 4.
-/

import NavierStokes.DivergenceFree
import Mathlib.MeasureTheory.Integral.Bochner

namespace NavierStokes

/-- The kinetic energy `E(u) = (1/2) ∫ |u|² dx` of a velocity field.

    VERIFIER target #EI-1: define via the Bochner / Lebesgue integral of the
    pointwise squared norm. Needs the integrability class on `VelocityField`
    pinned (finite energy). Currently a placeholder via `sorry`. -/
noncomputable def kineticEnergy (u : VelocityField) : ℝ :=
  sorry

/-- The enstrophy-type dissipation `D(u) = ∫ |∇u|² dx`.

    VERIFIER target #EI-2: define via the integral of the squared
    Hilbert-Schmidt norm of the derivative `fderiv ℝ u`. -/
noncomputable def dissipation (u : VelocityField) : ℝ :=
  sorry

/-- A time-dependent velocity, `u : time → field`. -/
abbrev TimeVelocity : Type := ℝ → VelocityField

/-- The energy inequality, stated for a (putative) Leray-Hopf solution `u` with
    viscosity `ν > 0`:

      kineticEnergy (u t) + ν · ∫₀ᵗ dissipation (u s) ds ≤ kineticEnergy (u 0).

    VERIFIER target #EI-3: this is the defining a priori bound of a Leray-Hopf
    weak solution. Stating it faithfully needs #EI-1, #EI-2, and the integral in
    time. The hypothesis `IsLerayHopf u ν` (a future definition) would carry it;
    here it is recorded as the goal a solution must satisfy. -/
def SatisfiesEnergyInequality (u : TimeVelocity) (ν : ℝ) : Prop :=
  ∀ t : ℝ, 0 ≤ t →
    kineticEnergy (u t) + ν * (∫ s in Set.Icc (0:ℝ) t, dissipation (u s)) ≤ kineticEnergy (u 0)

/-- The energy inequality is monotone in time: energy at a later time is bounded
    by energy at an earlier time (a consequence of `SatisfiesEnergyInequality`
    when ν ≥ 0 and the dissipation is nonnegative).

    VERIFIER target #EI-4: prove from `SatisfiesEnergyInequality` plus
    `0 ≤ dissipation`. The argument is monotonicity of the time integral; it is
    reachable once #EI-1/#EI-2 give the nonnegativity. -/
theorem energy_monotone
    (u : TimeVelocity) (ν : ℝ) (hν : 0 ≤ ν)
    (h : SatisfiesEnergyInequality u ν)
    (hdis : ∀ s, 0 ≤ dissipation (u s)) :
    ∀ t, 0 ≤ t → kineticEnergy (u t) ≤ kineticEnergy (u 0) := by
  sorry

end NavierStokes
