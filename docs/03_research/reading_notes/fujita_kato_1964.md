# Reading notes: Fujita-Kato (1964) and Kato (1984)

H. Fujita, T. Kato, "On the Navier-Stokes initial value problem. I," Archive for Rational Mechanics and Analysis 16 (1964), 269-315.

T. Kato, "Strong $L^p$-solutions of the Navier-Stokes equation in $\mathbb{R}^m$, with applications to weak solutions," Mathematische Zeitschrift 187 (1984), 471-480.

> These two papers found the critical-space side of the regularity problem. Fujita-Kato recast 3D Navier-Stokes as an abstract semilinear evolution equation driven by the Stokes semigroup, solved it by a contraction (fixed-point) argument in the domain of a fractional power of the Stokes operator, and proved: (i) local-in-time existence of a unique strong solution for arbitrary data in the critical-regularity space, and (ii) global-in-time existence when that critical norm of the data is small. Kato 1984 ported the same machinery from the Hilbert space $\dot H^{1/2}$ to the Lebesgue scale, giving mild solutions in $L^3(\mathbb{R}^3)$, the critical Lebesgue space and the exact space of the Escauriaza-Seregin-Sverak endpoint. This is the load-bearing entry for Architecture 3 (critical spaces and scaling). It is the positive half of the supercriticality story: at the critical scaling level you can close regularity, but only for small data. The control it engages directly is (B), the supercriticality ceiling: $\dot H^{1/2}$ and $L^3$ are exactly critical, the energy norm $L^2$ is supercritical, and the whole drama of the problem lives in the gap between "small critical data" and "any energy-class data."

## Statement

### Notation and the abstract reformulation

Write the incompressible Navier-Stokes system on $\mathbb{R}^3$ (or a smooth domain, or $\mathbb{T}^3$) as

$$\partial_t u - \nu \Delta u + (u\cdot\nabla) u + \nabla p = 0,\qquad \nabla\cdot u = 0,\qquad u(0)=u_0 .$$

Apply the **Leray-Helmholtz projector** $\mathbb{P}$ onto divergence-free fields. The pressure is eliminated and the system becomes a single equation for $u$ in the space of solenoidal fields:

$$\partial_t u + A u = -\,\mathbb{P}\,(u\cdot\nabla)u,\qquad A := -\nu\,\mathbb{P}\Delta ,$$

where $A$ is the **Stokes operator** (on $\mathbb{R}^3$ and $\mathbb{T}^3$, $\mathbb{P}$ commutes with $\Delta$ and $A = -\nu\Delta$ on divergence-free fields). $A$ is a positive self-adjoint operator generating the analytic **Stokes semigroup** $e^{-tA}$, and one can form its fractional powers $A^\alpha$ with domains $D(A^\alpha)$. Fujita and Kato work in $D(A^{1/4})$, which for $\mathbb{R}^3$ coincides (up to the divergence-free constraint) with the homogeneous Sobolev space $\dot H^{1/2}$ of solenoidal fields. The reason $\alpha = 1/4$ is exactly the criticality computation below: $D(A^{1/4}) \simeq \dot H^{2\cdot 1/4} = \dot H^{1/2}$.

### The integral (mild) formulation

Duhamel's principle converts the evolution equation into the fixed-point equation that both papers actually solve:

$$u(t) = e^{-tA}u_0 \;-\; \int_0^t e^{-(t-s)A}\,\mathbb{P}\,\nabla\cdot\big(u(s)\otimes u(s)\big)\,ds .$$

A function $u$ satisfying this integral identity in the relevant function space is a **mild solution**. The nonlinearity is written in divergence form $\nabla\cdot(u\otimes u)$ so that the single derivative can be moved onto the smoothing semigroup kernel. Define the bilinear operator

$$B(u,v)(t) := \int_0^t e^{-(t-s)A}\,\mathbb{P}\,\nabla\cdot\big(u(s)\otimes v(s)\big)\,ds ,$$

so the equation reads $u = e^{-tA}u_0 - B(u,u)$.

### Fujita-Kato 1964: the $\dot H^{1/2}$ theorem

**Theorem (FK, local existence, large data).** Let $u_0 \in D(A^{1/4}) \simeq \dot H^{1/2}(\mathbb{R}^3)$ be divergence-free. Then there is a time $T = T(u_0) > 0$ and a unique mild solution

