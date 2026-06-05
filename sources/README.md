# Sources

Original source PDFs and their converted text versions.

This folder holds primary sources that are freely distributable (for example, the official Clay problem statement, and any open-access preprints). Copyrighted textbooks and journal articles are NOT committed; they live in [`../references/`](../references/) (gitignored) and are recorded in that folder's tracked index.

## Convention

- A freely-distributable source PDF goes here as `name.pdf` (the `.gitignore` allows `sources/*.pdf`).
- Its text conversion (for searching and for the reading-notes workflow) goes alongside as `name.txt`, produced with `pdfminer.six` or `pypdf` (see `requirements.txt`).

## Contents

Two freely-distributable primary sources are present, each as a PDF (tracked, the `.gitignore` allows `sources/*.pdf`) with a `.txt` conversion produced by `pdfminer.six`:

| File | Source | Provenance | Reading note |
|---|---|---|---|
| `fefferman_navier_stokes.pdf` / `.txt` | C. Fefferman, "Existence and smoothness of the Navier-Stokes equation," official Clay Millennium Problem statement | Clay Mathematics Institute, `claymath.org` (freely distributed by CMI) | [notes](../docs/03_research/reading_notes/fefferman_problem_statement.md) |
| `tao_2016_averaged.pdf` / `.txt` | T. Tao, "Finite time blowup for an averaged three-dimensional Navier-Stokes equation," J. Amer. Math. Soc. 29 (2016) | arXiv:1402.0290 (open-access preprint) | [notes](../docs/03_research/reading_notes/tao_2016_averaged.md) |

To regenerate a `.txt` after adding a PDF:

```powershell
python -c "from pdfminer.high_level import extract_text; open('NAME.txt','w',encoding='utf-8').write(extract_text('NAME.pdf'))"
```

Note: the `.txt` files are verbatim extractions and retain each source's own punctuation (for example the en dash in Fefferman's "Navier-Stokes" title). The project no-dash style applies to authored prose, not to quoted primary sources, so these conversions are left unaltered.

Copyrighted textbooks and journal articles are NOT placed here; they live in [`../references/`](../references/) (gitignored `*.pdf`) and are recorded in that folder's tracked index, with deep reading notes in [`../docs/03_research/reading_notes/`](../docs/03_research/reading_notes/).
