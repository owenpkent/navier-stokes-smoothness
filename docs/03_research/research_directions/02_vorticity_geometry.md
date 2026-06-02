# Direction 02: vorticity-direction and geometric regularity

Architecture 2 (conditional criteria), the geometric branch. This is flagged across the repo as the most promising place to look for a structural critical control.

## The bet

The danger in 3D is vortex stretching $(\omega \cdot \nabla) u$. Constantin-Fefferman (1993) proved that stretching is harmless wherever the **direction** of the vorticity is coherent: if $\xi = \omega/|\omega|$ is Lipschitz in space in the region where $|\omega|$ is large, the solution stays regular. This is a scale-aware geometric condition, not a magnitude bound, and it uses the geometry of stretching directly. The bet: relax the coherence hypothesis toward criticality, or replace it with a quantity controllable from the data.

## Why this is the lead

Most regularity criteria bound a magnitude (a norm of $u$ or $\omega$). The geometric criterion bounds a **direction**, which is dimensionless and therefore automatically scale aware. It is the criterion that most directly encodes "stretching is dangerous only when vortex lines align," which is the physical mechanism. It also automatically respects the 2D control: in 2D the vorticity direction is constant (out of the plane), so the condition is trivially satisfied, exactly matching the fact that 2D is regular.

## Concrete targets

1. **Map the coherence-condition lineage.** Constantin-Fefferman (1993), then Beirao da Veiga-Berselli, then the Hölder-direction relaxations, then the recent quantitative versions. Build a table of how weak the coherence hypothesis can be made.
2. **Local vs global coherence.** The condition is local (where $|\omega|$ is large). Map what is known about whether local coherence can be propagated, and whether DNS of near-singular flows shows the vorticity direction staying coherent or buckling.
3. **Numerical probe.** In the Taylor-Green and Hou-Luo scenarios, measure the Lipschitz seminorm of $\xi = \omega/|\omega|$ in the high-vorticity region as a function of time and resolution. Does it stay bounded (regular per CF) or grow?

## Method

- Survey the geometric-regularity literature with the criticality bookkeeper applied to each variant.
- Add a vorticity-direction diagnostic to the `Flow3D` solver: compute $\xi$ and its spatial gradient in the high-$|\omega|$ region.
- Compare the coherence diagnostic against the BKM integral in the same runs.

## Success criteria

- A table of geometric regularity criteria ordered by strength of hypothesis, each placed on the criticality scale.
- A working vorticity-direction-coherence diagnostic in the solver and a first measurement on the Taylor-Green flow.

## Controls this must pass

- **2D**: the condition must be trivial in 2D (constant vorticity direction) and non-trivial in 3D. Constantin-Fefferman passes this by construction, which is part of why it is the lead.
- **Criticality**: the coherence quantity is dimensionless / scale aware; confirm any proposed relaxation stays critical, not supercritical.
- **Viscosity**: the result is for the viscous flow; the analogous Euler statement is more delicate (and Euler can blow up), so be explicit about the role of $\nu$.
