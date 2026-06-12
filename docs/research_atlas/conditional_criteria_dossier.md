# Conditional regularity criteria: the criticality dossier

SURVEYOR output for the PLAN item "criticality dossier for all conditional criteria" (Architecture 2). Every known family of conditional regularity criteria for 3D Navier-Stokes, placed on the project's sub/critical/super coordinate (`experiments/_shared/criticality.py`), with the structural information each uses and the obstruction to verifying its hypothesis from the energy class.

Provenance discipline: criteria marked **[repo dossier]** have a full reading note in [`../03_research/reading_notes/`](../03_research/reading_notes/) that was read for this survey. Criteria marked **[web-verified]** had their exact exponents confirmed against the literature during this survey (links in the references). Everything else is from structural knowledge of the literature; anything I am not certain of carries an explicit **[verify]**.

---

## 0. Conventions and the master scaling computation

Under the Navier-Stokes scaling

$$u_\lambda(x,t) = \lambda\, u(\lambda x, \lambda^2 t), \qquad p_\lambda(x,t) = \lambda^2\, p(\lambda x, \lambda^2 t),$$

a quantity $F$ built from $u$ that transforms pointwise as $F_\lambda(x,t) = \lambda^k F(\lambda x, \lambda^2 t)$ has space-time Lebesgue norm

$$\|F_\lambda\|_{L^p_t L^q_x} = \lambda^{\,a}\, \|F\|_{L^p_t L^q_x}, \qquad a = k - \frac{2}{p} - \frac{3}{q},$$

(the spatial change of variables gives $-3/q$, the time change gives $-2/p$). This is the single computation behind every entry below. The pointwise weights:

| Quantity | $k$ | Critical line $2/p + 3/q = k$ |
|---|---|---|
| velocity $u$ (or any single component $u_j$) | $1$ | $2/p + 3/q = 1$ |
| gradient $\nabla u$, vorticity $\omega$, strain $S$, pressure $\pi$ | $2$ | $2/p + 3/q = 2$ |
| pressure gradient $\nabla\pi$ | $3$ | $2/p + 3/q = 3$ |
| direction field $\xi = \omega/|\omega|$ | $0$ (dimensionless) | (see Section 7) |

Bookkeeper convention (`classify_exponent`): $a > 0$ subcritical, $a = 0$ critical, $a < 0$ supercritical.

**How to read the exponent of a criterion's hypothesis.** For a *criterion* "if $\|F\|_{L^p_tL^q_x} < \infty$ then $u$ is smooth," the exponent $a$ of the hypothesis norm measures how much the criterion demands:

