# Hou-Luo axisymmetric scenario at coarse resolution (Navier-Stokes with swirl)

Experiment (i). Architecture 4, the second "next" compute item in [`../PLAN.md`](../PLAN.md). Luo-Hou (PNAS 2014) found, numerically and at extreme resolution, a stable self-similar finite-time singularity candidate for axisymmetric **Euler** with swirl, anchored at a hyperbolic stagnation point on the solid wall $r = 1$; Chen-Hou (2022-2025) later proved the Euler blow-up rigorously. This experiment runs the **Navier-Stokes version** (finite $\nu > 0$) of that geometry at laptop resolution and applies the identical refinement diagnostic as [`../resolution_study/`](../resolution_study/): does the BKM integral converge under grid refinement, or grow with it? See the reading note [`../../docs/03_research/reading_notes/luo_hou_2014.md`](../../docs/03_research/reading_notes/luo_hou_2014.md) for the Euler-side story.

## Equations

Axisymmetric NS with swirl in the Hou-Li (2008) variables $u_1 = u^\theta/r$, $\omega_1 = \omega^\theta/r$, $\psi_1 = \psi/r$, all even in $r$ and smooth across the axis:

$$\partial_t u_1 + u^r \partial_r u_1 + u^z \partial_z u_1 = 2\,u_1\,\partial_z \psi_1 + \nu L u_1,$$
$$\partial_t \omega_1 + u^r \partial_r \omega_1 + u^z \partial_z \omega_1 = \partial_z(u_1^2) + \nu L \omega_1,$$
$$-L \psi_1 = \omega_1, \qquad u^r = -r\,\partial_z \psi_1, \qquad u^z = 2\psi_1 + r\,\partial_r \psi_1,$$

with $L = \partial_r^2 + (3/r)\partial_r + \partial_z^2$. The two source terms are the entire 3D content: $\partial_z(u_1^2)$ is vortex stretching driven by the swirl (the axisymmetric face of $\omega \cdot \nabla u$), and $2 u_1 \partial_z \psi_1$ feeds the meridional flow back into the swirl. Setting $u_1 \equiv 0$ kills both, and $\omega_1$ obeys pure transport-diffusion with a maximum principle: that system is globally regular (Ukhovskii-Yudovich 1968, Ladyzhenskaya 1968). The no-swirl run below is therefore this experiment's 2D-control analog.

## Setup

- **Domain**: $(r, z) \in [0,1] \times [0, 1)$, $z$ periodic. (Luo-Hou used period $1/6$; period 1 keeps the same mechanism with one wavelength.)
- **Wall** $r = 1$: no-penetration free-slip, $\psi_1 = 0$, $\omega_1 = 0$, $\partial_r u_1 = 0$. **Axis** $r = 0$: even symmetry of $(u_1, \omega_1, \psi_1)$, with $L f|_{r=0} = 4 f_{rr} + f_{zz}$.
- **Initial data** (Luo-Hou type): $u_1 = A\, e^{-30(1-r^2)^4} \sin(2\pi z)$, $\omega_1 = 0$, with $A = 4$. The profile peaks at the wall, satisfies $\partial_r u_1(1, z) = 0$ exactly, and its odd-in-$z$ symmetry places the hyperbolic stagnation point of the induced meridional flow at the wall, as in Luo-Hou. (Their amplitude 100 vs our 4 is a time rescaling for Euler; for NS it sets the Reynolds number.)
- **Discretization**: second-order finite differences in $r$, Fourier collocation in $z$, explicit RK2 (Heun), Poisson solve by precomputed Thomas sweeps per $z$ mode (verified second-order against an analytic solution: max error $1.19\times 10^{-3} \to 2.97\times 10^{-4} \to 7.42\times 10^{-5}$ on $n = 32 \to 64 \to 128$).
- **Baseline parameters**: $\nu = 0.005$, $t \in [0, 1]$, grids $64^2, 128^2, 256^2$.

## Run

```powershell
python -m experiments.hou_luo.hou_luo_axisymmetric
# knobs:
$env:NS_HL_NS = "64,128,256"; $env:NS_HL_NU = "0.005"; $env:NS_HL_AMP = "4.0"
```

About 5 minutes total (the $256^2$ leg is ~3 minutes). Time series cached in `_cache/hou_luo_runs.npz`.

## Result (2026-06-11 run)

### Refinement study (identical scenario, three grids, $\nu = 0.005$)

| $n$ ($r \times z$) | $dt$ | BKM $\int_0^1 \|\omega\|_\infty dt$ | peak $\|\omega\|_\infty$ | max $\|u_1\|_\infty$ | peak wall grad | $E(0)$ | $E(1)$ |
|---|---|---|---|---|---|---|---|
| $64^2$ | $7.81\times10^{-4}$ | 80.4113 | 128.9983 | 4.0000 | 128.9983 | 3.37521 | 0.86723 |
| $128^2$ | $3.91\times10^{-4}$ | 79.9070 | 128.5983 | 4.0000 | 128.5983 | 3.37406 | 0.86110 |
| $256^2$ | $1.18\times10^{-4}$ | 79.8195 | 128.4930 | 4.0000 | 128.4930 | 3.37377 | 0.85977 |

