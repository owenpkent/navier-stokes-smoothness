# Reading notes: Lin (1998) and Vasseur (2007), streamlined proofs of CKN partial regularity

Fanghua Lin, "A new proof of the Caffarelli-Kohn-Nirenberg theorem," Comm. Pure Appl. Math. 51 (1998), 241-257.

Alexis Vasseur, "A new proof of partial regularity of solutions to Navier-Stokes equations," NoDEA Nonlinear Differential Equations Appl. 14 (2007), 753-785.

> These two papers re-prove the central unconditional regularity theorem of Architecture 1, the Caffarelli-Kohn-Nirenberg (CKN) partial regularity theorem, by methods that are shorter, more modular, and more transparent about *where the criticality lives* than the original 1982 argument. Lin's proof replaces the explicit interpolation-and-iteration of CKN by a blow-up / compactness contradiction: the $\varepsilon$-regularity theorem becomes a statement that the only limit of a sequence of solutions with vanishing scale-invariant local energy is a regular (in fact linear-heat-controlled) solution. Vasseur replaces the iteration by the De Giorgi method: local boundedness of $u$ on a small cylinder is extracted from the local energy inequality alone, by a nonlinear truncation-energy iteration across a nested family of cylinders. Both land on the same conclusion as CKN, $\mathcal{P}^1(S) = 0$, but they make explicit a fact the project cares about: the $\varepsilon$-regularity mechanism is a *critical-scaling* statement run on top of a *supercritical* energy budget, and the gap between "$\mathcal{P}^1(S)=0$" and "$S=\varnothing$" is exactly the supercriticality gap (control B). They engage Architecture 1 and the supercriticality control; they do not, and structurally cannot, close regularity.

For the original theorem and its statement, see the sibling note [`caffarelli_kohn_nirenberg_1982.md`](caffarelli_kohn_nirenberg_1982.md). This note assumes that note as background and focuses on what the two streamlined proofs add.

---

## Statement

Both papers prove the same two-part result. Fix a **suitable weak solution** $(u,p)$ of the 3D incompressible Navier-Stokes equations on a spacetime domain, that is a Leray-Hopf weak solution that additionally satisfies the **local energy inequality**: for all nonnegative $\phi \in C_c^\infty$,

$$
\int |u(t)|^2 \phi\,dx + 2\nu \int\!\!\int |\nabla u|^2 \phi\,dx\,ds
\;\le\;
\int\!\!\int |u|^2(\partial_t \phi + \nu \Delta\phi)\,dx\,ds
+ \int\!\!\int \big(|u|^2 + 2p\big)\, u\cdot\nabla\phi\,dx\,ds .
$$

Write $Q_r(z_0) = B_r(x_0)\times(t_0 - r^2, t_0)$ for the backward parabolic cylinder, and let $S$ be the singular set, the spacetime points near which $u$ is not (essentially) locally bounded.

**Theorem ($\varepsilon$-regularity).** There is an absolute constant $\varepsilon_0 > 0$ such that if

$$
\frac{1}{r^2}\int\!\!\int_{Q_r(z_0)} |u|^3 + |p|^{3/2}\,dx\,dt \;\le\; \varepsilon_0 ,
$$

then $u$ is Hölder continuous (in particular bounded) on the smaller cylinder $Q_{r/2}(z_0)$, so $z_0 \notin S$. Lin and Vasseur prove this with the scale-invariant quantity in the $L^3$ form above; the original CKN used the closely related gradient form $\frac1r\iint_{Q_r}|\nabla u|^2$. The two are equivalent inputs to the same conclusion.

**Theorem (dimension of the singular set).** As a consequence,

$$
\mathcal{P}^1(S) = 0 ,
$$

the one-dimensional **parabolic** Hausdorff measure of $S$ is zero. In particular $\dim_{\mathcal P} S \le 1$, $S$ contains no spacetime curve, and at each fixed time the spatial singular set has Hausdorff dimension at most $1$.

The single most important structural remark, made cleanly by both proofs: every quantity in the $\varepsilon$-regularity hypothesis is **scale invariant** under the Navier-Stokes scaling $u_\lambda(x,t) = \lambda\,u(\lambda x, \lambda^2 t)$, $p_\lambda(x,t) = \lambda^2\,p(\lambda x, \lambda^2 t)$. The $\varepsilon$-regularity theorem is therefore a *critical* statement: regularity follows from smallness of a scale-invariant local quantity. The whole question is then why this critical smallness cannot be guaranteed everywhere, and the answer is that the only global budget feeding it is the supercritical energy.

