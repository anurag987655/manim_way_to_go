## videos objective to show the formula $$(a+b)^2 = a^2 + 2*a*b + b^2$ aim drawing a square of side a + b and inside showing its area is $(a+b)^2$
## later splitting and below the main showing that each component adds to the rhs for formula


from manim import *

config.frame_rate = 60
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16
config.background_color = "#0E1117"


class Formula1(Scene):
    def construct(self):
        # ── 1. Title & Formula ──
        title = Text(
            "Visualizing Geometrically",
            gradient=(BLUE, PURPLE, PINK),
            font_size=44,
        )
        title.to_edge(UP, buff=0.6)

        formula = MathTex("(a+b)^2 = a^2 + 2ab + b^2")
        formula.set_color_by_gradient(BLUE, GREEN, YELLOW)
        formula.next_to(title, DOWN, buff=0.4)
        self.add(title, formula)
        self.wait(0.5)

        # ── 2. Parameters ──
        a = 2.5
        b = 1.5
        s = a + b
        dash_len = 0.18
        stroke_w = 4

        # ── 3. Big Square ──
        big_sq = Square(side_length=s, color=RED, fill_opacity=0.15)
        big_sq.next_to(formula, DOWN, buff=1.5)
        c = big_sq.get_center()
        lx = c[0] - s / 2
        rx = c[0] + s / 2
        by = c[1] - s / 2
        ty = c[1] + s / 2

        self.play(Create(big_sq), run_time=0.8)
        self.wait(0.3)

        # ── 4. Tick marks (one at center of each side) ──
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

        # ── 5. Colored edge segments showing a and b portions ──
        seg_buff = 0.35

        # Top edge segments
        seg_top_a = Line(
            [lx, ty + seg_buff, 0], [lx + a, ty + seg_buff, 0],
            color=RED, stroke_width=6,
        )
        seg_top_b = Line(
            [lx + a, ty + seg_buff, 0], [rx, ty + seg_buff, 0],
            color=GREEN, stroke_width=6,
        )
        lbl_top_a = MathTex("a", font_size=38, color=RED)
        lbl_top_a.next_to(seg_top_a, UP, buff=0.15)
        lbl_top_b = MathTex("b", font_size=38, color=GREEN)
        lbl_top_b.next_to(seg_top_b, UP, buff=0.15)

        self.play(Create(seg_top_a), Create(seg_top_b), run_time=0.6)
        self.play(Write(lbl_top_a), Write(lbl_top_b), run_time=0.4)
        self.wait(0.2)

        # Left edge segments
        seg_left_b = Line(
            [lx - seg_buff, by, 0], [lx - seg_buff, by + b, 0],
            color=GREEN, stroke_width=6,
        )
        seg_left_a = Line(
            [lx - seg_buff, by + b, 0], [lx - seg_buff, ty, 0],
            color=RED, stroke_width=6,
        )
        lbl_left_b = MathTex("b", font_size=38, color=GREEN)
        lbl_left_b.next_to(seg_left_b, LEFT, buff=0.15)
        lbl_left_a = MathTex("a", font_size=38, color=RED)
        lbl_left_a.next_to(seg_left_a, LEFT, buff=0.15)

        self.play(Create(seg_left_a), Create(seg_left_b), run_time=0.6)
        self.play(Write(lbl_left_a), Write(lbl_left_b), run_time=0.4)
        self.wait(0.3)

        # ── 6. Internal dividing lines (one at a time) ──
        v_div = Line(
            [lx + a, by, 0], [lx + a, ty, 0],
            color="#FFD700", stroke_width=6,
        )

        self.play(Create(v_div), run_time=0.6)
        self.wait(0.2)

        h_div = Line(
            [lx, by + b, 0], [rx, by + b, 0],
            color="#FFD700", stroke_width=6,
        )

        self.play(Create(h_div), run_time=0.6)
        self.wait(0.3)

        # ── 7. Highlight each region ──
        # a² region (top-left)
        a2_fill = Polygon(
            [lx, by + b, 0], [lx + a, by + b, 0],
            [lx + a, ty, 0], [lx, ty, 0],
            color=BLUE, fill_opacity=0.6, stroke_width=0,
        )
        lab_a2 = MathTex(r"\text{Area} = \mathbf{a}^2", font_size=38)
        lab_a2.set_color_by_gradient("#FF4500", "#FFD700", "#FF69B4")
        lab_a2.move_to([lx + a / 2, by + b + a / 2, 0])

        self.play(FadeIn(a2_fill), Write(lab_a2), run_time=0.8)
        self.wait(0.8)

        # ab region (bottom-left)
        ab1_fill = Polygon(
            [lx, by, 0], [lx + a, by, 0],
            [lx + a, by + b, 0], [lx, by + b, 0],
            color=GREEN, fill_opacity=0.6, stroke_width=0,
        )
        lab_ab1 = MathTex(r"\text{Area} = \mathbf{ab}", font_size=28)
        lab_ab1.set_color_by_gradient("#00E5FF", "#00FF88")
        lab_ab1.move_to([lx + a / 2, by + b / 2, 0])

        self.play(FadeIn(ab1_fill), Write(lab_ab1), run_time=0.8)
        self.wait(0.8)

        # ab region (top-right)
        ab2_fill = Polygon(
            [lx + a, by + b, 0], [rx, by + b, 0],
            [rx, ty, 0], [lx + a, ty, 0],
            color="#FF8C00", fill_opacity=0.6, stroke_width=0,
        )
        lab_ab2 = MathTex(r"\text{Area} = \mathbf{ab}", font_size=28)
        lab_ab2.set_color_by_gradient("#00E5FF", "#00FF88")
        lab_ab2.move_to([lx + a + b / 2, by + b + a / 2, 0])

        self.play(FadeIn(ab2_fill), Write(lab_ab2), run_time=0.8)
        self.wait(0.8)

        # b² region (bottom-right)
        b2_fill = Polygon(
            [lx + a, by, 0], [rx, by, 0],
            [rx, by + b, 0], [lx + a, by + b, 0],
            color=PINK, fill_opacity=0.6, stroke_width=0,
        )
        lab_b2 = MathTex(r"\text{Area} = \mathbf{b}^2", font_size=26)
        lab_b2.set_color_by_gradient("#0E52DA", "#00E5FF", "#00FF88")
        lab_b2.move_to([lx + a + b / 2, by + b / 2, 0])

        self.play(FadeIn(b2_fill), Write(lab_b2), run_time=0.8)
        self.wait(0.5)

        # ── 8. Create copies, morph to rearranged row (original stays) ──
        target_y = by - 2.5

        # Rearrange: a² on left, ab1+ab2 vertical side by side in middle, b² on right
        gap = 0.4
        total_width = a + gap + 2 * b + gap + b
        start_x = c[0] - total_width / 2

        a2_final_x = start_x + a / 2
        a2_final_y = target_y

        # ab1 and ab2 both vertical (b×a), side by side without gap
        ab1_final_x = start_x + a + gap + b / 2
        ab1_final_y = target_y

        ab2_final_x = start_x + a + gap + b + b / 2
        ab2_final_y = target_y

        ab_center_x = start_x + a + gap + b

        b2_final_x = start_x + a + gap + 2 * b + gap + b / 2
        b2_final_y = target_y

        # Create copies of each fill + label
        a2_copy = a2_fill.copy()
        lab_a2_copy = lab_a2.copy()
        ab1_copy = ab1_fill.copy()
        lab_ab1_copy = lab_ab1.copy()
        ab2_copy = ab2_fill.copy()
        lab_ab2_copy = lab_ab2.copy()
        b2_copy = b2_fill.copy()
        lab_b2_copy = lab_b2.copy()

        self.add(a2_copy, lab_a2_copy, ab1_copy, lab_ab1_copy,
                 ab2_copy, lab_ab2_copy, b2_copy, lab_b2_copy)

        # Animate copies: ab1 rotated to vertical, ab2 already vertical, side by side
        self.play(
            a2_copy.animate.move_to([a2_final_x, a2_final_y, 0]),
            lab_a2_copy.animate.move_to([a2_final_x, a2_final_y, 0]),
            ab1_copy.animate.move_to([ab1_final_x, ab1_final_y, 0]).rotate(PI / 2),
            lab_ab1_copy.animate.move_to([ab1_final_x, ab1_final_y, 0]),
            ab2_copy.animate.move_to([ab2_final_x, ab2_final_y, 0]),
            lab_ab2_copy.animate.move_to([ab2_final_x, ab2_final_y, 0]),
            b2_copy.animate.move_to([b2_final_x, b2_final_y, 0]),
            lab_b2_copy.animate.move_to([b2_final_x, b2_final_y, 0]),
            run_time=2.5,
        )
        self.wait(0.3)

        # Add rearranged summary labels below the row
        label_a2_final = MathTex("a^2", font_size=40, color=BLUE)
        label_a2_final.move_to([a2_final_x, a2_final_y - a / 2 - 0.5, 0])

        label_2ab_final = MathTex("2ab", font_size=40, color=GREEN)
        label_2ab_final.move_to([ab_center_x, ab1_final_y - a / 2 - 0.5, 0])

        label_b2_final = MathTex("b^2", font_size=40, color=PINK)
        label_b2_final.move_to([b2_final_x, b2_final_y - b / 2 - 0.5, 0])

        self.play(
            Write(label_a2_final),
            Write(label_2ab_final),
            Write(label_b2_final),
        )
        self.wait(0.5)

        # ── 9. Final consolidated breakdown ──
        rearranged_row = VGroup(
            a2_copy, lab_a2_copy,
            ab1_copy, lab_ab1_copy,
            ab2_copy, lab_ab2_copy,
            b2_copy, lab_b2_copy,
            label_a2_final, label_2ab_final, label_b2_final,
        )

        final = MathTex(
            r"(a+b)^2 = a^2 + 2ab + b^2",
            font_size=42,
        )
        final.set_color_by_gradient(BLUE, GREEN, YELLOW, PINK)
        final.next_to(rearranged_row, DOWN, buff=0.8)

        self.play(Write(final))
        self.wait(2)