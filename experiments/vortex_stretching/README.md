# Vortex stretching anatomy: budget, alignment, depletion, direction coherence

Experiment (f). A direct measurement of the one term that separates 3D from 2D, aimed at the Constantin-Fefferman lead flagged in [`../../PHASE_STATE.md`](../../PHASE_STATE.md).

## Why this experiment

The enstrophy evolves by

$$\frac{dZ}{dt} = \underbrace{\int \omega \cdot S\,\omega\,dx}_{P\ \text{(stretching production)}} - \underbrace{\nu \int |\nabla\omega|^2\,dx}_{D\ \text{(dissipation)}},$$

with $S$ the strain tensor. In 2D, $P \equiv 0$ structurally, the enstrophy is non-increasing, and regularity follows (finding #3 in [`../LEARNINGS.md`](../LEARNINGS.md)). In 3D, $P$ is unsigned and pointwise bounded only by $\lambda_3 |\omega|^2$ ($\lambda_3$ = largest strain eigenvalue), and no a priori bound controls it for all time. Every credible path to regularity must say something about why $P$ does not win forever.

The experiment measures, along a Taylor-Green run, the four quantities that frame that question:

1. **The budget identity** $dZ/dt = P - D$, verified numerically (a solver-honesty check and the quantitative face of the 2D/3D contrast; the 2D control runs alongside with $P$ structurally zero).
2. **Strain-eigenvector alignment** in the high-vorticity region. Blow-up wants $\omega \parallel e_3$ (most extensional). The classical DNS fact (Ashurst-Kerstein-Kerr-Gibson 1987) is alignment with the **intermediate** eigenvector $e_2$ instead.
3. **The depletion factor** $P / \int \lambda_3 |\omega|^2$: how much of the maximal possible stretching the flow actually realizes.
4. **Constantin-Fefferman direction coherence**: $|\nabla \xi|$ for $\xi = \omega/|\omega|$ over the intense region. CF (1993) proved that if the vorticity direction is Lipschitz in the high-vorticity region, the solution stays regular: geometric coherence is a genuine, scaling-respecting regularity mechanism, and it is 3D-specific (it constrains the stretching term itself).

## Run

```powershell
python -m experiments.vortex_stretching.alignment_depletion
```

Defaults: $32^3$, $\nu = 0.01$, $t \in [0, 4]$, snapshots every $0.5$. About a minute.

## Result (2026-06-09 run, $32^3$, $\nu = 0.01$)

- The budget identity holds in the resolved window $t \le 2$ (max residual $0.65\%$ against the centered difference of $Z$). By $t = 3.5$ the residual grows to $36\%$: the grid has stopped resolving the cascade, so the budget residual doubles as a resolution alarm (the computational shadow of LEARNINGS #6).
- Alignment in the top-decile region: this laminar, symmetric flow does **not** show the classical turbulence $e_2$-dominance (Ashurst et al. is a turbulence statistic); at mid-run the vorticity aligns with the extensional direction $e_3$ (mean $|\cos| = 0.87$).
- Even so, the realized stretching is only a fraction $\approx 0.53$ of the pointwise-maximal $\int \lambda_3 |\omega|^2$, and production $P$ exceeds dissipation $D$ for an extended window ($t \approx 0.3$ to $4$) while the flow stays smooth: dissipation catches the cascade.
- $|\nabla\xi|$ in the intense region (mean $\approx 0.8$, p95 $\approx 1.3$ at mid-run) sits far below the Nyquist scale $16$: the direction field is coherent exactly where the vorticity is large.

## Reading

The flow systematically fails to use the stretching the strain field offers. That observed depletion is what the Constantin-Fefferman criterion converts into a conditional theorem, and the open problem in these coordinates is to make the depletion **forced** (an a priori consequence of the equation) rather than observed. This experiment passes the wrong-approach discipline by construction: it measures the 3D-only term (2D control attached), and it makes no claim the criticality bookkeeper would flag, because it proves nothing; it locates where the proof must act.

## Honest caveats

- $32^3$ at $\mathrm{Re} \sim 100$ is a mild flow; alignment and depletion statistics in turbulent or near-singular regimes need resolution this experiment does not have.
- Alignment statistics are observation. Nothing here shows depletion persists where it would matter (near a putative singularity); that is precisely the open question.
