# Reading notes: Koch-Tataru (2001)

Herbert Koch, Daniel Tataru, "Well-posedness for the Navier-Stokes equations," Advances in Mathematics **157** (2001), no. 1, 22-35.

> This is the endpoint of the critical small-data program (Architecture 3). It proves global well-posedness of the 3D incompressible Navier-Stokes equations for data small in $\mathrm{BMO}^{-1}$, the largest function space in the known scale of critical spaces. Every smaller critical space ($\dot H^{1/2}$, $L^3$, the Besov family $\dot B^{-1+3/q}_{q,\infty}$ for $q < \infty$) embeds continuously into $\mathrm{BMO}^{-1}$, so Koch-Tataru subsumes Fujita-Kato and Kato's $L^3$ theorem in a single statement. It engages structural control (B): it lives exactly at the critical scaling level, which is the level a regularity proof must reach, and it shows that the perturbative fixed-point method reaches that level for small data but stops there. The boundary just beyond it, ill-posedness in $\dot B^{-1}_{\infty,\infty}$ (Bourgain-Pavlovic), marks the exact edge of the small-data critical program. Large data remains blocked by the same supercriticality of the energy that blocks everything else.

This note is the Architecture 3 partner to the [Escauriaza-Seregin-Sverak](escauriaza_seregin_sverak_2003.md) note (the critical-continuation side) and the [Beale-Kato-Majda](beale_kato_majda_1984.md) note (the vorticity side). It is the upper end of the critical-space ladder; ESS is the upper end of the critical-Lebesgue-continuation ladder.

---

## Statement

Write the incompressible Navier-Stokes system on $\mathbb{R}^n$ ($n \ge 3$, the case of interest is $n = 3$), with viscosity normalized to $1$:

$$\partial_t u - \Delta u + (u \cdot \nabla) u + \nabla p = 0, \qquad \nabla \cdot u = 0, \qquad u(\cdot, 0) = u_0 .$$

Apply the Leray projector $\mathbb{P} = I - \nabla \Delta^{-1} \nabla\cdot$ onto divergence-free fields to eliminate the pressure. The system becomes the integral (mild) equation, with $e^{t\Delta}$ the heat semigroup,

$$u(t) = e^{t\Delta} u_0 - \int_0^t e^{(t-s)\Delta}\, \mathbb{P}\, \nabla \cdot \big(u(s) \otimes u(s)\big)\, ds \;=:\; e^{t\Delta} u_0 + B(u, u)(t) .$$

### The space $\mathrm{BMO}^{-1}$

A tempered distribution $f$ on $\mathbb{R}^n$ lies in $\mathrm{BMO}^{-1}$ (also written $\mathrm{BMO}^{-1}$ or $\partial \mathrm{BMO}$, the space of distributional derivatives of $\mathrm{BMO}$ functions) iff the heat extension $e^{t\Delta} f$ satisfies the Carleson-measure condition

$$\| f \|_{\mathrm{BMO}^{-1}}^2 \;:=\; \sup_{x \in \mathbb{R}^n,\, R > 0} \; \frac{1}{|B_R(x)|} \int_0^{R^2} \int_{B_R(x)} \big| (e^{t\Delta} f)(y) \big|^2 \, dy \, dt \;<\; \infty .$$

Equivalently $f \in \mathrm{BMO}^{-1}$ iff $f = \sum_j \partial_j f_j$ with each $f_j \in \mathrm{BMO}$. The Carleson measure is $d\mu = |e^{t\Delta} f|^2\, dy\, dt$ over the upper half-space $\mathbb{R}^n \times (0, \infty)$, and the condition is that $\mu$ is a Carleson measure with norm equal to $\|f\|_{\mathrm{BMO}^{-1}}^2$. This is the parabolic analogue of Fefferman-Stein's characterization of $\mathrm{BMO}$ via Carleson measures of the Poisson extension.

### The solution space $X$

Koch and Tataru solve the fixed point in a space $X$ (sometimes written $X_T$ or $\mathcal{X}$) whose norm is built to mirror the Carleson structure of the data and to be scale invariant. With $Q_R(x) = B_R(x) \times (0, R^2)$ the parabolic cylinder, the working norm is, schematically,

