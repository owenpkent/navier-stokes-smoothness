# Reading notes: Albritton-Brue-Colombo (2022), non-uniqueness of Leray solutions of the forced Navier-Stokes equations

Dallas Albritton, Elia Brue, Maria Colombo, "Non-uniqueness of Leray solutions of the forced Navier-Stokes equations," Annals of Mathematics (2) 196 (2022), 415-455. (arXiv:2112.03116, December 2021.)

> This is the first construction of two distinct Leray-Hopf solutions of the 3D Navier-Stokes equations with the same initial data and the same body force. It matters because it pushes non-uniqueness up from the rough convex-integration regime (below the energy class, Buckmaster-Vicol 2019) into the Leray-Hopf class itself, the very class in which the Millennium problem asks for uniqueness and regularity. The mechanism is not convex integration: it is a dynamical-systems instability. A linearly unstable similarity profile, built from Vishik's unstable two-dimensional vortex lifted to an axisymmetric-without-swirl 3D field, has an unstable manifold, and two distinct trajectories on that manifold (the background and a perturbation) share the same Cauchy data. It engages Architecture 5 (non-uniqueness) but lives at the boundary with Architecture 4 (self-similar / spectral instability). The decisive caveat: it requires an external force $f$, and that force sits OUTSIDE the unforced Clay statement. It is also distinct from control A: the seed is a 2D vortex, but the constructed object is a genuinely 3D axisymmetric field in the energy class, so it does not predict 2D blow-up and does not contradict 2D global regularity.

## What it proves

### Statement (main theorem)

There exist a body force $f \in L^1_t L^2_x(\mathbb{R}^3 \times (0,\infty))$ (more precisely with the integrability that keeps the solutions Leray-Hopf) and two distinct Leray-Hopf weak solutions $u^{(1)} \neq u^{(2)}$ of the forced 3D incompressible Navier-Stokes system

$$\partial_t u + (u \cdot \nabla) u - \Delta u + \nabla p = f, \qquad \nabla \cdot u = 0, \qquad u(\cdot, 0) = u_0,$$

on $\mathbb{R}^3 \times (0, \infty)$, with the same initial datum $u_0 = 0$ and the same force $f$, both satisfying the strong energy inequality

$$\tfrac12 \|u(t)\|_{L^2}^2 + \int_s^t \|\nabla u(\tau)\|_{L^2}^2 \, d\tau \le \tfrac12 \|u(s)\|_{L^2}^2 + \int_s^t \langle f, u \rangle \, d\tau$$

for a.e. $s$ (including $s = 0$) and all $t \ge s$. In the published construction the initial velocity is taken to be zero, so the non-uniqueness is driven entirely by the force together with the instability, not by any choice of initial data.

Both solutions belong to the Leray-Hopf class

$$u \in L^\infty_t L^2_x \cap L^2_t \dot H^1_x,$$

i.e. the finite-energy, finite-dissipation class. This is the headline: the two solutions are not below the energy class. They are honest Leray-Hopf solutions. The non-uniqueness is therefore at the level where the unforced theory has uniqueness open, not in the rougher class where Buckmaster-Vicol already produced non-uniqueness.

### The shape of the two solutions

- One solution is the **unstable background** $\bar u$, which is self-similar: $\bar u(x,t) = \tfrac{1}{\sqrt{t}}\, U\!\left(\tfrac{x}{\sqrt{t}}\right)$ for a fixed profile $U$ (a $(-1)$-homogeneous-in-the-similarity-variable object). This is a forward self-similar solution in the Jia-Sverak sense, not a backward (blow-up) self-similar solution.
- The other solution **$\bar u + $ perturbation** is a trajectory on the unstable manifold of $\bar u$. As $t \to 0^+$ the perturbation decays faster than $\bar u$, so both solutions emanate from $u_0 = 0$ with the same force. They separate at positive time because the perturbation grows along the unstable eigendirection.

