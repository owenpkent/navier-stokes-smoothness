# Energy spectrum and dissipation (experiment c)

Architecture 1 / 3, the spectral picture of the supercriticality gap.

## What it does

`energy_spectrum.py` computes the shell-averaged kinetic-energy spectrum $E(k)$ and the dissipation rate

$$\varepsilon = 2\nu \sum_k k^2 E(k)$$

from a 3D divergence-free velocity field. By default it builds a representative field with a smooth injection spectrum $E(k) \sim k^4 e^{-2(k/k_0)^2}$ (so the experiment always runs standalone); it has a hook to read a Taylor-Green DNS field snapshot when one is cached.

Run it:

```
python -m experiments.energy_spectrum.energy_spectrum
```

Fast. Plotting is optional.

## Result

- $E(k)$ peaks at low $k$ (large scales) and falls off smoothly.
- The dissipation integrand $k^2 E(k)$ is weighted toward higher $k$ (small scales) and peaks well inside the grid Nyquist wavenumber, so the field is resolved.
- Total energy matches the Parseval sum.

## Why it matters

The spectrum makes the supercriticality gap visible as a distribution over scales. Energy lives at large scales (low $k$), exactly where the a priori energy bound holds. A singularity, if one formed, would form at small scales (high $k$), exactly where the energy gives no control and where finite resolution always bites first. The wavenumber at which $E(k)$ falls below the grid resolution is the numerical face of the analytic gap: below it the DNS is trustworthy, above it the simulation cannot see what the equations are doing.

At the low Reynolds number of the coarse Taylor-Green run there is no inertial range and the spectrum is steep (dissipative): no incipient singularity, which is consistent with the finite BKM integral from experiment (a). At high Reynolds number a genuine inertial range would appear with the Kolmogorov $-5/3$ slope, and the resolution requirement to follow the dissipation peak grows; this is why research-resolution DNS is expensive and why the in-repo experiments are deliberately coarse.
