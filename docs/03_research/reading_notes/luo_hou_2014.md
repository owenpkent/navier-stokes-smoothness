# Reading notes: Luo-Hou (2014), the boundary-driven axisymmetric Euler singularity, with the Chen-Hou (2022-2025) computer-assisted proof

Guo Luo, Thomas Y. Hou, "Potentially singular solutions of the 3D axisymmetric Euler equations," Proc. Natl. Acad. Sci. USA 111, no. 36 (2014), 12968-12973.

Guo Luo, Thomas Y. Hou, "Toward the finite-time blowup of the 3D axisymmetric Euler equations: a numerical investigation," Multiscale Model. Simul. (SIAM) 12, no. 4 (2014), 1722-1776.

Jiajie Chen, Thomas Y. Hou, "Stable nearly self-similar blowup of the 2D Boussinesq and 3D Euler equations with smooth data I: Analysis," arXiv:2210.07191 (2022, rev. 2023); "... II: Rigorous Numerics," Multiscale Model. Simul. (SIAM) (2025), arXiv:2305.05660. DOI 10.1137/23M1580395.

Yongji Wang, Ching-Yao Lai, Javier Gomez-Serrano, Tristan Buckmaster, "Asymptotic self-similar blow-up profile for three-dimensional axisymmetric Euler equations using neural networks," Phys. Rev. Lett. 130 (2023), 244002.

> This is the inviscid blow-up dossier. Luo-Hou (2014) is the high-resolution numerical discovery of a finite-time singularity scenario for the 3D axisymmetric incompressible Euler equations in a cylinder: a hyperbolic stagnation-point flow pinned against a solid boundary ring drives sustained vortex stretching that the numerics carry, with sharp scaling diagnostics, all the way to an apparent blow-up. Chen-Hou (2022-2025) turn the scenario into a rigorous computer-assisted proof of finite-time singularity for the closely related 2D Boussinesq system and for 3D axisymmetric Euler with a boundary, with smooth finite-energy data, by proving nonlinear stability of an approximate self-similar profile. Wang-Lai-Gomez-Serrano-Buckmaster (2023) supply, in parallel, a physics-informed neural-network construction of smooth self-similar profiles, including unstable ones. This is Architecture 4 (blow-up and self-similar solutions) acting in the affirmative for the inviscid equation, and it is the single sharpest realization of structural control C: the 3D vortex-stretching mechanism $\omega\cdot\nabla u$ genuinely produces singularities when there is no viscosity. The load-bearing lesson for Navier-Stokes is therefore precise. The stretching engine is real and the inviscid flow blows up, so any proof of NS global regularity must come from the viscous term $\nu\Delta u$ beating that stretching, not from any soft feature shared by Euler. These works do not blow up NS. They sharpen the viscosity question to its exact form: does $\nu\Delta u$ defeat $\omega\cdot\nabla u$, or not?

## The equations and the scenario

The setting is the 3D incompressible Euler equations in axisymmetric form on a cylinder $D = \{(r,z): 0 \le r \le 1\}$ with periodicity in $z$ and a solid wall at $r = 1$ (a no-flow boundary $u_r = 0$ there). In axisymmetric variables the natural unknowns are the angular components

$$u_1 = u^\theta / r, \qquad \omega_1 = \omega^\theta / r, \qquad \psi_1 = \psi^\theta / r,$$

where $u^\theta, \omega^\theta, \psi^\theta$ are the swirl velocity, swirl vorticity, and swirl stream function. The equations of motion (no swirl in the poloidal stream function, swirl carried by $u_1$) are

$$\partial_t u_1 + u^r \partial_r u_1 + u^z \partial_z u_1 = 2\, u_1 \psi_{1,z},$$
$$\partial_t \omega_1 + u^r \partial_r \omega_1 + u^z \partial_z \omega_1 = \left(u_1^2\right)_z,$$
$$-\left(\partial_r^2 + \tfrac{3}{r}\partial_r + \partial_z^2\right)\psi_1 = \omega_1, \qquad u^r = -r\,\psi_{1,z}, \quad u^z = 2\psi_1 + r\,\psi_{1,r}.$$

