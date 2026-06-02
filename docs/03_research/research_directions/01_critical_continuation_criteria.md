# Direction 01: sharpen the critical continuation criteria

Architecture 2 (conditional regularity criteria).

## The bet

The continuation criteria (PSL, ESS, BKM) are sharp and sit exactly at critical scaling. A proof would bound the critical quantity using the data. The bet of this direction is incremental: rather than bound a critical quantity outright (which is the full problem), push a criterion toward something either the energy or a slightly-more-than-energy bound can reach, or weaken a criterion by a logarithmic factor, which is the kind of improvement that has historically preceded breakthroughs.

## Concrete targets

1. **Logarithmic improvements of the ESS endpoint.** ESS gives regularity from $u \in L^\infty_t L^3_x$. Can the $L^3$ norm be replaced by $L^3$ with a logarithmic relaxation, or by a slightly larger Lorentz space $L^{3,\infty}$ (known partial results exist; map exactly how far they reach)?
2. **Quantitative ESS (Tao 2019).** Tao proved a quantitative version: a bound on how concentrated a potential singularity must be ($\|u\|_{L^3}$ must grow at least triple-logarithmically). Survey this and identify whether the quantitative form suggests a self-improving estimate.
3. **BKM with a critical norm weaker than $L^\infty$.** The BKM integral uses $\|\omega\|_{L^\infty}$. There are refinements with $\|\omega\|_{\mathrm{BMO}}$ (Kozono-Taniuchi) and Besov variants. Map which are genuinely weaker and whether any is energy-reachable.

## Method

- Survey the precise statements and proofs (backward uniqueness and unique continuation for ESS; the harmonic-analysis refinements for BKM).
- For each, run the controlling norm through the criticality bookkeeper (`experiments/_shared/criticality.py`) to confirm it is critical and to quantify any logarithmic gap from the energy's supercritical level.
- Identify the smallest open improvement that would be a publishable result.

## Success criteria

- A precise table of every continuation criterion, its controlling norm, its scaling class, and its exact distance (in scaling exponent or in log factors) from the energy bound.
- Identification of one concrete, small, open improvement worth attempting.

## Controls this must pass

- **Criticality**: the target controlling norm must be critical or subcritical (a supercritical target is the energy restated; INSUFFICIENT_BY_ITSELF).
- **2D**: the criterion must be one that is non-trivial in 3D (in 2D the energy already implies regularity, so a 3D criterion that 2D makes vacuous is on the right track).
- **Viscosity**: continuation criteria are about the viscous flow; confirm the criterion genuinely uses $\nu > 0$ (BKM is stated for both Euler and NS, so be explicit about which regime).