Crucially the two solutions agree at $t = 0$ in the strong $L^2$ sense (both are zero) and the force is identical. The non-uniqueness is the existence of two distinct continuations.

## Method / structure

The construction is a dynamical-systems argument in similarity variables, not a convex-integration iteration. The skeleton, at the lemma level:

1. **Pass to similarity (self-similar) variables.** Write $\xi = x / \sqrt{t}$, $\tau = \log t$, and $u(x,t) = \tfrac{1}{\sqrt{t}}\, U(\xi, \tau)$. The Navier-Stokes equation becomes an autonomous-in-$\tau$ equation for the profile $U$:

$$\partial_\tau U - \tfrac12 (1 + \xi \cdot \nabla_\xi) U - \Delta_\xi U + (U \cdot \nabla_\xi) U + \nabla_\xi P = F,$$

where the term $-\tfrac12 (1 + \xi \cdot \nabla_\xi) U$ is the generator of the scaling/dilation. A genuinely self-similar Navier-Stokes solution is a fixed point ($\partial_\tau U = 0$, $F = 0$) of this flow; the regularity question for self-similar profiles is a steady problem in $\xi$.

2. **Choose an unstable steady profile.** The authors do not solve the steady self-similar Navier-Stokes equation exactly. They instead pick a smooth, compactly supported **vortex-ring** profile $\bar U$ whose cross-section is a modification of Vishik's unstable two-dimensional vortex, and they ADD a force $F$ (equivalently $f$) so that $\bar U$ is a solution of the forced steady profile equation by construction. This is the technical heart: the force absorbs the residual $-\tfrac12(1+\xi\cdot\nabla_\xi)\bar U - \Delta_\xi \bar U + (\bar U \cdot \nabla_\xi)\bar U + \nabla_\xi \bar P$, so $\bar U$ need not solve the unforced equation. This is why the force is essential, not incidental (see below).

3. **The Vishik instability, lifted to 3D.** M. Vishik (in two preprints, "Instability and non-uniqueness in the Cauchy problem for the Euler equations of an ideal incompressible fluid, Part I and Part II," arXiv:1805.09426 and arXiv:1805.09440, 2018) constructed a radially symmetric two-dimensional vorticity profile that is **linearly unstable** for the 2D Euler dynamics: the linearization around it has an unstable eigenvalue, i.e. an eigenfunction with eigenvalue of strictly positive real part. The ABC construction takes this 2D unstable vortex as the cross-sectional profile of a 3D **axisymmetric, swirl-free** vortex ring. The 3D axisymmetric-without-swirl vorticity equation for the scalar $\omega_\theta / r$ is transported like a 2D scalar (no swirl means the vortex-stretching is the controlled $r$-weighted form), which is exactly what lets the 2D spectral instability transfer to the 3D similarity dynamics.

4. **Spectral / unstable-manifold construction.** Linearize the similarity-variable flow around $\bar U$. The instability of step 3 yields an eigenvalue $\lambda$ of the linearized operator $L_{\bar U}$ with $\operatorname{Re}\lambda > 0$ and a corresponding eigenfunction $\eta$. The authors then build a genuine nonlinear trajectory $U(\tau) = \bar U + a\, e^{\lambda \tau}\eta + (\text{higher order})$ on the unstable manifold, via a fixed-point / Duhamel argument controlling the nonlinear remainder. Translating back to physical variables, $a\, e^{\lambda\tau}\eta$ becomes a perturbation that vanishes as $t \to 0^+$ (because $e^{\lambda\tau} = t^{\lambda} \to 0$ when $\operatorname{Re}\lambda > 0$ and $\tau = \log t \to -\infty$), so the perturbed solution and the background both attain $u_0 = 0$. Two trajectories, same Cauchy data, same force: non-uniqueness.

