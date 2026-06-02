# Direction 04: blow-up scenarios and the averaged-NS barrier

Architecture 4 (blow-up and self-similar solutions). The other half of the Clay problem: exhibit smooth data leading to finite-time blow-up.

## The bet

Two complementary bets. First, the constructive one: build (or numerically locate) NS initial data that blows up, evading the known exclusions. Second, the structural one: even without an NS example, Tao's 2016 averaged-NS blow-up is a barrier that tells the regularity side exactly what it must use. Extracting that lesson is itself progress.

## What is ruled out and what is not

- **Leray self-similar blow-up is excluded** in $L^3$ (Necas-Ruzicka-Sverak 1996; Tsai 1998): a nontrivial self-similar profile of Leray's form with finite energy does not exist. So any NS blow-up is not of the simplest self-similar type.
- **Discretely self-similar** and more general scenarios are not excluded, and remain open.
- **Tao (2016)** constructed finite-time blow-up for an averaged Navier-Stokes: a system with the same energy identity, the same scaling, and a nonlinearity that is a (carefully chosen) average of the NS nonlinearity. It builds a self-replicating cascade that concentrates energy at finer and finer scales in finite time.
- **Euler (inviscid):** Elgindi (2021) proved finite-time singularity for $C^{1,\alpha}$ axisymmetric Euler without swirl; Hou-Luo (2014) and Chen-Hou give compelling numerics for axisymmetric Euler with boundary.

## Concrete targets

1. **The averaged-NS barrier, made into a requirement.** Read Tao 2016 carefully and state precisely which structural feature of the true NS nonlinearity the averaging destroys (the locality/cancellation that prevents the self-replicating cascade). Turn this into a necessary condition any regularity proof must use. This is the single most valuable output of the direction.
2. **The Hou-Luo / Chen-Hou scenario.** Set up the axisymmetric-with-swirl near-singular flow at coarse resolution; track the BKM integral and the vorticity-direction coherence under refinement (the viscosity control: an apparent divergence that vanishes under refinement is an artifact).
3. **Map the self-similar exclusions.** Tabulate exactly which self-similar classes are excluded (Leray $L^3$) and which remain open (discretely self-similar, the recent Albritton-Brue-Colombo non-uniqueness from a forced self-similar background).

## Method

- Survey and write reading notes on Tao 2016, Necas-Ruzicka-Sverak, Tsai, Elgindi, Hou-Luo, Albritton-Brue-Colombo.
- Implement the Hou-Luo geometry as an axisymmetric solver (a 2D-in-(r,z) reduction) at coarse resolution; this is a TODO experiment.
- Apply the viscosity control rigorously: any near-singular numerics must show resolution-convergent diagnostics before being taken seriously.

## Success criteria

- A precise statement of the structural feature the averaged-NS barrier forbids, phrased as a requirement on any regularity proof.
- A coarse axisymmetric near-singular experiment with resolution-study diagnostics.

## Controls this must pass

- **Viscosity**: this is the central control here. Numerical blow-up evidence is only meaningful if the diagnostic converges under grid refinement; viscosity must not be quietly resolving the singularity that the coarse grid suggests.
- **Self-similar exclusion**: any proposed blow-up must not be a Leray self-similar profile in $L^3$ (excluded).
- **2D**: a blow-up scenario must be genuinely 3D (use swirl / stretching); a mechanism that would also blow up a 2D flow is wrong (2D does not blow up).
