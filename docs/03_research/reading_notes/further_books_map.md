# Reading notes: further books, an extended coordinate map

> A companion to [`textbooks_map.md`](textbooks_map.md), which maps the eight standard graduate references (Constantin-Foias, Temam, Doering-Gibbon, Majda-Bertozzi, Bahouri-Chemin-Danchin, Robinson-Rodrigo-Sadowski, Galdi, Sohr), and to the single-book dossier [`lemarie_rieusset_book.md`](lemarie_rieusset_book.md). This note documents the *other* books that are useful to this program: additional Navier-Stokes and Euler monographs, the analysis substrate the critical-space and partial-regularity theory is built on, and the books tied to the project's own experimental threads (the Taylor-Green DNS, the energy spectrum, the Chen-Hou rigorous-numerics frontier). Each entry says what the book is the best reference *for*, which architecture (1 through 5) and research direction it serves, and where its central machinery sits on the criticality scale and against the three controls (A: 2D stays smooth; B: the energy is supercritical; C: viscosity and the exact 3D structure are essential). As in the eight-book map, a textbook collects results rather than proving one, so the criticality placement is of the *machinery* the book is built around, not of a single theorem.

The criticality convention is the bookkeeper's (`experiments/_shared/criticality.py`): a spatial norm $\|u\|_{L^q(\mathbb{R}^3)}$ has scaling exponent $a = 1 - 3/q$ under $u_\lambda(x,t)=\lambda\,u(\lambda x,\lambda^2 t)$, with $a>0$ subcritical, $a=0$ critical, $a<0$ supercritical. The energy pair $L^\infty_t L^2_x$ ($a=-1/2$) and $L^2_t\dot H^1_x$ is the supercritical bound every functional-analytic book is ultimately built on.

## The books mapped here

| # | Reference | Year | Best for | Architecture | Control |
|---|---|---|---|---|---|
| **NS / Euler monographs** ||||||
| 1 | Tsai, *Lectures on Navier-Stokes Equations* | 2018 | modern graduate text; self-similar solutions, by the NRS-exclusion author | 1, 2, 3, 4 | A, B, C |
| 2 | Bedrossian-Vicol, *Math. Analysis of Euler and NS: An Introduction* | 2022 | the only modern text that reaches the convex-integration boundary | 1, 4, 5 | A, B, C |
| 3 | Chemin, *Perfect Incompressible Fluids* | 1998 | the inviscid (Euler) paradifferential theory; the $\nu=0$ contrast | 4 | C (the inviscid limit) |
| 4 | Marchioro-Pulvirenti, *Math. Theory of Incompressible Nonviscous Fluids* | 1994 | 2D Euler global theory, vortex dynamics, point vortices | 2, 4 | A and C |
| 5 | Cannone, *Ondelettes, paraproduits et Navier-Stokes* | 1995 | the origin of the wavelet / Besov self-similar critical-space program | 3 | B (critical side) |
| 6 | Lemarie-Rieusset, *Recent Developments in the NS Problem* | 2002 | the predecessor encyclopedia; mild solutions, critical spaces | 1, 2, 3 | B |
| 7 | Boyer-Fabrie, *Math. Tools for Incompressible NS and Related Models* | 2013 | the modern function-space toolkit (traces, div/curl, Stokes) | 1 | B (substrate) |
| 8 | P.-L. Lions, *Mathematical Topics in Fluid Mechanics, Vol. 1* | 1996 | compactness methods; the renormalized / weak-solution boundary | 1, 5 | B |
| 9 | Seregin, *Lecture Notes on Regularity Theory for the NS Equations* | 2014 | suitable weak solutions, $\varepsilon$-regularity, ESS with full proofs | 1, 2 | B |
| 10 | Foias-Manley-Rosa-Temam, *Navier-Stokes Equations and Turbulence* | 2001 | the rigorous bridge to turbulence (cascade, attractors, statistics) | 1 | B |
| **Analysis substrate** ||||||
| 11 | Grafakos, *Classical* and *Modern Fourier Analysis* | 2014 | the harmonic-analysis foundation under all critical-space work | 3 | B |
| 12 | Stein, *Singular Integrals* (and *Harmonic Analysis*) | 1970, 1993 | Calderon-Zygmund theory; the Leray projector and Riesz transforms | 1, 3 | B |
| 13 | Triebel, *Theory of Function Spaces* | 1983-2006 | the definitive Besov / Triebel-Lizorkin scale | 3 | B |
| 14 | Bergh-Lofstrom, *Interpolation Spaces* | 1976 | the interpolation theory that places the critical spaces | 3 | B |
| 15 | Adams-Fournier, *Sobolev Spaces* (and Brezis) | 2003, 2011 | the Sobolev / embedding substrate | all | B |
| 16 | Evans, *Partial Differential Equations* | 2010 | the graduate PDE backbone; energy methods, Sobolev | 1 | B |
| 17 | Taylor, *PDE III: Nonlinear Equations* | 2011 | NS and Euler via paradifferential calculus, in one text | 1, 2, 3 | A, B, C |
| **Experiment-adjacent threads** ||||||
| 18 | Frisch, *Turbulence: The Legacy of A. N. Kolmogorov* | 1995 | the cascade / Onsager phenomenology behind the energy spectrum | 4, 5 | B, C |
| 19 | Robinson, *Infinite-Dimensional Dynamical Systems* | 2001 | the attractor theory cleanly; the 2D-finite / 3D-conditional split | 1 | A, B |
| 20 | Canuto-Hussaini-Quarteroni-Zang, *Spectral Methods* | 2006-2007 | the numerical-analysis backing for the pseudo-spectral DNS | (numerics) | C |
| 21 | Nakao-Plum-Watanabe, *Numerical Verification ... for PDEs* | 2019 | the rigorous-numerics method behind the Chen-Hou blow-up proof | 4 | C |