$$\| u \|_{X} \;:=\; \sup_{t > 0} \; t^{1/2} \, \| u(t) \|_{L^\infty}\;\; +\;\; \sup_{x,\, R} \left( \frac{1}{|B_R(x)|} \int_0^{R^2} \int_{B_R(x)} |u(y, t)|^2 \, dy\, dt \right)^{1/2}.$$

The first piece is a pointwise decay matching the heat-kernel smoothing ($t^{1/2}\|e^{t\Delta} u_0\|_{L^\infty} \lesssim \|u_0\|_{\mathrm{BMO}^{-1}}$); the second is the Carleson/local-energy piece. A field in $X$ is exactly one whose heat-type evolution carries the same Carleson budget as a $\mathrm{BMO}^{-1}$ datum. Both pieces are invariant under the parabolic rescaling below, so $\|\cdot\|_X$ is critical.

### The theorem

**Theorem (Koch-Tataru 2001).** There is a constant $\varepsilon = \varepsilon(n) > 0$ such that for every divergence-free $u_0 \in \mathrm{BMO}^{-1}(\mathbb{R}^n)$ with

$$\| u_0 \|_{\mathrm{BMO}^{-1}} < \varepsilon ,$$

the mild equation has a unique global solution $u \in X$, and the solution depends analytically on $u_0$. The map $u_0 \mapsto u$ is real-analytic in a $\mathrm{BMO}^{-1}$-ball; in particular the data-to-solution map is Lipschitz (indeed smooth) near $0$. The solution is smooth for $t > 0$ and global in time.

The smallness is in the scale-invariant norm $\|u_0\|_{\mathrm{BMO}^{-1}}$, so by scaling it is not a smallness of physical size but a smallness of the critical-norm content of the data. A datum can be large in $L^2$ (large energy) yet small in $\mathrm{BMO}^{-1}$, and the theorem still applies; this is the usual feature of critical small-data theorems and is what makes them say something the energy cannot.

Koch-Tataru also prove a local-in-time existence statement for data in the closure of test functions in $\mathrm{BMO}^{-1}$ (the "$\mathrm{vmo}^{-1}$" predual-type subspace), where the smallness is bought from a short time interval rather than from small norm; this is the analogue of local existence for arbitrary $\dot H^{1/2}$ data.

---

## The critical-space ladder

The known scale of critical (scale-invariant) spaces for 3D Navier-Stokes data, ordered by inclusion, is

$$\dot H^{1/2}(\mathbb{R}^3) \;\hookrightarrow\; L^3(\mathbb{R}^3) \;\hookrightarrow\; \dot B^{-1+3/q}_{q,\infty}(\mathbb{R}^3)\;\;(3 < q < \infty)\;\hookrightarrow\; \mathrm{BMO}^{-1}(\mathbb{R}^3) \;\hookrightarrow\; \dot B^{-1}_{\infty,\infty}(\mathbb{R}^3) .$$

Every space in this chain is invariant under the NS data rescaling $u_0 \mapsto \lambda\, u_0(\lambda \cdot)$. Reading the chain:

- $\dot H^{1/2}$ is the Fujita-Kato space (1964): the critical Sobolev space, smallest in the chain, smallest small-data theorem.
- $L^3$ is the Kato (1984) space and the ESS (2003) endpoint on the continuation side.
- $\dot B^{-1+3/q}_{q,\infty}$, $q < \infty$, are the Cannone-Meyer-Planchon Besov spaces; as $q \to \infty$ the space grows. The case $q = \infty$ formally gives $\dot B^{-1}_{\infty,\infty}$.
- $\mathrm{BMO}^{-1}$ is strictly larger than every $\dot B^{-1+3/q}_{q,\infty}$ with $q < \infty$ and strictly smaller than $\dot B^{-1}_{\infty,\infty}$. It is the **largest space in which small-data global well-posedness is known**.
- $\dot B^{-1}_{\infty,\infty}$ is the largest critical space, the formal endpoint $q = \infty$. Well-posedness here is **false** (Bourgain-Pavlovic 2008; see below). So $\mathrm{BMO}^{-1}$ and $\dot B^{-1}_{\infty,\infty}$ straddle the boundary between well-posed and ill-posed at the critical level.

