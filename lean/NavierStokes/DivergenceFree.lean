/-
Divergence-free vector fields on the torus / R^3.

This module sets up the basic objects of the incompressible Navier-Stokes
problem: a (time-dependent) velocity field and the incompressibility constraint
div u = 0.

Status: skeleton. Mathlib (as of v4.13.0) has the differential-geometry and
vector-calculus pieces (`fderiv`, divergence via traces of the derivative) but
lacks a packaged "Sobolev space of divergence-free vector fields" and the Leray
decomposition. The definitions here are typed placeholders with documented
`sorry`s marking the VERIFIER targets. The skeleton is NOT expected to build
until the Mathlib analysis infrastructure (Bochner integral on vector-valued
Sobolev spaces, Helmholtz-Leray decomposition) is in place.
-/

import Mathlib.Analysis.Calculus.FDeriv.Basic
import Mathlib.Analysis.InnerProductSpace.Basic
import Mathlib.Topology.MetricSpace.Basic

namespace NavierStokes

open scoped BigOperators

/-- A velocity field on R^3 (we model space as `Fin 3 → ℝ` and the velocity as a
    map into `Fin 3 → ℝ`). Time dependence is carried by an extra `ℝ` argument
    where needed. This is the simplest faithful model; a research-grade version
    would use the torus `(ℝ / 2π ℤ)^3` and a Sobolev regularity class. -/
abbrev VelocityField : Type := (Fin 3 → ℝ) → (Fin 3 → ℝ)

/-- The divergence of a (sufficiently differentiable) velocity field at a point,
    `div u (x) = ∑ i, ∂_i u_i (x)`.

    VERIFIER target #DF-1: replace this with the genuine sum of partial
    derivatives once the differentiability class is fixed (it currently returns
    a placeholder via `sorry`; Mathlib has `fderiv` but we have not pinned the
    differentiability hypotheses on `VelocityField`). -/
noncomputable def divergence (u : VelocityField) (x : Fin 3 → ℝ) : ℝ :=
  -- ∑ i, (partial derivative of the i-th component in the i-th direction) at x
  sorry

/-- The incompressibility (divergence-free) predicate: `div u = 0` everywhere. -/
def IsDivergenceFree (u : VelocityField) : Prop :=
  ∀ x, divergence u x = 0

/-- A trivial witness: the zero field is divergence-free. This is the one fact
    we can record without the differentiation infrastructure; it documents the
    intended meaning of `IsDivergenceFree`.

    VERIFIER target #DF-2: once `divergence` is real, prove `divergence 0 = 0`
    properly instead of by `sorry`. -/
theorem zero_isDivergenceFree : IsDivergenceFree (fun _ => 0) := by
  intro x
  -- needs `divergence` to compute to 0 on the zero field
  sorry

end NavierStokes
