# Reference library

Index of the key references for the Navier-Stokes existence and smoothness problem. PDFs are gitignored (copyrighted); this tracked index records the bibliography, the role each source plays, and which research direction or finding it informs. Reading notes for the load-bearing sources are in [`../docs/03_research/reading_notes/`](../docs/03_research/reading_notes/).

## The problem statement

| Source | Role |
|---|---|
| C. Fefferman, "Existence and smoothness of the Navier-Stokes equation" (Clay Millennium Problem description, 2000) | The official problem statement. Defines the target (existence-and-smoothness on $\mathbb{R}^3$ or $\mathbb{T}^3$) and the four acceptable statements. |

## Foundational existence and partial regularity (Architecture 1)

| Source | Role |
|---|---|
| J. Leray, "Sur le mouvement d'un liquide visqueux emplissant l'espace," Acta Math. 63 (1934) | Global weak solutions exist; the energy inequality; the self-similar blow-up attempt. |
| E. Hopf, "Uber die Anfangswertaufgabe fur die hydrodynamischen Grundgleichungen," Math. Nachr. 4 (1951) | Leray-Hopf weak solutions on bounded domains. |
| L. Caffarelli, R. Kohn, L. Nirenberg, "Partial regularity of suitable weak solutions," Comm. Pure Appl. Math. 35 (1982) | The singular set has parabolic Hausdorff measure $\mathcal{P}^1 = 0$; the $\varepsilon$-regularity method. |

## Conditional regularity criteria (Architecture 2)

| Source | Role |
|---|---|
| G. Prodi (1959), J. Serrin (1962), O. Ladyzhenskaya | The $L^p_t L^q_x$, $2/p+3/q\le1$ criterion. |
| J. T. Beale, T. Kato, A. Majda, Comm. Math. Phys. 94 (1984) | The vorticity blow-up criterion $\int\|\omega\|_\infty\,dt$. |
| L. Escauriaza, G. Seregin, V. Sverak, Russian Math. Surveys 58 (2003) | The endpoint $L^\infty_t L^3_x$ criterion; backward uniqueness. |
| P. Constantin, C. Fefferman, Indiana Univ. Math. J. 42 (1993) | The vorticity-direction (geometric) regularity criterion. |
| T. Tao, "Quantitative bounds for critically bounded solutions," (2019) | Quantitative ESS: triple-log lower bound on $\|u\|_{L^3}$ growth at a singularity. |

## Critical spaces and scaling (Architecture 3)

| Source | Role |
|---|---|
| H. Fujita, T. Kato, Arch. Rational Mech. Anal. 16 (1964) | Small-data global existence in $\dot H^{1/2}$. |
| H. Koch, D. Tataru, Adv. Math. 157 (2001) | Small-data global existence in $\mathrm{BMO}^{-1}$ (the largest known critical space). |

## Blow-up and self-similar solutions (Architecture 4)

| Source | Role |
|---|---|
| J. Necas, M. Ruzicka, V. Sverak, Acta Math. 176 (1996); T.-P. Tsai (1998) | Leray self-similar blow-up ruled out in $L^3$. |
| T. Tao, J. Amer. Math. Soc. 29 (2016) | Finite-time blow-up for an averaged Navier-Stokes (the barrier). |
| T. Elgindi, Ann. of Math. (2021) | Finite-time singularity for $C^{1,\alpha}$ axisymmetric Euler. |
| G. Luo, T. Hou (2014); J. Chen, T. Hou | Numerically-supported axisymmetric Euler near-singularity. |

## Non-uniqueness via convex integration (Architecture 5)

| Source | Role |
|---|---|
| T. Buckmaster, V. Vicol, Ann. of Math. (2019) | Non-uniqueness of weak solutions of 3D NS below the Leray-Hopf class. |
| P. Isett, Ann. of Math. (2018) | The Onsager conjecture for Euler ($C^{1/3}$ threshold). |
| D. Albritton, E. Brue, M. Colombo, Ann. of Math. (2022) | Non-uniqueness of Leray-Hopf solutions for forced NS. |

## Textbooks and surveys

| Source | Role |
|---|---|
| P. Constantin, C. Foias, "Navier-Stokes Equations," Univ. of Chicago Press (1988) | The standard graduate reference for the mathematical theory. |
| R. Temam, "Navier-Stokes Equations: Theory and Numerical Analysis" | Functional-analytic framework; weak solutions; numerical analysis. |
| C. Doering, J. Gibbon, "Applied Analysis of the Navier-Stokes Equations" | Applied / energy-method oriented introduction. |
| P.-L. Lions, "Mathematical Topics in Fluid Mechanics" | The compressible and incompressible theory. |

## Conventions

- PDFs go in this folder and are gitignored (`*.pdf`). Only this index and the reading notes are tracked.
- When adding a source, record it here with its role and link a reading note in `docs/03_research/reading_notes/` if it is load-bearing.
