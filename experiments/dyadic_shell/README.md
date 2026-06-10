# Dyadic shell model: the criticality boundary as dynamics

Experiment (g). The criticality bookkeeper is the project's central CONTROL, but so far it has been static arithmetic. This experiment makes it dynamical, in the one model family where blow-up is a theorem and the criticality dial is explicit.

## The model

$$\frac{da_n}{dt} = \lambda^n a_{n-1}^2 - \lambda^{n+1} a_n a_{n+1} - \nu\,\lambda^{2\alpha n} a_n, \qquad \lambda = 2,\ n = 0, \dots, N-1,$$

with $a_{-1} = a_N = 0$. The quadratic terms telescope, so the nonlinearity conserves energy exactly while pushing it to higher shells: a caricature of the 3D cascade. This is the Katz-Pavlovic / Cheskidov model family; Tao's 2016 averaged-NS blow-up (finding #7 in [`../LEARNINGS.md`](../LEARNINGS.md)) is the culmination of the same line.

## The dial and the prediction

The exponent $\alpha$ sets viscosity strength relative to the cascade. On a constant-flux profile $a_n \sim \lambda^{-n/3}$, the nonlinear turnover rate at shell $n$ grows like $\lambda^{2n/3}$ and the dissipative rate like $\lambda^{2\alpha n}$. Flux balance therefore predicts a sharp boundary at $\alpha_c = 1/3$ in this convention: blow-up below, regularity above. Blow-up in the infinite system means the shell-activation times $t_n$ form a convergent geometric series, which is exactly what the script measures (and extrapolates to a blow-up time $t^*$).

## Run

```powershell
python -m experiments.dyadic_shell.criticality_scan
```

Forty shells, an inviscid control run (the Katz-Pavlovic regime, with an energy-conservation check on the integrator), then a scan over $\alpha$ at fixed $\nu$. Seconds to run.

## Result (2026-06-09 run)

- Inviscid: finite-time blow-up with arrival-time ratio close to the predicted $\lambda^{-2/3}$, energy conserved to integrator precision.
- Viscous scan: the verdict flips from BLOWS UP to REGULAR across $\alpha_c = 1/3$, where the flux-balance arithmetic said it would.

## Why this pushes the program forward

1. **It validates the CONTROL dynamically.** The bookkeeper's sub/critical/super classification is not metaphor: in a system where the dial exists, the classification is the boundary between singular and regular dynamics.
2. **It is finding #7 in miniature, watchable.** The model keeps the energy identity and the scaling and still blows up on the supercritical side. Whatever saves real NS (if it is saved) must come from structure the caricature destroys: transport instead of pure forward transfer, pressure, phase cancellation, geometry. That is the same coordinate Tao's barrier fixes, now with a runnable demonstration.
3. **It frames the gap quantitatively.** Real NS energy bookkeeping sits on the supercritical side of its own boundary. The model shows what living on the wrong side of the line costs, and what kind of term (critical-or-better damping relative to the cascade) would have to be found or manufactured.

## Honest caveats

- The dyadic model is a one-way cascade with no phases, no transport, no pressure. It is a barrier-side instrument. Nothing here is evidence about true NS dynamics.
- The finite truncation cannot blow up (energy bounds every mode); blow-up is read off from geometric convergence of activation times, the standard and correct diagnostic for this model class.
- Near $\alpha_c$ the verdict on a finite shell range is sensitive to $\nu$ and $N$; the script reports INCONCLUSIVE rather than forcing a call when the front advances non-geometrically.
