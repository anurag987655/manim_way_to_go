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
    """Create a MathTex label at the requested screen corner."""
    return MathTex(text, color=color).scale(scale_factor).to_corner(position)


def animate_sample_points(scene, axes, sample_points, next_label_anchor,
                          dot_color=YELLOW, label_color=GOLD,
                          label_scale=0.7, dot_radius=0.08):
    """Animate sample points and move their labels below the anchor."""
    dots = VGroup()
    labels = VGroup()

    for t_value, x_value in sample_points:
        dot = Dot(axes.c2p(t_value, x_value), color=dot_color, radius=dot_radius)
        label = MathTex(f"x({t_value})={x_value}", color=label_color).scale(label_scale)
        label.next_to(dot, UP, buff=0.2)

        scene.play(FadeIn(dot), run_time=0.4)
        scene.play(Write(label), run_time=0.4)
        scene.play(dot.animate.shift(RIGHT * 0.15 + UP * 0.05), run_time=0.4)

        target_position = label.copy().next_to(next_label_anchor, DOWN, aligned_edge=LEFT, buff=0.1)
        scene.play(Transform(label, target_position), run_time=0.5)
        scene.wait(0.2)

        dots.add(dot)
        labels.add(label)
        next_label_anchor = label

    return dots, labels


def build_custom_signal(axes):
    # 1. zero: (-3 to -1), value = 0
    zero1 = axes.plot(
        lambda t: 0,
        x_range=[-3, -1],
        color=GREEN_C
    )

    # 2. ramp up: (-1 to 0), 0 → 1
    ramp_up = axes.plot(
        lambda t: t + 1,
        x_range=[-1, 0],
        color=GREEN_C
    )

    # 3. flat: (0 to 1), value = 1
    flat = axes.plot(
        lambda t: 1,
        x_range=[0, 1],
        color=GREEN_C
    )

    # 4. ramp down: (1 to 2), 1 → 0
    ramp_down = axes.plot(
        lambda t: 2 - t,
        x_range=[1, 2],
        color=GREEN_C
    )

    # 5. zero: (2 to 3), value = 0
    zero2 = axes.plot(
        lambda t: 0,
        x_range=[2, 3],
        color=GREEN_C
    )

    return VGroup(zero1, ramp_up, flat, ramp_down, zero2)
