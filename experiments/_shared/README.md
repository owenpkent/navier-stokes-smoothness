# Shared experiment infrastructure

Phase 0 of the [experimental plan](../PLAN.md). Provides the computational substrate so every architecture (energy methods, conditional criteria, critical spaces, blow-up, the controls) can be exercised with shared, audited code.

## Modules

| File | Purpose |
|---|---|
| [`criticality.py`](criticality.py) | The **criticality bookkeeper**, the project's wrong-approach CONTROL. Classifies any norm as sub/critical/super under the NS scaling $u_\lambda(x,t)=\lambda u(\lambda x,\lambda^2 t)$, and audits a proposed a priori estimate by the norm it controls. A supercritical controlling norm is flagged INSUFFICIENT_BY_ITSELF. |
| [`flow.py`](flow.py) | Pseudo-spectral solvers. `Flow3D`: 3D incompressible Navier-Stokes on $\mathbb{T}^3$ with an exact Leray projection and RK2 time stepping; reports energy, enstrophy, max vorticity. `Flow2D`: the 2D vorticity-form CONTROL (no vortex stretching, enstrophy non-increasing, globally smooth). `taylor_green_initial`: the canonical smooth divergence-free test datum. |
| [`smoke_test.py`](smoke_test.py) | Phase 0 regression suite: 5 tests covering the criticality classification, the energy audit firing, the Leray projection keeping $\nabla\cdot u\approx 0$, energy dissipation under viscosity, and the 2D enstrophy staying non-increasing. |

## The wrong-approach discipline

Three structural detectors guard the project. Any candidate method must pass all three.

1. **2D Navier-Stokes is globally smooth** (Ladyzhenskaya). `Flow2D` makes this concrete: in 2D the vorticity is a transported-and-diffused scalar with no stretching term, so the enstrophy is non-increasing. Any 3D method that would apply verbatim in 2D and predict 2D blow-up is wrong, because 2D does not blow up. **2D is the must-stay-smooth control.**
2. **Supercriticality is the structural ceiling.** The energy is the only all-time a priori bound, and in 3D the $L^2$ velocity norm is supercritical (scaling exponent $-1/2$). The criticality bookkeeper audits any proposed estimate and fires INSUFFICIENT_BY_ITSELF on supercritical controlling norms. This is the analog of a saturated exponent: energy methods alone cannot reach a critical regularity statement.
3. **Viscosity is essential.** Inviscid Burgers shocks in finite time; 3D Euler blows up (Elgindi). See [`../burgers_shock/`](../burgers_shock/). A method blind to the viscous term $\nu\Delta u$ is suspect, because the inviscid relatives are singular.

Architecture 5 (convex integration) sits partly outside this discipline: it is about non-smooth, non-unique weak solutions below the energy class, i.e. the boundary of what "solution" means, not the regularity of the smooth flow.

## Smoke test

Run it from the repo root:

```
python -m experiments._shared.smoke_test
```

All 5 tests should pass. It is fast (a few seconds) and uses only `numpy`.

## Conventions

- Periodic torus $\mathbb{T}^d = [0, 2\pi)^d$, Fourier collocation via `numpy.fft`.
- 3D state is the velocity in Fourier space; incompressibility is the exact algebraic Leray projection on each wavenumber.
- Diagnostics: energy $\tfrac12\langle|u|^2\rangle$, enstrophy $\tfrac12\langle|\omega|^2\rangle$, max vorticity $\|\omega\|_\infty$, and the running Beale-Kato-Majda integral $\int_0^t\|\omega\|_\infty\,ds$.
- Grids are deliberately small (16^3 in the smoke test, 32^3 in the DNS) so everything runs on a laptop. These are a control substrate, not research-resolution DNS.
