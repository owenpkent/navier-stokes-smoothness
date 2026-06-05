# Reading notes: Prodi-Serrin-Ladyzhenskaya (1959-1967)

Full citations of the three load-bearing sources:

- G. Prodi, "Un teorema di unicita per le equazioni di Navier-Stokes," Annali di Matematica Pura ed Applicata 48 (1959), 173-182.
- J. Serrin, "On the interior regularity of weak solutions of the Navier-Stokes equations," Arch. Rational Mech. Anal. 9 (1962), 187-195.
- O. A. Ladyzhenskaya, "On uniqueness and smoothness of generalized solutions to the Navier-Stokes equations," Zap. Nauchn. Sem. LOMI 5 (1967), 169-185 (English transl. Sem. Math. V. A. Steklov Math. Inst. Leningrad 5 (1969), 60-66).

> The Prodi-Serrin-Ladyzhenskaya (PSL) criterion is the first sharp conditional-regularity statement of the theory: a Leray-Hopf weak solution that happens to lie in $L^p_t L^q_x$ with $2/p + 3/q \le 1$ and $q > 3$ is automatically smooth, and is the unique Leray-Hopf solution with its data. It is load-bearing because the constraint line $2/p + 3/q = 1$ is exactly the set of $(p,q)$ for which the norm $\|u\|_{L^p_t L^q_x}$ is invariant under the Navier-Stokes scaling. PSL is therefore the original statement that "regularity is a critical-scaling statement," made decades before that language existed. It belongs to Architecture 2 (conditional regularity criteria) and engages primarily structural control (B): it sits exactly at the criticality ceiling, on the critical side, and the supercritical energy norm cannot reach it. ESS (2003) later closed the one excluded point $q = 3$, $p = \infty$; PSL is its parent.

## Statement

Fix the 3D incompressible Navier-Stokes equations on $\mathbb{R}^3$ (or a domain, or $\mathbb{T}^3$) with viscosity $\nu > 0$. Let $u$ be a Leray-Hopf weak solution: $u \in L^\infty_t L^2_x \cap L^2_t \dot H^1_x$ satisfying the equations distributionally and the energy inequality. The PSL family of theorems reads as follows.

**Serrin's interior regularity theorem (1962).** Suppose, in a space-time cylinder $Q = \Omega \times (t_1, t_2)$, that the weak solution satisfies
$$u \in L^p\big(t_1, t_2;\, L^q(\Omega)\big), \qquad \frac{2}{p} + \frac{3}{q} < 1, \qquad q > 3,\ p < \infty.$$
Then $u$ is smooth in the spatial variables in the interior of $Q$ (Serrin obtains spatial smoothness; full space-time smoothness needs the additional pressure or time-derivative argument supplied later). The hypothesis is the strict inequality $2/p + 3/q < 1$, i.e. $u$ lies strictly on the subcritical side of the line.

**Prodi's uniqueness theorem (1959).** If a Leray-Hopf solution $u$ additionally satisfies
$$u \in L^4\big(0,T;\, L^4(\mathbb{R}^3)\big),$$
(the symmetric point $p = q = 4$, which lies on $2/p + 3/q = 1/2 + 3/4 = 5/4$, see the caveat below) then it coincides on $[0,T]$ with every Leray-Hopf solution sharing its initial data. Prodi's actual sufficient condition is more general, of the form $u \in L^p_t L^q_x$ with $2/p + 3/q \le 1$; the $L^4_t L^4_x$ statement is the headline special case in the introduction of his paper. This is the original **weak-strong uniqueness** theorem: as long as one solution in the comparison is regular enough to be in the PSL class, it is the unique Leray-Hopf solution, so uniqueness holds within any interval of regularity.

**Ladyzhenskaya's endpoint-of-the-line theorem (1967).** Ladyzhenskaya treated the borderline equality case
$$u \in L^p\big(0,T;\, L^q(\mathbb{R}^3)\big), \qquad \frac{2}{p} + \frac{3}{q} = 1, \qquad 3 < q \le \infty,\ \ \text{with } p < \infty,$$
proving that this implies both uniqueness and smoothness. The equality case is harder than Serrin's strict inequality because there is no margin: the controlled norm is exactly scale invariant, so the iteration that closes the strict case has zero slack and must be run more carefully. Ladyzhenskaya's contribution is precisely to push the criterion from the open subcritical region $2/p + 3/q < 1$ onto the critical line $2/p + 3/q = 1$ (with $q$ finite).

