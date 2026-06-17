# discrete_transformation.py
from manim import *
from base_signal import *

# Define the base discrete signal data
# x[-2]=2, x[-1]=-1, x[0]=1, x[1]=3, x[2]=0, x[3]=-2
DISCRETE_DATA = {-2: 2, -1: -1, 0: 1, 1: 3, 2: 0, 3: -2}

class Shift(Scene):
    def construct(self):
        axes = make_discrete_axes()
        labels = add_axis_labels(axes, "n", "x[n]")
        signal = build_discrete_signal(axes, DISCRETE_DATA)

        formula = create_formula_label("x[n]")
        next_label_anchor = formula

        self.play(Create(axes))
        self.play(Create(labels))
        self.play(Create(signal), run_time=2)
        self.play(Write(formula))
        self.wait(0.5)

        # Pick some sample points to track
        sample_points = [(-1, -1), (0, 1), (1, 3)]

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

        # Mapping for x[n-2] -> n_new = n_old + 2
        labels_data = [
            {"text": r"n=0,\ x[0-2]=x[-2]", "point": (0, 2)},
            {"text": r"n=1,\ x[1-2]=x[-1]", "point": (1, -1)},
            {"text": r"n=2,\ x[2-2]=x[0]",  "point": (2, 1)},
        ]
        
        group = create_transformation_animation(
            scene=self,
            axes=axes,
            formula="x[n-2]",
            labels_data=labels_data,
            corner=UR,
            dot_color=RED,
            dot_radius=0.08,
            dot_run_time=1.2,
            label_scale=0.7,
            label_color=GOLD
        )
        
        self.wait(2)

        old_y_label = labels[1]
        new_y_label = MathTex("x[n-2]", color=old_y_label.get_color()).scale(0.8)
        new_y_label.move_to(old_y_label)
        self.play(Transform(old_y_label, new_y_label))

        # Shift the signal (Right shift by 2)
        shifted_signal = build_shifted_discrete_signal(axes, DISCRETE_DATA, shift=-2)
        self.play(Transform(signal, shifted_signal, run_time=2))

        # Turn mapping dots to yellow to match the signal
        self.play(group[2].animate.set_color(YELLOW))

        self.play(FadeOut(yellow_dots))
        self.wait(2)


class Scale(Scene):
    def construct(self):
        axes = make_discrete_axes()
        labels = add_axis_labels(axes, "n", "x[n]")
        signal = build_discrete_signal(axes, DISCRETE_DATA)

        formula = create_formula_label("x[n]")
        next_label_anchor = formula

        self.play(Create(axes))
        self.play(Create(labels))
        self.play(Create(signal), run_time=2)
        self.play(Write(formula))
        self.wait(0.5)

        sample_points = [(-1, -1), (0, 1), (1, 3)]

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

        # Mapping for x[n/2] -> n_new = n_old * 2
        labels_data = [
            {"text": r"n=-2,\ x[-2/2]=x[-1]", "point": (-2, -1)},
            {"text": r"n=0,\ x[0/2]=x[0]",   "point": (0, 1)},
            {"text": r"n=2,\ x[2/2]=x[1]",   "point": (2, 3)},
        ]
        
        group = create_transformation_animation(
            scene=self,
            axes=axes,
            formula="x[n/2]",
            labels_data=labels_data,
            corner=UR,
            dot_color=RED,
            dot_radius=0.08,
            dot_run_time=1.2,
            label_scale=0.7,
            label_color=GOLD
        )
        
        self.wait(2)

        old_y_label = labels[1]
        new_y_label = MathTex("x[n/2]", color=old_y_label.get_color()).scale(0.8)
        new_y_label.move_to(old_y_label)
        self.play(Transform(old_y_label, new_y_label))

        # Scale the signal
        scaled_signal = build_scaled_discrete_signal(axes, DISCRETE_DATA, factor=2)
        self.play(Transform(signal, scaled_signal, run_time=2))

        # Turn mapping dots to yellow to match the signal
        self.play(group[2].animate.set_color(YELLOW))

        self.play(FadeOut(yellow_dots))
        self.wait(2)


class Reversal(Scene):
    def construct(self):
        axes = make_discrete_axes()
        labels = add_axis_labels(axes, "n", "x[n]")
        signal = build_discrete_signal(axes, DISCRETE_DATA)

        formula = create_formula_label("x[n]")
        next_label_anchor = formula

        self.play(Create(axes))
        self.play(Create(labels))
        self.play(Create(signal), run_time=2)
        self.play(Write(formula))
        self.wait(0.5)

        sample_points = [(-1, -1), (0, 1), (1, 3)]

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

        # Mapping for x[-n] -> n_new = -n_old
        labels_data = [
            {"text": r"n=1,\ x[-(1)]=x[-1]", "point": (1, -1)},
            {"text": r"n=0,\ x[-(0)]=x[0]",   "point": (0, 1)},
            {"text": r"n=-1,\ x[-(-1)]=x[1]", "point": (-1, 3)},
        ]
        
        group = create_transformation_animation(
            scene=self,
            axes=axes,
            formula="x[-n]",
            labels_data=labels_data,
            corner=UR,
            dot_color=RED,
            dot_radius=0.08,
            dot_run_time=1.2,
            label_scale=0.7,
            label_color=GOLD
        )
        
        self.wait(2)

        old_y_label = labels[1]
        new_y_label = MathTex("x[-n]", color=old_y_label.get_color()).scale(0.8)
        new_y_label.move_to(old_y_label)
        self.play(Transform(old_y_label, new_y_label))

        # Perform the 2D flip for reversal
        self.play(
            signal.animate.scale([-1, 1, 1], about_point=axes.c2p(0, 0)),
            run_time=2,
            rate_func=rate_functions.ease_in_out_sine
        )

        # Turn mapping dots to yellow to match the signal
        self.play(group[2].animate.set_color(YELLOW))

        self.play(FadeOut(yellow_dots))
        self.wait(2)
