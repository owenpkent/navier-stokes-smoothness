# Cross-field conjecture forge (2026-06-11)

A run of the conjecture-forge protocol ([`OPERATIONS.md`](../../../OPERATIONS.md) section 10) in its cross-field variant: instead of the ten in-field lenses, three BUILDER forges each imported structure from a genuinely different discipline, every card was run through the four gates by ADVERSARY (with independent derivation of the two load-bearing mathematical claims), and survivors got SURVEYOR precedent checks.

## The run

| Stage | Output |
|---|---|
| Forge (3 builders, 6 lenses) | [`cards_quantum_info.md`](cards_quantum_info.md) (fault-tolerance threshold, uncertainty principle), [`cards_gr_geometric.md`](cards_gr_geometric.md) (trapped surfaces, Perelman monotonicity), [`cards_statmech_kinetic.md`](cards_statmech_kinetic.md) (instanton action, hypocoercivity) |
| Attack + precedent | [`adversary_report.md`](adversary_report.md) (identity audits, gate table, verdicts, probe ranking, precedent statuses) |

## Scoreboard

| Card | Lens source | Self-assessed | ADVERSARY verdict | Precedent |
|---|---|---|---|---|
| No fault-tolerant cascade | quantum error correction | wounded | wounded | not checked (below funding line) |
| Circulation-quantum halo | uncertainty principle / GP vortices | alive | **wounded** (two leaks in the conditional chain) | partially_known |
| Trapped region / NS censorship | GR trapped surfaces | wounded | wounded | not checked (below funding line) |
| Lagrangian backward kernel + conjecture (H) | Perelman entropy | alive | **wounded** ((H) false as universally quantified; repair must be intensity-conditioned) | partially_known |
| Octave-Reynolds tollgate | Freidlin-Wentzell instantons | wounded | wounded | partially_known (largest known fraction) |
| Hypocoercivity twist | Villani hypocoercivity | dead | dead (autopsy confirmed; the viscous-commutator wound is the fatal one) | n/a |

No card survived unconditionally. That is the expected and honest outcome; the yield is below.

## What the forge yielded (the keepers)

1. **An exact critical identity, audit-confirmed.** With $G^u$ the backward Kolmogorov kernel of $dX = u\,dt + \sqrt{2\nu}\,dB$ (Constantin-Iyer process), $$\frac{d}{dt}\int |\omega|^2 G^u\,dx = -2\nu\int |\nabla\omega|^2 G^u + 2\int (\omega\cdot S\omega)\, G^u,$$ with zero error terms (the cancellation requires the backward equation; the forward kernel leaves an uncancelled term). The weighted quantity $W = (t_0 - t)^2 \int |\omega|^2 G^u$ is exactly critical ($a = 0$). Precedent: the ingredients are known (Constantin-Iyer, Drivas-Eyink), the identity itself appears to be unstated folklore, and the assembly (critical $W$, the $\kappa = 1$ pin saturated by Elgindi's profile, the reduction of everything to the conditioned Harnack inequality (H)) is the new part. (H) as universally quantified is FALSE (long-time mixing degenerates it to global enstrophy decay, contradicted by observed enstrophy growth); the open repaired form is intensity-conditioned (H), the sharpest new analytic target this run produced.
2. **A provable halo lemma with an explicit constant.** Kinetic energy in the annulus around a direction-coherent vortex tube (circulation $\Gamma$, core $a$, length $L$) is $\ge \frac{\sqrt{3}}{4}\, \Gamma^2 L \log(L/a)$. Audit-confirmed (with the closed-curve direction-swing constant corrected to $\sqrt 2$). The unconditional budget argument dies by exactly the LEARNINGS #1 factor, as it must; the conditional chain through the $\beta = 0$ coherence endpoint leaks at two named places (length pinning, opposite-signed sheath cancellation), and sheet roll-up is the standing evasion. VERIFIER candidate: the lemma itself is elementary and Lean-shaped.
3. **A folklore re-coordinatization with new dials.** The octave-Reynolds tollgate is mostly CKN-as-local-Reynolds folklore, but the per-octave ledger (the $q$ ratio, the gear ratio $g$, the depletion margin of conjecture A1) is new instrumentation, and its probe is the cheapest on the table.
4. **Two corpses with transferable autopsies.** Hypocoercivity dies structurally: commutator methods transfer dissipation across directions at fixed amplitude order, while the NS degeneracy is across amplitude orders; this fences off all constant-coefficient polynomial twists, not just the one tried. The naive cascade-timing and energy-toll imports die at the Tao barrier, with the counterfeit-currency table recorded.
5. **Convergence as corroboration.** Independently, the quantum-information, stat-mech, and kinetic lenses all terminated at the same residue: pressure nonlocality plus geometric depletion is the only currency averaging cannot counterfeit. Three foreign starting points arriving at Direction 02's doorstep is evidence the prioritization is right.

## Funded-first probe (ADVERSARY ranking)

The **octave ledger post-processor** (`experiments/octave_ledger/`, to be built): runs today on the stored Hou-Luo and vortex-stretching outputs, measures $q$ vs 1 at octave Reynolds $R \approx 1$, the gear ratio $g$, and depletion at peak, with the circulation-morphology diagnostics of the halo card co-mounted (active-scale circulation $\Gamma_{act}/\nu$, sheet-vs-tube aspect ratio, radial $\Gamma(s)$ profile). Registered in [`experiments/PLAN.md`](../../../experiments/PLAN.md).

## Status of the cards

Wounded cards are coordinates, not trash: each carries a precise repair target (intensity-conditioned (H); the two halo-chain leaks; the $R_*$ constant gap) and a named kill-signature its probe can deliver. Dead cards are kept with autopsies per [`docs/researcher_mindset.md`](../../researcher_mindset.md).
