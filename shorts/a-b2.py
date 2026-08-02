from manim import *

config.frame_rate = 60
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16
config.background_color = "#0E1117"


class Formula1(Scene):
    def construct(self):
        # ── 1. Title & Formula (pop together) ──
        title = Text(
            "Visualizing Geometrically",
            gradient=(BLUE, PURPLE, PINK),
            font_size=40,
        )
        title.to_edge(UP, buff=0.7)

        formula = MathTex("(a-b)^2 = a^2 - 2ab + b^2")
        formula.set_color_by_gradient(BLUE, GREEN, YELLOW)
        formula.next_to(title, DOWN, buff=0.5)

        self.play(
            FadeIn(title, scale=0.8),
            FadeIn(formula, scale=0.8),
            run_time=0.8,
        )
        self.wait(0.3)

        # ── 2. Parameters ──
        a = 3.4
        b = 1.0
        a_minus_b = a - b
        dash_len = 0.18
        stroke_w = 4

        # ── 3. Draw Big Square from separate edge lines ──
        big_sq_fill = Square(side_length=a, color=WHITE, fill_opacity=0.08, stroke_width=0)
        big_sq_fill.next_to(formula, DOWN, buff=1)

        c = big_sq_fill.get_center()
        lx = c[0] - a / 2
        rx = c[0] + a / 2
        by = c[1] - a / 2
        ty = c[1] + a / 2

        # Partial edge lines (7 pieces that form the complete square)
        # Left edge: bottom portion (stays) + top portion (fades with ab)
        edge_left_bot = Line([lx, by, 0], [lx, by + a_minus_b, 0], color=WHITE, stroke_width=5)
        edge_l_top = Line([lx, by + a_minus_b, 0], [lx, ty, 0], color=WHITE, stroke_width=5)
        # Right edge: bottom portion (fades with b(a-b)) + top portion (fades with ab)
        edge_r_bot = Line([rx, by, 0], [rx, by + a_minus_b, 0], color=WHITE, stroke_width=5)
        edge_r_top = Line([rx, by + a_minus_b, 0], [rx, ty, 0], color=WHITE, stroke_width=5)
        # Bottom edge: left portion (stays) + right portion (fades with b(a-b))
        edge_bot_left = Line([lx, by, 0], [lx + a_minus_b, by, 0], color=WHITE, stroke_width=5)
        edge_b_right = Line([lx + a_minus_b, by, 0], [rx, by, 0], color=WHITE, stroke_width=5)
        # Top edge: full (fades with ab)
        edge_top = Line([lx, ty, 0], [rx, ty, 0], color=WHITE, stroke_width=5)

        big_sq = VGroup(big_sq_fill, edge_left_bot, edge_l_top, edge_r_bot, edge_r_top, edge_bot_left, edge_b_right, edge_top)

        self.play(Create(big_sq), run_time=0.6)

        c = big_sq_fill.get_center()
        lx = c[0] - a / 2
        rx = c[0] + a / 2
        by = c[1] - a / 2
        ty = c[1] + a / 2

        # ── 4. Tick marks at center of each side ──
        def tick(x, y, horizontal):
            if horizontal:
                return Line(
                    [x, y - dash_len / 2, 0],
                    [x, y + dash_len / 2, 0],
                    color=BLUE, stroke_width=stroke_w,
                )
            else:
                return Line(
                    [x - dash_len / 2, y, 0],
                    [x + dash_len / 2, y, 0],
                    color=BLUE, stroke_width=stroke_w,
                )

        t_top = tick(c[0], ty, True)
        t_bot = tick(c[0], by, True)
        t_left = tick(lx, c[1], False)
        t_right = tick(rx, c[1], False)

        all_ticks = VGroup(t_top, t_bot, t_left, t_right)
        all_ticks.set_stroke(opacity=0)

        self.play(all_ticks.animate.set_stroke(opacity=1), run_time=0.5)
        self.wait(0.2)

        # ── 5. Label a at top with buffer ──
        label_a = MathTex("a", font_size=40, color=WHITE)
        label_a.next_to(big_sq, UP, buff=0.4)

        self.play(Write(label_a), run_time=0.4)
        self.wait(0.3)

        # ── 6. Mark b and a-b on bottom edge ──
        seg_bot_b = Line(
            [rx, by - 0.3, 0], [rx - b, by - 0.3, 0],
            color=ORANGE, stroke_width=6,
        )
        lbl_bot_b = MathTex("b", font_size=34, color=ORANGE)
        lbl_bot_b.next_to(seg_bot_b, DOWN, buff=0.12)

        self.play(Create(seg_bot_b), Write(lbl_bot_b), run_time=0.5)
        self.wait(0.2)

        seg_bot_ab = Line(
            [rx - b, by - 0.3, 0], [lx, by - 0.3, 0],
            color=TEAL, stroke_width=6,
        )
        lbl_bot_ab = MathTex("a-b", font_size=32, color=TEAL)
        lbl_bot_ab.next_to(seg_bot_ab, DOWN, buff=0.12)

        self.play(Create(seg_bot_ab), Write(lbl_bot_ab), run_time=0.5)
        self.wait(0.3)

        # ── 7. Mark b from top then a-b remaining on left edge ──
        seg_left_b = Line(
            [lx - 0.3, ty, 0], [lx - 0.3, ty - b, 0],
            color=PURPLE, stroke_width=6,
        )
        lbl_left_b = MathTex("b", font_size=34, color=PURPLE)
        lbl_left_b.next_to(seg_left_b, LEFT, buff=0.12)

        self.play(Create(seg_left_b), Write(lbl_left_b), run_time=0.5)
        self.wait(0.2)

        seg_left_ab = Line(
            [lx - 0.3, ty - b, 0], [lx - 0.3, by, 0],
            color=TEAL, stroke_width=6,
        )
        lbl_left_ab = MathTex("a-b", font_size=32, color=TEAL)
        lbl_left_ab.next_to(seg_left_ab, LEFT, buff=0.12)

        self.play(Create(seg_left_ab), Write(lbl_left_ab), run_time=0.5)
        self.wait(0.3)

        # ── 8. Dividing lines (3 regions) ──
        v_div = Line(
            [lx + a_minus_b, by, 0], [lx + a_minus_b, ty - b, 0],
            color="#FFD700", stroke_width=4,
        )

        self.play(Create(v_div), run_time=0.4)
        self.wait(0.2)

        h_div = Line(
            [lx, by + a_minus_b, 0], [rx, by + a_minus_b, 0],
            color="#FFD700", stroke_width=4,
        )

        self.play(Create(h_div), run_time=0.4)
        self.wait(0.3)

        # ── 9. Highlight & label 3 regions ──
        # Region 1: (a-b)^2 - bottom-left - GOLD
        r1 = Polygon(
            [lx, by, 0], [lx + a_minus_b, by, 0],
            [lx + a_minus_b, by + a_minus_b, 0], [lx, by + a_minus_b, 0],
            color=GOLD, fill_opacity=0.55, stroke_width=0,
        )
        l1 = MathTex(r"\text{Area} = (a-b)^2", font_size=30)
        l1.set_color_by_gradient(WHITE, GOLD)
        l1.move_to(r1.get_center())

        self.play(FadeIn(r1), Write(l1), run_time=0.5)
        self.wait(0.3)

        # Region 2: b(a-b) - bottom-right - ORANGE
        r2 = Polygon(
            [lx + a_minus_b, by, 0], [rx, by, 0],
            [rx, by + a_minus_b, 0], [lx + a_minus_b, by + a_minus_b, 0],
            color=ORANGE, fill_opacity=0.55, stroke_width=0,
        )
        l2 = MathTex(r"\text{Area} =", r"b(a-b)", font_size=24)
        l2.set_color_by_gradient(WHITE, YELLOW)
        l2.arrange(DOWN, buff=0.1)
        l2.move_to(r2.get_center())

        self.play(FadeIn(r2), Write(l2), run_time=0.5)
        self.wait(0.3)

        # Region 3: ab - top - PURPLE
        r3 = Polygon(
            [lx, by + a_minus_b, 0], [rx, by + a_minus_b, 0],
            [rx, ty, 0], [lx, ty, 0],
            color=PURPLE, fill_opacity=0.55, stroke_width=0,
        )
        l3 = MathTex(r"\text{Area} = ab", font_size=26)
        l3.set_color_by_gradient(WHITE, PINK)
        l3.move_to(r3.get_center())

        self.play(FadeIn(r3), Write(l3), run_time=0.5)
        self.wait(0.3)

        # Fade out initial square fill
        self.play(FadeOut(big_sq_fill), run_time=0.4)
        self.wait(0.2)

        # ── 10. Copy splits from original and slides down ──
        target_y = c[1] - 5.0
        sq_copy = big_sq.copy()
        la_copy = label_a.copy()
        ticks_copy = all_ticks.copy()
        copy_group = VGroup(sq_copy, la_copy, ticks_copy)
        copy_group.move_to(big_sq.get_center())

        self.play(copy_group.animate.move_to([c[0] - 1.8, target_y, 0]), run_time=0.8)

        # Use known position for copy center
        c2_x = c[0] - 1.8
        c2_y = target_y
        rx2 = c2_x + a / 2
        lx2 = c2_x - a / 2
        by2 = c2_y - a / 2
        ty2 = c2_y + a / 2

        lbl_clean = MathTex(r"a^2", font_size=40)
        lbl_clean.set_color_by_gradient(WHITE, TEAL_C)
        lbl_clean.move_to([c2_x, c2_y, 0])

        self.play(Write(lbl_clean), run_time=0.4)
        self.wait(0.3)

        # ── 11. Remove b(a-b) from original + fade edges + labels/ticks ──
        self.play(
            FadeOut(r2), FadeOut(l2),
            FadeOut(edge_r_bot), FadeOut(edge_b_right),
            FadeOut(seg_bot_b), FadeOut(lbl_bot_b),
            FadeOut(t_right),
            run_time=0.4,
        )

        # b(a-b) rectangle with its edge copies
        r_slide_bab = Polygon(
            [lx + a_minus_b, by, 0], [rx, by, 0],
            [rx, by + a_minus_b, 0], [lx + a_minus_b, by + a_minus_b, 0],
            color=ORANGE, fill_opacity=0.6, stroke_width=0,
        )
        l_slide_bab = MathTex(r"b(a-b)", font_size=22)
        l_slide_bab.set_color_by_gradient(WHITE, YELLOW)
        l_slide_bab.move_to(r_slide_bab.get_center())

        # Edge copies for b(a-b)
        e_rbot_slide = Line([rx, by, 0], [rx, by + a_minus_b, 0], color=WHITE, stroke_width=5)
        e_bright_slide = Line([lx + a_minus_b, by, 0], [rx, by, 0], color=WHITE, stroke_width=5)

        bab_group = VGroup(r_slide_bab, l_slide_bab, e_rbot_slide, e_bright_slide)
        target_bab_x = rx2 + 0.3 + a_minus_b / 2
        target_bab_y = c2_y

        self.play(
            bab_group.animate.move_to([target_bab_x, target_bab_y, 0]),
            run_time=0.8,
        )
        self.wait(0.2)

        # ── 12. Minus sign between sq_copy and b(a-b) ──
        minus1 = MathTex(r"-", font_size=40, color=WHITE)
        minus1_x = (rx2 + (target_bab_x - a_minus_b / 2)) / 2
        minus1.move_to([minus1_x, c2_y, 0])

        self.play(Write(minus1), run_time=0.3)
        self.wait(0.2)

        # ── 13. Remove ab from original + fade edges + labels/ticks ──
        self.play(
            FadeOut(r3), FadeOut(l3),
            FadeOut(edge_top), FadeOut(edge_r_top), FadeOut(edge_l_top),
            FadeOut(seg_left_b), FadeOut(lbl_left_b),
            FadeOut(seg_left_ab), FadeOut(lbl_left_ab),
            FadeOut(label_a), FadeOut(t_top),
            run_time=0.4,
        )

        # ab rectangle with its edge copies
        r_slide_ab = Polygon(
            [lx, by + a_minus_b, 0], [rx, by + a_minus_b, 0],
            [rx, ty, 0], [lx, ty, 0],
            color=PURPLE, fill_opacity=0.6, stroke_width=0,
        )
        r_slide_ab.rotate(PI / 2)
        l_slide_ab = MathTex(r"ab", font_size=24)
        l_slide_ab.set_color_by_gradient(WHITE, PINK)
        l_slide_ab.move_to(r_slide_ab.get_center())

        # Edge copies for ab
        e_top_slide = Line([lx, ty, 0], [rx, ty, 0], color=WHITE, stroke_width=5)
        e_rtop_slide = Line([rx, by + a_minus_b, 0], [rx, ty, 0], color=WHITE, stroke_width=5)
        e_ltop_slide = Line([lx, by + a_minus_b, 0], [lx, ty, 0], color=WHITE, stroke_width=5)

        e_top_slide.rotate(PI / 2, about_point=r_slide_ab.get_center())
        e_rtop_slide.rotate(PI / 2, about_point=r_slide_ab.get_center())
        e_ltop_slide.rotate(PI / 2, about_point=r_slide_ab.get_center())

        ab_group = VGroup(r_slide_ab, l_slide_ab, e_top_slide, e_rtop_slide, e_ltop_slide)
        target_ab_x = target_bab_x + a_minus_b / 2 + 0.3 + b / 2
        target_ab_y = c2_y

        self.play(
            ab_group.animate.move_to([target_ab_x, target_ab_y, 0]),
            run_time=0.8,
        )
        self.wait(0.2)

        # ── 14. Minus sign between b(a-b) and ab ──
        minus2 = MathTex(r"-", font_size=40, color=WHITE)
        minus2_x = ((target_bab_x + a_minus_b / 2) + (target_ab_x - b / 2)) / 2
        minus2.move_to([minus2_x, c2_y, 0])

        self.play(Write(minus2), run_time=0.3)
        self.wait(0.3)

        # ── 15. Reveal remaining (a-b)^2 in copy ──
        r_remain = Polygon(
            [lx2, by2, 0], [lx2 + a_minus_b, by2, 0],
            [lx2 + a_minus_b, by2 + a_minus_b, 0], [lx2, by2 + a_minus_b, 0],
            color=GOLD, fill_opacity=0.6, stroke_width=0,
        )
        l_remain = MathTex(r"(a-b)^2", font_size=32)
        l_remain.set_color_by_gradient(GOLD, YELLOW)
        l_remain.move_to(r_remain.get_center())

        self.play(FadeIn(r_remain), Write(l_remain), run_time=0.5)

        # Glow pulse
        self.play(
            r_remain.animate.scale(1.08),
            l_remain.animate.scale(1.08),
            run_time=0.25,
        )
        self.play(
            r_remain.animate.scale(0.92),
            l_remain.animate.scale(0.92),
            run_time=0.25,
        )
        self.wait(0.4)

        # ── 16. Final formula ──
        eq_final = MathTex(r"= a^2 - 2ab + b^2", font_size=32)
        eq_final.set_color_by_gradient(GREEN, YELLOW)
        eq_final.next_to(ab_group, DOWN, buff=0.5)

        self.play(Write(eq_final), run_time=0.7)
        self.wait(1.5)
