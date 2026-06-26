import sys
sys.path.insert(0, "/home/anurag/Desktop/manim_way_to_go")
from global_templates import ct_axes, dt_axes
from manim import *
import numpy as np 

config.pixel_width = 1920
config.pixel_height = 1080
config.frame_rate = 60
config.background_color = "#0e0e10"


class Scene1(Scene):
    def construct(self):
        title = Text("Even and Odd signal", color = BLUE_C)
        self.play(Write(title), run_time = 2)
        self.play(FadeOut(title))

        title1 = Text("Even Signal", color = BLUE_C)
        self.play(Write(title1, run_time = 2))
        self.play(title1.animate.to_edge(UP))
        self.wait(1)

        even_eq = MathTex(r"x(t) = x(-t)", color = GOLD)
        even_eq.next_to(title1, DOWN, buff = 0.5)
        self.play(Write(even_eq), run_time = 2)

        # Positioning the continuous axis
        caxes, x_lab, y_lab = ct_axes(y_range=[-1.2, 1.5, 0.5])
        caxes.next_to(even_eq, DOWN, buff = 0.3)
        self.play(Create(caxes), run_time = 1)
        self.wait(2)
        
        # Creating a cosine wave animation 

        axes_left = caxes[0]
        cosine_plot = axes_left.plot(lambda t : np.cos(t), x_range=[-5,5], color = GREEN_C)
        self.play(Create(cosine_plot), run_time = 2)
        self.wait(1)

        # Group everything together and move to left half
        left_group = VGroup(caxes, cosine_plot)
        self.play(left_group.animate.scale(0.5).to_edge(LEFT).shift(DOWN*0.5))
        self.wait(1)

        # Create right axes aligned with left
        rgroup, xlab2, ylab2 = ct_axes(y_range=[-1.2, 1.5, 0.5], x_label="t", y_label="x(-t)")
        rgroup.scale(0.5)
        rgroup.next_to(left_group, RIGHT, buff=1.0)
        axes_right = rgroup[0]
        self.play(Create(rgroup), run_time = 1)
        self.wait(1)

        # Animate the flip: copy wave, flip it horizontally, move to right
        cosine_copy = cosine_plot.copy()
        self.add(cosine_copy)

        # Flip and move to right axes
        self.play(
            cosine_copy.animate.scale([-1, 1, 0]).move_to(axes_right.get_center()),
            run_time=2
        )
        self.wait(1)

class Scene2(Scene):
    def construct(self):
        title2 = Text("Odd Signal", color = BLUE_C)
        self.play(Write(title2), run_time = 2)
        self.play(title2.animate.to_edge(UP))
        self.wait(1)
        
        odd_eq  = MathTex(r"x(t)=-x(-t)", color = GOLD)
        odd_eq.next_to(title2, DOWN, buff = 0.1)
        self.play(Write(odd_eq), run_time = 2)
        self.wait(1)

        caxes, x_lab, y_lab = ct_axes(y_range=[-1.5, 1.5, 0.5])
        caxes.next_to(odd_eq, DOWN, buff=0.3)
        self.play(Create(caxes), run_time=1)
        self.wait(2)

        axes_left = caxes[0]
        sine_plot = axes_left.plot(lambda t: np.sin(t), x_range=[-5, 5], color=RED_C)
        self.play(Create(sine_plot), run_time=2)
        self.wait(1)

        left_group = VGroup(caxes, sine_plot)
        self.play(left_group.animate.scale(0.5).to_edge(LEFT).shift(DOWN*0.5))
        self.wait(1)

        rgroup, xlab2, ylab2 = ct_axes(y_range=[-1.5, 1.5, 0.5], x_label="t", y_label="x(-t)")
        rgroup.scale(0.5)
        rgroup.next_to(left_group, RIGHT, buff=1.0)
        axes_right = rgroup[0]
        self.play(Create(rgroup), run_time=1)
        self.wait(1)

        sine_copy = sine_plot.copy()
        self.add(sine_copy)

        self.play(
            sine_copy.animate.rotate(PI, axis=UP).move_to(axes_right.get_center()),
            run_time=2
        )
        self.wait(1)

        neg_y_lab = MathTex("-x(-t)", color=WHITE).scale(0.8).next_to(axes_right.y_axis, UP, buff=0.1)
        self.play(
            sine_copy.animate.scale([1, -1, 1]),
            Transform(ylab2, neg_y_lab),
            run_time=2
        )
        self.wait(1)


