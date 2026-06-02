# Reading notes

Notes on the key reference sources, each mapped to the project's findings and directions. The notes focus on structural content (what is actually proved, at the lemma level where it matters) and on how each source bears on the supercriticality gap.

This is a seed set covering the load-bearing references. It grows as the SURVEYOR agent works through the corpus (see [`../../../references/README.md`](../../../references/README.md) for the full library index).

## Index

| Source | Year | Role | Notes |
|---|---|---|---|
| Fefferman, official problem statement | 2000 | the problem | [notes](fefferman_problem_statement.md) |
| Leray | 1934 | weak solutions exist | [notes](leray_1934.md) |
| Caffarelli-Kohn-Nirenberg | 1982 | partial regularity | [notes](caffarelli_kohn_nirenberg_1982.md) |
| Beale-Kato-Majda | 1984 | the blow-up criterion | [notes](beale_kato_majda_1984.md) |
| Escauriaza-Seregin-Sverak | 2003 | the $L^3$ endpoint | [notes](escauriaza_seregin_sverak_2003.md) |
| Tao, averaged Navier-Stokes | 2016 | the barrier | [notes](tao_2016_averaged.md) |

Pending (TODO, see directions): Hopf 1951, Koch-Tataru 2001, Buckmaster-Vicol 2019, Necas-Ruzicka-Sverak 1996, Elgindi 2021, Constantin-Fefferman 1993, Constantin-Foias and Temam textbooks.

## How the sources line up with the spine

- Fefferman fixes the precise target (existence-and-smoothness on $\mathbb{R}^3$ or $\mathbb{T}^3$, four statements).
- Leray and CKN are the unconditional results, and both stop exactly where the supercriticality stops them (existence but not regularity; small singular set but not empty).
- BKM and ESS are the critical continuation criteria: sharp, conditional, unreachable from the supercritical energy.
- Tao 2016 is the barrier that says the missing control must use the exact nonlinearity, not energy-plus-scaling. It is the single most important "negative" result for orienting the regularity side.