$$u \in C\big([0,T]; D(A^{1/4})\big),\qquad t^{\,(1/2-1/4)/1}\, A^{1/2}u(t)\ \text{bounded near } t=0,$$

with the parabolic smoothing $u(t) \in D(A^{\beta})$ for $\beta < 1$ and $t > 0$ (so the solution is instantaneously smooth in space for $t > 0$). The solution depends continuously on $u_0$.

**Theorem (FK, global existence, small data).** There is an absolute constant $\varepsilon_0 > 0$ such that if

$$\|u_0\|_{\dot H^{1/2}(\mathbb{R}^3)} \le \varepsilon_0\,\nu ,$$

then $T = +\infty$: the mild solution is global and smooth for all $t > 0$, and $\|u(t)\|_{\dot H^{1/2}}$ stays small. (The smallness threshold scales with viscosity $\nu$; the dimensionless smallness is on $\|u_0\|_{\dot H^{1/2}}/\nu$.)

In their dimension count, 2D is the favorable case: in $\mathbb{R}^2$ the critical Sobolev index is $\dot H^{0} = L^2 =$ energy, so the data norm controlling the fixed point coincides with the conserved energy and the local solution extends to a global one for arbitrary data. The 1964 paper records exactly this dichotomy: global unique strong solutions in 2D for all data, local in 3D for all data and global in 3D for small data. The 2D-global / 3D-local split is the seed of the entire criticality picture (see control A below).

### Kato 1984: the $L^3(\mathbb{R}^m)$ theorem

**Theorem (Kato, local existence in $L^m$).** On $\mathbb{R}^m$ ($m \ge 2$), let $u_0 \in L^m(\mathbb{R}^m)$ be divergence-free. Then there is $T = T(u_0) > 0$ and a unique mild solution

$$u \in C\big([0,T]; L^m(\mathbb{R}^m)\big),\qquad t^{(1-m/q)/2}\,\|u(t)\|_{L^q}\ \text{bounded for } q > m,$$

constructed by the contraction mapping in the **Kato space**: the space of $u$ with $\sup_{0<t<T} t^{(1-m/q)/2}\|u(t)\|_{L^q} < \infty$ for a fixed $q > m$ (together with $u \in BC([0,T];L^m)$). For $m = 3$ this is the critical Lebesgue space $L^3(\mathbb{R}^3)$.

**Theorem (Kato, global existence, small data in $L^m$).** There is $\varepsilon_0 > 0$ such that if $\|u_0\|_{L^m(\mathbb{R}^m)} \le \varepsilon_0\,\nu$, the solution is global.

**Application to weak solutions (the "with applications" of the title).** Kato uses the strong $L^3$ theory to sharpen Leray's structure theory: the strong solution coincides with a Leray-Hopf weak solution where both exist, the strong solution is unique in its class, and the set of singular times of a weak solution is small (the Leray epochs-of-irregularity picture is recovered and sharpened through the $L^m$ smoothing estimates). This is the bridge from Architecture 3 back to Architecture 1.

The crucial point for the project: the controlling norms here, $\|u_0\|_{\dot H^{1/2}}$ and $\|u_0\|_{L^3}$, are **scale invariant** under the Navier-Stokes scaling. That is what makes the two existence times $T(u_0)$ honest critical statements and what makes the smallness condition a statement about a dimensionless quantity, not an artifact of units.

## Method / structure

The mechanism is a **contraction-mapping fixed point** for $\Phi(u) := e^{-tA}u_0 - B(u,u)$ in a Banach space $X_T$ chosen so that the linear term lands in $X_T$ and the bilinear term is a bounded map $X_T \times X_T \to X_T$ with norm small (either because $T$ is small, "large data local," or because $\|u_0\|$ is small, "small data global"). Three estimates carry everything.

1. **Linear smoothing of the Stokes semigroup.** $e^{-tA}$ is analytic, so it trades time decay for derivatives: in the Sobolev setting,
$$\|A^{\sigma} e^{-tA} f\|_{L^2} \lesssim t^{-(\sigma-\rho)}\|A^{\rho}f\|_{L^2}\quad(\sigma \ge \rho),$$
and in the Lebesgue setting (the heat-type $L^p$-$L^q$ estimates Kato uses),
$$\|e^{-tA} f\|_{L^q} \lesssim t^{-\frac{m}{2}(\frac1p-\frac1q)}\|f\|_{L^p},\qquad \|\nabla e^{-tA} f\|_{L^q}\lesssim t^{-\frac12-\frac{m}{2}(\frac1p-\frac1q)}\|f\|_{L^p}.$$
The single $\nabla$ from the divergence-form nonlinearity costs one extra half-power $t^{-1/2}$, which is exactly integrable in time precisely at the critical exponent and not below it.