class Scene3(Scene):
    def construct(self):
        title3 = Text("Even-Odd Decomposition", color=BLUE_C)
        self.play(Write(title3), run_time=2)
        self.play(title3.animate.to_edge(UP))
        self.wait(1)

        # Formulas
        decomp_formula = MathTex(
            r"x(t)", r"=", r"x_e(t)", r"+", r"x_o(t)",
            color=WHITE
        )
        decomp_formula.scale(0.8)
        decomp_formula.next_to(title3, DOWN, buff=0.3)
        self.play(Write(decomp_formula), run_time=2)
        self.wait(1)

        even_formula = MathTex(
            r"x_e(t)", r"=", r"\frac{x(t) + x(-t)}{2}",
            color=GOLD
        )
        even_formula.scale(0.7)
        even_formula.next_to(decomp_formula, DOWN, buff=0.2)
        self.play(Write(even_formula), run_time=2)
        self.wait(1)

        odd_formula = MathTex(
            r"x_o(t)", r"=", r"\frac{x(t) - x(-t)}{2}",
            color=GOLD
        )
        odd_formula.scale(0.7)
        odd_formula.next_to(even_formula, DOWN, buff=0.2)
        self.play(Write(odd_formula), run_time=2)
        self.wait(2)

        # === Even proof: x_e(t) = x_e(-t) ===
        even_rect = SurroundingRectangle(even_formula, color=YELLOW_C, buff=0.1)
        self.play(Create(even_rect))
        self.play(
            FadeOut(decomp_formula),
            FadeOut(odd_formula),
        )
        self.play(
            even_rect.animate.move_to(UP * 1.4),
            even_formula.animate.move_to(UP * 1.4),
        )
        self.wait(0.3)

        e1 = MathTex(r"x_e(t) = \frac{x(t) + x(-t)}{2}", color=YELLOW_C).scale(0.65)
        e1.next_to(even_formula, DOWN, buff=0.5)
        e1_rect = SurroundingRectangle(e1, color=WHITE, fill_opacity=0.2, stroke_width=0, buff=0.1)
        self.play(
            Write(e1, run_time=2),
            Transform(even_rect, e1_rect),
        )
        self.wait(2)

        e2 = MathTex(r"\Rightarrow x_e(-t) = \frac{x(-t) + x(t)}{2}", color=YELLOW_C).scale(0.65)
        e2.next_to(e1, DOWN, buff=0.25)
        e2_rect = SurroundingRectangle(e2, color=WHITE, fill_opacity=0.2, stroke_width=0, buff=0.1)
        self.play(
            Write(e2, run_time=2),
            Transform(even_rect, e2_rect),
        )
        self.wait(2)

        e3 = MathTex(r"\Rightarrow x_e(-t) = \frac{x(t) + x(-t)}{2}", color=YELLOW_C).scale(0.65)
        e3.next_to(e2, DOWN, buff=0.25)
        e3_rect = SurroundingRectangle(e3, color=WHITE, fill_opacity=0.2, stroke_width=0, buff=0.1)
        self.play(
            Write(e3, run_time=2),
            Transform(even_rect, e3_rect),
        )
        self.wait(2)

        e_conc = MathTex(r"\therefore x_e(t) = x_e(-t)", color=YELLOW_C).scale(0.65)
        e_conc.next_to(e3, DOWN, buff=0.25)
        conc_rect = SurroundingRectangle(e_conc, color=WHITE, fill_opacity=0.2, stroke_width=0, buff=0.1)
        self.play(
            Write(e_conc, run_time=2),
            Transform(even_rect, conc_rect),
        )
        self.wait(2.5)

        self.play(
            FadeOut(even_rect),
            FadeOut(even_formula),
            FadeOut(e1),
            FadeOut(e2),
            FadeOut(e3),
            FadeOut(e_conc),
        )
        self.wait(0.3)

        # === Odd proof: x_o(t) = -x_o(-t) ===
        odd_formula2 = MathTex(
            r"x_o(t)", r"=", r"\frac{x(t) - x(-t)}{2}", color=GOLD
        ).scale(0.7)
        odd_formula2.move_to(UP * 1.4)

        odd_rect = SurroundingRectangle(odd_formula2, color=PURPLE_B, buff=0.1)
        self.play(Write(odd_formula2), Create(odd_rect))
        self.wait(0.3)

        o1 = MathTex(r"x_o(t) = \frac{x(t) - x(-t)}{2}", color=PURPLE_B).scale(0.65)
        o1.next_to(odd_formula2, DOWN, buff=0.5)
        o1_rect = SurroundingRectangle(o1, color=WHITE, fill_opacity=0.2, stroke_width=0, buff=0.1)
        self.play(
            Write(o1, run_time=2),
            Transform(odd_rect, o1_rect),
        )
        self.wait(2)

        o2 = MathTex(r"\Rightarrow x_o(-t) = \frac{x(-t) - x(t)}{2}", color=PURPLE_B).scale(0.65)
        o2.next_to(o1, DOWN, buff=0.25)
        o2_rect = SurroundingRectangle(o2, color=WHITE, fill_opacity=0.2, stroke_width=0, buff=0.1)
        self.play(
            Write(o2, run_time=2),
            Transform(odd_rect, o2_rect),
        )
        self.wait(2)

        o3 = MathTex(r"\Rightarrow x_o(-t) = -\frac{x(t) - x(-t)}{2}", color=PURPLE_B).scale(0.65)
        o3.next_to(o2, DOWN, buff=0.25)
        o3_rect = SurroundingRectangle(o3, color=WHITE, fill_opacity=0.2, stroke_width=0, buff=0.1)
        self.play(
            Write(o3, run_time=2),
            Transform(odd_rect, o3_rect),
        )
        self.wait(2)

        o_conc = MathTex(r"\therefore x_o(t) = -x_o(-t)", color=PURPLE_B).scale(0.65)
        o_conc.next_to(o3, DOWN, buff=0.25)
        conc_o_rect = SurroundingRectangle(o_conc, color=WHITE, fill_opacity=0.2, stroke_width=0, buff=0.1)
        self.play(
            Write(o_conc, run_time=2),
            Transform(odd_rect, conc_o_rect),
        )
        self.wait(2.5)

        self.play(
            FadeOut(odd_rect),
            FadeOut(odd_formula2),
            FadeOut(o1),
            FadeOut(o2),
            FadeOut(o3),
            FadeOut(o_conc),
        )
        self.wait(0.5)

        # Example signal: rectangular pulse
        example_label = MathTex(
            r"x(t) = \begin{cases} 1, & 0 < t < 2 \\ 0, & \text{otherwise} \end{cases}",
            color=GREEN_C
        )
        example_label.scale(0.65)
        example_label.next_to(title3, DOWN, buff=0.3)
        self.play(Write(example_label), run_time=2)
        self.wait(1)

        # Helper: create a scaled axis
        def make_axis(y_range, y_label):
            axes, _, _ = ct_axes(
                x_range=[-3, 3, 1],
                y_range=y_range,
                y_label=y_label,
                buff=0.05,
            )
            axes.scale(0.4)
            return axes

        def pulse_mobject(axes, start, end, height, color):
            """Draw a rectangular pulse without function-plot artifacts at jumps."""
            points = [
                ((start, 0), (start, height)),
                ((start, height), (end, height)),
                ((end, height), (end, 0)),
            ]
            return VGroup(*[
                Line(axes.c2p(*p0), axes.c2p(*p1), color=color, stroke_width=4)
                for p0, p1 in points
            ])

        # Create axes — top row first, bottom row later
        ax_xt = make_axis([-0.3, 1.5, 0.5], "x(t)")
        ax_xnt = make_axis([-0.3, 1.5, 0.5], "x(-t)")
        ax_xe = make_axis([-0.3, 1.5, 0.5], "x_e(t)")
        ax_xo = make_axis([-1, 1, 0.5], "x_o(t)")

        top_row = VGroup(ax_xt, ax_xnt).arrange(RIGHT, buff=0.6)
        bottom_row = VGroup(ax_xe, ax_xo).arrange(RIGHT, buff=0.6)
        grid = VGroup(top_row, bottom_row).arrange(DOWN, buff=0.4)
        grid.next_to(example_label, DOWN, buff=0.3)

        # --- Reveal top row ---
        self.play(Create(ax_xt), Create(ax_xnt), run_time=1)
        self.wait(0.3)

        # Draw x(t) on top-left
        curve_xt = pulse_mobject(ax_xt[0], 0, 2, 1, GREEN_C)
        self.play(Create(curve_xt, run_time=1.5))
        self.wait(0.5)

        # Flip x(t) ➔ x(-t) like a page turning into the destination axes.
        def flip_frame(alpha):
            left_origin = ax_xt[0].c2p(0, 0)
            right_origin = ax_xnt[0].c2p(0, 0)
            origin = interpolate(left_origin, right_origin, alpha)

            left_h = ax_xt[0].c2p(1, 0) - left_origin
            right_h = ax_xnt[0].c2p(1, 0) - right_origin
            h_vec = interpolate(left_h, right_h, alpha)

            left_v = ax_xt[0].c2p(0, 1) - left_origin
            right_v = ax_xnt[0].c2p(0, 1) - right_origin
            v_vec = interpolate(left_v, right_v, alpha)

            x_scale = np.cos(PI * alpha)
            color = interpolate_color(GREEN_C, RED_C, alpha)

            def point(x, y):
                return origin + x * x_scale * h_vec + y * v_vec

            return VGroup(
                Line(point(0, 0), point(0, 1), color=color, stroke_width=4),
                Line(point(0, 1), point(2, 1), color=color, stroke_width=4),
                Line(point(2, 1), point(2, 0), color=color, stroke_width=4),
            )

        flip_alpha = ValueTracker(0)
        flip_copy = flip_frame(0)
        flip_copy.add_updater(lambda mob: mob.become(flip_frame(flip_alpha.get_value())))
        self.add(flip_copy)
        target_xnt = pulse_mobject(ax_xnt[0], -2, 0, 1, RED_C)
        self.play(
            flip_alpha.animate.set_value(1),
            run_time=2,
            rate_func=smooth,
        )
        flip_copy.clear_updaters()
        # Replace copy with proper x(-t) curve
        self.remove(flip_copy)
        curve_xnt = target_xnt
        self.add(curve_xnt)
        self.wait(0.5)

        # --- Reveal bottom row instantly ---
        self.add(ax_xe, ax_xo)

        # --- x_e(t): signals slide down from above, then smoothly halve ---
        green_xe = pulse_mobject(ax_xt[0], 0, 2, 1, GREEN_C)
        red_xe = pulse_mobject(ax_xnt[0], -2, 0, 1, RED_C)
        green_xe_target = pulse_mobject(ax_xe[0], 0, 2, 1, GREEN_C)
        red_xe_target = pulse_mobject(ax_xe[0], -2, 0, 1, RED_C)

        self.play(
            Transform(green_xe, green_xe_target),
            Transform(red_xe, red_xe_target),
            run_time=1.2
        )
        self.wait(0.2)

        deriv_e = MathTex(r"\frac{x(t)+x(-t)}{2}", color=YELLOW_C).scale(0.4)
        deriv_e.next_to(ax_xe[0], UP, buff=0.05).shift(RIGHT * 0.4)
        self.play(Write(deriv_e), run_time=0.8)

        # Smoothly half both pulses
        green_half = pulse_mobject(ax_xe[0], 0, 2, 0.5, GREEN_C)
        red_half = pulse_mobject(ax_xe[0], -2, 0, 0.5, RED_C)
        self.play(
            Transform(green_xe, green_half),
            Transform(red_xe, red_half),
            run_time=1.5
        )
        # Unify even signal color and remove middle vertical line
        even_color = YELLOW_C
        even_signal = VGroup(
            Line(ax_xe[0].c2p(-2, 0), ax_xe[0].c2p(-2, 0.5), color=even_color, stroke_width=4),
            Line(ax_xe[0].c2p(-2, 0.5), ax_xe[0].c2p(2, 0.5), color=even_color, stroke_width=4),
            Line(ax_xe[0].c2p(2, 0.5), ax_xe[0].c2p(2, 0), color=even_color, stroke_width=4),
        )
        self.play(
            FadeOut(green_xe),
            FadeOut(red_xe),
            FadeIn(even_signal),
            run_time=0.6
        )
        self.wait(0.3)

        # Show even symmetry property
        even_prop = MathTex(r"x_e(t) = x_e(-t)", color=YELLOW_C).scale(0.45)
        even_prop.next_to(ax_xe, DOWN, buff=0.1)
        self.play(Write(even_prop), run_time=1)
        self.wait(0.5)

        # --- x_o(t): both slide down together, x(-t) flips at top first ---
        green_xo = pulse_mobject(ax_xt[0], 0, 2, 1, GREEN_C)
        red_xo = pulse_mobject(ax_xnt[0], -2, 0, 1, RED_C)
        flipped_red_top = pulse_mobject(ax_xnt[0], -2, 0, -1, RED_C)
        green_xo_target = pulse_mobject(ax_xo[0], 0, 2, 1, GREEN_C)
        red_xo_target = pulse_mobject(ax_xo[0], -2, 0, -1, RED_C)

        # Flip red at top, then both slide down together
        self.play(
            Transform(red_xo, flipped_red_top),
            run_time=0.8
        )
        self.play(
            Transform(green_xo, green_xo_target),
            Transform(red_xo, red_xo_target),
            run_time=1.2
        )
        self.wait(0.2)

        deriv_o = MathTex(r"\frac{x(t)-x(-t)}{2}", color=PURPLE_C).scale(0.4)
        deriv_o.next_to(ax_xo[0], UP, buff=0.05).shift(RIGHT * 0.4)
        self.play(Write(deriv_o), run_time=0.8)

        # Smoothly half both pulses
        green_half_xo = pulse_mobject(ax_xo[0], 0, 2, 0.5, GREEN_C)
        red_half_xo = pulse_mobject(ax_xo[0], -2, 0, -0.5, RED_C)
        self.play(
            Transform(green_xo, green_half_xo),
            Transform(red_xo, red_half_xo),
            run_time=1.5
        )
        # Unify odd signal color
        odd_color = PURPLE_C
        self.play(
            green_xo.animate.set_color(odd_color),
            red_xo.animate.set_color(odd_color),
            run_time=0.6
        )
        # Show odd symmetry property
        odd_prop = MathTex(r"x_o(t) = -x_o(-t)", color=PURPLE_C).scale(0.45)
        odd_prop.next_to(ax_xo, DOWN, buff=0.1)
        self.play(Write(odd_prop), run_time=1)
        self.wait(0.5)

        # Verification
        verify = MathTex(
            r"x_e(t)", r"+", r"x_o(t)", r"=", r"x(t)",
            color=WHITE
        )
        verify.scale(0.6)
        verify[0].set_color(YELLOW_C)
        verify[2].set_color(PURPLE_C)
        verify[4].set_color(GREEN_C)
        verify.next_to(VGroup(even_prop, odd_prop), DOWN, buff=0.3)
        self.play(Write(verify), run_time=1.5)
        self.wait(2)
        self.play(FadeOut(deriv_e), FadeOut(deriv_o), run_time=0.5)
        self.wait(2)
