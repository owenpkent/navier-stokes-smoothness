# Reading notes: Beale-Kato-Majda (1984)

J. Thomas Beale, Tosio Kato, Andrew Majda, "Remarks on the breakdown of smooth solutions for the 3-D Euler equations," *Communications in Mathematical Physics* **94** (1984), 61-66.

> The single most-used breakdown criterion in incompressible fluid dynamics. BKM reduces the question "does a smooth solution of 3D Euler (or Navier-Stokes) break down at time $T$?" to the divergence of one scalar, scale-invariant integral, $\int_0^T \|\omega(t)\|_{L^\infty}\,dt$. It is load-bearing for the regularity problem because it isolates the exact quantity the proof must control: not the energy, not a velocity gradient, but the sup-norm of the vorticity, which is precisely the object the 3D vortex-stretching term $\omega\cdot\nabla u$ amplifies and which has no analog growth mechanism in 2D. The result is **Architecture 2** (conditional regularity criteria) and it engages structural controls **(A)** (it lives on the vorticity equation, where the 3D-only stretching term sits) and **(C)** (the criterion is stated for inviscid Euler, where breakdown is genuinely possible, so the gap to NS is exactly the role of viscosity).

## Statement

Let $u$ solve the 3D incompressible Euler equations on $\mathbb{R}^3$ (or $\mathbb{T}^3$),
$$\partial_t u + (u\cdot\nabla) u = -\nabla p, \qquad \nabla\cdot u = 0,$$
with initial data $u_0 \in H^s(\mathbb{R}^3)$, $s \ge 3$ (the classical local well-posedness range; $s>5/2$ suffices for the local theory, and the original paper takes $s\ge 3$). Let $\omega = \nabla\times u$ be the vorticity. Suppose $u$ is a smooth solution on the maximal interval $[0,T)$.

