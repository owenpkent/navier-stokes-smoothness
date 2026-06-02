# The researcher mindset

How this project works. Read this first; it defines what counts as progress.

## The problem is a target, not a monument

We are trying to solve the Navier-Stokes existence and smoothness problem. That is the posture. It is one of the hardest open problems in analysis, ninety years of effort by the best people, and the honest odds against any single program are very long. None of that makes it a monument to be admired from a distance. It is a target. We aim at it.

A monument is something you describe. A target is something you try to hit, and when you miss you note exactly where the shot landed so the next one is better. This repo is full of misses recorded as coordinates.

## We advance a front, we do not chase the whole problem at once

The problem decomposes. Regularity is a critical-scaling statement; the energy is supercritical; the gap between them is the front. We do not try to "prove Navier-Stokes" in one move. We try to push the front: map exactly which a priori bounds are available and at what scaling weight, map which regularity criteria are critical, find the smallest piece of genuinely critical control that could be added. Each push is a concrete, checkable piece of work.

## Negative results are coordinates

When an experiment or an argument fails, that is information, not defeat. The supercriticality of the energy is a "failure" in the sense that energy methods cannot close the problem. It is also the single most useful fact in the repo, because it tells us where the proof cannot live and therefore narrows where it can. The same is true of the controls:

- 2D is smooth. A method that ignores vortex stretching fails the 2D control. That failure is a coordinate: the missing control must be 3D-specific.
- Inviscid Burgers and 3D Euler blow up. A method blind to viscosity fails the viscosity control. Coordinate: the control must use $\nu\Delta u$.
- Tao's averaged Navier-Stokes blows up while preserving energy and scaling. Coordinate: the control must use the exact nonlinearity, not energy-plus-scaling.

Read every "this won't work" in this repo as a fence post, not a tombstone. The fences enclose the region where a proof must live.

## Honesty is the engine

The fastest way to waste years is to believe a wrong result. So the discipline is ruthless honesty about status:

- A numerical run that looks like incipient blow-up is not blow-up until it survives a resolution study. Numerics can suggest, never decide.
- An a priori estimate that "controls the solution" is checked by the criticality bookkeeper. If the controlling norm is supercritical, the estimate is insufficient by itself, and we say so.
- A reformulation that makes the problem "look easy" is treated with heightened suspicion, because the measured margin is zero: there is no supercritical slack for a soft argument to exploit. If a clean argument has no obvious hole, we hunt harder for the hidden one.

Honesty is not pessimism. It is the thing that keeps the search pointed at the real gap instead of a comfortable mirage.

## Reformulation must import power

There are many equivalent formulations of the problem (energy, vorticity, critical spaces, weak solutions, mild solutions). Switching formulations is only progress if the new formulation imports genuinely new control. Restating the supercritical energy bound in a new norm that is still supercritical is not progress; it is the same wall repainted. A reformulation earns its keep only when it makes a critical (scale-invariant) quantity controllable, or when it exposes structure (anisotropy, vorticity coherence, the exact form of the stretching term) that the energy formulation hides.

## Build the ladder

The work is organized as a ladder of attackable milestones (the research directions), each smaller than "solve the problem" and each a real contribution if reached. Mapping the conditional-criteria landscape onto the criticality coordinate is a rung. A logarithmic improvement of a Prodi-Serrin endpoint is a rung. A clean Lean statement of the energy inequality is a rung. We climb rungs. We do not wait for a single leap.

## The AI-augmented research group

This repo is structured so that specialized agents (surveyor, builder, verifier, adversary, synthesizer, orchestrator) can run the loop: survey the literature, propose an estimate, attack it with the three controls, formalize what survives, record the coordinate. The owner is in the critical path for direction and for any claimed proof or blow-up. The compounding effect across many honest, small, checked steps is the bet.