---

## Method / structure: Lin's compactness proof

Lin's contribution is to extract the $\varepsilon$-regularity theorem from a **blow-up and compactness contradiction** rather than from explicit iterated interpolation inequalities. The skeleton:

1. **Scale-invariant functionals.** Define the dimensionless local quantities
$$
A(r) = \sup_{t}\frac1r\int_{B_r}|u|^2,\quad
\delta(r) = \frac1r\int\!\!\int_{Q_r}|\nabla u|^2,\quad
G(r) = \frac1{r^2}\int\!\!\int_{Q_r}|u|^3,\quad
K(r) = \frac1{r^2}\int\!\!\int_{Q_r}|p|^{3/2},
$$
each invariant under the NS scaling. The local energy inequality and the pressure equation $-\Delta p = \partial_i\partial_j(u_i u_j)$ relate these across scales.

2. **The decay step as a compactness statement.** The heart is an iteration inequality of the form: there is $\theta \in (0,1)$ such that if the scale-invariant energy at scale $r$ is below $\varepsilon_0$, then it decreases by a fixed factor at scale $\theta r$. Lin proves this *not* by tracking constants but by contradiction. Suppose it fails. Then there is a sequence $(u^{(k)}, p^{(k)})$ of suitable solutions whose scale-invariant local energy tends to zero but whose decay step fails. Rescale each to unit scale. By the a priori bounds (the energy inequality plus the pressure estimate $\|p\|_{L^{3/2}} \lesssim \|u\|_{L^3}^2$ from the Calderon-Zygmund theory of the Leray projector) the rescaled sequence is compact in the relevant local norms.

3. **The limit is a heat solution.** The limit $(u^\infty, p^\infty)$ of the rescaled sequence, because its nonlinear term has been driven to zero by the smallness, satisfies a *linear* problem: $u^\infty$ is controlled by the heat equation. Linear parabolic regularity gives the missing decay for $u^\infty$, contradicting the assumed failure. The nonlinearity $u\cdot\nabla u$ and the pressure are present only as perturbations that vanish in the limit; this is exactly why the limit is regular.

4. **Covering.** With the decay step in hand, the points where the scale-invariant energy stays above $\varepsilon_0$ at all scales form $S$. A Vitali-type parabolic covering converts the per-point smallness failure into the measure bound $\mathcal{P}^1(S)=0$. This step is essentially unchanged from CKN.

The conceptual gain: the $\varepsilon$-regularity theorem is revealed to be a statement that *the rescaled blow-up of any potential singularity is a solution of the linear heat equation*, and such a solution cannot be singular. The role of the smallness $\varepsilon_0$ is precisely to make the nonlinearity subdominant under blow-up rescaling. This blow-up viewpoint is the same idea that organizes Architecture 4 (Necas-Ruzicka-Sverak, Jia-Sverak) and Architecture 2 (the rescaling in Escauriaza-Seregin-Sverak); Lin makes it the organizing principle of partial regularity as well.

---

## Method / structure: Vasseur's De Giorgi proof

Vasseur's contribution is to obtain **local boundedness of $u$ directly from the local energy inequality** by the **De Giorgi iteration**, the technique De Giorgi introduced (1957) for Holder continuity of solutions of second-order elliptic equations with bounded measurable coefficients (Hilbert's 19th problem). The structure:

1. **Truncation energies.** For a level $L \ge 0$ define the truncated function $u_L = (|u| - L)_+$, the positive part of $|u|$ above the level $L$. The strategy is to show that for a suitable increasing sequence of levels $L_k \uparrow L_\infty$ and shrinking cylinders $Q_{r_k} \downarrow Q_{r_\infty}$, the "energy of the part of $u$ above level $L_k$ on cylinder $Q_{r_k}$,"
$$
\mathcal{E}_k = \sup_t \int_{B_{r_k}} u_{L_k}^2\,dx + \int\!\!\int_{Q_{r_k}} |\nabla u_{L_k}|^2\,dx\,dt ,
$$
satisfies a **nonlinear recurrence** $\mathcal{E}_{k+1} \le C\, b^{k}\, \mathcal{E}_k^{1+\beta}$ for constants $C, b > 1$ and an exponent $\beta > 0$.

