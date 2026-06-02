# Burgers shock: the viscosity control (experiment b)

Architecture 4 (blow-up), used here as a wrong-approach detector: the viscosity control.

## What it does

`burgers_blowup.py` integrates the 1D Burgers equation

$$\partial_t u + u\,\partial_x u = \nu\, \partial_{xx} u$$

from $u_0 = \sin x$ on the periodic interval, once with $\nu = 0$ (inviscid) and once with $\nu = 0.05$ (viscous), using an accurate pseudo-spectral scheme. It tracks $\max_x |u_x|$ in time.

Run it:

```
python -m experiments.burgers_shock.burgers_blowup
```

Fast (a few seconds). Plotting is optional and is skipped if matplotlib is unavailable.

## Result

For $u_0 = \sin x$, characteristics cross at $t^* = -1 / \min_x u_0'(x) = 1.0$. The experiment reproduces this:

- **Inviscid** ($\nu = 0$): $\max|u_x|$ grows without bound as $t \to t^* = 1.0$ (the gradient blows up: a shock forms). Peak gradient over the run reaches several hundred before the run stops.
- **Viscous** ($\nu = 0.05$): $\max|u_x|$ saturates at a finite value (about $8$) and the solution stays smooth for all time.

The detector fires: inviscid peak gradient is more than an order of magnitude above the viscous peak.

## Why it matters

Burgers carries the same quadratic transport nonlinearity $u \cdot \nabla u$ as Navier-Stokes, in the simplest possible setting. The contrast is the structural lesson: **dissipation is what prevents gradient blow-up**. This is a control on candidate regularity arguments. Any argument for 3D Navier-Stokes regularity that does not use the viscous term $\nu \Delta u$ cannot be correct, because the inviscid relative is singular. The point is not academic: 3D Euler (the genuine inviscid relative of NS) is now known to admit finite-time singularities in some settings (Elgindi 2021) and is numerically supported in others (Hou-Luo, Chen-Hou). So the question of NS regularity is precisely a question about what $\nu \Delta u$ buys, and a method blind to viscosity is suspect.