The single-line takeaway for the project: Koch-Tataru pushed the small-data critical program to the largest space where it can run, and the very next space is where it provably breaks. The critical-space attack on regularity is therefore not blocked by lack of a large enough space; it is blocked by the smallness hypothesis, which the energy cannot remove.

---

## Method / structure

The proof is a fixed point for the mild equation $u = e^{t\Delta} u_0 + B(u, u)$ in the Banach space $X$, run by the contraction-mapping / Picard iteration. The whole content is in two estimates.

### 1. The linear estimate (data enters $X$)

$$\| e^{t\Delta} u_0 \|_{X} \;\lesssim\; \| u_0 \|_{\mathrm{BMO}^{-1}} .$$

This is essentially the definition of $\mathrm{BMO}^{-1}$ via the Carleson condition: the Carleson piece of $\|e^{t\Delta} u_0\|_X$ *is* $\|u_0\|_{\mathrm{BMO}^{-1}}$ by construction, and the $t^{1/2}\|\cdot\|_{L^\infty}$ piece follows from the heat-kernel pointwise bound for $\mathrm{BMO}^{-1}$ data. So the space $X$ is reverse-engineered from the data space precisely to make this trivial. This is the design insight: choose the iteration space so that the linear term lands in it isometrically.

### 2. The bilinear estimate (the heart)

$$\| B(u, v) \|_{X} \;\lesssim\; \| u \|_{X} \, \| v \|_{X} ,$$

where $B(u, v)(t) = -\int_0^t e^{(t-s)\Delta}\, \mathbb{P}\, \nabla \cdot (u \otimes v)(s)\, ds$. Granting this, the map $u \mapsto e^{t\Delta} u_0 + B(u, u)$ is a contraction on a small ball of $X$ once $\|u_0\|_{\mathrm{BMO}^{-1}} < \varepsilon$, by the standard quadratic fixed-point lemma (if $\|y\| \le \delta$ and $\|B(u,v)\| \le C\|u\|\|v\|$ then $u = y + B(u,u)$ has a unique small solution when $4C\delta < 1$). Uniqueness, analyticity in $u_0$, and global existence all come for free from the abstract lemma.

The bilinear estimate is where the work is, and where the Carleson-measure machinery is indispensable. The kernel of $B$ combines the Leray projector $\mathbb{P}$ (a Calderon-Zygmund operator of order $0$), one derivative $\nabla\cdot$, and the heat semigroup $e^{(t-s)\Delta}$. The $L^\infty$ piece of the $X$-norm is controlled by an off-diagonal heat-kernel bound; the **Carleson piece is controlled by a parabolic Carleson-measure / square-function estimate**, the technically novel ingredient. Koch and Tataru show the bilinear form maps the Carleson budget of two inputs into the Carleson budget of the output, using that $\mathbb{P}\nabla\cdot e^{(t-s)\Delta}$ has a kernel with Gaussian off-diagonal decay and the right homogeneity. The $\mathbb{P}$ and the divergence-free constraint matter: without the projector the pressure term would not be controlled, and the estimate uses the cancellation $\nabla \cdot (u \otimes v)$ with $\nabla \cdot u = 0$.

The structural point for this project: the proof is **perturbative**. It controls the nonlinearity $B(u,u)$ by the *same* norm it controls the linear evolution, and closes because $\|B(u,u)\|_X \lesssim \|u\|_X^2$ is quadratically small when $\|u\|_X$ is small. There is no monotone quantity, no coercive a priori bound, no use of the energy identity, and no use of 3D vortex stretching. It is a small-data contraction, full stop. That is its power (it reaches the largest critical space) and its ceiling (small data only).

---

## Criticality placement

Under the Navier-Stokes scaling $u_\lambda(x, t) = \lambda\, u(\lambda x, \lambda^2 t)$, $p_\lambda(x, t) = \lambda^2 p(\lambda x, \lambda^2 t)$, the corresponding data rescaling is $u_0 \mapsto \lambda\, u_0(\lambda \cdot)$.

