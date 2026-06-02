# Direction 05: the convex-integration boundary

Architecture 5 (non-uniqueness via convex integration). A survey-and-clarify direction: map precisely what the non-uniqueness results do and do not say about the regularity problem.

## The bet

Convex integration (Buckmaster-Vicol 2019 for NS, building on De Lellis-Szekelyhidi and Isett for Euler/Onsager) produces non-unique weak solutions below the Leray-Hopf regularity. There is a persistent risk of category error: treating non-uniqueness of rough weak solutions as if it bore on smoothness of the strong flow. The bet of this direction is clarifying: establish exactly where the Onsager-type regularity threshold sits, so the regularity question and the non-uniqueness phenomena are kept in their separate regimes. A clean account is a real contribution and prevents wasted effort.

## What the results say

- **Buckmaster-Vicol (2019):** weak solutions of 3D NS in $C_t L^2$ are not unique; there exist non-Leray-Hopf weak solutions with prescribed (non-monotone) energy profiles. These are constructed by iterating high-frequency, high-amplitude perturbations (intermittent Beltrami flows / convex integration).
- **Albritton-Brue-Colombo (2022):** non-uniqueness of Leray-Hopf solutions for NS **with a force**, using a self-similar unstable background. This is closer to the regularity class but uses a force, so it does not settle the unforced Clay problem.
- **Onsager / Isett (2018):** for Euler, the threshold is $C^{1/3}$: above it energy is conserved, below it anomalous dissipation and non-uniqueness appear. The analogous NS threshold organizes where convex integration can operate.

## What they do not say

None of these constructs a singularity of a smooth NS flow, and none contradicts the possibility of global regularity for smooth data. The non-unique solutions are rough (low regularity), the regularity question is about smooth solutions, and the two regimes are separated by the Onsager-type threshold. The non-uniqueness sharpens the **solution concept** (Leray-Hopf is the right class; below it uniqueness fails) without touching the smoothness question.

## Concrete targets

1. **Locate the thresholds.** Tabulate the regularity classes: smooth strong solutions; Leray-Hopf weak solutions; $C_t L^2$ weak solutions; the Onsager threshold. Mark where each non-uniqueness result lives.
2. **The forced vs unforced distinction.** Make precise why Albritton-Brue-Colombo needs a force and what an unforced analog would require.
3. **Implications for the regularity program.** State clearly that convex integration is outside the regularity discipline (it does not concern the smooth flow), and record this so future sessions do not conflate the regimes.

## Method

- Reading notes on Buckmaster-Vicol, Albritton-Brue-Colombo, Isett, De Lellis-Szekelyhidi.
- A single clear diagram / table of regularity classes and thresholds.

## Success criteria

- A precise map of the regularity-class hierarchy with each non-uniqueness result placed.
- A clear written statement of why this architecture is outside the smoothness discipline, to prevent the category error.

## Controls this must pass

This direction is a clarification, so the controls apply in reverse: the point is to confirm that convex integration sits **outside** the regularity discipline. It does not need to pass the 2D / criticality / viscosity controls because it is not a regularity argument; the deliverable is the precise statement of that fact.
