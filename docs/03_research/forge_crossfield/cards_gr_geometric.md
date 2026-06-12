# Forge cards: general relativity and geometric flows (cross-field session)

BUILDER output, conjecture-forge protocol ([`OPERATIONS.md`](../../../OPERATIONS.md) section 10), cross-field variant. Two lenses imported from GR and geometric flows: (A) trapped surfaces / critical collapse, (B) Perelman-type monotonicity. Both cards are CANDIDATES pending ADVERSARY and SURVEYOR passes. All scaling exponents below were verified mechanically (dimension-count script plus the repo bookkeeper `experiments/_shared/criticality.py`); the Card B evolution identity was verified spectrally on a band-limited random divergence-free field (relative residual $2.0 \times 10^{-16}$ at $N = 32$, $K = 4$, $\nu = 0.37$; details in the card).

Convention: $a = k - 2/p - 3/q$ for $\|\nabla^{k-1} u\|_{L^p_t L^q_x}$-type norms ($u$ carries $k = 1$, $\omega$ and $\nabla u$ carry $k = 2$, $p$ carries $k = 2$, $\nabla\omega$ carries $k = 3$). Anchors: energy $a(\|u\|_{L^\infty_t L^2_x}) = 1 - 3/2 = -1/2$ (supercritical), $a(\|u\|_{L^\infty_t L^3_x}) = 0$, BKM $a(\|\omega\|_{L^1_t L^\infty_x}) = 2 - 2 = 0$, enstrophy $a(\|\omega\|_{L^\infty_t L^2_x}) = 2 - 3/2 = +1/2$ (subcritical norm, hence no a priori bound). For local quantities the equivalent currency is the parabolic length dimension: assign $[x] = +1$, $[t] = +2$, $[u] = -1$, $[p] = -2$, $[\omega] = -2$, $[\nu] = 0$, and divide by the power of $r$ that makes the quantity dimensionless; $a = 0$ then means CKN-type scale invariance.

---

## Card A: Parabolic trapped regions and Navier-Stokes weak censorship

**Name**: The expansion scalar $\Theta(r)$ and the no-trapping conjecture (NS weak censorship).

**Status (self-assessed)**: wounded. Alive as a precise intermediate target strictly between "nothing" and full regularity; wounded because the diagnostic is dimension-neutral (like CKN itself) and the conjecture is non-coercive by design. Both wounds are stated below, not hidden.

**Formal statement**.

Setting: $u$ a solution smooth on $[0, t_0)$ (the first-singularity framing), $(x_0, t_0)$ a candidate singular point, $Q_r = B_r(x_0) \times (t_0 - r^2, t_0)$. All quantities are radius-averaged over $\rho \in [r, 2r]$ (written $\fint_r^{2r} d\rho$) to avoid boundary traces.

Definitions (each has $a = 0$, table below):

$$\mathcal{A}(t; r) := \frac{1}{r} \fint_r^{2r} \int_{B_\rho} |u(x,t)|^2\, dx\, d\rho, \qquad E(r) := \frac{1}{r} \fint_r^{2r} \int_{t_0 - r^2}^{t_0} \int_{B_\rho} |\nabla u|^2\, dx\, dt\, d\rho,$$

$$\Phi(r) := \frac{1}{r} \fint_r^{2r} \int_{t_0 - r^2}^{t_0} \int_{\partial B_\rho} \Big[ \Big( \tfrac{|u|^2}{2} + p \Big)(-u \cdot n) + \nu\, \partial_n \tfrac{|u|^2}{2} \Big]\, dS\, dt\, d\rho,$$

$$\Theta(r) := \nu E(r) - \Phi(r) \quad (\text{the expansion scalar: dissipative outgo minus total inward flux}).$$

The local energy identity for smooth solutions gives the exact balance

$$\tfrac{1}{2}\mathcal{A}(t_0; r) - \tfrac{1}{2}\mathcal{A}(t_0 - r^2; r) = -\,\Theta(r).$$

Definition (trapped point): $(x_0, t_0)$ is $(r_0, \delta)$-trapped if $\Theta(r) \le -\delta$ for ALL $0 < r \le r_0$. (The all-scale quantifier is forced; see "How it most likely dies".)

