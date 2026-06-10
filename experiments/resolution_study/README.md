# Resolution study: the BKM integral under grid refinement

Experiment (e). The viscosity control run dynamically, and the first of the two "next" compute items in [`../PLAN.md`](../PLAN.md).

## The question

Beale-Kato-Majda makes blow-up at time $T$ equivalent to

$$\int_0^T \|\omega(t)\|_{L^\infty}\,dt = \infty.$$

On any finite grid that integral is finite, so a single DNS can never speak to blow-up. The only meaningful numerical statement is about behavior **under refinement**: run the same flow on grids $16^3, 24^3, 32^3, \dots$ and watch whether the BKM integral converges or keeps growing with resolution.

- **Converges**: the vorticity dynamics is resolved; the flow is (as far as numerics can say) smooth at these parameters. This is the expected verdict at laptop Reynolds numbers and it calibrates the instrument.
- **Grows with resolution**: the signature of a candidate singularity. Nothing at these parameters should produce it; if a future near-singular scenario (e.g. an axisymmetric Hou-Luo-type setup) does, that is the flag worth chasing.

## What else is tracked

Along each run we record the scaling-critical norms $\|u\|_{L^3}$ and $\|u\|_{\dot H^{1/2}}$ (exponent 0 in the criticality bookkeeper). Escauriaza-Seregin-Sverak says blow-up requires the $L^3$ norm to become unbounded, so watching the critical norms stay bounded while the supercritical energy decays ties the bookkeeper's static arithmetic to the actual dynamics: the quantities that would have to explode are exactly the ones the energy bound does not control.

## Run

```powershell
python -m experiments.resolution_study.bkm_refinement
# wider sweep (slower):
$env:NS_RES_NS = "16,24,32,48"; python -m experiments.resolution_study.bkm_refinement
```

Defaults: Taylor-Green initial data, $\nu \in \{0.025, 0.01\}$, grids $\{16^3, 24^3, 32^3\}$, $t \in [0, 3]$, time step shrinking with the grid (advective CFL). Runs in a few minutes.

## Result (2026-06-09 run)

At both viscosities the BKM integral converges under refinement, the critical norms stay bounded, and the energy decays. Verdict: CONVERGED, the smooth-regime calibration.

| $\nu$ | BKM ($16^3$) | BKM ($24^3$) | BKM ($32^3$) | last change | max $\|u\|_{L^3}$ | max $\|u\|_{\dot H^{1/2}}$ |
|---|---|---|---|---|---|---|
| 0.025 | 4.379 | 4.414 | 4.432 | 0.39% | 3.445 | 10.364 |
| 0.01 | 5.170 | 5.135 | 5.148 | 0.25% | 3.445 | 10.595 |

## Honest caveats

- Convergence at $\mathrm{Re}\sim 40$ to $100$ says nothing about the supercritical regime; it is calibration, not evidence for global regularity.
- The solver has no dealiasing; at the highest Reynolds number on the coarsest grid the under-resolution is the very thing the refinement comparison is designed to expose.
