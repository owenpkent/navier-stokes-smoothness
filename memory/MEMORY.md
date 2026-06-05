# Memory

Cross-session persistent context. Read at session start. Keep it short and current; the authoritative state lives in [`../PHASE_STATE.md`](../PHASE_STATE.md).

## The one fact

The energy is the only all-time a priori bound and it is supercritical (3D $L^2$ velocity norm, scaling exponent $-1/2$). Regularity is a critical statement. The gap between them is the whole problem. This is the compass; do not lose it.

## The three controls (always apply)

1. **2D**: 2D Navier-Stokes is globally smooth (no vortex stretching). A method that ignores stretching is wrong.
2. **Criticality**: a supercritical controlling norm is INSUFFICIENT_BY_ITSELF (`experiments/_shared/criticality.py`).
3. **Viscosity**: inviscid Burgers and 3D Euler blow up; a method blind to $\nu$ is suspect (`experiments/burgers_shock/`).

Plus the **averaged-NS barrier** (Tao 2016): energy-plus-scaling is not enough; the argument must use the exact nonlinearity.

## What runs

- `python -m experiments._shared.smoke_test` (5/5 pass).
- `python -m experiments.scaling_criticality.criticality_table` (instant).
- `python -m experiments.burgers_shock.burgers_blowup` (seconds; inviscid peak ~381 vs viscous ~8).
- `python -m experiments.taylor_green.taylor_green_dns` (~1 min at 32^3; energy dissipates, BKM finite, div ~1e-17).
- `python -m experiments.energy_spectrum.energy_spectrum` (seconds).

Environment note: the local matplotlib is built against NumPy 1.x and crashes on import under NumPy 2.x. The experiments catch this and skip plotting; the numerics are unaffected. To restore plots, reinstall matplotlib for NumPy 2.x.

## Reference corpus

`references/README.md` (annotated bibliography, ~50 entries by architecture) and `references/reading_guide.md` (curated entry path) index the library. `docs/03_research/reading_notes/` holds 22 deep dossiers, one per load-bearing source, each following a fixed template: precise statement, method at the lemma level, criticality placement on the sub/critical/super scale, audit against the three controls, what-it-gives/what-it-doesn't, lineage, references. The index `reading_notes/README.md` groups them by architecture and carries a criticality-placement table. Extend in this template; PDFs stay gitignored.

## Owner

Owen, wheelchair user with muscular dystrophy. Typing is hard. Be proactive, offer A/B/C choices, PowerShell on Windows, no em dashes anywhere.

## Stance

Target not monument. Negative results are coordinates. Honesty is the engine. See [`../docs/researcher_mindset.md`](../docs/researcher_mindset.md).

## Next moves (see PHASE_STATE.md for the live list)

1. SURVEYOR: map every regularity criterion onto the criticality scale (the Constantin-Fefferman vorticity-direction criterion is the lead).
2. BUILDER + ADVERSARY: resolution study on near-singular data with the viscosity control.
3. VERIFIER: state the energy inequality cleanly in Lean; document the Mathlib gap.