**Consolidated PSL statement.** A Leray-Hopf solution with
$$u \in L^p_t L^q_x, \qquad \frac{2}{p} + \frac{3}{q} \le 1, \qquad q > 3,\ \ 2 \le p < \infty$$
is smooth on its time interval and is the unique Leray-Hopf solution with its data. The single excluded point is $q = 3$, $p = \infty$ (the $L^\infty_t L^3_x$ corner). That corner is genuinely outside the method and stayed open until Escauriaza-Seregin-Sverak (2003); see [`escauriaza_seregin_sverak_2003.md`](escauriaza_seregin_sverak_2003.md).

### Scaling class of every norm that appears

Under $u_\lambda(x,t) = \lambda\, u(\lambda x, \lambda^2 t)$, the mixed norm rescales as
$$\|u_\lambda\|_{L^p_t L^q_x} = \lambda^{\,1 - 3/q - 2/p}\, \|u\|_{L^p_t L^q_x}.$$
So the scaling exponent of $\|u\|_{L^p_t L^q_x}$ is
$$a(p,q) = 1 - \frac{3}{q} - \frac{2}{p}.$$
Reading off against the criticality bookkeeper convention ($a > 0$ subcritical, $a = 0$ critical, $a < 0$ supercritical):

- $2/p + 3/q < 1 \iff a > 0$: **subcritical** (Serrin's region).
- $2/p + 3/q = 1 \iff a = 0$: **critical**, scale invariant (Ladyzhenskaya's line, and the ESS corner).
- $2/p + 3/q > 1 \iff a < 0$: **supercritical** (where the energy lives; see below).

This is the whole point: the regularity threshold is the zero set of the scaling exponent. The criterion does not improve as you go further subcritical, because subcritical norms all sit on the safe side; the action is the boundary $a = 0$.

## Method / structure

The mechanism is a local-energy bootstrap (Serrin) and a difference-of-solutions energy estimate (Prodi), both driven by the same convective term and the same critical Holder exponent. The lemma-level structure is what matters here.

**Serrin's bootstrap.** Take a weak solution and a test region. The nonlinear term to control is the convective flux $u \otimes u$, equivalently the term $\int (u \cdot \nabla) u \cdot \varphi$ when one differentiates a localized energy. The engine is a single interpolation: split a higher Lebesgue/Sobolev norm of $u$ by Holder against the assumed control $\|u\|_{L^q}$, then absorb the remaining factor into the dissipation $\|\nabla u\|_{L^2}^2$ supplied by the energy class. The Holder split closes (the absorbed exponent is $\le 1$, so it can be hidden in the dissipation with a small constant) precisely when
$$\frac{2}{p} + \frac{3}{q} \le 1.$$
This inequality is not chosen for convenience: it is exactly the exponent count that makes the bilinear estimate scale correctly, i.e. that makes both sides transform the same way under $u_\lambda$. Once the local energy is bounded, parabolic regularity (the smoothing of the heat operator, which requires $\nu > 0$) bootstraps $u$ up to spatial smoothness inside the cylinder. The viscosity enters here in a load-bearing way: it is the heat-kernel smoothing that turns an a priori integrability gain into honest derivatives. A purely inviscid (Euler) version of this step would not bootstrap.

**Prodi's weak-strong uniqueness.** Let $u$ be a (possibly merely Leray-Hopf) solution and $v$ a solution in the PSL class, with the same data. Form $w = u - v$ and write the energy identity for $w$. The only term that does not obviously have a sign is the convective cross term
$$\int (w \cdot \nabla) v \cdot w \, dx,$$
which is the linearization of the nonlinearity about the regular solution $v$. Estimate it by Holder and Sobolev:
$$\Big| \int (w\cdot\nabla) v \cdot w \Big| \le \|w\|_{L^{2q/(q-2)}} \|\nabla v\|_{L^q}\ \text{(schematic)} \lesssim \|w\|_{L^2}^{1-3/q} \|\nabla w\|_{L^2}^{3/q} \|v\|_{L^q},$$
where the Gagliardo-Nirenberg interpolation exponent $3/q$ appears exactly because of the same scaling count. Young's inequality then absorbs the $\|\nabla w\|_{L^2}^2$ factor into the dissipation when $2/p + 3/q \le 1$, leaving a Gronwall inequality $\frac{d}{dt}\|w\|_{L^2}^2 \le g(t)\|w\|_{L^2}^2$ with $g \in L^1_t$ (this is where $v \in L^p_t L^q_x$ with that exponent is used). Since $w(0) = 0$, Gronwall forces $w \equiv 0$. The structure is: regularity of one solution buys a coercive control of the difference, hence uniqueness.

**Where vortex stretching is and is not visible.** The PSL proofs do not name $\omega \cdot \nabla u$. They work at the level of $u$ and the convective term $(u\cdot\nabla)u$. Vortex stretching is implicit: the reason no a priori bound delivers a PSL-class norm in 3D is exactly the production term in the vorticity equation, which is absent in 2D. PSL is genuinely a 3D-aware criterion not because the proof invokes stretching but because the hypothesis it requires (a critical $L^p_t L^q_x$ bound) is precisely what 3D fails to supply and 2D supplies for free (control A, below).

## Criticality placement

Run the controlling norm through the bookkeeper. With $a(p,q) = 1 - 3/q - 2/p$:

| $(p,q)$ | $2/p + 3/q$ | exponent $a$ | class | who |
|---|---|---|---|---|
| $(\infty, \infty)$ | $0$ | $1$ | subcritical | trivial |
| $(p, q)$, $2/p+3/q<1$ | $<1$ | $>0$ | subcritical | Serrin 1962 |
| $(p, q)$, $2/p+3/q=1$, $q<\infty$ | $1$ | $0$ | **critical** | Ladyzhenskaya 1967 |
| $(\infty, 3)$ | $1$ | $0$ | **critical** | open until ESS 2003 |
| $(\infty, 2)$ energy | $3/2$ | $-1/2$ | **supercritical** | Leray 1934 (the only all-time bound) |
| $(4,4)$ Prodi headline | $5/4$ | $-1/4$ | supercritical | Prodi 1959 (uniqueness) |

Two bookkeeping notes that matter for the project.

1. **The Serrin-Ladyzhenskaya line is the criticality boundary itself.** This is not a norm that is incidentally critical (like $L^3$ or $\dot H^{1/2}$, which the bookkeeper lists). It is the entire one-parameter family of critical mixed norms. PSL says: control any one of them and you win. Audit verdict for the line $2/p+3/q = 1$ ($q$ finite): `AT_THE_MARGIN`. Bounding such a norm would close regularity, but no all-time a priori bound at this level is known.

2. **The Prodi $L^4_t L^4_x$ headline is supercritical, and this is the standard point of confusion.** The symmetric exponent $p=q=4$ gives $2/4 + 3/4 = 5/4 > 1$, exponent $a = -1/4$, supercritical. So the famous $L^4 L^4$ condition is *not* on the scaling line. It is the condition for **uniqueness and energy equality** (the same exponent appears in the Lions-Prodi energy-equality criterion $u \in L^4_t L^4_x$), which is a weaker demand than scale-critical regularity: you can be supercritical and still get uniqueness because uniqueness only needs the difference estimate to close in the energy norm, not a scale-invariant bound. Do not conflate "the $L^4 L^4$ uniqueness/energy-equality condition" with "the critical Serrin line." They are different statements with different exponents. (verify the precise sub/superscript of Prodi's most general condition; the headline $L^4 L^4$ result is certain, the fully general exponent range stated in his 1959 paper I am quoting from secondary sources.)

The bookkeeper module that produces these exponents is `experiments/_shared/criticality.py`; its `lebesgue_exponent(q)` gives $1 - 3/q$ for the purely spatial part, and the time integral contributes the $-2/p$ via the parabolic scaling $t \mapsto \lambda^2 t$. The mixed-norm exponent $1 - 3/q - 2/p$ is the natural extension and is what the table above uses.

## Against the three controls

**(A) 2D Navier-Stokes is globally smooth.** PSL passes cleanly and is in fact a sharp diagnostic of why 2D is easy. In 2D the energy class already supplies a PSL-admissible critical bound. Concretely, 2D enstrophy control gives $u \in L^\infty_t \dot H^1 \cap$ better, and the 2D analog of the Serrin line is $2/p + 2/q = 1$ (dimension $d = 2$ replaces the $3$). The 2D energy plus the Ladyzhenskaya inequality $\|u\|_{L^4}^2 \lesssim \|u\|_{L^2}\|\nabla u\|_{L^2}$ delivers $u \in L^4_t L^4_x$, which in 2D sits on the critical line $2/4 + 2/4 = 1$. So in 2D the criterion is *met automatically by the energy*, which is exactly why 2D is globally regular. In 3D the same energy gives only the supercritical side. PSL therefore does not falsely predict 2D blow-up; on the contrary it explains, in one exponent count, why 2D is smooth and 3D is open. This is the criterion behaving correctly under control (A).

**(B) Supercriticality is the ceiling.** This is the control PSL is built around. The energy norm $\|u\|_{L^\infty_t L^2_x}$ has exponent $a = -1/2$ (supercritical), and the dissipation $\|u\|_{L^2_t \dot H^1_x}$ corresponds to $u \in L^2_t L^6_x$ by Sobolev, which sits on $2/2 + 3/6 = 3/2 > 1$, again supercritical ($a = -1/2$). So the entire energy class lies strictly on the supercritical side of the PSL line. There is no Holder interpolation between two supercritical bounds that lands on the critical line: the convex hull of $\{(p,q): 2/p+3/q = 3/2\}$ data points stays at $3/2$, never reaching $1$. This is the precise sense in which the energy cannot supply a PSL bound. The bookkeeper's `audit_estimate` on the energy norm returns `INSUFFICIENT_BY_ITSELF` for exactly this reason. PSL is the cleanest illustration in the literature of the supercriticality gap: it tells you the prize (any critical mixed norm) and the energy tells you that you cannot afford it.

**(C) Viscosity / Burgers.** PSL uses $\nu > 0$ essentially, in the parabolic-smoothing bootstrap step (Serrin) and in absorbing $\|\nabla w\|_{L^2}^2$ into the dissipation (Prodi). It is not a statement about the inviscid flow. The Euler analog of the Serrin bootstrap fails at the smoothing step, consistent with control (C): inviscid models (Burgers shocks, Euler near-singularities) are exactly the regime where the parabolic gain is unavailable. So PSL is not blind to viscosity; it is one of the criteria where viscosity is doing visible work. Note that the *vorticity* version (below) connects PSL to BKM, which is stated for both Euler and NS, so for the vorticity formulation one must be explicit about which regime is meant.

## What it gives / what it does not give

**What it gives.**

1. The first rigorous proof that a single scale-invariant integrability bound forces full smoothness. This converts the regularity question into "produce an a priori bound on some critical $\|u\|_{L^p_t L^q_x}$ with $2/p + 3/q \le 1$, $q > 3$."
2. Weak-strong uniqueness: Leray-Hopf solutions are unique as long as one of them is regular, so non-uniqueness (if it occurs) must happen entirely outside the PSL class. This is the precise frontier that Architecture 5 (convex integration) later attacks: Buckmaster-Vicol (2019) and the Albritton-Brue-Colombo (2022) forced example produce non-unique solutions *below* the PSL/Leray-Hopf regularity, never inside it. PSL draws the line; convex integration colonizes the far side. See [`05_convex_integration_boundary.md`](../research_directions/05_convex_integration_boundary.md).
3. A clean criticality map: the line $2/p + 3/q = 1$ is the regularity threshold, the energy is a fixed distance below it, and that distance ($a = -1/2$) is the size of the gap.

**What it does not give (the gap to closing regularity).**

1. PSL is *conditional*. It assumes a critical bound; it does not produce one. The only unconditional all-time bound (energy) is supercritical and cannot be interpolated up to the line. So PSL by itself closes nothing; it relocates the difficulty to "find a critical a priori estimate," which is the supercriticality gap, [`03_supercriticality_gap.md`](../research_directions/03_supercriticality_gap.md).
2. PSL leaves the corner $q = 3$, $p = \infty$ open. That corner is special because $L^\infty_t L^3_x$ is critical with *no* time integrability to spend, so the bootstrap has nothing to absorb into; it needed the genuinely new backward-uniqueness machinery of ESS. PSL is the parent result that makes the ESS endpoint the obviously-right target.
3. PSL is silent on *how concentrated* a singularity must be. It says blow-up forces every critical $L^p_t L^q_x$ norm (with $q > 3$) to diverge, but gives no rate. The quantitative refinements (Tao 2019 for the $L^3$ endpoint; type-I/type-II distinctions) live downstream.

The honest one-line summary: PSL identifies the target (a critical mixed-norm bound) and proves it would suffice, but the target is exactly the thing the supercritical energy cannot reach, so PSL sharpens the gap rather than crossing it. In the project's frame this is progress: it pins the regularity statement to the zero set of the scaling exponent and certifies that any energy-only argument is `INSUFFICIENT_BY_ITSELF`.

## Lineage and sharpest known form

**Builds on.** Leray (1934) and Hopf (1951) for the weak-solution class and the energy inequality, [`leray_1934.md`](leray_1934.md). The local-energy / interpolation technique is in the lineage that runs through Sobolev embedding and Gagliardo-Nirenberg.

**Vorticity versions.** The same scaling line has a vorticity formulation. If $\omega = \mathrm{curl}\, u \in L^p_t L^q_x$ with $2/p + 3/q \le 2$ and $q > 3/2$, the solution is regular (Beirao da Veiga, 1995, and predecessors). The shift from $1$ to $2$ on the right-hand side is exactly the one derivative between $u$ and $\omega$: $\omega$ scales one power of $\lambda$ higher than $u$, so the critical line moves. The sharpest pointwise vorticity statement is Beale-Kato-Majda, $\int_0^T \|\omega\|_{L^\infty}\, dt < \infty$, which is the $p = 1$, $q = \infty$ corner of the vorticity line $2/p + 3/q = 2$ (giving $2/1 + 3/\infty = 2$, on the line), [`beale_kato_majda_1984.md`](beale_kato_majda_1984.md). PSL on $u$ and BKM on $\omega$ are the same critical-scaling phenomenon one derivative apart.

**Built on it.**

- **The endpoint:** Escauriaza-Seregin-Sverak (2003) closed $L^\infty_t L^3_x$, the one PSL omission, by backward uniqueness and Carleman estimates rather than bootstrap, [`escauriaza_seregin_sverak_2003.md`](escauriaza_seregin_sverak_2003.md).
- **Component reductions:** regularity from fewer than all three velocity components, or from one component, on Serrin-type scaling lines (Kukavica-Ziane; Chemin-Zhang; Chemin-Zhang-Zhang for the one-component scaling-invariant criterion). These exploit the divergence-free constraint to need less data, and are catalogued under [`02_vorticity_geometry.md`](../research_directions/02_vorticity_geometry.md) and the anisotropic-norm thread of [`03_supercriticality_gap.md`](../research_directions/03_supercriticality_gap.md).
- **Lorentz and logarithmic refinements:** the spatial exponent can be relaxed to the Lorentz space $L^{q,\infty}$ (weak-$L^q$) on the same line for $q > 3$; the endpoint $L^{3,\infty}$ is borderline and known under a smallness assumption (Kozono; Sohr). Log-in-time improvements of the Prodi-Serrin criteria exist (Montgomery-Smith; Chan-Vasseur-type log relaxations).
- **Pressure and gradient versions:** Serrin-type conditions on $\nabla u$ ($2/p + 3/q \le 2$) and on the pressure $\pi$ ($2/p + 3/q \le 2$ for $\pi \in L^p_t L^q_x$, Berselli-Galdi and others), each the natural one-derivative or pressure analog on its own critical line.

**Sharpest known form as of 2025.** The criterion family is essentially closed on the line $2/p + 3/q = 1$: regularity holds for all $3 < q \le \infty$ with $p < \infty$ (Serrin-Ladyzhenskaya) and at the corner $q = 3$, $p = \infty$ (ESS). The remaining research frontier is not the line itself but (i) replacing the strong norm by a weaker critical object (Lorentz $L^{3,\infty}$ in time-space is still only conditional, requiring smallness), (ii) the quantitative form (Tao 2019: a Type-I-like triple-logarithmic lower bound on the growth of the critical norm at a putative singularity, the $L^3$ endpoint of the PSL family), and (iii) anisotropic / one-component scaling-invariant versions. All three are surveyed under Direction 01, [`01_critical_continuation_criteria.md`](../research_directions/01_critical_continuation_criteria.md). No unconditional a priori bound on any point of the line is known; that is the unchanged headline.

## References

- G. Prodi, "Un teorema di unicita per le equazioni di Navier-Stokes," Annali di Matematica Pura ed Applicata 48 (1959), 173-182.
- J. Serrin, "On the interior regularity of weak solutions of the Navier-Stokes equations," Arch. Rational Mech. Anal. 9 (1962), 187-195.
- O. A. Ladyzhenskaya, "On uniqueness and smoothness of generalized solutions to the Navier-Stokes equations," Zap. Nauchn. Sem. LOMI 5 (1967), 169-185; Engl. transl. Sem. Math. V. A. Steklov Math. Inst. Leningrad 5 (1969), 60-66.
- J. Leray, "Sur le mouvement d'un liquide visqueux emplissant l'espace," Acta Math. 63 (1934), 193-248.
- E. Hopf, "Uber die Anfangswertaufgabe fur die hydrodynamischen Grundgleichungen," Math. Nachr. 4 (1951), 213-231.
- J. T. Beale, T. Kato, A. Majda, "Remarks on the breakdown of smooth solutions for the 3-D Euler equations," Comm. Math. Phys. 94 (1984), 61-66.
- H. Beirao da Veiga, "A new regularity class for the Navier-Stokes equations in $\mathbb{R}^n$," Chinese Ann. Math. Ser. B 16 (1995), 407-412.
- L. Escauriaza, G. Seregin, V. Sverak, "$L_{3,\infty}$-solutions of Navier-Stokes equations and backward uniqueness," Russian Math. Surveys 58 (2003), 211-250.
- J.-Y. Chemin, P. Zhang, "On the critical one component regularity for 3-D Navier-Stokes system," Ann. Sci. Ec. Norm. Super. 49 (2016).
- T. Tao, "Quantitative bounds for critically bounded solutions of the Navier-Stokes equations," (2019, arXiv:1908.04958).
- T. Buckmaster, V. Vicol, "Nonuniqueness of weak solutions to the Navier-Stokes equation," Ann. of Math. 189 (2019), 101-144.
- D. Albritton, E. Brue, M. Colombo, "Non-uniqueness of Leray solutions of the forced Navier-Stokes equations," Ann. of Math. 196 (2022), 415-455.
- J. C. Robinson, "The Navier-Stokes regularity problem," Philos. Trans. R. Soc. A 378 (2020), 20190526 (survey used to confirm the historical attributions of the equality-line case).

## Cross-links

- Research direction (primary): [`01_critical_continuation_criteria.md`](../research_directions/01_critical_continuation_criteria.md) (PSL is the founding member of this family).
- Research direction (the gap PSL exposes): [`03_supercriticality_gap.md`](../research_directions/03_supercriticality_gap.md).
- Research direction (component / anisotropic descendants and vorticity geometry): [`02_vorticity_geometry.md`](../research_directions/02_vorticity_geometry.md).
- Research direction (the far side of the weak-strong uniqueness line): [`05_convex_integration_boundary.md`](../research_directions/05_convex_integration_boundary.md).
- Sibling note (the endpoint PSL omitted): [`escauriaza_seregin_sverak_2003.md`](escauriaza_seregin_sverak_2003.md).
- Sibling note (the vorticity, one-derivative-up cousin): [`beale_kato_majda_1984.md`](beale_kato_majda_1984.md).
- Sibling note (the class PSL conditions live in): [`leray_1934.md`](leray_1934.md).