2. **Why a superlinear recurrence is the whole game.** A recurrence of the form $\mathcal{E}_{k+1} \le C b^k \mathcal{E}_k^{1+\beta}$ has the property that *if the initial energy $\mathcal{E}_0$ is below a threshold depending only on $C, b, \beta$, then $\mathcal{E}_k \to 0$*. Driving $\mathcal{E}_k \to 0$ means $u_{L_\infty} = 0$ on $Q_{r_\infty}$, that is $|u| \le L_\infty$ there: **local boundedness**. The smallness of $\mathcal{E}_0$ is exactly the $\varepsilon$-regularity hypothesis. So De Giorgi turns "small scale-invariant local energy" into "bounded" by a purely iterative, constant-light mechanism.

3. **Where the local energy inequality enters.** Each step of the recurrence is the local energy inequality applied to the truncated field $u_{L_k}$, combined with the parabolic Sobolev embedding $L^\infty_t L^2_x \cap L^2_t \dot H^1_x \hookrightarrow L^{10/3}_{t,x}$ in $3+1$ dimensions. The gain $\beta > 0$ comes from the measure of the set $\{|u| > L_k\}$ shrinking as the level rises (a "deLevel" or energy-gain factor), which upgrades a linear estimate to a superlinear one. The Sobolev exponent $10/3$ is the same parabolic embedding that drives every energy-method estimate; here it provides the nonlinear excess $\beta$.

4. **The pressure.** The local energy inequality contains the pressure through the term $\iint (|u|^2 + 2p)\,u\cdot\nabla\phi$. Vasseur handles the pressure by the standard splitting $p = p_{\mathrm{loc}} + p_{\mathrm{harm}}$: a local Calderon-Zygmund part $-\Delta p_{\mathrm{loc}} = \partial_i\partial_j(u_iu_j)$ controlled in $L^{3/2}$ by $\|u\|_{L^3}^2$, and a harmonic remainder $\Delta p_{\mathrm{harm}} = 0$ on the cylinder that is smooth in the interior and so contributes only lower-order, controllable terms after a further interior shrink. This is the one nonlocal ingredient; everything else in the De Giorgi iteration is local. The pressure is *not* a higher-order obstruction here, it is a bounded perturbation, precisely because $L^3$-control of $u$ buys $L^{3/2}$-control of $p$ at the same scaling.

5. **From boundedness to full $\varepsilon$-regularity and $\mathcal{P}^1(S)=0$.** Once $u$ is locally bounded on a cylinder, standard parabolic bootstrapping (the equation becomes subcritical) gives Holder continuity and then smoothness in the interior. The covering argument producing $\mathcal P^1(S)=0$ is then identical to CKN. So De Giorgi supplies the *hard* step, local boundedness from local energy, and the rest is classical.

The conceptual clarification Vasseur isolates: the *only* thing standing between the local energy inequality and local boundedness is a nonlinear iteration that needs a small initial scale-invariant energy. There is no hidden critical input. This is why partial regularity is unconditional (it needs no assumption beyond suitability) and also why it stops where it does: the iteration converges only from below the threshold $\varepsilon_0$, and nothing in the energy budget forces the local scale-invariant energy below $\varepsilon_0$ at every point.

---

## Criticality placement

Run the quantities through the criticality bookkeeper (`experiments/_shared/criticality.py`), using the convention there that exponent $a$ in $\|u_\lambda\|_X = \lambda^a\|u\|_X$ gives $a>0$ subcritical, $a=0$ critical, $a<0$ supercritical.

- **The $\varepsilon$-regularity functionals are critical ($a=0$).** Each of $\frac1r\int_{B_r}|u|^2$, $\frac1r\iint_{Q_r}|\nabla u|^2$, $\frac1{r^2}\iint_{Q_r}|u|^3$, $\frac1{r^2}\iint_{Q_r}|p|^{3/2}$ is scale invariant. Spatially, $\|u\|_{L^3}$ has `lebesgue_exponent(3)` $= 1 - 3/3 = 0$: this is the **same critical $L^3$ scale** as Escauriaza-Seregin-Sverak (see [`escauriaza_seregin_sverak_2003.md`](escauriaza_seregin_sverak_2003.md)). Lin and Vasseur both make this explicit by writing the hypothesis in the $\iint |u|^3 + |p|^{3/2}$ form. The $\varepsilon$-regularity theorem is the *local* critical statement; ESS is the *global* one. Both say: control the critical $L^3$-scaled quantity and you get regularity.

