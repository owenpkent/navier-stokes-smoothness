# Reading notes: Lemarie-Rieusset, "The Navier-Stokes Problem in the 21st Century" (2016; 2nd ed. 2024)

Pierre Gilles Lemarie-Rieusset, *The Navier-Stokes Problem in the 21st Century*, CRC Press / Chapman and Hall (1st ed. 2016, ISBN 978-1-4665-6621-7; 2nd ed. 2024, ISBN 978-0-367-48726-3). The 2016 book is itself the successor to the author's earlier *Recent Developments in the Navier-Stokes Problem*, Chapman and Hall/CRC Research Notes in Mathematics **431** (2002).

> This is not a single result; it is the project's primary textbook backbone for Architectures 1 through 4. It is the modern encyclopedic treatment of the *mathematical* Navier-Stokes problem (mild solutions, the Leray projector and the pressure, critical spaces up to $\mathrm{BMO}^{-1}$, Leray-Hopf weak solutions, partial regularity, self-similar solutions, and the conditional criteria including ESS). It is load-bearing because it gives full, harmonic-analysis-correct proofs of almost everything the project's other reading notes summarize, with the function-space technology (Littlewood-Paley, Besov, Morrey, Lorentz, multiplier theorems) developed in place. It engages all three structural controls but is the *definitive* reference for two: critical-space well-posedness (Control B, the supercriticality ceiling and what sits exactly at the critical level) and weak-solution / partial-regularity theory (Architecture 1). It covers Architecture 5 (convex-integration non-uniqueness) only lightly and as a frontier remark, and it is not a numerics or turbulence-physics book. This note is a *map of the book*: which part to open for each architecture, what it is authoritative on, and where to go elsewhere.

This note is the textbook anchor for the single-source notes: [Leray (1934)](leray_1934.md) and [Hopf (1951)](hopf_1951.md) (Architecture 1), [Fujita-Kato (1964)](fujita_kato_1964.md) and [Koch-Tataru (2001)](koch_tataru_2001.md) (Architecture 3), [Prodi-Serrin-Ladyzhenskaya](prodi_serrin_ladyzhenskaya.md) and [Escauriaza-Seregin-Sverak (2003)](escauriaza_seregin_sverak_2003.md) (Architecture 2), [Caffarelli-Kohn-Nirenberg (1982)](caffarelli_kohn_nirenberg_1982.md) (partial regularity), and [Necas-Ruzicka-Sverak (1996)](necas_ruzicka_sverak_1996.md) (self-similar). Lemarie-Rieusset gives the proof-complete version of each.

---

## What it is / scope

The book is a self-contained development of the rigorous analysis of the incompressible Navier-Stokes system on $\mathbb{R}^3$ (and $\mathbb{R}^d$, with the torus $\mathbb{T}^3$ treated where it differs),
$$\partial_t u + (u\cdot\nabla)u = \Delta u - \nabla p, \qquad \nabla\cdot u = 0, \qquad u(\cdot,0)=u_0,$$
with viscosity normalized to $\nu=1$. The viewpoint is harmonic-analytic: the equation is reduced, via the Leray projector $\mathbb{P}=I-\nabla\Delta^{-1}\nabla\cdot$, to the divergence-form integral (mild) equation
$$u(t)=e^{t\Delta}u_0 - \int_0^t e^{(t-s)\Delta}\,\mathbb{P}\,\nabla\cdot\big(u(s)\otimes u(s)\big)\,ds =: e^{t\Delta}u_0 + B(u,u)(t),$$
and the bulk of the well-posedness theory is the study of the bilinear operator $B$ on scale-invariant function spaces.

The first edition runs roughly 20 chapters and about 700 pages; the second edition (2024) is enlarged to roughly 700+ pages and adds chapters on developments after 2016, notably the convex-integration non-uniqueness results and the quantitative-regularity program. The precise chapter numbering differs between the two editions, so the chapter pointers below name the *topic* and give the edition-stable part it lives in, rather than betting on a single chapter number. (verify: exact chapter numbers per edition.)

What the book is built around, in order:

1. The classical setting: the heat kernel, the Oseen kernel, the Leray projector, the pressure, and the meaning of "solution" (weak, mild, suitable). Function-space prerequisites (Lebesgue, Sobolev, Lorentz, Morrey, Besov, $\mathrm{BMO}$) are developed as needed.
2. Mild solutions and critical-space well-posedness: Kato's $L^3$ theory, Fujita-Kato $\dot H^{1/2}$, Cannone-Meyer-Planchon Besov spaces, and Koch-Tataru $\mathrm{BMO}^{-1}$, all via the same bilinear-estimate template.
3. Leray-Hopf weak solutions: existence, the energy inequality, weak-strong uniqueness, and the structure of the proof (Galerkin / mollification / compactness).
4. Partial regularity: suitable weak solutions, the local energy inequality, $\varepsilon$-regularity, and the Caffarelli-Kohn-Nirenberg theorem with a full modern proof.
5. The conditional criteria: Prodi-Serrin-Ladyzhenskaya, the ESS $L^3$ endpoint (backward uniqueness and Carleman estimates), and the vorticity / geometric criteria.
6. Self-similar solutions, forward and backward, and the Necas-Ruzicka-Sverak exclusion; large-data and special-structure global results (axisymmetric, helical).
7. (2nd ed.) Frontier remarks: convex-integration non-uniqueness, the quantitative-regularity / concentration program.

---

## What it proves / the load-bearing statements (with edition-stable pointers)

The book is authoritative because it gives the *proofs*, with constants and exact hypotheses, in one notation. The key theorems, each tagged with its architecture and where to read it.

### Architecture 1: weak solutions and partial regularity

**Leray-Hopf existence.** For $u_0\in L^2(\mathbb{R}^3)$ divergence-free, there exists a global weak solution $u\in L^\infty(0,\infty;L^2)\cap L^2(0,\infty;\dot H^1)$ satisfying the energy inequality
$$\tfrac12\|u(t)\|_{L^2}^2 + \int_0^t\|\nabla u(s)\|_{L^2}^2\,ds \;\le\; \tfrac12\|u_0\|_{L^2}^2.$$
The book gives this via mollified/Galerkin approximation and weak compactness, with care about the pressure recovered from $-\Delta p = \nabla\cdot\nabla\cdot(u\otimes u)$ (the Leray projector made explicit). Read: the weak-solution part (early-middle of the book). See [Leray (1934)](leray_1934.md), [Hopf (1951)](hopf_1951.md).

**Weak-strong uniqueness.** If a Leray-Hopf solution coincides at $t=0$ with a solution in a Prodi-Serrin class ($u\in L^p_tL^q_x$, $2/p+3/q\le1$, $q>3$), the two agree as long as the strong one exists. Proved by the relative-energy / Gronwall method.

**Caffarelli-Kohn-Nirenberg partial regularity.** For a *suitable* weak solution (one satisfying the local energy inequality with the pressure), the singular set $S$ has one-dimensional parabolic Hausdorff measure zero, $\mathcal{P}^1(S)=0$. The engine is the $\varepsilon$-regularity lemma: there is an absolute $\varepsilon_0>0$ such that if the scale-invariant local quantity
$$\frac{1}{r^2}\int_{Q_r(z_0)}\big(|u|^3+|p|^{3/2}\big)\,dx\,dt \;<\; \varepsilon_0$$
on a parabolic cylinder $Q_r(z_0)=B_r(x_0)\times(t_0-r^2,t_0)$, then $u$ is Holder continuous near $z_0$. The book gives the modern compactness proof (in the lineage of [Lin-Vasseur](lin_vasseur_partial_regularity.md)). Read: the partial-regularity part. See [Caffarelli-Kohn-Nirenberg (1982)](caffarelli_kohn_nirenberg_1982.md).

### Architecture 2: conditional regularity criteria

**Prodi-Serrin-Ladyzhenskaya.** A Leray-Hopf solution with $u\in L^p_tL^q_x$, $2/p+3/q\le1$, $3<q\le\infty$, is smooth on the interior. The endpoint $q=3,p=\infty$ is *not* covered by the elementary proof and is treated separately. See [Prodi-Serrin-Ladyzhenskaya](prodi_serrin_ladyzhenskaya.md).

