# Reading notes: Tao (2016), averaged Navier-Stokes blow-up

Terence Tao, "Finite time blowup for an averaged three-dimensional Navier-Stokes equation," J. Amer. Math. Soc. 29 (2016).

## What it proves

There exists an **averaged** version of the 3D Navier-Stokes equations, with a nonlinearity that is a (carefully constructed) average of the true bilinear NS nonlinearity, the same energy identity, the same scaling symmetry, and the same dimensional structure, that admits a finite-energy smooth solution which blows up in finite time.

This is a **barrier** result, not a result about NS itself. It does not prove NS blows up. It proves that any method for ruling out NS blow-up must use a feature of the NS nonlinearity that the averaging destroys.

## Structural content

- **The averaged nonlinearity.** Tao replaces the bilinear term $B(u,u) = \mathbb{P}(u\cdot\nabla u)$ by an averaged bilinear operator $\tilde B(u,u)$ built from Fourier multipliers and rotations. It is engineered to (i) preserve the cancellation that gives the energy identity ($\langle \tilde B(u,u), u\rangle = 0$), (ii) preserve the scaling, and (iii) support a specific dynamical mechanism.
- **The self-replicating cascade.** The averaged dynamics is designed so a "blowup machine" (a quasi-periodic, self-similar transfer of energy to a sequence of higher and higher frequency modes) operates: energy moves to scale $2^n$ at time $T_n$, with $T_n \to T_* < \infty$, concentrating into a singularity. Tao calls this a von-Neumann-machine / self-replicator embedded in the nonlinearity.
- **Why the energy identity does not stop it.** The cascade conserves total energy at each transfer; the energy budget is satisfied throughout. The blow-up is in the higher norms (the $H^s$ for $s$ large), exactly the small-scale information the supercritical energy does not see.

## The lesson, stated as a requirement

Any proof of NS global regularity must use a property of the **exact** NS nonlinearity that is **not** shared by the averaged caricature. Candidate distinguishing features: the precise local/pointwise structure of $u\cdot\nabla u$ (the averaging delocalizes it), the divergence-free transport structure, the exact pressure coupling, or a monotone quantity that the averaging breaks. A regularity argument that uses only the energy identity and the scaling cannot work, because $\tilde B$ has both.

## How it bears on the spine

This is the most important "negative" result for orienting the regularity side. It is the analog of a sharp counterexample: it removes the entire class of soft arguments (energy plus scaling) at one stroke, and it is the basis for the criticality bookkeeper's INSUFFICIENT_BY_ITSELF verdict on supercritical estimates. Direction 03 (attack the supercriticality gap) is explicitly disciplined by the Tao barrier: any candidate critical quantity must fail to be monotone for the averaged system, i.e. must engage the exact nonlinearity. See [`../research_directions/03_supercriticality_gap.md`](../research_directions/03_supercriticality_gap.md) and LEARNINGS #7.
