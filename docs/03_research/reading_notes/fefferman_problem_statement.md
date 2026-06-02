# Reading notes: Fefferman, the official Clay problem statement (2000)

Charles Fefferman, "Existence and smoothness of the Navier-Stokes equation," official problem description for the Clay Mathematics Institute Millennium Prize.

## What it fixes

The precise target. The 3D incompressible Navier-Stokes equations with viscosity $\nu > 0$,

$$\partial_t u + (u\cdot\nabla)u = -\nabla p + \nu\Delta u, \qquad \nabla\cdot u = 0, \qquad u(\cdot,0)=u_0,$$

with $u_0$ smooth, divergence-free, and rapidly decreasing (on $\mathbb{R}^3$) or smooth and periodic (on $\mathbb{T}^3$), and with bounded energy.

Fefferman offers four statements; a prize is awarded for proving any one:

- (A) Existence and smoothness on $\mathbb{R}^3$: global smooth finite-energy solutions exist for all smooth divergence-free $u_0$.
- (B) Existence and smoothness on $\mathbb{T}^3$: the periodic analog.
- (C) Breakdown on $\mathbb{R}^3$: there exist smooth $u_0$ (and forcing) for which no global smooth solution exists.
- (D) Breakdown on $\mathbb{T}^3$: the periodic analog.

The canonical target is (A) or (B): global existence and smoothness, no forcing.

## Structural content

The statement is careful about the function-space setting: finite energy ($u_0 \in L^2$), smoothness, and the precise decay so that the energy and the solution are well defined. It explicitly notes the known background: Leray-Hopf weak solutions exist globally, and smooth solutions exist for a short time, but global smoothness in 3D is open. It also notes that the analogous 2D problem is solved (global regularity), and frames the 3D difficulty as the gap between short-time smoothness and global weak existence.

## How it bears on the spine

This is the contract. It defines "solution" (finite energy, the energy inequality is the natural class), it names the two acceptable answers (regularity or blow-up), and it flags the two structural facts the whole repo is organized around: 2D is solved, and 3D sits between short-time smoothness and global weak existence. The supercriticality gap is the analytic content of that "between." See [`../../02_graduate/scaling_and_supercriticality.md`](../../02_graduate/scaling_and_supercriticality.md).