**Escauriaza-Seregin-Sverak endpoint.** If $u\in L^\infty(0,T;L^3(\mathbb{R}^3))$ then $u$ is smooth on $(0,T]$; equivalently the critical $L^3$ norm must become unbounded at a first singular time. The book presents the backward-uniqueness-for-the-heat-operator and unique-continuation (Carleman-estimate) machinery in detail, the part of the theory most other textbooks omit. Read: the critical-criteria / ESS part. See [Escauriaza-Seregin-Sverak (2003)](escauriaza_seregin_sverak_2003.md).

**Vorticity and geometric criteria.** Beale-Kato-Majda ($\int_0^T\|\omega(t)\|_{L^\infty}\,dt<\infty$ continues smoothness) and the Constantin-Fefferman vorticity-direction criterion (Lipschitz alignment of $\omega/|\omega|$ in high-vorticity regions forces regularity) are stated and connected to the velocity criteria. See [Beale-Kato-Majda (1984)](beale_kato_majda_1984.md), [Constantin-Fefferman (1993)](constantin_fefferman_1993.md).

### Architecture 3: critical spaces and scaling

This is the book's signature strength. The critical-space ladder is developed with its inclusions proved:
$$\dot H^{1/2}(\mathbb{R}^3)\hookrightarrow L^3(\mathbb{R}^3)\hookrightarrow \dot B^{-1+3/q}_{q,\infty}(\mathbb{R}^3)\ (3<q<\infty)\hookrightarrow \mathrm{BMO}^{-1}(\mathbb{R}^3)\hookrightarrow \dot B^{-1}_{\infty,\infty}(\mathbb{R}^3).$$

- **Kato (1984), $L^3$ mild solutions.** Local well-posedness and small-data global existence by Picard iteration on $B$ using the smoothing estimate $\|e^{t\Delta}\mathbb{P}\nabla\cdot F\|_{L^q}\lesssim t^{-1/2-\cdots}\|F\|$.
- **Fujita-Kato (1964), $\dot H^{1/2}$.** The critical Sobolev space. See [Fujita-Kato (1964)](fujita_kato_1964.md).
- **Cannone-Meyer-Planchon Besov spaces $\dot B^{-1+3/q}_{q,\infty}$**, including the construction of forward self-similar solutions from $(-1)$-homogeneous data.
- **Koch-Tataru (2001), $\mathrm{BMO}^{-1}$.** The largest space with small-data global well-posedness, with the Carleson-measure norm and the bilinear estimate proved in full. The book is the standard textbook reference for this proof. See [Koch-Tataru (2001)](koch_tataru_2001.md).
- **Ill-posedness boundary.** The failure in $\dot B^{-1}_{\infty,\infty}$ (Bourgain-Pavlovic norm inflation) is discussed as the sharp outer edge. See [Bourgain-Pavlovic (2008)](bourgain_pavlovic_2008.md).

Read: the mild-solution and critical-space part (the central third of the book).

### Architecture 4: self-similar solutions and special-structure global results

- **Backward self-similar exclusion.** Leray's backward self-similar blow-up profiles are ruled out in $L^3$ (Necas-Ruzicka-Sverak) and under local energy bounds (Tsai). See [Necas-Ruzicka-Sverak (1996)](necas_ruzicka_sverak_1996.md).
- **Forward self-similar existence.** Global forward self-similar solutions from rough $(-1)$-homogeneous critical data (Cannone-Planchon; later Jia-Sverak), the scenario underlying proposed self-similar non-uniqueness.
- **Conditional / special-structure global results.** Axisymmetric-without-swirl global regularity, helical flows, and large-data results under structural restrictions are catalogued.

Read: the self-similar and special-solutions part (later chapters).

### Architecture 5: convex-integration non-uniqueness (light coverage)

The 2nd edition (2024) adds frontier discussion of the Buckmaster-Vicol non-uniqueness of weak solutions below the Leray-Hopf class, and the Albritton-Brue-Colombo non-uniqueness of Leray solutions for forced NS. This is *survey-level*, not a full development of the intermittent-convex-integration machinery; for that, go to the dedicated sources. The book's role here is to place these results relative to the energy class, which is exactly the project's framing: convex integration lives *below* the energy bound and concerns the boundary of "solution," not regularity of the smooth flow.