2. **The bilinear estimate.** Combining the gradient smoothing with Holder gives, in the Kato space with weight $t^{(1-m/q)/2}$,
$$\|B(u,v)\|_{X_T} \le C\,\|u\|_{X_T}\,\|v\|_{X_T},$$
with $C$ independent of $T$ at the critical exponent (this scale invariance of $C$ is the signature of working at criticality). The time integral $\int_0^t (t-s)^{-1/2 - \cdots} s^{-\cdots}\,ds$ is a Beta integral that converges exactly when the exponents sum to the critical value.

3. **The abstract fixed-point lemma.** If $\|y\|_{X} \le \eta$ (here $y = e^{-tA}u_0$) and $B$ is bounded bilinear with constant $C$, then $u = y - B(u,u)$ has a unique small solution provided $4C\eta < 1$. For **small data**, $\eta = \|e^{-\cdot A}u_0\|_{X_\infty} \lesssim \|u_0\|_{\text{critical}}$ is small by hypothesis and $T=\infty$ works. For **large data local**, $\eta = \|e^{-\cdot A}u_0\|_{X_T} \to 0$ as $T \to 0$ (the tail of the linear evolution in the weighted norm vanishes as the time window shrinks), so a small enough $T$ makes $4C\eta<1$. This single lemma produces both halves, and the difference between them is entirely whether the smallness comes from the data or from the time window.

Where the structural objects enter:

- The **Leray projector** $\mathbb{P}$ enters at the very start, removing the pressure and turning the constrained PDE into an unconstrained evolution equation. The pressure is recovered a posteriori from $-\Delta p = \nabla\cdot\nabla\cdot(u\otimes u)$.
- **Vortex stretching $\omega\cdot\nabla u$ does not appear explicitly.** The method works at the velocity level in critical norms; the stretching nonlinearity is hidden inside the generic quadratic term $\mathbb{P}\nabla\cdot(u\otimes u)$. This is important for control A below: the proof does not distinguish 2D from 3D by any structural use of stretching; it distinguishes them only by the dimension count of the critical Sobolev index. That is exactly why the method is honest about being small-data only in 3D.
- **Viscosity is essential and visible.** Every smoothing estimate is a property of $e^{-tA} = e^{\nu t\Delta}$ (on divergence-free fields). With $\nu = 0$ there is no smoothing kernel, $B$ is not bounded, and the fixed point does not close. So the method is not blind to viscosity (control C); it is built entirely on it.

## Criticality placement

Apply the Navier-Stokes scaling $u_\lambda(x,t) = \lambda\,u(\lambda x, \lambda^2 t)$, $p_\lambda(x,t)=\lambda^2 p(\lambda x,\lambda^2 t)$, and read off the spatial-norm scaling exponents from the criticality bookkeeper `experiments/_shared/criticality.py`.

- **$\dot H^{1/2}(\mathbb{R}^3)$.** `homogeneous_sobolev_exponent(1/2, 3)` returns $1 + s - d/2 = 1 + 1/2 - 3/2 = 0$. Exponent $0$: **CRITICAL**, scale invariant. $\|u_{0,\lambda}\|_{\dot H^{1/2}} = \|u_0\|_{\dot H^{1/2}}$. This is the reason $\dot H^{1/2}$ is *the* Hilbert critical space and why the Fujita-Kato fixed point closes without a scale-dependent constant.
- **$L^3(\mathbb{R}^3)$.** `lebesgue_exponent(3, 3)` returns $1 - d/q = 1 - 3/3 = 0$. Exponent $0$: **CRITICAL**. The Kato 1984 space sits at the same scaling level as $\dot H^{1/2}$ (in fact $\dot H^{1/2}(\mathbb{R}^3)\hookrightarrow L^3(\mathbb{R}^3)$ by Sobolev embedding, so $L^3$ is a strictly larger critical space, which is why Kato 1984 is a genuine extension, not a translation).
- **Energy $L^2(\mathbb{R}^3)$.** `lebesgue_exponent(2, 3)` returns $1 - 3/2 = -1/2$. Exponent $-1/2 < 0$: **SUPERCRITICAL**. This is the gap. The only globally coercive a priori bound is the energy, and it sits half a derivative below the critical threshold $\dot H^{1/2}$.