Lemma A1 (the Penrose analog; provable, VERIFIER target): if $(x_0, t_0)$ is $(r_0, \delta)$-trapped with $\delta > 0$ for a solution smooth before $t_0$, then $(x_0, t_0)$ is a singular point. Proof shape: the exact balance gives $\mathcal{A}(t_0; r) \ge 2\delta$ for every $r \le r_0$; at a regular point $\mathcal{A}(t_0; r) \le C \|u\|_{L^\infty(Q_\rho)}^2 r^2 \to 0$. Two lines once the balance is set up.

Conjecture A2 (NS weak censorship): for every $\nu > 0$ and every solution evolving from smooth, divergence-free, finite-energy data on $\mathbb{T}^3$ or $\mathbb{R}^3$, no point is $(r_0, \delta)$-trapped for any $r_0, \delta > 0$. Equivalently: at every point, $\limsup_{r \to 0} \Theta(r) \ge 0$. In words: the scale-invariant local balance can never tip to sustained net inward flux at all scales simultaneously; viscous defocusing wins the critical balance at some scale, at all data sizes.

Logical position: global regularity implies A2 (regular points have $\Theta(r) \to 0$); A2 is a priori strictly weaker than regularity, because a singular point may have $\Theta(r)$ oscillating in sign across scales. A2 is the analog of "no trapped surfaces form", not of full censorship.

**Cross-field source**: Penrose 1965 (trapped surface implies incompleteness); Christodoulou-Klainerman 1993 (Minkowski stability: small data never traps); Christodoulou 2008 (focused large data DOES trap, for vacuum gravity); Choptuik 1993 and Gundlach-Martin-Garcia 2007 (the blow-up threshold is a codimension-one critical manifold). The forged claim is that NS at $\nu > 0$ is globally in the Christodoulou-Klainerman regime: the analog of Christodoulou 2008 never happens. The structural inversion to record honestly: in GR, Raychaudhuri focusing makes LARGENESS self-propagating (one trapped slice forces collapse); in NS, the CKN local energy inequality makes SMALLNESS self-propagating (epsilon-regularity) and gives no lower bounds. That is why the trapped set here carries an all-scale quantifier instead of a one-scale propagation lemma, and it is the precise sense in which the two problems are duals rather than twins.

