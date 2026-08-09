## Video objective: Show WHY the radius is perpendicular to the tangent.
## A line that is NOT perpendicular slices the circle at TWO points (secant).
## Sweep it down toward the perpendicular: the second intersection slides along
## the circle — at exactly 90° the two points merge into ONE → the tangent.
## Format: 9:16 Vertical Video (Shorts / Reels / TikTok)

from manim import *
import numpy as np

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16
config.frame_rate = 60
config.background_color = "#0B0E14"


class TangentPerpendicular(Scene):
    def construct(self):
        # ══════════════════════════════════════════════════════
        #  GEOMETRY — P on BOTTOM, radius VERTICAL, tangent HORIZONTAL
        # ══════════════════════════════════════════════════════
        center = np.array([0, 2.55, 0])   # O
        max_r = 1.7
        P = center + DOWN * max_r         # point of contact, bottom of circle

        D50 = np.radians(50)              # sweep start (secant, NOT tangent)
        D90 = PI / 2                      # sweep end  (the tangent)

        angle_tracker = ValueTracker(D50)

        def d():                          # line unit direction at angle θ from radius
            th = angle_tracker.get_value()
            return np.array([np.sin(th), np.cos(th), 0])

        def q_of():                       # second intersection with the circle
            th = angle_tracker.get_value()
            return P + 2 * max_r * np.cos(th) * np.array([np.sin(th), np.cos(th), 0])

        def progress():                   # 0 .. 1 over the sweep (50° → 90°)
            return np.clip((angle_tracker.get_value() - D50) / (D90 - D50), 0.0, 1.0)

        def color_at():                   # bright magenta → GOLD as it becomes tangent
            return interpolate_color(PINK, GOLD, progress())

        # ── Line rotating about P, color follows the angle ──
        swing_line = always_redraw(lambda: Line(
            P - 2.2 * d(),
            P + 2.2 * d(),
            stroke_width=5,
        ).set_color(color_at()))

        # ── Inner secant segment (the part cutting the circle) ──
        chord = always_redraw(lambda: Line(P, q_of(), color=RED, stroke_width=6))

        # ── Second intersection dot: slides along the circle, merges at P ──
        q_dot = always_redraw(lambda: Dot(q_of(), radius=0.095, color=RED))

        # ── Q label rides on the second dot (bright & bold) ──
        q_label = always_redraw(lambda: Text(
            "Q", font_size=26, color=RED_A, weight=BOLD,
        ).move_to(q_of() + UR * 0.12))

        # ── Continuous angle readout: rides on Q, drifting outward ──
        readout = always_redraw(lambda: Text(
            f"\u03b8 = {int(round(np.degrees(angle_tracker.get_value())))}\u00b0",
            font_size=30, color=GRAY_B,
        ).move_to(q_of() + 1.1 * (q_of() - center) / max_r))

        # ══════════════════════════════════════════════════════
        #  1. TITLE CARD
        # ══════════════════════════════════════════════════════
        header_bg = RoundedRectangle(
            corner_radius=0.3, height=1.3, width=8.2,
            fill_color="#141A24", fill_opacity=0.92,
            stroke_color=TEAL_C, stroke_width=2,
        ).move_to([0, 6.2, 0])

        title_tex = MathTex(
            "\\text{Why is Radius } \\perp \\text{ Tangent?}",
            font_size=38,
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
        #  2. SETUP — circle + VERTICAL radius (bright cyan)
        # ══════════════════════════════════════════════════════
        circle = Circle(
            radius=max_r, color=WHITE, stroke_width=3,
        ).move_to(center)

        radius_line = Line(center, P, color=TEAL_A, stroke_width=3.5)
        o_dot = Dot(center, color=TEAL_A, radius=0.07)
        r_label = MathTex("r", font_size=38, color=TEAL_A)
        r_label.next_to(radius_line, LEFT, buff=0.12)

        p_dot = Dot(P, color=GOLD, radius=0.09)
        p_label = Text("P", font_size=26, color=GOLD, weight=BOLD)
        p_label.next_to(P, DOWN, buff=0.1)

        self.play(Create(circle), run_time=1.2)
        self.play(
            Create(radius_line), FadeIn(o_dot),
            Write(r_label), FadeIn(p_dot), Write(p_label),
            run_time=0.8,
        )
        self.wait(0.4)

        # ══════════════════════════════════════════════════════
        #  3. THE LINE IS NOT A TANGENT — it arrives SLICING the circle
        # ══════════════════════════════════════════════════════
        self.play(
            Create(swing_line),
            Create(chord),
            FadeIn(q_dot),
            FadeIn(q_label),
            FadeIn(readout, scale=0.8),
            run_time=1.1,
        )

        secant_chip = RoundedRectangle(
            corner_radius=0.25, height=0.7, width=6.0,
            fill_color="#2A1016", fill_opacity=0.95,
            stroke_color=RED_A, stroke_width=2,
        ).move_to([0, -1.4, 0])
        secant_txt = Text(
            "PQ is a SECANT",
            font_size=23, color=RED_A, weight=BOLD,
        ).move_to(secant_chip.get_center())

        self.play(
            FadeIn(secant_chip, shift=UP * 0.2),
            Write(secant_txt),
            run_time=0.7,
        )
        self.wait(0.6)

        # ══════════════════════════════════════════════════════
        #  4. THE SWEEP — trace the angle as the line comes down
        # ══════════════════════════════════════════════════════
        sweep_tease = Text(
            "Sweep it down... watch θ trace the way!",
            font_size=24, color=GRAY_B,
        ).move_to([0, -1.4, 0])
        sweep_tease.set_opacity(0)
        self.play(
            FadeOut(secant_chip), FadeOut(secant_txt),
            FadeIn(sweep_tease),
            run_time=0.5,
        )

        self.play(
            angle_tracker.animate.set_value(D90),
            run_time=3.0,
            rate_func=smooth,
        )
        self.wait(0.4)

        # ══════════════════════════════════════════════════════
        #  5. THE MERGE — at exactly 90° the two points become ONE
        # ══════════════════════════════════════════════════════
        self.remove(q_dot, chord)
        self.play(
            FadeOut(sweep_tease),
            FadeOut(q_label),
            run_time=0.4,
        )

        tangent_chip = RoundedRectangle(
            corner_radius=0.25, height=0.7, width=6.0,
            fill_color="#0F2A1E", fill_opacity=0.95,
            stroke_color=GREEN_B, stroke_width=2,
        ).move_to([0, -1.4, 0])
        tangent_txt = Text(
            "P is now a TANGENT",
            font_size=23, color=GREEN_B, weight=BOLD,
        ).move_to(tangent_chip.get_center())
        self.play(
            FadeIn(tangent_chip, shift=UP * 0.2),
            Write(tangent_txt),
            run_time=0.7,
        )
        self.wait(0.6)

        # ── Right-angle marker at P (between radius ↑ and line →) ──
        cs = 0.32
        ra_corner = VGroup(
            Line(P, P + RIGHT * cs, color=GREEN_E, stroke_width=3.5),
            Line(P + RIGHT * cs, P + RIGHT * cs + UP * cs, color=GREEN_E, stroke_width=3.5),
            Line(P + RIGHT * cs + UP * cs, P + UP * cs, color=GREEN_E, stroke_width=3.5),
        )
        self.play(Create(ra_corner), run_time=0.7)
        self.wait(0.4)

        # ══════════════════════════════════════════════════════
        #  6. THE "WHY" CARD
        # ══════════════════════════════════════════════════════
        why_card = RoundedRectangle(
            corner_radius=0.3, height=3.6, width=8.2,
            fill_color="#121722", fill_opacity=0.92,
            stroke_color=GOLD_E, stroke_width=2.5,
        ).move_to([0, -4.3, 0])

        w1 = MathTex(
            "\\text{\\textbf{Any other angle: touches the circle TWICE}}",
            font_size=30, color=RED,
        ).move_to([0, -3.45, 0])
        w2 = MathTex(
            "\\text{\\textbf{At }} 90^\\circ\\text{\\textbf{: touches it in exactly ONE point}}",
            font_size=30, color=TEAL_A,
        ).move_to([0, -4.35, 0])
        w3 = MathTex(
            "\\\\therefore \\ \\text{\\textbf{Radius}} \\perp \\text{\\textbf{Tangent}}",
            font_size=36, color=GOLD,
        ).move_to([0, -5.2, 0])

        self.play(
            FadeIn(why_card, shift=UP * 0.3),
            FadeOut(tangent_chip),
            FadeOut(tangent_txt),
            FadeOut(readout),
            run_time=0.5,
        )
        self.play(Write(w1), run_time=0.7)
        self.wait(0.3)
        self.play(Write(w2), run_time=0.7)
        self.wait(0.3)
        self.play(Write(w3), run_time=0.9)
        self.wait(0.8)

        # ══════════════════════════════════════════════════════
        #  7. FINALE
        # ══════════════════════════════════════════════════════
        final_tex = MathTex(
            "\\text{\\textbf{Tangent}} \\perp \\text{\\textbf{Radius}}",
            font_size=50,
        )
        final_tex.set_color_by_gradient(GOLD, ORANGE)
        final_tex.move_to([0, -0.8, 0])

        final_box = SurroundingRectangle(
            final_tex, color=GOLD, buff=0.25,
            stroke_width=3.5, corner_radius=0.15,
        )

        self.play(
            FadeOut(why_card), FadeOut(w1), FadeOut(w2), FadeOut(w3),
            FadeOut(p_dot), FadeOut(p_label),
            run_time=0.5,
        )
        self.play(
            FadeIn(final_tex, scale=0.7),
            Create(final_box),
            run_time=1.4,
        )
        self.wait(0.5)

        for _ in range(2):
            self.play(
                final_tex.animate.scale(1.05),
                run_time=0.35, rate_func=there_and_back,
            )

        self.wait(2.6)