Running these through `audit_estimate`: a method controlling $\dot H^{1/2}$ or $L^3$ returns verdict `AT_THE_MARGIN` ("bounding it would close regularity, but no all-time a priori bound at this level is known; this is exactly the gap"). A method controlling only $L^2$ returns `INSUFFICIENT_BY_ITSELF`. Fujita-Kato and Kato live at `AT_THE_MARGIN`: they *do* control the critical norm, but only conditionally (small data, or short time), never as a global a priori bound for arbitrary data. The fixed point gives the bound; it does not produce it from a conservation law.

The clean way to state the placement: **Fujita-Kato proves that smallness of a critical norm is sufficient for global regularity, and the local theory shows the critical norm is the right currency. What is missing is any mechanism forcing the critical norm to stay small (or even finite) for large data.** The energy cannot supply it because the energy is supercritical and $L^2 \not\hookrightarrow L^3$, $L^2 \not\hookrightarrow \dot H^{1/2}$ in 3D. The half-derivative gap between $L^2$ and $\dot H^{1/2}$ is, quantitatively, the supercriticality gap (Direction 03).

A note on the subcritical local theory versus the critical small-data theory. If one runs the same fixed point in a **subcritical** space, for example $\dot H^{s}$ with $s > 1/2$ or $H^1$, the bilinear constant $C$ carries a positive power of $T$ (because the norm is subcritical, exponent $> 0$ in the bookkeeper), so large-data local existence is even easier, but the global small-data threshold becomes scale dependent and the statement loses its clean dimensionless form. The genius of choosing $s = 1/2$ is that the local time and the small-data threshold both become scale invariant, which is what makes the result the correct structural statement rather than one convenient choice among many.

## Against the three controls

**(A) 2D must stay smooth.** The method passes, and informatively. In $\mathbb{R}^2$ the critical Sobolev index is $1 + s - d/2 = 0 \Rightarrow s = 0$, i.e. the critical space is $\dot H^0 = L^2$, which is exactly the conserved energy. So in 2D the small-data threshold is automatically met by every finite-energy datum after the energy bound is invoked, and the local solution is global for all data. The same fixed point that gives only small-data global existence in 3D gives unconditional global existence in 2D, because in 2D the critical norm and the coercive norm coincide. This is the textbook instance of control A working correctly: a method that respects criticality reproduces 2D global smoothness for the right structural reason (the dimension count), not by accident. Crucially, the method does **not** falsely predict 2D blow-up, and it does not pretend to give 3D large-data global existence. It is honest about the dimension where the coercive norm meets the critical norm. (The method does not use the absence of vortex stretching in 2D directly; it uses the equivalent fact that the critical index drops to the energy level. These are two faces of the same scaling truth.)

**(B) Supercriticality ceiling.** This is the control the source most directly illuminates. Fujita-Kato is the positive statement at the critical level: it shows the critical norm is sufficient. It does not breach the ceiling, because it never produces a global a priori bound on the critical norm for large data. It converts the regularity problem into the sharper question "can the critical norm blow up?" which is precisely the question ESS (2003) answers at the endpoint ($L^3$ cannot stay bounded at a singularity) and Tao (2019) quantifies. Fujita-Kato sits at the margin (exponent $0$) and shows the margin is the right place to stand; the ceiling is intact because no coercive critical quantity is exhibited.

**(C) Viscosity / exact structure.** The method passes cleanly and is built on viscosity: every estimate is a smoothing property of $e^{\nu t\Delta}$, and the small-data threshold scales with $\nu$. Set $\nu = 0$ (Euler) and the construction collapses, consistent with the inviscid controls (Burgers shocks, Elgindi Euler blow-up). The method does **not** use the exact transport-plus-pressure structure beyond the generic divergence-form quadratic bound; it treats the nonlinearity as an abstract bounded bilinear map. This is the limitation that connects to the Tao 2016 barrier (Direction 04): the averaged Navier-Stokes system has the same Duhamel structure, the same scaling, the same energy identity, and the same Fujita-Kato small-data theory, yet it blows up for large data. So Fujita-Kato, being a soft (structure-agnostic) argument, cannot by itself reach large data; the large-data closure must use the exact nonlinearity that averaging destroys. The fixed point is the right tool for the small-data regime and provably the wrong tool, alone, for the large-data regime.

