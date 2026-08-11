## Video objective: Show WHY the angle in a semicircle is always 90° (Thales' theorem).
## A glides along the semicircle while ∠PAQ stays glued at 90°, then a short
## proof: OP = OQ = OA (radii) → two isosceles triangles → base angles α, β
## → 2(α+β) = 180° → ∠PAQ = α+β = 90°.
## Format: 9:16 Vertical Video (Shorts / Reels / TikTok)

from manim import *
import numpy as np

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16
config.frame_rate = 60
config.background_color = "#0B0E14"


class SemicircleAngle90(Scene):
    def construct(self):
        # ══════════════════════════════════════════════════════
        #  GEOMETRY — O at center, PQ horizontal diameter
        # ══════════════════════════════════════════════════════
        center = np.array([0, 3.1, 0])
        max_r = 1.7
        P = center + LEFT * max_r
        Q = center + RIGHT * max_r

        theta_tracker = ValueTracker(PI / 2)  # A starts at top of semicircle

        def a():
            th = theta_tracker.get_value()
            return center + max_r * np.array([np.cos(th), np.sin(th), 0])

        # ══════════════════════════════════════════════════════
        #  1. TITLE CARD
        # ══════════════════════════════════════════════════════
        header_bg = RoundedRectangle(
            corner_radius=0.3, height=1.3, width=8.2,
            fill_color="#141A24", fill_opacity=0.92,
            stroke_color=TEAL_C, stroke_width=2,
        ).move_to([0, 6.5, 0])

        title_tex = MathTex(
            "\\text{Why is the Angle in a Semicircle } 90^\\circ\\text{?}",
            font_size=36,
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
        #  2. CIRCLE (gold + glow) & DIAMETER PQ
        # ══════════════════════════════════════════════════════
        halo1 = Circle(
            radius=max_r + 0.1, color=GOLD,
            stroke_width=10, stroke_opacity=0.22,
        ).move_to(center)
        halo2 = Circle(
            radius=max_r + 0.24, color=GOLD,
            stroke_width=14, stroke_opacity=0.10,
        ).move_to(center)
        circle = Circle(
            radius=max_r, color=GOLD, stroke_width=3.5,
        ).move_to(center)

        self.play(
            Create(circle),
            FadeIn(halo1, rate_func=rush_into),
            FadeIn(halo2, rate_func=rush_into),
            run_time=1.2,
        )
        self.wait(0.3)

        diameter = Line(P, Q, color=GOLD_E, stroke_width=4)
        p_dot = Dot(P, color=GOLD, radius=0.09)
        q_dot = Dot(Q, color=GOLD, radius=0.09)
        p_label = Text("P", font_size=28, color=GOLD, weight=BOLD)
        p_label.next_to(P, DOWN, buff=0.12).shift(LEFT * 0.05)
        q_label = Text("Q", font_size=28, color=GOLD, weight=BOLD)
        q_label.next_to(Q, DOWN, buff=0.12).shift(RIGHT * 0.05)

        self.play(
            Create(diameter), FadeIn(p_dot), FadeIn(q_dot),
            Write(p_label), Write(q_label),
            run_time=0.9,
        )
        self.wait(0.3)

        # ══════════════════════════════════════════════════════
        #  3. CENTER O — small dot
        # ══════════════════════════════════════════════════════
        o_dot = Dot(center, color=WHITE, radius=0.06)
        o_label = Text("O", font_size=26, color=WHITE, weight=BOLD)
        o_label.next_to(center, DOWN, buff=0.14).shift(DOWN * 0.0)

        self.play(FadeIn(o_dot), Write(o_label), run_time=0.6)
        self.wait(0.3)

        # ══════════════════════════════════════════════════════
        #  4. THE GLIDE — A moves, ∠PAQ stays 90°
        # ══════════════════════════════════════════════════════
        ap = always_redraw(lambda: Line(a(), P, color=TEAL_B, stroke_width=4.5))
        aq = always_redraw(lambda: Line(a(), Q, color=PINK, stroke_width=4.5))
        a_dot = always_redraw(lambda: Dot(a(), radius=0.1, color=GOLD))
        a_label = always_redraw(lambda: Text(
            "A", font_size=28, color=GOLD, weight=BOLD,
        ).move_to(a() + UP * 0.18 + LEFT * 0.05))

        angle_mark = always_redraw(lambda: Angle(
            Line(a(), P), Line(a(), Q),
            radius=0.38, color=GOLD, stroke_width=3.5,
        ))
        angle_label = always_redraw(lambda: Text(
            "90°", font_size=26, color=GOLD, weight=BOLD,
        ).move_to(a() + normalize((P - a()) + (Q - a())) * 0.9))

        teaser = Text(
            "A glides along the circle — ∠PAQ stays 90°!",
            font_size=23, color=GRAY_B,
        ).move_to([0, 0.6, 0])

        self.play(
            Create(ap), Create(aq),
            FadeIn(a_dot), Write(a_label),
            Create(angle_mark), FadeIn(angle_label, scale=0.7),
            FadeIn(teaser),
            run_time=1.2,
        )
        self.wait(0.4)

        # Continuous back-and-forth gliding (θ: π/2 → π → 0 → π/2)
        self.play(theta_tracker.animate.set_value(PI - 0.02), run_time=2.0, rate_func=smooth)
        self.play(theta_tracker.animate.set_value(0.02), run_time=4.0, rate_func=smooth)
        self.play(theta_tracker.animate.set_value(PI / 2), run_time=2.0, rate_func=smooth)
        self.wait(0.4)

        # ══════════════════════════════════════════════════════
        #  5. THE "WHY?" QUESTION
        # ══════════════════════════════════════════════════════
        why_card = RoundedRectangle(
            corner_radius=0.25, height=0.75, width=6.4,
            fill_color="#241A0F", fill_opacity=0.95,
            stroke_color=GOLD_E, stroke_width=2,
        ).move_to([0, 0.6, 0])
        why_txt = Text(
            "Why is it always 90°?",
            font_size=27, color=GOLD, weight=BOLD,
        ).move_to(why_card.get_center())

        self.play(
            FadeOut(teaser),
            FadeIn(why_card, shift=UP * 0.2),
            Write(why_txt),
            run_time=0.7,
        )
        self.wait(0.6)

        # ══════════════════════════════════════════════════════
        #  6. THE PROOF — below, in a rectangle, bigger font
        # ══════════════════════════════════════════════════════
        # Move A to the top and draw OA first
        self.play(theta_tracker.animate.set_value(PI / 2), run_time=0.8)
        self.play(
            FadeOut(why_card), FadeOut(why_txt),
            run_time=0.4,
        )

        proof_card = RoundedRectangle(
            corner_radius=0.3, height=5.1, width=8.2,
            fill_color="#121722", fill_opacity=0.93,
            stroke_color=BLUE_E, stroke_width=2,
        ).move_to([0, -4.35, 0])
        proof_head = Text(
            "THE PROOF", font_size=21, color=GRAY_B, weight=BOLD,
        ).move_to([0, -2.35, 0])

        self.play(FadeIn(proof_card, shift=UP * 0.3), Write(proof_head), run_time=0.6)

        oa_line = DashedLine(center, a(), color=YELLOW, stroke_width=3.5)
        self.play(Create(oa_line), run_time=0.5)

        # Labels: OP = OQ = OA — all radii
        p1 = MathTex(
            "OP = OQ = OA", "\\quad (\\text{all are radii})",
            font_size=32,
        ).move_to([0, -3.05, 0])
        p1[0].set_color(GOLD)
        p1[1].set_color(WHITE)
        p1_box = SurroundingRectangle(
            p1, color=GOLD, buff=0.16, stroke_width=2.5, corner_radius=0.12,
        )

        self.play(Write(p1), run_time=0.8)
        self.play(Create(p1_box), run_time=0.4)
        self.wait(0.3)
        self.play(FadeOut(p1_box), run_time=0.3)

        # Isosceles triangles
        p2 = MathTex(
            "\\triangle AOP \\ \\text{and}\\ \\triangle AOQ \\ \\text{are isosceles}",
            font_size=28, color=TEAL_B,
        ).move_to([0, -3.75, 0])
        self.play(Write(p2), run_time=0.7)
        self.wait(0.2)

        # Base angles marked on the diagram: α and β
        arc_rad = 0.3
        a1 = Angle(Line(P, center), Line(P, a()), radius=arc_rad, color=YELLOW)
        a2 = Angle(Line(a(), center), Line(a(), P), radius=arc_rad, color=YELLOW)
        b1 = Angle(Line(Q, center), Line(Q, a()), radius=arc_rad, color=TEAL_A)
        b2 = Angle(Line(a(), center), Line(a(), Q), radius=arc_rad, color=TEAL_A)
        a1_lab = MathTex("\\alpha", font_size=26, color=YELLOW).move_to(
            P + normalize((a() - P) + (center - P)) * 0.5)
        a2_lab = MathTex("\\alpha", font_size=26, color=YELLOW).move_to(
            a() + normalize((P - a()) + (center - a())) * 0.64)
        b1_lab = MathTex("\\beta", font_size=26, color=TEAL_A).move_to(
            Q + normalize((a() - Q) + (center - Q)) * 0.5)
        b2_lab = MathTex("\\beta", font_size=26, color=TEAL_A).move_to(
            a() + normalize((Q - a()) + (center - a())) * 0.64)

        p3 = MathTex(
            "\\angle OPA = \\angle OAP = \\alpha,\\quad \\angle OQA = \\angle OAQ = \\beta",
            font_size=23, color=WHITE,
        ).move_to([0, -4.45, 0])

        self.play(
            *[Create(x) for x in [a1, a2, b1, b2]],
            *[FadeIn(x, scale=0.6) for x in [a1_lab, a2_lab, b1_lab, b2_lab]],
            run_time=0.9,
        )
        self.play(Write(p3), run_time=0.8)
        self.wait(0.3)

        # Angle sum
        p4 = MathTex(
            "\\angle P + \\angle Q + \\angle A = \\alpha + \\beta + (\\alpha + \\beta) = 180^\\circ",
            font_size=27, color=BLUE_B,
        ).move_to([0, -5.15, 0])
        self.play(Write(p4), run_time=0.8)
        self.wait(0.3)

        # ∴ α + β = 90°
        p5 = MathTex(
            "\\therefore\\ \\alpha + \\beta = 90^\\circ",
            font_size=32, color=TEAL_A,
        ).move_to([0, -5.75, 0])
        self.play(Write(p5), run_time=0.8)
        self.wait(0.3)

        # Final: ∠PAQ = α + β = 90°
        p6 = MathTex(
            "\\angle PAQ = \\alpha + \\beta = 90^\\circ",
            font_size=33, color=GOLD,
        ).move_to([0, -6.35, 0])
        self.play(Write(p6), run_time=0.8)
        self.wait(0.6)

        # ══════════════════════════════════════════════════════
        #  7. FINALE
        # ══════════════════════════════════════════════════════
        final_tex = MathTex(
            "\\text{Angle in a Semicircle} = 90^\\circ",
            font_size=46,
        )
        final_tex.set_color_by_gradient(GOLD, ORANGE)
        final_tex.move_to([0, -0.8, 0])

        final_box = SurroundingRectangle(
            final_tex, color=GOLD, buff=0.25,
            stroke_width=3.5, corner_radius=0.15,
        )

        self.play(
            FadeOut(proof_card), FadeOut(proof_head),
            FadeOut(p1), FadeOut(p2), FadeOut(p3),
            FadeOut(p4), FadeOut(p5), FadeOut(p6),
            FadeOut(oa_line),
            FadeOut(a1), FadeOut(a2), FadeOut(b1), FadeOut(b2),
            FadeOut(a1_lab), FadeOut(a2_lab), FadeOut(b1_lab), FadeOut(b2_lab),
            FadeOut(ap), FadeOut(aq), FadeOut(angle_mark), FadeOut(angle_label),
            run_time=0.5,
        )
        self.play(FadeOut(a_dot), FadeOut(a_label), run_time=0.3)

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

        self.wait(2.5)