# Sources

Original source PDFs and their converted text versions.

This folder holds primary sources that are freely distributable (for example, the official Clay problem statement, and any open-access preprints). Copyrighted textbooks and journal articles are NOT committed; they live in [`../references/`](../references/) (gitignored) and are recorded in that folder's tracked index.

## Convention

- A freely-distributable source PDF goes here as `name.pdf` (the `.gitignore` allows `sources/*.pdf`).
- Its text conversion (for searching and for the reading-notes workflow) goes alongside as `name.txt`, produced with `pdfminer.six` or `pypdf` (see `requirements.txt`).

## Suggested first source

- The Clay Mathematics Institute official problem statement by Charles Fefferman is the canonical primary source and is freely available from the CMI website. Place it here as `fefferman_navier_stokes.pdf` with a `.txt` conversion, and see the reading note at [`../docs/03_research/reading_notes/fefferman_problem_statement.md`](../docs/03_research/reading_notes/fefferman_problem_statement.md).

(Empty of binaries at scaffold time; the index records the intended contents.)