- **The driving budget is supercritical ($a<0$).** The global a priori bound feeding the local functionals is the energy inequality, controlling $\|u\|_{L^\infty_t L^2_x}$ and $\|\nabla u\|_{L^2_{t,x}}$. By the bookkeeper, `lebesgue_exponent(2)` $= 1 - 3/2 = -1/2 < 0$: **supercritical** (control B fires). The parabolic Sobolev space $L^{10/3}_{t,x}$ that the energy controls has the spacetime scaling exponent that makes $\iint_{Q_r}|u|^{10/3}$ scale like $r^{0}$ only after the $r^{-?}$ normalization; the relevant point is that energy delivers $u \in L^{10/3}_{t,x}$, which is *one half a parabolic dimension short* of the critical $L^5_{t,x}$ (the spacetime Prodi-Serrin endpoint $2/p+3/q\le1$ with $p=q=5$). That half-dimension deficit is the $\mathcal P^1$ in the conclusion.

- **The dimension $1$ is the supercriticality deficit made geometric.** The reason the singular set lands at parabolic dimension $\le 1$ rather than $0$ is the gap between the supercritical energy ($a=-1/2$ for $L^2$) and the critical $L^3$ / $L^5_{t,x}$ scale ($a=0$). The covering argument can only excise the points where the *energy*-supplied scale-invariant quantity is small, and energy is half a power short of guaranteeing that everywhere. Audit verdict from `audit_estimate` on the controlling norm ($L^2$ energy): `INSUFFICIENT_BY_ITSELF`. The $\varepsilon$-regularity theorem, audited on its own controlling norm ($L^3$, critical): `AT_THE_MARGIN`, would close regularity if a global $L^3$ bound were available, which is exactly ESS-style and not known unconditionally.

This is the cleanest illustration in the corpus of the project's central thesis: a *critical* local mechanism ($\varepsilon$-regularity) sitting on a *supercritical* global budget (energy) yields a *partial* result whose precise dimension ($1$) is the numerical image of the criticality gap.

---

## Against the three controls

- **Control A (2D must stay smooth).** Both proofs are dimension-honest. The parabolic Sobolev embedding exponent ($L^{10/3}_{t,x}$ in $3{+}1$ dimensions) and the pressure estimate ($\|p\|_{L^{3/2}}\lesssim\|u\|_{L^3}^2$) depend on $d=3$. Run the same machinery in 2D and the energy budget already controls the critical scale outright (in 2D, $\|u\|_{L^2}$ has `lebesgue_exponent(2, d=2)` $= 1 - 2/2 = 0$, **critical**, not supercritical), so the $\varepsilon$-regularity smallness is automatically available everywhere and $S = \varnothing$: full regularity, as it must be. Neither proof would falsely predict 2D blow-up. Note however that neither proof uses the *vortex-stretching* structure $\omega\cdot\nabla u$ explicitly; they are velocity-energy arguments. They pass control A by the scaling arithmetic (energy is critical in 2D, supercritical in 3D), not by engaging the 2D-versus-3D *mechanism*. This is a structural limitation shared with all energy-method partial regularity: it sees the deficit but not the stretching term that would have to be tamed to remove it.

- **Control B (supercriticality is the ceiling).** Both proofs *exhibit* the ceiling rather than break it. The driving norm is the supercritical $L^2$ energy; the conclusion is partial ($\mathcal P^1(S)=0$), not full. The bookkeeper audit returns `INSUFFICIENT_BY_ITSELF` on the controlling norm. These proofs are, in the project's terms, the sharpest possible *consequence* of energy plus the critical $\varepsilon$-regularity scaling, and the residual dimension-$1$ singular set is the unbridged gap. They neither violate nor close control B; they measure it.

