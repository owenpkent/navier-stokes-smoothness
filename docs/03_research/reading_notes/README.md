# Reading notes

Notes on the key reference sources, each mapped to the project's findings and directions. The notes focus on structural content (what is actually proved, at the lemma level where it matters) and on how each source bears on the supercriticality gap. Every dossier places its result on the criticality scale (sub/critical/super under the Navier-Stokes scaling $u_\lambda(x,t)=\lambda\,u(\lambda x,\lambda^2 t)$) and against the three structural controls (2D must stay smooth, supercriticality is the ceiling, viscosity is essential).

The corpus now covers the load-bearing references across all five candidate architectures, the problem statement that frames them, and the textbook layer underneath. It grows as the SURVEYOR agent works through the library (see [`../../../references/README.md`](../../../references/README.md) for the full bibliographic index, and [`../../../references/reading_guide.md`](../../../references/reading_guide.md) for the curated entry path).

## Index, grouped by architecture

The five architectures are those of the project spine (see [`../../../CLAUDE.md`](../../../CLAUDE.md) and [`../../research_atlas/README.md`](../../research_atlas/README.md)). "Problem statement" and "Textbooks" bracket them. Every dossier `.md` currently in this folder appears below.

### Problem statement

| Source | Year | One-line role | Notes |
|---|---|---|---|
| Fefferman, official Clay problem statement | 2000 | the contract: fixes equation, data class, solution class, four targets | [notes](fefferman_problem_statement.md) |

### Architecture 1: energy methods and weak solutions

| Source | Year | One-line role | Notes |
|---|---|---|---|
| Leray | 1934 | global weak solutions exist; the energy inequality; the self-similar ansatz | [notes](leray_1934.md) |
| Hopf | 1951 | the same on bounded domains via Galerkin; names the Leray-Hopf class | [notes](hopf_1951.md) |
| Caffarelli-Kohn-Nirenberg | 1982 | sharpest unconditional partial regularity, $\mathcal{P}^1(S)=0$ | [notes](caffarelli_kohn_nirenberg_1982.md) |
| Lin; Vasseur | 1998; 2007 | streamlined CKN proofs (blow-up/compactness; De Giorgi) | [notes](lin_vasseur_partial_regularity.md) |

### Architecture 2: conditional regularity criteria

| Source | Year | One-line role | Notes |
|---|---|---|---|
| Prodi-Serrin-Ladyzhenskaya | 1959-1967 | the critical line $2/p+3/q\le 1$ forces smoothness ($q>3$) | [notes](prodi_serrin_ladyzhenskaya.md) |
| Beale-Kato-Majda | 1984 | breakdown iff $\int_0^T\|\omega\|_{L^\infty}\,dt=\infty$ | [notes](beale_kato_majda_1984.md) |
| Constantin-Fefferman | 1993 | geometric criterion: coherent vorticity direction prevents blow-up | [notes](constantin_fefferman_1993.md) |
| Escauriaza-Seregin-Sverak | 2003 | the $L^\infty_t L^3_x$ critical endpoint | [notes](escauriaza_seregin_sverak_2003.md) |
| Tao, quantitative ESS | 2019 | makes ESS effective: triple-log lower bound on $\|u\|_{L^3}$ at blow-up | [notes](tao_2019_quantitative.md) |

### Architecture 3: critical spaces and scaling

| Source | Year | One-line role | Notes |
|---|---|---|---|
| Fujita-Kato (and Kato 1984) | 1964 | small-data global existence in critical $\dot H^{1/2}$ (and $L^3$) | [notes](fujita_kato_1964.md) |
| Koch-Tataru | 2001 | small-data global existence in $\mathrm{BMO}^{-1}$, the largest critical space | [notes](koch_tataru_2001.md) |
| Bourgain-Pavlovic | 2008 | ill-posedness one notch larger, in $\dot B^{-1}_{\infty,\infty}$ (norm inflation) | [notes](bourgain_pavlovic_2008.md) |

### Architecture 4: blow-up and self-similar solutions

