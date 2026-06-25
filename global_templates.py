from manim import *


def ct_axes(
    x_range=[-6, 6, 1],
    y_range=[-0.5, 2, 0.5],
    x_label="t",
    y_label="x(t)",
    buff=0.1
):
    axes = Axes(
        x_range=x_range,
        y_range=y_range,
        axis_config={"color": GREY_B},
        x_axis_config={"include_numbers": True},
        y_axis_config={"include_numbers": True},
    ).scale(0.9)

    x_lab = MathTex(x_label, color=WHITE).scale(0.8).next_to(
        axes.x_axis, RIGHT, buff=buff
    )
    y_lab = MathTex(y_label, color=WHITE).scale(0.8).next_to(
        axes.y_axis, UP, buff=buff
    )

    group = VGroup(axes, x_lab, y_lab)
    return group, x_lab, y_lab


def dt_axes(
    x_range=[-7, 7, 1],
    y_range=[-3, 4, 1],
    x_label="n",
    y_label="x[n]",
    buff=0.1
):
    axes = Axes(
        x_range=x_range,
        y_range=y_range,
        axis_config={"color": GREY_B},
        x_axis_config={"include_numbers": True},
        y_axis_config={"include_numbers": True},
    ).scale(0.9)

    x_lab = MathTex(x_label, color=WHITE).scale(0.8).next_to(
        axes.x_axis, RIGHT, buff=buff
    )
    y_lab = MathTex(y_label, color=WHITE).scale(0.8).next_to(
        axes.y_axis, UP, buff=buff
    )

    group = VGroup(axes, x_lab, y_lab)
    return group, x_lab, y_lab
