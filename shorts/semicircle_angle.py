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
        #  2. CIRCLE (gold) & DIAMETER PQ
        # ══════════════════════════════════════════════════════
        circle = Circle(
            radius=max_r, color=GOLD, stroke_width=3.5,
        ).move_to(center)

        self.play(
            Create(circle),
            run_time=1.2,
        )
        self.wait(0.3)

        diameter = Line(P, Q, color=TEAL_B, stroke_width=4)
        p_dot = Dot(P, color=GOLD, radius=0.09, z_index=10)
        q_dot = Dot(Q, color=GOLD, radius=0.09, z_index=10)
        p_label = Text("P", font_size=28, color=GOLD, weight=BOLD, z_index=10)
        p_label.next_to(P, DOWN, buff=0.12).shift(LEFT * 0.22)
        q_label = Text("Q", font_size=28, color=GOLD, weight=BOLD, z_index=10)
        q_label.next_to(Q, DOWN, buff=0.12).shift(RIGHT * 0.22)

        self.play(
            Create(diameter), FadeIn(p_dot), FadeIn(q_dot),
            Write(p_label), Write(q_label),
            run_time=0.9,
        )
        self.wait(0.3)

        # ══════════════════════════════════════════════════════
        #  3. CENTER O — small dot
        # ══════════════════════════════════════════════════════
        o_dot = Dot(center, color=WHITE, radius=0.06, z_index=10)
        o_label = Text("O", font_size=26, color=WHITE, weight=BOLD)
        o_label.next_to(center, DOWN, buff=0.14).shift(DOWN * 0.0)

        self.play(FadeIn(o_dot), Write(o_label), run_time=0.6)
        self.wait(0.3)

        # ══════════════════════════════════════════════════════
        #  4. THE GLIDE — A moves, ∠PAQ stays 90°
        # ══════════════════════════════════════════════════════
        ap = always_redraw(lambda: Line(a(), P, color=TEAL_B, stroke_width=4.5))
        aq = always_redraw(lambda: Line(a(), Q, color=TEAL_B, stroke_width=4.5))
        a_dot = always_redraw(lambda: Dot(a(), radius=0.1, color=TEAL_B))
        a_label = always_redraw(lambda: Text(
            "A", font_size=28, color=TEAL_B, weight=BOLD,
        ).move_to(a() + UP * 0.32 + LEFT * 0.05))

        angle_mark = always_redraw(lambda: RightAngle(
            Line(a(), P), Line(a(), Q),
            length=0.36, color=TEAL_B, stroke_width=3.5,
        ))
        angle_label = always_redraw(lambda: Text(
            "90°", font_size=26, color=TEAL_B, weight=BOLD,
        ).move_to(a() + normalize((P - a()) + (Q - a())) * 1.05))

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

        # Continuous back-and-forth gliding (θ: π/2 → π-0.35 → 0.35 → π/2)
        # A always stays inside the semicircle — never reaching P or Q,
        # so AP and AQ never collapse into a single line.
        glide_min, glide_max = 0.35, PI - 0.35
        self.play(theta_tracker.animate.set_value(glide_max), run_time=2.0, rate_func=smooth)
        self.play(theta_tracker.animate.set_value(glide_min), run_time=4.0, rate_func=smooth)
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
            FadeOut(angle_mark), FadeOut(angle_label),
            run_time=0.4,
        )

        proof_card = RoundedRectangle(
            corner_radius=0.3, height=5.1, width=8.2,
            fill_color="#121722", fill_opacity=0.93,
            stroke_color=BLUE_E, stroke_width=2,
        ).move_to([0, -1.55, 0])
        proof_head = Text(
            "THE PROOF", font_size=21, color=GRAY_B, weight=BOLD,
        ).move_to([0, 0.45, 0])

        self.play(FadeIn(proof_card, shift=UP * 0.3), Write(proof_head), run_time=0.6)

        oa_line = DashedLine(center, a(), color=YELLOW, stroke_width=3.5)
        self.play(Create(oa_line), run_time=0.5)
        self.wait(0.2)

        # Equal-length tick marks on the three radii
        def tick_mark(p1_, p2_):
            d = normalize(p2_ - p1_)
            n = np.array([-d[1], d[0], 0.0])
            mid = (p1_ + p2_) / 2
            return Line(mid - n * 0.07, mid + n * 0.07, color=YELLOW_E, stroke_width=3)

        tick_oa = tick_mark(center, a())
        tick_op = tick_mark(center, P)
        tick_oq = tick_mark(center, Q)
        self.play(
            *[Create(t) for t in [tick_oa, tick_op, tick_oq]],
            run_time=0.9,
        )
        self.wait(0.2)

        # Labels: OP = OQ = OA — all radii (highlight each radius in red)
        p1 = MathTex(
            "OP = OQ = OA", "\\quad (\\text{all are radii})",
            font_size=32,
        ).move_to([0, -0.25, 0])
        p1[0].set_color(GOLD)
        p1[1].set_color(WHITE)
        p1_box = SurroundingRectangle(
            p1, color=GOLD, buff=0.16, stroke_width=2.5, corner_radius=0.12,
        )

        red_op = Line(center, P, color=RED, stroke_width=5)
        red_oq = Line(center, Q, color=RED, stroke_width=5)
        red_oa = Line(center, a(), color=RED, stroke_width=5)
        self.play(Write(p1), run_time=0.4)
        self.play(Create(red_op), run_time=0.3)
        self.play(Create(red_oq), run_time=0.3)
        self.play(Create(red_oa), run_time=0.3)
        self.play(Create(p1_box), run_time=0.4)
        self.wait(0.3)
        self.play(
            FadeOut(p1_box), FadeOut(red_op),
            FadeOut(red_oq), FadeOut(red_oa),
            run_time=0.3,
        )

        # Isosceles triangles — highlight the two triangles one at a time
        p2 = MathTex(
            "\\triangle AOP \\ \\text{and}\\ \\triangle AOQ \\ \\text{are isosceles}",
            font_size=28, color=TEAL_B,
        ).move_to([0, -0.95, 0])

        tri_aop = Polygon(
            a(), center, P,
            fill_color=TEAL_B, fill_opacity=0.18, stroke_width=0,
        )
        tri_aoq = Polygon(
            a(), center, Q,
            fill_color=TEAL_B, fill_opacity=0.18, stroke_width=0,
        )

        self.play(Write(p2), run_time=0.5)
        self.play(
            FadeIn(tri_aop, scale=0.7),
            run_time=0.9,
        )
        self.wait(0.25)
        self.play(
            FadeIn(tri_aoq, scale=0.7),
            run_time=0.9,
        )
        self.play(FadeOut(tri_aop), FadeOut(tri_aoq), run_time=0.4)
        self.wait(0.2)

        # Base angles marked on the diagram: only α at P
        arc_rad = 0.3
        a1 = Angle(Line(P, center), Line(P, a()), radius=arc_rad, color=YELLOW)
        a1_lab = MathTex("\\alpha", font_size=26, color=YELLOW).move_to(
            P + normalize((a() - P) + (center - P)) * 0.5)

        p3 = MathTex(
            "\\angle OPA = \\angle OAP = \\alpha,\\quad \\angle OQA = \\angle OAQ = \\beta",
            font_size=23, color=WHITE,
        ).move_to([0, -1.65, 0])

        self.play(
            Create(a1),
            FadeIn(a1_lab, scale=0.6),
            run_time=0.9,
        )
        self.play(Write(p3), run_time=0.8)
        self.play(
            Indicate(a1, color=YELLOW, scale_factor=1.2),
            run_time=0.9,
        )
        self.wait(0.3)

        # Angle sum
        p4 = MathTex(
            "\\angle P + \\angle Q + \\angle A = \\alpha + \\beta + (\\alpha + \\beta) = 180^\\circ",
            font_size=27, color=BLUE_B,
        ).move_to([0, -2.35, 0])
        self.play(Write(p4), run_time=0.8)
        self.play(
            Indicate(p4, color=BLUE_A, scale_factor=1.1),
            run_time=0.8,
        )
        self.wait(0.3)

        # ∴ α + β = 90°
        p5 = MathTex(
            "\\therefore\\ \\alpha + \\beta = 90^\\circ",
            font_size=32, color=TEAL_A,
        ).move_to([0, -2.95, 0])
        self.play(Write(p5), run_time=0.8)
        self.play(
            Indicate(p5, color=TEAL_B, scale_factor=1.12),
            run_time=0.6,
        )
        self.wait(0.3)

        # Final: ∠PAQ = α + β = 90°
        p6 = MathTex(
            "\\angle PAQ = \\alpha + \\beta = 90^\\circ",
            font_size=33, color=GOLD,
        ).move_to([0, -3.55, 0])
        self.play(Write(p6), run_time=0.8)
        for _ in range(2):
            self.play(
                p6.animate.scale(1.08),
                run_time=0.3, rate_func=there_and_back,
            )
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
            FadeOut(tick_oa), FadeOut(tick_op), FadeOut(tick_oq),
            FadeOut(a1),
            FadeOut(a1_lab),
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