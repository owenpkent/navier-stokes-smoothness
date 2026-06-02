# Reading notes: Leray (1934)

Jean Leray, "Sur le mouvement d'un liquide visqueux emplissant l'espace," Acta Mathematica 63 (1934).

## What it proves

Global-in-time existence of **weak solutions** (Leray called them "turbulent solutions") of the 3D incompressible Navier-Stokes equations for any finite-energy divergence-free initial velocity. These solutions:

- satisfy the equations in a distributional / integrated sense,
- lie in $L^\infty_t L^2_x \cap L^2_t \dot H^1_x$,
- obey the energy inequality $\tfrac12\|u(t)\|_2^2 + \nu\int_0^t\|\nabla u\|_2^2 \le \tfrac12\|u_0\|_2^2$.

This is the foundational existence result. Hopf (1951) extended it to bounded domains; the class is now called Leray-Hopf weak solutions.

## Structural content

- **Construction by compactness.** Leray regularizes the equation (mollifying the transport velocity), solves the regularized problem, derives the energy bound uniformly in the regularization, and extracts a weakly convergent subsequence. The energy bound is exactly what gives the compactness (via Aubin-Lions-type arguments in modern language).
- **The energy inequality, not equality.** The limit solution satisfies the energy inequality, possibly with strict inequality: passing to the weak limit can only lose energy, not create it. Whether equality holds (no anomalous dissipation) is tied to regularity and to the Onsager threshold.
- **Leray's own attempt at self-similar blow-up.** In the same circle of ideas Leray proposed self-similar singular solutions as a candidate blow-up mechanism. These were ruled out in $L^3$ decades later (Necas-Ruzicka-Sverak 1996; Tsai 1998).
- **Partial regularity precursor.** Leray already bounded the set of singular times, the seed of the Caffarelli-Kohn-Nirenberg theory.

## How it bears on the spine

Leray gives the class in which the problem is posed (finite energy, energy inequality) and the only all-time bound (energy), which the repo identifies as supercritical. Everything downstream is the attempt to upgrade Leray's weak solution to a smooth one, and the obstruction is exactly that Leray's bound does not see small scales. The self-similar attempt and its later exclusion are Direction 04.