- **Control C (viscosity / exact NS structure).** Viscosity is load-bearing in both. The parabolic cylinder geometry $Q_r = B_r\times(t_0-r^2,t_0)$, the $\partial_t - \nu\Delta$ heat operator whose linear regularity Lin's limit inherits, the dissipation term $2\nu\iint|\nabla u|^2$ in the local energy inequality, and the $L^{10/3}_{t,x}$ embedding that uses the *parabolic* (heat) smoothing are all viscosity-dependent. Set $\nu = 0$ (Euler) and the local energy inequality loses its coercive dissipation, the De Giorgi gain $\beta>0$ disappears (no $L^2_t\dot H^1_x$ to feed the Sobolev embedding), and Lin's blow-up limit is no longer a heat solution. Both proofs would fail for Euler, correctly: there is no analogous unconditional partial regularity for Euler, and the modern $C^{1,\alpha}$ Euler singularity results (Elgindi 2021) show why one should not expect one. The proofs pass control C cleanly: remove viscosity and they break exactly where they should.

Summary: Lin and Vasseur are well-behaved against all three controls. They are *not* regularity-closing, and the reason is precisely control B: they live on the supercritical energy budget and convert it, optimally, into a critical local statement, but the conversion leaves a half-parabolic-dimension residue.

---

## What it gives / what it does not give

**What it gives.**

- Two independent, shorter, and more modular routes to $\mathcal P^1(S)=0$, each importing a powerful external technique into NS partial regularity: Lin imports the **blow-up/compactness** method (the same engine as the Liouville-theorem program for self-similar solutions), Vasseur imports the **De Giorgi iteration** (the bounded-measurable-coefficients regularity machine).
- A clean separation of concerns. Lin: the only obstruction to regularity is that the rescaled blow-up could be nonlinear; smallness kills the nonlinearity. Vasseur: the only obstruction is that a truncation-energy iteration could fail to converge; smallness guarantees convergence. Both isolate the role of the smallness threshold $\varepsilon_0$ as the gate.
- A reusable toolkit. The De Giorgi-for-NS method has since been the template for partial regularity in many related systems (MHD, Navier-Stokes-Planck-Nernst-Poisson, liquid crystals, hyperdissipative NS), because it is local and robust to lower-order couplings. This is the main *technological* legacy.
- An explicit, audit-ready placement of the $\varepsilon$-regularity hypothesis at the critical $L^3$ / $L^5_{t,x}$ scale, which is the same scale as ESS. This makes the link between unconditional partial regularity (Architecture 1) and the conditional critical criteria (Architecture 2) precise rather than analogical.

**What it does not give (the gap to closing regularity).**

- It does **not** improve the dimension of the singular set below $1$. The conclusion is identical to CKN 1982. The new proofs are sharper in *method*, not in *result*. Pushing $\mathcal P^1(S)=0$ toward $S=\varnothing$ requires a genuinely *more-than-energy* global bound, i.e. some global control at the critical scale, which is the open problem and is precisely what control B says energy alone cannot supply.
- It does **not** engage 3D vortex stretching. Like all velocity-energy partial regularity, it treats the nonlinearity as a perturbation to be dominated by smallness, not as a structure to be exploited. A regularity-closing argument almost certainly has to use $\omega\cdot\nabla u$ (the term absent in 2D); these proofs route around it. See [`../research_directions/02_vorticity_geometry.md`](../research_directions/02_vorticity_geometry.md).
- It does **not** provide a *quantitative, self-improving* critical estimate of the kind that would upgrade local $\varepsilon$-regularity into a global statement. The Tao (2019) quantitative-ESS program (triple-log lower bound on $\|u\|_{L^3}$ growth at a singularity) is the right shape for that upgrade, and it is conditional; De Giorgi/compactness partial regularity is its unconditional but strictly weaker shadow. See [`../research_directions/01_critical_continuation_criteria.md`](../research_directions/01_critical_continuation_criteria.md).

Net: these papers are the optimal *unconditional* squeeze of the supercritical energy budget through a critical local mechanism. The residue is the supercriticality gap, dimension $1$, and closing it is a different (critical, 3D-structure-using) kind of input. See [`../research_directions/03_supercriticality_gap.md`](../research_directions/03_supercriticality_gap.md).

---

## Lineage and sharpest known form

**Builds on.**

