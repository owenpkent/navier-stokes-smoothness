/-
The Beale-Kato-Majda criterion.

A smooth solution on [0, T) can be continued past T if and only if the time
integral of the sup-norm of the vorticity is finite:

    ∫₀ᵀ ‖ω(t)‖_{L^∞} dt < ∞.

This is the sharp blow-up criterion. The integrand ‖ω‖_{L^∞} scales like λ², the
time integral over the rescaled interval contributes λ^{-2}, so the BKM quantity
is scale invariant (critical), as `experiments/_shared/criticality.py` records.
The energy is supercritical and cannot bound it, which is the gap.

Status: skeleton. Needs the vorticity (curl), the L^∞ norm, the time integral,
and the notion of "smooth solution on [0,T)". Documented `sorry`s mark the
VERIFIER targets. The BKM integral is tracked numerically in the Taylor-Green
DNS, `experiments/taylor_green/taylor_green_dns.py`.
-/

import NavierStokes.DivergenceFree
import NavierStokes.EnergyInequality

namespace NavierStokes

/-- The vorticity `ω = curl u` of a velocity field.

    VERIFIER target #BKM-1: define `curl` from `fderiv` (the antisymmetric part
    of the derivative). Mathlib has the pieces but not a packaged `curl` in 3D. -/
noncomputable def vorticity (u : VelocityField) : VelocityField :=
  sorry

/-- The spatial sup-norm of the vorticity at a fixed time, `‖ω‖_{L^∞}`.

    VERIFIER target #BKM-2: the essential supremum of `|vorticity u x|` over `x`. -/
noncomputable def vorticitySupNorm (u : VelocityField) : ℝ :=
  sorry

/-- The Beale-Kato-Majda integral up to time T: `∫₀ᵀ ‖ω(t)‖_{L^∞} dt`. -/
noncomputable def bkmIntegral (u : TimeVelocity) (T : ℝ) : ℝ :=
  ∫ t in Set.Icc (0:ℝ) T, vorticitySupNorm (u t)

/-- The predicate that a time-dependent field is a smooth solution on `[0, T)`.

    VERIFIER target #BKM-3: replace by the genuine "smooth (C^∞ in space and
    time) Navier-Stokes solution on the half-open interval" once the equation is
    formalized. Currently a typed placeholder. -/
def IsSmoothSolutionOn (u : TimeVelocity) (ν T : ℝ) : Prop :=
  True

/-- The Beale-Kato-Majda continuation criterion: a smooth solution on `[0, T)`
    extends to a smooth solution past `T` if and only if the BKM integral is
    finite on `[0, T]`.

    Here finiteness is modeled, in this skeleton, by the existence of a real
    bound `M` on the BKM integral (a faithful version would integrate the
    `L^∞` norm in the extended nonnegative reals and ask for `< ⊤`).

    VERIFIER target #BKM-4: THE central conditional-regularity statement. This
    is far beyond current Mathlib (it needs the log-Sobolev inequality, the
    higher-Sobolev energy estimates, and the local existence theory). Stated as
    a `sorry`-backed equivalence to record the target precisely. -/
theorem beale_kato_majda
    (u : TimeVelocity) (ν T : ℝ) (hν : 0 < ν)
    (h : IsSmoothSolutionOn u ν T) :
    (∃ M : ℝ, bkmIntegral u T ≤ M) ↔
      (∃ T' > T, IsSmoothSolutionOn u ν T') := by
  sorry

end NavierStokes