The term $\left(u_1^2\right)_z$ in the $\omega_1$ equation is the axisymmetric face of 3D vortex stretching $\omega\cdot\nabla u$. It is exactly the term that is absent in 2D Navier-Stokes and the term the project identifies as the engine of any genuine 3D blow-up. The structural point of the Hou-Luo scenario is geometric: the singularity does not form in the interior but on the boundary ring $r = 1$, where the no-flow wall forces a hyperbolic (saddle) stagnation-point flow in the $(r,z)$ plane. The hyperbolic flow compresses the vorticity into a thin layer against the wall and along a symmetry plane, and the compression sustains the stretching $\left(u_1^2\right)_z$ long enough to drive $\|\omega\|_{L^\infty}$ to infinity in finite time. The wall is essential to the mechanism: it pins the stagnation point and prevents the structure from translating away, so the stretching does not get advected out of the danger zone.

## What it proves

### Luo-Hou (2014): the numerical evidence

The two 2014 papers (the PNAS announcement and the long Multiscale Model. Simul. companion) are numerical, not a theorem. They report a direct numerical simulation of axisymmetric Euler in the cylinder, with a specially designed adaptive (moving) mesh achieving an effective resolution reported up to roughly $(3 \times 10^{12})$ mesh points near the singularity (a $131072 \times 131072$ adaptive grid in the reported runs), resolving the focusing region to scales on the order of $10^{-15}$ relative to the domain. The diagnostics that constitute the evidence:

- **Maximum vorticity growth consistent with a finite-time singularity.** $\|\omega(\cdot,t)\|_{L^\infty}$ grows double-exponentially and, near the apparent singular time $T_*$, fits the inverse-power law

$$\|\omega(\cdot,t)\|_{L^\infty} \sim \frac{c}{(T_* - t)}, \qquad t \to T_*^-,$$

with $T_* \approx 0.0035056$ in their normalization. The exponent very close to $-1$ is the Type I (self-similar) rate.

- **The Beale-Kato-Majda integral diverges.** $\int_0^t \|\omega(\cdot,s)\|_{L^\infty}\, ds \to \infty$ as $t \to T_*$, the BKM continuation criterion (Beale-Kato-Majda 1984) firing, which is the rigorous signature that the smooth solution cannot be continued past $T_*$ if the numerics are faithful. See [`beale_kato_majda_1984.md`](beale_kato_majda_1984.md).

- **A locally self-similar focusing structure.** Near the boundary point the solution rescales onto an approximately self-similar profile with definite scaling exponents (the spatial focusing scale shrinks like a power of $(T_* - t)$), and the vorticity vector direction stays well-organized (no loss of regularity of the direction field), so the scenario survives the geometric depletion criteria (Constantin-Fefferman 1993; Constantin-Fefferman-Majda 1996; Deng-Hou-Yu non-blowup criteria) that rule out many earlier candidate singularities. See [`constantin_fefferman_1993.md`](constantin_fefferman_1993.md).

The honest status of the 2014 work in this dossier: it is **potential** blow-up, numerically supported. It establishes a credible, geometrically robust scenario and the scaling diagnostics, and it passed the known non-blowup screens, but it is not a proof.

### Chen-Hou (2022-2025): the rigorous computer-assisted proof

Chen and Hou convert the scenario into theorems. They prove finite-time singularity rigorously for two systems whose blow-up is governed by the same boundary-driven mechanism.

**Theorem (Chen-Hou, 2D Boussinesq with boundary).** There exist smooth, finite-energy initial data for the 2D Boussinesq equations on the half-space (or a domain with a boundary) such that the unique local smooth solution develops a finite-time singularity. The blow-up is **stable** (it persists under small smooth perturbations of the data) and is **nearly self-similar**: the rescaled solution converges to an approximate self-similar profile, with $\|\omega(\cdot,t)\|_{L^\infty}$ and the temperature gradient blowing up at a definite rate as $t \to T_*$.

**Theorem (Chen-Hou, 3D axisymmetric Euler with boundary).** The same conclusion holds for the 3D axisymmetric Euler equations with a solid boundary and smooth finite-energy initial data: finite-time blow-up, stable, nearly self-similar, of exactly the Hou-Luo type. (The Boussinesq result is the engine; the 2D Boussinesq system is the formal $r \to \infty$ analog of axisymmetric Euler away from the axis, and the boundary case transfers.)

The 2D Boussinesq system here is

$$\partial_t \omega + u\cdot\nabla\omega = \theta_x, \qquad \partial_t \theta + u\cdot\nabla\theta = 0, \qquad u = \nabla^\perp(-\Delta)^{-1}\omega,$$