**Physics heuristic**: a singularity needs its parabolic cylinder fed: the energy dissipated inside $B_r$ during $(t_0 - r^2, t_0)$ at a near-singular point exceeds what the cylinder holds, so the Bernoulli flux $(\tfrac{|u|^2}{2} + p)\, u \cdot n$ must run net-inward, with scale-invariant margin, at every scale down the cascade. Trapping is the physical-space face of a sustained constant-flux cascade focused on a point: exactly the profile $a_n \sim \lambda^{-n/3}$ that blows up the dyadic model on the supercritical side (finding #9). A2 says the true pressure-transport structure cannot hold that configuration together at any $\nu > 0$.

**3D mechanism engaged**: indirectly, and this is the wound. The functional itself is mechanism-agnostic (so is CKN). The 3D content sits in the only term that can sustain trapping: the inward flux must be refilled scale-by-scale, which in 3D is powered by vortex stretching, and the pressure part of the flux, $\frac{1}{r}\iint p\,(-u \cdot n)$, is slaved to the velocity by $-\Delta p = \partial_i u_j\, \partial_j u_i$. Note the structural detail: since $\nabla \cdot u = 0$, constants drop from the pressure flux ($\int_{\partial B_\rho} c\, (u \cdot n)\, dS = 0$), so only the oscillation $p - \bar{p}_\rho$ enters; this is exactly the CKN $D(r)$ currency, and pressure can export or import energy with zero net mass flux. The restricted-Euler control (drop the nonlocal pressure Hessian: finite-time blow-up, Vieillefosse 1982, Cantwell 1992) says any proof of A2 must use the nonlocal pressure reaction, not just the local balance.

**Scaling arithmetic** (verified mechanically; raw $L$-dimension, then the $r$-normalization that pins $a = 0$):

| quantity | raw dim | normalization | $a$ |
|---|---|---|---|
| $\sup_t \int_{B_r} \lvert u\rvert^2 dx$ | $+1$ | $r^{-1}$ | $0$ |
| $\iint_{Q_r} \lvert\nabla u\rvert^2$ | $+1$ | $r^{-1}$ | $0$ |
| $\iint_{Q_r} \lvert u\rvert^3$ | $+2$ | $r^{-2}$ | $0$ |
| $\iint_{Q_r} \lvert p\rvert^{3/2}$ | $+2$ | $r^{-2}$ | $0$ |
| advective flux $\iint (\lvert u\rvert^2/2)(u \cdot n)\, dS\, dt$ | $+1$ | $r^{-1}$ | $0$ |
| pressure flux $\iint p\,(u \cdot n)\, dS\, dt$ | $+1$ | $r^{-1}$ | $0$ |
| viscous flux $\iint \nu\, \partial_n (\lvert u\rvert^2/2)\, dS\, dt$ | $+1$ | $r^{-1}$ | $0$ |

$\Theta$ is a difference of two $a = 0$ quantities, so the trapped condition is scale-invariant: trapping for $u$ at scale $r$ is trapping for $u_\lambda$ at scale $r/\lambda$. There is no hidden supercritical crutch; the energy norm ($a = -1/2$) appears nowhere as a controlling quantity. Conversely A2 does not CLAIM a critical bound; it claims a sign.

**Role of viscosity**: $\nu E(r)$ is half of $\Theta$, and the conjecture is false without it: for Euler ($\nu = 0$), $\Theta = -\Phi$ and trapping only requires sustained inward flux, which the Elgindi 2021 and Luo-Hou 2014 scenarios plausibly realize (adversarial test below). For Burgers there is no pressure to oppose the influx and shocks form. A2 is precisely a statement about what $\nu \Delta u$ buys in the critical local balance, which is the project's framing of the whole problem (finding #4).

**Tao-barrier check**: passes at the level of the statement, with a named caveat. The averaged system (Tao 2016) preserves the global energy identity but the averaged bilinear operator does not admit the pointwise divergence-form Bernoulli flux: there is no local energy identity, hence no flux form of $\Theta$. Defining trapping intrinsically (realized local-energy gain at all scales, via the balance) the dyadic/averaged blow-up IS trapped: on the constant-flux profile $a_n \sim \lambda^{-n/3}$, the local energy at scale $r = \lambda^{-n}$ is $\mathcal{A} \sim r^{-1} \sum_{m \ge n} \lambda^{-2m/3} \sim \lambda^{n/3} \to \infty$, so the margin even diverges (ratio $\lambda^{1/3} \approx 1.26$ per shell at $\lambda = 2$). So A2 is FALSE for the caricature, which is exactly what gate 4 demands of a true statement: any proof must use the Bernoulli flux form and the slaved pressure, which averaging destroys. Caveat for SURVEYOR: pin the precise remark in Tao 2016 about the failure of the local energy inequality for the averaged system.

**2D check**: wounded, recorded honestly. The same $\Theta$ exists in 2D (with $d = 2$ normalizations everything again sits at $a = 0$ because 2D energy is itself critical), and A2 in 2D is true but follows from the enstrophy bound. The functional does not require stretching; it would not predict 2D blow-up (so it does not FAIL the gate), but a proof of A2 that never touches the vorticity equation would prove the 2D statement by the same argument, flagging that it used only soft structure, and gate 4 already says soft structure cannot suffice. Conclusion: the diagnostic is dimension-neutral; the difficulty and any eventual proof must localize in the 3D refilling mechanism. This is a wound, not a kill.

**Cheapest falsification test** (laptop-runnable; module to create: `experiments/trapped_region/theta_scan.py`):

1. Compute $\Theta(r)$ on dyadic $r \in \{2\pi/32, \dots, 2\pi/4\}$, centered at the running max-$|\omega|$ point, along (a) Taylor-Green $32^3$, $\nu = 0.01$ (smooth baseline, `experiments/taylor_green/`), (b) the Hou-Luo axisymmetric run at $\nu = 0.005$ and $\nu/4$ (`experiments/hou_luo/`), (c) the 2D control (`Flow2D`, $n = 64$, $\nu = 0.01$).
2. Shell-model surrogate: intrinsic trapping margin per shell on the recorded dyadic blow-up trajectory ($\alpha = 1/3$, $\lambda = 2$, $\nu = 0.1$, `experiments/dyadic_shell/`). Quantitative prediction to check: margin ratio per shell $\to \lambda^{1/3} \approx 1.26$.
3. Diagnostics: the profile $r \mapsto \Theta(r)$ over time; persistence length of any negative excursion; refinement stability per the finding #11 protocol ($16^3 \to 24^3 \to 32^3$).

Kill signatures, named: (K1) $\Theta(r) < -\delta$ across the whole resolved dyadic band, sustained over a parabolic window, refinement-stable, in the KNOWN-SMOOTH baseline: the diagnostic has no discriminating power, card dies as an instrument. (K2) the dyadic blow-up trajectory is NOT uniformly trapped (sign of the shell margin oscillates): the all-scale trapped condition is too strong to capture even clean supercritical collapse, card dies as a target. Healthy readout: TG sign-mixed with no persistence; Hou-Luo transient negativity deepening as $\nu$ drops; dyadic uniformly trapped at ratio $\approx 1.26$; 2D no persistent trapping.

**How it most likely dies**: (1) The GR import genuinely inverts: with no Raychaudhuri-type lower bound, the all-scale quantifier makes A2 only thinly separated from full regularity, so the "intermediate target" inherits the full difficulty (most likely). (2) Singular scenarios with scale-oscillating flux make A2 true but vacuous, reducing it to a physical-space cousin of the known exclusion of monotone collapse (Necas-Ruzicka-Sverak 1996, Tsai 1998). (3) K1 fires and the instrument is dull. Even in deaths (1)-(2) the coordinate gained is sharp: it would establish that NS singularity formation, if any, cannot be a steady local cascade but must be scale-intermittent, which constrains the anti-lens (blow-up construction) directly.

---

## Card B: The Lagrangian backward kernel and the weighted-stretching Harnack

**Name**: $\mathcal{W}(t) = (t_0 - t)^2 \int |\omega|^2\, G^u\, dx$ and the missing Perelman identity (H).

**Status (self-assessed)**: alive. The evolution identity is exact and verified; the conjecture is pinned at exponent 0, saturated by Euler self-similarity, structurally dead for the averaged caricature, and trivially true in 2D. Precedent risk on the identity itself is flagged for SURVEYOR.

**Formal statement**.

Setting: $u$ smooth on $[0, T^*)$, $\nu > 0$, center $(x_0, t_0)$ with $t_0 \le T^*$. Define the Lagrangian backward kernel $G^u_{x_0,t_0}(x, t)$ as the solution of the backward Kolmogorov equation

$$\partial_t G^u + u \cdot \nabla G^u + \nu \Delta G^u = 0, \qquad G^u(\cdot, t) \to \delta_{x_0} \ (t \uparrow t_0);$$

equivalently $G^u(x,t)$ is the transition density to $(x_0, t_0)$ of the stochastic Lagrangian flow $dX_s = u(X_s, s)\, ds + \sqrt{2\nu}\, dB_s$ (the Constantin-Iyer 2008 process). Because $\nabla \cdot u = 0$ the transition density is doubly stochastic: $G^u(\cdot, t)$ is a genuine probability density in $x$ for each $t < t_0$. This kernel is the Perelman-type weight: it replaces Perelman's conjugate heat kernel, with the flow itself supplying the transport part.

Theorem B1 (exact identity; verified spectrally, residual $2.0 \times 10^{-16}$; VERIFIER target): for smooth $u$ and any smooth weight $\phi$,

$$\frac{d}{dt} \int |\omega|^2 \phi\, dx = \int |\omega|^2 \big( \partial_t \phi + \nu \Delta \phi + u \cdot \nabla \phi \big)\, dx \;-\; 2\nu \int |\nabla \omega|^2 \phi\, dx \;+\; 2 \int (\omega \cdot S \omega)\, \phi\, dx,$$

with $S = \tfrac{1}{2}(\nabla u + \nabla u^T)$ and $\omega \cdot (\omega \cdot \nabla u) = \omega \cdot S\omega$ pointwise. With $\phi = G^u$ the entire first bracket vanishes IDENTICALLY: every transport and linear-diffusion term cancels, and

$$\frac{d}{dt} \int |\omega|^2 G^u\, dx = -2\nu \int |\nabla \omega|^2 G^u\, dx + 2 \int (\omega \cdot S\omega)\, G^u\, dx.$$

The only term without a sign is the weighted stretching: the obstruction is isolated in exactly the genuinely 3D term, with no error terms. Numerical verification (this session, band-limited random divergence-free field, $N = 32$, $K = 4$, $\nu = 0.37$): $\max|\nabla \cdot u| = 1.0 \times 10^{-14}$, pointwise $|\omega\cdot(\omega\cdot\nabla u) - \omega \cdot S\omega| \le 1.7 \times 10^{-13}$ against field scale $5.2 \times 10^2$, identity residual $|{\rm LHS} - {\rm RHS}|/|{\rm LHS}| = 2.0 \times 10^{-16}$, and on a planar (2D) field $\omega \cdot S\omega \equiv 0$ exactly.

The critical quantity: $\mathcal{W}_{x_0,t_0}(t) := (t_0 - t)^2 \int |\omega|^2\, G^u_{x_0,t_0}\, dx$, with

$$\frac{d\mathcal{W}}{dt} = -\frac{2}{t_0 - t}\, \mathcal{W} \;-\; 2\nu (t_0 - t)^2 \int |\nabla \omega|^2 G^u \;+\; 2 (t_0 - t)^2 \int (\omega \cdot S\omega)\, G^u.$$

Conjecture B2 (the weighted-stretching Harnack, the named missing identity): for all smooth solutions, all centers, all $t < t_0$,

$$\textbf{(H)} \qquad \int (\omega \cdot S\omega)\, G^u\, dx \;\le\; \frac{1}{t_0 - t} \int |\omega|^2\, G^u\, dx \;+\; \nu \int |\nabla \omega|^2\, G^u\, dx.$$

(H) is equivalent to $\frac{d}{dt}\mathcal{W} \le 0$: monotonicity of a coercive-at-the-Type-I-level, exponent-0, localized enstrophy. (H) is the NS analog of Perelman's differential Harnack for the conjugate heat kernel (the inequality that makes the $\mathcal{W}$-entropy monotone); the analog of Perelman's completed square is the missing algebra that would control $\omega \cdot S\omega$ by the pressure Hessian: differentiating the stretching term meets $\frac{DS}{Dt} = -S^2 - \tfrac{1}{4}(\omega \otimes \omega - |\omega|^2 I) - \nabla^2 p + \nu \Delta S$, and the restricted-Euler control (drop the nonlocal part of $\nabla^2 p$: blow-up) shows the nonlocal pressure Hessian MUST appear in any proof. If (H) needs a constant $\kappa > 1$ on the first term, the monotone object becomes $(t_0 - t)^{2\kappa} \int |\omega|^2 G^u$, which has $L$-dimension $4(\kappa - 1) \ne 0$: the conjecture drifts off the critical pin and the cap weakens below Type-I, excluded by nothing known. $\kappa = 1$ is the unique scale-consistent pin, and it is exactly saturated by self-similar Euler collapse: along the deterministic ($\nu = 0$) limit of the kernel, (H) reads $\frac{D}{Dt} |\omega|^2 \le \frac{2|\omega|^2}{t_0 - t}$ on the trajectory into the singularity, i.e. a Lagrangian Type-I cap, and Elgindi's $C^{1,\alpha}$ self-similar Euler blow-up ($|\omega| \sim (t_0 - t)^{-1}$) saturates it with equality. So the strict inequality, if true, is bought entirely by $\nu > 0$.

Supporting fact B3 (no-local-collapsing of the kernel; essentially known, SURVEYOR to confirm scope): for divergence-free drift, $\frac{d}{d\tau} \|g\|_{L^2}^2 = -2\nu \|\nabla g\|_{L^2}^2$ EXACTLY (the drift term vanishes by incompressibility), so Nash iteration gives the on-diagonal bound $\|G^u(\cdot, t)\|_\infty \le C (\nu (t_0 - t))^{-3/2}$ unconditionally (Nash 1958; Osada 1987; cf. Seregin-Silvestre-Sverak-Zlatos 2012: it is the off-diagonal Gaussian decay and Harnack that need critical drift information, not the sup bound). So the weight can never collapse below the viscous parabolic width: the analog of Perelman's no-local-collapsing comes for free here, and the entire open content of the card is (H).

Downstream chain, stated honestly: (H) gives $\mathcal{W}(t) \le \mathcal{W}(t_1)$, hence a Lagrangian-averaged Type-I vorticity cap $\int |\omega|^2 G^u \lesssim (t_0 - t)^{-2}$. This does NOT close BKM ($\int (t_0-t)^{-1} dt$ is log-divergent: the cap sits exactly at the borderline BKM just fails to cover). Closing regularity needs the second Perelman step: blow-up limits under the cap are Type-I / ancient solutions, where partial rigidity EXISTS for NS: self-similar excluded in $L^3$ (Necas-Ruzicka-Sverak 1996; Tsai 1998), axisymmetric Type-I excluded (Chen-Strain-Tsai-Yau 2008-09; Koch-Nadirashvili-Seregin-Sverak 2009), bounded-ancient-solution rigidity is the open Seregin-Sverak program, and ESS 2003 supplies the backward-uniqueness machinery. (H) would funnel every blow-up into exactly the regime where the existing kill theorems live.

**Cross-field source**: Perelman 2002 ($\mathcal{W}$-entropy, no-local-collapsing, reduced volume; the proof pattern monotonicity $\to$ collapse classification $\to$ rigidity); Hamilton 1993 (differential Harnack); Struwe 1988 (harmonic map heat flow monotonicity); Huisken 1990 (MCF). The kill-comparison the brief demands, recorded with numbers: Struwe's HMHF quantity $(t_0 - t) \int |\nabla v|^2 G\, dx$ is scale-invariant in EVERY dimension $m$ and monotone in every dimension, yet HMHF blows up for $m \ge 2$ (Chang-Ding-Ye 1992 at $m = 2$; equivariant shrinkers exist for $3 \le m \le 6$, Fan 1999, Germain-Rupflin 2011; nonexistence for $m \ge 7$, Bizon-Wasserman 2015). LESSON: a critical monotone quantity is NOT sufficient; regularity = monotonicity AND empty shrinker set. The NS-specific bet of this card is that the shrinker set is empty (NRS/Tsai already prove the self-similar slice of that), whereas for HMHF it is provably nonempty. Monotonicity of a supercritical quantity would be worth even less; that is why $\mathcal{W}$ is pinned at $a = 0$ and the $\kappa$-drift is recorded as a death mode.

**Physics heuristic**: ride the dye. $G^u$ is the density of a passive tracer released backward from the would-be singular event; $\int |\omega|^2 G^u$ is the enstrophy the EVENT will actually inherit, weighted by what can physically reach it through transport plus molecular diffusion. The claim (H) says: the vorticity headed into an event can be stretched no faster than the self-similar rate, once you average over the viscous fuzz of the arriving trajectories; faster-than-self-similar focusing requires coherence the noise floor $\sqrt{2\nu}$ destroys. Euler ($\nu = 0$) sits exactly on the boundary, which matches the fact that Euler does blow up.

**3D mechanism engaged**: directly and exclusively. The single obstruction term is $\int (\omega \cdot S\omega) G^u$: weighted vortex stretching, the term that defines the 3D problem (finding #3). The strain is slaved to the vorticity through the nonlocal Biot-Savart/pressure structure, and the proof-path for (H) runs through the pressure Hessian in $DS/Dt$ (Vieillefosse 1982, Cantwell 1992, Ohkitani 1993 for why the nonlocal part is the whole fight). The depletion phenomenology of findings #10 and #14 (realized stretching $\approx 0.53$ of the pointwise maximum, unforced) is exactly what (H) would force a priori in averaged form.

**Scaling arithmetic** (every exponent computed and machine-checked):

| object | computation | $a$ |
|---|---|---|
| $\|\omega\|_{L^\infty_t L^2_x}$ (raw enstrophy) | $2 - 0 - 3/2$ | $+1/2$ (subcritical norm: monotonicity of it is not even conjecturable) |
| $G^u\, dx$ | probability measure, doubly stochastic | $0$ |
| $\int \lvert\omega\rvert^2 G^u dx$ | $L$-dim $-4-3+3$ | $-4$ |
| $\mathcal{W} = (t_0-t)^2 \int \lvert\omega\rvert^2 G^u dx$ | $-4 + 2 \cdot 2$ | $0$ exactly |
| (H) LHS $\int \omega \cdot S\omega\, G^u$ | $-2-2-2-3+3$ | $L$-dim $-6$ |
| (H) term $\frac{1}{t_0-t} \int \lvert\omega\rvert^2 G^u$ | $-4 - 2$ | $L$-dim $-6$ |
| (H) term $\nu \int \lvert\nabla\omega\rvert^2 G^u$ | $0 - 6 - 3 + 3$ | $L$-dim $-6$ |

All three (H) terms scale identically ($\lambda^6$ under the zoom): the inequality is scale-COVARIANT with zero slack, i.e. pinned at exponent 0 as demanded. Under $u \mapsto u_\lambda$: $\omega_\lambda = \lambda^2 \omega(\lambda x, \lambda^2 t)$, $G^{u_\lambda}(x,t) = \lambda^3 G^u(\lambda x, \lambda^2 t)$ (densities), $(t_0 - t) \mapsto \lambda^{-2}(t_0' - t')$, so $\mathcal{W}_{u_\lambda}(t) = \mathcal{W}_u(\lambda^2 t)$: invariant, checked.

**Role of viscosity**: enters three times, all essentially. (i) The dissipation term in B1 is half the budget of (H). (ii) The kernel itself spreads at the noise scale $\sqrt{2\nu (t_0-t)}$ and B3 (Nash) forbids its collapse, with constant degrading as $\nu^{-3/2}$: at $\nu = 0$ the kernel degenerates to a Lagrangian delta and (H) becomes the Type-I cap that Elgindi's Euler blow-up saturates with equality. (iii) Burgers: no incompressibility, no doubly stochastic kernel, no pressure to generate the depletion; the analog fails at shocks. The conjecture is precisely a quantification of what $\nu > 0$ buys over Euler, and it buys it at exponent 0, not through the supercritical energy.

**Tao-barrier check**: passes structurally. The exact cancellation in B1 requires (i) the SAME field $u$ transporting $\omega$ and driving the kernel, (ii) the pointwise algebra $\omega \cdot (\omega \cdot \nabla u) = \omega \cdot S\omega$, (iii) pointwise $\nabla \cdot u = 0$. Tao's averaged bilinear operator decouples the transporter from the transported (rotated, dilated Fourier-localized copies), so no single backward kernel cancels the transport: B1 has no analog for the averaged system, and the quantity $\mathcal{W}$ cannot even be defined there. This is the strongest barrier pass available: not "the proof would not transfer" but "the OBJECT does not exist for the caricature". The shell-model surrogate test below additionally checks that the (H)-balance is violated on the caricature's blow-up trajectory.

**2D check**: passes non-vacuously and cleanly. In 2D the identity gives $\frac{d}{dt} \int \omega^2 G^u = -2\nu \int |\nabla \omega|^2 G^u \le 0$: the weighted enstrophy is UNCONDITIONALLY monotone (and $(t_0-t)^2 \int \omega^2 G^u$ is again $a = 0$ in the 2D currency). The obstruction term is identically zero in 2D through the same algebra (verified: $\omega \cdot S\omega \equiv 0$ on planar fields, exact zero in the probe). So the card's open content is EXACTLY the 3D stretching term and nothing else: the cleanest possible factorization of the problem across the 2D gate. The card does not "apply verbatim in 2D"; in 2D it degenerates to a true and easy statement, in 3D its entire difficulty is the one term 2D lacks.

**Cheapest falsification test** (laptop-runnable; module to create: `experiments/forge_crossfield/weighted_harnack_probe.py`):

1. Surrogate-kernel Harnack ratio on Taylor-Green $32^3$, $\nu = 0.01$: with the drift-free Gaussian $G_{\nu\sigma^2}$ standing in for $G^u$ and the transport defect $\int |\omega|^2\, u \cdot \nabla G\, dx$ reported as a separate column (it vanishes for the true kernel), compute
$$\mathcal{R}(t; \sigma) = \frac{\int (\omega \cdot S\omega)\, G\, dx}{\frac{1}{\sigma^2} \int |\omega|^2 G\, dx + \nu \int |\nabla\omega|^2 G\, dx}$$
at centers on the max-$|\omega|$ trajectory, $\sigma^2 = t_0 - t$ over a dyadic ladder, refinement-checked $16^3 \to 24^3 \to 32^3$ (finding #11 protocol).
2. True-kernel version: advect $G^u$ by integrating the backward Kolmogorov equation through the same pseudo-spectral stepper over a stored window of $u$ snapshots (one extra scalar field; trivial at $32^3$), removing the transport-defect caveat.
3. Mount on Hou-Luo (`experiments/hou_luo/`, $\nu = 0.005$ and $\nu/4$): trend of $\max_t \mathcal{R}$ as $\nu$ decreases is the headline number.
4. Barrier surrogate: shell-model ratio $R_n = \dfrac{\lambda^n a_{n-1}^2 a_n}{(t_0 - t_n)^{-1} a_n^2 + \nu \lambda^{2n} a_n^2}$ on the recorded dyadic blow-up ($\alpha = 1/3$, $\lambda = 2$, $\nu = 0.1$): expect $R_n \to$ const $> 1$ uniformly (the caricature violates the (H)-balance).
5. 2D control: same code path on `Flow2D`; the numerator must be structurally zero (already confirmed on static fields).

Kill signatures, named: (KB1) $\mathcal{R} > 1$ sustained over a parabolic window in the SMOOTH baseline, with the transport defect small and the value refinement-stable: (H) is false at $\kappa = 1$ even in mild regimes; then measure $\kappa^* = \sup \mathcal{R}$, and if $\kappa^*$ grows with Reynolds number the card is dead outright (no fixed-$\kappa$ retreat). (KB2) $R_n < 1$ on the dyadic blow-up trajectory: the (H)-balance fails to flag even clean supercritical collapse, so monotonicity of $\mathcal{W}$ would not discriminate singular from regular: dead as a target. Healthy readout: $\mathcal{R}$ comfortably below 1 on TG, approaching 1 from below on Hou-Luo as $\nu$ drops, $R_n > 1$ on the shell blow-up.

**How it most likely dies**: (1) Most likely: (H) at $\kappa = 1$ fails transiently in real flows during peak stretching (finding #10 already shows production exceeding dissipation for extended intervals; whether the $(t_0-t)^{-1}$ term carries the difference is exactly what the probe measures), and the empirical $\kappa^*$ drifts with Reynolds number, killing the fixed-constant version. (2) Even if (H) holds, the chain to regularity still needs Type-I/ancient rigidity (open: the Seregin-Sverak program), so the card at best RELOCATES the problem; that is still the Perelman shape and still progress, but it must not be oversold. (3) Precedent: B1 is elementary enough that it likely exists somewhere in the stochastic-Lagrangian literature (Constantin-Iyer 2008 circle, Eyink, Rezakhanlou); if SURVEYOR finds (H) itself stated and refuted, the card dies by citation. The genuinely new candidates are the Perelman framing, the $\kappa = 1$ pin with Elgindi-saturation, and the Nash no-collapsing reduction of everything to the single inequality (H).

---

## Handoff

**VERIFIER targets**:
1. Lemma A1 with full quantifiers (two-line argument from the exact local balance; statement-level Lean feasible against the current skeleton's conventions, proof needs the local energy identity).
2. Theorem B1 by symbolic algebra (sympy vector calculus or by-hand IBP; the spectral check above is the mechanical layer, residual $2.0 \times 10^{-16}$).
3. Scale invariance of $\mathcal{W}$ and of the trapped condition as statements alongside `lean/NavierStokes/Scaling.lean`.

**ADVERSARY test cases** (control, parameters, expected/kill readouts):
- (ADV-A1) 2D control, `Flow2D` $n = 64$, $\nu = 0.01$: $\Theta_{2D}$ must show no persistent trapping; checks the Card A wound assessment.
- (ADV-A2) Dyadic intrinsic trapping, $\alpha = 1/3$, $\lambda = 2$, $\nu = 0.1$: uniform trapping with per-shell margin ratio $\approx \lambda^{1/3} = 1.26$; kill K2 if oscillating.
- (ADV-B1) Harnack ratio on TG $32^3$, $\nu = 0.01$, refinement $16^3/24^3/32^3$: kill KB1 if $\mathcal{R} > 1$ sustained and converged.
- (ADV-B2) Hou-Luo $\nu = 0.005$ vs $0.00125$: report $\max_t \mathcal{R}(\nu)$ trend; the $\nu$-sensitivity dial of finding #13 applied to (H).
- (ADV-B3) Shell surrogate on the dyadic blow-up: require $R_n > 1$ (barrier pass); kill KB2 otherwise.

**SURVEYOR precedent queries**: (a) Tao 2016, exact statement on failure of the local energy inequality for the averaged system; (b) stochastic-Lagrangian weighted-enstrophy identities (Constantin-Iyer 2008 and descendants; Eyink; Rezakhanlou): is B1 stated anywhere; (c) Nash/Osada/SSSZ scope for the unconditional on-diagonal kernel bound B3 with drift only in $L^\infty_t L^2_x$; (d) trapped-region or "irreversible collapse criterion" formulations in the CKN literature (Scheffer's work and Choe-Lewis-type local analyses) for Card A priority.
