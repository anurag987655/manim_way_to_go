from manim import *
from transformation.base_signal import make_discrete_axes, add_axis_labels, build_discrete_signal

# Data for the discrete signal
DISCRETE_DATA = {
    -3: 1,
    -2: 2,
    -1: 1,
    0: 3,  # This is the origin point
    1: 2,
    2: 0.5,
    3: -1
}

class DiscreteSignalPlotting(Scene):
    def construct(self):
        # Title
        title = Text("Understanding Discrete Signals", font_size=48).to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

        # Case 1: Discrete signal with origin arrow
        self.next_section("With Origin Arrow", skip_animations=False)
        case1_title = Text("Discrete Signal with Origin Indication", font_size=36, color=BLUE).to_edge(UP)
        self.play(Write(case1_title))

        axes1 = make_discrete_axes(x_range=[-4, 4, 1], y_range=[-2, 4, 1])
        labels1 = add_axis_labels(axes1, "n", "x[n]")
        signal1 = build_discrete_signal(axes1, DISCRETE_DATA)

        # Explicit origin arrow
        origin_point = axes1.coords_to_point(0, 0)
        origin_arrow = Arrow(origin_point + DOWN * 0.5, origin_point, buff=0.1, color=RED, tip_length=0.2)
        origin_text = Text("Origin (n=0)", font_size=24, color=RED).next_to(origin_arrow, DOWN)

        self.play(Create(axes1), Create(labels1))
        self.play(Create(signal1))
        self.wait(0.5)
        self.play(GrowArrow(origin_arrow), Write(origin_text))
        self.wait(2)

        explanation1 = Text(
            "An arrow often indicates the origin (n=0) for clarity.",
            font_size=28
        ).next_to(signal1, DOWN, buff=0.7)
        self.play(Write(explanation1))
        self.wait(3)
        self.play(FadeOut(VGroup(signal1, origin_arrow, origin_text, explanation1, case1_title)))
        self.play(FadeOut(axes1, labels1))


        # Case 2: Discrete signal without explicit origin arrow
        self.next_section("Without Origin Arrow", skip_animations=False)
        case2_title = Text("Discrete Signal without Explicit Origin Indication", font_size=36, color=GREEN).to_edge(UP)
        self.play(Write(case2_title))

        axes2 = make_discrete_axes(x_range=[-4, 4, 1], y_range=[-2, 4, 1])
        labels2 = add_axis_labels(axes2, "n", "x[n]")
        signal2 = build_discrete_signal(axes2, DISCRETE_DATA)

        self.play(Create(axes2), Create(labels2))
        self.play(Create(signal2))
        self.wait(0.5)

        explanation2 = Text(
            "Sometimes, the origin is implied by the graph's structure.",
            font_size=28
        ).next_to(signal2, DOWN, buff=0.7)
        self.play(Write(explanation2))
        self.wait(3)
        self.play(FadeOut(VGroup(signal2, explanation2, case2_title)))
        self.play(FadeOut(axes2, labels2))

        final_text = Text("Discrete signals are crucial in digital signal processing.", font_size=36)
        self.play(Write(final_text))
        self.wait(2)
        self.play(FadeOut(final_text))
