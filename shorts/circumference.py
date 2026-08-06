## Video objective: To prove Circumference = 2πr using inscribed polygon approximation
## Format: 9:16 Vertical Video (Shorts / Reels / TikTok)

from manim import *
import numpy as np

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16
config.frame_rate = 60
config.background_color = "#0B0E14"


class CircumferenceProof(Scene):
    def construct(self):
        # ══════════════════════════════════════════════════════
        #  1. TITLE CARD
        # ══════════════════════════════════════════════════════
        header_bg = RoundedRectangle(
            corner_radius=0.3, height=1.3, width=8.2,
            fill_color="#141A24", fill_opacity=0.92,
            stroke_color=TEAL_C, stroke_width=2,
        ).move_to([0, 6.5, 0])

        title_tex = MathTex(
            "\\text{Why is } \\text{Circumference} = 2\\pi r\\text{?}",
            font_size=40,
        )
        title_tex.set_color_by_gradient(TEAL_B, BLUE_B, PURPLE_B)
        title_tex.move_to(header_bg.get_center())

        self.play(
            FadeIn(header_bg, shift=DOWN * 0.3),
            FadeIn(title_tex, scale=0.85),
            run_time=1.2,
        )
        self.wait(0.5)

        # ══════════════════════════════════════════════════════
        #  2. CIRCLE + RADIUS
        # ══════════════════════════════════════════════════════
        circle_center = np.array([0, 3.2, 0])
        max_r = 1.5

        border_circle = Circle(
            radius=max_r, color=GOLD, stroke_width=3,
        ).move_to(circle_center)  

        # Radius line
        radius_end = circle_center + RIGHT * max_r
        rad_line = Line(circle_center, radius_end, color=YELLOW, stroke_width=3.5)
        rad_dot = Dot(circle_center, color=YELLOW, radius=0.07)
        rad_label = MathTex("r", font_size=38, color=YELLOW)
        rad_label.next_to(rad_line, UP, buff=0.15)

        self.play(Create(border_circle), run_time=1.5)
        self.play(
            Create(rad_line),
            FadeIn(rad_dot),
            FadeIn(rad_label),
            run_time=0.8,
        )
        self.wait(0.5)

        # Show "C = ?" below the circle
        c_query = MathTex("C = \\ ?", font_size=44, color=WHITE)
        c_query.move_to(circle_center + DOWN * (max_r + 0.6))

        self.play(FadeIn(c_query, scale=0.8), run_time=0.6)
        self.wait(0.8)

        # Fade radius stuff before polygons
        self.play(
            FadeOut(rad_line), FadeOut(rad_dot),
            FadeOut(rad_label), FadeOut(c_query),
            run_time=0.5,
        )

        # ══════════════════════════════════════════════════════
        #  3. INSCRIBED POLYGON PROGRESSION
        # ══════════════════════════════════════════════════════
        subtitle_text = Text(
            "Inscribe polygons inside the circle...",
            font_size=22, color=GRAY_B,
        ).move_to([0, 1.0, 0])
        subtitle_text.set_opacity(0)
        self.play(subtitle_text.animate.set_opacity(1.0), run_time=0.4)

        # Perimeter card (smaller, top stays same)
        # Old: height=5.5, center at -4.6 => top at -1.85
        # New: height=3.8, center at -3.7 => top at -1.85 (same!)
        card_bg = RoundedRectangle(
            corner_radius=0.25, height=3.8, width=8.2,
            fill_color="#121722", fill_opacity=0.92,
            stroke_color=BLUE_E, stroke_width=2,
        ).move_to([0, -3.7, 0])

        card_heading = Text(
            "Polygon Perimeter vs Circumference",
            font_size=24, color=WHITE, weight=BOLD,
        ).move_to([0, -2.2, 0])

        self.play(FadeIn(card_bg, shift=UP * 0.3), Write(card_heading), run_time=0.7)

        # Polygon data: (n_sides, label, perimeter_formula, numerical_value)
        polygons_data = [
            (3, "Triangle", "3 \\times 2r \\times \\sin(60°)", "5.196r"),
            (4, "Square", "4 \\times 2r \\times \\sin(45°)", "5.657r"),
            (5, "Pentagon", "5 \\times 2r \\times \\sin(36°)", "5.878r"),
            (6, "Hexagon", "6 \\times 2r \\times \\sin(30°)", "6.000r"),
            (8, "Octagon", "8 \\times 2r \\times \\sin(22.5°)", "6.123r"),
            (12, "Dodecagon", "12 \\times 2r \\times \\sin(15°)", "6.211r"),
            (16, "16-gon", "16 \\times 2r \\times \\sin(11.25°)", "6.249r"),
            (24, "24-gon", "24 \\times 2r \\times \\sin(7.5°)", "6.269r"),
        ]

        palette = [RED, ORANGE, YELLOW, GREEN, TEAL, BLUE, PURPLE, PINK]

        prev_polygon = None
        prev_n_label = None
        prev_formula = None

        # Single fixed position for all formulas (centered in card)
        formula_fixed_y = -3.5

        for idx, (n, name, formula_tex, value) in enumerate(polygons_data):
            color = palette[idx % len(palette)]

            # ── Draw inscribed polygon ──
            vertices = []
            for k in range(n):
                angle = TAU * k / n - PI / 2  # Start from top
                v = circle_center + max_r * np.array([np.cos(angle), np.sin(angle), 0])
                vertices.append(v)

            polygon = Polygon(
                *vertices, color=color, stroke_width=3.5,
                fill_color=color, fill_opacity=0.12,
            )

            # Side count label
            n_label = MathTex(f"n = {n}", font_size=34, color=color)
            n_label.next_to(border_circle, LEFT, buff=0.5).shift(DOWN * 0.3)

            # Perimeter formula — single centered line
            full_str = f"P_{{{n}}} = {formula_tex} = {value}"
            perim_formula = MathTex(full_str, font_size=34, color=color)
            perim_formula.move_to([0, formula_fixed_y, 0])

            # Animate polygon appearing
            anims = [Create(polygon), FadeIn(n_label)]

            if prev_polygon is not None:
                anims.extend([
                    ReplacementTransform(prev_polygon, polygon),
                    ReplacementTransform(prev_n_label, n_label),
                ])

            self.play(*anims, run_time=0.7)
            self.wait(0.15)

            # Show formula
            if prev_formula is not None:
                self.play(
                    ReplacementTransform(prev_formula, perim_formula),
                    run_time=0.35,
                )
            else:
                self.play(Write(perim_formula), run_time=0.5)

            self.wait(0.2)

            prev_polygon = polygon
            prev_n_label = n_label
            prev_formula = perim_formula

        self.wait(0.5)

        # ══════════════════════════════════════════════════════
        #  4. LIMIT TRANSITION — Polygon merges into circle
        # ══════════════════════════════════════════════════════
        self.play(
            ReplacementTransform(prev_polygon, border_circle),
            FadeOut(prev_n_label),
            run_time=1.0,
        )

        # Circle color pulse: GOLD → WHITE → GOLD
        self.play(border_circle.animate.set_color(WHITE), run_time=0.3)
        self.play(border_circle.animate.set_color(GOLD), run_time=0.3)

        # Show the limit formula (shifted up)
        limit_card = RoundedRectangle(
            corner_radius=0.3, height=3.2, width=8.2,
            fill_color="#121722", fill_opacity=0.95,
            stroke_color=GOLD_E, stroke_width=2.5,
        ).move_to([0, -4.2, 0])

        limit_title = Text(
            "Taking the Limit as n → ∞",
            font_size=26, color=GOLD, weight=BOLD,
        ).move_to([0, -3.1, 0])

        limit_f1 = MathTex(
            "\\lim_{n \\to \\infty} \\, n \\times 2r \\times \\sin\\!\\left(\\frac{\\pi}{n}\\right)",
            font_size=26, color=BLUE_B,
        ).move_to([0, -3.8, 0])

        limit_f2 = MathTex(
            "= \\, 2\\pi r",
            font_size=34, color=GOLD,
        ).move_to([0, -4.5, 0])

        # Staggered fade-out: formula first, then card
        if prev_formula is not None:
            self.play(FadeOut(prev_formula), run_time=0.3)
        self.play(
            FadeOut(card_bg), FadeOut(card_heading),
            FadeOut(subtitle_text),
            run_time=0.5,
        )

        self.play(FadeIn(limit_card, shift=UP * 0.2), run_time=0.5)
        self.play(Write(limit_title), run_time=0.6)
        self.wait(0.3)
        self.play(Write(limit_f1), run_time=0.9)
        self.wait(0.4)

        # Animate f1 → f2
        self.play(Write(limit_f2), run_time=0.8)
        self.wait(0.5)

        # ══════════════════════════════════════════════════════
        #  5. FINAL REVEAL — C = 2πr
        # ══════════════════════════════════════════════════════
        final_tex = MathTex(
            "\\text{Circumference} = 2\\pi r",
            font_size=52,
        )
        final_tex.set_color_by_gradient(GOLD, ORANGE)
        final_tex.move_to([0, -2.0, 0])

        final_box = SurroundingRectangle(
            final_tex, color=GOLD, buff=0.25,
            stroke_width=3.5, corner_radius=0.15,
        )

        self.play(
            FadeOut(limit_card), FadeOut(limit_title),
            FadeOut(limit_f1), FadeOut(limit_f2),
            run_time=0.4,
        )

        self.play(
            FadeIn(final_tex, scale=0.7),
            Create(final_box),
            run_time=1.5,
        )
        self.wait(0.5)

        # Pulse effect on final formula
        self.play(
            final_tex.animate.scale(1.06),
            run_time=0.4,
            rate_func=there_and_back,
        )
        self.play(
            final_tex.animate.scale(1.06),
            run_time=0.4,
            rate_func=there_and_back,
        )

        self.wait(2.5)