---

## Method / structure: the unifying mechanisms the book makes explicit

The book's pedagogical value is that it shows the same few mechanisms recurring, which is precisely the structure this project tracks.

1. **The Leray projector and the pressure as a derived field.** $\mathbb{P}=I-\nabla\Delta^{-1}\nabla\cdot$ is a matrix of Calderon-Zygmund operators of order $0$. The pressure is *not* an independent unknown: it is recovered from $-\Delta p=\partial_i\partial_j(u_iu_j)$, so $p=\Delta^{-1}\partial_i\partial_j(u_iu_j)$, a non-local quadratic function of $u$. The book is unusually careful about the function-space subtleties of this recovery (the pressure can be only locally defined, can have low integrability, and is the reason "suitable" weak solutions need the local energy inequality with $p$ in it). This non-locality is also why the projector matters in every bilinear estimate: it both removes the gradient part and is the reason the nonlinearity is genuinely non-local.

2. **The bilinear operator on scale-invariant spaces.** All of the critical-space well-posedness reduces to: prove $\|B(u,v)\|_X\lesssim\|u\|_X\|v\|_X$ on a scale-invariant space $X$, then run the quadratic fixed-point lemma (if $\|y\|\le\delta$ and $\|B\|\le C\|\cdot\|^2$, then $u=y+B(u,u)$ has a unique small solution for $4C\delta<1$). The differences among $\dot H^{1/2}$, $L^3$, Besov, and $\mathrm{BMO}^{-1}$ are differences in the function-space estimate for the *same* $B$. This is the cleanest possible statement of why these are all "the same theorem at the critical level, ordered by the size of the space."

3. **The energy identity and its supercriticality.** The only coercive global-in-time bound is the energy inequality above. The book is explicit that this controls $L^\infty_tL^2_x\cap L^2_t\dot H^1_x$, which does *not* embed into any critical space on $\mathbb{R}^3$, and therefore cannot feed the critical-space machinery for large data. This is the supercriticality gap stated cleanly.

4. **$\varepsilon$-regularity via the local energy inequality.** Partial regularity is a local-in-space-time bootstrap: smallness of a scale-invariant local quantity implies Holder continuity, and a covering/dimension argument bounds the singular set. The pressure enters through the local energy inequality, which is why CKN needs *suitable* weak solutions, not just Leray-Hopf ones.

5. **Backward uniqueness and Carleman estimates (the ESS engine).** For the critical $L^3$ endpoint the mechanism is non-perturbative: blow-up-rescale a hypothetical singularity to an ancient bounded solution, reduce the vorticity to a heat differential inequality $|(\partial_s-\Delta)\omega|\le c(|\omega|+|\nabla\omega|)$, then kill it with backward uniqueness and unique continuation for the heat operator (weighted $L^2$ Carleman inequalities). The book develops the Carleman machinery itself, which is the part that distinguishes it from lighter texts.

---

## Criticality placement

The book *is* the criticality bookkeeper in prose form. Under the scaling $u_\lambda(x,t)=\lambda\,u(\lambda x,\lambda^2 t)$, $p_\lambda(x,t)=\lambda^2 p(\lambda x,\lambda^2 t)$, the data rescaling is $u_0\mapsto\lambda\,u_0(\lambda\cdot)$, and the spaces sort as follows. Each placement matches `experiments/_shared/criticality.py` (`standard_norms_3d()`); run the table to confirm.

- **Critical (scaling exponent $0$):** $\dot H^{1/2}(\mathbb{R}^3)$, $L^3(\mathbb{R}^3)$, the Besov family $\dot B^{-1+3/q}_{q,\infty}$, $\mathrm{BMO}^{-1}$, and $\dot B^{-1}_{\infty,\infty}$. These are exactly the spaces in which the book's well-posedness (or ill-posedness, at the top) is stated. The entire critical-space chapter lives at exponent $0$.
- **Supercritical (negative exponent):** the energy $\|u\|_{L^2}^2$ scales as $\lambda^{-1}$, so $L^\infty_tL^2_x$ is supercritical. The book's repeated point is that this is the only global bound, hence Control (B).
- **Subcritical (positive exponent):** $L^p_tL^q_x$ with $2/p+3/q<1$ (the strict Prodi-Serrin interior) and higher Sobolev norms $\dot H^s$, $s>1/2$. The conditional criteria with strict inequality buy a margin of subcriticality, which the perturbative bootstrap can spend; the endpoint $2/p+3/q=1$ has no margin, which is why the $L^\infty_tL^3_x$ endpoint needed the non-perturbative ESS machine.

