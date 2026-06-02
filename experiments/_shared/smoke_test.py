"""Phase 0 smoke test: does the shared infrastructure work?

Validates:
  1. The criticality bookkeeper classifies the standard 3D norms correctly
     (energy L^2 supercritical; H^{1/2}, L^3, BMO^{-1}, BKM critical; H^1 sub).
  2. The energy norm is flagged supercritical AND audited as
     INSUFFICIENT_BY_ITSELF (the wrong-approach detector fires).
  3. The Flow3D solver keeps a velocity field divergence-free after a step
     (the Leray projection works to near machine precision).
  4. The Flow3D solver dissipates energy on a Taylor-Green start (viscosity
     decreases the energy; this is the energy inequality holding numerically).
  5. The Flow2D control keeps enstrophy non-increasing on a random vorticity
     field (the structural 2D fact: no stretching => enstrophy decays).
"""

from __future__ import annotations

import numpy as np

from experiments._shared import (
    standard_norms_3d,
    audit_estimate,
    SUPERCRITICAL,
    CRITICAL,
    SUBCRITICAL,
    Flow3D,
    Flow2D,
    taylor_green_initial,
)


def check(label, ok, info=""):
    status = "PASS" if ok else "FAIL"
    print(f"  [{status}] {label}{(' - ' + info) if info else ''}")
    return ok


def test_criticality_classification():
    print("Test 1: criticality bookkeeper classifies the standard norms")
    norms = {n.name: n for n in standard_norms_3d()}
    expected = {
        "energy L^2 (||u||_2)": SUPERCRITICAL,
        "H^1 (||u||_{dot H^1}, enstrophy^{1/2})": SUBCRITICAL,
        "H^{1/2} (Fujita-Kato critical Sobolev)": CRITICAL,
        "L^3 (Escauriaza-Seregin-Sverak endpoint)": CRITICAL,
        "BMO^{-1} (Koch-Tataru critical space)": CRITICAL,
        "vorticity L^infinity in time (BKM integral)": CRITICAL,
    }
    ok_all = True
    for name, exp in expected.items():
        got = norms[name].classification
        ok_all = ok_all and check(
            f"{name} is {exp}", got == exp, f"got {got} (exponent {norms[name].exponent})"
        )
    return ok_all


def test_energy_supercritical_audit():
    print("Test 2: the energy estimate is flagged INSUFFICIENT_BY_ITSELF")
    energy = next(n for n in standard_norms_3d() if n.name.startswith("energy"))
    verdict = audit_estimate(energy)
    ok = verdict["classification"] == SUPERCRITICAL and verdict["verdict"] == "INSUFFICIENT_BY_ITSELF"
    return check("energy audit fires the wrong-approach detector", ok, verdict["verdict"])


def test_flow3d_divergence_free():
    print("Test 3: Flow3D keeps the field divergence-free after a step")
    f = Flow3D(n=16, nu=0.05)
    f.set_velocity(taylor_green_initial(16))
    f.step(0.01)
    div = f.divergence_Linfty()
    return check("max |div u| is near machine precision", div < 1e-9, f"max|div u|={div:.2e}")


def test_flow3d_energy_dissipates():
    print("Test 4: Flow3D dissipates energy (energy inequality, numerically)")
    f = Flow3D(n=16, nu=0.05)
    f.set_velocity(taylor_green_initial(16))
    e0 = f.energy()
    for _ in range(10):
        f.step(0.01)
    e1 = f.energy()
    return check("energy decreased under viscosity", e1 < e0, f"E0={e0:.5f} -> E1={e1:.5f}")


def test_flow2d_enstrophy_nonincreasing():
    print("Test 5: Flow2D (control) keeps enstrophy non-increasing")
    rng = np.random.default_rng(0)
    n = 32
    w0 = rng.standard_normal((n, n))
    # remove mean so the field is a genuine vorticity (zero circulation)
    w0 -= w0.mean()
    f = Flow2D(n=n, nu=0.02)
    f.set_vorticity(w0)
    z0 = f.enstrophy()
    for _ in range(20):
        f.step(0.005)
    z1 = f.enstrophy()
    # allow a tiny numerical tolerance
    return check(
        "enstrophy non-increasing (no vortex stretching in 2D)",
        z1 <= z0 * (1 + 1e-8),
        f"Z0={z0:.5f} -> Z1={z1:.5f}",
    )


def main():
    results = [
        test_criticality_classification(),
        test_energy_supercritical_audit(),
        test_flow3d_divergence_free(),
        test_flow3d_energy_dissipates(),
        test_flow2d_enstrophy_nonincreasing(),
    ]
    print()
    n_pass = sum(results)
    print(f"Smoke test: {n_pass}/{len(results)} passed")
    return 0 if n_pass == len(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
