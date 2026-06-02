# Research overview: the state of the art

A research-level orientation across the five candidate proof architectures, with the obstruction each faces stated as a coordinate rather than a verdict.

## The shape of the problem

The Clay problem (Fefferman's statement) asks, for 3D incompressible Navier-Stokes on $\mathbb{R}^3$ or $\mathbb{T}^3$ with $\nu > 0$ and smooth divergence-free finite-energy data, to prove either global existence of a smooth solution or the existence of smooth data leading to finite-time blow-up. Four precise statements are offered; existence-and-smoothness for $\mathbb{R}^3$ or $\mathbb{T}^3$ is the canonical target.

The single organizing fact: the energy inequality is the only coercive bound that holds for all time, and it is supercritical. Closing the gap to a critical regularity statement is the problem. The five architectures are five strategies, and each meets the gap in a characteristic way.

## Architecture 1: energy methods and weak solutions

**What it is.** Construct solutions by compactness (Galerkin) and bound their singularities directly. Leray (1934), Hopf (1951): global weak solutions exist. Caffarelli-Kohn-Nirenberg (1982): the singular set of a suitable weak solution has parabolic Hausdorff dimension at most $1$ (measure $\mathcal{P}^1 = 0$).

**The obstruction.** The method is built on the energy, which is supercritical, so it cannot upgrade "small singular set" to "no singular set." CKN is the best unconditional result and it stops exactly where the supercriticality stops it. **Coordinate**: partial regularity is as far as energy compactness reaches; closing the last dimension needs critical control energy cannot give.

## Architecture 2: conditional regularity criteria

**What it is.** Prove "if a critical quantity is bounded, the solution is smooth," then try to bound that quantity. Prodi-Serrin-Ladyzhenskaya ($L^p_t L^q_x$, $2/p+3/q\le1$), Beale-Kato-Majda ($\int\|\omega\|_\infty\,dt$), Escauriaza-Seregin-Sverak ($L^\infty_t L^3_x$), Constantin-Fefferman (vorticity direction).

**The obstruction.** Every criterion is at the critical scaling level, and the energy is supercritical, so the energy cannot bound any of them. The criteria are sharp and correct; the missing piece is always the a priori control of the critical quantity. **Coordinate**: this is the architecture closest to the gap, and the geometric (vorticity-direction) refinements are the most promising place to look for a structural critical bound.

## Architecture 3: critical spaces and scaling

**What it is.** Work in scale-invariant function spaces where small data gives global smooth solutions: Fujita-Kato ($\dot H^{1/2}$, 1964), Kato ($L^3$), Koch-Tataru ($\mathrm{BMO}^{-1}$, 2001, the largest known). Mild solutions via the Duhamel/heat-semigroup formulation and fixed-point iteration.

**The obstruction.** The smallness is essential: the fixed point closes only for small critical data. For large data the iteration does not converge, and there is no mechanism to bootstrap from the supercritical energy to a critical bound. **Coordinate**: the boundary between small-data global existence and the open large-data problem is exactly the supercriticality gap, drawn in critical-space language.

## Architecture 4: blow-up and self-similar solutions

**What it is.** Try to construct a singularity. Leray's self-similar ansatz $u(x,t) = (2a(T-t))^{-1/2} U(x/\sqrt{2a(T-t)})$; modern scenarios (axisymmetric with swirl, the Hou-Luo flow); the inviscid relative (Euler).

**The obstruction (and a barrier).** Leray self-similar blow-up is ruled out in $L^3$ (Necas-Ruzicka-Sverak 1996; Tsai 1998). No NS singularity is known. But Tao (2016) constructed finite-time blow-up for an **averaged** Navier-Stokes that keeps the energy identity and the scaling: a barrier showing that any regularity proof must use more than energy-plus-scaling. On the inviscid side, Elgindi (2021) established Euler blow-up in some settings, and Hou-Luo and Chen-Hou give strong numerical evidence in others. **Coordinate**: blow-up, if it exists for NS, must evade the $L^3$ ruling-out and must be a place where viscosity is not quite enough; the averaged caricature tells the regularity side what structure it must exploit.

## Architecture 5: non-uniqueness via convex integration

**What it is.** Construct many distinct weak solutions to the same data by the Nash-Kuiper / De Lellis-Szekelyhidi convex-integration method, adapted to NS by Buckmaster-Vicol (2019): non-uniqueness of weak solutions in $C_t L^2$ below the Leray-Hopf regularity.

**The obstruction (it is about the solution concept).** These solutions are rough and dissipate or produce energy anomalously; they live below the Onsager-type regularity threshold and are not Leray-Hopf. They show the weak solution concept is too weak to be unique, which sharpens the question to the Leray-Hopf class, but they say nothing about whether the smooth flow stays smooth. **Coordinate**: Leray-Hopf is the right class for the regularity question; the convex-integration phenomena are a different regime, separated by the Onsager threshold, and conflating the two is a category error.

## The synthesis

A proof of global regularity must supply a coercive, scaling-critical a priori bound that uses the exact 3D nonlinear structure (vortex stretching, the precise pressure coupling), respects that 2D is smooth, uses the viscous term, and survives the averaged caricature. A blow-up proof must construct data evading the $L^3$ self-similar exclusion in a regime where viscosity does not save the flow. The architectures map the territory; the research directions ([`research_directions/`](research_directions/)) are the attacks.