| Source | Year | One-line role | Notes |
|---|---|---|---|
| Necas-Ruzicka-Sverak (with Tsai 1998) | 1996 | rules out Leray self-similar blow-up in $L^3$ (viscous rigidity) | [notes](necas_ruzicka_sverak_1996.md) |
| Tao, averaged Navier-Stokes | 2016 | the central barrier: energy-plus-scaling alone cannot close regularity | [notes](tao_2016_averaged.md) |
| Elgindi (with Ghoul-Masmoudi) | 2021 | rigorous finite-time singularity for $C^{1,\alpha}$ 3D Euler | [notes](elgindi_2021.md) |
| Luo-Hou; Chen-Hou | 2014; 2022-2025 | boundary-driven axisymmetric Euler singularity, numerics then computer-assisted proof | [notes](luo_hou_2014.md) |

### Architecture 5: non-uniqueness via convex integration

| Source | Year | One-line role | Notes |
|---|---|---|---|
| Isett (with BDSV) | 2018 | proves Onsager's conjecture for Euler: the inviscid template and $1/3$ threshold | [notes](isett_2018.md) |
| Buckmaster-Vicol | 2019 | non-uniqueness of finite-energy weak solutions below Leray-Hopf | [notes](buckmaster_vicol_2019.md) |
| Albritton-Brue-Colombo | 2022 | non-uniqueness inside the Leray-Hopf class, for forced NS | [notes](albritton_brue_colombo_2022.md) |

### Textbooks and background

| Source | Year | One-line role | Notes |
|---|---|---|---|
| Lemarie-Rieusset, *The Navier-Stokes Problem in the 21st Century* | 2016; 2024 | proof-complete encyclopedic backbone for Architectures 1-4 | [notes](lemarie_rieusset_book.md) |
| Annotated map of the eight standard graduate references | various | one-lookup routing across Constantin-Foias, Temam, Doering-Gibbon, Majda-Bertozzi, Bahouri-Chemin-Danchin, Robinson-Rodrigo-Sadowski, Galdi, Sohr | [notes](textbooks_map.md) |

## Criticality placement

For each landmark source, the key norm or space, its classification under the scaling, what the result gives toward regularity, and what it does not. The exponent convention is the project bookkeeper's (`experiments/_shared/criticality.py`): a purely spatial norm $\|u\|_{L^q}$ has exponent $a=1-d/q$ in dimension $d=3$, with $a>0$ subcritical, $a=0$ critical, $a<0$ supercritical.

