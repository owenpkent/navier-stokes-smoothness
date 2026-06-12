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

---

# Part 2: the beta-dial and intense-set sparseness (`beta_dial.py`)

Implements the two survey-to-builder handoffs of the Architecture 2 dossier ([`../../docs/research_atlas/conditional_criteria_dossier.md`](../../docs/research_atlas/conditional_criteria_dossier.md), sections 11.3.1 and 11.3.2; LEARNINGS #12). The Constantin-Fefferman family has an internal criticality ladder: a Holder-$\beta$ modulus on $\xi = \omega/|\omega|$ carries scaling tax $a = +\beta$, with $\beta = 1$ the CF 1993 rung, $\beta = 1/2$ the Beirao da Veiga-Berselli 2002 rung (enstrophy height), and the unconditional $\beta = 0$ endpoint open (Direction 02). This experiment measures where on that ladder the actual flow sits.

**What it measures.** On the intense set (top decile of $|\omega|$, both pair endpoints inside), at dyadic separations $h = \Delta x \cdot 2^m$ along the three axes:

1. The Holder-$\beta$ seminorm of $\xi$ for $\beta \in \{1, 1/2, 1/4\}$, using the CF modulus $|\xi(x) \times \xi(x + h e)| = \sin\theta$ (orientation-insensitive, the exact quantity in the CF hypothesis) with a 99th-percentile estimator robust to isolated pairs, tracked along the run.
2. The misalignment-angle curve $\theta(h)$ at the time of peak resolved enstrophy production; its log-log slope is the empirical local Holder exponent of the direction field, the single most informative number for Direction 02.
3. Grujic sparseness diagnostics at dyadic thresholds $M = \max|\omega| \cdot 2^{-k}$, $k = 0..4$: volume fraction of the super-level set, largest connected run length along grid lines (the linear-slice statistic, as a fraction of the box), and the depletion factor restricted to each sub-set.

## Run

```powershell
python -m experiments.vortex_stretching.beta_dial
```

Defaults match part 1: $32^3$, $\nu = 0.01$, $t \in [0, 4]$, snapshots every $0.25$. About a minute. Full time series cached in `_cache/beta_dial.npz` (gitignored). Does not touch `alignment_depletion.py`.

## Result (2026-06-11 run, $32^3$, $\nu = 0.01$)

**Beta-dial (handoff 11.3.1).** Seminorms $[\xi]_{C^\beta}$ (q99 of $\sin\theta / h^\beta$ over pairs, sup over $h \in [2\Delta x, 16\Delta x]$):

| $t$ | $\beta = 1$ | $\beta = 1/2$ | $\beta = 1/4$ |
|---|---|---|---|
| 0.5 | 0.63 | 0.50 | 0.47 |
| 1.0 | 0.89 | 0.68 | 0.64 |
| 1.5 | 0.94 | 0.84 | 0.89 |
| 1.75 to 2.25 (plateau) | 1.27 | 1.13 | 1.06 |

All three grow by a factor $2.0$ to $2.3$ while the cascade develops ($t \le 1.75$), then hold exactly flat to the edge of the resolved window ($t \le 2.25$, budget residual $\le 5\%$): bounded, but not $\beta$-separating. The plateau is saturation, not extra coherence information: the 99th-percentile misalignment reaches $90^\circ$ at $h = 4\Delta x$, after which the seminorm reads $h^{-\beta}$ mechanically. The later jump at $t = 3.25$ ($1.27 \to 2.55$ for $\beta = 1$) lands exactly where the budget residual passes $27\%$: under-resolution announcing itself, not physics.

**The headline number.** $\theta(h)$ at peak resolved production ($t^* = 2.25$, $P = 45.6$, global depletion $0.55$):

| $h/\Delta x$ | pairs | median $\theta$ | p99 $\theta$ | status |
|---|---|---|---|---|
| 1 | 5952 | $4.1^\circ$ | $9.7^\circ$ | one cell, untrusted |
| 2 | 3200 | $7.9^\circ$ | $13.7^\circ$ | fit window |
| 4 | 2240 | $17.8^\circ$ | $89.6^\circ$ | fit window |
| 8 | 1744 | $52.0^\circ$ | $89.6^\circ$ | fit window |
| 16 | 3504 | $88.6^\circ$ | $89.4^\circ$ | half-box, decorrelated |

Empirical local Holder exponent: $\alpha = 1.36$ over the trusted window $h \in [2\Delta x, 8\Delta x]$ (adjacent dyadic slopes $1.17$ and $1.54$; the upper one is inflated by the approach to decorrelation, since random direction lines give median $60^\circ$). The cleanest local reading is the $2\Delta x \to 4\Delta x$ slope, $\alpha \approx 1.2$. Either way $\alpha \ge 1$: at the resolved scales this flow sustains the full **CF-1993 Lipschitz rung**; the sustained $\beta$ has not degraded toward $1/2$, let alone toward the open $\beta = 0$ endpoint.

**Sparseness (handoff 11.3.2)** at $t^* = 2.25$ ($\max|\omega| = 1.71$); run lengths as fraction of the box, depletion restricted to each set:

| $k$ | $M/\max$ | vol. fraction | run med | run p95 | depletion on set |
|---|---|---|---|---|---|
| 0 | $1$ | 0.00003 | 0.03 | 0.03 | 1.00 |
| 1 | $1/2$ | 0.67 | 0.34 | 0.97 | 0.58 |
| 2 | $1/4$ | 0.90 | 0.97 | 1.00 | 0.55 |
| 3 | $1/8$ | 0.92 | 0.97 | 1.00 | 0.55 |
| 4 | $1/16$ | 0.93 | 0.97 | 1.00 | 0.55 |

The verdict is negative and informative: the laminar Taylor-Green field is **not sparse** (two thirds of the box sits above half of $\max|\omega|$, run lengths span the box, depletion is flat at $\approx 0.55$ across thresholds, so no sparseness-to-depletion trend has dynamic range here). One weak trend points the right way: the $k = 2$ volume fraction falls from $0.92$ ($t = 1.5$) to $0.67$ ($t = 4$) as the cascade concentrates the field. This run is the non-filamentary baseline, not a test of the Grujic hypothesis, which concerns near-singular fields.

**2D control.** Through the same code path with $\xi$ embedded as $\pm e_z$: $\sup |\xi(x) \times \xi(y)| = 0.0$ exactly, over all pairs and separations, so every Holder-$\beta$ seminorm vanishes identically. The geometric family passes the 2D control non-vacuously: its hypothesis is automatic precisely where regularity is free.

## Reading

The handoff question was: which $\beta$ does the flow sustain, and does it degrade toward $0$ or stall near $1/2$? At laminar TG parameters the answer is the top of the ladder: bounded seminorms at all three $\beta$ in the resolved window, with local exponent $\alpha \ge 1$, i.e. the flow is at least Lipschitz-coherent exactly where the vorticity is intense. The staircase question is not settled by a mild flow, but the instrument now exists, is calibrated (2D control exact, resolution alarm built in), and has a sharp one-number readout ($\alpha$) ready to mount on the Hou-Luo geometry, where intensity actually grows. For sparseness the readout is a clean negative: no filamentary structure at these parameters, so the observed depletion ($\approx 0.55$) cannot be attributed to sparseness here, which sharpens the question of what does force it.

## Honest caveats

- Trusted separations are $h \ge 2\Delta x \approx 0.39$; the one-cell separation is reported but excluded from seminorms and fits (the last octave of a $32^3$ spectral grid is aliasing-contaminated). No claim about the modulus of $\xi$ below $h = 0.39$.
- $t^* = 2.25$ is the edge of the resolved window and production is still rising there; the true production peak lies beyond what this grid resolves.
- $\alpha \ge 1$ at laminar parameters does not transfer to near-singular regimes. The dossier's real question (does the sustained $\beta$ degrade as intensity grows?) needs this instrument on a Hou-Luo-type run with per-resolution convergence checks (LEARNINGS #13).