Successive relative changes: BKM $0.63\% \to 0.11\%$, peak vorticity $0.31\% \to 0.08\%$. **Verdict: CONVERGED under refinement.** Viscosity wins at these parameters: the wall-driven stretching event ($\|\omega\|_\infty$ rises from 25.13 to 128.5, a factor 5.1, peaking near $t \approx 0.42$) is fully resolved, the BKM integral is finite and grid-independent, and the energy decays monotonically (the free-slip boundary does no work). This is the expected viscous outcome, recorded as instrument output: the same diagnostic applied to a genuine near-singular candidate must show the opposite signature, BKM growth that survives refinement.

### Control (a): the no-swirl comparison (the 2D-control analog), $128^2$

Same solver, $u_1 \equiv 0$, initial $\omega_1$ scaled so the initial $\|\omega\|_\infty = 25.1327$ matches the swirl run, concentrated in the same wall band.

| run | initial $\|\omega\|_\infty$ | peak $\|\omega\|_\infty$ | amplification | BKM |
|---|---|---|---|---|
| swirl (Luo-Hou data) | 25.1327 | 128.5983 | **x5.12** | 79.9070 |
| no swirl | 25.1327 | 25.1327 | x1.00 | 17.6304 |

The no-swirl run never exceeds its initial vorticity, and $\|\omega_1\|_\infty$ obeys the transport-diffusion maximum principle to the digits sampled ($29.9136 \to 29.9136$, never above). Swirl is essentially what drives the growth: with the stretching source $\partial_z(u_1^2)$ removed, the same geometry, wall, and viscosity produce pure decay. This is the structural point: axisymmetric **with** swirl is regularity-open precisely because of this term; **without** swirl it is a theorem that nothing happens (Ukhovskii-Yudovich, Ladyzhenskaya).

### Control (b): viscosity reduced 4x, $128^2$

| $\nu$ | BKM | peak $\|\omega\|_\infty$ | peak wall grad |
|---|---|---|---|
| 0.005 | 79.9070 | 128.5983 | 128.5983 |
| 0.00125 | 246.7157 | 387.6871 | 387.6818 |

Growth under $\nu/4$: BKM x3.09, peak vorticity x3.01, wall gradient x3.01. The mechanism strengthens as viscosity weakens, consistent with its Euler ($\nu = 0$) limit being the Luo-Hou singularity candidate. The dependence is strong (roughly $\nu^{-0.8}$ in peak vorticity over this one step in $\nu$), which is exactly why a laptop cannot follow the scenario to the regime where the regularity question is actually contested.

## What this gives the program

1. **The instrument now exists on the right geometry.** `resolution_study/` calibrated the BKM-under-refinement diagnostic on Taylor-Green, a flow nobody expects to be near-singular. This experiment ports it to the one geometry where the inviscid limit provably blows up (Chen-Hou). Any future claim of NS near-singularity in this scenario has a concrete bar to clear: BKM growth that survives $64^2 \to 128^2 \to 256^2$.
2. **The swirl/no-swirl pair localizes the open problem dynamically.** One source term separates a globally-regular system from the regularity-open one, and the experiment shows that term doing all the work (x5.12 vs x1.00 at matched initial vorticity).
3. **A viscous-defeat data point.** At $\mathrm{Re} \sim 800$ on the Luo-Hou geometry, viscosity beats the wall-stretching mechanism with a converged, finite BKM integral. The known no-theorem gap (does $\nu \Delta u$ defeat the scenario at all $\nu > 0$?) stays open; this run marks the easy end of the curve and the $\nu/4$ control shows the direction of difficulty.

## Honest caveats

- **Wall condition**: free-slip ($\omega_1 = 0$ at $r = 1$), not no-slip. Luo-Hou's Euler scenario needs only no-penetration, which we keep, but the viscous closure pins the azimuthal wall vorticity to zero exactly where the Euler singularity concentrates. This choice avoids an unresolvable no-slip boundary layer at these grids; a no-slip variant (Thom's formula for $\omega_1$ at the wall) would be the natural follow-up and may strengthen wall vorticity production.
- **The $\nu/4$ control is directional, not converged**: at $\nu = 0.00125$ the $64^2 \to 128^2$ change is 13.1% in BKM and 17.7% in peak vorticity, so its numbers mark a trend, not resolved values. The headline refinement verdict applies only to the $\nu = 0.005$ scenario.
- Central differences in $r$ without upwinding and no dealiasing in $z$; at sharper gradients than these runs produce, that would show up first as grid oscillations, which the refinement comparison is designed to expose.
- $\|u_1\|_\infty$ never exceeded its initial value 4.0 in any run, so the swirl feedback channel $2 u_1 \partial_z \psi_1$ stayed passive at these parameters; the growth lived entirely in gradients. At higher Reynolds number this need not persist.
- Convergence at $\mathrm{Re} \sim 800$ says nothing about the supercritical regime. It is calibration on the right geometry, not evidence for global regularity.

## Handoff

- **VERIFIER targets**: none new; the relevant formal statement remains BKM (already in the Lean substrate as a target). The no-swirl global regularity statement (Ukhovskii-Yudovich) is a candidate for a future formalization rung, well below current Mathlib PDE coverage.
- **ADVERSARY tests run here**: 2D-control analog (no-swirl, PASSED: mechanism is swirl-essential), viscosity control (PASSED: growth strengthens at $\nu/4$). Criticality control: not applicable, no estimate is claimed; this is an instrument, not a bound.
- **Suggested attacks**: rerun with no-slip wall (Thom closure) at $128^2/256^2$ to test whether the free-slip choice suppresses wall vorticity materially; push $\nu$ down at fixed $t_{end}$ until the refinement verdict first fails to converge at $256^2$, and record that $\nu$ as the instrument's resolution boundary.