| Source | Key norm / space | Exponent / class | Gives | Does NOT give |
|---|---|---|---|---|
| Fefferman 2000 | $\|u\|_{L^2}$ (bounded-energy clause) | $a=-1/2$, supercritical | a precise gradeable target; "smooth = no blow-up" | the change of currency from the supercritical bound granted to the critical bound required |
| Leray 1934 | $L^\infty_t L^2_x \cap L^2_t\dot H^1_x$ (energy) | $a=-1/2$, supercritical | global weak solutions for all data; singular times of dimension $\le 1/2$; eventual regularity | uniqueness, regularity, energy equality, or any critical-scale control |
| Hopf 1951 | same energy norms, bounded domain | $a=-1/2$, supercritical | weak existence on walled domains with no-slip; the Leray-Hopf class | the same gap: no uniqueness, no regularity, no critical control |
| CKN 1982 | scale-invariant local energy on $Q_r$ | critical ($\varepsilon$-regularity) over a supercritical budget | $\mathcal{P}^1(S)=0$: no singular spacetime curve; the best unconditional result | $S=\varnothing$; the gap from "small singular set" to "empty" is the supercriticality gap |
| Lin 1998 / Vasseur 2007 | same $\varepsilon$-regularity quantity ($r^{-2}\int_{Q_r}|u|^3$) | critical | shorter, modular CKN proofs (compactness; De Giorgi); clearer where criticality lives | nothing beyond CKN; structurally cannot close regularity |
| Prodi-Serrin-Ladyzhenskaya | $\|u\|_{L^p_t L^q_x}$, $2/p+3/q\le 1$ | critical on the line, $q>3$ | smoothness and weak-strong uniqueness if the critical norm is finite | the endpoint $q=3$ (left to ESS); the norm is not known finite for general data |
| BKM 1984 | $\int_0^T\|\omega\|_{L^\infty}\,dt$ | scale invariant, critical | exact breakdown criterion: this integral diverging is the only obstruction | a way to bound the integral; energy controls only $L^2_t L^2_x$ vorticity |
| Constantin-Fefferman 1993 | $\sin\theta(x,y)=|\xi(x)\times\xi(y)|$, vorticity direction | dimensionless, scale aware (critical) | a genuinely 3D geometric criterion: coherent direction tames stretching | an a priori reason the direction stays coherent for general data |
| ESS 2003 | $\|u\|_{L^\infty_t L^3_x}$ | $a=0$, critical | the sharpest continuation criterion; new parabolic backward-uniqueness machinery | a rate (supplied later by Tao 2019); a way to bound $L^3$ for general data |
| Tao 2019 | $\|u\|_{L^3}$ at first singularity | critical, quantitative | triple-log lower blow-up rate; effective higher-norm bounds in $A$ | a bound that prevents blow-up; the constants grow, so no self-improvement |
| Fujita-Kato 1964 | $\|u_0\|_{\dot H^{1/2}}$ (and $L^3$, Kato 1984) | $a=0$, critical | global smoothness for small critical data; the mild-solution machine | anything for large data; smallness is essential |
| Koch-Tataru 2001 | $\|u_0\|_{\mathrm{BMO}^{-1}}$ | $a=0$, critical (largest such space) | small-data global well-posedness at the top of the critical ladder | large-data control; the method stops at small data |
| Bourgain-Pavlovic 2008 | $\dot B^{-1}_{\infty,\infty}$ | $a=0$, critical (roughest) | the frontier: ill-posedness (norm inflation) just beyond $\mathrm{BMO}^{-1}$ | well-posedness; a critical norm bound alone is not a recipe, the space matters |
| Necas-Ruzicka-Sverak 1996 | Leray profile $U\in L^3$ | critical class of the ansatz | exclusion of Leray backward self-similar blow-up; uses viscosity essentially | exclusion outside $L^3$; no use of 3D stretching; does not touch the gap |
| Tao 2016 | averaged $\tilde B$ with energy identity + scaling | preserves criticality of energy method | a finite-time blow-up that obeys energy and scaling: the barrier | a counterexample to NS; it constrains methods, not the equation |
| Elgindi 2021 | $C^{1,\alpha}$ velocity; $\|\omega\|_{L^\infty}\sim(T_*-t)^{-1}$ | regularity-borderline (inviscid), not Lebesgue-critical | rigorous 3D Euler singularity by vortex stretching; energy conserved through it | nothing about NS; needs $\alpha$ small; no $C^\infty$ Euler blow-up; no NS bound |
| Luo-Hou / Chen-Hou 2014-2025 | $\|\omega\|_{L^\infty}\sim(T_*-t)^{-1}$, Type I | inviscid; supercritical vorticity escaping | boundary-driven Euler singularity, numerics then computer-assisted proof | NS blow-up; the viscous version is open; no coercive NS bound |
| Isett 2018 | $C^\beta_x$ Euler, $\beta<1/3$ | inviscid energy-flux threshold at $\beta=1/3$ | sharp Onsager threshold; explicit anomalous-dissipation weak solutions | nothing about NS smoothness; flexibility, not rigidity; below every coercive norm |
| Buckmaster-Vicol 2019 | $C_t H^\beta_x$, $\beta>0$ small | below critical / supercritical regularity | non-uniqueness of finite-energy weak solutions below Leray-Hopf | non-uniqueness inside Leray-Hopf (unforced); no singularity of a smooth flow |
| Albritton-Brue-Colombo 2022 | forward self-similar profile, $(-1)$-homogeneous data | critical scaling; energy supercritical | two distinct Leray-Hopf solutions, same data and force (spectral instability) | the unforced case; the force is essential and sits outside the Clay statement |

The single recurring reading: every unconditional all-time bound the theory produces sits at $a=-1/2$ (supercritical), while every norm whose finiteness would force smoothness sits at $a=0$ (critical). The whole problem is the change of currency from the bound we have to the bound we need.