5. **Energy class check.** The profiles are smooth and compactly supported in $\xi$ (the vortex ring is localized), the self-similar scaling $\tfrac{1}{\sqrt t} U(x/\sqrt t)$ produces $L^2_x$-finite, $\dot H^1_x$-finite fields with the right time-integrability, and the force is chosen with the integrability ($f \in L^1_t L^2_x$ regime) that preserves the strong energy inequality. So both solutions are Leray-Hopf.

The mechanism is therefore: **2D linear instability (Vishik) $\to$ 3D axisymmetric similarity profile $\to$ unstable eigenvalue $\lambda$ $\to$ unstable manifold $\to$ two solutions from $u_0 = 0$**. This realizes, rigorously and with a force, the Jia-Sverak program (Invent. Math. 196 (2014)) which had conjectured exactly this scenario for forward self-similar solutions.

## Criticality placement

The construction lives **precisely on the critical scaling line**, by design.

- The self-similar ansatz $u(x,t) = \tfrac{1}{\sqrt t}\, U(x/\sqrt t)$ is invariant under the Navier-Stokes scaling $u_\lambda(x,t) = \lambda\, u(\lambda x, \lambda^2 t)$. A $(-1)$-homogeneous-in-$x$ datum and a self-similar profile are scale-invariant objects: they sit at criticality, not below it.
- The corresponding initial data class for forward self-similar solutions is $(-1)$-homogeneous, which lands in the critical Lebesgue-weak / Besov scale (e.g. $L^{3,\infty}(\mathbb{R}^3)$ and critical Besov spaces $\dot B^{-1+3/q}_{q,\infty}$), the same scale as $\dot H^{1/2}$, $L^3$, and $\mathrm{BMO}^{-1}$. The ABC solutions, the authors note, "live precisely on the borderline of the known well-posedness theory." That borderline is the critical scaling line.
- Run it through the criticality bookkeeper (`experiments/_shared/criticality.py`): the kinetic energy $\|u\|_{L^2_x}^2$ scales as $\lambda^{-1}$ in 3D and is SUPERCRITICAL (the energy does not see the small-scale self-similar concentration). The critical norms ($\dot H^{1/2}$, $L^3$) are scale-invariant. The ABC profile is finite-energy but its non-uniqueness is invisible to the energy: the two solutions have the same energy budget. This is the supercriticality gap manifesting as a uniqueness gap. Energy bounds (the only global a priori control) do not separate $u^{(1)}$ from $u^{(2)}$, because both satisfy the same energy inequality. The non-uniqueness is precisely a phenomenon the supercritical energy cannot exclude.

So: critical scaling for the solutions, supercritical energy as the only global bound, and the gap between them is exactly the room in which two Leray-Hopf solutions coexist. This is the same structural ceiling that the criticality control (B) flags everywhere in the project, viewed from the uniqueness side rather than the regularity side.

## Against the three controls

This result is in Architecture 5 / 4-boundary, so it is partly OUTSIDE the regularity discipline. It is not a candidate regularity argument and is not trying to pass the controls in the "this would close regularity" sense. The right question is where it sits relative to each control.

- **Control A (2D NS is globally smooth; a method that would predict 2D blow-up is wrong).** This is the subtle one and the reason the result does not contradict the 2D control. The instability seed is a 2D vortex (Vishik), but the constructed non-unique object is a **3D axisymmetric, swirl-free** field, not a 2D flow. Two distinctions matter:
  1. Vishik's instability is for the **Euler** (inviscid) 2D dynamics and concerns **non-uniqueness**, not blow-up. 2D Navier-Stokes (viscous) remains globally smooth and unique with $L^2$ data; nothing here touches that. 2D Euler uniqueness for merely $L^p$ vorticity is a genuinely different question (the Yudovich class requires $L^\infty$ vorticity), and Vishik's instability lives in that gap.
  2. The ABC solutions are 3D. The similarity variable couples the 2D cross-sectional dynamics to the dilation generator $-\tfrac12(1+\xi\cdot\nabla)$, which is a 3D-self-similar object with no 2D analog at the level used. So the construction does NOT "lift to a 2D Navier-Stokes blow-up or 2D NS non-uniqueness." It does not predict any 2D Navier-Stokes pathology. The 2D control is respected. The seeding by a 2D vortex is a tool, not a claim about 2D NS.
