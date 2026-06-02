# What is the Navier-Stokes problem?

No math. Just the picture.

## The equations describe moving fluid

Water in a pipe, air over a wing, smoke curling off a candle, the cream you stir into coffee. The Navier-Stokes equations are the rulebook for how a fluid moves. They have been used for almost two centuries, and they work: every weather forecast, every aircraft design, every simulation of blood flow leans on them. They are not in doubt as physics.

There are two pieces to the rulebook:

- **Fluid pushes itself around.** Where the fluid is already moving, it carries itself along and shoves neighboring fluid. This is the part that makes water swirl into vortices and smoke break into curls. It is the troublemaker.
- **Fluid is sticky (viscosity).** Honey is very sticky, water less so, air barely at all. Stickiness smooths things out: it spreads sharp differences in speed into gentle ones, like friction calming a spinning top.

The whole drama of the problem is a tug of war between these two. The self-pushing wants to make the flow wilder and finer (smaller and smaller swirls). The stickiness wants to smooth it back out.

## The question

Start with a fluid that is moving smoothly. No sharp edges, no infinite speeds, a sensible finite amount of energy. Let it evolve by the rulebook.

> Does it stay smooth forever, or can it tie itself into a knot so tight that, at one instant, at one point, the speed becomes infinite?

That knot, a point where some quantity blows up to infinity, is called a **singularity** or **blow-up**. Nobody has ever seen one in water. But nobody has been able to prove the fluid cannot make one either.

The Clay Mathematics Institute offers one million dollars for settling it, in three dimensions, with stickiness present. You can win by proving the flow always stays smooth, OR by exhibiting one smooth starting flow that does blow up. Either answer counts.

## Why it is hard: the one idea

Here is the heart of it, in words.

There is exactly one thing we can promise about the flow for all time: its total energy never increases (stickiness only ever drains energy away). That is a real, ironclad budget.

The trouble is that this energy budget is a statement about the **big picture** of the flow, the large swirls. A singularity, if it happened, would happen in the **fine detail**, an ever-smaller swirl spinning ever faster. And the energy budget says almost nothing about the fine detail. You can hide a faster and faster, smaller and smaller swirl while keeping the total energy budget perfectly satisfied.

So the only thing we can guarantee forever is blind to the only place a disaster could happen. Mathematicians call this **supercriticality**: the guarantee we have lives at the wrong scale to rule out the catastrophe. Closing that gap, finding some new guarantee that does see the fine detail, is the whole game.

## Two clues from simpler worlds

- **Flatland is fine.** If the fluid is confined to a flat sheet (two dimensions instead of three), the problem was solved long ago: it always stays smooth. The reason is that in two dimensions the swirls cannot stretch and intensify the way they can in three. So whatever makes three dimensions dangerous is exactly the stretching of swirls, and any idea for solving the 3D problem that would also "work" in flatland is missing the point, because flatland never had the problem.
- **Stickiness matters.** Turn off the stickiness entirely (a fluid with zero viscosity) and related equations are now known to be able to blow up. So the stickiness is not a minor footnote. The 3D question is really: is the smoothing from stickiness always just barely enough to win the tug of war? We think yes. We cannot prove it.

## Where this repo goes from here

- The [undergraduate level](../01_undergraduate/) writes the equations down and explains energy, vorticity, and scaling with calculus.
- The [graduate level](../02_graduate/) makes "supercritical" precise and surveys the regularity criteria.
- The [research level](../03_research/) maps the candidate proof routes and the walls each one hits.
- The [experiments](../../experiments/) let you watch the tug of war in code: a swirling vortex relaxing smoothly, and a simpler equation tying itself into a knot when you switch the stickiness off.