- $a = 0$: the hypothesis is scale invariant. This is the optimal position a criterion can occupy, because regularity itself is a scale-invariant statement.
- $a > 0$: the hypothesis is **subcritical-demanding**. The criterion asks for more than scale-invariant information, so it is a weaker theorem (an easier conclusion bought with a stronger assumption). The size of $a$ is the **tax**.
- $a < 0$ would mean a supercritical hypothesis, i.e. a criterion whose hypothesis the energy class could supply. **No such criterion exists**, and the Tao 2016 averaged-NS barrier (LEARNINGS #7) explains why none can be soft: a supercritical hypothesis plus energy plus scaling is satisfied by the averaged caricature, which blows up.

**What the energy class supplies, in each currency.** A Leray-Hopf solution has $u \in L^\infty_t L^2_x \cap L^2_t \dot H^1_x$, and the whole interpolation family sits at one exponent:

- velocity: $u \in L^p_t L^q_x$ exactly on $2/p + 3/q = 3/2$ (from $L^\infty_tL^2$ to $L^2_tL^6$), so $a = 1 - 3/2 = -1/2$;
- gradient/vorticity: $\nabla u, \omega \in L^2_t L^2_x$, so $2/p + 3/q = 5/2$ and $a = 2 - 5/2 = -1/2$;
- pressure: $\pi \in L^{p}_tL^{q}_x$ on $2/p + 3/q = 3$ (Calderon-Zygmund from $|u|^2$), so $a = -1$;
- pressure gradient: $\nabla\pi \in L^1_t L^{3/2}_x$, so $a = -1$.

In velocity currency the deficit is uniformly $1/2$; quantities quadratic in $u$ show deficit $1$ (which is $1/2$ per power of $u$). The deficit is a **polynomial** gap in the scaling parameter: to close it, a bound must improve on the energy by a factor $\lambda^{1/2}$ at scale $\lambda$. Keep that number in mind when reading Section 9, where the best known improvements are logarithms.

---

## 1. The Prodi-Serrin-Ladyzhenskaya family (velocity size) **[repo dossier]**

**Statement.** If a Leray-Hopf solution satisfies $u \in L^p(0,T; L^q(\mathbb{R}^3))$ with $2/p + 3/q \le 1$, $3 < q \le \infty$, then $u$ is smooth on $(0,T]$ (Prodi 1959; Serrin 1962, interior version; Ladyzhenskaya 1967; the smooth-extension form in Giga 1986). The same class gives weak-strong uniqueness.

**Scaling.** $a = 1 - 2/p - 3/q$. On the line $2/p + 3/q = 1$: $a = 0$, exactly critical. Inside the region ($2/p + 3/q < 1$): $a > 0$, subcritical-demanding. The criterion family is the critical line itself.

**Classification.** Critical (at equality).

**Structure used.** None beyond the equation: the proof is an energy estimate on the difference or on higher norms, with the nonlinear term absorbed into dissipation via Holder, Sobolev, and Young. The mechanism is dimension generic; what is special to 3D is only the location of the line.

**Obstruction from the energy class.** Energy delivers the family $2/p + 3/q = 3/2$; the criterion needs $1$. The deficit $1/2$ is the supercriticality gap, stated in PSL coordinates. The 2D contrast is exact: in 2D the energy interpolation gives $2/p + 2/q = 1$, which *is* the 2D regularity line, and that is the analytic reason 2D closes (LEARNINGS #3).

---

## 2. The $L^3$ endpoint and its extensions **[repo dossier]**

**Statement (ESS).** Escauriaza-Seregin-Sverak (2003): if $u \in L^\infty(0,T; L^3(\mathbb{R}^3))$, then $u$ is smooth on $(0,T]$. This is the PSL endpoint $q = 3$, $p = \infty$, excluded from Section 1 and genuinely harder: the proof needs backward uniqueness and unique continuation for parabolic operators, not energy estimates.

**Scaling.** $\|u\|_{L^3}$ has $a = 1 - 3/3 = 0$ at each fixed time, and the $L^\infty$ time norm adds nothing: critical.

**Extensions, all at $a = 0$ (the Lorentz second index and the Besov microscopic indices do not move the scaling exponent):**

- **Seregin (2012)**: at a blow-up time $T$, $\|u(t)\|_{L^3} \to \infty$ as $t \to T$ (limit, not just limsup). A necessary-condition sharpening.
- **Lorentz nonendpoint (Phuc 2015)**: $u \in L^\infty_t L^{3,q}$ with $q < \infty$ still implies regularity. The genuine endpoint $L^\infty_t L^{3,\infty}$ (weak-$L^3$) is **open** for large norm; smallness of the $L^{3,\infty}$ norm suffices (mild-solution theory, Kozono-Yamazaki lineage **[verify attribution]**).
- **Critical Besov (Gallagher-Koch-Planchon 2016)**: at a putative singularity the critical Besov norms $\|u(t)\|_{\dot B^{-1+3/p}_{p,q}}$ blow up, for $3 < p, q < \infty$, via profile decomposition. Pushes the ESS phenomenon up the critical ladder toward (but not reaching) $\mathrm{BMO}^{-1}$ and $\dot B^{-1}_{\infty,\infty}$.
- **Quantitative ESS (Tao 2019)** **[repo dossier]**: effective version; blow-up forces $\limsup_{t\to T}\|u(t)\|_{L^3} / \big(\log\log\log\tfrac{1}{T-t}\big)^c = \infty$. The rate is triple-logarithmic; see Section 9. Later quantitative improvements exist in restricted settings (Palasek, axisymmetric and scale-of-critical-spaces versions) **[verify exact scope]**.

**Classification.** Critical; the deepest purely-size criterion.

**Structure used.** None geometric. The new machinery (backward uniqueness) is about the heat operator, i.e. viscosity: the result genuinely uses $\nu > 0$ and fails to have an Euler analog. Passes the viscosity control in the strongest sense.

**Obstruction from the energy class.** Energy controls $L^\infty_t L^2$ ($a = -1/2$); it says nothing about $L^\infty_t L^3$ ($a = 0$). There is no interpolation route: the gap is exactly the half power of scaling. ESS converts the regularity problem into "bound one critical norm for all time," which is the cleanest known restatement of the open problem.

---

## 3. The Beale-Kato-Majda family (vorticity magnitude) **[repo dossier]**

**Statement (BKM).** A smooth solution on $[0,T)$ extends past $T$ if and only if $\int_0^T \|\omega(t)\|_{L^\infty}\, dt < \infty$ (Beale-Kato-Majda 1984; stated for Euler, holds for NS).

**Scaling.** $\omega$ has $k = 2$; with $(p,q) = (1,\infty)$: $a = 2 - 2/1 - 3/\infty = 0$. Exactly critical, in every dimension (the bookkeeper computes this in `vorticity_Linfty_time_integral_exponent`).

**Refinements at the same scaling level, in progressively larger spaces (all zero-order spaces, so $k = 2$ and $a = 0$ is unchanged):**

- **Kozono-Taniuchi (2000)**: $\int_0^T \|\omega\|_{\mathrm{BMO}}\, dt < \infty$ suffices.
- **Kozono-Ogawa-Taniuchi (2002)**: $\int_0^T \|\omega\|_{\dot B^0_{\infty,\infty}}\, dt < \infty$ suffices. The proof runs through the Brezis-Gallouet-Wainger log-interpolation $\|f\|_{L^\infty} \lesssim 1 + \|f\|_{\dot B^0_{\infty,\infty}} \log(e + \|f\|_{H^s})$: the logarithm is absorbed by Gronwall. This is the prototype of every "log-improved" criterion in Section 9.

**Classification.** Critical. The refinements enlarge the space at fixed criticality; none lowers the scaling demand.

**Structure used.** Vorticity, but only its magnitude. The criterion is blind to the geometry of $\omega$ and applies verbatim to Euler (it is an inviscid theorem), so it does not use viscosity. It is the sharp *diagnostic* of blow-up, not a mechanism against it. The Taylor-Green DNS and the resolution study track exactly this integral (LEARNINGS #5, #11).

**Obstruction from the energy class.** Energy gives $\omega \in L^2_t L^2_x$, i.e. $2/p + 3/q = 5/2$ vs the needed $2$: deficit $1/2$ in gradient currency. Pointwise control of $\omega$ is two derivatives and a Sobolev embedding away from anything the energy sees.

---

## 4. Gradient and vorticity $L^p_t L^q_x$ criteria

**Statement (Beirao da Veiga 1995).** If $\nabla u \in L^p(0,T; L^q)$ with $2/p + 3/q = 2$, $3/2 < q < \infty$, then $u$ is smooth.

**Scaling.** $k = 2$, so $a = 2 - 2/p - 3/q = 0$ on the line: critical. The energy gives $\nabla u \in L^2_tL^2_x$, which sits on $2/p+3/q = 5/2$: the same $1/2$ deficit as everywhere.

**Endpoints and variants:**

- $q = 3/2$, $p = \infty$: $\sup_t \|\nabla u\|_{L^{3/2}}$ is critical ($a = 0$), and by Sobolev $\dot W^{1,3/2} \hookrightarrow L^3$ this endpoint **follows from ESS**. A small observation worth recording: the gradient family's hard endpoint was retroactively closed by the 2003 velocity endpoint.
- $q = \infty$: handled by the Besov BKM refinements of Section 3.
- **Vorticity form**: $\omega \in L^p_tL^q_x$ on the same line is equivalent (Biot-Savart plus Calderon-Zygmund, $\|\nabla u\|_{L^q} \lesssim \|\omega\|_{L^q}$ for $1 < q < \infty$).
- **Two components of vorticity (Chae-Choe 1999)**: only $\tilde\omega = (\omega_1, \omega_2) \in L^p_tL^q_x$, $2/p + 3/q = 2$, $3/2 < q < \infty$, is needed. First sign that the full vector is more than the problem requires: an anisotropy result at zero tax.
- **One directional derivative (Kukavica-Ziane 2007)** **[web-verified]**: $\partial_3 u \in L^p(0,T;L^q)$ with $2/p + 3/q = 2$ and $9/4 \le q \le 3$ implies regularity. Critical line, restricted $q$-window; later work has widened the window (e.g. the anisotropic conditions of arXiv:2007.10888 and arXiv:2102.06152, skimmed at abstract level only).
- **Middle strain eigenvalue (Miller 2019)**: control of the positive part $\lambda_2^+$ of the intermediate eigenvalue of the strain $S$ in $L^p_tL^q_x$ on the critical line $2/p+3/q = 2$ implies regularity **[verify exact $q$-range]**. Structurally notable: $\lambda_2$ is exactly the quantity the classical alignment story (Section 7, and `experiments/vortex_stretching/`) measures.

**Classification.** Critical (the whole section sits on the $k=2$ line).

**Structure used.** Size only, except: Chae-Choe and Kukavica-Ziane use the divergence-free anisotropy (some components/directions are redundant), and Miller uses strain geometry (the sign and ranking of eigenvalues), which is genuinely 3D-flavored: in 2D the strain eigenvalues are $\pm\lambda$ and the stretching term is absent.

**Obstruction from the energy class.** Deficit $1/2$ on the $(2/p+3/q)$ axis in every variant. Reducing components does not reduce the scaling demand: the line stays at $2$.

---

## 5. Pressure criteria

**Statement (Berselli-Galdi 2002; also Chae-Lee 2001)** **[web-verified]**. If $\pi \in L^p(0,T; L^q)$ with $2/p + 3/q = 2$, $q > 3/2$, then $u$ is smooth. Gradient version: $\nabla\pi \in L^p_tL^q_x$ with $2/p + 3/q = 3$ **[verify exact $q$-range]**.

**Scaling.** Pressure has $k = 2$ (it scales like $|u|^2$), so the line $2/p+3/q = 2$ is $a = 0$: critical. For $\nabla\pi$, $k = 3$ and the line $2/p + 3/q = 3$ is again $a = 0$.

**The Calderon-Zygmund reading.** $-\Delta \pi = \partial_i\partial_j(u_i u_j)$, so $\pi = R_iR_j(u_iu_j)$ and $\|\pi\|_{L^q} \lesssim \|u\|_{L^{2q}}^2$ for $1 < q < \infty$. Substituting, the pressure criterion at $(p, q)$ is implied by PSL at $(2p, 2q)$, and the lines map onto each other exactly: $2/(2p) + 3/(2q) = 1 \iff 2/p + 3/q = 2$. **Size-based pressure criteria are PSL in disguise.** Their value is practical (pressure is sometimes easier to estimate), not structural.

**The structurally different pressure result (Seregin-Sverak 2002).** Solutions whose pressure is bounded below are smooth. This uses the Bernoulli structure (the quantity $\tfrac12|u|^2 + \pi$ and a maximum-principle-flavored argument), i.e. **sign** information rather than size. Note honestly: "bounded below by a constant" is not a scale-invariant hypothesis (a constant lower bound has $k=2$ dimension); the scale-invariant core of the idea is the sign structure of $\pi$, and how far that can be pushed is part of Direction 03's search space.

**Classification.** Critical (size versions); the sign version is off-axis (not a Lebesgue-exponent statement).

**Structure used.** Size versions: none (reducible to PSL). Sign version: the pressure-velocity coupling of the exact nonlinearity, which is precisely the structure the Tao 2016 averaging destroys. That makes the Seregin-Sverak direction more interesting than its current strength suggests.

**Obstruction from the energy class.** Energy gives $\pi$ on $2/p+3/q = 3$ vs the needed $2$: deficit $1$ in pressure currency ($1/2$ per power of $u$).

---

## 6. One-component and anisotropic criteria (the anisotropy tax)

The family: control only $u_3$ (or one entry of $\nabla u$) and conclude full regularity, exploiting $\nabla \cdot u = 0$ and the structure of the equations for the horizontal components. The history is a staircase descending toward the critical line, and the height above the line is the **anisotropy tax** $a = 1 - (2/p + 3/q) > 0$ on the hypothesis.

| Result | Hypothesis on $u_3$ | $2/p+3/q$ | Tax $a$ |
|---|---|---|---|
| Neustupa-Penel (1999) | $u_3 \in L^\infty_t L^\infty_x$ | $0$ | $1$ |
| Neustupa-Novotny-Penel (2002) | $L^p_tL^q_x$, $2/p+3/q \le 1/2$, $q > 6$ **[verify]** | $1/2$ | $1/2$ |
| Kukavica-Ziane (2006) | $L^p_tL^q_x$, $2/p+3/q \le 5/8$, $q \ge 24/5$ **[verify range]** | $5/8$ | $3/8$ |
| Zhou-Pokorny (2010) **[web-verified]** | $L^p_tL^q_x$, $2/p+3/q = 3/4 + 1/(2q)$, $q > 10/3$ | $3/4 + \tfrac{1}{2q}$ | $\tfrac14 - \tfrac{1}{2q}$, as small as $\approx \tfrac{1}{10}$ |
| Chemin-Zhang (2016) | $u_3 \in L^p_t \dot H^{1/2 + 2/p}$, $4 < p < 6$ | (anisotropic Sobolev) | $0$: **critical** |
| Chemin-Zhang-Zhang (2017) | same, $4 < p < \infty$ | | $0$: **critical** |
| "Serrin-type condition on one velocity component" (arXiv:1911.02699, ARMA 2021) | $u_3 \in L^p_tL^q_x$ on $2/p+3/q = 1$, partial $q$-range **[verify range; skimmed title/abstract only]** | $1$ | $0$: **critical** |

Scaling check for Chemin-Zhang: $\|u_3\|_{\dot H^{1/2+2/p}}$ has per-time exponent $1 + (1/2 + 2/p) - 3/2 = 2/p$, and the $L^p$ time integral contributes $-2/p$: net $a = 0$. Genuinely scale invariant: the tax is zero, at the price of an anisotropic Sobolev space rather than Lebesgue.

**Gradient-entry versions.** Cao-Titi (2008, 2011): regularity from one entry of $\nabla u$ (e.g. $\partial_3 u_3$), with conditions strictly above the $k=2$ critical line (a positive tax whose size depends on the entry; diagonal entries do better) **[verify exact exponents]**. Kukavica-Ziane 2007 (Section 4) is the zero-tax result for the full vector $\partial_3 u$.

**Classification.** Historically subcritical-demanding, with the tax driven to zero only in 2016-2021. The one-component family **reached** the critical line; it has not crossed it.

**Structure used.** Component anisotropy: the divergence-free constraint and the special role of one coordinate. The structural reading: these criteria quantify "how much 2D-ness suffices." If $u_3 \equiv 0$ and $\partial_3 u = 0$ the flow is 2D and regular; the criteria interpolate from that pole. They pass the 2D control vacuously (in 2D the hypothesis is free and the conclusion true). They do **not** engage vortex-stretching geometry: the mechanism is anisotropic energy estimates, not depletion.

**Obstruction from the energy class.** The energy is isotropic and supplies $u_3$ exactly what it supplies $u$: the $a = -1/2$ family. Even the zero-tax critical versions sit half a power above reach, and the taxed versions sit higher still.

---

## 7. Vorticity-direction and geometric-depletion criteria **[repo dossier: CF]**

The only family whose hypothesis is about the *mechanism* of 3D blow-up (vortex stretching) rather than the *size* of the solution.

**Statement (Constantin-Fefferman 1993).** If the vorticity direction $\xi = \omega/|\omega|$ satisfies $|\xi(x) \times \xi(y)| \le C|x-y|$ for $x, y$ in the high-vorticity region (a Lipschitz modulus on the direction, uniformly on $[0,T]$), then the Leray-Hopf solution is smooth on $[0,T]$. Mechanism: the stretching factor $\alpha = \xi^\top S \xi$ is a singular integral whose kernel degenerates with the misalignment angle; Lipschitz coherence trades one power of the singularity, turning the $|y|^{-3}$ kernel into integrable $|y|^{-2}$, and viscosity absorbs the remainder. See the full reading note: [`../03_research/reading_notes/constantin_fefferman_1993.md`](../03_research/reading_notes/constantin_fefferman_1993.md).

**Scaling: the $\beta$-dial.** The direction field itself is dimensionless and scale invariant ($\xi_\lambda(x,t) = \xi(\lambda x, \lambda^2 t)$, $k = 0$). But the Holder-$\beta$ seminorm of a dimensionless field scales as

$$[\xi_\lambda]_{C^\beta} = \lambda^{\beta}\, [\xi]_{C^\beta}, \qquad a = +\beta.$$

So a fixed-constant coherence hypothesis at exponent $\beta$ is **subcritical-demanding with tax $\beta$**, and the family has its own internal criticality ladder with the Holder exponent as the dial:

| Result | Coherence demanded | Tax $a = \beta$ | Note |
|---|---|---|---|
| Constantin-Fefferman (1993) | Lipschitz, $\beta = 1$ | $+1$ | the prototype |
| Beirao da Veiga-Berselli (2002) | Holder $\beta = 1/2$ | $+1/2$ | same scaling height as bounded enstrophy ($\sup_t\|\omega\|_{L^2}$ has $a = +1/2$), and indeed $\beta = 1/2$ is where the geometric argument meets the classical enstrophy theory |
| $\beta < 1/2$ with $|\omega|$-integrability compensation (Beirao da Veiga and others, surveyed in arXiv:1604.08083) | mixed | between $0$ and $1/2$ | the open tradeoff region |
| Giga-Miura (2011) | uniform continuity of $\xi$ on the high-vorticity set, i.e. the $\beta \to 0$ edge | $\to 0$ | but proved within a type-I / scaling-bounded solution class **[verify exact class]**, via blow-up and Liouville rather than the CF singular integral |

The critical endpoint of the family, $\beta = 0$ unconditionally (a scale-invariant coherence modulus, e.g. dyadic-scale oscillation smallness of $\xi$, with no extra solution-class hypothesis), is **open**, and is the natural target of Direction 02.

**The sparseness/depletion branch (Grujic and collaborators).** Instead of a modulus on $\xi$, hypothesize geometric smallness of the super-level sets of $|\omega|$: if at times approaching a putative singularity the set $\{|\omega| > M\}$ is "1D-sparse" at the parabolic scale $\sim (T-t)^{1/2}$, regularity follows (Grujic 2013). Because the hypothesis is a volumetric ratio evaluated at the self-similar scale, it is scale invariant by construction. Bradshaw-Farhat-Grujic (2019) use this framework to reduce the scaling gap **algebraically** (a power improvement, not a log) *conditional on the sparseness structure* **[verify exact exponent; skimmed]**. This is the only thread in the entire dossier that claims a polynomial bite out of the $1/2$ deficit, at the price of an unproven geometric hypothesis that DNS so far supports (filamentary, sparse intense-vorticity regions are the universal turbulence observation).

**Classification.** Critical *object*, subcritical-demanding *modulus* (tax $= \beta$); sparseness branch critical by construction. See the discrepancy log (Section 12) for how this refines the repo's existing "critical / scale-aware" labels.

**Structure used.** Vorticity geometry: the exact 3D stretching term $\omega \cdot \nabla u$ and its depletion by alignment. This is the family's distinction. The 2D control is passed in the strongest, non-vacuous sense: in 2D $\xi$ is constant, $\sin\theta \equiv 0$, the hypothesis is automatic and the conclusion (2D regularity) is true; the criterion's content lives exactly in the degrees of freedom 2D lacks. Viscosity is essential (the absorbed remainder needs $-\nu\int|\nabla\omega|^2$); the Euler analog (Constantin-Fefferman-Majda 1996) degrades to a constraint on singularities, as it must, since Euler blows up.

**Obstruction from the energy class.** The energy bounds no modulus of continuity of $\xi$: a field can have finite energy and wildly oscillating direction at small scales. Worse, the hypothesis is geometric, so no interpolation from Lebesgue norms can produce it. What the project's own experiment shows (LEARNINGS #10) is that the coherence is *observed* in smooth flow ($|\nabla\xi|$ far below Nyquist in the intense region, depletion factor $\approx 0.53$); the open problem is to prove it is *forced*.

---

## 8. The largest-space endpoint: $\dot B^{-1}_{\infty,\infty}$ and the Onsager picture **[web-verified]**

**Statement (Cheskidov-Shvydkoy 2010).** If a Leray-Hopf solution belongs to $C((0,T]; B^{-1}_{\infty,\infty})$, or if its jump discontinuities in the $B^{-1}_{\infty,\infty}$ norm do not exceed a constant multiple of the viscosity, then it is regular on $(0,T]$.

**Scaling.** $\dot B^{-1}_{\infty,\infty}$ has $a = 1 + (-1) - 3/\infty = 0$: critical, and it is the *largest* critical space (every critical space in the ladder $\dot H^{1/2} \hookrightarrow L^3 \hookrightarrow \dot B^{-1+3/p}_{p,\infty} \hookrightarrow \mathrm{BMO}^{-1} \hookrightarrow \dot B^{-1}_{\infty,\infty}$ embeds into it; the norm is equivalent to $\sup_{t} \sqrt{t}\,\|e^{t\Delta}u\|_{L^\infty}$).

**Classification.** Critical, at the absolute end of the size axis. Note what is demanded: not boundedness (which would be the ultimate criterion and is far out of reach) but *continuity in time* of the weakest critical norm. Blow-up must be accompanied by an $O(\nu)$ jump in $\dot B^{-1}_{\infty,\infty}$.

**Context: the boundary is real.** Bourgain-Pavlovic (2008) prove norm inflation (ill-posedness) for the initial value problem in the same space. So $\dot B^{-1}_{\infty,\infty}$ is simultaneously where the continuation criterion family ends and where the solution map breaks; the criterion survives past the point where well-posedness fails because it constrains an existing Leray-Hopf solution rather than constructing one.

**The Onsager-space picture.** The same authors' dissipation-range program (Cheskidov-Shvydkoy 2014) reframes regularity through the energy flux: regularity holds if the flux dies beyond a determining wavenumber, and the natural function space for flux control is the Onsager-type space $\dot B^{1/3}_{3,\infty}$. Two distinct layers must not be conflated (LEARNINGS #8): the **energy-equality layer** (Lions $L^4_{t,x}$; Shinbrot $2/p + 2/q \le 1$, $q \ge 4$; Cheskidov-Constantin-Friedlander-Shvydkoy $L^3_t B^{1/3}_{3,c_0}$) is about anomalous dissipation, sits at Onsager scaling, and is *not* a regularity threshold. The Shinbrot line $2/p+2/q = 1$ is not NS-scale-invariant at all, a reminder that the energy-equality question has different geometry than the regularity question.

**Structure used.** Frequency-local flux estimates: how the nonlinearity moves energy between dyadic shells. This engages the cascade (the project's dyadic-shell experiment, LEARNINGS #9, is the toy of exactly this picture) but not vortex-stretching geometry per se.

**Obstruction from the energy class.** The energy gives no time-continuity in any critical norm; Leray-Hopf solutions are only weakly continuous in $L^2$. The hypothesis is qualitative (continuity) rather than quantitative, but it lives at $a = 0$ all the same.

---

## 9. The log-thin frontier: how wide is the provable layer beyond critical?

The gap between energy ($a = -1/2$) and the criteria ($a = 0$) is polynomial: $\lambda^{1/2}$. The entire stock of unconditional-side progress on weakening the criteria is **logarithmic**. Measuring that width is the point of this section.

- **Log-improved BKM (Kozono-Ogawa-Taniuchi 2002).** Already in Section 3: the $L^\infty \to \dot B^0_{\infty,\infty}$ enlargement costs exactly one Gronwall-absorbable logarithm. Space enlargement at fixed criticality, log-priced.
- **Log-improved Prodi-Serrin (Chan-Vasseur 2007).** $\int_0^T\!\!\int \frac{|u|^5}{\log(1 + |u|)}\, dx\, dt < \infty$ implies regularity. Since $u \in L^5_{t,x}$ is exactly critical ($2/5 + 3/5 = 1$, $a = 0$), dividing the integrand by a log makes the hypothesis strictly weaker than critical: **log-supercritical**. This is the cleanest instance of a criterion below the line, and the margin is a single logarithm. A genre of variants exists (logarithmically improved criteria in $\mathrm{BMO}$, Besov, multiplier spaces: Zhou, Fan, and others), all with the same one-to-two-log margin.
- **Log-supercritical dissipation (Tao 2009).** The hyperdissipative NS with $(-\Delta)^{5/4}$ is energy-critical and globally regular; Tao showed the exponent can be relaxed by a logarithmic factor (dissipation symbol $|\xi|^{5/4}/g(|\xi|)$ with $\int^\infty \frac{ds}{s\, g(s)^4} = \infty$, so $g = \log^{1/4}$ qualifies), with Barbato-Morandin-Romito (2014) improving the allowed give-back to $g^2$ **[verify the exact power]**. Same message from the modified-equation axis: the provable layer beyond the critical line is logarithms wide.
- **Quantitative ESS (Tao 2019)** **[repo dossier]**: blow-up requires $\|u(t)\|_{L^3}$ to exceed $(\log\log\log \frac{1}{T-t})^c$. Read as a width measurement: at the critical endpoint, the effective penetration *into* the supercritical regime that current technology achieves is a triple logarithm. Improvements (double-log in restricted settings, Palasek) do not change the type **[verify]**.
- **Slightly supercritical dyadic models.** In the shell-model family the same phenomenon is exactly solvable: the project's own dyadic scan (LEARNINGS #9) confirms the regular/singular boundary sits at the flux-balance exponent, and barely-supercritical log-modifications inherit the borderline behavior (Tao's barrier in miniature).

**Classification.** Log-supercritical: hypotheses weaker than critical by powers of $\log$, never by a power of $\lambda$.

**The compass reading.** This is the measured width of the no-man's-land: the criteria need $\lambda^{1/2}$; the best tools cross $(\log\lambda)^{O(1)}$. A proof that closes regularity by grinding along this axis would need to win a polynomial with logarithmic tools, which is the precise, quantitative form of "genuinely new critical control is required." The one thread claiming an algebraic (polynomial) bite is the conditional sparseness framework of Section 7, which is why the geometric family is the lead.

---

## 10. The master table

Exponent $a$ is the scaling exponent of the **hypothesis** under $u_\lambda = \lambda u(\lambda x, \lambda^2 t)$, in the bookkeeper's convention. "Energy gap" is the distance from what the energy class supplies in the same currency.

| Criterion | Hypothesis (one line) | $a$ | Class | Structure used | Energy gap |
|---|---|---|---|---|---|
| PSL (1959-1967) | $u \in L^p_tL^q_x$, $2/p+3/q = 1$, $q>3$ | $0$ | critical | none (size) | $1/2$ |
| ESS (2003) | $u \in L^\infty_t L^3_x$ | $0$ | critical | viscosity (backward uniqueness) | $1/2$ |
| Seregin (2012) | necessary: $\|u(t)\|_{L^3} \to \infty$ at blow-up | $0$ | critical | same | $1/2$ |
| Phuc (2015) | $u \in L^\infty_t L^{3,q}$, $q<\infty$ | $0$ | critical | none (size) | $1/2$; $L^{3,\infty}$ open |
| GKP (2016) | critical Besov norms blow up, $3<p,q<\infty$ | $0$ | critical | profile decomposition | $1/2$ |
| BKM (1984) | $\int_0^T \|\omega\|_{L^\infty} dt < \infty$ | $0$ | critical | vorticity magnitude only | $1/2$ |
| Kozono-Taniuchi (2000) | $\int_0^T \|\omega\|_{\mathrm{BMO}} dt$ | $0$ | critical | same | $1/2$ |
| KOT (2002) | $\int_0^T \|\omega\|_{\dot B^0_{\infty,\infty}} dt$ | $0$ | critical (log-priced space) | same | $1/2$ |
| Beirao da Veiga (1995) | $\nabla u \in L^p_tL^q_x$, $2/p+3/q=2$ | $0$ | critical | none (size) | $1/2$ |
| Chae-Choe (1999) | two vorticity components on the same line | $0$ | critical | anisotropy | $1/2$ |
| Kukavica-Ziane (2007) | $\partial_3 u$, $2/p+3/q=2$, $q\in[9/4,3]$ | $0$ | critical | anisotropy | $1/2$ |
| Miller (2019) | $\lambda_2^+ \in L^p_tL^q_x$, $2/p+3/q=2$ | $0$ | critical | strain geometry | $1/2$ |
| Berselli-Galdi (2002) | $\pi \in L^p_tL^q_x$, $2/p+3/q=2$, $q>3/2$ | $0$ | critical | none (PSL in disguise) | $1$ (pressure currency) |
| Seregin-Sverak (2002) | $\pi$ bounded below | off-axis | sign, not size | pressure-velocity coupling | not comparable |
| Neustupa-Penel et al. (1999-2002) | $u_3$, $2/p+3/q \le 1/2$ | $+1/2$ to $+1$ | subcritical-demanding | anisotropy | $1$ to $3/2$ |
| Kukavica-Ziane (2006) | $u_3$, $2/p+3/q \le 5/8$ | $+3/8$ | subcritical-demanding | anisotropy | $7/8$ |
| Zhou-Pokorny (2010) | $u_3$, $2/p+3/q = \tfrac34{+}\tfrac1{2q}$ | $+\tfrac14{-}\tfrac1{2q}$ | subcritical-demanding | anisotropy | $\gtrsim 0.6$ |
| Chemin-Zhang(-Zhang) (2016, 2017) | $u_3 \in L^p_t\dot H^{1/2+2/p}$ | $0$ | **critical** | anisotropy | $1/2$ |
| Constantin-Fefferman (1993) | $\xi$ Lipschitz on intense set | $+1$ (modulus) | critical object, $\beta{=}1$ tax | **vorticity geometry** | not norm-comparable |
| Beirao da Veiga-Berselli (2002) | $\xi \in C^{1/2}$ on intense set | $+1/2$ (modulus) | $\beta{=}1/2$ tax | **vorticity geometry** | enstrophy-height |
| Giga-Miura (2011) | $\xi$ uniformly continuous, type-I class | $\to 0$ | critical edge, class-restricted | **vorticity geometry** | open at $\beta=0$ |
| Grujic sparseness (2013); BFG (2019) | super-level sets 1D-sparse at parabolic scale | $0$ (by construction) | critical, conditional | **vorticity geometry** | algebraic bite, conditional |
| Cheskidov-Shvydkoy (2010) | $u \in C((0,T]; B^{-1}_{\infty,\infty})$ or jumps $< c\nu$ | $0$ | critical (largest space) | frequency-local flux | $1/2$, plus continuity |
| Chan-Vasseur (2007) | $\int\!\!\int |u|^5/\log(1{+}|u|) < \infty$ | $0^-$ | **log-supercritical** | none (size) | $1/2$ minus one log |
| Tao (2009) hyperdissipative | $(-\Delta)^{5/4}/\log$-dissipation, modified NS | $0^-$ | log-supercritical (equation axis) | none | one log past energy-critical |
| Tao (2019) | quantitative ESS, triple-log rate | $0$ | critical, quantitative | viscosity (Carleman) | triple-log penetration |

---

## 11. Synthesis

### 11.1 The frontier is a log-thin layer on the critical line

Every row of the master table has $a \ge 0$ (up to logarithms): **no known criterion has a hypothesis the supercritical energy bound can verify**, and none comes within a power of $\lambda$ of it. The conditional-regularity literature, surveyed whole, is the critical line drawn with increasing precision: PSL drew it for velocity size, BKM for vorticity size, Beirao da Veiga for gradients, Berselli-Galdi for pressure (and that one collapses back onto PSL under Calderon-Zygmund), ESS and Cheskidov-Shvydkoy pinned its two endpoints ($L^3$ the smallest natural space, $\dot B^{-1}_{\infty,\infty}$ the largest), and the one-component program spent twenty years descending a staircase of taxes to finally touch the same line in 2016. Everything provable *past* the line is logarithmic: one log (Chan-Vasseur, KOT, Tao 2009), three logs of quantitative penetration at the endpoint (Tao 2019). The deficit to the energy is $\lambda^{1/2}$. The measured rate of advance is $(\log\lambda)^{O(1)}$. That arithmetic is not despair, it is the compass bearing: the proof will not come from sharpening size criteria along this axis, so effort belongs on the structural axes (geometry, sign, anisotropy) where the layer's thinness has not been measured because the right hypothesis has not been found yet.

### 11.2 Which criteria engage the 3D stretching structure

Sorted by what the hypothesis actually constrains:

- **Pure size, no structure** (would make sense for any equation with the same scaling): PSL, ESS and its Lorentz/Besov extensions, BKM and its BMO/Besov refinements, gradient/vorticity size, pressure size. These are the *measurement* of the 2D-3D deficit, not mechanisms against stretching. In 2D the energy itself reaches the corresponding line; in 3D it misses by $1/2$. The 2D control is passed only vacuously.
- **Component anisotropy** (uses $\nabla\cdot u = 0$ and a distinguished direction): one-component family, Kukavica-Ziane, Cao-Titi, Chae-Choe. These quantify *how much 2D-ness suffices*: the hypothesis interpolates toward the 2D pole ($u_3 \equiv 0$), and regularity flows from the part of the flow that is "almost 2D." Genuine structure, but the mechanism is anisotropic energy estimates; the stretching term is circumvented, not engaged.
- **Vorticity/strain geometry** (constrains the stretching mechanism itself): **Constantin-Fefferman and its lineage (the lead)**, Beirao da Veiga-Berselli, Giga-Miura, Grujic sparseness/depletion, Miller's $\lambda_2^+$ criterion. Plus one outlier: Seregin-Sverak's pressure sign condition, the only criterion touching the exact pressure-velocity coupling (the structure Tao 2016 shows is load-bearing). These are the only hypotheses that would be *false to state* in 2D rather than trivially true: they live entirely in the degrees of freedom (direction variation, eigenvalue ranking, level-set geometry) that the 2D equation lacks. And they conditionalize exactly what the project's instrumentation observes unforced: depletion ($\approx 0.53$ of maximal stretching) and direction coherence ($|\nabla\xi|$ small on the intense region), LEARNINGS #10.

The criticality coordinate adds a sharper statement about the lead: the CF family's hypothesis has its own dial ($\beta$, the coherence exponent), the literature has marched it from $\beta = 1$ (1993) to $\beta = 1/2$ (2002) to the $\beta \to 0$ edge under a type-I restriction (2011), and the unconditional $\beta = 0$ endpoint is open. That is a *descending staircase that has not yet touched its critical line*, in contrast with the size criteria, whose line was reached in 1959-1984 and has moved only by logarithms since. The geometric family is where headroom remains.

### 11.3 Survey-to-builder handoffs

Three criteria whose hypotheses are closest to being checkable with the existing `experiments/vortex_stretching/` instrumentation (which already computes the strain eigenframe, the depletion factor, and the CF coherence $|\nabla\xi|$ on the intense set; LEARNINGS #10):

1. **The Beirao da Veiga-Berselli $\beta = 1/2$ coherence (the lead handoff).** The experiment currently measures $|\nabla\xi|$, the $\beta = 1$ (CF) modulus. Add the Holder-$1/2$ seminorm of $\xi$ on $\{|\omega| > \text{threshold}\}$ (computable from pairwise dyadic-separation samples on the grid) and track *both* moduli along the run. Deliverable for BUILDER: which $\beta$ the flow actually sustains as the cascade develops, and whether the sustained $\beta$ degrades toward the open $\beta = 0$ endpoint or stalls at the enstrophy height $1/2$. This is a direct experimental probe of the only staircase still descending.
2. **Grujic-type sparseness of the intense set.** The depletion factor $\approx 0.53$ is already measured; the sparseness framework says *why* depletion should happen (filamentary level sets cannot support sustained nonlocal stretching). Add the cheap diagnostic: volume fraction and linear-slice statistics of $\{|\omega| > M\}$ across dyadic $M$, at the instantaneous Taylor microscale. Deliverable: the empirical sparseness-to-depletion curve, which is the quantitative relationship BUILDER would need to convert into a candidate estimate (and the only conditional route in this dossier with a claimed algebraic, rather than logarithmic, bite on the gap).
3. **The Chemin-Zhang critical one-component norm.** $\|u_3\|_{\dot H^{1/2 + 2/p}}$ is a one-line spectral computation in the existing solver. Track it against $\|u\|_{\dot H^{1/2}}$ along Taylor-Green runs (and any future Hou-Luo-type run): the anisotropy ratio measures how much of the critical norm a near-singular flow concentrates in one component. Deliverable: whether the zero-tax one-component criterion is *empirically* much weaker than the full critical norm (large headroom for the anisotropic route) or comparable (the route is cosmetic).

Secondary note for BUILDER: Miller's $\lambda_2^+$ criterion is also directly instrumentable (the strain eigenvalues are already computed), and it is the natural bridge between the alignment statistics and a norm-form criterion.

---

## 12. Discrepancy log

Reported, not resolved (ADVERSARY/VERIFIER to adjudicate):

1. **The CF "critical" label needs a refinement.** The atlas obstruction map calls Constantin-Fefferman "scale-aware geometric," and the reading-notes criticality table calls the CF quantity "dimensionless, scale aware (critical)." The computation in Section 7 refines this: the *object* $\xi$ is scale invariant ($k=0$, critical), but the fixed-constant Holder-$\beta$ hypothesis carries exponent $a = +\beta$, so CF-1993 as stated is a subcritical-demanding hypothesis with tax $1$, BdVB has tax $1/2$, and only the open $\beta = 0$ endpoint is genuinely critical. The CF reading note itself contains the ingredients of this refinement (it notes the Lipschitz constant scales like inverse length) but does not state the $\beta$-ladder. Suggested wording everywhere: "critical object, subcritical-demanding modulus; the critical endpoint $\beta = 0$ is open."
2. **"Every regularity criterion is critical" overstates slightly.** The atlas header and LEARNINGS #2 say every criterion sits at critical scaling. Correct for the size criteria; the one-component family sat strictly *above* critical (taxes $3/8$ to $1$) until Chemin-Zhang 2016, and the geometric family still sits above its own critical endpoint. Suggested wording: "every known criterion sits at critical scaling **or worse** (subcritical-demanding); none is supercritical."
3. **Kukavica-Ziane grouping.** [`../02_graduate/regularity_criteria.md`](../02_graduate/regularity_criteria.md) groups Kukavica-Ziane under one-component criteria without distinguishing the two results: KZ 2006 is one-component velocity ($u_3$, taxed at $3/8$), KZ 2007 is one directional derivative of the full velocity ($\partial_3 u$, zero tax, restricted window). The distinction matters for the criticality ledger.
4. **The "$1/2$ deficit" is currency dependent.** [`../02_graduate/scaling_and_supercriticality.md`](../02_graduate/scaling_and_supercriticality.md) states the deficit is exactly $1/2$; that is the velocity-currency figure. Quadratic quantities (pressure) show deficit $1$. Per power of $u$ it is uniformly $1/2$, so the statement is right in spirit; the dossier's Section 0 records the normalization.

---

## 13. What this enables / what remains open

**Enables.** A complete coordinate chart of Architecture 2: every criterion family located by hypothesis exponent, structural content, and distance from the energy class. BUILDER gets three instrumentable handoffs (11.3) with the $\beta$-dial as the sharpest target; ADVERSARY gets the tax table for auditing any proposed "new criterion" (if its hypothesis exponent is $\ge 0$ and its structure column is "none," it is a relabeling of a known row); SYNTHESIZER gets the discrepancy log (Section 12) and the refined slogan: the size-criteria frontier has been log-thin since 1984, the geometric staircase is still descending.

**Remains open** (the dossier's coordinates for the standing problems):

1. Any unconditional all-time bound at $a = 0$ in any currency (the supercriticality gap itself, Direction 03).
2. The weak-$L^3$ endpoint: $L^\infty_t L^{3,\infty}$ with large norm (the last size endpoint).
3. The $\beta = 0$ unconditional endpoint of the direction-coherence ladder (Direction 02's precise target).
4. The one-component Lebesgue endpoint range, and whether $L^\infty_t \dot H^{1/2}$ on one component suffices **[verify current state]**.
5. Converting observed depletion/sparseness (LEARNINGS #10) into a forced, a priori statement: the only route on the table with a claimed algebraic bite.

---

## References

Primary sources with repo reading notes: [PSL](../03_research/reading_notes/prodi_serrin_ladyzhenskaya.md), [BKM 1984](../03_research/reading_notes/beale_kato_majda_1984.md), [ESS 2003](../03_research/reading_notes/escauriaza_seregin_sverak_2003.md), [Constantin-Fefferman 1993](../03_research/reading_notes/constantin_fefferman_1993.md), [Tao 2019](../03_research/reading_notes/tao_2019_quantitative.md), [Tao 2016](../03_research/reading_notes/tao_2016_averaged.md).

Web-verified during this survey (2026-06-11):

- Cheskidov-Shvydkoy, *The regularity of weak solutions of the 3D Navier-Stokes equations in* $B^{-1}_{\infty,\infty}$, ARMA 195 (2010), 159-169. [arXiv:0708.3067](https://arxiv.org/abs/0708.3067), [Springer](https://link.springer.com/article/10.1007/s00205-009-0265-2).
- Cheskidov-Shvydkoy, *A unified approach ... Kolmogorov's dissipation range*, JMFM 16 (2014). [arXiv:1102.1944](https://arxiv.org/abs/1102.1944).
- Kukavica-Ziane, *Navier-Stokes equations with regularity in one direction*, J. Math. Phys. 48 (2007), 065203. [AIP](https://pubs.aip.org/aip/jmp/article/48/6/065203/914654/Navier-Stokes-equations-with-regularity-in-one).
- Zhou-Pokorny, *On the regularity ... via one velocity component*, Nonlinearity 23 (2010), 1097-1107. [IOPscience](https://iopscience.iop.org/article/10.1088/0951-7715/23/5/004).
- Cao-Titi, *Global regularity criterion ... one entry of the velocity gradient tensor*, ARMA 202 (2011), 919-932. [Springer](https://link.springer.com/article/10.1007/s00205-011-0439-6).
- Berselli-Galdi, *Regularity criteria involving the pressure ...*, Proc. AMS 130 (2002), 3585-3595. [AMS](https://www.ams.org/journals/proc/2002-130-12/S0002-9939-02-06697-2/).
- Miller, *A regularity criterion ... middle eigenvalue of the strain tensor*, ARMA (2019). [arXiv:1710.05569](https://arxiv.org/abs/1710.05569).
- *On the Serrin-type condition on one velocity component ...*, ARMA (2021). [arXiv:1911.02699](https://arxiv.org/abs/1911.02699) **[skimmed title/abstract only]**.

Cited from structural knowledge (statements believed accurate; exact ranges flagged [verify] in the text where uncertain): Serrin 1962; Ladyzhenskaya 1967; Giga 1986; Seregin CMP 312 (2012); Phuc JMFM 17 (2015); Gallagher-Koch-Planchon CMP 343 (2016); Kozono-Taniuchi Math. Z. 235 (2000); Kozono-Ogawa-Taniuchi Math. Z. 242 (2002); Beirao da Veiga, Chinese Ann. Math. B 16 (1995); Chae-Choe EJDE (1999); Chae-Lee (2001); Seregin-Sverak ARMA 163 (2002); Neustupa-Penel (1999); Neustupa-Novotny-Penel (2002); Kukavica-Ziane Nonlinearity 19 (2006); Chemin-Zhang, Ann. Sci. Ec. Norm. Super. 49 (2016); Chemin-Zhang-Zhang ARMA 224 (2017); Beirao da Veiga-Berselli, Differential Integral Equations 15 (2002); Beirao da Veiga, arXiv:1604.08083 (2016); Giga-Miura CMP 303 (2011); Grujic, Nonlinearity 26 (2013); Bradshaw-Farhat-Grujic ARMA (2019); Bourgain-Pavlovic JFA 255 (2008); Chan-Vasseur, Methods Appl. Anal. 14 (2007); Tao, Anal. PDE 2 (2009); Barbato-Morandin-Romito, Anal. PDE 7 (2014); Lions (1960); Shinbrot (1974); Cheskidov-Constantin-Friedlander-Shvydkoy, Nonlinearity 21 (2008); Palasek (2021-2022).
