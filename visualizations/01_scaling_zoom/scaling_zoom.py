"""manim scene: the Navier-Stokes scaling symmetry and supercriticality.

Renders the central structural fact of the problem. The scaling

    u_lambda(x, t) = lambda * u(lambda x, lambda^2 t)

maps solutions to solutions. As we zoom into small scales (lambda -> infinity),
the energy norm shrinks (it is SUPERCRITICAL, exponent -1/2 in 3D) while a
critical norm stays fixed (exponent 0). The scene shows a velocity profile being
rescaled and two "norm bars" tracking the two behaviors, making visible why the
only all-time a priori bound (energy) cannot see the small scales where a
singularity would form.

Render:
    manim -ql visualizations/01_scaling_zoom/scaling_zoom.py ScalingZoom

WHY this scene: the supercriticality gap is the compass for the whole repo, and
it is an inherently visual statement about how a norm responds to zooming. A
static table (experiments/scaling_criticality/) states it; this shows it.
"""

from manim import (
    Scene,
    Axes,
    MathTex,
    Text,
    VGroup,
    Rectangle,
    Create,
    Write,
    Transform,
    FadeIn,
    UP,
    DOWN,
    LEFT,
    RIGHT,
    BLUE,
    RED,
    GREEN,
    YELLOW,
    WHITE,
)
import numpy as np


class ScalingZoom(Scene):
    def construct(self):
        title = Text("Navier-Stokes scaling: why the energy is supercritical", font_size=30)
        title.to_edge(UP)
        self.play(Write(title))

        scaling = MathTex(
            r"u_\lambda(x,t) = \lambda\, u(\lambda x,\ \lambda^2 t)",
            font_size=40,
        )
        scaling.next_to(title, DOWN, buff=0.4)
        self.play(Write(scaling))

        # a velocity profile and its rescaling
        axes = Axes(
            x_range=[0, 2 * np.pi, np.pi],
            y_range=[-1.5, 1.5, 1],
            x_length=6,
            y_length=2.5,
            tips=False,
        )
        axes.shift(DOWN * 0.5 + LEFT * 2.5)

        def profile(x, lam):
            # u_lambda(x) = lambda * u(lambda x); base profile u(x)=sin(x)
            return lam * np.sin(lam * x)

        base = axes.plot(lambda x: profile(x, 1.0), color=BLUE)
        base_label = Text("u (large scale)", font_size=22, color=BLUE)
        base_label.next_to(axes, DOWN, buff=0.2)

        self.play(Create(axes), Create(base), FadeIn(base_label))

        # two norm bars: energy (supercritical) and critical
        bar_h_energy = 2.2
        bar_h_crit = 2.2
        energy_bar = Rectangle(width=0.6, height=bar_h_energy, color=RED, fill_opacity=0.6)
        crit_bar = Rectangle(width=0.6, height=bar_h_crit, color=GREEN, fill_opacity=0.6)
        energy_bar.shift(RIGHT * 3.2 + DOWN * 0.5)
        crit_bar.next_to(energy_bar, RIGHT, buff=0.8)

        energy_lbl = MathTex(r"\|u\|_{L^2}", font_size=26, color=RED).next_to(energy_bar, UP, buff=0.15)
        crit_lbl = MathTex(r"\|u\|_{\dot H^{1/2}}", font_size=26, color=GREEN).next_to(crit_bar, UP, buff=0.15)

        self.play(
            FadeIn(energy_bar), FadeIn(crit_bar),
            Write(energy_lbl), Write(crit_lbl),
        )

        zoom_label = Text("zoom into small scales:  lambda grows", font_size=24, color=YELLOW)
        zoom_label.to_edge(DOWN)
        self.play(FadeIn(zoom_label))

        # animate increasing lambda: profile gets finer, energy bar shrinks, critical bar fixed
        for lam in [1.5, 2.5, 4.0]:
            new_profile = axes.plot(lambda x: profile(x, lam), color=BLUE)
            # energy norm of lambda*sin(lambda x) scales as lambda^{-1/2}: shrink
            new_energy_h = bar_h_energy * (lam ** (-0.5))
            new_energy = Rectangle(width=0.6, height=new_energy_h, color=RED, fill_opacity=0.6)
            new_energy.move_to(energy_bar.get_bottom() + UP * new_energy_h / 2)
            # critical norm is scale invariant: bar fixed
            self.play(
                Transform(base, new_profile),
                Transform(energy_bar, new_energy),
                run_time=1.2,
            )

        verdict = VGroup(
            Text("energy shrinks: SUPERCRITICAL (blind to small scales)", font_size=22, color=RED),
            Text("critical norm fixed: lives where a singularity forms", font_size=22, color=GREEN),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        verdict.to_edge(DOWN)
        self.play(Transform(zoom_label, verdict))
        self.wait(2)
