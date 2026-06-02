# State of the research program (repo-wide)

> A one-page strategic snapshot of the whole project: where every architecture stands, what wall each hits, where the live work is, and the single most-leveraged next move. Companion to the operational [`PHASE_STATE.md`](PHASE_STATE.md) (current sub-task, falsifiability triggers) and the synthesis surface [`experiments/LEARNINGS.md`](experiments/LEARNINGS.md) (cross-architecture findings).

## The thesis in one paragraph

The program does not have a proof of global regularity (nor a blow-up example) and is not close to one. What it has is a **sharp map of where a proof cannot live and a precise specification of the gap a proof must cross**. The dominant meta-finding, structural and not heuristic, is the **supercriticality of the energy estimate**: the only coercive a priori bound that holds for all time in 3D (the energy inequality) controls a norm that is supercritical with respect to the scaling symmetry, so it provides no control at small scales where a singularity would form. Every classical regularity criterion (Prodi-Serrin-Ladyzhenskaya, Beale-Kato-Majda, the endpoint $L^3$ of Escauriaza-Seregin-Sverak) sits at or above the critical level the energy cannot reach. That gap, energy below, regularity above, with the scaling-critical line between them, is the compass. A proof must supply genuinely **critical** control, and it must use the exact 3D structure (vortex stretching), because in 2D the same structure is absent and the problem is solved.

## The five architectures

| Arch | What it is | Status | The wall (what we learned) |
|---|---|---|---|
| **1. Energy / weak solutions** (Leray-Hopf, CKN) | global weak solutions exist; bound the singular set | **Foundational, not closing** | Leray-Hopf solutions exist for all time (1934/1951) but are not known unique or smooth in 3D. CKN (1982) bounds the singular set ($\mathcal{P}^1 = 0$) but does not exclude it. The energy is supercritical. |
| **2. Conditional regularity criteria** (PSL, BKM, ESS) | "if quantity $X$ is bounded, the solution stays smooth" | **Sharp but conditional** | PSL ($2/p+3/q\le1$), BKM ($\int\|\omega\|_\infty$), ESS ($L^\infty_t L^3_x$) are all at the critical scaling level. They convert the problem to controlling a critical quantity, which the energy cannot do. |
| **3. Critical spaces / scaling** (Fujita-Kato, Koch-Tataru) | global existence for small critical data | **Small-data only** | Small data in $\dot H^{1/2}$, $L^3$, or $\mathrm{BMO}^{-1}$ gives global smooth solutions. Large data is the open problem; the supercriticality gap is exactly the obstruction to bootstrapping from energy. |
| **4. Blow-up / self-similar** (Leray, Tao, Elgindi) | construct a singularity | **No NS example; barriers exist** | Leray self-similar blow-up is ruled out in $L^3$ (Necas-Ruzicka-Sverak; Tsai). Tao (2016) built finite-time blow-up for an *averaged* NS (a barrier: any regularity proof must exclude the averaged caricature). Euler blow-up is now established in some settings (Elgindi 2021) and numerically supported (Chen-Hou). |
| **5. Non-uniqueness / convex integration** (Buckmaster-Vicol) | non-unique weak solutions below energy class | **Boundary of "solution," not regularity** | Buckmaster-Vicol (2019) show non-uniqueness of weak solutions below the Leray-Hopf class. This sharpens what "solution" must mean (Leray-Hopf is the right class) but does not address smoothness of the strong flow. |

Each status is a coordinate. Together they say: the proof is **not** a soft energy argument, **not** a small-data argument scaled up, and the blow-up side has no NS example but a real barrier (Tao). Effort concentrates on supplying critical control that excludes the Tao-type caricature while respecting that 2D is smooth.

## The live front: the supercriticality gap

The bet (the analog of what worked elsewhere in analysis): find a quantity that is (a) controlled by the data for all time and (b) at least scaling-critical, so that bounding it closes BKM or PSL. What is in hand vs. missing:

**In hand (mapped and, where computational, validated):**
- The scaling exponents of every standard norm, classified sub/critical/super by the criticality bookkeeper (experiment `scaling_criticality`). Energy $L^2$ is supercritical; $\dot H^{1/2}$, $L^3$, $\mathrm{BMO}^{-1}$ are critical; $\sup_t \|\omega\|_{L^\infty}$ integrated in time is the BKM critical control.
- The 2D control: in 2D the enstrophy is non-increasing because there is no stretching term, so the same chain of estimates closes. Any 3D method must break exactly where 2D does not.
- The viscosity control: inviscid Burgers forms a shock in finite time, viscous Burgers does not (experiment `burgers_shock`). 3D Euler blows up (Elgindi); 3D NS regularity, if true, is a statement about what $\nu \Delta u$ buys.
- A coarse Taylor-Green DNS that, at low Reynolds number, shows the BKM integral staying finite (no blow-up at these parameters), as expected.

**The one missing object:** a coercive, scaling-critical (or subcritical) a priori bound, derived from the data and the equation, that controls a BKM/PSL quantity for all time and genuinely uses 3D vortex stretching. No such bound is known. This is the open problem.

## The cross-cutting compass

- **Supercriticality** (the dominant finding): no buffer in the energy. Dig where a critical bound could come from: the structure of the nonlinear vortex-stretching term, anisotropy, or a partial/conditional critical norm.
- **The scaling line**: regularity is a critical-scaling statement. Sub/critical/super is the coordinate system; everything maps onto it.
- **The three controls**: 2D must stay smooth (uses no stretching, so any method that ignores stretching is wrong); supercriticality is the ceiling on energy methods; viscosity is essential (a method blind to $\nu$ is suspect, since Burgers and Euler blow up).

## Lean substrate

Skeleton with documented `sorry`s (need not build). Targets: divergence-free vector fields, the Leray projector, the energy inequality, the Beale-Kato-Majda criterion statement, the scaling identity, and the global-regularity goal statement. Mathlib lacks the Sobolev-spaces-of-vector-fields and Leray-projection infrastructure to make these clean, so the skeleton flags the gaps. See [`lean/README.md`](lean/README.md).

## The single most-leveraged next move

**Hunt for a partial critical bound under the 2D-and-viscosity discipline.** The cheapest high-value moves are computational and survey work that sharpen the gap:
1. Map exactly which conditional criteria (PSL, BKM, ESS, one-component, vorticity-direction Constantin-Fefferman) are critical and which are subcritical, and which have been weakened to scale-invariant geometric conditions (vorticity coherence). The vorticity-direction-regularity result (Constantin-Fefferman 1993) is the closest thing to a structural critical control and is the most promising survey target.
2. Run resolution studies on near-singular initial data (Taylor-Green at higher Reynolds; the Hou-Luo axisymmetric scenario) to see whether the BKM integral shows any sign of divergence, with the explicit understanding that numerics cannot prove blow-up, only suggest where to look.

Honest odds: an unconditional proof from this repo is far below 1%. The value is that any genuine advance (a new critical bound, or a rigorous NS blow-up) would be a top-tier result, and the partial work (mapping the gap, the controls, the formalization) is a contribution in its own right.

## Canonical pointers

- Operational state / next sub-task: [`PHASE_STATE.md`](PHASE_STATE.md)
- Cross-architecture findings: [`experiments/LEARNINGS.md`](experiments/LEARNINGS.md)
- Test plan + per-architecture status: [`experiments/PLAN.md`](experiments/PLAN.md)
- Master research map (all approaches, obstructions): [`docs/research_atlas/README.md`](docs/research_atlas/README.md)
- The research directions: [`docs/03_research/research_directions/`](docs/03_research/research_directions/)
- The operating philosophy: [`docs/researcher_mindset.md`](docs/researcher_mindset.md)
- Lean substrate + VERIFIER targets: [`lean/README.md`](lean/README.md)