The book's organizing thesis (and the project's): **regularity is a critical-scaling statement.** The well-posedness theory reaches the critical level for small data and stops there; the only large-data a priori bound is one level too low (supercritical). The gap between them is the open problem, and it is a gap *in scaling*, not a gap that more function-space technology can close. See [`../research_directions/03_supercriticality_gap.md`](../research_directions/03_supercriticality_gap.md).

---

## Against the three controls

- **(A) 2D control: the book respects it and explains it.** Lemarie-Rieusset treats $\mathbb{R}^d$, and the 2D case appears as the dimension where the energy method *does* close, because the enstrophy $\int|\omega|^2$ is controlled (the vorticity equation $\partial_t\omega+u\cdot\nabla\omega=\Delta\omega$ is scalar, no stretching term $\omega\cdot\nabla u$). The book's critical-space machinery is dimension-agnostic and, being small-data, makes no false large-data prediction in 2D, so it passes (A) the same way [Koch-Tataru](koch_tataru_2001.md) does: vacuously / orthogonally. The book is useful for (A) precisely because it lets the reader see *which* estimates are dimension-blind (the perturbative bilinear ones, which therefore cannot be the large-data 3D mechanism) and which genuinely use 3D structure (the vortex-stretching term in the ESS reduction, the geometric criteria). A BUILDER should use the book to audit any candidate estimate against this: if the book's version of your estimate runs identically in 2D, it is not engaging 3D structure.
- **(B) Supercriticality ceiling: the book is the canonical statement of it.** The repeated structural observation, that the energy controls only $L^\infty_tL^2_x\cap L^2_t\dot H^1_x$, which is supercritical and does not embed into any critical space, is exactly Control (B). The book also exhibits what a response to (B) looks like: ESS adds Carleman/backward-uniqueness input that is orthogonal to the energy and lives at the critical scale. Verdict from `audit_estimate` on the book's central object: any energy-level a priori bound is `SUPERCRITICAL`; any critical norm is `AT_THE_MARGIN` (bounding it for large data would close regularity, but no such all-time bound is known).
- **(C) Viscosity control: the book is viscous throughout and makes the dependence visible.** Every estimate is built on the heat semigroup $e^{t\Delta}$ and its smoothing; the Koch-Tataru Carleson norm is a heat-extension object; the ESS Carleman machine is a theorem about $\partial_s-\Delta$. The whole apparatus degenerates at $\nu=0$. The book does not develop Euler blow-up (Elgindi, Chen-Hou), so for the *inviscid* side of Control (C) one goes elsewhere; but it is precisely because the book's methods are so visibly parabolic that it makes clear why there is no Euler analogue of ESS or Koch-Tataru. See [`../research_directions/04_blowup_and_barriers.md`](../research_directions/04_blowup_and_barriers.md).

**Architecture 5 relative to the discipline.** The convex-integration material (2nd ed.) sits partly *outside* the wrong-approach discipline, as the project's framing says: it constructs non-smooth, non-unique weak solutions *below* the Leray-Hopf energy class, so it is about the boundary of what "solution" means, not about regularity of the smooth flow. The book's light treatment is appropriate to its role as a critical-space-and-weak-solution reference; for the full machinery use the dedicated sources. See [`../research_directions/05_convex_integration_boundary.md`](../research_directions/05_convex_integration_boundary.md).

---

## What it gives / what it does not give