with $\theta$ the density/temperature. The forcing $\theta_x$ plays the role of $\left(u_1^2\right)_z$: it is the formal analog of vortex stretching, and it is what is absent in plain 2D Euler (which is globally smooth, Wolibner/Yudovich). This is why Boussinesq, not 2D Euler, is the right model: Boussinesq retains a stretching-like source and the boundary mechanism, and it genuinely blows up.

**Method of proof (structure).** The proof is a nonlinear-stability argument around a numerically constructed approximate self-similar profile $\bar U$, with all approximation errors controlled by rigorous (interval-arithmetic) numerics. The skeleton:

1. **Dynamic rescaling.** Pass to self-similar variables $(\xi, \tau)$ with a time-dependent scaling $\xi = x / \lambda(t)$, $\tau = \int_0^t \lambda(s)^{-1} ds$ chosen dynamically so the rescaled solution is order one. The Euler/Boussinesq PDE becomes an evolution for the rescaled profile with a self-similar drift term carrying the scaling rates $(c_\omega, c_l)$ (the analogs of the drift $a(U + (y\cdot\nabla)U)$ in the Leray ansatz; see [`necas_ruzicka_sverak_1996.md`](necas_ruzicka_sverak_1996.md)).

2. **An approximate steady profile $\bar U$.** Construct, numerically, an approximate fixed point of the rescaled equation: a smooth approximate self-similar profile with a small, explicitly bounded residual.

3. **Linearized stability with a coercive energy.** Linearize the rescaled dynamics around $\bar U$ and prove the linearized operator is stable in a carefully designed weighted norm. The technical heart is a pair of **weighted $L^\infty$ and weighted Holder ($C^{1/2}$) norms**, with weights singular at the origin that capture the focusing geometry, plus **sharp functional inequalities** (singular-kernel estimates proved with symmetry of the Biot-Savart kernel and optimal-transport techniques) to control the nonlocal velocity in those norms.

4. **Nonlinear closure by rigorous numerics.** The residual of $\bar U$ and the constants in the functional inequalities are all bounded with computer-assisted interval arithmetic (this is the content of Part II, the "Rigorous Numerics" paper). The smallness of the residual against the spectral gap of the linearized operator closes a Gronwall/bootstrap estimate: the true rescaled solution stays close to $\bar U$ for all rescaled time, hence blows up in finite physical time. Stability is built in because the argument controls a neighborhood, not a single trajectory.

The proof is rigorous and complete modulo the verified numerics; it is a theorem, not a simulation.

### Wang-Lai-Gomez-Serrano-Buckmaster (2023): neural-network profiles

In parallel, this group uses physics-informed neural networks (PINNs) to represent the self-similar profile $\bar U$ and the scaling rates as the trainable output of a network, minimizing the PDE residual of the self-similar profile equation directly. They recover smooth asymptotically self-similar blow-up profiles for the Hou-Luo 3D axisymmetric Euler scenario (and for the Cordoba-Cordoba-Fontelos / incompressible porous media, IPM, model). The notable contribution is **unstable** profiles: by not restricting to the dynamically stable manifold, the PINN finds self-similar solutions a forward-in-time simulation would never see. This is the ML-assisted route to candidate blow-up data; it produces high-accuracy profiles but, by itself, not a proof (the profiles feed, in principle, into a Chen-Hou-style rigorous stability argument).

## Method / structure (the shared mechanism, at the lemma level)

The common engine across all four works is **hyperbolic-flow-driven sustained vortex stretching against a boundary**, and it is worth isolating what makes it work and why viscosity is the only thing that could stop it.

- **The stretching term is a genuine source, not a transport.** In the $\omega_1$ equation the right side $\left(u_1^2\right)_z$ (Euler) or $\theta_x$ (Boussinesq) is a production term: it can grow $\omega_1$ even as transport moves it around. This is the structural difference from 2D Euler/NS, where the vorticity equation has no source and $\|\omega\|_{L^\infty}$ is bounded by the maximum principle for all time.

- **The hyperbolic boundary flow sustains the source.** The no-flow wall at $r = 1$ and the symmetry across $z = 0$ create a saddle-point velocity field $(u^r, u^z)$ with a stable and an unstable manifold meeting at the boundary point. Fluid is compressed toward the point along one direction and ejected along the other; the compression keeps the stretching active and the structure pinned. Without the wall the stagnation structure would translate and the stretching would not focus.

