# The incompressible Navier-Stokes equations

Prerequisites: vector calculus (gradient, divergence, curl, the divergence theorem), ODEs, and a first acquaintance with PDEs.

## The equations

Let $u(x, t) = (u_1, u_2, u_3)$ be the velocity of a fluid at position $x \in \mathbb{R}^3$ (or the torus $\mathbb{T}^3$) and time $t$, and let $p(x, t)$ be the pressure. The incompressible Navier-Stokes equations are

$$\partial_t u + (u \cdot \nabla) u = -\nabla p + \nu \Delta u, \qquad \nabla \cdot u = 0,$$

with viscosity $\nu > 0$, and a smooth divergence-free initial velocity $u(x, 0) = u_0(x)$ of finite energy.

Term by term:

- $\partial_t u$: the velocity is changing in time. This is what we solve for.
- $(u \cdot \nabla) u$: the **nonlinear transport** term, $\sum_j u_j \partial_j u_i$ in components. The fluid carries itself along. This term is quadratic in $u$ and is the source of all the difficulty.
- $-\nabla p$: the **pressure gradient**. Pressure is not an independent unknown with its own evolution equation; it is whatever it needs to be to keep the flow incompressible (see below).
- $\nu \Delta u$: **viscous diffusion**. The Laplacian smooths the velocity, draining energy and spreading sharp features. This is the stabilizing term.
- $\nabla \cdot u = 0$: **incompressibility**. The fluid neither compresses nor expands; the velocity field is divergence-free.

## Pressure is a Lagrange multiplier (the Leray projection)

Because $p$ has no evolution equation, it is determined by the incompressibility constraint. Take the divergence of the momentum equation and use $\nabla \cdot u = 0$:

$$-\Delta p = \nabla \cdot \big((u \cdot \nabla) u\big).$$

So $p$ is recovered from $u$ by solving a Poisson equation. Equivalently, one applies the **Leray projector** $\mathbb{P}$, the orthogonal projection onto divergence-free vector fields, to the whole equation; this eliminates the pressure entirely:

$$\partial_t u = \mathbb{P}\big[-(u \cdot \nabla) u\big] + \nu \Delta u.$$

On the torus, $\mathbb{P}$ is algebraic in Fourier space (it removes the component of each Fourier mode $\hat u(k)$ along $k$). This is exactly how the pseudo-spectral solver in `experiments/_shared/flow.py` enforces incompressibility to machine precision.

## The energy identity

Take the dot product of the momentum equation with $u$ and integrate over space. The pressure term integrates to zero (because $\nabla \cdot u = 0$), and the transport term also integrates to zero (it is a perfect divergence for divergence-free $u$). What remains is

$$\frac{d}{dt}\, \frac12 \int |u|^2\, dx = -\nu \int |\nabla u|^2\, dx \le 0.$$

Integrating in time gives the **energy inequality**

$$\frac12 \|u(t)\|_{L^2}^2 + \nu \int_0^t \|\nabla u\|_{L^2}^2\, ds \le \frac12 \|u_0\|_{L^2}^2.$$

This is the one bound that holds for all time, for any reasonable solution, in any dimension. The kinetic energy never increases, and the total amount dissipated by viscosity is bounded by the initial energy. Keep this inequality in mind: it is the only globally-in-time control we have, and the entire difficulty of the problem is that it is not enough in three dimensions.

## Vorticity and stretching

The **vorticity** $\omega = \nabla \times u$ measures local spinning. Taking the curl of the momentum equation gives the vorticity equation

$$\partial_t \omega + (u \cdot \nabla)\omega = (\omega \cdot \nabla) u + \nu \Delta \omega.$$

The new term $(\omega \cdot \nabla) u$ is **vortex stretching**: it can amplify vorticity by stretching vortex tubes (think of a spinning skater pulling in their arms and speeding up). This term is the engine of small-scale generation and the suspected route to any singularity.

Here is the decisive structural fact. In **two dimensions** the vorticity is a scalar pointing out of the plane, and the stretching term $(\omega \cdot \nabla)u$ vanishes identically. The 2D vorticity equation is just transport plus diffusion of a scalar, so $\int \omega^2$ (the enstrophy) cannot increase, and 2D Navier-Stokes is globally smooth (Ladyzhenskaya 1959). In three dimensions the stretching term is present and there is no such bound. **The 3D problem is the problem of controlling vortex stretching.** This is why 2D is the "must-stay-smooth" control: any idea that does not use the 3D stretching term would apply equally in 2D, where it is not needed.

## The scaling symmetry

The Navier-Stokes equations have a one-parameter scaling symmetry. If $(u, p)$ is a solution, then so is

$$u_\lambda(x, t) = \lambda\, u(\lambda x, \lambda^2 t), \qquad p_\lambda(x, t) = \lambda^2\, p(\lambda x, \lambda^2 t),$$

for any $\lambda > 0$. Check it by substituting into the equations: every term scales the same way, and the viscosity $\nu$ is unchanged (which is special to this exact rescaling, $\lambda$ in space matched with $\lambda^2$ in time).

This symmetry is the ruler that measures everything. Ask how a norm of $u$ behaves under the rescaling:

- The energy $\|u\|_{L^2}$ shrinks as you zoom into small scales ($\lambda \to \infty$). It is **supercritical**: blind to small scales.
- The $\dot H^{1/2}$, $L^3$, and $\mathrm{BMO}^{-1}$ norms are unchanged by the rescaling. They are **critical**: they live exactly at the scale where a singularity would form.
- The enstrophy ($H^1$) norm grows as you zoom in. It is **subcritical**: it would control small scales, but it is not bounded for all time in 3D (in 2D it is, which is exactly why 2D is solved).

A regularity statement must be at the critical or subcritical level. The energy is at the supercritical level. That mismatch, made precise with this scaling, is the subject of the [graduate level](../02_graduate/) and the heart of the problem. You can compute these exponents yourself with `experiments/scaling_criticality/criticality_table.py`.