## How the sources line up with the spine

- **Fefferman fixes the target.** The 2000 note is the contract: it pins the equation ($\nu>0$, the exact nonlinearity), the data class (Schwartz, divergence-free), the solution class ($C^\infty$ with bounded energy), and the four gradeable verdicts. Its own definition of "no blow-up" is phrased through the supercritical energy quantity, so the supercriticality gap is built into the problem statement.

- **Leray, Hopf, CKN, and Lin-Vasseur are the unconditional results, and all stop exactly where supercriticality stops them.** Leray and Hopf produce global weak solutions for arbitrary finite-energy data, but the only all-time a priori bound they get is the energy, which is supercritical ($a=-1/2$). CKN pushes this to its frontier: the $\varepsilon$-regularity theorem is a critical-scaling statement run on the supercritical energy budget, and it proves the singular set is small ($\mathcal{P}^1(S)=0$) but cannot prove it empty. Lin (blow-up/compactness) and Vasseur (De Giorgi) re-derive CKN more transparently and make the same boundary visible: a critical local mechanism over a supercritical global budget leaves a dimension-$1$ residue. The gap from "small singular set" to "no singular set" is the geometric image of the supercriticality gap.

- **The conditional criteria are sharp but unreachable from energy.** Prodi-Serrin-Ladyzhenskaya identify the exact critical line $2/p+3/q=1$ where a norm bound forces smoothness; BKM isolates the scale-invariant vorticity integral $\int_0^T\|\omega\|_{L^\infty}\,dt$; Constantin-Fefferman adds the genuinely 3D geometric (vortex-direction) criterion; ESS closes the endpoint $L^\infty_t L^3_x$ with new parabolic backward-uniqueness machinery; Tao 2019 makes ESS quantitative (a triple-log blow-up rate). Each says "if this critical quantity stays finite, the solution is smooth," and each is sharp. None of these critical quantities is known to stay finite for general data, because the only unconditional all-time bound (energy) is supercritical and does not control them. The conditional results restate the regularity problem in critical coordinates; they do not cross the gap.

- **The critical-space results are small-data only, and they pin the critical frontier.** Fujita-Kato solve the problem at the critical scaling level ($\dot H^{1/2}$, and $L^3$ via Kato 1984), and Koch-Tataru push to the largest critical space $\mathrm{BMO}^{-1}$. This is the positive half of the supercriticality story: at criticality you can close regularity, but only for small data. Bourgain-Pavlovic mark the outer edge, ill-posedness (norm inflation) in $\dot B^{-1}_{\infty,\infty}$, which shows a critical norm bound is not by itself a recipe: the space has to support a continuous flow. The chain $\dot H^{1/2}\hookrightarrow L^3\hookrightarrow\mathrm{BMO}^{-1}\hookrightarrow\dot B^{-1}_{\infty,\infty}$ is the critical frontier, well-posed up to $\mathrm{BMO}^{-1}$ and ill-posed beyond. Large data stays blocked by the same supercriticality of the energy that blocks everything else.

- **The blow-up and Euler results show the mechanism is real, so viscosity must beat it.** Necas-Ruzicka-Sverak (with Tsai) kill Leray's specific backward self-similar singularity in $L^3$ by a Liouville rigidity argument that uses the viscous term essentially, ruling out the simplest scenario while showing precisely why Navier-Stokes differs from inviscid Burgers and Euler. Elgindi (2021) then proves, rigorously and at $C^{1,\alpha}$, that inviscid 3D Euler genuinely blows up by vortex stretching, with energy conserved through the collapse. Luo-Hou (2014, numerics) and Chen-Hou (2022-2025, computer-assisted proof) establish the boundary-driven axisymmetric Euler singularity for smooth data. Together these say the stretching engine is real: any Navier-Stokes regularity proof must come from $\nu\Delta u$ beating $\omega\cdot\nabla u$, not from any soft feature shared with Euler.

- **Tao 2016 is the central barrier.** The averaged Navier-Stokes obeys the same energy identity and the same scaling and yet blows up in finite time. This removes, at one stroke, the entire class of arguments that use only energy plus scaling, and it is the basis for the bookkeeper's `INSUFFICIENT_BY_ITSELF` verdict on supercritical estimates. It is a compass, not a counterexample: any regularity proof must use a feature of the exact NS nonlinearity that the averaging destroys.