- **The self-similar profile is the fixed point of focusing-against-stretching.** As the vorticity focuses, the velocity gradient at the point grows; the growing gradient feeds back into faster focusing. The balance is a self-similar profile: the solution reproduces itself at scale $\lambda(t) \sim (T_* - t)^{c_l}$ with amplitude $\sim (T_* - t)^{-1}$. The Chen-Hou theorem is precisely that this fixed point exists, is approximately the numerically computed $\bar U$, and is dynamically stable.

- **Why this is rigorous now and was not in 2014.** The 2014 work computed the trajectory; the 2022-2025 work proves the trajectory is trapped near a fixed point. The new ingredients are the weighted $L^\infty \cap C^{1/2}$ functional framework (which makes the linearized operator coercive despite the nonlocal Biot-Savart law) and verified interval arithmetic (which makes the residual and constants honest). This is the same shape of argument as a Lyapunov/spectral-gap proof, computer-assisted at the two places (residual, constants) where closed-form bounds are out of reach.

## Criticality placement

The relevant scaling here is the **Euler** scaling, which is the inviscid case of the NS scaling $u_\lambda(x,t) = \lambda\, u(\lambda x, \lambda^2 t)$. Euler is invariant under the one-parameter family $u_\mu(x,t) = \mu^{a-1} u(\mu^{-a} \cdot, \cdot)$ for any focusing exponent (the inviscid scaling is two-parameter, not one-parameter, precisely because there is no viscosity to fix the parabolic relation between space and time scales). This extra freedom is exactly why Euler can blow up and is the cleanest statement of the supercriticality issue.

- **Vorticity magnitude is supercritical for Euler.** Under the NS scaling the vorticity $\omega = \nabla\times u$ has $\omega_\lambda = \lambda^2\, \omega(\lambda x, \lambda^2 t)$, so $\|\omega\|_{L^\infty}$ has scaling exponent $-2$ in the bookkeeper sense (it is **supercritical**: it grows under focusing $\lambda \to \infty$). The blow-up is the statement that this supercritical quantity is uncontrolled. The only Euler quantity with a sign-definite a priori bound is the energy $\tfrac12\|u\|_{L^2}^2$ (conserved, not just bounded), and the energy is **supercritical**: `lebesgue_exponent(2, 3)` $= 1 - 3/2 = -1/2 < 0$ in `experiments/_shared/criticality.py`. Conserved energy is compatible with $\|\omega\|_{L^\infty} \to \infty$ because the blow-up concentrates in a region of vanishing volume. This is the same supercriticality gap (control B) the project flags for NS, displayed in the cleanest possible setting: for Euler the gap is not a gap, it is an actual singularity.

- **The blow-up rate sits at Type I (self-similar).** The reported rate $\|\omega\|_{L^\infty} \sim (T_* - t)^{-1}$ is the borderline self-similar (Type I) rate. For NS, Type I (self-similar-rate) singularities are excluded by the Caffarelli-Kohn-Nirenberg / Seregin-type local-energy arguments under suitable bounds and are constrained by the ESS / quantitative-regularity program at the critical $L^3$ level. For Euler there is no such exclusion, and Chen-Hou realize the Type I rate. The contrast is the whole point: the viscous parabolic scaling is what would, if it could, force the focusing exponent and rule out Type I; inviscid, nothing does.

- **The boundary breaks scale invariance but not the focusing.** The wall at $r = 1$ is not scale-invariant, so the global solution is not exactly self-similar; the blow-up is "nearly" self-similar (asymptotically self-similar in the focusing limit). The criticality bookkeeper still reads the local focusing region as critical-to-supercritical: locally the solution rescales onto a critical-amplitude profile, and the supercritical $\|\omega\|_{L^\infty}$ runs away.

## Against the three controls

- **(A) 2D control.** This is the case where control A is most informative, and the works pass it correctly. The blow-up uses 3D vortex stretching $\omega\cdot\nabla u$ essentially: the axisymmetric source $\left(u_1^2\right)_z$ (3D Euler) and its analog $\theta_x$ (Boussinesq) are exactly the terms with no 2D counterpart. Plain 2D Euler and 2D NS have no such source (vorticity is transported, $\|\omega\|_{L^\infty}$ bounded by the maximum principle), and they do not blow up; the Chen-Hou method does **not** apply to them, because the system it analyzes has the production term. This is the positive content of control A from the blow-up side: the singularity lives exactly where 3D differs from 2D. A would-be NS regularity proof that did not engage this term would be predicting 2D-style behavior and would be wrong; the Hou-Luo scenario is the witness that the term is dangerous.

