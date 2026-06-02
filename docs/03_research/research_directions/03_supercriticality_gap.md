# Direction 03: attack the supercriticality gap directly

Architecture 3 (critical spaces and scaling). The hardest and highest-value direction: find a genuinely new coercive quantity at the critical scaling level.

## The bet

The whole problem is that the only all-time a priori bound (energy) is supercritical. The most direct attack is to look for a new quantity that is (i) coercive enough to control regularity, (ii) at the critical or subcritical scaling level, and (iii) non-increasing (or controlled by the data) along the flow. If such a quantity existed and could be found, it would close the problem. None is known, which is why this is the hardest direction. It is included because any partial progress (even a critical quantity that is *almost* monotone, with a controlled defect) would be a major result.

## Why it is so hard, stated precisely

Tao's 2016 averaged-Navier-Stokes blow-up shows that the target quantity cannot be a soft consequence of energy and scaling alone: the averaged system has the same energy identity and the same scaling and still blows up. So a critical coercive quantity, if it exists, must depend on the **exact** structure of the nonlinear term (the precise transport-and-pressure coupling), in a way the averaging destroys. This is the analog of a "marginal positivity" result: there is no slack for a soft argument, so the quantity must engage the exact equation.

## Concrete targets

1. **Catalog candidate critical quantities.** Beyond $\|u\|_{L^3}$ and $\|u\|_{\dot H^{1/2}}$: helicity (not sign-definite, not coercive, but structurally interesting), the $L^3$ norm restricted to scales, weighted/local critical energies (the CKN local energy), and entropy-type functionals. For each, check coercivity, scaling, and whether it has any monotonicity.
2. **Defect-monotonicity.** For a critical quantity that is not monotone, quantify the defect (the term that breaks monotonicity) and ask whether the defect is controlled by the data. This is the "almost-monotone" program.
3. **Anisotropic critical norms.** Exploit the divergence-free constraint to control regularity from fewer components; map the one-component and anisotropic results and whether any anisotropic critical norm is energy-reachable.

## Method

- For each candidate, derive its evolution equation symbolically (`sympy`), identify the production term, and run its scaling through the criticality bookkeeper.
- Numerically track candidate quantities in the Taylor-Green DNS and look for monotonicity or controlled defect.
- Cross-check against the averaged-NS barrier: would the candidate be monotone for the averaged system too? If yes, it is a soft quantity and cannot work (it is killed by the Tao barrier).

## Success criteria

- A catalog of candidate critical quantities with coercivity, scaling, monotonicity, and the averaged-NS-barrier check for each.
- Identification of any candidate with a controlled monotonicity defect, however partial.

## Controls this must pass

- **Criticality**: the quantity must be critical or subcritical; a supercritical candidate is the energy in disguise.
- **2D**: the quantity must be the one that becomes monotone in 2D (the enstrophy is the 2D answer); a 3D candidate should reduce to a known-good 2D quantity.
- **Averaged-NS barrier**: the candidate must fail to be monotone for Tao's averaged system, i.e. it must use the exact nonlinearity. A candidate monotone for the averaged system is automatically insufficient.
