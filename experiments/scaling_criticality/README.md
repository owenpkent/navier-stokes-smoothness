# Scaling and criticality (experiment d)

Architecture 3 (critical spaces and scaling). This is the headline control of the project in tabular form.

## What it does

`criticality_table.py` classifies the norms named in the problem spec (energy $L^2$, $H^1$, $H^{1/2}$, $L^3$, $\mathrm{BMO}^{-1}$, and the Beale-Kato-Majda vorticity integral) as subcritical, critical, or supercritical under the Navier-Stokes scaling

$$u_\lambda(x, t) = \lambda\, u(\lambda x, \lambda^2 t).$$

It then audits each norm as a candidate controlling quantity for a regularity proof.

Run it:

```
python -m experiments.scaling_criticality.criticality_table
```

It is pure bookkeeping (no PDE solve), so it is instant and deterministic.

## Result

| Norm | Exponent | Class | Verdict |
|---|---|---|---|
| energy $L^2$ | $-1/2$ | supercritical | INSUFFICIENT_BY_ITSELF |
| $H^1$ (enstrophy$^{1/2}$) | $+1/2$ | subcritical | WOULD_CLOSE_IF_AVAILABLE |
| $H^{1/2}$ (Fujita-Kato) | $0$ | critical | AT_THE_MARGIN |
| $L^3$ (ESS endpoint) | $0$ | critical | AT_THE_MARGIN |
| $\mathrm{BMO}^{-1}$ (Koch-Tataru) | $0$ | critical | AT_THE_MARGIN |
| vorticity $L^\infty$-in-time (BKM) | $0$ | critical | AT_THE_MARGIN |

## Why it matters

The energy inequality is the only coercive a priori bound that holds for all time in 3D, and it controls the $L^2$ norm of $u$, which is supercritical (exponent $-1/2$). Supercritical means: rescaling to small scales makes the norm small, so it gives no control where a singularity would form. Regularity, by contrast, is a critical-or-subcritical statement (BKM, PSL, ESS all sit at exponent $0$). The gap between the supercritical bound we have and the critical control we need is the supercriticality gap. It is the compass for the whole project: a proof must add genuinely critical control, and it must use the 3D vortex-stretching structure (the $H^1$/enstrophy bound IS available in 2D, which is why 2D is solved).

The exponents are derived in `experiments/_shared/criticality.py` with the algebra documented in the docstrings. The classification is convention independent.