- **(B) Supercriticality.** The blow-up is the supercritical quantity ($\|\omega\|_{L^\infty}$, exponent $-2$) escaping while the only coercive bound (energy, exponent $-1/2$) stays satisfied. This is control B made concrete: energy-level conservation does not prevent singularity formation, because the singularity hides in vanishing volume. For NS the same energy bound is the only global one and is equally supercritical; the difference is that NS additionally has the viscous dissipation $\nu\int\|\nabla u\|_{L^2}^2$, still supercritical but a genuine smoothing the Euler flow lacks. The dossier's reading: Euler blow-up shows that closing the supercriticality gap is not optional and cannot be done at the energy level; for NS it must be done by the viscous term adding control the energy alone does not.

- **(C) Viscosity / Burgers.** This is the control these works exist to sharpen, and it is the reason they belong together in one dossier. The Hou-Luo singularity is **inviscid**. The entire question for Navier-Stokes is whether $\nu\Delta u$ defeats the stretching that drives this Euler blow-up. The works make that question exact: the stretching mechanism is real, geometrically robust, stable, and now (Chen-Hou) rigorously proven to produce a singularity for the inviscid equation with a boundary. So the NS regularity problem is precisely the contest between the supercritical stretching engine (which wins for Euler) and the viscous dissipation. A method blind to viscosity cannot distinguish NS from Euler and would predict NS blow-up; control C says such a method is wrong, and the Hou-Luo scenario is the cleanest demonstration that the inviscid side really does blow up. The Burgers control ([`burgers_shock`](../../../experiments/burgers_shock/)) and Elgindi's $C^{1,\alpha}$ Euler singularity (Elgindi 2021) are the same lesson at lower complexity; Hou-Luo / Chen-Hou is the lesson at full 3D incompressible strength with a smooth, physically natural scenario.

## What it gives / what it does not give

**What it gives.**

- A geometrically robust, stable, and (for Boussinesq and boundary-Euler) **rigorously proven** finite-time singularity for the inviscid equations, driven by the exact 3D stretching term. This converts "does the stretching engine actually produce singularities?" from open to **yes, for Euler with a boundary**.
- The sharpest possible form of control C: it pins the NS regularity question to a single contest, viscous dissipation versus supercritical stretching, and shows the stretching wins absent viscosity.
- A template (dynamic rescaling + weighted $L^\infty \cap C^{1/2}$ stability + rigorous numerics) that is now the state of the art for proving blow-up in fluid equations, and a parallel ML template (PINNs) for discovering candidate profiles including unstable ones.
- A concrete target for the viscous problem: the same scenario **with viscosity added** (axisymmetric NS in the cylinder, Hou-Luo geometry) is the natural test of whether $\nu\Delta u$ regularizes. Numerically and heuristically, viscosity appears to defeat this particular focusing (the singular layer is smoothed before it can run away), which is the project's expectation, but there is no theorem.

**What it does not give (the gap to NS regularity).**

- **It is Euler, not Navier-Stokes.** Nothing here blows up NS, and nothing here proves NS stays smooth. The result is a sharpening of the question, not an answer to it. The viscous version of the Hou-Luo scenario is open: it is believed (and numerically supported) that viscosity defeats this specific singularity, but that belief is not a theorem and, even granted, would address one scenario, not all.
- **It does not supply a coercive critical NS bound.** Like every Architecture 4 entry, it produces no global-in-time critical-or-subcritical a priori bound for NS. The supercriticality gap (control B) for the viscous problem is untouched; if anything the result emphasizes how much the viscous term must do.
- **It is computer-assisted for the rigorous part.** The Chen-Hou theorem depends on verified interval-arithmetic numerics for the residual of $\bar U$ and the functional-inequality constants. This is a fully accepted mode of rigorous proof (as in Hales' Kepler proof and Gonzalez-Tomei-Hou-type CAPs), and the proof is a theorem, but it is not a closed-form argument, and the NS analog (if attempted) would inherit the same dependence. (verify: the precise reliance is on Part II's rigorous numerics; the analysis in Part I reduces blow-up to finitely many verifiable inequalities.)
- **The exact blow-up rate and profile are scenario-specific.** The $(T_* - t)^{-1}$ rate and the specific weighted norms are tuned to this geometry; they do not transfer mechanically to other candidate singularities (interior, no-boundary, or NS).