- **$\mathrm{BMO}^{-1}$ is exactly critical.** $\|\lambda\, u_0(\lambda \cdot)\|_{\mathrm{BMO}^{-1}} = \|u_0\|_{\mathrm{BMO}^{-1}}$: the Carleson supremum is taken over all $(x, R)$, and the rescaling permutes the parabolic cylinders $Q_R(x)$ while leaving the normalized local-energy integral invariant. The criticality bookkeeper returns scaling exponent $0$ for $\mathrm{BMO}^{-1}$: see `bmo_inverse_exponent` in `experiments/_shared/criticality.py`, which returns `Fraction(0)` because scale invariance is the defining property of the Koch-Tataru space.
- **The solution norm $\|\cdot\|_X$ is critical.** Both pieces are parabolic-scale invariant by construction; $u \mapsto u_\lambda$ preserves $\|u\|_X$. This is mandatory: a global small-data theorem at the critical level requires a scale-invariant iteration space, or else the rescaled data would fall out of the small ball.
- **Place on the ladder.** Running the bookkeeper's `standard_norms_3d()` table: $\dot H^{1/2}$ has exponent $1 + \tfrac12 - \tfrac32 = 0$ (critical), $L^3$ has exponent $1 - \tfrac33 = 0$ (critical), $\mathrm{BMO}^{-1}$ has exponent $0$ (critical). All three are critical, and the inclusions $\dot H^{1/2} \hookrightarrow L^3 \hookrightarrow \mathrm{BMO}^{-1}$ are inclusions *within* the critical level, ordered by size. Koch-Tataru is the largest-space member of the critical small-data family.

