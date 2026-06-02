# Known approaches and their obstructions

An architecture-by-architecture summary of how people have tried to solve the Navier-Stokes existence and smoothness problem, and the wall each approach meets. This is the compact companion to the fuller [`../research_atlas/README.md`](../research_atlas/README.md).

Every wall is stated as a coordinate (where the proof cannot live), not a verdict (that the proof cannot exist). The five architectures and their experiments are tracked in [`../../experiments/PLAN.md`](../../experiments/PLAN.md).

## The one fact that organizes everything

The energy inequality is the only coercive a priori bound that holds for all time, and it is **supercritical** with respect to the scaling symmetry $u_\lambda(x,t)=\lambda u(\lambda x,\lambda^2 t)$. Regularity is a critical statement. Every approach below either lives at the supercritical level (and so cannot close) or names a critical quantity (which it cannot control from the data). The gap between them is the problem.

## Architecture 1: energy methods and weak solutions

- **Approach**: construct solutions by compactness from the energy bound (Leray-Hopf); bound the singular set (Caffarelli-Kohn-Nirenberg).
- **What it achieves**: global weak existence; the singular set has parabolic Hausdorff measure $\mathcal{P}^1 = 0$.
- **The wall**: the energy is supercritical, so partial regularity is as far as it reaches. CKN stops at dimension $1$ for exactly this reason.
- **Coordinate**: closing the last dimension needs critical control the energy cannot give.

## Architecture 2: conditional regularity criteria

- **Approach**: prove "if a critical quantity is bounded, the solution is smooth," then try to bound it. PSL ($L^p_tL^q_x$, $2/p+3/q\le1$), BKM ($\int\|\omega\|_\infty$), ESS ($L^\infty_tL^3_x$), Constantin-Fefferman (vorticity direction).
- **What it achieves**: sharp, correct continuation criteria at the critical scaling level.
- **The wall**: the energy is supercritical and cannot bound any critical quantity. The missing piece is always the a priori control.
- **Coordinate**: closest to the gap; the geometric vorticity-direction criterion is the most promising place for a structural critical bound (Direction 02).

## Architecture 3: critical spaces and scaling

- **Approach**: work in scale-invariant spaces where small data gives global smooth solutions. Fujita-Kato ($\dot H^{1/2}$), Kato ($L^3$), Koch-Tataru ($\mathrm{BMO}^{-1}$).
- **What it achieves**: global smooth solutions for small critical data; the sharp small-data theory.
- **The wall**: smallness is essential; the fixed-point iteration does not close for large data, and there is no bridge from the supercritical energy to a critical bound.
- **Coordinate**: the boundary between small-data success and the open large-data problem is the supercriticality gap in critical-space language (Direction 03).

## Architecture 4: blow-up and self-similar solutions

- **Approach**: construct a singularity. Leray self-similar profiles; axisymmetric-with-swirl scenarios; the inviscid Euler relative.
- **What it achieves**: exclusions (Leray self-similar ruled out in $L^3$) and barriers (Tao's averaged-NS blow-up); Euler blow-up (Elgindi) and strong numerics (Hou-Luo, Chen-Hou).
- **The wall**: no NS singularity is known; the simplest self-similar route is excluded; Tao's barrier shows energy-plus-scaling is not enough.
- **Coordinate**: NS blow-up, if it exists, must evade the $L^3$ exclusion and live where viscosity is just barely insufficient; the averaged caricature tells the regularity side what structure to exploit (Direction 04).

## Architecture 5: non-uniqueness via convex integration

- **Approach**: construct many weak solutions to the same data (Buckmaster-Vicol).
- **What it achieves**: non-uniqueness of weak solutions below the Leray-Hopf class; the Albritton-Brue-Colombo forced non-uniqueness in the Leray-Hopf class.
- **The wall**: these are rough solutions below the Onsager threshold; they do not bear on smoothness of the strong flow.
- **Coordinate**: sharpens the solution concept (Leray-Hopf is the right class), outside the regularity discipline (Direction 05).

## The synthesis

A regularity proof must add a coercive, scaling-critical a priori bound using the exact 3D nonlinear structure (vortex stretching, pressure coupling), respecting 2D smoothness, using viscosity, and surviving the averaged-NS barrier. A blow-up proof must construct data evading the $L^3$ self-similar exclusion in a regime where viscosity does not save the flow. See [`../research_atlas/README.md`](../research_atlas/README.md) for the full obstruction map.