The honest one-line summary for the spine: Luo-Hou plus Chen-Hou prove the stretching engine really does produce a finite-time singularity for inviscid 3D flow with a boundary, which converts the NS regularity problem into the sharp question "does $\nu\Delta u$ beat $\omega\cdot\nabla u$?", and leaves that question open.

## Lineage and sharpest known form

**Builds on.**

- The Beale-Kato-Majda criterion (Beale-Kato-Majda 1984): the rigorous BKM integral $\int_0^t\|\omega\|_{L^\infty}$ is the quantity Luo-Hou track to certify the singularity. See [`beale_kato_majda_1984.md`](beale_kato_majda_1984.md).
- The geometric non-blowup criteria (Constantin-Fefferman 1993; Constantin-Fefferman-Majda 1996; Deng-Hou-Yu): the screens that earlier candidate Euler singularities failed and that the Hou-Luo scenario passes, because the vorticity direction stays regular. See [`constantin_fefferman_1993.md`](constantin_fefferman_1993.md).
- The Hou-Luo model / 1D models (Choi-Kiselev-Yao; Choi-Hou-Kiselev-Nadirashvili-Sverak-Yao 2017; the De Gregorio and Constantin-Lax-Majda models): simplified 1D caricatures of the boundary scenario that were proven to blow up first and guided the profile analysis. Hou-Luo (the model) is the 1D reduction; Chen-Hou's "Exact self-similar finite-time blowup of the Hou-Luo model with smooth profiles" (arXiv:2308.01528) is a 2023 companion at the model level.
- The Leray self-similar tradition (Leray 1934; Necas-Ruzicka-Sverak 1996; Tsai 1998): the self-similar ansatz and the dynamic-rescaling viewpoint, here applied affirmatively to Euler rather than as an exclusion for NS. See [`necas_ruzicka_sverak_1996.md`](necas_ruzicka_sverak_1996.md).

**Built on it / parallel developments through 2025.**

- **Elgindi (2021):** finite-time singularity for axisymmetric **$C^{1,\alpha}$** Euler on $\mathbb{R}^3$ without swirl, via a fundamentally different (low-regularity, exact self-similar profile) mechanism. Elgindi proves a rigorous Euler singularity for non-smooth ($C^{1,\alpha}$) data; Chen-Hou prove one for **smooth** data **with boundary**. The two together establish that 3D Euler singularity is not an artifact of either roughness or a contrived domain. T. Elgindi, "Finite-time singularity formation for $C^{1,\alpha}$ solutions to the incompressible Euler equations on $\mathbb{R}^3$," Ann. of Math. 194 (2021), 647-727.
- **Chen-Hou (2022-2025):** the rigorous computer-assisted proof itself, Parts I (Analysis, arXiv:2210.07191) and II (Rigorous Numerics, Multiscale Model. Simul. / SIAM, 2025, arXiv:2305.05660). This is the headline rigorous result and the current state of the art on the Hou-Luo scenario.
- **Wang-Lai-Gomez-Serrano-Buckmaster (2023):** PINN-discovered self-similar profiles for axisymmetric Euler and IPM, including unstable ones; the ML route to candidate data. Phys. Rev. Lett. 130 (2023), 244002.
- **Cordoba-Martinez-Zoroa and related (2023-2025):** further rigorous and numerical work on Euler and related active-scalar singularities (SQG, IPM, Boussinesq without boundary), extending the catalogue of inviscid singularities. (verify: specific 2024-2025 citations.)

**Sharpest known form (2025).** For the inviscid equations: 3D axisymmetric Euler with a solid boundary and smooth finite-energy data has a stable, nearly self-similar finite-time singularity (Chen-Hou, rigorous, computer-assisted); 3D axisymmetric Euler on $\mathbb{R}^3$ has a finite-time singularity for $C^{1,\alpha}$ data (Elgindi, rigorous, closed-form). 2D Boussinesq with boundary blows up for smooth data (Chen-Hou). For the **viscous** equation: the corresponding NS regularity question is open; the prevailing numerical and heuristic evidence is that viscosity defeats the specific Hou-Luo focusing, but there is no theorem either way, and the supercriticality gap that the Euler singularity exposes is exactly the gap a viscous proof must close.

