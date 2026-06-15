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

def build_shifted_signal(axes, shift=2):
    """
    Build the signal x(t + shift) for shift=2.
    Original signal x(t) is defined as:
        0       for -3 <= t <= -1
        t+1     for -1 <= t <= 0
        1       for 0 <= t <= 1
        2-t     for 1 <= t <= 2
        0       for 2 <= t <= 3
    Then x(t+2) is:
        0       for -5 <= t <= -3
        (t+2)+1 = t+3  for -3 <= t <= -2
        1       for -2 <= t <= -1
        2-(t+2) = -t   for -1 <= t <= 0
        0       for 0 <= t <= 1
    """
    zero1 = axes.plot(lambda t: 0, x_range=[-5, -3], color=GREEN_C)
    ramp_up = axes.plot(lambda t: t + 3, x_range=[-3, -2], color=GREEN_C)
    flat = axes.plot(lambda t: 1, x_range=[-2, -1], color=GREEN_C)
    ramp_down = axes.plot(lambda t: -t, x_range=[-1, 0], color=GREEN_C)
    zero2 = axes.plot(lambda t: 0, x_range=[0, 1], color=GREEN_C)
    return VGroup(zero1, ramp_up, flat, ramp_down, zero2)



def create_shift_animation(scene, axes, formula, labels_data, corner=UR,
                           dot_color=RED, dot_radius=0.08, dot_run_time=1.0,
                           label_scale=0.7, label_color=GOLD):
    """
    Create a formula at the specified corner, then stack labels below it,
    and animate red dots from the left side of each label to its corresponding point on the axes.

    Parameters
    ----------
    scene : Scene
        The Manim scene.
    axes : Axes
        The coordinate system.
    formula : str
        LaTeX string for the formula (e.g. "x(t+2)").
    labels_data : list of dict
        Each dict: {"text": str, "point": (t, x)}.
        The order of the list defines the vertical stack (top to bottom).
    corner : str or list, default=UR
        Where to place the formula.
    dot_color : str, default=RED
        Color of the flying dots.
    dot_radius : float, default=0.08
        Radius of each dot.
    dot_run_time : float, default=1.0
        Duration of the dot's flight.
    label_scale : float, default=0.7
        Scale of the stacked labels.
    label_color : str, default=GOLD
        Color of the labels.

    Returns
    -------
    VGroup
        The formula and all stacked labels (useful for later removal).
    """
    # Create formula label
    formula_label = MathTex(formula, color=BLUE).scale(0.9).to_corner(corner)
    scene.play(Write(formula_label))
    
    # Build stacked labels
    labels_vgroup = VGroup()
    prev_label = formula_label
    first = True
    
    for data in labels_data:
        label = MathTex(data["text"], color=label_color).scale(label_scale)
        # Alignment: first label below formula aligned RIGHT, others LEFT
        if first:
            label.next_to(prev_label, DOWN, aligned_edge=RIGHT, buff=0.15)
            first = False
        else:
            label.next_to(prev_label, DOWN, aligned_edge=LEFT, buff=0.15)
        scene.play(Write(label))
        labels_vgroup.add(label)
        prev_label = label
    
    # Now animate dots from left side of each label to axes point
    for label, data in zip(labels_vgroup, labels_data):
        # Get left side of the label (a bit to the left for clarity)
        start_point = label.get_left() + LEFT * 0.2
        # Target point on axes
        t, x = data["point"]
        target_point = axes.c2p(t, x)
        
        dot = Dot(start_point, color=dot_color, radius=dot_radius)
        scene.add(dot)
        scene.play(dot.animate.move_to(target_point), run_time=dot_run_time, rate_func=rate_functions.ease_out_sine)
    
    return VGroup(formula_label, labels_vgroup)