- **Control B (energy is the only global bound and is supercritical, so energy-level estimates cannot close regularity).** The result is a vivid positive illustration of control B from the uniqueness angle. Both solutions satisfy the same strong energy inequality, so the energy cannot distinguish them. The supercriticality gap is precisely the space the second solution lives in. This is consistent with, and sharpens, the project's structural commitment: the energy is too weak to enforce uniqueness, just as it is too weak to enforce regularity.
- **Control C (inviscid models blow up; a method blind to viscosity is suspect).** Viscosity is present and essential to the Leray-Hopf framing (the $L^2_t \dot H^1_x$ dissipation is part of the class). The instability, however, is inherited from a 2D **Euler** unstable vortex, so the inviscid layer is where the mechanism originates. The viscous similarity flow inherits the unstable eigenvalue. The result does not ignore viscosity; it shows that viscosity is not enough to restore uniqueness once a forced unstable critical background is allowed. This is consistent with the viscosity control: viscosity matters, but it is not a uniqueness panacea at the critical scale.

Net: as an Architecture 5 / 4-boundary result, it sits OUTSIDE the regularity discipline (it is about uniqueness with a force, not smoothness of the unforced flow). It respects all three controls. The forcing is what places it outside the Clay statement; see next section.

## What it gives / what it does not give

**What it gives.**

- The first non-uniqueness of Navier-Stokes solutions **inside** the Leray-Hopf class (with a force). Before this, non-uniqueness was known only below the energy class (Buckmaster-Vicol 2019) or for the unforced problem not at all. This locates the uniqueness frontier: the Leray-Hopf class does not by itself guarantee uniqueness once a (rough but admissible) force is allowed.
- A rigorous realization of the Jia-Sverak (2014) scenario: forward self-similar solutions with an unstable manifold producing genuine non-uniqueness. It converts a conjectural mechanism into a theorem.
- A clean separation of mechanisms: this is a **spectral / dynamical-systems** non-uniqueness (an unstable eigenvalue and its unstable manifold), categorically different from the **convex-integration** non-uniqueness of Buckmaster-Vicol. Two independent routes to non-uniqueness now exist.
- A precise statement of what an unforced analog would have to overcome: one would need an unstable self-similar profile that solves the **unforced** steady similarity equation exactly, which the force is currently covering for.

**What it does not give.**