This is the precise sense in which the source is a coordinate, not a wall: it pins down that the critical norm is the right object (compass heading), it shows the energy cannot reach it (the gap is half a derivative in 3D), and it shows the gap cannot be soft (the barrier). The remaining work is exactly to add a genuinely critical, structure-using, coercive control. That is Direction 03.

## What it gives / what it does not give

**Gives:**

- A unique, smooth-for-$t>0$ local solution for arbitrary divergence-free $u_0 \in \dot H^{1/2}(\mathbb{R}^3)$ (FK) or $u_0 \in L^3(\mathbb{R}^3)$ (Kato), via the contraction mapping in the critical space. Uniqueness is in the strong (Kato-space) class.
- Global smooth solutions when the critical norm of the data is small relative to viscosity. This is the first rigorous global 3D existence statement of its kind and the template for all later critical-space well-posedness (Fujita-Kato $\to$ Kato $L^3$ $\to$ Cannone/Planchon Besov $\to$ Koch-Tataru $\mathrm{BMO}^{-1}$).
- The structural reformulation (Leray projector, Stokes semigroup, Duhamel, fractional powers, mild solutions) that the entire modern critical theory is written in. Every Architecture 3 result is a refinement of this scaffold.
- A bridge to Architecture 1: Kato 1984 sharpens Leray-Hopf structure theory (uniqueness in the strong class, smallness of the singular-time set, weak-strong uniqueness).

**Does not give (the gap to closing regularity):**

- **No large-data global existence in 3D.** The smallness $\|u_0\|_{\dot H^{1/2}} \lesssim \nu$ (or $\|u_0\|_{L^3}\lesssim\nu$) is essential to the fixed point and there is no known way to remove it by this method. The Clay problem is precisely the large-data case.
- **No coercive critical quantity.** The fixed point produces a bound on the critical norm; it does not exhibit a conserved or monotone critical quantity. The supercriticality gap is untouched: between the supercritical coercive energy ($L^2$, exponent $-1/2$) and the critical sufficient norm ($\dot H^{1/2}$, exponent $0$) there is no bridge.
- **No use of the exact 3D structure.** The argument is structure-agnostic (generic bilinear bound) and therefore equally proves small-data global existence for Tao's averaged system, which blows up for large data. So the method, alone, *cannot* be the route to large-data 3D regularity; that route must engage the exact nonlinearity (Direction 03, Direction 04).
- **Continuation, not prevention.** Combined with ESS, the picture is: the solution stays smooth as long as $\|u(t)\|_{L^3}$ (or $\dot H^{1/2}$) stays finite, and it must blow up there if it blows up at all. Fujita-Kato-Kato builds the solution and identifies the critical currency; ESS proves the currency is sharp; neither bounds the currency for large data. That bounding is the open problem.

The honest one-line summary for the program: **this is the proof that the critical scaling level is where regularity is decided, plus a proof that you win there for small data. It converts the Millennium problem into "control the critical norm for large data," which is the cleanest possible restatement and is exactly as hard as the original.**

## Lineage and sharpest known form

**Builds on.** Leray (1934, weak solutions and the smoothing/structure theory), Hopf (1951, the Leray-Hopf class). The functional-analytic engine (analytic semigroups, fractional powers, $D(A^\alpha)$) is Kato's own operator theory applied to the Stokes operator. The 2D global / 3D local dichotomy is already implicit in Leray; Fujita-Kato made it the explicit consequence of a criticality count.

**Built on it (the critical-space tower).**

- T. Kato (1984): the $L^3(\mathbb{R}^3)$ extension above, the first move off the Hilbert space onto the Lebesgue scale. $L^3 \supset \dot H^{1/2}$, a strictly larger critical space.
- Y. Giga, T. Miyakawa (1980s): mild solutions and self-similar solutions via the same semigroup machinery; Giga's uniqueness in $C([0,T];L^3)$.
- M. Cannone, F. Planchon, M. Cannone-Y. Meyer (1990s): global small-data solutions in critical **Besov spaces** $\dot B^{-1+3/p}_{p,\infty}$, larger than $L^3$, allowing highly oscillatory large-amplitude data with small Besov norm.
- H. Koch, D. Tataru, "Well-posedness for the Navier-Stokes equations," Adv. Math. 157 (2001): global small-data well-posedness in $\mathrm{BMO}^{-1}$ (= $\partial \mathrm{BMO}$), the **largest known critical space** in the FK chain (bookkeeper: $\mathrm{BMO}^{-1}$ exponent $0$, CRITICAL). See the companion note `koch_tataru_2001.md` (pending). This is the current endpoint of "how large a critical space can the small-data fixed point reach."
- J. Bourgain, N. Pavlovic (2008): ill-posedness ("norm inflation") in $\dot B^{-1}_{\infty,\infty}$, the one critical Besov space just beyond $\mathrm{BMO}^{-1}$, showing the small-data critical theory has a genuine outer boundary. This marks where the Fujita-Kato strategy provably stops.