## References

- G. Luo, T. Y. Hou, "Potentially singular solutions of the 3D axisymmetric Euler equations," Proceedings of the National Academy of Sciences USA 111, no. 36 (2014), 12968-12973. DOI 10.1073/pnas.1405238111.
- G. Luo, T. Y. Hou, "Toward the finite-time blowup of the 3D axisymmetric Euler equations: a numerical investigation," Multiscale Modeling and Simulation (SIAM) 12, no. 4 (2014), 1722-1776. DOI 10.1137/140966411.
- J. Chen, T. Y. Hou, "Stable nearly self-similar blowup of the 2D Boussinesq and 3D Euler equations with smooth data I: Analysis," arXiv:2210.07191 (2022, rev. 2023).
- J. Chen, T. Y. Hou, "Stable nearly self-similar blowup of the 2D Boussinesq and 3D Euler equations with smooth data II: Rigorous Numerics," Multiscale Modeling and Simulation (SIAM) (2025), arXiv:2305.05660. DOI 10.1137/23M1580395.
- J. Chen, T. Y. Hou, "Exact self-similar finite-time blowup of the Hou-Luo model with smooth profiles," arXiv:2308.01528 (2023).
- Y. Wang, C.-Y. Lai, J. Gomez-Serrano, T. Buckmaster, "Asymptotic self-similar blow-up profile for three-dimensional axisymmetric Euler equations using neural networks," Physical Review Letters 130 (2023), 244002. DOI 10.1103/PhysRevLett.130.244002.
- J. T. Beale, T. Kato, A. Majda, "Remarks on the breakdown of smooth solutions for the 3-D Euler equations," Communications in Mathematical Physics 94, no. 1 (1984), 61-66.
- P. Constantin, C. Fefferman, "Direction of vorticity and the problem of global regularity for the Navier-Stokes equations," Indiana University Mathematics Journal 42, no. 3 (1993), 775-789.
- T. Elgindi, "Finite-time singularity formation for $C^{1,\alpha}$ solutions to the incompressible Euler equations on $\mathbb{R}^3$," Annals of Mathematics 194, no. 3 (2021), 647-727.
- J. Leray, "Sur le mouvement d'un liquide visqueux emplissant l'espace," Acta Mathematica 63 (1934), 193-248.

## Cross-links

- Primary direction: [`04_blowup_and_barriers.md`](../research_directions/04_blowup_and_barriers.md). This is the "Euler blow-up is real" entry; the note supplies the boundary-driven stretching mechanism, the scaling diagnostics, the Chen-Hou rigorous theorem, and the exact form in which it sharpens the viscosity question.
- Vorticity geometry: [`02_vorticity_geometry.md`](../research_directions/02_vorticity_geometry.md). The scenario passes the Constantin-Fefferman direction-of-vorticity screen, which is why it is credible; the stretching term $\omega\cdot\nabla u$ is the engine.
- Supercriticality: [`03_supercriticality_gap.md`](../research_directions/03_supercriticality_gap.md). Euler blow-up is the supercritical $\|\omega\|_{L^\infty}$ escaping while conserved (supercritical) energy stays satisfied; the cleanest display of the gap.
- Sibling notes: [`necas_ruzicka_sverak_1996.md`](necas_ruzicka_sverak_1996.md) (the same self-similar/dynamic-rescaling machinery used as an exclusion for **viscous** backward self-similar blow-up, where viscosity supplies the rigidity Euler lacks), [`beale_kato_majda_1984.md`](beale_kato_majda_1984.md) (the BKM integral that certifies the numerical singularity), [`constantin_fefferman_1993.md`](constantin_fefferman_1993.md) (the geometric screen the scenario passes), [`tao_2016_averaged.md`](tao_2016_averaged.md) (the complementary barrier: a cascade the averaged nonlinearity permits, here a real geometric stretching the true Euler nonlinearity carries to a singularity).
- Experiment tie-in: [`../../../experiments/burgers_shock/`](../../../experiments/burgers_shock/) (the viscosity control at 1D complexity) and the criticality bookkeeper [`../../../experiments/_shared/criticality.py`](../../../experiments/_shared/criticality.py) (flags $\|\omega\|_{L^\infty}$ and energy as supercritical).
