# Research atlas: the master map

The comprehensive catalog of approaches to the Navier-Stokes existence and smoothness problem, the obstruction each meets, and the directions (including machine-learning directions) that remain. Start here for research orientation. The compact version is [`../solutions/README.md`](../solutions/README.md); the live experimental thread is [`../../experiments/PLAN.md`](../../experiments/PLAN.md).

## How to read this atlas

The problem has a single organizing obstruction, the **supercriticality gap**: the only all-time a priori bound (energy) is supercritical, every regularity criterion is critical, and the gap between them must be crossed by genuinely new critical control. Every entry below is positioned relative to this gap. Three structural controls keep candidates honest:

1. **2D control**: 2D Navier-Stokes is globally smooth (no vortex stretching). A method that ignores stretching fails.
2. **Criticality control**: a supercritical controlling norm is insufficient by itself.
3. **Viscosity control**: inviscid relatives (Burgers, Euler) blow up; a method blind to $\nu$ is suspect.

## The obstruction map

| Approach | Best result | Obstruction | Relation to the gap |
|---|---|---|---|
| Energy / Galerkin compactness | Leray-Hopf global weak existence | energy is supercritical | gives existence, not regularity |
| Partial regularity (CKN) | singular set $\mathcal{P}^1 = 0$ | local energy is supercritical | stops at parabolic dimension 1 |
| Prodi-Serrin-Ladyzhenskaya | regularity from $L^p_tL^q_x$, $2/p+3/q\le1$ | criterion is critical, energy gives $3/2$ | conditional; energy cannot reach |
| ESS endpoint | regularity from $L^\infty_tL^3_x$ | critical norm, no a priori control | conditional; deepest critical criterion |
| Beale-Kato-Majda | blow-up iff $\int\|\omega\|_\infty=\infty$ | critical integral, no a priori control | the sharp blow-up criterion |
| Constantin-Fefferman | regularity from vorticity-direction coherence | coherence not known a priori | scale-aware geometric; the lead |
| Critical-space small data | global smooth for small $\dot H^{1/2}$, $L^3$, $\mathrm{BMO}^{-1}$ | smallness essential | large data is the open problem |
| Leray self-similar blow-up | the ansatz | ruled out in $L^3$ (NRS, Tsai) | a closed branch of the blow-up side |
| Averaged-NS blow-up (Tao) | finite-time blow-up of a caricature | not NS; a barrier | forbids energy-plus-scaling proofs |
| Euler blow-up (Elgindi, Hou-Luo) | $C^{1,\alpha}$ Euler singularity; strong numerics | inviscid; viscosity may save NS | informs where viscosity is marginal |
| Convex-integration non-uniqueness | non-unique weak solutions (Buckmaster-Vicol) | below the Onsager threshold | outside the regularity discipline |

For Architecture 2 in full detail, see the [conditional-criteria criticality dossier](conditional_criteria_dossier.md): every known conditional criterion (PSL, ESS and its extensions, BKM, gradient, pressure, one-component, vorticity-direction, the $\dot B^{-1}_{\infty,\infty}$ endpoint, and the log-improved layer) placed on the sub/critical/super coordinate, with the structural information each uses.

## The five obstructions, named

Reading down the table, the obstructions cluster into five recurring walls:

1. **Supercriticality** (the master wall): the energy is at the wrong scaling level. Everything else is a consequence.
2. **The 2D-3D divide**: the danger is vortex stretching, present only in 3D. Any method must be 3D-specific.
3. **The viscosity question**: regularity is about what $\nu\Delta u$ buys; the inviscid relatives blow up.
4. **The averaged-NS barrier**: soft arguments (energy + scaling) are excluded by an explicit counterexample.
5. **The solution-concept boundary**: non-uniqueness lives below the Onsager threshold, separate from smoothness.

A proof must thread all five: critical control (1), 3D-specific (2), using viscosity (3), using the exact nonlinearity (4), in the Leray-Hopf class (5).

## Machine-learning and computational directions

ML cannot prove a theorem, but it can find structure that suggests where a proof or a blow-up lives. Honest, scoped uses:

- **Near-singular structure detection.** Train on DNS fields (e.g. the Johns Hopkins Turbulence Database) to detect the geometric configurations (vortex-line alignment, anti-parallel tubes) that precede intense stretching. This sharpens Direction 02.
- **Lyapunov-functional search.** Search a parameterized family of functionals for one that is critical-scaling and (almost) monotone along DNS trajectories, then hand any candidate to analysis (Direction 03). The criticality bookkeeper screens candidates automatically.
- **Blow-up scenario optimization.** Optimize initial data to maximize a BKM-type diagnostic at fixed resolution, with the viscosity control as the referee (resolution-convergent or it is an artifact). This informs Direction 04.
- **Learned closures as hypothesis generators.** Not for proof, but a learned closure that reproduces the cascade can suggest which structural feature of the nonlinearity matters, feeding the averaged-NS-barrier analysis.

Every ML output is a hypothesis, not a result, and is checked by analysis and by the three controls before it enters the canonical narrative.

## Where the live work is

The most-leveraged directions (see [`../03_research/research_directions/`](../03_research/research_directions/)):

- **Direction 02 (vorticity geometry)**: the geometric criterion is the closest existing thing to a structural critical control.
- **Direction 03 (the supercriticality gap)**: the highest value, the hardest; a critical (almost-)monotone quantity would be a breakthrough.
- **Direction 01 (sharpen critical criteria)**: the most likely place for an incremental, publishable advance (quantitative ESS, logarithmic BKM).

Honest odds: an unconditional proof from this repo is far below 1%. The value is the map, the controls, the formalization, and the chance that one of the small rungs is real.