**Gives.**
- A single, notation-consistent, proof-complete reference for Architectures 1 through 4: weak solutions, partial regularity (CKN), the conditional criteria (PSL, ESS, BKM, vorticity-direction), and the entire critical-space ladder up to $\mathrm{BMO}^{-1}$ with the bilinear-estimate proofs.
- The function-space technology (Littlewood-Paley, Besov, Morrey, Lorentz, $\mathrm{BMO}$, multiplier and maximal-function theorems) developed in place, so the reader is not sent to a separate harmonic-analysis text for the tools. (For deeper Besov/Littlewood-Paley machinery the standard complement is Bahouri-Chemin-Danchin.)
- A careful treatment of the pressure and the Leray projector, including the low-regularity subtleties that most texts skip and that matter for "suitable" weak solutions.
- The Carleman / backward-uniqueness development behind ESS, rarely given in full elsewhere at textbook level.
- (2nd ed.) Up-to-date frontier orientation on non-uniqueness (Buckmaster-Vicol, Albritton-Brue-Colombo) and the quantitative-regularity program.

**Does not give (the gap to closing regularity, and coverage limits).**
- **No regularity proof.** It is honest that the large-data problem is open; it maps the state of the art, it does not resolve it. The supercriticality gap is described, not bridged.
- **Light on convex integration (Architecture 5).** The intermittent-convex-integration construction is surveyed, not built. Use [Buckmaster-Vicol (2019)](../../../references/README.md) and the Onsager/Euler templates for the machinery.
- **Not a numerics or turbulence-physics book.** No DNS, no spectral methods, no Kolmogorov-cascade derivations beyond what bears on the analysis. For the energy cascade and statistical theory go to Foias-Manley-Rosa-Temam; for the project's own numerics see `experiments/`.
- **Light on Euler blow-up.** The inviscid singularity program (Elgindi; Luo-Hou; Chen-Hou) is not its subject. For Control (C)'s inviscid side go to those sources and [`../research_directions/04_blowup_and_barriers.md`](../research_directions/04_blowup_and_barriers.md).
- **Edition drift.** Chapter and theorem numbers differ between the 2016 and 2024 editions; cite by topic and edition, and verify the exact number against the edition in hand.

---

## How to use it as the project's textbook backbone

A practical routing table for the agents. Open the book at the named part; cross-check the dedicated reading note for the structural placement.

| Need | Architecture | Open in Lemarie-Rieusset | Dedicated note |
|---|---|---|---|
| Weak-solution existence, energy inequality, pressure recovery | 1 | weak-solution part | [Leray](leray_1934.md), [Hopf](hopf_1951.md) |
| Partial regularity, $\varepsilon$-regularity, $\mathcal{P}^1(S)=0$ | 1 | partial-regularity part | [CKN](caffarelli_kohn_nirenberg_1982.md), [Lin-Vasseur](lin_vasseur_partial_regularity.md) |
| Mild solutions, $L^3$, $\dot H^{1/2}$, Besov, $\mathrm{BMO}^{-1}$, the bilinear estimate | 3 | critical-space part | [Fujita-Kato](fujita_kato_1964.md), [Koch-Tataru](koch_tataru_2001.md), [Bourgain-Pavlovic](bourgain_pavlovic_2008.md) |
| Prodi-Serrin-Ladyzhenskaya, the $q>3$ criteria | 2 | conditional-criteria part | [PSL](prodi_serrin_ladyzhenskaya.md) |
| ESS $L^3$ endpoint, backward uniqueness, Carleman | 2 | critical-endpoint part | [ESS](escauriaza_seregin_sverak_2003.md) |
| Vorticity / geometric criteria, BKM | 2 | vorticity-criteria part | [BKM](beale_kato_majda_1984.md), [Constantin-Fefferman](constantin_fefferman_1993.md) |
| Self-similar solutions (backward exclusion, forward existence) | 4 | self-similar part | [NRS](necas_ruzicka_sverak_1996.md) |
| Non-uniqueness below the energy class (survey only) | 5 | 2nd-ed. frontier remarks | references index, Architecture 5 |
| The supercriticality gap in prose | (B) | energy-inequality + critical-space parts | [`../research_directions/03_supercriticality_gap.md`](../research_directions/03_supercriticality_gap.md) |

