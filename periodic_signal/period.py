from manim import *
import numpy as np


class PeriodicSignal(Scene):
    def construct(self):
        # Step 1: Display "Periodic Signal" text at center in blue
        title = Text("Periodic Signal", color=BLUE)
        self.play(Write(title))
        self.wait(2)

        # Step 2: Move text to top edge
        self.play(title.animate.to_edge(UP))
        self.wait(1)

        # Step 3: Square wave axes (shifted up)
        square_axes = Axes(
            x_range=[0, 6 * PI, PI],
            y_range=[-1.5, 1.5, 0.5],
            x_length=10,
            y_length=2.2,
            tips=True,
        ).shift(UP * 1.5)

        # X-axis tick labels for square wave
        x_labels_sq = VGroup()
        x_vals = [0, PI, 2 * PI, 3 * PI, 4 * PI, 5 * PI, 6 * PI]
        x_texts = ["0", r"\pi", r"2\pi", r"3\pi", r"4\pi", r"5\pi", r"6\pi"]
        for val, txt in zip(x_vals, x_texts):
            label = MathTex(txt, font_size=28)
            label.next_to(square_axes.c2p(val, 0), DOWN, buff=0.15)
            x_labels_sq.add(label)

        # Y-axis tick labels for square wave
        y_labels_sq = VGroup()
        for val in [-1, 1]:
            label = MathTex(str(val), font_size=28)
            label.next_to(square_axes.c2p(0, val), LEFT, buff=0.15)
            y_labels_sq.add(label)

        t_label_sq = MathTex("t", font_size=30).next_to(
            square_axes.c2p(6 * PI, 0), RIGHT, buff=0.2
        )
        x_label_sq = MathTex("x(t)", font_size=30).next_to(
            square_axes.c2p(0, 1.5), UP, buff=0.2
        )

        def square_func(t):
            s = np.sin(t)
            if abs(s) < 0.01:
                return 0.0
            return float(np.sign(s))

        # Full square wave - GREEN
        square_wave = square_axes.plot(
            square_func,
            color=GREEN,
            use_smoothing=False,
        )

        self.play(Create(square_axes), Write(t_label_sq), Write(x_label_sq))
        self.play(Write(x_labels_sq), Write(y_labels_sq))
        self.play(Create(square_wave), run_time=2)
        self.wait(1)

        # Step 4: Triangular wave axes (shifted down)
        tri_axes = Axes(
            x_range=[0, 6 * PI, PI],
            y_range=[-1.5, 1.5, 0.5],
            x_length=10,
            y_length=2.2,
            tips=True,
        ).shift(DOWN * 2.2)

        # X-axis tick labels for tri wave
        x_labels_tri = VGroup()
        for val, txt in zip(x_vals, x_texts):
            label = MathTex(txt, font_size=28)
            label.next_to(tri_axes.c2p(val, 0), DOWN, buff=0.15)
            x_labels_tri.add(label)

        # Y-axis tick labels for tri wave
        y_labels_tri = VGroup()
        for val in [-1, 1]:
            label = MathTex(str(val), font_size=28)
            label.next_to(tri_axes.c2p(0, val), LEFT, buff=0.15)
            y_labels_tri.add(label)

        t_label_tri = MathTex("t", font_size=30).next_to(
            tri_axes.c2p(6 * PI, 0), RIGHT, buff=0.2
        )
        x_label_tri = MathTex("x(t)", font_size=30).next_to(
            tri_axes.c2p(0, 1.5), UP, buff=0.2
        )

        def tri_func(t):
            period = 2 * PI
            mod = t % period
            if mod < PI:
                return -1 + 2 * mod / PI
            else:
                return 1 - 2 * (mod - PI) / PI

        # Full triangular wave - YELLOW
        tri_wave = tri_axes.plot(
            tri_func,
            color=YELLOW,
        )

        self.play(Create(tri_axes), Write(t_label_tri), Write(x_label_tri))
        self.play(Write(x_labels_tri), Write(y_labels_tri))
        self.play(Create(tri_wave), run_time=2)
        self.wait(1)

        # Step 5: Now highlight non-redundant part (first period)
        # Square wave - highlight first period in RED
        square_non_redundant = square_axes.plot(
            square_func,
            x_range=[0, 2 * PI],
            color=RED,
            use_smoothing=False,
        )
        # Bracket for period T - below with arrows
        bracket_line_sq = Line(
            square_axes.c2p(0, 0) + DOWN * 1.4,
            square_axes.c2p(2 * PI, 0) + DOWN * 1.4,
            color=RED,
            stroke_width=2,
        )
        arrow_left_sq = Arrow(
            bracket_line_sq.get_start() + LEFT * 0.1,
            bracket_line_sq.get_start(),
            color=RED,
            buff=0,
            stroke_width=2,
            max_tip_length_to_length_ratio=0.5,
        )
        arrow_right_sq = Arrow(
            bracket_line_sq.get_end() + RIGHT * 0.1,
            bracket_line_sq.get_end(),
            color=RED,
            buff=0,
            stroke_width=2,
            max_tip_length_to_length_ratio=0.5,
        )
        bracket_label_sq = MathTex("T", font_size=28, color=RED).next_to(
            bracket_line_sq, DOWN, buff=0.1
        )

        self.play(Create(square_non_redundant), run_time=1.5)
        self.play(Create(bracket_line_sq), Create(arrow_left_sq), Create(arrow_right_sq), Write(bracket_label_sq))
        self.wait(1)

        # Triangular wave - highlight first period in ORANGE
        tri_non_redundant = tri_axes.plot(
            tri_func,
            x_range=[0, 2 * PI],
            color=ORANGE,
        )
        # Bracket for period T - below with arrows
        bracket_line_tri = Line(
            tri_axes.c2p(0, 0) + DOWN * 1.4,
            tri_axes.c2p(2 * PI, 0) + DOWN * 1.4,
            color=ORANGE,
            stroke_width=2,
        )
        arrow_left_tri = Arrow(
            bracket_line_tri.get_start() + LEFT * 0.1,
            bracket_line_tri.get_start(),
            color=ORANGE,
            buff=0,
            stroke_width=2,
            max_tip_length_to_length_ratio=0.5,
        )
        arrow_right_tri = Arrow(
            bracket_line_tri.get_end() + RIGHT * 0.1,
            bracket_line_tri.get_end(),
            color=ORANGE,
            buff=0,
            stroke_width=2,
            max_tip_length_to_length_ratio=0.5,
        )
        bracket_label_tri = MathTex("T", font_size=28, color=ORANGE).next_to(
            bracket_line_tri, DOWN, buff=0.1
        )

        self.play(Create(tri_non_redundant), run_time=1.5)
        self.play(Create(bracket_line_tri), Create(arrow_left_tri), Create(arrow_right_tri), Write(bracket_label_tri))

        # Step 6: Pause for 2 seconds after highlighting T on both signals
        self.wait(2)

        # Step 7: Fade out the triangular wave (bottom signal) completely
        tri_group = VGroup(
            tri_axes, x_labels_tri, y_labels_tri,
            t_label_tri, x_label_tri, tri_wave,
            tri_non_redundant, bracket_line_tri,
            arrow_left_tri, arrow_right_tri, bracket_label_tri,
        )
        self.play(FadeOut(tri_group), run_time=1.5)
        self.wait(2)

        # Step 8: Bring square wave down and increase size
        sq_group = VGroup(
            square_axes, x_labels_sq, y_labels_sq,
            t_label_sq, x_label_sq, square_wave,
            square_non_redundant, bracket_line_sq,
            arrow_left_sq, arrow_right_sq, bracket_label_sq,
        )
        self.play(
            sq_group.animate.shift(DOWN * 0.8).scale(1.15),
            run_time=1.5,
        )
        self.wait(0.5)

        # Step 9: Perform shift animation - copy first period and shift it
        shift_phys = square_axes.c2p(2 * PI, 0)[0] - square_axes.c2p(0, 0)[0]

        copied_period = square_axes.plot(
            square_func,
            x_range=[0, 2 * PI],
            color=RED,
            use_smoothing=False,
        ).set_opacity(0.5)

        self.play(Create(copied_period), run_time=1)

        # Shift arrow above the graph
        arrow_start = square_axes.c2p(PI, 0) + UP * 1.2 
        arrow_end = arrow_start + RIGHT * shift_phys
        shift_arrow = Arrow(
            arrow_start,
            arrow_end,
            color=WHITE,
            buff=0,
            stroke_width=3,
        )
        shift_label = MathTex(r"\text{Shift by } T", font_size=30, color=WHITE)
        shift_label.next_to(shift_arrow, UP, buff=0.15)

        self.play(
            copied_period.animate.shift(RIGHT * shift_phys),
            Create(shift_arrow),
            Write(shift_label),
            run_time=2,
        )
        self.wait(1)

        # Step 10: Glow effect on original and shifted sections
        glow_original = square_axes.plot(
            square_func,
            x_range=[0, 2 * PI],
            color=YELLOW,
            use_smoothing=False,
        ).set_stroke(width=8, opacity=0.9)

        glow_copied = square_axes.plot(
            square_func,
            x_range=[2 * PI, 4 * PI],
            color=YELLOW,
            use_smoothing=False,
        ).set_stroke(width=8, opacity=0.9)

        self.play(
            Create(glow_original),
            Create(glow_copied),
            run_time=0.7,
        )   
        self.play(
            FadeOut(glow_original),
            FadeOut(glow_copied),
            run_time=0.7,
        )
        self.wait(0.5)

        # Step 11: Fade out shift elements
        self.play(FadeOut(shift_arrow), FadeOut(shift_label), FadeOut(copied_period), run_time=0.5)

        # Step 12: Display the periodicity equation x(t) = x(t+T)
        equation = MathTex(r"x(t) = x(t + T)", font_size=48, color=WHITE)
        equation.next_to(title, DOWN, buff=0.5)
        self.play(Write(equation), run_time=2)
        self.wait(3)