Why this matters for control (B): regularity is a critical-or-subcritical statement (the criticality bookkeeper's verdict `AT_THE_MARGIN` for any critical controlling norm). Koch-Tataru is a theorem *at the margin*: it controls a critical norm, but only when that norm is small. It does not produce an a priori bound on $\|u(t)\|_{\mathrm{BMO}^{-1}}$ for large data; the smallness is an input, not an output. The energy gives $L^\infty_t L^2_x$ (exponent $-\tfrac12$, supercritical), which does not embed into $\mathrm{BMO}^{-1}$ and does not bound it. So there is no path from the global energy bound to the Koch-Tataru smallness, which is exactly the supercriticality gap restated in the largest critical space. This is the cleanest single statement of why "the largest known critical space" still leaves the millennium problem open.

---

## Against the three controls

- **(A) 2D control.** Koch-Tataru is dimension-agnostic ($n \ge 3$ in the paper, and the same proof runs verbatim in $n = 2$). It does **not** use 3D vortex stretching $\omega \cdot \nabla u$. This is the correct behavior for a small-data critical theorem and is *not* a red flag here, because the theorem makes no claim about large data and therefore makes no false prediction about 2D large-data blow-up. The 2D control (A) fires only against methods that would predict 2D blow-up; Koch-Tataru predicts global smoothness for small data in every dimension, which is true in 2D, so it passes (A) trivially. The honest reading is that Koch-Tataru is *orthogonal* to control (A): it never engages the stretching term, because the small-data regime never needs to. A regularity proof for large data must engage it; Koch-Tataru shows the perturbative method reaches the critical level without it, and stops.
- **(B) Supercriticality ceiling.** This is the control Koch-Tataru most sharply illuminates. It reaches the critical level (good), but only with smallness (the ceiling). It supplies no coercive global-in-time quantity at the critical level. The only global a priori bound remains the supercritical energy. So Koch-Tataru does not lower the ceiling; it shows precisely how high the perturbative method climbs (the largest critical space) before the ceiling stops it. Verdict from `audit_estimate` on a critical controlling norm: `AT_THE_MARGIN`, "bounding it would close regularity, but no all-time a priori bound at this level is known."
- **(C) Viscosity control.** The proof is built on the heat semigroup $e^{t\Delta}$ and its parabolic smoothing; the Carleson-measure norm is a *parabolic* (heat-extension) object. The whole estimate would collapse at $\nu = 0$ (Euler): there is no $e^{t\Delta}$ to smooth, no Carleson budget to carry, and the $t^{1/2}\|u\|_{L^\infty}$ decay is heat-kernel decay. So the method is fully viscosity-aware and passes (C). It is, if anything, *maximally* viscosity-dependent: it is a theorem about the parabolic regularization of critical data and has no inviscid analogue.

Net: Koch-Tataru passes (C) emphatically, passes (A) vacuously (it is orthogonal to stretching), and is the cleanest illustration of (B). It is a correct, sharp, perturbative theorem that maps the upper edge of the small-data critical program.

---

## What it gives / what it does not give

**Gives.**
- Global smooth solutions for all data small in $\mathrm{BMO}^{-1}$, the largest known critical space. Subsumes Fujita-Kato ($\dot H^{1/2}$), Kato ($L^3$), and the Cannone-Planchon Besov theorems in one statement.
- A scale-invariant solution space $X$ and a clean bilinear-estimate proof that is now the template for critical well-posedness across dispersive and parabolic PDE (the "Koch-Tataru method").
- Real-analytic dependence on data, hence stability and uniqueness in the small-data class.
- A sharp upper bound on how far the perturbative critical program can reach: one space further ($\dot B^{-1}_{\infty,\infty}$) it is false.

**Does not give (the gap to closing regularity).**
- **No large-data result.** The smallness $\|u_0\|_{\mathrm{BMO}^{-1}} < \varepsilon$ is essential and cannot be removed by any known argument. Large critical-norm data is exactly the open millennium regime.
- **No a priori bound.** It does not produce a global-in-time bound on any critical norm of a general Leray-Hopf solution. It is a construction theorem (small data $\Rightarrow$ global solution), not an a priori-estimate theorem (general solution $\Rightarrow$ bound). The supercriticality gap is precisely the absence of a coercive critical a priori bound, and Koch-Tataru does not supply one.
- **No engagement with 3D structure.** Because it is perturbative, it never touches vortex stretching or any genuinely 3D mechanism. Tao's 2016 averaged-NS barrier shows the missing large-data control must use the exact nonlinearity; a perturbative small-data method, which works for the averaged system too, cannot be that control. (See [tao_2016_averaged](tao_2016_averaged.md): the averaged equation has the same energy and scaling and is small-data well-posed in the same critical sense, yet blows up for large data. So small-data critical well-posedness is exactly the kind of "soft" result that survives averaging and therefore cannot close large-data regularity.)

The directional reading (project stance): Koch-Tataru is not a wall; it is a survey marker. It tells us the perturbative critical method tops out at $\mathrm{BMO}^{-1}$ and that the boundary is sharp ($\dot B^{-1}_{\infty,\infty}$ is ill-posed). The proof that the small-data program is *complete* is itself a coordinate: the large-data proof must come from a different mechanism (a coercive critical quantity, an a priori bound engaging the exact nonlinearity), not from enlarging the data space further. That redirects effort toward Direction 03 (a new critical coercive quantity) and away from "find an even bigger critical space," which is now known to be a dead branch.

---

## The boundary just beyond: ill-posedness in $\dot B^{-1}_{\infty,\infty}$

The space one step larger than $\mathrm{BMO}^{-1}$ in the critical ladder is $\dot B^{-1}_{\infty,\infty}$. Here well-posedness **fails**:

**Bourgain-Pavlovic (2008).** *Ill-posedness of the Navier-Stokes equations in a critical space in 3D*, J. Funct. Anal. **255** (2008), 2233-2247. They exhibit norm inflation: for any $\delta > 0$ there is Schwartz, divergence-free data $u_0$ with $\|u_0\|_{\dot B^{-1}_{\infty,\infty}} < \delta$ whose solution satisfies $\|u(t)\|_{\dot B^{-1}_{\infty,\infty}} > 1/\delta$ at some time $t < \delta$. Hence the data-to-solution map is discontinuous at $0$ in $\dot B^{-1}_{\infty,\infty}$, and the equation is ill-posed there. (Verified: J. Funct. Anal. 255, 2233-2247, 2008.)

Refinements sharpen exactly where the transition sits. Yoneda (2010), *Ill-posedness of the 3D Navier-Stokes equations in a generalized Besov space near $\mathrm{BMO}^{-1}$*, J. Funct. Anal. **258** (2010), shows ill-posedness in spaces strictly between $\mathrm{BMO}^{-1}$ and $\dot B^{-1}_{\infty,\infty}$, narrowing the gap from above. Wang (2015) and others closed further variants. The combined picture: $\mathrm{BMO}^{-1}$ is at or extremely near the true threshold; well-posedness holds in $\mathrm{BMO}^{-1}$ (Koch-Tataru) and fails just beyond it (Bourgain-Pavlovic, Yoneda). The critical small-data well-posedness program is essentially complete and its boundary is identified.

The structural lesson: the failure mode just past $\mathrm{BMO}^{-1}$ is a *perturbative* failure (the bilinear estimate $\|B(u,u)\|_X \lesssim \|u\|_X^2$ cannot hold in the larger space, and norm inflation is the witness). It is not a statement that solutions blow up; it is a statement that the contraction method, and indeed any method giving a continuous solution map, breaks. This is a sharp diagnostic of where the perturbative regime ends, and it confirms that the route past it cannot be perturbative.

---

## Lineage and sharpest known form

**Builds on.**
- Kato (1984), $T^3$/$\mathbb{R}^3$ mild solutions in $L^3$ via the heat semigroup and the same bilinear structure; Fujita-Kato (1964) in $\dot H^{1/2}$ (see [references](../../../references/README.md)). Koch-Tataru is the same Picard-iteration philosophy pushed to the largest space by replacing the Lebesgue/Sobolev iteration norm with the Carleson norm.
- The Fefferman-Stein Carleson-measure characterization of $\mathrm{BMO}$, adapted to the parabolic heat extension. The $\mathrm{BMO}^{-1}$ space and its Carleson norm are the import that makes the bilinear estimate close.
- Cannone-Meyer-Planchon Besov small-data theory ($\dot B^{-1+3/q}_{q,\infty}$), which Koch-Tataru contains.

**Built on it.**
- The "Koch-Tataru method" (choose a scale-invariant solution space tailored to make the linear estimate trivial, then prove a single bilinear/multilinear estimate) became standard for critical well-posedness across PDE, including dispersive equations far from fluids.
- Auscher-Dubois-Tchamitchian (2004) and Miura-Sawada gave stability and persistence-of-regularity refinements in $\mathrm{BMO}^{-1}$.
- Lemarie-Rieusset's monograph *Recent Developments in the Navier-Stokes Problem* (2002) and its 2016 successor *The Navier-Stokes Problem in the 21st Century* give the definitive textbook treatment of the Koch-Tataru space and the surrounding critical theory.
- Germain (2006) and others analyzed uniqueness subtleties in $\mathrm{BMO}^{-1}$ (uniqueness of the Koch-Tataru solution in the full $X$ class versus in smaller classes).
- A streamlined re-proof: Q. Deng / collaborators, *A new proof for Koch and Tataru's result* (arXiv:1310.3783, 2013), recasting the bilinear estimate.

**Sharpest known form / boundary, as of 2025.**
- The well-posedness side is sharp at the space level: $\mathrm{BMO}^{-1}$ is the largest space with small-data global well-posedness, and Bourgain-Pavlovic (2008) plus Yoneda (2010) show the next space up is ill-posed. No enlargement of the data space is possible without losing well-posedness.
- The smallness side is *not* removable, and this is the open frontier. Recent non-uniqueness results from critical data (for example work on non-uniqueness of mild/smooth solutions from critical data, arXiv:2503.14699, 2025 (verify)) probe whether large critical data can fail uniqueness, which would be a hard limit on extending Koch-Tataru beyond smallness. On the regularity side, the relevant 2025-level frontier is quantitative: Tao (2019) and Barker-Prange made the ESS critical-$L^3$ continuation quantitative (triple-logarithmic lower bounds on critical-norm growth at a hypothetical singularity), which is the closest the critical-norm program comes to a large-data statement, and it lives on the continuation side (ESS), not the construction side (Koch-Tataru). See [escauriaza_seregin_sverak_2003](escauriaza_seregin_sverak_2003.md).

---

## References

- H. Koch, D. Tataru, "Well-posedness for the Navier-Stokes equations," Adv. Math. **157** (2001), no. 1, 22-35. [The source.]
- H. Fujita, T. Kato, "On the Navier-Stokes initial value problem I," Arch. Rational Mech. Anal. **16** (1964), 269-315. [Critical $\dot H^{1/2}$ small-data theory.]
- T. Kato, "Strong $L^p$-solutions of the Navier-Stokes equation in $\mathbb{R}^m$, with applications to weak solutions," Math. Z. **187** (1984), 471-480. [Critical $L^3$ mild solutions.]
- M. Cannone, Y. Meyer, F. Planchon; F. Planchon, on Besov critical spaces $\dot B^{-1+3/q}_{q,\infty}$. [Intermediate critical spaces.]
- C. Fefferman, E. M. Stein, "$H^p$ spaces of several variables," Acta Math. **129** (1972), 137-193. [Carleson-measure characterization of $\mathrm{BMO}$, the parabolic analogue of which underlies $\mathrm{BMO}^{-1}$.]
- J. Bourgain, N. Pavlovic, "Ill-posedness of the Navier-Stokes equations in a critical space in 3D," J. Funct. Anal. **255** (2008), 2233-2247. [Norm inflation in $\dot B^{-1}_{\infty,\infty}$, the boundary beyond Koch-Tataru.]
- T. Yoneda, "Ill-posedness of the 3D Navier-Stokes equations in a generalized Besov space near $\mathrm{BMO}^{-1}$," J. Funct. Anal. **258** (2010), 3376-3387. [Narrows the well-posed/ill-posed boundary toward $\mathrm{BMO}^{-1}$.]
- P. Auscher, S. Dubois, P. Tchamitchian, "On the stability of global solutions to Navier-Stokes equations in the space," J. Math. Pures Appl. (2004). [Stability in $\mathrm{BMO}^{-1}$.]
- P. G. Lemarie-Rieusset, *The Navier-Stokes Problem in the 21st Century*, CRC Press (2016). [Definitive textbook treatment of the Koch-Tataru space.]
- L. Escauriaza, G. Seregin, V. Sverak, "$L_{3,\infty}$-solutions of Navier-Stokes equations and backward uniqueness," Russian Math. Surveys **58** (2003), 211-250. [Critical-$L^3$ continuation endpoint; the continuation-side partner.]
- T. Tao, "Finite time blowup for an averaged three-dimensional Navier-Stokes equation," J. Amer. Math. Soc. **29** (2016), 601-674. [The barrier: small-data critical well-posedness survives averaging, so it cannot close large-data regularity.]

---

## What this enables / what remains open

**Enables.**
- A clean upper marker for the critical-space attack (Architecture 3): the perturbative small-data method reaches $\mathrm{BMO}^{-1}$ and no further. BUILDER should not propose "find a larger critical space" as a route to large-data regularity; that branch is closed by Bourgain-Pavlovic.
- The $X$-space / bilinear-estimate template, available for any small-data or near-critical construction the program might want (for example perturbation around a known global solution).
- A precise statement of the gap for SYNTHESIZER: Koch-Tataru is the strongest *construction* theorem at the critical level, ESS is the strongest *continuation* theorem at the critical level, and the millennium problem is the large-data gap between "small critical data is fine" and "critical-norm blow-up is excluded a priori," which neither theorem reaches.

**Remains open (handoff to BUILDER / ADVERSARY / Direction 03).**
- Remove the smallness: any a priori bound on a critical norm ($\mathrm{BMO}^{-1}$, $L^3$, $\dot H^{1/2}$) for large data would close regularity. None is known, and the energy (supercritical) cannot supply one. This is Direction 03 (a new coercive critical quantity).
- The smallness cannot be soft: by the Tao 2016 barrier, whatever removes it must use the exact nonlinearity, since the perturbative critical theory works equally for the averaged system that blows up. ADVERSARY check: any candidate large-data critical bound that would also hold for the averaged equation is automatically insufficient.
- Quantitative critical-norm growth (Tao 2019, Barker-Prange) is the live thread that turns the continuation side quantitative; the open question is whether a self-improving quantitative critical estimate can be pushed to an unconditional bound. See [escauriaza_seregin_sverak_2003](escauriaza_seregin_sverak_2003.md) and Direction 01.

Cross-links: [Direction 03 (supercriticality gap)](../research_directions/03_supercriticality_gap.md) is the primary home of this note (the critical-level coercive-quantity hunt). Secondary: [Direction 01 (critical continuation criteria)](../research_directions/01_critical_continuation_criteria.md) for the ESS/quantitative thread, and [Direction 04 (blow-up and barriers)](../research_directions/04_blowup_and_barriers.md) for the Tao averaged-NS barrier that bounds what small-data critical well-posedness can ever achieve. Sibling notes: [Escauriaza-Seregin-Sverak (2003)](escauriaza_seregin_sverak_2003.md), [Beale-Kato-Majda (1984)](beale_kato_majda_1984.md), [Tao (2016)](tao_2016_averaged.md).
