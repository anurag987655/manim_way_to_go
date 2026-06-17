# continuos_transformation.py
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

        # One line replaces the whole loop
        yellow_dots,yellow_labels = animate_sample_points(
            scene=self,
            axes=axes,
            sample_points=sample_points,
            next_label_anchor=next_label_anchor,
            dot_color=YELLOW,
            label_color=GOLD,
            label_scale=0.7,
            dot_radius=0.08
        )

        self.wait(1)

        labels_data = [
            {"text": r"t=-3,\ x(-3+2)=x(-1)", "point": (-3, 0)},
            {"text": r"t=-2,\ x(-2+2)=x(0)",  "point": (-2, 1)},
            {"text": r"t=-1,\ x(-1+2)=x(1)",  "point": (-1, 1)},
            {"text": r"t=0,\ x(0+2)=x(2)",    "point": (0, 0)},
        ]
        
        group = create_transformation_animation(
            scene=self,
            axes=axes,
            formula="x(t+2)",
            labels_data=labels_data,
            corner=UR,
            dot_color=RED,
            dot_radius=0.08,
            dot_run_time=1.2,
            label_scale=0.7,
            label_color=GOLD
        )
        
        self.wait(2)

        old_y_label = labels[1]  # because labels = VGroup(x_label, y_label)
        new_y_label = MathTex("x(t+2)", color=old_y_label.get_color()).scale(0.8)
        new_y_label.move_to(old_y_label)
        self.play(Transform(old_y_label, new_y_label))

        # 2. Build the shifted signal and transform (slide/morph)
        shifted_signal = build_shifted_signal(axes, shift=2)
        self.play(Transform(signal, shifted_signal, run_time=2, rate_func=rate_functions.ease_in_out_sine))

        # 3. Fade out the yellow dots and their labels (they are no longer needed)
        self.play(FadeOut(yellow_dots))

        self.wait(2)


class Scale(Scene):
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

        # Initial sample points
        yellow_dots, yellow_labels = animate_sample_points(
            scene=self,
            axes=axes,
            sample_points=sample_points,
            next_label_anchor=next_label_anchor,
            dot_color=YELLOW,
            label_color=GOLD,
            label_scale=0.7,
            dot_radius=0.08
        )

        self.wait(1)

        # Labels for compression x(2t)
        labels_data = [
            {"text": r"t=-0.5,\ x(2 \cdot -0.5)=x(-1)", "point": (-0.5, 0)},
            {"text": r"t=0,\ x(2 \cdot 0)=x(0)",       "point": (0, 1)},
            {"text": r"t=0.5,\ x(2 \cdot 0.5)=x(1)",   "point": (0.5, 1)},
            {"text": r"t=1,\ x(2 \cdot 1)=x(2)",       "point": (1, 0)},
        ]
        
        group = create_transformation_animation(
            scene=self,
            axes=axes,
            formula="x(2t)",
            labels_data=labels_data,
            corner=UR,
            dot_color=RED,
            dot_radius=0.08,
            dot_run_time=1.2,
            label_scale=0.7,
            label_color=GOLD
        )
        
        self.wait(2)

        # Transform the axis label
        old_y_label = labels[1]
        new_y_label = MathTex("x(2t)", color=old_y_label.get_color()).scale(0.8)
        new_y_label.move_to(old_y_label)
        self.play(Transform(old_y_label, new_y_label))

        # Transform the signal
        scaled_signal = build_scaled_signal(axes, scale=2)
        self.play(Transform(signal, scaled_signal, run_time=2, rate_func=rate_functions.ease_in_out_sine))

        # Cleanup
        self.play(FadeOut(yellow_dots))
        self.wait(2)


class Reversal(Scene):
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

        # Initial sample points
        yellow_dots, yellow_labels = animate_sample_points(
            scene=self,
            axes=axes,
            sample_points=sample_points,
            next_label_anchor=next_label_anchor,
            dot_color=YELLOW,
            label_color=GOLD,
            label_scale=0.7,
            dot_radius=0.08
        )

        self.wait(1)

        # Labels for reversal x(-t)
        # We pick points that map to our original samples
        labels_data = [
            {"text": r"t=-2,\ x(-(-2))=x(2)", "point": (-2, 0)},
            {"text": r"t=-1,\ x(-(-1))=x(1)", "point": (-1, 1)},
            {"text": r"t=0,\ x(-(0))=x(0)",    "point": (0, 1)},
            {"text": r"t=1,\ x(-(1))=x(-1)",   "point": (1, 0)},
        ]
        
        group = create_transformation_animation(
            scene=self,
            axes=axes,
            formula="x(-t)",
            labels_data=labels_data,
            corner=UR,
            dot_color=RED,
            dot_radius=0.08,
            dot_run_time=1.2,
            label_scale=0.7,
            label_color=GOLD
        )
        
        self.wait(2)

        # Transform the axis label
        old_y_label = labels[1]
        new_y_label = MathTex("x(-t)", color=old_y_label.get_color()).scale(0.8)
        new_y_label.move_to(old_y_label)
        self.play(Transform(old_y_label, new_y_label))

        # Transform the signal (Flip effect)
        # Scaling X by -1 creates a perfect reflection across the Y-axis
        # This "squashes" and then "expands" the signal, looking like a 2D flip
        self.play(
            signal.animate.scale([-1, 1, 1], about_point=axes.c2p(0, 0)),
            run_time=2,
            rate_func=rate_functions.ease_in_out_sine
        )

        # Cleanup
        self.play(FadeOut(yellow_dots))
        self.wait(2)