---

## Part I. Further Navier-Stokes and Euler monographs

### 1. Tsai, "Lectures on Navier-Stokes Equations" (2018)

T.-P. Tsai, *Lectures on Navier-Stokes Equations*, Graduate Studies in Mathematics 192, American Mathematical Society (2018). ISBN 978-1-4704-3096-2.

> The most useful single *modern* graduate textbook to put next to Robinson-Rodrigo-Sadowski. It is course-tested, self-contained, and written by Tian-Peng Tsai, who proved the local-energy strengthening of the Necas-Ruzicka-Sverak self-similar exclusion (the Tsai 1998 result that sits inside the project's NRS dossier). It covers the Stokes equations, weak and mild solutions, the regularity criteria, partial regularity, and a genuinely modern chapter on self-similar (both backward and forward) solutions that most older texts lack. It serves Architectures 1 through 4 and engages all three controls.

What it is the best reference for: the Stokes system and the Oseen tensor as a warm-up; mild solutions in $L^q$ and the critical $L^3$ / $\dot H^{1/2}$ theory with clean fixed-point proofs; the Prodi-Serrin criteria and the CKN partial-regularity theorem in modern notation; and, distinctively, **self-similar solutions** done carefully, backward (Leray's ansatz, the NRS and Tsai exclusion in $L^3$ and under local energy bounds) and forward (the Jia-Sverak construction and its link to the non-uniqueness program). This is the best textbook home for Architecture 4's self-similar strand.

Criticality placement: the book is organized along the scaling axis. The mild-solution chapters live at the **critical** line ($L^3$, $\dot H^{1/2}$, $a=0$, small data); the weak-solution and partial-regularity chapters run on the **supercritical** energy ($a=-1/2$); the self-similar chapters are explicitly about objects invariant under the scaling, so criticality is the organizing variable throughout. Against the controls: (A) the 2D/3D divide is stated where the strong-solution theory parts; (B) foregrounded, the small-data-critical vs large-data-supercritical split is the spine; (C) viscosity is essential to the self-similar exclusion, and the book makes the contrast with the inviscid ansatz visible.

Gives: a current, proof-complete graduate route that uniquely includes the self-similar theory. Does not give: the convex-integration boundary (see Bedrossian-Vicol) or the deepest backward-uniqueness machinery (see Seregin). The natural co-text for the NRS, Fujita-Kato, and CKN dossiers and for Direction 04.

### 2. Bedrossian and Vicol, "The Mathematical Analysis of the Incompressible Euler and Navier-Stokes Equations: An Introduction" (2022)

J. Bedrossian, V. Vicol, *The Mathematical Analysis of the Incompressible Euler and Navier-Stokes Equations: An Introduction*, Graduate Studies in Mathematics 225, American Mathematical Society (2022). ISBN 978-1-4704-7078-4.

> The most recent graduate text, and the only textbook that carries a reader from the classical theory all the way to the **convex-integration non-uniqueness** results (Architecture 5). Co-written by Vlad Vicol, an author of the Buckmaster-Vicol NS non-uniqueness theorem. It treats Euler and Navier-Stokes side by side, develops the local and conditional theory, and then gives a textbook account of the differential-inclusion / convex-integration method and intermittency. It is the bridge from the eight-book classical map to the post-2018 frontier that no older text covers.

What it is the best reference for: a unified Euler/NS development of local well-posedness and the energy/enstrophy structure; the vorticity formulation and the 2D global theory; the conditional criteria; and then the **convex-integration machinery** (the Nash-Kuiper lineage, building blocks, the role of intermittency in reaching the viscous NS equation) presented at textbook granularity. It is the place to learn why Architecture 5 sits partly outside the regularity question.

Criticality placement: the classical chapters track the same supercritical-energy / critical-target split as every NS text. The convex-integration chapters live **below** every coercive norm, at regularity $C_t H^\beta_x$ with $\beta$ small (sub-Onsager, sub-Leray-Hopf), which is where flexibility replaces rigidity. Against the controls: (A) the 2D theory is the rigid backdrop the flexible constructions deliberately avoid; (B) the non-uniqueness solutions sit beneath the energy class, illustrating from below why the supercritical energy is the floor of the rigid theory; (C) Euler/NS side by side makes the role of $\nu$ explicit, and the intermittent constructions are exactly the adaptation needed to reach $\nu>0$.

Gives: the only textbook path to the convex-integration boundary, plus a clean unified classical core. Does not give: the encyclopedic critical-space depth of Lemarie-Rieusset or the partial-regularity detail of Seregin. The home text for Direction 05 and the co-text for the Isett, Buckmaster-Vicol, and Albritton-Brue-Colombo dossiers.

### 3. Chemin, "Perfect Incompressible Fluids" (1998)

J.-Y. Chemin, *Perfect Incompressible Fluids*, Oxford Lecture Series in Mathematics and its Applications 14, Oxford University Press (1998); translated from *Fluides parfaits incompressibles*, Asterisque 230 (1995).

> The reference for the **inviscid** (Euler) theory through the paradifferential lens: local well-posedness in Holder and Besov spaces, the 2D global theory with Yudovich-class data, and the logarithmic estimates that govern how Euler regularity can degrade. It is the $\nu=0$ contrast case that makes control (C) precise: everything that viscosity buys is, in this book, absent, so the book shows exactly what the parabolic smoothing in Navier-Stokes is compensating for.

What it is the best reference for: local existence for Euler in $C^{1,\alpha}$ and Besov spaces via paradifferential calculus; the 2D global theory and the propagation of vortex-patch regularity (the Chemin persistence-of-striated-regularity theorem); and the log-Lipschitz / log-loss estimates that quantify the failure of the inviscid flow to be uniformly smooth. It pairs with Bahouri-Chemin-Danchin (same paradifferential toolkit, viscous side) and Majda-Bertozzi (vorticity, both sides).

Criticality placement: Euler has the same scaling as NS but no dissipation, so the natural spaces are the regularity-critical Holder/Besov classes ($C^{1,\alpha}$, $\dot B^{s}_{p,r}$ at the Lipschitz threshold), not the Lebesgue-critical $L^3$. The book lives at the **borderline-Lipschitz** regularity where 3D stretching can act unimpeded. Against the controls: (A) the 2D global theory is a centerpiece, by exactly the absence of stretching; (B) less central, there is no energy-vs-critical gap of the viscous kind because there is no dissipative gain; (C) this is the pure statement of "no viscosity," the contrast that Elgindi 2021 and the Chen-Hou program realize as actual blow-up.

Gives: the definitive paradifferential Euler local theory and the 2D vortex-patch results. Does not give: any viscous regularity result, the inviscid blow-up itself is not constructed here (see Elgindi, Chen-Hou). The co-text for Direction 04 and the Elgindi/Luo-Hou dossiers.

### 4. Marchioro and Pulvirenti, "Mathematical Theory of Incompressible Nonviscous Fluids" (1994)

C. Marchioro, M. Pulvirenti, *Mathematical Theory of Incompressible Nonviscous Fluids*, Applied Mathematical Sciences 96, Springer (1994). ISBN 0-387-94044-8.

> The reference for **2D Euler vortex dynamics**: global existence and uniqueness for $L^\infty$ and measure vorticity, the point-vortex system, vortex-sheet and weak-solution questions, and the mean-field / statistical-mechanics picture of 2D turbulence. It is a deep articulation of control (A) on the inviscid side: 2D stays well-behaved because vorticity is transported (no stretching), and this book is where that mechanism is developed to its sharp conclusions.

What it is the best reference for: Yudovich uniqueness for 2D Euler with bounded vorticity; the point-vortex approximation and its rigorous justification; weak solutions with vortex-sheet data and the surrounding subtleties; and the statistical (Onsager point-vortex, mean-field) theory of 2D turbulence. It complements Majda-Bertozzi (which carries the 3D stretching story) by being the deep 2D-inviscid reference.

Criticality placement: 2D vorticity is **critical-and-conserved** in $L^p$ for every $p$ (transport along a measure-preserving flow), which is the structural reason the 2D theory closes. The book is the inviscid image of the project's 2D control. Against the controls: (A) this is a primary reference for A, the absence of stretching is the whole engine; (B) the supercriticality gap does not arise in 2D, which is precisely the point; (C) inviscid, so it is the $\nu=0$ baseline whose 2D good behavior survives adding viscosity.

Gives: the complete 2D Euler / vortex-dynamics theory and the statistical-mechanics bridge. Does not give: any 3D regularity content or viscous theory. Background for Direction 02 (vorticity geometry) and the 2D control's inviscid face.

### 5. Cannone, "Ondelettes, paraproduits et Navier-Stokes" (1995)

M. Cannone, *Ondelettes, paraproduits et Navier-Stokes*, Diderot Editeur, Paris (1995). (English-language successor: M. Cannone, "Harmonic analysis tools for solving the incompressible Navier-Stokes equations," in *Handbook of Mathematical Fluid Dynamics*, Vol. 3, North-Holland (2004), 161-244.)

> The book that launched the **wavelet / Besov critical-space** program and the modern theory of self-similar solutions from homogeneous data. Cannone introduced the use of paraproducts and Littlewood-Paley adapted norms to solve Navier-Stokes for data in critical Besov spaces larger than $L^3$, and to construct forward self-similar solutions. It is the historical and conceptual root of the Cannone-Meyer-Planchon critical-Besov result already in the bibliography, and a more readable entry than the encyclopedic Lemarie-Rieusset for the harmonic-analysis-of-NS viewpoint.

What it is the best reference for: the construction of mild solutions in critical Besov spaces $\dot B^{-1+3/q}_{q,\infty}$ via adapted norms; the precise role of paraproducts in taming the NS bilinear term at low regularity; and forward self-similar solutions from $(-1)$-homogeneous initial data. The English Handbook chapter is the practical modern reference for the same material.

Criticality placement: pure **critical line** ($a=0$). Every space the book features is scale invariant; the contribution is enlarging the critical class beyond $L^3$ up toward $\mathrm{BMO}^{-1}$ while keeping the fixed point closed for small data. Against the controls: (B) engaged from the critical side, small data only, the same positive-half-of-the-gap story as Bahouri-Chemin-Danchin; (A), (C) not foregrounded. Co-text for Direction 01/03 and the Cannone-Meyer-Planchon and Koch-Tataru material.

### 6. Lemarie-Rieusset, "Recent Developments in the Navier-Stokes Problem" (2002)

P. G. Lemarie-Rieusset, *Recent Developments in the Navier-Stokes Problem*, Chapman & Hall/CRC Research Notes in Mathematics 431 (2002). ISBN 1-58488-220-4.

> The direct predecessor of the project's main encyclopedic reference, *The Navier-Stokes Problem in the 21st Century* (see [`lemarie_rieusset_book.md`](lemarie_rieusset_book.md)). It is the book that consolidated the mild-solution / critical-space theory through 2001, including a careful treatment of the Koch-Tataru $\mathrm{BMO}^{-1}$ result and the uniqueness theory in critical spaces. Listed here because it is frequently cited in its own right and is sometimes the cleaner entry to a specific argument that the larger 2016/2024 book generalizes.

What it is the best reference for: the unified mild-solution theory across the critical scale; the original book-form account of well-posedness up to $\mathrm{BMO}^{-1}$; and the critical-space uniqueness results. Criticality placement and controls are as for its successor: it lives on the **critical** line for the well-posedness theory and on the **supercritical** energy for the weak-solution theory, engaging control (B) from both sides, with (A)/(C) present but not central. Use the 21st-Century dossier for the full treatment; reach for this when a citation points specifically to the 2002 edition.

### 7. Boyer and Fabrie, "Mathematical Tools for the Study of the Incompressible Navier-Stokes Equations and Related Models" (2013)

F. Boyer, P. Fabrie, *Mathematical Tools for the Study of the Incompressible Navier-Stokes Equations and Related Models*, Applied Mathematical Sciences 183, Springer (2013). ISBN 978-1-4614-5974-3.

> The modern function-space toolkit, assembled specifically for fluid PDE. Where Adams-Fournier is the general Sobolev reference, this book collects exactly the tools the Navier-Stokes analyst needs: trace theorems, the div/curl and Helmholtz-Weyl decompositions, the surjectivity of the divergence (the Bogovskii operator and the $\inf$-$\sup$ / LBB condition), and the Stokes problem, all stated with the hypotheses fluid problems actually use. It serves Architecture 1 as the substrate beneath the weak-solution theory.

What it is the best reference for: the **Bogovskii operator** and the right-inverse of the divergence (essential for handling the pressure and for constructing test fields); trace and lifting theorems on Lipschitz domains; the Helmholtz decomposition and the Leray projector with careful domain hypotheses; and the steady and unsteady Stokes problem with the $\inf$-$\sup$ condition that also underwrites mixed finite elements. It pairs with Galdi (steady/elliptic) and Sohr ($L^q$ semigroup) as the function-space foundation.

Criticality placement: a substrate reference, the tools are scaling-covariant building blocks rather than results at a fixed criticality. It supplies the lemmas (Helmholtz, Bogovskii, trace) that the **supercritical** energy theory and the **critical** mild-solution theory both consume. Against the controls: (B) it is the toolbox under the energy theory; (A)/(C) not its subject. Background for Architecture 1 and the function-space foundations; a natural source for VERIFIER lemmas (the Helmholtz decomposition, the divergence right-inverse).

### 8. P.-L. Lions, "Mathematical Topics in Fluid Mechanics, Vol. 1: Incompressible Models" (1996)

P.-L. Lions, *Mathematical Topics in Fluid Mechanics, Volume 1: Incompressible Models*, Oxford Lecture Series in Mathematics and its Applications 3, Clarendon Press (1996). ISBN 0-19-851487-5.

> The reference for **compactness methods** in incompressible fluid PDE: the structure of weak solutions, the role of compensated compactness and the div-curl lemma, and the renormalized-solution viewpoint (carried over from Lions' transport-equation theory with DiPerna). It sharpens the boundary of what the weak-solution concept controls, which is exactly the question Architecture 5 later answers from the flexible side.

What it is the best reference for: refined existence and stability of Leray-Hopf weak solutions via compactness; the analysis of the nonlinear term under weak convergence (where compensated compactness and concentration phenomena enter); and the renormalization framework that clarifies which weak solutions are "good." It is dense and research-level. Criticality placement: the analysis runs on the **supercritical** energy ($a=-1/2$) and is precisely a study of how much the energy compactness does and does not control, which is control (B) examined at the level of weak convergence. Against the controls: (B) central; (A)/(C) present but not the focus. Background for Architecture 1 and a conceptual precursor to the non-uniqueness boundary of Architecture 5 (it asks, from the rigid side, the question convex integration answers from the flexible side).

### 9. Seregin, "Lecture Notes on Regularity Theory for the Navier-Stokes Equations" (2014)

G. Seregin, *Lecture Notes on Regularity Theory for the Navier-Stokes Equations*, World Scientific (2014). ISBN 978-981-4623-40-7.

> The cleanest self-contained route to the **partial-regularity and $L^3$-endpoint machinery**: suitable weak solutions, the local energy inequality, the $\varepsilon$-regularity theorem (CKN), and the backward-uniqueness / unique-continuation apparatus behind Escauriaza-Seregin-Sverak, all with full proofs, by one of the authors of ESS. It is the book to open when the project needs the proof of an $\varepsilon$-regularity or backward-uniqueness step at the granularity a formalization can track.

What it is the best reference for: the definition and construction of **suitable weak solutions** and the local energy inequality; the CKN $\varepsilon$-regularity theorem with a modern proof; the **backward uniqueness and unique continuation** for parabolic operators that drive the ESS $L^\infty_t L^3_x$ result; and the mild-solution and Stokes-system prerequisites. It is the deepest single source for the partial-regularity strand, complementing Robinson-Rodrigo-Sadowski (which states these with proofs but in less depth) and the CKN/ESS dossiers.

Criticality placement: the $\varepsilon$-regularity theory is a **critical-scaling** local statement run over the **supercritical** energy budget, exactly the CKN structure. The ESS endpoint is at the **critical** $L^3$ ($a=0$). The book is the technical home of the critical-local-mechanism-over-supercritical-budget picture. Against the controls: (B) foregrounded, the partial-regularity theory is the sharpest thing the supercritical budget yields; (C) viscosity is essential (parabolic backward uniqueness has no inviscid analog); (A) not central. The primary co-text for the CKN, Lin-Vasseur, and ESS dossiers, and a prime source of VERIFIER targets.

### 10. Foias, Manley, Rosa, Temam, "Navier-Stokes Equations and Turbulence" (2001)

C. Foias, O. Manley, R. Rosa, R. Temam, *Navier-Stokes Equations and Turbulence*, Encyclopedia of Mathematics and its Applications 83, Cambridge University Press (2001). ISBN 0-521-36032-3.

> The rigorous bridge from the Navier-Stokes theory to **turbulence**: the energy cascade made precise, the global attractor and its dimension, time-averaged and stationary statistical solutions, and the Kolmogorov-law heuristics framed against what is actually provable. It deepens the dynamical-systems side of Constantin-Foias and supplies the rigorous backdrop for the project's `energy_spectrum/` experiment.

What it is the best reference for: statistical solutions (time-average and stationary) and the mathematically precise version of ensemble averaging; the attractor-dimension and degrees-of-freedom estimates in turbulence language; and the rigorous status of the energy-dissipation law and the cascade. It is where the project's energy-spectrum diagnostics get their theoretical frame.

Criticality placement: the rigorous results run on the **supercritical** energy and the (2D-)critical enstrophy; the turbulence heuristics (Kolmogorov $-5/3$) are dimensional-analysis statements the rigorous theory can bound but not derive in 3D, which is the supercriticality gap wearing turbulence clothing. Against the controls: (A) the rigorous attractor theory is complete in 2D and conditional in 3D, the same divide as Constantin-Foias; (B) central, the cascade is the physical face of supercriticality; (C) the dissipation rate and $\nu$-dependence are explicit. Background for the energy-spectrum experiment and the supercriticality framing of Direction 03.

---

## Part II. The analysis substrate

These are not Navier-Stokes books. They are the harmonic analysis, function-space, interpolation, and general-PDE references that the critical-space program (Architecture 3) and the partial-regularity theory (Architecture 1) are built on. A reader who finds the harmonic analysis in Bahouri-Chemin-Danchin or Lemarie-Rieusset opaque should pull the relevant one of these.

### 11. Grafakos, "Classical Fourier Analysis" and "Modern Fourier Analysis" (2014)

L. Grafakos, *Classical Fourier Analysis* (GTM 249) and *Modern Fourier Analysis* (GTM 250), 3rd ed., Springer (2014).

> The standard modern two-volume foundation for the harmonic analysis that the whole critical-space program rests on: Calderon-Zygmund operators, the Hardy-Littlewood maximal function, Littlewood-Paley theory, $H^1$ and $\mathrm{BMO}$, and interpolation. When the boundedness of the Leray projector on $L^q$, the Riesz transforms in the pressure, or the Littlewood-Paley characterization of a Besov norm is used as a black box, this is where the proof lives. Serves Architecture 3 (and the $L^q$ substrate of Architecture 1). Criticality placement: it provides the operators and inequalities; $\mathrm{BMO}$ and $H^1$ here are the duality endpoints that make $\mathrm{BMO}^{-1}$ (the largest **critical** NS space) natural. Engages control (B) only as substrate.

### 12. Stein, "Singular Integrals and Differentiability Properties of Functions" (1970); "Harmonic Analysis" (1993)

E. M. Stein, *Singular Integrals and Differentiability Properties of Functions*, Princeton Mathematical Series 30, Princeton University Press (1970); *Harmonic Analysis: Real-Variable Methods, Orthogonality, and Oscillatory Integrals*, Princeton Mathematical Series 43 (1993).

> The classic source for **Calderon-Zygmund singular integrals**, Riesz transforms, Sobolev and potential spaces, and (in the 1993 volume) $\mathrm{BMO}$, Hardy spaces, and Littlewood-Paley square functions. The Leray-Helmholtz projector $P = I - \nabla\Delta^{-1}\nabla\cdot$ is a matrix of Riesz transforms, so its $L^q$-boundedness, the workhorse of the entire $L^q$ Navier-Stokes theory, is a Calderon-Zygmund theorem from this book. Serves Architectures 1 and 3 as the deepest substrate; engages control (B) only as a tool.

### 13. Triebel, "Theory of Function Spaces" I, II, III (1983, 1992, 2006)

H. Triebel, *Theory of Function Spaces*, Monographs in Mathematics 78 (1983); *II*, Monographs 84 (1992); *III*, Monographs 100 (2006), Birkhauser.

> The definitive treatment of the **Besov $B^s_{p,q}$ and Triebel-Lizorkin $F^s_{p,q}$ scales** that index every critical and subcritical NS space. When a regularity criterion or a well-posedness result is stated in a Besov space, the embedding, interpolation, and trace properties used come from here. Serves Architecture 3. Criticality placement: it is the atlas of the spaces the bookkeeper classifies; the NS-critical members ($\dot H^{1/2}=\dot B^{1/2}_{2,2}$, $\dot B^{-1+3/q}_{q,r}$, the $\mathrm{BMO}^{-1}=\dot F^{-1}_{\infty,2}$ identification) are all located on its scale. Substrate for control (B).

### 14. Bergh-Lofstrom, "Interpolation Spaces: An Introduction" (1976)

J. Bergh, J. Lofstrom, *Interpolation Spaces: An Introduction*, Grundlehren der mathematischen Wissenschaften 223, Springer (1976). ISBN 3-540-07875-4.

> The compact standard reference for **real and complex interpolation** (the $K$-method, $J$-method, the complex method), which is the machinery that defines Besov spaces as interpolation spaces and that underlies almost every "interpolate between the energy bound and a higher norm" step in the theory. The ubiquitous Ladyzhenskaya and Gagliardo-Nirenberg inequalities are interpolation statements; this is where the abstract reason they hold lives. Serves Architecture 3 and the energy-method interpolation of Architecture 1. Substrate for control (B).

### 15. Adams-Fournier, "Sobolev Spaces" (2003); Brezis (2011)

R. A. Adams, J. J. F. Fournier, *Sobolev Spaces*, 2nd ed., Pure and Applied Mathematics 140, Academic Press (2003); H. Brezis, *Functional Analysis, Sobolev Spaces and Partial Differential Equations*, Universitext, Springer (2011).

> The standard references for **Sobolev spaces and their embeddings** ($W^{k,p}$, fractional $W^{s,p}$, the Sobolev, Rellich-Kondrachov, and Gagliardo-Nirenberg-Sobolev inequalities). Every a priori estimate in the project, from the energy inequality to the ladder of higher norms, is read in these spaces, and the exact embedding exponents are what the criticality bookkeeper tracks. Brezis adds the clean functional-analysis prerequisites (weak convergence, compactness) the weak-solution theory relies on. Substrate for all architectures; the home of the inequalities that the supercriticality gap is a statement about.

### 16. Evans, "Partial Differential Equations" (2010)

L. C. Evans, *Partial Differential Equations*, 2nd ed., Graduate Studies in Mathematics 19, American Mathematical Society (2010). ISBN 978-0-8218-4974-3.

> The standard first graduate PDE text. Its chapters on Sobolev spaces, second-order parabolic equations (existence via Galerkin, energy estimates, regularity), and the heat equation are the exact prerequisites for the Navier-Stokes weak-solution and parabolic-smoothing theory. It also contains a self-contained section on the Euler and Navier-Stokes equations. The right place to consolidate the parabolic-PDE background before Robinson-Rodrigo-Sadowski. Serves Architecture 1 as prerequisite; control (B) as the energy-method substrate.

### 17. Taylor, "Partial Differential Equations III: Nonlinear Equations" (2011)

M. E. Taylor, *Partial Differential Equations III: Nonlinear Equations*, 2nd ed., Applied Mathematical Sciences 117, Springer (2011). ISBN 978-1-4419-7048-0.

> A graduate PDE treatise whose third volume develops **paradifferential calculus and applies it to Euler and Navier-Stokes** in one coherent place (Chapter 17). It is a useful bridge between the pure-harmonic-analysis references (Grafakos, Stein, Triebel) and the fluid texts (Bahouri-Chemin-Danchin, Chemin): it shows the paradifferential machinery being built and then used on the equations of interest, with both the inviscid and viscous cases treated. Serves Architectures 1, 2, 3; engages controls A, B, C as it carries both Euler and NS.

---

## Part III. Books tied to the project's experimental threads

These connect to the computational threads in `experiments/` and to the rigorous-numerics frontier the project tracks (the Chen-Hou Euler blow-up program). They are not regularity-proof references; they are the rigorous backing for what the experiments compute and for how the singularity side is being settled by computer-assisted proof.

### 18. Frisch, "Turbulence: The Legacy of A. N. Kolmogorov" (1995)

U. Frisch, *Turbulence: The Legacy of A. N. Kolmogorov*, Cambridge University Press (1995). ISBN 0-521-45713-0.

> The standard rigorous-minded account of the **turbulence phenomenology** that frames the energy cascade, the Kolmogorov $-5/3$ spectrum, the dissipation anomaly, and intermittency. It is the conceptual background for the project's `energy_spectrum/` experiment and, importantly, for the **Onsager** $1/3$ regularity threshold that the convex-integration results (Architecture 5) realize rigorously: the anomalous dissipation Frisch describes phenomenologically is exactly what Isett and Buckmaster-Vicol construct. Criticality placement: the cascade is the physical image of supercriticality (energy flux to small scales that the energy norm cannot see); the $1/3$ Onsager exponent is the regularity-critical threshold for energy conservation. Engages controls B (the cascade is supercriticality) and C (the dissipation anomaly is the $\nu\to 0$ limit). Background for the energy-spectrum experiment and Direction 05.

### 19. Robinson, "Infinite-Dimensional Dynamical Systems" (2001)

J. C. Robinson, *Infinite-Dimensional Dynamical Systems: An Introduction to Dissipative Parabolic PDEs and the Theory of Global Attractors*, Cambridge Texts in Applied Mathematics, Cambridge University Press (2001). ISBN 0-521-63564-3.

> The clean modern textbook for the **global-attractor theory** of dissipative PDEs, with Navier-Stokes as a running example. It develops attractor existence, finite Hausdorff/fractal dimension, and inertial manifolds at a level more accessible than Constantin-Foias or Temam's dynamical-systems monograph, and it states plainly that the 2D attractor theory is unconditional while the 3D theory is conditional on regularity. Useful as the readable on-ramp to the dynamical-systems coordinate that Constantin-Foias and Foias-Manley-Rosa-Temam use. Criticality placement: the 2D attractor is finite-dimensional because the enstrophy is a **critical, non-increasing** bound; the 3D attractor is conditional because the energy is **supercritical**. Engages controls A (the 2D/3D split is explicit) and B. (Companion at research depth: R. Temam, *Infinite-Dimensional Dynamical Systems in Mechanics and Physics*, 2nd ed., Applied Math. Sciences 68, Springer, 1997.)

### 20. Canuto, Hussaini, Quarteroni, Zang, "Spectral Methods" (2006, 2007)

C. Canuto, M. Y. Hussaini, A. Quarteroni, T. A. Zang, *Spectral Methods: Fundamentals in Single Domains* (2006) and *Spectral Methods: Evolution to Complex Geometries and Applications to Fluid Dynamics* (2007), Scientific Computation, Springer.

> The definitive reference for the **pseudo-spectral / Fourier-collocation methods** the project's `taylor_green/` and `energy_spectrum/` experiments are built on: Fourier and Chebyshev approximation theory, aliasing and the 2/3 dealiasing rule, time-stepping for the incompressible equations, and the convergence theory that makes a $32^3$ or $48^3$ spectral DNS a legitimate approximation. It is the numerical-analysis backing for the project's solver interface, the analog on the computational side of what Temam's numerical half provides on the Galerkin side. Engages control (C): the viscous dissipation is what makes the spectral truncation converge. (Accessible companions: J. P. Boyd, *Chebyshev and Fourier Spectral Methods*, 2nd ed., Dover (2001); L. N. Trefethen, *Spectral Methods in MATLAB*, SIAM (2000).) Background for the DNS experimental thread, not for the regularity proof.

### 21. Nakao, Plum, Watanabe, "Numerical Verification Methods and Computer-Assisted Proofs for Partial Differential Equations" (2019)

M. T. Nakao, M. Plum, Y. Watanabe, *Numerical Verification Methods and Computer-Assisted Proofs for Partial Differential Equations*, Springer Series in Computational Mathematics 53 (2019). ISBN 978-981-13-7668-9.

> The reference for the **rigorous-numerics machinery** behind the modern blow-up frontier: interval arithmetic, validated fixed-point theorems (Newton-Kantorovich-type), and the verification of solutions to nonlinear PDEs with mathematical certainty. This is the method class that the **Chen-Hou** computer-assisted proof of finite-time 3D Euler / 2D Boussinesq blow-up (already in the project's Architecture 4 dossiers) is an instance of: a near-self-similar profile is constructed numerically and its nonlinear stability is then *proved* by validated computation. Engages control (C) at the inviscid frontier: it is how the viscosity-essential thesis is being tested, by establishing that the inviscid equation genuinely blows up. (Companions: W. Tucker, *Validated Numerics*, Princeton (2011); R. E. Moore, R. B. Kearfott, M. J. Cloud, *Introduction to Interval Analysis*, SIAM (2009).) The reference layer under the Luo-Hou / Chen-Hou dossier; deserves its own dossier as the rigorous-numerics thread matures.

---

## Cross-cutting summary: which further book for which job

| If you need ... | Open ... |
|---|---|
| A current graduate text with the self-similar theory | Tsai (2018) |
| The convex-integration boundary in a textbook | Bedrossian-Vicol (2022) |
| The inviscid (Euler) paradifferential local theory | Chemin (1998) |
| 2D Euler vortex dynamics and point vortices | Marchioro-Pulvirenti (1994) |
| The origin of the wavelet/Besov self-similar program | Cannone (1995) |
| Suitable weak solutions, $\varepsilon$-regularity, ESS with full proofs | Seregin (2014) |
| The div right-inverse (Bogovskii), traces, Helmholtz | Boyer-Fabrie (2013) |
| Compactness / renormalized weak-solution structure | P.-L. Lions (1996) |
| The rigorous turbulence / cascade backdrop | Foias-Manley-Rosa-Temam (2001), Frisch (1995) |
| Calderon-Zygmund, Riesz transforms, the Leray projector's boundedness | Stein (1970/1993), Grafakos (2014) |
| The Besov/Triebel-Lizorkin scale and interpolation | Triebel (1983-2006), Bergh-Lofstrom (1976) |
| Sobolev embeddings and the inequalities behind the a priori estimates | Adams-Fournier (2003), Brezis (2011) |
| Parabolic PDE prerequisites; paradifferential NS/Euler in one text | Evans (2010), Taylor III (2011) |
| The attractor theory as a readable on-ramp | Robinson (2001) |
| Numerical-analysis backing for the pseudo-spectral DNS | Canuto-Hussaini-Quarteroni-Zang (2006/2007) |
| The rigorous-numerics method behind Chen-Hou blow-up | Nakao-Plum-Watanabe (2019) |

## What this enables / what remains open

**Enables.**
- Three additions close real gaps the eight-book map left open: **Tsai (2018)** supplies a current graduate text with the self-similar theory; **Bedrossian-Vicol (2022)** is the only textbook reaching the convex-integration boundary (Architecture 5); **Seregin (2014)** is the deepest proof-complete source for partial regularity and the ESS backward-uniqueness machinery, a prime VERIFIER quarry.
- The analysis substrate (Part II) gives BUILDER and VERIFIER the proof of every harmonic-analysis or function-space step the fluid texts cite as a black box (the Leray projector's $L^q$-boundedness in Stein, the Besov scale in Triebel, the interpolation inequalities in Bergh-Lofstrom).
- The experiment-adjacent books (Part III) put the project's computational threads on a rigorous footing: Canuto et al. for the DNS convergence theory, Frisch and Foias-Manley-Rosa-Temam for the energy-spectrum interpretation, and Nakao-Plum-Watanabe for the rigorous-numerics method that the Chen-Hou blow-up proof instantiates.
- Read together with the eight-book map, the same boundary appears once more from new angles: the inviscid books (Chemin, Marchioro-Pulvirenti) close the 2D theory by the absence of stretching (control A) and exhibit, with Frisch and the rigorous-numerics literature, exactly the inviscid blow-up that viscosity must beat (control C).

**Remains open (each book's silence).**
- No book here closes 3D large-data regularity. Bedrossian-Vicol reaches the non-uniqueness boundary but that boundary is below the energy class; Tsai and Seregin reach the sharpest conditional and partial-regularity results but those sit at the critical line the supercritical energy cannot reach.
- The rigorous-numerics thread (Nakao-Plum-Watanabe, the Chen-Hou program) settles the *inviscid* singularity question and is silent on Navier-Stokes; whether viscosity defeats the same mechanism is the open question, and the validated-computation method has not closed the viscous case.
- A genuinely critical *large-data* a priori bound is in none of these books because it does not exist yet. As with the eight-book map, these references say which partial ingredient lives where; assembling them across the supercriticality gap is the open problem.

## References

- T.-P. Tsai, *Lectures on Navier-Stokes Equations*, Graduate Studies in Mathematics 192, AMS (2018).
- J. Bedrossian, V. Vicol, *The Mathematical Analysis of the Incompressible Euler and Navier-Stokes Equations: An Introduction*, Graduate Studies in Mathematics 225, AMS (2022).
- J.-Y. Chemin, *Perfect Incompressible Fluids*, Oxford Lecture Series in Mathematics and its Applications 14, Oxford University Press (1998); orig. *Fluides parfaits incompressibles*, Asterisque 230 (1995).
- C. Marchioro, M. Pulvirenti, *Mathematical Theory of Incompressible Nonviscous Fluids*, Applied Mathematical Sciences 96, Springer (1994).
- M. Cannone, *Ondelettes, paraproduits et Navier-Stokes*, Diderot Editeur (1995); and "Harmonic analysis tools for solving the incompressible Navier-Stokes equations," *Handbook of Mathematical Fluid Dynamics*, Vol. 3, North-Holland (2004), 161-244.
- P. G. Lemarie-Rieusset, *Recent Developments in the Navier-Stokes Problem*, Chapman & Hall/CRC Research Notes in Mathematics 431 (2002).
- F. Boyer, P. Fabrie, *Mathematical Tools for the Study of the Incompressible Navier-Stokes Equations and Related Models*, Applied Mathematical Sciences 183, Springer (2013).
- P.-L. Lions, *Mathematical Topics in Fluid Mechanics, Vol. 1: Incompressible Models*, Oxford Lecture Series in Mathematics and its Applications 3, Clarendon Press (1996).
- G. Seregin, *Lecture Notes on Regularity Theory for the Navier-Stokes Equations*, World Scientific (2014).
- C. Foias, O. Manley, R. Rosa, R. Temam, *Navier-Stokes Equations and Turbulence*, Encyclopedia of Mathematics and its Applications 83, Cambridge University Press (2001).
- L. Grafakos, *Classical Fourier Analysis* (GTM 249), *Modern Fourier Analysis* (GTM 250), 3rd ed., Springer (2014).
- E. M. Stein, *Singular Integrals and Differentiability Properties of Functions*, Princeton (1970); *Harmonic Analysis*, Princeton (1993).
- H. Triebel, *Theory of Function Spaces* I, II, III, Birkhauser (1983, 1992, 2006).
- J. Bergh, J. Lofstrom, *Interpolation Spaces: An Introduction*, Grundlehren 223, Springer (1976).
- R. A. Adams, J. J. F. Fournier, *Sobolev Spaces*, 2nd ed., Academic Press (2003); H. Brezis, *Functional Analysis, Sobolev Spaces and Partial Differential Equations*, Springer (2011).
- L. C. Evans, *Partial Differential Equations*, 2nd ed., Graduate Studies in Mathematics 19, AMS (2010).
- M. E. Taylor, *Partial Differential Equations III: Nonlinear Equations*, 2nd ed., Applied Mathematical Sciences 117, Springer (2011).
- U. Frisch, *Turbulence: The Legacy of A. N. Kolmogorov*, Cambridge University Press (1995).
- J. C. Robinson, *Infinite-Dimensional Dynamical Systems*, Cambridge Texts in Applied Mathematics (2001); R. Temam, *Infinite-Dimensional Dynamical Systems in Mechanics and Physics*, 2nd ed., Springer (1997).
- C. Canuto, M. Y. Hussaini, A. Quarteroni, T. A. Zang, *Spectral Methods*, Springer (2006, 2007); J. P. Boyd, *Chebyshev and Fourier Spectral Methods*, Dover (2001); L. N. Trefethen, *Spectral Methods in MATLAB*, SIAM (2000).
- M. T. Nakao, M. Plum, Y. Watanabe, *Numerical Verification Methods and Computer-Assisted Proofs for PDEs*, Springer (2019); W. Tucker, *Validated Numerics*, Princeton (2011); R. E. Moore, R. B. Kearfott, M. J. Cloud, *Introduction to Interval Analysis*, SIAM (2009).

## Cross-links

- The eight standard graduate references, mapped in depth: [`textbooks_map.md`](textbooks_map.md). The encyclopedic backbone, full dossier: [`lemarie_rieusset_book.md`](lemarie_rieusset_book.md).
- Direction 01 (critical continuation), served here by Tsai, Cannone, and the analysis substrate: [`../research_directions/01_critical_continuation_criteria.md`](../research_directions/01_critical_continuation_criteria.md).
- Direction 02 (vorticity geometry), served by Marchioro-Pulvirenti and Chemin: [`../research_directions/02_vorticity_geometry.md`](../research_directions/02_vorticity_geometry.md).
- Direction 03 (the supercriticality gap), served by Foias-Manley-Rosa-Temam, Robinson, Frisch: [`../research_directions/03_supercriticality_gap.md`](../research_directions/03_supercriticality_gap.md).
- Direction 04 (blow-up and barriers), served by Tsai (self-similar), Chemin, and Nakao-Plum-Watanabe (rigorous numerics): [`../research_directions/04_blowup_and_barriers.md`](../research_directions/04_blowup_and_barriers.md).
- Direction 05 (convex integration boundary), served by Bedrossian-Vicol and P.-L. Lions (from the rigid side): [`../research_directions/05_convex_integration_boundary.md`](../research_directions/05_convex_integration_boundary.md).
- Sibling dossiers whose proofs these books carry: NRS/Tsai self-similar exclusion [`./necas_ruzicka_sverak_1996.md`](./necas_ruzicka_sverak_1996.md); CKN and its modern proofs [`./caffarelli_kohn_nirenberg_1982.md`](./caffarelli_kohn_nirenberg_1982.md), [`./lin_vasseur_partial_regularity.md`](./lin_vasseur_partial_regularity.md); ESS backward uniqueness [`./escauriaza_seregin_sverak_2003.md`](./escauriaza_seregin_sverak_2003.md); the convex-integration boundary [`./isett_2018.md`](./isett_2018.md), [`./buckmaster_vicol_2019.md`](./buckmaster_vicol_2019.md); the inviscid blow-up [`./elgindi_2021.md`](./elgindi_2021.md), [`./luo_hou_2014.md`](./luo_hou_2014.md).
- The full bibliographic index: [`../../../references/README.md`](../../../references/README.md). The curated entry path: [`../../../references/reading_guide.md`](../../../references/reading_guide.md). The criticality bookkeeper: `experiments/_shared/criticality.py`.
