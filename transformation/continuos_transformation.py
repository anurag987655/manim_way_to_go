from manim import * 
from base_signal import *

class Shift(Scene):
    def construct(self):
        axes = make_axes()
        labels = add_axis_labels(axes, "t", "x(t)")
        signal = build_custom_signal(axes)

        formula = create_formula_label("x(t)")
        next_label_anchor = formula

        self.play(Create(axes))
        self.play(Create(labels))
        self.play(Create(signal), run_time=3)
        self.play(Write(formula))
        self.wait(0.5)

        sample_points = [(-1, 0), (0, 1), (1, 1), (2, 0)]

        for t_value, x_value in sample_points:
            dot = create_sample_dot(axes, t_value, x_value)
            label = create_sample_label(dot, t_value, x_value)

            self.play(FadeIn(dot), run_time=0.5)
            self.play(Write(label), run_time=0.5)
            self.play(dot.animate.shift(RIGHT * 0.15 + UP * 0.05), run_time=0.4)

            target_position = label.copy().next_to(next_label_anchor, DOWN, aligned_edge=LEFT, buff=0.1)
            self.play(Transform(label, target_position), run_time=0.5)
            self.wait(0.2)

            next_label_anchor = label

        self.wait(1)