**Theorem (BKM, 1984).** If
$$\int_0^T \|\omega(t)\|_{L^\infty(\mathbb{R}^3)}\, dt < \infty,$$
then $u$ extends to a smooth solution on $[0,T']$ for some $T' > T$; equivalently the $H^s$ norm stays bounded up to and including $T$. Contrapositively, if $T < \infty$ is the first singular time then necessarily
$$\int_0^T \|\omega(t)\|_{L^\infty}\, dt = \infty, \qquad\text{and in particular}\qquad \limsup_{t\to T}\|\omega(t)\|_{L^\infty} = \infty.$$

Two corollaries make the diagnostic sharp:

1. **No milder blow-up is possible.** A solution cannot lose smoothness while $\|\omega\|_{L^\infty}$ remains integrable in time. So the vorticity sup-norm is not merely *a* control; its time integral is the *exact* obstruction. This rules out, for example, a scenario where $\|u\|_{H^s}\to\infty$ but $\omega$ stays bounded.
2. **It transfers to Navier-Stokes.** The same proof applies to the viscous equation
$$\partial_t u + (u\cdot\nabla)u = -\nabla p + \nu\Delta u, \qquad \nabla\cdot u = 0,$$
because the extra term $\nu\Delta u$ only helps: it contributes a non-positive (dissipative) term to the $H^s$ energy estimate. Hence a Navier-Stokes solution that is smooth on $[0,T)$ extends past $T$ provided $\int_0^T\|\omega(t)\|_{L^\infty}\,dt<\infty$. This is the form used throughout the project's DNS thread.

The norms that appear and their scaling class under $u_\lambda(x,t)=\lambda u(\lambda x,\lambda^2 t)$, $\omega_\lambda(x,t)=\lambda^2\omega(\lambda x,\lambda^2 t)$:

| Quantity | Scaling | Class |
|---|---|---|
| $\|\omega(t)\|_{L^\infty}$ | $\sim \lambda^2$ (with $t\mapsto\lambda^2 t$) | pointwise-in-time supercritical, but |
| $\displaystyle\int_0^T \|\omega(t)\|_{L^\infty}\,dt$ | invariant | **critical** (scale invariant) |
| $\|u(t)\|_{H^s}$, $s\ge 3$ | depends on $s$ | subcritical for the local theory |
| $\|\omega(t)\|_{L^2}$ (enstrophy$^{1/2}$) | $\sim\lambda^{1/2}$ | supercritical |

The middle row is the whole point: the *instantaneous* sup-norm scales (it is not by itself scale invariant), but its **time integral** is exactly scale invariant, which is why BKM is the canonical *critical continuation criterion* rather than a subcritical one.

## Method / structure

The proof is a Sobolev energy estimate on the velocity, closed by a logarithmic interpolation inequality that converts a velocity-gradient sup-norm into a vorticity sup-norm. Three pieces:

### 1. The high-norm differential inequality

Apply $D^\alpha$ ($|\alpha|=s$) to the Euler equations, pair with $D^\alpha u$ in $L^2$, and use the divergence-free commutator (Kato-Ponce / Moser) estimates. The transport term $(u\cdot\nabla)u$ produces, after the standard cancellation of the top-order self-transport, a bound controlled by $\|\nabla u\|_{L^\infty}$:
$$\frac{d}{dt}\,\|u(t)\|_{H^s} \;\le\; C_s\,\|\nabla u(t)\|_{L^\infty}\,\|u(t)\|_{H^s}.$$
If one stops here and applies Gronwall, the criterion would read $\int_0^T\|\nabla u\|_{L^\infty}\,dt<\infty$. That is *true* but not sharp, and it is awkward, because $\|\nabla u\|_{L^\infty}$ is not controlled by $\|\omega\|_{L^\infty}$ via Calderon-Zygmund: the map $\omega\mapsto\nabla u$ is a zeroth-order singular integral operator (a Riesz-transform composition through the Biot-Savart law $u = (-\Delta)^{-1}\nabla\times\omega$), and such operators are **not** bounded on $L^\infty$. There is a genuine logarithmic loss. Removing that loss is the content of the paper.

### 2. The Beale-Kato-Majda logarithmic Sobolev inequality

This is the technical engine. For a divergence-free vector field $u$ on $\mathbb{R}^3$ with vorticity $\omega=\nabla\times u$ and $s > 3/2 + 1 = 5/2$ (so that $H^s\hookrightarrow C^1$),
$$\|\nabla u\|_{L^\infty} \;\le\; C\,\Big(1 + \|\omega\|_{L^\infty}\big(1 + \log^+\|u\|_{H^s}\big) + \|\omega\|_{L^2}\Big),$$
where $\log^+ x = \max(\log x, 0)$ and $C=C(s)$. The inequality says: the $L^\infty$ failure of "$\nabla u$ is controlled by $\omega$" is only **logarithmic** in the high Sobolev norm. The $\|\omega\|_{L^2}$ term is the low-frequency piece (in the periodic / decaying setting it is the enstrophy, which is bounded on $[0,T)$); the $\|\omega\|_{L^\infty}(1+\log^+\|u\|_{H^s})$ term is the high-frequency piece, where the borderline non-boundedness of the singular integral on $L^\infty$ is paid for by the logarithm. This is a fluid-dynamics analog of the Brezis-Gallouet-Wainger inequality, specialized to the Biot-Savart structure so that it is the curl (vorticity) and not the full gradient that carries the sup-norm.

### 3. Closing the loop with Gronwall

Insert the log-Sobolev bound into the high-norm inequality. Writing $y(t)=\|u(t)\|_{H^s}$ and $g(t)=\|\omega(t)\|_{L^\infty}$, and absorbing the bounded $\|\omega\|_{L^2}$ and the additive constant, one gets schematically
$$\frac{d}{dt}\,y \;\le\; C\,g\,y\,\big(1 + \log^+ y\big) + C\,y.$$
Set $Y = \log^+ y + e$. Then $\frac{d}{dt}\log Y \le C\,(1+g)$, so
$$Y(t) \le Y(0)\,\exp\!\Big(C\int_0^t (1+g(\tau))\,d\tau\Big),$$
i.e. $\log\|u(t)\|_{H^s}$ is controlled by $\exp\big(C\int_0^t \|\omega\|_{L^\infty}\,d\tau\big)$. A double exponential in the BKM integral, but **finite** as long as that integral is finite. Hence $\|u\|_{H^s}$ cannot blow up before the integral does, which is exactly the theorem. The double-exponential growth is the price of the logarithm and is consistent with the worst-case stretching bounds; it is not believed sharp for typical flows but is structurally honest about how little is controlled.

### Where the 3D structure enters

The vorticity equation in 3D is
$$\partial_t\omega + (u\cdot\nabla)\omega = (\omega\cdot\nabla)u \;(+\,\nu\Delta\omega\ \text{for NS}),$$
and the term $(\omega\cdot\nabla)u$ is **vortex stretching**: it can amplify $|\omega|$ along the flow. BKM does not bound this term; it *certifies its role*. The criterion says: the only way smoothness is lost is if stretching drives $\|\omega\|_{L^\infty}$ to be non-integrable in time. Because the proof routes everything through $\omega$ and through the Biot-Savart reconstruction $u=(-\Delta)^{-1}\nabla\times\omega$, it is intrinsically a statement about the curl, which is where stretching acts.

## Criticality placement

Run the controlling quantity through the criticality bookkeeper (`experiments/_shared/criticality.py`). Under $u_\lambda(x,t)=\lambda u(\lambda x,\lambda^2 t)$ the vorticity obeys $\omega_\lambda(x,t)=\lambda^2\omega(\lambda x,\lambda^2 t)$, so
$$\|\omega_\lambda(\cdot,t)\|_{L^\infty} = \lambda^2\,\|\omega(\cdot,\lambda^2 t)\|_{L^\infty}.$$
Integrating in time over the rescaled window (substitute $\tau=\lambda^2 t$, $d\tau=\lambda^2\,dt$, picking up $\lambda^{-2}$),
$$\int_0^{T/\lambda^2}\|\omega_\lambda(\cdot,t)\|_{L^\infty}\,dt = \lambda^2\cdot\lambda^{-2}\int_0^{T}\|\omega(\cdot,\tau)\|_{L^\infty}\,d\tau = \int_0^{T}\|\omega\|_{L^\infty}\,d\tau.$$
The BKM integral has scaling exponent exactly $0$: it is **critical**, scale invariant. This is the structurally correct place for a sharp continuation criterion to sit. The bookkeeper returns `CRITICAL` for $\int_0^T\|\omega\|_{L^\infty}\,dt$, the same class it returns for the ESS critical norm $\|u\|_{L^\infty_t L^3_x}$ and for $\|u\|_{L^p_tL^q_x}$ on the Prodi-Serrin line $2/p+3/q=1$. (BKM corresponds to the vorticity formulation of the endpoint: $\omega\in L^1_t L^\infty_x$, which matches $u\in L^1_t \dot W^{1,\infty}_x$, on the scaling line $2/p+3/q=1$ at $p=1$.)

**The supercriticality gap (control B), made explicit.** The only coercive global-in-time a priori bound is the energy inequality
$$\tfrac12\|u(t)\|_{L^2}^2 + \nu\int_0^t\|\nabla u\|_{L^2}^2\,d\tau \le \tfrac12\|u_0\|_{L^2}^2,$$
which controls $u\in L^\infty_t L^2_x \cap L^2_t \dot H^1_x$. Both norms are **supercritical** (scaling exponents $-1/2$ and $0$ in the wrong-direction sense catalogued in `scaling_criticality/`). The energy controls $\|\omega\|_{L^2_tL^2_x}$ (since $\|\nabla u\|_{L^2}\approx\|\omega\|_{L^2}$), but BKM needs $\|\omega\|_{L^1_t L^\infty_x}$. The gap from $L^2_tL^2_x$ to $L^1_tL^\infty_x$ is the gap from supercritical to critical, and it is not bridgeable by any Sobolev embedding in the available regularity. **This is the exact sense in which BKM names the target the energy cannot reach.** BKM is not a regularity proof; it is the precise statement of what a regularity proof must additionally control, expressed at the critical level the energy misses.

## Against the three controls

**(A) 2D control: does it use genuine 3D structure, and is it vacuous in 2D?** Yes and yes, in the most diagnostic possible way. In 2D the vorticity is a scalar $\omega$ transported with diffusion, $\partial_t\omega+(u\cdot\nabla)\omega=\nu\Delta\omega$ (NS) or $\partial_t\omega+(u\cdot\nabla)\omega=0$ (Euler), with **no stretching term**: $(\omega\cdot\nabla)u\equiv 0$ because $\omega$ points out of the plane and $u$ has no out-of-plane gradient component to stretch it. For 2D Euler, transport along a measure-preserving flow gives $\|\omega(t)\|_{L^\infty}=\|\omega_0\|_{L^\infty}$ exactly (it is conserved), so $\int_0^T\|\omega\|_{L^\infty}\,dt = T\|\omega_0\|_{L^\infty}<\infty$ for all finite $T$, and BKM *immediately* yields global smoothness. The criterion is therefore **non-trivial only in 3D**, where stretching can make $\|\omega\|_{L^\infty}$ grow. A method that would predict 2D blow-up could not satisfy BKM, because BKM is automatically satisfied in 2D. BKM passes control (A) by construction: it is built on the very term ($\omega\cdot\nabla u$) whose absence is why 2D is smooth.

**(B) Supercriticality ceiling: is it energy-supercritical?** BKM's controlling quantity is **critical**, not supercritical, which is the good news; that is the right level. The honest accounting (see Criticality placement) is that the energy supplies only supercritical control of $\omega$ ($L^2_tL^2_x$), so BKM does not become a closed theorem when combined with the energy. BKM passes control (B) in the sense that it correctly identifies a *critical* target rather than dressing up the energy; it does not by itself close the gap, and the project records it as `INSUFFICIENT_BY_ITSELF` for exactly this reason. It is a compass, not a proof: it points at $L^1_tL^\infty_x$ control of vorticity as the missing input.

**(C) Viscosity / Burgers control: is it blind to viscosity?** BKM is *deliberately* stated first for inviscid Euler, where breakdown is genuinely possible and is an active research question (Elgindi's $C^{1,\alpha}$ axisymmetric Euler singularity, 2021; the Chen-Hou and Luo-Hou numerical scenarios). For Euler the BKM integral *can* diverge, and BKM is then the certificate that a singularity has formed. The transfer to Navier-Stokes works precisely because $\nu\Delta u$ only adds dissipation to the $H^s$ estimate. So BKM is *not* blind to viscosity; it is agnostic in a controlled way, and the role of $\nu$ is sharply visible: in the inviscid limit the criterion is the same, but the dynamics it monitors are genuinely more singular. This matches the Burgers control: the inviscid Burgers equation shocks in finite time (gradient blow-up), and viscosity is what regularizes; BKM is the vorticity analog of "watch the gradient," with the curl playing the role of the gradient and stretching playing the role of the nonlinear steepening.

**Verdict.** BKM passes all three structural controls and sits at the right (critical) level. It is a model of what the project wants: a criterion that is 3D-essential, critical, and viscosity-aware. It is not regularity-closing because the critical target it names is not reachable from the only global a priori bound.

## What it gives / what it does not give

**Gives.**
- A clean, computable blow-up monitor. The DNS thread (`experiments/taylor_green/`) tracks $\max_x|\omega(t)|$ directly and accumulates $\int_0^t\|\omega\|_{L^\infty}$; a numerical singularity is diagnosed by this integral trending to divergence, with the double-exponential safety margin built into the interpretation.
- The correct reduction of the regularity problem to a vorticity statement. Any future proof can target $\int_0^T\|\omega\|_{L^\infty}\,dt<\infty$ and know that success there is success outright.
- A rigidity statement: no "soft" blow-up. The first singularity, if any, must show up as non-integrable sup-vorticity. This constrains the geometry of putative singularities and feeds the partial-regularity and self-similar analyses (CKN, Necas-Ruzicka-Sverak).
- An honest accounting of the gap: BKM converts "prove regularity" into "control a critical norm," which is the whole project's thesis that regularity is a critical-scaling statement.

**Does not give.**
- **Any bound on the integral.** BKM is purely conditional. It does not show $\int_0^T\|\omega\|_{L^\infty}\,dt$ is finite for Navier-Stokes; that *is* the open problem in vorticity form.
- **A way to reach the integral from the energy.** The energy controls $\omega$ only in $L^2_tL^2_x$ (supercritical); BKM needs $L^1_tL^\infty_x$ (critical). The gap is the supercriticality gap, restated. No interpolation closes it without new input.
- **Control of the stretching term.** BKM monitors the *consequence* of stretching ($\|\omega\|_{L^\infty}$ growth) but offers no mechanism to bound $(\omega\cdot\nabla)u$. The geometric criteria (Constantin-Fefferman, Direction 02) are the complementary attack: they bound stretching by constraining the *direction* $\xi=\omega/|\omega|$, which is dimensionless and scale aware, rather than the magnitude.
- **A viscosity-specific improvement.** BKM uses none of the parabolic smoothing of NS beyond sign-definiteness. The criteria that *do* exploit $\nu>0$ (Prodi-Serrin-Ladyzhenskaya, ESS) reach critical *velocity* norms and are NS-only. BKM is weaker in this sense (it is the same for Euler and NS) but more universal.

The most important sentence for the project: **BKM tells us the proof must produce $L^1_t L^\infty_x$ control of vorticity (or any genuinely critical control that implies it), and that the energy cannot, so the missing ingredient is a new critical estimate engaging vortex stretching.** That is the compass reading, not a wall.

## Lineage and sharpest known form

**Builds on.**
- The Biot-Savart law and the $L^\infty$-unboundedness of Calderon-Zygmund operators (the reason a logarithm is unavoidable).
- Brezis-Gallouet (1980) and Brezis-Wainger (1980) logarithmic interpolation inequalities, of which the BKM log-Sobolev inequality is the divergence-free, curl-specialized form.
- Kato's local well-posedness theory for Euler in $H^s$ (the framework the high-norm estimate lives in).

**Built on it / sharper forms (chronological).**
- **Ponce (1985)**, "Remarks on a paper by J. T. Beale, T. Kato and A. Majda," *Comm. Math. Phys.* **98**, 349-353: the criterion can be phrased with the deformation tensor (symmetric part of $\nabla u$), $\int_0^T\|\mathrm{Def}\,u(t)\|_{L^\infty}\,dt$, which is the part of $\nabla u$ that actually drives stretching.
- **Kozono-Taniuchi (2000)**, *Comm. Math. Phys.* **214**, 191-200, "Bilinear estimates in BMO and the Navier-Stokes equations": the BKM log-Sobolev inequality is upgraded so that $\|\omega\|_{L^\infty}$ is replaced by the strictly weaker $\|\omega\|_{\mathrm{BMO}}$,
$$\|\nabla u\|_{L^\infty} \le C\big(1 + \|\omega\|_{\mathrm{BMO}}(1+\log^+\|u\|_{H^s}) + \|\omega\|_{L^2}\big),$$
giving the **BMO endpoint** continuation criterion: smoothness extends past $T$ if $\int_0^T\|\omega(t)\|_{\mathrm{BMO}}\,dt<\infty$. $\mathrm{BMO}$ is critical (same scaling as $L^\infty$ at this order) but genuinely larger, so this is a strict weakening of the hypothesis. This is the Direction 01, target 3 lead.
- **Kozono-Ogawa-Taniuchi (2002)**, "The critical Sobolev inequalities in Besov spaces and regularity criterion to some semi-linear evolution equations," *Math. Z.* **242**, 251-278: a further weakening to the homogeneous Besov space $\dot B^0_{\infty,\infty}$ (which contains BMO), with the log-Sobolev inequality
$$\|f\|_{L^\infty} \le C\big(1 + \|f\|_{\dot B^0_{\infty,\infty}}(1+\log^+\|f\|_{H^s})\big),$$
yielding the criterion $\int_0^T\|\omega(t)\|_{\dot B^0_{\infty,\infty}}\,dt<\infty$. This is the weakest-hypothesis member of the magnitude-based BKM family, and $\dot B^0_{\infty,\infty}$ is the natural critical endpoint.
- **Planchon (2003)**, "An extension of the Beale-Kato-Majda criterion for the Euler equations," *Comm. Math. Phys.* **232**, 319-326: a Littlewood-Paley refinement showing it is enough to control the high-frequency part of the vorticity (a $\limsup$ of dyadic blocks), localizing the obstruction in frequency.
- **Gallagher-Koch-Planchon (2016)**, "Blow-up of critical Besov norms at a potential Navier-Stokes singularity," *Comm. Math. Phys.* **343**, 39-82: the velocity-side analog and ESS companion; at a putative NS singularity a critical Besov norm $\|u\|_{\dot B^{-1+3/p}_{p,q}}$ must become unbounded for $3<p,q<\infty$, extending ESS off the $L^3$ point. Together with BKM this brackets the singularity from both the vorticity and velocity sides at the critical level.

**Sharpest known form as of 2025.** For the *vorticity* continuation criterion the frontier remains the critical Besov / BMO endpoints (Kozono-Taniuchi $\mathrm{BMO}$; Kozono-Ogawa-Taniuchi $\dot B^0_{\infty,\infty}$); these are weaker hypotheses than the original $L^\infty$ but all still **critical**, hence none is reachable from the energy, and no version weakens the time integrability below $L^1_t$ in a way that the energy supplies. The complementary frontier is geometric: Constantin-Fefferman (1993) and its descendants replace the magnitude criterion by a coherence-of-direction criterion, which is the Direction 02 lead and the most structurally promising departure from the BKM magnitude family. On the velocity side the analogous endpoint is ESS (2003) at $L^\infty_tL^3_x$, made quantitative by Tao (2019, triple-logarithmic lower bound on $\|u\|_{L^3}$ concentration at a singularity). All of these sit at scaling exponent $0$; the supercriticality gap to the energy is unchanged across the whole family. The open improvement worth chasing (Direction 01) is any genuinely *sub-*$L^1_t$ or self-improving relaxation, or a coupling of the BMO/Besov refinement to a quantity the energy or a slightly-stronger-than-energy bound can reach.

## References

- J. T. Beale, T. Kato, A. Majda, "Remarks on the breakdown of smooth solutions for the 3-D Euler equations," *Comm. Math. Phys.* **94** (1984), 61-66.
- G. Ponce, "Remarks on a paper by J. T. Beale, T. Kato and A. Majda," *Comm. Math. Phys.* **98** (1985), 349-353.
- H. Brezis, T. Gallouet, "Nonlinear Schrodinger evolution equations," *Nonlinear Anal.* **4** (1980), 677-681; H. Brezis, S. Wainger, "A note on limiting cases of Sobolev embeddings and convolution inequalities," *Comm. PDE* **5** (1980), 773-789.
- H. Kozono, Y. Taniuchi, "Bilinear estimates in BMO and the Navier-Stokes equations," *Comm. Math. Phys.* **214** (2000), 191-200. (Also *Math. Z.* **235** (2000), 173-194, for the limiting-case log inequality.)
- H. Kozono, T. Ogawa, Y. Taniuchi, "The critical Sobolev inequalities in Besov spaces and regularity criterion to some semi-linear evolution equations," *Math. Z.* **242** (2002), 251-278.
- F. Planchon, "An extension of the Beale-Kato-Majda criterion for the Euler equations," *Comm. Math. Phys.* **232** (2003), 319-326.
- I. Gallagher, G. Koch, F. Planchon, "Blow-up of critical Besov norms at a potential Navier-Stokes singularity," *Comm. Math. Phys.* **343** (2016), 39-82.
- P. Constantin, C. Fefferman, "Direction of vorticity and the problem of global regularity for the Navier-Stokes equations," *Indiana Univ. Math. J.* **42** (1993), 775-789.
- L. Escauriaza, G. Seregin, V. Sverak, "$L_{3,\infty}$-solutions of Navier-Stokes equations and backward uniqueness," *Russian Math. Surveys* **58** (2003), 211-250.
- T. Tao, "Quantitative bounds for critically bounded solutions of the Navier-Stokes equations," (2019).
- T. M. Elgindi, "Finite-time singularity formation for $C^{1,\alpha}$ solutions to the incompressible Euler equations on $\mathbb{R}^3$," *Ann. of Math.* **194** (2021), 647-727.

## Cross-links

- Direction 01 (critical continuation criteria), where BKM and its BMO/Besov refinements are the central objects: [`../research_directions/01_critical_continuation_criteria.md`](../research_directions/01_critical_continuation_criteria.md).
- Direction 02 (vorticity geometry), the complementary attack on the stretching term BKM only monitors: [`../research_directions/02_vorticity_geometry.md`](../research_directions/02_vorticity_geometry.md).
- Direction 03 (the supercriticality gap), which is exactly the gap between the energy's $L^2_tL^2_x$ vorticity control and BKM's critical $L^1_tL^\infty_x$ target: [`../research_directions/03_supercriticality_gap.md`](../research_directions/03_supercriticality_gap.md).
- Direction 04 (blow-up and barriers), the Euler side where the BKM integral genuinely diverges (Elgindi, Chen-Hou): [`../research_directions/04_blowup_and_barriers.md`](../research_directions/04_blowup_and_barriers.md).
- Sibling note ESS (2003), the velocity-side critical endpoint: [`./escauriaza_seregin_sverak_2003.md`](./escauriaza_seregin_sverak_2003.md).
- Sibling note CKN (1982), partial regularity, which constrains the geometry of the singular set BKM rules "soft" blow-up out of: [`./caffarelli_kohn_nirenberg_1982.md`](./caffarelli_kohn_nirenberg_1982.md).
- The criticality bookkeeper that returns `CRITICAL` for $\int_0^T\|\omega\|_{L^\infty}\,dt$: `experiments/_shared/criticality.py`; the DNS that tracks the integral: `experiments/taylor_green/`.
