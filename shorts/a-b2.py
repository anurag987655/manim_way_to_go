from manim import *

# Set up configuration for standard 9:16 vertical video
config.frame_rate = 60
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16
config.background_color = "#0B0C10"  # Rich dark charcoal background


class Formula1(Scene):
    def construct(self):
        # ── 1. Title & Formula ──
        title = Text(
            "Visualizing Geometrically",
            gradient=(BLUE_C, PURPLE_C, PINK),
            font_size=40,
        )
        title.to_edge(UP, buff=0.7)

        formula = MathTex("(a-b)^2 = a^2 - 2ab + b^2")
        formula.set_color_by_gradient(TEAL, BLUE_D, GREEN)
        formula.next_to(title, DOWN, buff=0.5)

        self.play(
            FadeIn(title, scale=0.9),
            FadeIn(formula, scale=0.9),
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
        big_sq_fill = Square(side_length=a, color=WHITE, fill_opacity=0.06, stroke_width=0)
        big_sq_fill.next_to(formula, DOWN, buff=1.0)

        c = big_sq_fill.get_center()
        lx = c[0] - a / 2
        rx = c[0] + a / 2
        by = c[1] - a / 2
        ty = c[1] + a / 2

        # Partial edge lines (7 pieces that form the complete square)
        edge_left_bot = Line([lx, by, 0], [lx, by + a_minus_b, 0], color=WHITE, stroke_width=4)
        edge_l_top = Line([lx, by + a_minus_b, 0], [lx, ty, 0], color=WHITE, stroke_width=4)
        edge_r_bot = Line([rx, by, 0], [rx, by + a_minus_b, 0], color=WHITE, stroke_width=4)
        edge_r_top = Line([rx, by + a_minus_b, 0], [rx, ty, 0], color=WHITE, stroke_width=4)
        edge_bot_left = Line([lx, by, 0], [lx + a_minus_b, by, 0], color=WHITE, stroke_width=4)
        edge_b_right = Line([lx + a_minus_b, by, 0], [rx, by, 0], color=WHITE, stroke_width=4)
        edge_top = Line([lx, ty, 0], [rx, ty, 0], color=WHITE, stroke_width=4)

        big_sq = VGroup(
            big_sq_fill, edge_left_bot, edge_l_top, 
            edge_r_bot, edge_r_top, edge_bot_left, 
            edge_b_right, edge_top
        )

        self.play(Create(big_sq), run_time=0.6)
        self.wait(0.2)

        # ── 4. Tick marks at center of each side ──
        def tick(x, y, horizontal):
            if horizontal:
                return Line(
                    [x, y - dash_len / 2, 0],
                    [x, y + dash_len / 2, 0],
                    color=BLUE_C, stroke_width=stroke_w,
                )
            else:
                return Line(
                    [x - dash_len / 2, y, 0],
                    [x + dash_len / 2, y, 0],
                    color=BLUE_C, stroke_width=stroke_w,
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
        label_a.next_to(big_sq_fill, UP, buff=0.4)

        self.play(Write(label_a), run_time=0.4)
        self.wait(0.3)


        # ── 4b. Area label inside square ──
        area_label = MathTex(r"\text{Area} = a^2", font_size=30, color=WHITE)
        area_label.move_to(c)

        self.play(Write(area_label), run_time=0.5)
        self.wait(0.2)
        self.play(FadeOut(area_label))


        # ── 6. Mark b and a-b on bottom edge ──
        seg_bot_b = Line(
            [rx, by - 0.35, 0], [rx - b, by - 0.35, 0],
            color=ORANGE, stroke_width=5,
        )
        lbl_bot_b = MathTex("b", font_size=34, color=ORANGE)
        lbl_bot_b.next_to(seg_bot_b, DOWN, buff=0.1)

        self.play(Create(seg_bot_b), Write(lbl_bot_b), run_time=0.5)
        self.wait(0.2)

        seg_bot_ab = Line(
            [rx - b, by - 0.35, 0], [lx, by - 0.35, 0],
            color=TEAL, stroke_width=5,
        )
        lbl_bot_ab = MathTex("a-b", font_size=32, color=TEAL)
        lbl_bot_ab.next_to(seg_bot_ab, DOWN, buff=0.1)

        self.play(Create(seg_bot_ab), Write(lbl_bot_ab), run_time=0.5)
        self.wait(0.3)

        # ── 7. Mark b from top then a-b remaining on left edge ──
        seg_left_b = Line(
            [lx - 0.35, ty, 0], [lx - 0.35, ty - b, 0],
            color=ORANGE, stroke_width=5,
        )
        lbl_left_b = MathTex("b", font_size=34, color=ORANGE)
        lbl_left_b.next_to(seg_left_b, LEFT, buff=0.1)

        self.play(Create(seg_left_b), Write(lbl_left_b), run_time=0.5)
        self.wait(0.2)

        seg_left_ab = Line(
            [lx - 0.35, ty - b, 0], [lx - 0.35, by, 0],
            color=TEAL, stroke_width=5,
        )
        lbl_left_ab = MathTex("a-b", font_size=32, color=TEAL)
        lbl_left_ab.next_to(seg_left_ab, LEFT, buff=0.1)

        self.play(Create(seg_left_ab), Write(lbl_left_ab), run_time=0.5)
        self.wait(0.3)

        # ── 8. Dividing lines (3 regions) ──
        v_div = Line(
            [lx + a_minus_b, by, 0], [lx + a_minus_b, ty - b, 0],
            color=WHITE, stroke_width=2,
        ).set_stroke(opacity=0.6)

        self.play(Create(v_div), run_time=0.4)
        self.wait(0.2)

        h_div = Line(
            [lx, by + a_minus_b, 0], [rx, by + a_minus_b, 0],
            color=WHITE, stroke_width=2,
        ).set_stroke(opacity=0.6)

        self.play(Create(h_div), run_time=0.4)
        self.wait(0.3)

        # ── 9. Highlight & label 3 regions ──
        # Region 1: (a-b)^2 - bottom-left - TEAL
        r1 = Polygon(
            [lx, by, 0], [lx + a_minus_b, by, 0],
            [lx + a_minus_b, by + a_minus_b, 0], [lx, by + a_minus_b, 0],
            color=TEAL, fill_opacity=0.25, stroke_width=0,
        )
        l1 = MathTex(r"\text{Area} = (a-b)^2", font_size=30, color=TEAL)
        l1.move_to(r1.get_center())

        self.play(FadeIn(r1), Write(l1), run_time=0.5)
        self.wait(0.3)

        # Region 2: b(a-b) - bottom-right - ORANGE
        r2 = Polygon(
            [lx + a_minus_b, by, 0], [rx, by, 0],
            [rx, by + a_minus_b, 0], [lx + a_minus_b, by + a_minus_b, 0],
            color=ORANGE, fill_opacity=0.25, stroke_width=0,
        )
        l2 = MathTex(r"\text{Area} =", r"b(a-b)", font_size=24)
        l2[0].set_color(WHITE)
        l2[1].set_color(ORANGE)
        l2.arrange(DOWN, buff=0.1)
        l2.move_to(r2.get_center())

        self.play(FadeIn(r2), Write(l2), run_time=0.5)
        self.wait(0.3)

        # Region 3: ab - top - PURPLE
        r3 = Polygon(
            [lx, by + a_minus_b, 0], [rx, by + a_minus_b, 0],
            [rx, ty, 0], [lx, ty, 0],
            color=PURPLE, fill_opacity=0.25, stroke_width=0,
        )
        l3 = MathTex(r"\text{Area} = ab", font_size=26, color=PURPLE_B)
        l3.move_to(r3.get_center())

        self.play(FadeIn(r3), Write(l3), run_time=0.5)
        self.wait(0.3)

        # Fade out initial square fill
        self.play(FadeOut(big_sq_fill), run_time=0.4)
        self.wait(0.2)

        # ── 10. Copy splits from original and slide down using dummy layout ──
        # We calculate the alignment automatically using dummy objects arranged in a VGroup
        sq_copy_dummy = big_sq.copy()
        minus1_dummy = MathTex(r"-", font_size=40, color=WHITE)
        
        # bab_group_dummy
        r_slide_bab_dummy = Polygon(
            [lx + a_minus_b, by, 0], [rx, by, 0],
            [rx, by + a_minus_b, 0], [lx + a_minus_b, by + a_minus_b, 0],
            color=ORANGE, fill_opacity=0.25, stroke_width=0,
        )
        l_slide_bab_dummy = MathTex(r"b(a-b)", font_size=22, color=ORANGE)
        l_slide_bab_dummy.move_to(r_slide_bab_dummy.get_center())
        e_rbot_slide_dummy = Line([rx, by, 0], [rx, by + a_minus_b, 0], color=WHITE, stroke_width=4)
        e_bright_slide_dummy = Line([lx + a_minus_b, by, 0], [rx, by, 0], color=WHITE, stroke_width=4)
        e_lbot_slide_dummy = Line([lx + a_minus_b, by, 0], [lx + a_minus_b, by + a_minus_b, 0], color=WHITE, stroke_width=4)
        e_tleft_slide_dummy = Line([lx + a_minus_b, by + a_minus_b, 0], [rx, by + a_minus_b, 0], color=WHITE, stroke_width=4)
        bab_group_dummy = VGroup(r_slide_bab_dummy, l_slide_bab_dummy, e_rbot_slide_dummy, e_bright_slide_dummy, e_lbot_slide_dummy, e_tleft_slide_dummy)

        minus2_dummy = MathTex(r"-", font_size=40, color=WHITE)

        # ab_group_dummy (rotated)
        r_slide_ab_dummy = Polygon(
            [lx, by + a_minus_b, 0], [rx, by + a_minus_b, 0],
            [rx, ty, 0], [lx, ty, 0],
            color=PURPLE, fill_opacity=0.25, stroke_width=0,
        ).rotate(PI / 2)
        e_top_slide_dummy = Line([lx, ty, 0], [rx, ty, 0], color=WHITE, stroke_width=4).rotate(PI / 2, about_point=r_slide_ab_dummy.get_center())
        e_rtop_slide_dummy = Line([rx, by + a_minus_b, 0], [rx, ty, 0], color=WHITE, stroke_width=4).rotate(PI / 2, about_point=r_slide_ab_dummy.get_center())
        e_ltop_slide_dummy = Line([lx, by + a_minus_b, 0], [lx, ty, 0], color=WHITE, stroke_width=4).rotate(PI / 2, about_point=r_slide_ab_dummy.get_center())
        e_bot_slide_dummy = Line([lx, by + a_minus_b, 0], [rx, by + a_minus_b, 0], color=WHITE, stroke_width=4).rotate(PI / 2, about_point=r_slide_ab_dummy.get_center())
        l_slide_ab_dummy = MathTex(r"ab", font_size=24, color=PURPLE_B).move_to(r_slide_ab_dummy.get_center())
        ab_group_dummy = VGroup(r_slide_ab_dummy, l_slide_ab_dummy, e_top_slide_dummy, e_rtop_slide_dummy, e_ltop_slide_dummy, e_bot_slide_dummy)

        # Arrange dummy layout at y = c[1] - 4.5
        bottom_row = VGroup(
            sq_copy_dummy, minus1_dummy, bab_group_dummy, minus2_dummy, ab_group_dummy
        ).arrange(RIGHT, buff=0.25)
        bottom_row.move_to([0, c[1] - 4.5, 0])

        # Extract target positions
        pos_sq = sq_copy_dummy.get_center()
        pos_minus1 = minus1_dummy.get_center()
        pos_bab = bab_group_dummy.get_center()
        pos_minus2 = minus2_dummy.get_center()
        pos_ab = ab_group_dummy.get_center()

        # Animate big square copy sliding down
        sq_copy = big_sq.copy()
        la_copy = label_a.copy()
        ticks_copy = all_ticks.copy()
        copy_group = VGroup(sq_copy, la_copy, ticks_copy)
        copy_group.move_to(big_sq.get_center())

        self.play(copy_group.animate.move_to(pos_sq), run_time=0.8)

        lbl_clean = MathTex(r"a^2", font_size=40, color=WHITE).move_to(pos_sq)
        self.play(Write(lbl_clean), run_time=0.4)
        self.wait(0.3)

        # ── 11. Slide b(a-b) down from original position ──
        # Draw white boundary for right side of (a-b)^2 in place
        right_ab2_line = Line(
            [lx + a_minus_b, by, 0], [lx + a_minus_b, by + a_minus_b, 0],
            color=WHITE, stroke_width=4,
        )

        # Build group that includes the original r2 polygon and boundary copy lines
        e_rbot_slide = Line([rx, by, 0], [rx, by + a_minus_b, 0], color=WHITE, stroke_width=4)
        e_bright_slide = Line([lx + a_minus_b, by, 0], [rx, by, 0], color=WHITE, stroke_width=4)
        e_lbot_slide = Line([lx + a_minus_b, by, 0], [lx + a_minus_b, by + a_minus_b, 0], color=WHITE, stroke_width=4)
        e_tleft_slide = Line([lx + a_minus_b, by + a_minus_b, 0], [rx, by + a_minus_b, 0], color=WHITE, stroke_width=4)

        # bab_group contains r2 (originally created at top square region) and border outlines
        bab_group = VGroup(r2, e_rbot_slide, e_bright_slide, e_lbot_slide, e_tleft_slide)
        
        l_slide_bab = MathTex(r"b(a-b)", font_size=22, color=ORANGE).move_to(pos_bab)

        # Animate static elements fading out while the rectangle slides down directly
        self.play(
            FadeOut(edge_r_bot), FadeOut(edge_b_right),
            FadeOut(seg_bot_b), FadeOut(lbl_bot_b),
            FadeOut(t_right),
            FadeOut(v_div),
            Create(right_ab2_line),
            bab_group.animate.move_to(pos_bab),
            ReplacementTransform(l2, l_slide_bab),
            run_time=0.8
        )
        self.wait(0.2)

        # ── 12. Minus sign between sq_copy and b(a-b) ──
        minus1 = MathTex(r"-", font_size=40, color=WHITE).move_to(pos_minus1)
        self.play(Write(minus1), run_time=0.3)
        self.wait(0.2)

        # ── 13. Slide ab down from original position ──
        # Draw white boundary for top of (a-b)^2 in place
        top_ab2_line = Line(
            [lx, by + a_minus_b, 0], [lx + a_minus_b, by + a_minus_b, 0],
            color=WHITE, stroke_width=4,
        )

        # Build group that includes the original r3 polygon and boundary copy lines
        e_top_slide = Line([lx, ty, 0], [rx, ty, 0], color=WHITE, stroke_width=4)
        e_rtop_slide = Line([rx, by + a_minus_b, 0], [rx, ty, 0], color=WHITE, stroke_width=4)
        e_ltop_slide = Line([lx, by + a_minus_b, 0], [lx, ty, 0], color=WHITE, stroke_width=4)
        e_bot_slide = Line([lx, by + a_minus_b, 0], [rx, by + a_minus_b, 0], color=WHITE, stroke_width=4)

        # ab_group_shapes contains r3 (originally created at top square region) and border outlines
        ab_group_shapes = VGroup(r3, e_top_slide, e_rtop_slide, e_ltop_slide, e_bot_slide)

        l_slide_ab = MathTex(r"ab", font_size=24, color=PURPLE_B).move_to(pos_ab)

        # Animate static elements fading out while the top horizontal rectangle slides down and rotates by 90 degrees
        self.play(
            FadeOut(edge_top), FadeOut(edge_r_top), FadeOut(edge_l_top),
            FadeOut(seg_left_b), FadeOut(lbl_left_b),
            FadeOut(seg_left_ab), FadeOut(lbl_left_ab),
            FadeOut(label_a), FadeOut(t_top),
            FadeOut(h_div),
            Create(top_ab2_line),
            ab_group_shapes.animate.move_to(pos_ab).rotate(PI / 2),
            ReplacementTransform(l3, l_slide_ab),
            run_time=0.8
        )
        self.wait(0.2)

        # ── 14. Minus sign between b(a-b) and ab ──
        minus2 = MathTex(r"-", font_size=40, color=WHITE).move_to(pos_minus2)
        self.play(Write(minus2), run_time=0.3)
        self.wait(0.3)

        # ── 15. Formula labels below the arranged elements ──
        y_label = pos_sq[1] - a / 2 - 0.6

        lbl_formula = MathTex(r"a^2 - b(a-b) - ab", font_size=32, color=WHITE)
        lbl_formula.move_to([0, y_label, 0])

        self.play(Write(lbl_formula), run_time=0.8)
        self.wait(0.5)

        # Step 2: Expand b(a-b)
        lbl_step2 = MathTex(r"= a^2 - ab + b^2 - ab", font_size=30, color=ORANGE)
        lbl_step2.next_to(lbl_formula, DOWN, buff=0.3)

        self.play(Write(lbl_step2), run_time=0.6)
        self.wait(0.4)

        # Step 3: Combine like terms
        lbl_step3 = MathTex(r"= a^2 - 2ab + b^2", font_size=34, color=TEAL)
        lbl_step3.next_to(lbl_step2, DOWN, buff=0.3)

        self.play(Write(lbl_step3), run_time=0.6)
        self.wait(0.8)