"""Shared infrastructure for the Navier-Stokes proof-architecture experiments.

Provides the computational substrate used across the experimental thread:

  - The criticality bookkeeper (the wrong-approach CONTROL): classifies any norm
    as sub/critical/super under the Navier-Stokes scaling and audits proposed
    a priori estimates. See criticality.py.
  - The pseudo-spectral solvers Flow3D (Navier-Stokes on T^3) and Flow2D (the
    2D control, globally smooth). See flow.py.
"""

from .criticality import (
    SUBCRITICAL,
    CRITICAL,
    SUPERCRITICAL,
    NormSpec,
    classify_exponent,
    homogeneous_sobolev_exponent,
    lebesgue_exponent,
    bmo_inverse_exponent,
    vorticity_Linfty_time_integral_exponent,
    standard_norms_3d,
    audit_estimate,
)
from .flow import (
    Flow3D,
    Flow2D,
    Diagnostics3D,
    taylor_green_initial,
)

__all__ = [
    "SUBCRITICAL",
    "CRITICAL",
    "SUPERCRITICAL",
    "NormSpec",
    "classify_exponent",
    "homogeneous_sobolev_exponent",
    "lebesgue_exponent",
    "bmo_inverse_exponent",
    "vorticity_Linfty_time_integral_exponent",
    "standard_norms_3d",
    "audit_estimate",
    "Flow3D",
    "Flow2D",
    "Diagnostics3D",
    "taylor_green_initial",
]
