# Taylor-Green vortex DNS (experiment a)

Architecture 1 / 2 (energy methods and conditional criteria), in computational form.

## What it does

`taylor_green_dns.py` is a pseudo-spectral direct numerical simulation of the 3D incompressible Navier-Stokes equations on $\mathbb{T}^3$, started from the Taylor-Green vortex

$$u_0 = (\sin x \cos y \cos z,\; -\cos x \sin y \cos z,\; 0).$$

On a coarse $32^3$ grid at low Reynolds number ($\nu = 0.025$, $\mathrm{Re} \approx 40$) it tracks:

- kinetic energy $E(t) = \tfrac12 \langle |u|^2 \rangle$
- enstrophy $Z(t) = \tfrac12 \langle |\omega|^2 \rangle$
- max vorticity $\|\omega(t)\|_{L^\infty}$
- the Beale-Kato-Majda integral $\int_0^t \|\omega\|_{L^\infty}\, ds$

Run it:

```
python -m experiments.taylor_green.taylor_green_dns
```

It finishes in about a minute at $32^3$. Resolution and Reynolds number are tunable via the environment variables `NS_TG_N`, `NS_TG_NU`, `NS_TG_TEND`, `NS_TG_DT`.

## Result (32^3, nu = 0.025, to t = 3)

- **Energy** decreases monotonically ($0.125 \to 0.072$): the energy inequality $\tfrac12\|u(t)\|_2^2 + \nu\int_0^t\|\nabla u\|_2^2 \le \tfrac12\|u_0\|_2^2$ holds numerically.
- **BKM integral** reaches about $4.4$ and stays finite: by Beale-Kato-Majda the solution remains smooth, which is the expected behavior at this low Reynolds number.
- **Incompressibility** $\max|\nabla\cdot u| \approx 10^{-17}$ at the final time: the Leray projection holds the constraint to machine precision.

## Why it matters

This is the non-singular baseline. The Taylor-Green vortex is the canonical test flow for the transition to small scales; at low Reynolds number it relaxes smoothly, and the diagnostics confirm the solver respects the structural a priori bounds (energy dissipation, incompressibility, finite BKM integral).

It is emphatically **not** a proof of global regularity. Numerics can suggest where to look but cannot decide the problem. The criticality control still applies: the energy bound that holds here is supercritical and cannot close regularity on its own. The value of the experiment is twofold: it validates the solver against the analytic structure, and it provides the baseline against which near-singular scenarios (higher Reynolds, the Hou-Luo axisymmetric flow) would be compared in a resolution study, where the diagnostic of interest is whether the BKM integral shows any sign of divergence under grid refinement (it must not, if the diagnostic is to be trusted; an apparent divergence that goes away under refinement is a numerical artifact, the viscosity-control discipline).