**Where the large-data question went (the other half).**

- The endpoint criticality criterion: Escauriaza-Seregin-Sverak (2003), $L^\infty_t L^3_x$ regularity, the sharp statement that the critical $L^3$ norm must blow up at a singularity (see `escauriaza_seregin_sverak_2003.md`). FK identifies $L^3$ as the currency; ESS proves it is the sharp currency.
- Quantitative ESS: T. Tao (2019), a triple-logarithmic lower bound on the rate at which $\|u(t)\|_{L^3}$ must concentrate at a singularity; Barker-Prange and others have pushed the quantitative/local versions. These are the Direction 01 leads: turn the conditional critical criterion into a self-improving quantitative one.
- The barrier: T. Tao (2016), finite-time blow-up for an averaged Navier-Stokes that shares the FK small-data theory, energy identity, and scaling. This is the proof that the FK soft argument cannot extend to large data (Direction 04).

**Sharpest known form, as of 2025.** For *small* critical data, the strongest statement remains the $\mathrm{BMO}^{-1}$ small-data global well-posedness of Koch-Tataru (2001), refined in the intervening years (uniqueness classes, analyticity and decay of the small-data solution, and local-in-space variants), with $\dot B^{-1}_{\infty,\infty}$ ill-posedness (Bourgain-Pavlovic, and Germain) marking the boundary. For *large* data the Fujita-Kato program gives, and still gives, only local existence; the global question is open and is the Clay problem. No critical space strictly larger than $\mathrm{BMO}^{-1}$ is known to support the small-data global theory, and the program is understood (post Tao 2016) to be intrinsically small-data: the missing large-data ingredient must be a genuinely critical, structure-using coercive control of the kind catalogued in Direction 03, not a further enlargement of the critical space. (The exact optimal constant $\varepsilon_0$ in the FK/Kato smallness threshold, and its sharp dependence on $\nu$ and on the precise critical norm, are space-dependent and not pinned to a single universal value; treat $\|u_0\|_{\dot H^{1/2}} \le \varepsilon_0\,\nu$ as the dimensionally correct form with an unspecified absolute $\varepsilon_0$. (verify))

## References

- H. Fujita, T. Kato, "On the Navier-Stokes initial value problem. I," Archive for Rational Mechanics and Analysis 16 (1964), 269-315.
- T. Kato, "Strong $L^p$-solutions of the Navier-Stokes equation in $\mathbb{R}^m$, with applications to weak solutions," Mathematische Zeitschrift 187 (1984), 471-480. DOI 10.1007/BF01174182.
- J. Leray, "Sur le mouvement d'un liquide visqueux emplissant l'espace," Acta Mathematica 63 (1934), 193-248.
- E. Hopf, "Uber die Anfangswertaufgabe fur die hydrodynamischen Grundgleichungen," Mathematische Nachrichten 4 (1951), 213-231.
- Y. Giga, T. Miyakawa, "Solutions in $L_r$ of the Navier-Stokes initial value problem," Arch. Rational Mech. Anal. 89 (1985), 267-281.
- M. Cannone, "Ondelettes, paraproduits et Navier-Stokes," Diderot (1995); M. Cannone, Y. Meyer, F. Planchon, critical Besov-space solutions (1990s).
- H. Koch, D. Tataru, "Well-posedness for the Navier-Stokes equations," Advances in Mathematics 157 (2001), 22-35.
- J. Bourgain, N. Pavlovic, "Ill-posedness of the Navier-Stokes equations in a critical space in 3D," J. Funct. Anal. 255 (2008), 2233-2247.
- L. Escauriaza, G. Seregin, V. Sverak, "$L_{3,\infty}$-solutions of Navier-Stokes equations and backward uniqueness," Russian Math. Surveys 58 (2003), 211-250.
- T. Tao, "Quantitative bounds for critically bounded solutions to the Navier-Stokes equations," (2019/2021).
- T. Tao, "Finite time blowup for an averaged three-dimensional Navier-Stokes equation," J. Amer. Math. Soc. 29 (2016), 601-674.