- Scheffer (1976-1980): first partial regularity and the first Hausdorff-dimension bounds for the space-time singular set (at most $5/3$ for the space-time set in early work).
- Caffarelli-Kohn-Nirenberg, Comm. Pure Appl. Math. 35 (1982): the theorem itself, $\mathcal P^1(S)=0$, via explicit $\varepsilon$-regularity and interpolation.
- De Giorgi (1957): the iteration method, originally for elliptic equations with bounded measurable coefficients (Hilbert's 19th problem); Vasseur transplants it to the parabolic NS setting.

**Built on it / parallel streamlinings.**

- Lin's compactness method and Vasseur's De Giorgi method became the two standard modern templates. Both are now textbook (for example in Robinson-Rodrigo-Sadowski, "The Three-Dimensional Navier-Stokes Equations," Cambridge 2016, and in Tsai, "Lectures on Navier-Stokes Equations," AMS GSM 192, 2018).
- **Box-counting (Minkowski) dimension refinements.** Hausdorff $\mathcal P^1(S)=0$ leaves open the *box-counting* dimension, which is larger and controls covering numbers uniformly. Robinson-Sadowski, "Decay of weak solutions and the singular set of the three-dimensional Navier-Stokes equations," Nonlinearity 20 (2007), 1185-1191, proved the upper box-counting dimension of the set of *singular times* is at most $1/2$, and bounded the space-time box-counting dimension (at most $5/3$, matching Scheffer's Hausdorff bound but now in the stronger box sense). Kukavica, "On partial regularity for the Navier-Stokes equations," Discrete Contin. Dyn. Syst. 21 (2008), 717-728, and the subsequent Kukavica-Pei works pushed the upper box-counting dimension of the space-time singular set below $5/3$: to $135/82 \approx 1.646$, then $45/29 \approx 1.552$, and later to $135/104 \approx 1.298$ by exploiting the **pressure** term more fully. (Exact constants vary by hypothesis; treat the chain $5/3 \to 135/82 \to 45/29 \to 135/104$ as the trajectory rather than a single canonical number. (verify))
- **Lower-bound / wild side.** Convex-integration-adjacent constructions (Architecture 5) produce weak solutions whose singular sets in *time* have Hausdorff dimension strictly below $1$ (Buckmaster-Colombo-Vicol and successors), which is a statement about the *boundary of what "solution" means* below the energy class, not about suitable weak solutions. It sits partly outside the three-control discipline (it is about non-uniqueness, not regularity of the smooth flow). See [`../research_directions/05_convex_integration_boundary.md`](../research_directions/05_convex_integration_boundary.md).
- **Robustness legacy.** The De Giorgi-for-NS template (Vasseur) underlies partial-regularity results for coupled and hyperdissipative systems and for boundary $\varepsilon$-regularity, and reappears in the "one scale" pressure-free regularity criteria of the 2010s.

**Sharpest known form as of 2025.**

- The *Hausdorff* result is still $\mathcal P^1(S)=0$ (CKN 1982, re-proved by Lin 1998 and Vasseur 2007); it has not been improved. The frontier of *improvement* is the **box-counting** dimension, where the chain above (Kukavica; Kukavica-Pei; and refinements using the pressure) has pushed the space-time bound toward $\approx 1.3$. (verify exact current record)
- The conceptual frontier for *closing* the gap is not in this lineage at all: it is the quantitative critical program (Tao 2019; Barker-Prange quantitative regularity, 2021) and the geometric / vortex-direction criteria (Constantin-Fefferman 1993), which add critical or 3D-structural input that energy-based partial regularity lacks.

---

## What this enables / what remains open

**Enables (for BUILDER and SYNTHESIZER).**

- A precise template for the *shape* of any improvement: partial regularity converts a global budget into a local scale-invariant smallness via a robust iteration/compactness step. To move the needle, BUILDER must supply a *global* quantity that is critical (scaling exponent $0$) or subcritical, not the supercritical $L^2$ energy. The De Giorgi recurrence and the compactness Liouville step are reusable scaffolds for testing whether a proposed new critical bound would actually drive the singular set empty.
- A clean unification point: the $\varepsilon$-regularity hypothesis is the *same* $L^3$ critical scale as ESS. Any BUILDER candidate that controls a critical norm globally can be checked against *both* the local ($\varepsilon$-regularity) and global (ESS) statements with one criticality audit.
- A concrete falsifiable handle: if a proposed estimate's controlling norm runs through `experiments/_shared/criticality.py` as supercritical, `audit_estimate` returns `INSUFFICIENT_BY_ITSELF`, and the estimate cannot, by these proofs' own logic, do better than dimension-$1$ partial regularity. That is a fast wrong-approach filter.

**Remains open (for ADVERSARY to probe and the program to target).**

- Whether $S=\varnothing$ (full regularity). The dimension-$1$ residue is exactly the supercriticality gap; nothing in these two proofs touches it.
- Whether the *box-counting* dimension can be pushed to $0$ or below $1$ unconditionally (the current chain stalls around $\approx 1.3$, far from $0$). A genuinely new critical input would be needed.
- Whether a partial-regularity-style argument can be made to *use* $\omega\cdot\nabla u$ rather than dominate the nonlinearity by smallness. No such argument exists; this is where control A's "must use 3D structure" demand bites the hardest. The honest reading: Lin and Vasseur perfected the energy-side method, and its ceiling is the supercriticality gap, which is a compass pointing at critical, vortex-stretching-aware control as the place the real proof must live.

---

## References

- F. Lin, "A new proof of the Caffarelli-Kohn-Nirenberg theorem," Comm. Pure Appl. Math. 51 (1998), 241-257.
- A. Vasseur, "A new proof of partial regularity of solutions to Navier-Stokes equations," NoDEA Nonlinear Differential Equations Appl. 14 (2007), 753-785. DOI 10.1007/s00030-007-6001-4.
- L. Caffarelli, R. Kohn, L. Nirenberg, "Partial regularity of suitable weak solutions of the Navier-Stokes equations," Comm. Pure Appl. Math. 35 (1982), 771-831.
- V. Scheffer, "Hausdorff measure and the Navier-Stokes equations," Comm. Math. Phys. 55 (1977), 97-112, and related Scheffer papers (1976-1980).
- E. De Giorgi, "Sulla differenziabilita e l'analiticita delle estremali degli integrali multipli regolari," Mem. Accad. Sci. Torino Cl. Sci. Fis. Mat. Natur. (3) 3 (1957), 25-43.
- J. C. Robinson, W. Sadowski, "Decay of weak solutions and the singular set of the three-dimensional Navier-Stokes equations," Nonlinearity 20 (2007), 1185-1191.
- I. Kukavica, "On partial regularity for the Navier-Stokes equations," Discrete Contin. Dyn. Syst. 21 (2008), 717-728; and Kukavica-Pei, box-counting dimension refinements (singular-set Minkowski dimension below $5/3$, improved using the pressure). (verify exact constants/venues)
- L. Escauriaza, G. Seregin, V. Sverak, "$L_{3,\infty}$-solutions of Navier-Stokes equations and backward uniqueness," Russian Math. Surveys 58 (2003), 211-250.
- T. Tao, "Quantitative bounds for critically bounded solutions of the Navier-Stokes equations" (2019).
- J. C. Robinson, J. L. Rodrigo, W. Sadowski, "The Three-Dimensional Navier-Stokes Equations," Cambridge Univ. Press (2016) (textbook treatment of both proofs).
- T.-P. Tsai, "Lectures on Navier-Stokes Equations," AMS Grad. Studies in Math. 192 (2018) (textbook treatment).

## Cross-links

- Direction 01: [`../research_directions/01_critical_continuation_criteria.md`](../research_directions/01_critical_continuation_criteria.md) (the critical-scale criteria these proofs shadow).
- Direction 02: [`../research_directions/02_vorticity_geometry.md`](../research_directions/02_vorticity_geometry.md) (the $\omega\cdot\nabla u$ structure these proofs route around).
- Direction 03: [`../research_directions/03_supercriticality_gap.md`](../research_directions/03_supercriticality_gap.md) (the gap the dimension-$1$ residue measures).
- Direction 05: [`../research_directions/05_convex_integration_boundary.md`](../research_directions/05_convex_integration_boundary.md) (the wild-solution singular-set statements, outside the regularity discipline).
- Sibling notes: [`caffarelli_kohn_nirenberg_1982.md`](caffarelli_kohn_nirenberg_1982.md) (the original theorem), [`escauriaza_seregin_sverak_2003.md`](escauriaza_seregin_sverak_2003.md) (the global $L^3$ critical criterion), [`leray_1934.md`](leray_1934.md) (the energy inequality these build on).
