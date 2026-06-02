"""The criticality bookkeeper: a wrong-approach detector for Navier-Stokes.

This is the project's structural CONTROL, the analog of the Davenport-Heilbronn
L-function in the companion analysis repo. It encodes the single most important
fact about the regularity problem: under the Navier-Stokes scaling symmetry

    u_lambda(x, t) = lambda * u(lambda x, lambda^2 t),
    p_lambda(x, t) = lambda^2 * p(lambda x, lambda^2 t),

a given norm of u scales like lambda raised to some exponent. A norm is

    SUBcritical   if it grows as lambda -> infinity (exponent > 0): it dominates
                  small scales, so bounding it controls singularity formation;
    CRITICAL      if it is scale invariant (exponent = 0): it lives exactly at
                  the level a singularity would form;
    SUPERcritical if it decays as lambda -> infinity (exponent < 0): it gives no
                  control at small scales, where a singularity would form.

WHY this is the control: the only a priori bound that holds for all time in 3D
is the energy inequality, which controls the L^2 norm of u (and the L^2-in-time
norm of grad u). The L^2 norm of u in three dimensions is SUPERCRITICAL. So
energy bounds alone cannot reach a regularity statement, which is a critical-or-
subcritical statement. Any proposed a priori estimate whose controlling norm is
supercritical is, by this bookkeeping, insufficient by itself. The bookkeeper
flags exactly that.

The scaling exponent of the homogeneous norm ||u||_X for X = dot{H}^s, L^q,
Lebesgue-in-time-and-space, or a vorticity norm, in spatial dimension d, is a
short algebraic computation. We implement it for the norms named in the problem
spec and expose a classifier that any candidate-estimate audit can call.

Convention used throughout: we report the exponent a such that

    ||u_lambda||_X = lambda^a * ||u||_X      (purely spatial norms, fixed t),

so a > 0 means SUBcritical (grows at small scales), a = 0 CRITICAL, a < 0
SUPERcritical. This is the convention in which "scale invariant <=> critical"
reads off directly as a = 0. (Some texts flip the sign of the rescaling
variable; the classification sub/critical/super is convention independent and
is what matters.)
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction


# Classification labels, ordered from "controls singularities" to "does not".
SUBCRITICAL = "subcritical"
CRITICAL = "critical"
SUPERCRITICAL = "supercritical"


def classify_exponent(a) -> str:
    """Map a scaling exponent a to a sub/critical/super label.

    a > 0  -> subcritical (the norm grows at small scales; it controls them).
    a == 0 -> critical (scale invariant).
    a < 0  -> supercritical (no control at small scales).
    """
    a = Fraction(a)
    if a > 0:
        return SUBCRITICAL
    if a == 0:
        return CRITICAL
    return SUPERCRITICAL


def homogeneous_sobolev_exponent(s, d: int = 3) -> Fraction:
    """Scaling exponent of the homogeneous Sobolev seminorm ||u||_{dot H^s}.

    For v_lambda(x) = lambda * u(lambda x) (the velocity rescaling, fixed time),
    a direct change of variables gives, in dimension d,

        ||v_lambda||_{dot H^s} = lambda^{1 + s - d/2} ||u||_{dot H^s}.

    So the exponent is a = 1 + s - d/2. For d = 3 this is s - 1/2, which
    vanishes at the critical regularity s = 1/2 (the Fujita-Kato space).
    """
    return Fraction(1) + Fraction(s) - Fraction(d, 2)


def lebesgue_exponent(q, d: int = 3) -> Fraction:
    """Scaling exponent of the spatial Lebesgue norm ||u||_{L^q}.

    For v_lambda(x) = lambda * u(lambda x),

        ||v_lambda||_{L^q} = lambda^{1 - d/q} ||u||_{L^q}.

    Exponent a = 1 - d/q. For d = 3 this vanishes at q = 3 (the
    Escauriaza-Seregin-Sverak endpoint). q = 2 (energy) gives a = -1/2 < 0,
    so the energy norm is SUPERcritical in 3D.
    """
    return Fraction(1) - Fraction(d, q)


def bmo_inverse_exponent(d: int = 3) -> Fraction:
    """Scaling exponent of the BMO^{-1} norm (Koch-Tataru critical space).

    BMO^{-1} = dot{B}^{-1}_{infinity, infinity}-flavored space scales exactly
    like dot H^{d/2 - 1}, i.e. it is scale invariant: a = 0. We return 0
    directly rather than reconstructing it, because the defining property of
    the Koch-Tataru space is precisely its scale invariance.
    """
    return Fraction(0)


def vorticity_Linfty_time_integral_exponent(d: int = 3) -> Fraction:
    """Scaling exponent of the Beale-Kato-Majda control integral_0^T ||omega||_{L^infinity} dt.

    The vorticity omega = curl u rescales as omega_lambda(x, t) =
    lambda^2 omega(lambda x, lambda^2 t). The spatial sup norm picks up
    lambda^2; integrating in time over a rescaled interval (dt -> lambda^2 dt,
    i.e. the integral is over t in [0, lambda^2 T]) contributes lambda^{-2}.
    Net exponent 0: the BKM quantity is exactly CRITICAL (scale invariant).
    This is independent of dimension (curl and the time integral conspire),
    and it is why BKM is the sharp regularity criterion.
    """
    return Fraction(0)


@dataclass(frozen=True)
class NormSpec:
    """A named norm together with how to compute its NS scaling exponent."""

    name: str
    description: str
    exponent: Fraction

    @property
    def classification(self) -> str:
        return classify_exponent(self.exponent)


def standard_norms_3d() -> list[NormSpec]:
    """The norms named in the problem spec, with their 3D scaling exponents.

    These are the quantities a Navier-Stokes regularity argument typically
    tries to control. The point of the table is the column of classifications:
    energy is supercritical, the named regularity criteria sit at critical.
    """
    d = 3
    return [
        NormSpec(
            "energy L^2 (||u||_2)",
            "the energy norm; the only all-time a priori bound (energy inequality)",
            lebesgue_exponent(2, d),
        ),
        NormSpec(
            "H^1 (||u||_{dot H^1}, enstrophy^{1/2})",
            "one derivative; controls enstrophy; not an all-time bound in 3D",
            homogeneous_sobolev_exponent(1, d),
        ),
        NormSpec(
            "H^{1/2} (Fujita-Kato critical Sobolev)",
            "the critical Sobolev space; small data here gives global smooth solutions",
            homogeneous_sobolev_exponent(Fraction(1, 2), d),
        ),
        NormSpec(
            "L^3 (Escauriaza-Seregin-Sverak endpoint)",
            "the borderline Lebesgue regularity space; ESS 2003 is the L^infty_t L^3_x endpoint",
            lebesgue_exponent(3, d),
        ),
        NormSpec(
            "BMO^{-1} (Koch-Tataru critical space)",
            "the largest known critical space for small-data global existence",
            bmo_inverse_exponent(d),
        ),
        NormSpec(
            "vorticity L^infinity in time (BKM integral)",
            "integral_0^T ||omega(t)||_{L^infinity} dt; finite <=> no blow-up (Beale-Kato-Majda)",
            vorticity_Linfty_time_integral_exponent(d),
        ),
    ]


def audit_estimate(controlling_norm: NormSpec) -> dict:
    """Audit a proposed a priori estimate by the norm it controls.

    Returns a verdict dict. A supercritical controlling norm is flagged as
    INSUFFICIENT-BY-ITSELF: it cannot, on its own, close a regularity statement,
    because regularity is a critical-or-subcritical statement. This is the
    wrong-approach detector firing.
    """
    cls = controlling_norm.classification
    if cls == SUPERCRITICAL:
        verdict = "INSUFFICIENT_BY_ITSELF"
        reason = (
            "controlling norm is supercritical: it gives no control at the small "
            "scales where a singularity would form, so it cannot close regularity "
            "alone. New genuinely critical control is required."
        )
    elif cls == CRITICAL:
        verdict = "AT_THE_MARGIN"
        reason = (
            "controlling norm is critical (scale invariant): bounding it would "
            "close regularity, but no all-time a priori bound at this level is "
            "known. This is exactly the gap."
        )
    else:
        verdict = "WOULD_CLOSE_IF_AVAILABLE"
        reason = (
            "controlling norm is subcritical: a global a priori bound here would "
            "close regularity outright. No such bound is known in 3D."
        )
    return {
        "norm": controlling_norm.name,
        "exponent": str(controlling_norm.exponent),
        "classification": cls,
        "verdict": verdict,
        "reason": reason,
    }