Operationally: when a BUILDER proposes an estimate, look it up here first to get the sharp known hypotheses and constants and to check whether the proof is perturbative (dimension-blind, hence failing Control A as a large-data mechanism) or genuinely uses 3D / viscous / critical structure. When a VERIFIER needs the exact statement to formalize in Lean, this is the citation of record for Architectures 1 through 4. When a SYNTHESIZER needs to state what is and is not known at the critical level, this is the source whose scope *is* "what is known."

---

## Lineage and sharpest known form

**Builds on / supersedes.**
- The author's own *Recent Developments in the Navier-Stokes Problem* (Chapman and Hall/CRC, 2002), which the 2016 book extends and modernizes (Koch-Tataru, partial regularity, ESS treated in current form).
- The classical functional-analytic references it complements: Constantin-Foias (1988), Temam (1977/2001), Ladyzhenskaya (1969), Lions (1996). Lemarie-Rieusset is the harmonic-analytic counterpart to these PDE/functional-analytic texts.
- The harmonic-analysis toolbox of Stein, Fefferman-Stein ($\mathrm{BMO}$ and Carleson measures), and the Littlewood-Paley / Besov tradition (Bahouri-Chemin-Danchin is the companion reference for that machinery).

**Built on it / complements.**
- It is the de facto citation of record for the Koch-Tataru proof and for the modern critical-space ladder; later papers cite it for the function-space estimates rather than reproving them.
- Robinson-Rodrigo-Sadowski, *The Three-Dimensional Navier-Stokes Equations: Classical Theory* (Cambridge, 2016), is the cleaner self-contained entry to Architectures 1 and 2; Lemarie-Rieusset is the broader and more harmonic-analytic reference covering Architecture 3 in depth. Seregin's *Lecture Notes on Regularity Theory* (2014) is the focused complement for the partial-regularity and $L^3$-endpoint machinery.

**Sharpest known form as of 2025.**
- The 2nd edition (2024) is the current state of the textbook literature for Architectures 1 through 4, with frontier coverage of the post-2016 developments: Buckmaster-Vicol (2019) and Albritton-Brue-Colombo (2022) non-uniqueness (Architecture 5, surveyed), and the Tao (2019) / Barker-Prange (2021) quantitative-regularity and concentration program (Architecture 2/4, the live thread on the critical-continuation side). For the quantitative program in depth go to those papers and to the Prange survey; the book is the orientation, not the frontier-paper-level detail.
- For the inviscid Control (C) frontier (Elgindi 2021; Chen-Hou 2022/2025; Wang-Lai-Gomez-Serrano-Buckmaster 2023) the book is not the reference; those live in [`../research_directions/04_blowup_and_barriers.md`](../research_directions/04_blowup_and_barriers.md).

---

## References

- P. G. Lemarie-Rieusset, *The Navier-Stokes Problem in the 21st Century*, CRC Press / Chapman and Hall, 1st ed. (2016), ISBN 978-1-4665-6621-7; 2nd ed. (2024), ISBN 978-0-367-48726-3. [The source.]
- P. G. Lemarie-Rieusset, *Recent Developments in the Navier-Stokes Problem*, Chapman and Hall/CRC Research Notes in Mathematics **431** (2002). [The predecessor volume.]
- H. Koch, D. Tataru, "Well-posedness for the Navier-Stokes equations," Adv. Math. **157** (2001), 22-35. [The $\mathrm{BMO}^{-1}$ theorem the book develops in full.]
- L. Escauriaza, G. A. Seregin, V. Sverak, "$L_{3,\infty}$-solutions of the Navier-Stokes equations and backward uniqueness," Russian Math. Surveys **58**:2 (2003), 211-250. [The $L^3$ endpoint and Carleman machine.]
- L. Caffarelli, R. Kohn, L. Nirenberg, "Partial regularity of suitable weak solutions of the Navier-Stokes equations," Comm. Pure Appl. Math. **35** (1982), 771-831. [The partial-regularity theorem.]
- T. Kato, "Strong $L^p$-solutions of the Navier-Stokes equation in $\mathbb{R}^m$," Math. Z. **187** (1984), 471-480. [Critical $L^3$ mild solutions.]
- H. Fujita, T. Kato, "On the Navier-Stokes initial value problem I," Arch. Rational Mech. Anal. **16** (1964), 269-315. [Critical $\dot H^{1/2}$.]
- J. Bourgain, N. Pavlovic, "Ill-posedness of the Navier-Stokes equations in a critical space in 3D," J. Funct. Anal. **255** (2008), 2233-2247. [The boundary beyond $\mathrm{BMO}^{-1}$.]
- H. Bahouri, J.-Y. Chemin, R. Danchin, *Fourier Analysis and Nonlinear Partial Differential Equations*, Grundlehren **343**, Springer (2011). [The Besov / Littlewood-Paley companion.]
- J. C. Robinson, J. L. Rodrigo, W. Sadowski, *The Three-Dimensional Navier-Stokes Equations: Classical Theory*, Cambridge Studies in Advanced Mathematics **157** (2016). [The self-contained complement for Architectures 1 and 2.]
- G. Seregin, *Lecture Notes on Regularity Theory for the Navier-Stokes Equations*, World Scientific (2014). [Focused complement for partial regularity and the $L^3$ endpoint.]
- T. Buckmaster, V. Vicol, "Nonuniqueness of weak solutions to the Navier-Stokes equations," Ann. of Math. (2) **189** (2019), 101-144. [Architecture 5, surveyed in the 2nd ed.]
- Book review (orientation): C. Bardos / reviewers, on *The Navier-Stokes Problem in the 21st Century*, CRC Press, 2016, ISBN 978-1-4665-6621-7. (verify reviewer.)

