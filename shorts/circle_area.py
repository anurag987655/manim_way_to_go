## Video objective: To animate why Circle Area = πr² using concentric rings unrolling into a triangle
## Format: 9:16 Vertical Video (Shorts / Reels / TikTok)

from manim import *
import numpy as np

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16
config.frame_rate = 60
config.background_color = "#0B0E14"


class CircleArea(Scene):
    def construct(self):
        # ── 1. Header Title Card ──
        header_card = RoundedRectangle(
            corner_radius=0.25,
            height=1.2,
            width=8.0,
            fill_color="#141A24",
            fill_opacity=0.9,
            stroke_color=TEAL_C,
            stroke_width=2,
        ).move_to(np.array([0, 6.5, 0]))

        title_text = MathTex(
            "\\text{Why is } \\text{Area} = \\pi r^2?",
            font_size=42,
        ).move_to(header_card.get_center())
        title_text.set_color_by_gradient(TEAL_B, BLUE_B, PURPLE_B)

        self.play(
            FadeIn(header_card, shift=DOWN * 0.3),
            Write(title_text),
            run_time=1.0,
        )
        self.wait(0.3)

        # ── 2. Geometric Setup & Parameters ──
        num_rings = 16
        circle_center = np.array([0, 3.1, 0])
        max_radius = 1.45
        stack_base_y = -0.5
        line_scale = 0.50  # Base width: 2 * pi * 1.45 * 0.50 = 4.55
        ring_thickness = 0.165

        # Rich neon gradient palette across concentric rings
        palette = [RED, ORANGE, YELLOW, GREEN, TEAL, BLUE, PURPLE, PINK]
        colors = color_gradient(palette, num_rings)

        # Create Arc rings & stacked Line strips
        rings = []
        lines = []

        for i in range(num_rings):
            # Outer ring (i=0) to inner ring (i=num_rings-1)
            r = max_radius * (num_rings - i) / num_rings
            ring = Arc(
                radius=r,
                start_angle=PI / 2,
                angle=-TAU + 0.001,
                stroke_width=8.5,
                color=colors[i],
            )
            ring.move_to(circle_center)
            rings.append(ring)

            line_len = 2 * PI * r * line_scale
            y = stack_base_y + i * ring_thickness
            line = Line(
                LEFT * line_len / 2,
                RIGHT * line_len / 2,
                stroke_width=8.5,
                color=colors[i],
            )
            line.move_to(np.array([0, y, 0]))
            lines.append(line)

        # Outer boundary circle & radius line
        border_circle = Circle(
            radius=max_radius,
            color=WHITE,
            stroke_width=2.5,
            stroke_opacity=0.6,
        ).move_to(circle_center)

        radius_line = Line(
            circle_center,
            circle_center + RIGHT * max_radius,
            color=YELLOW,
            stroke_width=3.5,
        )
        radius_dot = Dot(circle_center, color=YELLOW, radius=0.07)
        radius_label = MathTex("r", font_size=38, color=YELLOW).next_to(
            radius_line, UP, buff=0.12
        )

        # ── 3. Animate Circle & Concentric Rings Creation ──
        self.play(
            Create(border_circle),
            *[Create(ring) for ring in rings],
            run_time=1.8,
        )
        self.play(
            Create(radius_dot),
            Create(radius_line),
            Write(radius_label),
            run_time=0.8,
        )
        self.wait(0.6)

        # Fade out radius indicator before ring unrolling
        self.play(
            FadeOut(radius_line),
            FadeOut(radius_dot),
            FadeOut(radius_label),
            run_time=0.4,
        )

        # ── 4. Peeling & Unrolling Transition (Rings -> Triangle Stack) ──
        unroll_sub = Text(
            "Unroll concentric rings into straight strips...",
            font_size=24,
            color=GRAY_A,
        ).move_to(np.array([0, 1.2, 0]))
        unroll_sub.set_opacity(0.0)
        self.play(unroll_sub.animate.set_opacity(1.0), run_time=0.4)

        # Staggered morphing of rings into stacked triangle strips
        # Text dims with each ring; disappears when top (innermost) ring arrives
        for i in range(num_rings):
            if i < num_rings - 1:
                self.play(
                    ReplacementTransform(rings[i], lines[i]),
                    unroll_sub.animate.set_opacity(1.0 - (i + 1) / num_rings),
                    run_time=0.2,
                )
            else:
                self.play(
                    ReplacementTransform(rings[i], lines[i]),
                    FadeOut(unroll_sub),
                    run_time=0.2,
                )

        self.play(FadeOut(border_circle), run_time=0.5)
        self.wait(0.4)

        # ── 5. Form Triangle Boundary & Annotations ──
        base_width = 2 * PI * max_radius * line_scale
        triangle_height = num_rings * ring_thickness

        triangle_outline = Polygon(
            np.array([-base_width / 2, stack_base_y - 0.08, 0]),
            np.array([base_width / 2, stack_base_y - 0.08, 0]),
            np.array([0, stack_base_y + triangle_height + 0.05, 0]),
            color=WHITE,
            stroke_width=2.5,
            stroke_opacity=0.7,
            fill_opacity=0.06,
            fill_color=BLUE,
        )

        self.play(
            Create(triangle_outline),
            FadeOut(unroll_sub),
            run_time=0.8,
        )

        # Base Brace (2πr) - Bottom
        base_brace_line = Line(
            np.array([-base_width / 2, stack_base_y - 0.15, 0]),
            np.array([base_width / 2, stack_base_y - 0.15, 0]),
        )
        base_brace = Brace(base_brace_line, DOWN, color=GOLD)
        base_label = MathTex("\\text{Base} = 2\\pi r", font_size=30, color=GOLD).next_to(
            base_brace, DOWN, buff=0.1
        )

        # Height Brace (r) - Placed safely on the RIGHT side
        height_guide = Line(
            np.array([base_width / 2 + 0.15, stack_base_y, 0]),
            np.array([base_width / 2 + 0.15, stack_base_y + triangle_height, 0]),
        )
        height_brace = Brace(height_guide, RIGHT, color=YELLOW, buff=0.05)
        height_label = MathTex("\\text{Height} = r", font_size=28, color=YELLOW).next_to(
            height_brace, RIGHT, buff=0.08
        )

        self.play(
            Create(base_brace),
            Write(base_label),
            Create(height_brace),
            Write(height_label),
            run_time=1.0,
        )
        self.wait(0.6)

        # ── 6. Step-by-Step Derivation Card ──
        card_bg = RoundedRectangle(
            corner_radius=0.3,
            height=4.6,
            width=8.2,
            fill_color="#121722",
            fill_opacity=0.92,
            stroke_color=BLUE_E,
            stroke_width=2,
        ).move_to(np.array([0, -4.8, 0]))

        card_heading = Text(
            "Area of Triangle = Area of Circle",
            font_size=24,
            color=WHITE,
            weight=BOLD,
        ).move_to(np.array([0, -3.0, 0]))

        f1 = MathTex(
            "\\text{Area} = \\frac{1}{2} \\times \\text{Base} \\times \\text{Height}",
            font_size=30,
            color=BLUE_B,
        ).move_to(np.array([0, -3.7, 0]))

        f2 = MathTex(
            "\\text{Area} = \\frac{1}{2} \\times (2\\pi r) \\times (r)",
            font_size=30,
            color=TEAL_B,
        ).move_to(np.array([0, -4.5, 0]))

        f3 = MathTex(
            "\\text{Area} = \\pi r^2",
            font_size=42,
            color=GOLD,
        ).move_to(np.array([0, -5.6, 0]))

        highlight_box = SurroundingRectangle(
            f3,
            color=GOLD,
            buff=0.18,
            stroke_width=3,
            corner_radius=0.12,
        )

        # Animate derivation card
        self.play(FadeIn(card_bg, shift=UP * 0.3), Write(card_heading), run_time=0.8)
        self.play(Write(f1), run_time=0.8)
        self.wait(0.4)
        self.play(Write(f2), run_time=0.9)
        self.wait(0.4)
        self.play(TransformMatchingTex(f2.copy(), f3), run_time=1.0)
        self.play(
            Create(highlight_box),
            f3.animate.scale(1.08),
            run_time=0.6,
        )
        self.wait(2.5)
