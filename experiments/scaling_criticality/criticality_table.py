"""Experiment (d): the scaling / criticality classification table.

Programmatically classifies a list of norms (energy L^2, H^1, L^3, BMO^{-1},
H^{1/2}, vorticity L^infinity in time) as sub/critical/super under the
Navier-Stokes scaling, and prints the table together with the audit verdict for
each.

WHY this is the headline control: regularity of the 3D flow is a critical-
scaling statement, and the only all-time a priori bound (the energy) is
supercritical. The table is the coordinate system of the whole problem. The
verdict column shows the wrong-approach detector firing on the energy norm:
energy methods, by themselves, cannot close regularity, because the norm they
control gives no information at the small scales where a singularity forms.

This experiment is pure bookkeeping (no PDE solve), so it runs instantly and is
deterministic. It uses the shared criticality module, the same CONTROL the
smoke test exercises.
"""

from __future__ import annotations

from experiments._shared import standard_norms_3d, audit_estimate


def print_table():
    norms = standard_norms_3d()
    name_w = max(len(n.name) for n in norms) + 2
    print("Navier-Stokes scaling classification on R^3 / T^3")
    print("scaling: u_lambda(x,t) = lambda * u(lambda x, lambda^2 t)")
    print("exponent a: ||u_lambda||_X = lambda^a ||u||_X  (a>0 sub, a=0 critical, a<0 super)")
    print()
    header = f"{'norm':<{name_w}} {'exponent':>10} {'class':>14}   verdict"
    print(header)
    print("-" * (len(header) + 8))
    for n in norms:
        verdict = audit_estimate(n)
        print(
            f"{n.name:<{name_w}} {str(n.exponent):>10} {n.classification:>14}   {verdict['verdict']}"
        )
    print()
    print("Reading of the table:")
    print("  - energy L^2 is SUPERCRITICAL: the one all-time a priori bound gives no")
    print("    small-scale control. This is the supercriticality gap.")
    print("  - H^1 (enstrophy) is SUBcritical: a global bound here would close")
    print("    regularity, but none is known in 3D (in 2D the enstrophy IS bounded).")
    print("  - H^{1/2}, L^3, BMO^{-1} are CRITICAL: small data here gives global smooth")
    print("    solutions (Fujita-Kato, ESS endpoint, Koch-Tataru); large data is open.")
    print("  - the BKM vorticity integral is CRITICAL and is the sharp blow-up criterion.")


def main():
    print_table()
    print()
    print("CONTROL note: any proposed a priori estimate whose controlling norm is")
    print("supercritical is INSUFFICIENT_BY_ITSELF. A regularity proof must add")
    print("genuinely critical control that uses 3D vortex stretching (absent in 2D).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