---

## What this enables / what remains open

**Enables.**
- A single authoritative backbone the program can cite for Architectures 1 through 4, with exact hypotheses, constants, and proofs, so the other reading notes can stay structural and defer technical detail here.
- A perturbative-vs-structural audit tool: because the book gives the proofs, one can see at a glance whether a candidate estimate is dimension-blind (perturbative, hence not the large-data 3D mechanism, failing Control A as a closing argument) or genuinely engages 3D vortex stretching, viscosity, and the critical scale.
- The cleanest textbook statement of the supercriticality gap (Control B): the energy controls only the supercritical $L^\infty_tL^2_x\cap L^2_t\dot H^1_x$, which does not reach any critical space for large data.

**Remains open (handoff).**
- BUILDER: the book specifies the *target* (a large-data a priori bound on a critical norm such as $L^3$, $\dot H^{1/2}$, or $\mathrm{BMO}^{-1}$) without supplying it. Any proposed bound must add input beyond the energy and beyond perturbation, of the kind ESS exemplifies (Carleman/backward uniqueness) but applied to derive, not assume, the critical bound. See [`../research_directions/03_supercriticality_gap.md`](../research_directions/03_supercriticality_gap.md).
- ADVERSARY: use the book to check that any candidate estimate is not one whose proof runs identically in 2D (Control A) and is not blind to viscosity (Control C). The book's dimension-agnostic perturbative estimates are the explicit catalogue of what *cannot* be the closing mechanism.
- SYNTHESIZER: the book's scope is "what is known"; the program's job is the complement. The frontier threads it points to (quantitative regularity, concentration, non-uniqueness below the energy class) are tracked in [`../research_directions/01_critical_continuation_criteria.md`](../research_directions/01_critical_continuation_criteria.md) and [`../research_directions/05_convex_integration_boundary.md`](../research_directions/05_convex_integration_boundary.md).

**Cross-links.** Primary: [`../research_directions/03_supercriticality_gap.md`](../research_directions/03_supercriticality_gap.md) (the book is the canonical statement of the gap). Secondary: [`../research_directions/01_critical_continuation_criteria.md`](../research_directions/01_critical_continuation_criteria.md) (PSL/ESS and the quantitative thread), [`../research_directions/02_vorticity_geometry.md`](../research_directions/02_vorticity_geometry.md) (BKM and vorticity-direction criteria), [`../research_directions/04_blowup_and_barriers.md`](../research_directions/04_blowup_and_barriers.md) (self-similar exclusion; the Euler/inviscid side the book does not cover), [`../research_directions/05_convex_integration_boundary.md`](../research_directions/05_convex_integration_boundary.md) (Architecture 5, surveyed in the 2nd ed.). Sibling notes: every single-source note above; this book is their proof-complete textbook anchor.
