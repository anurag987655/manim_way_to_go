# base_signal.py
from manim import *

def make_axes(x_range=[-6, 6, 1], y_range=[-0.5, 2, 0.5]):
    return Axes(
        x_range=x_range,
        y_range=y_range,
        axis_config={"color": GREY_B},
        x_axis_config={"include_numbers": True},
        y_axis_config={"include_numbers": True},
    ).scale(0.9)

def add_axis_labels(axes, x_text="t", y_text="x(t)"):
    x_label = MathTex(x_text).scale(0.8)
    y_label = MathTex(y_text).scale(0.8)
    x_label.next_to(axes.x_axis, RIGHT, buff=0.1)
    y_label.next_to(axes.y_axis, UP, buff=0.1)
    return VGroup(x_label, y_label)

def create_formula_label(text="x(t)", position=UL, color=BLUE, scale_factor=0.9):
    return MathTex(text, color=color).scale(scale_factor).to_corner(position)

# Helpers to match your original code
def create_sample_dot(axes, t, x, radius=0.8, color=YELLOW):
    return Dot(axes.c2p(t, x), color=color, radius=radius)

def create_sample_label(dot, t, x, color=GOLD, scale=0.7):
    label = MathTex(f"x({t})={x}", color=color).scale(scale)
    label.next_to(dot, UP, buff=0.2)
    return label

def animate_sample_points(scene, axes, sample_points, next_label_anchor,
                          dot_color=YELLOW, label_color=GOLD,
                          label_scale=0.7, dot_radius=0.08):
    """
    Exactly replicates the animation loop from your original code.
    """
    dots = VGroup()
    labels = VGroup()

    for t_value, x_value in sample_points:
        dot = create_sample_dot(axes, t_value, x_value, radius=dot_radius, color=dot_color)
        label = create_sample_label(dot, t_value, x_value, color=label_color, scale=label_scale)

        scene.play(FadeIn(dot), run_time=0.5)
        scene.play(Write(label), run_time=0.5)

        target_position = label.copy().next_to(next_label_anchor, DOWN, aligned_edge=LEFT, buff=0.1)
        scene.play(Transform(label, target_position), run_time=0.5)
        scene.wait(0.2)

        dots.add(dot)
        labels.add(label)
        next_label_anchor = label

    return dots, labels

def build_custom_signal(axes):
    zero1 = axes.plot(lambda t: 0, x_range=[-3, -1], color=GREEN_C)
    ramp_up = axes.plot(lambda t: t + 1, x_range=[-1, 0], color=GREEN_C)
    flat = axes.plot(lambda t: 1, x_range=[0, 1], color=GREEN_C)
    ramp_down = axes.plot(lambda t: 2 - t, x_range=[1, 2], color=GREEN_C)
    zero2 = axes.plot(lambda t: 0, x_range=[2, 3], color=GREEN_C)
    return VGroup(zero1, ramp_up, flat, ramp_down, zero2)