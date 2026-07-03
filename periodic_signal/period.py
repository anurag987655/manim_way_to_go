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

        square_wave = square_axes.plot(
            square_func,
            color=GREEN,
            use_smoothing=False,
        )


        self.play(Create(square_axes), Write(t_label_sq), Write(x_label_sq))
        self.play(Write(x_labels_sq), Write(y_labels_sq))
        self.play(Create(square_wave))
        self.wait(1)

        # Step 4: Triangular wave axes (shifted down, with more buff)
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

        tri_wave = tri_axes.plot(
            tri_func,
            color=YELLOW,
        )

        self.play(Create(tri_axes), Write(t_label_tri), Write(x_label_tri))
        self.play(Write(x_labels_tri), Write(y_labels_tri))
        self.play(Create(tri_wave))

        # Step 5: Pause for 3 seconds
        self.wait(3)