- It does **not** settle or even directly bear on the **unforced** Clay problem. The force $f$ is essential to the construction (it is what makes the chosen Vishik-based vortex an exact background). Remove the force and the background is no longer a solution. The Millennium problem asks about $f = 0$ (or smooth decaying $f$ derived from a potential, per Fefferman's statement). ABC is OUTSIDE that statement.
- It does **not** construct a singularity or any loss of smoothness of a strong solution. Both ABC solutions are, away from $t = 0$, as smooth as the self-similar profile (smooth). There is no blow-up. Non-uniqueness and blow-up are different pathologies; this is non-uniqueness only.
- It does **not** show 2D Navier-Stokes is non-unique or singular (control A respected, as above).
- It does **not** by itself rule out unforced uniqueness in the Leray-Hopf class; it shows the energy inequality alone cannot enforce it, which was already structurally expected from supercriticality. The unforced uniqueness question stays open.

The gap to the Clay problem is therefore exactly the force. The result is a coordinate, in the project's sense: it tells us that any proof of unforced uniqueness/regularity must use a feature that the force can break, i.e. it cannot be a soft argument that would survive the addition of an admissible force. This disciplines the uniqueness side the way the Tao 2016 averaged barrier disciplines the regularity side.

## Lineage and sharpest known form

**Builds on.**

- M. Vishik, "Instability and non-uniqueness in the Cauchy problem for the Euler equations of an ideal incompressible fluid, Part I and Part II," arXiv:1805.09426 and arXiv:1805.09440 (2018). The unstable 2D vortex and its unstable eigenvalue are the seed. (A book-length account: M. Vishik, with appendices by the editors, was later circulated; the instability is the load-bearing input.)
- H. Jia, V. Sverak, "Local-in-space estimates near initial time for weak solutions of the Navier-Stokes equations and forward self-similar solutions," Invent. Math. 196 (2014), 233-265, and their companion work conjecturing non-uniqueness via unstable self-similar profiles. ABC is the rigorous fulfillment of that program (with a force).
- J. Leray (1934) for the self-similar ansatz idea and the Leray-Hopf class; the forward (not backward) self-similar regime here is the one Necas-Ruzicka-Sverak (1996) left open after ruling out backward $L^3$ profiles.
- T. Buckmaster, V. Vicol, "Nonuniqueness of weak solutions to the Navier-Stokes equations," Ann. of Math. (2) 189 (2019), 101-144, as the contrasting (convex-integration, below-energy) non-uniqueness it sharpens by moving INTO the energy class.

**Built on it / sharpest known form (as of 2025).**

- The same authors and collaborators extended the mechanism. ABC-type instability arguments seeded the program of moving non-uniqueness toward less and less forcing.
- Stochastic / law-non-uniqueness analogs: e.g. "Non-uniqueness in law of Leray solutions to 3D forced stochastic Navier-Stokes equations" (arXiv:2309.09753, 2023) and "Non-uniqueness of Leray-Hopf solutions for stochastic forced Navier-Stokes equations" (arXiv:2309.03668, 2023) carry the forced non-uniqueness into the stochastic setting.
- Gluing and density: "Gluing non-unique Navier-Stokes solutions" (arXiv:2209.03530, 2022) builds on the ABC background to glue non-unique trajectories.
- The frontier question, the **unforced** Leray-Hopf non-uniqueness, has seen claimed progress: "Nonuniqueness of Leray-Hopf solutions to the unforced incompressible 3D Navier-Stokes equation" (arXiv:2509.25116, 2025) (verify: this is a recent preprint, status and acceptance not yet confirmed against a published version as of this writing). If it stands, it would remove the force and bear much more directly on the Clay uniqueness question; until verified it should be treated as an unconfirmed claim, and it does not change the published ABC statement, which is forced.
- For the 2D forced case, sharp non-uniqueness thresholds for forced 2D Navier-Stokes and dissipative SQG have been pushed in the convex-integration line (e.g. arXiv:2601.00331, 2026, "Sharp nonuniqueness for the forced 2D Navier-Stokes and dissipative SQG equations") (verify: preprint metadata). Note the 2D-forced non-uniqueness uses a force and so does not contradict control A's statement about unforced 2D Navier-Stokes global regularity.

The sharpest **published, peer-reviewed** form of the ABC result itself remains the Annals 2022 paper: two distinct Leray-Hopf solutions, same zero datum, same force, via the Vishik-seeded unstable self-similar profile.

## References

- D. Albritton, E. Brue, M. Colombo, "Non-uniqueness of Leray solutions of the forced Navier-Stokes equations," Ann. of Math. (2) 196 (2022), 415-455. arXiv:2112.03116. [Annals page](https://annals.math.princeton.edu/2022/196-1/p03), [arXiv abstract](https://arxiv.org/abs/2112.03116).
- M. Vishik, "Instability and non-uniqueness in the Cauchy problem for the Euler equations of an ideal incompressible fluid, Part I/Part II," arXiv:1805.09426, arXiv:1805.09440 (2018).
- H. Jia, V. Sverak, "Local-in-space estimates near initial time for weak solutions of the Navier-Stokes equations and forward self-similar solutions," Invent. Math. 196 (2014), 233-265.
- T. Buckmaster, V. Vicol, "Nonuniqueness of weak solutions to the Navier-Stokes equations," Ann. of Math. (2) 189 (2019), 101-144.
- J. Necas, M. Ruzicka, V. Sverak, "On Leray's self-similar solutions of the Navier-Stokes equations," Acta Math. 176 (1996), 283-294.
- J. Leray, "Sur le mouvement d'un liquide visqueux emplissant l'espace," Acta Math. 63 (1934), 193-248.
- Follow-up preprints (verify status): [arXiv:2309.09753](https://arxiv.org/pdf/2309.09753), [arXiv:2309.03668](https://arxiv.org/pdf/2309.03668), [arXiv:2209.03530](https://arxiv.org/abs/2209.03530), [arXiv:2509.25116](https://arxiv.org/pdf/2509.25116) (claimed unforced non-uniqueness, unconfirmed), [arXiv:2601.00331](https://arxiv.org/pdf/2601.00331) (forced 2D sharp non-uniqueness).

## Cross-links

- Primary direction: [`../research_directions/05_convex_integration_boundary.md`](../research_directions/05_convex_integration_boundary.md). ABC is the "non-uniqueness inside the Leray-Hopf class, but with a force" entry; this note supplies the lemma-level mechanism and the forced-vs-unforced distinction that direction 05 asks for as a concrete target.
- Secondary direction: [`../research_directions/04_blowup_and_barriers.md`](../research_directions/04_blowup_and_barriers.md). The forward self-similar / unstable-manifold mechanism is shared with the Jia-Sverak scenario catalogued there.
- Criticality tie-in: [`../research_directions/03_supercriticality_gap.md`](../research_directions/03_supercriticality_gap.md). The two solutions share an energy budget; the gap between supercritical energy and critical scaling is exactly where the second solution lives.
- 2D-control subtlety: [`../research_directions/02_vorticity_geometry.md`](../research_directions/02_vorticity_geometry.md). The seed is a 2D vortex but the object is 3D axisymmetric swirl-free; the axisymmetric vortex-stretching structure is the relevant geometry.
- Sibling notes: [`./necas_ruzicka_sverak_1996.md`](./necas_ruzicka_sverak_1996.md) (backward self-similar ruled out in $L^3$, the complement to the forward regime used here), [`./leray_1934.md`](./leray_1934.md) (the Leray-Hopf class and self-similar ansatz), [`./tao_2016_averaged.md`](./tao_2016_averaged.md) (the regularity-side barrier, the dual of this uniqueness-side coordinate).
- Bibliography entry: [`../../../references/README.md`](../../../references/README.md), Architecture 5 and "Recent developments (2018-2025)" tables.

## What this enables / what remains open

**Enables.** A precise statement, for BUILDER and ADVERSARY, of the forced-vs-unforced boundary: any unforced uniqueness/regularity argument must use structure that the addition of an admissible $L^1_t L^2_x$ force can destroy, because that force is exactly what ABC exploits. It gives SYNTHESIZER a clean placement of the uniqueness frontier (inside Leray-Hopf, but forced) and a categorical distinction between spectral/instability non-uniqueness and convex-integration non-uniqueness. It supplies the criticality bookkeeper a uniqueness-side example of the supercriticality gap: two solutions, one energy budget.

**Remains open.** (1) Unforced Leray-Hopf non-uniqueness, the actual Clay-adjacent question. There is a 2025 preprint claiming it (arXiv:2509.25116, unverified here); its status should be checked before any downstream use. (2) Whether the ABC force can be made smooth and decaying (potential-type, per Fefferman's allowed forcing) rather than merely $L^1_t L^2_x$; if so the result would move closer to the Clay framing. (3) The exact location of the unstable eigenvalue $\lambda$ and whether a sharper profile lowers the regularity of the required force. (4) Whether an unstable self-similar profile solving the **unforced** steady similarity equation exists, which is the missing ingredient for a force-free analog. None of these is the unforced regularity (smoothness) problem, which this result leaves entirely untouched: ABC is about uniqueness with a force, not smoothness without one.
