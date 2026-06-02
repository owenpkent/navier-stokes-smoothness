/-
The Leray projector.

The Leray projector P is the orthogonal projection (in L^2) of a vector field
onto its divergence-free part. It is the algebraic content of incompressibility:
applying P to the Navier-Stokes momentum equation eliminates the pressure,

    ∂_t u = P[ -(u·∇)u ] + ν Δ u.

On the torus, P acts mode by mode in Fourier space: it removes the component of
each Fourier coefficient û(k) along the wavevector k. That is exactly how the
pseudo-spectral solver in `experiments/_shared/flow.py` enforces div u = 0.

Status: skeleton. Mathlib has Hilbert-space orthogonal projections
(`orthogonalProjection`) but not the Helmholtz-Leray decomposition of vector
fields into gradient + divergence-free parts. The statements below are typed
placeholders with documented `sorry`s.
-/

import NavierStokes.DivergenceFree
import Mathlib.Analysis.InnerProductSpace.Projection

namespace NavierStokes

/-- The Leray projector, sending a velocity field to its divergence-free part.

    VERIFIER target #LP-1: define this as the orthogonal projection onto the
    closed subspace of divergence-free L^2 fields (the Helmholtz-Leray
    decomposition), which Mathlib does not yet have. Currently a placeholder
    (identity-like) via `sorry`. -/
noncomputable def lerayProjector (u : VelocityField) : VelocityField :=
  sorry

/-- The defining property: the Leray projection of any field is divergence-free.

    VERIFIER target #LP-2: prove once `lerayProjector` is the genuine
    projection. This is the algebraic heart of incompressibility. -/
theorem lerayProjector_isDivergenceFree (u : VelocityField) :
    IsDivergenceFree (lerayProjector u) := by
  sorry

/-- The Leray projector fixes divergence-free fields: `P u = u` when `div u = 0`.

    VERIFIER target #LP-3: a projection is the identity on its range. -/
theorem lerayProjector_eq_self_of_divergenceFree
    (u : VelocityField) (h : IsDivergenceFree u) :
    lerayProjector u = u := by
  sorry

/-- Idempotence: `P (P u) = P u`.

    VERIFIER target #LP-4: follows from #LP-1 / #LP-2 / #LP-3. -/
theorem lerayProjector_idempotent (u : VelocityField) :
    lerayProjector (lerayProjector u) = lerayProjector u := by
  exact lerayProjector_eq_self_of_divergenceFree _ (lerayProjector_isDivergenceFree u)

end NavierStokes