- **Convex integration delimits the solution class.** Isett (2018) proves the flexible half of Onsager's conjecture for Euler, supplying the inviscid template (Mikado flows, the geometric lemma) and the $1/3$ flux threshold that mirrors the supercriticality gap. Buckmaster-Vicol (2019) carry the machinery to viscous NS with intermittent building blocks, proving non-uniqueness of finite-energy weak solutions below the Leray-Hopf class. Albritton-Brue-Colombo (2022) reach inside the Leray-Hopf class, but only for forced NS and via a spectral (self-similar instability) mechanism rather than convex integration. These objects are not $C^\infty$ (or the force sits outside the Clay statement), so they are not solutions in Fefferman's sense; they sharpen what "solution" can mean and pin the floor (the Leray-Hopf class) below which uniqueness fails, rather than answering the regularity question.

- **The textbooks are the proof-complete substrate.** Lemarie-Rieusset is the encyclopedic backbone for Architectures 1-4 (weak solutions, partial regularity, the conditional criteria, and the full critical-space ladder with bilinear-estimate proofs), and the annotated map routes any specific need to the right one of the eight standard graduate references. Read across them, four independent functional-analytic traditions close the 2D theory and stall in 3D at the same boundary: the only global a priori bound is the supercritical energy.

## Suggested reading order

1. **Fefferman 2000** ([notes](fefferman_problem_statement.md)): the target, the data class, the four verdicts, and why the bounded-energy clause is supercritical. Read this first; everything is graded against it.
2. **Leray 1934** ([notes](leray_1934.md)) then **Hopf 1951** ([notes](hopf_1951.md)): the existence theory and the energy inequality, where the supercriticality enters the story.
3. **Prodi-Serrin-Ladyzhenskaya** ([notes](prodi_serrin_ladyzhenskaya.md)) then **ESS 2003** ([notes](escauriaza_seregin_sverak_2003.md)) and **BKM 1984** ([notes](beale_kato_majda_1984.md)): the conditional criteria that restate regularity at the critical level.
4. **Fujita-Kato 1964** ([notes](fujita_kato_1964.md)) then **Koch-Tataru 2001** ([notes](koch_tataru_2001.md)) and **Bourgain-Pavlovic 2008** ([notes](bourgain_pavlovic_2008.md)): the critical-space small-data theory and its outer edge.
5. **CKN 1982** ([notes](caffarelli_kohn_nirenberg_1982.md)) with **Lin-Vasseur** ([notes](lin_vasseur_partial_regularity.md)): the best unconditional partial regularity and its modern proofs.
6. **Tao 2016** ([notes](tao_2016_averaged.md)): the barrier. Read this once the energy method's reach is clear; it explains why energy plus scaling cannot suffice.
7. Specialist branches, as needed: **Constantin-Fefferman 1993** ([notes](constantin_fefferman_1993.md)) and **Tao 2019** ([notes](tao_2019_quantitative.md)) for the vorticity-geometry and quantitative-ESS directions; **Necas-Ruzicka-Sverak 1996** ([notes](necas_ruzicka_sverak_1996.md)), **Elgindi 2021** ([notes](elgindi_2021.md)), and **Luo-Hou / Chen-Hou** ([notes](luo_hou_2014.md)) for self-similar exclusion and the inviscid blow-up that viscosity must beat; **Isett 2018** ([notes](isett_2018.md)), **Buckmaster-Vicol 2019** ([notes](buckmaster_vicol_2019.md)), and **Albritton-Brue-Colombo 2022** ([notes](albritton_brue_colombo_2022.md)) for the convex-integration / non-uniqueness boundary.
8. Textbook backbone, for proofs and routing: **Lemarie-Rieusset** ([notes](lemarie_rieusset_book.md)) and the **annotated map of standard references** ([notes](textbooks_map.md)).

For a curated entry path through the broader bibliography, see [`../../../references/reading_guide.md`](../../../references/reading_guide.md).