## Cross-links

- Direction 03, the supercriticality gap (the home direction for this source): [`../research_directions/03_supercriticality_gap.md`](../research_directions/03_supercriticality_gap.md). FK pins the critical level; Direction 03 is the search for a coercive quantity there.
- Direction 01, critical continuation criteria: [`../research_directions/01_critical_continuation_criteria.md`](../research_directions/01_critical_continuation_criteria.md). FK identifies the critical norm; ESS and the quantitative refinements live here.
- Direction 04, blow-up and barriers: [`../research_directions/04_blowup_and_barriers.md`](../research_directions/04_blowup_and_barriers.md). The Tao 2016 barrier is why the FK soft argument cannot reach large data.
- Sibling notes: [`escauriaza_seregin_sverak_2003.md`](escauriaza_seregin_sverak_2003.md) (the sharp $L^3$ endpoint, the same critical currency as Kato 1984), [`leray_1934.md`](leray_1934.md) (weak solutions and the structure theory FK refines), [`tao_2016_averaged.md`](tao_2016_averaged.md) (the barrier), [`beale_kato_majda_1984.md`](beale_kato_majda_1984.md) (the vorticity continuation criterion, a different critical currency).
- Criticality bookkeeper: [`../../../experiments/_shared/criticality.py`](../../../experiments/_shared/criticality.py). `homogeneous_sobolev_exponent(1/2, 3) = 0`, `lebesgue_exponent(3, 3) = 0`, `lebesgue_exponent(2, 3) = -1/2`.

## What this enables / what remains open

**Enables.** This note fixes, for BUILDER and SYNTHESIZER, the exact statement of the positive critical-space result: small critical data gives global 3D regularity, via a structure-agnostic contraction mapping in $\dot H^{1/2}$ or $L^3$. It gives the precise scaling placement (both spaces exponent $0$, critical; energy exponent $-1/2$, supercritical) and the precise reason the method is small-data only (the fixed point needs $4C\eta < 1$ and there is no coercive critical bound to make $\eta$ small for large data). For BUILDER, the actionable target is Direction 03: any candidate coercive critical quantity should be tested for whether it would have *removed* the smallness assumption here, and must fail the averaged-NS check (or it is the energy in disguise / a soft quantity).

**Remains open (handoff to ADVERSARY).**

1. The large-data global question itself (the Clay problem), restated by FK as "control the critical norm for large data."
2. Whether any critical space strictly larger than $\mathrm{BMO}^{-1}$ supports small-data global well-posedness (boundary marked by $\dot B^{-1}_{\infty,\infty}$ ill-posedness; this is a sharp-frontier question, not the regularity question).
3. The precise sharp smallness constant and its $\nu$-dependence across the critical-space chain (flagged "(verify)" above; minor, but a SURVEYOR should not assert a universal constant).
4. ADVERSARY check to log: confirm the claim that the averaged Navier-Stokes system admits the same Fujita-Kato small-data theory (it does, by the same Duhamel/bilinear structure), since that claim is what makes "FK cannot reach large data" rigorous and it is asserted here from structural reasoning rather than a line-by-line reading of Tao 2016.

**Discrepancy log.** No disagreement with the existing project analyses. This note is consistent with `escauriaza_seregin_sverak_2003.md` (same critical $L^3$ currency), with `tao_2016_averaged.md` (the barrier explanation of why FK is small-data only), and with the bookkeeper's exponents ($\dot H^{1/2}$ and $L^3$ critical, $L^2$ supercritical). One emphasis to flag for SYNTHESIZER: the project framing sometimes lists "$\dot H^{1/2}$, $L^3$, $\mathrm{BMO}^{-1}$ are critical" as a flat set; this note records the strict ordering $\dot H^{1/2} \hookrightarrow L^3 \hookrightarrow \mathrm{BMO}^{-1}$ (all critical, increasing in size), which is the correct structural refinement and explains why Kato 1984 and Koch-Tataru 2001 are genuine extensions of Fujita-Kato 1964 rather than restatements.
