## videos objective : visualizing a square - b square = a + b a - b animation idea firstly there should be a title and then below it there should be a formula for titile gradient of 
# blue purple and pink and just below it there should be formula and it should also be gradient and then finally below it there should be a big square of size a inside it small at 
# right down corner of it with left corner align should be b square the a square - b square portion should be  highlighted and then transformed to form the rectangle of side
## a - b a + b 

from manim import *

config.frame_rate = 60
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16
config.background_color = "#0E1117"

class formula1(Scene):
    def construct(self):
        title = Text("Visualizing Geometrically", gradient=(BLUE, PURPLE, PINK), font_size=44)
        title.to_edge(UP, buff=0.6)
        
        formula = MathTex("a^2 - b^2 = (a + b)(a - b)")
        formula.set_color_by_gradient(BLUE, GREEN, YELLOW)
        formula.next_to(title, DOWN, buff=0.4)
        self.add(title,formula)
        
        a = 4.5
        square_a = Square(side_length=a, color=BLUE, fill_opacity=0.3)
        square_a.next_to(formula,DOWN, buff = 1.5)
        label_a = MathTex("a", font_size=36, color=RED)
        label_a.next_to(square_a, UP, buff=0.2)

        dash_len = 0.18
        stroke_w = 4
        offset_a = 0.06
        offset_b = 0.2

        def add_ticks(square, color, n_ticks, side_center_offset):
            c = square.get_center()
            s = square.side_length
            half = s / 2
            l = c[0] - half
            r = c[0] + half
            b = c[1] - half
            t = c[1] + half

            ticks = VGroup()
            sides = [
                ((c[0], t), True),
                ((c[0], b), True),
                ((l, c[1]), False),
                ((r, c[1]), False),
            ]
            for (sx, sy), is_horizontal in sides:
                if n_ticks == 1:
                    offsets = [0]
                else:
                    offsets = [-side_center_offset, side_center_offset]
                for off in offsets:
                    if is_horizontal:
                        start = [sx + off, sy - dash_len / 2, 0]
                        end = [sx + off, sy + dash_len / 2, 0]
                    else:
                        start = [sx - dash_len / 2, sy + off, 0]
                        end = [sx + dash_len / 2, sy + off, 0]
                    ticks.add(Line(start, end, color=color, stroke_width=stroke_w))
            return ticks

        ticks_a = add_ticks(square_a, BLUE, 2, offset_a)
        ticks_a.set_stroke(opacity=0)

        self.play(Create(square_a), Write(label_a))
        self.wait(0.3)
        self.play(ticks_a.animate.set_stroke(opacity=1), run_time=0.5)
        self.wait(0.3)

        area_label_a = MathTex(r"\textbf{Area} = \mathbf{a}^2", font_size=42)
        area_label_a.set_color_by_gradient("#FF4500", "#FFD700", "#FF69B4")
        area_label_a.move_to(square_a.get_center())
        self.play(Write(area_label_a))
        self.wait(0.5)
        self.play(FadeOut(area_label_a))
        self.wait(0.2)

        b = a * 0.5
        square_b = Square(side_length=b, color=RED, fill_opacity=0.3)
        square_b.align_to(square_a, DOWN)
        square_b.align_to(square_a, RIGHT)
        label_b = MathTex("b", font_size=30, color=RED)
        label_b.next_to(square_b, UP, buff=0.2)

        ticks_b = add_ticks(square_b, RED, 1, offset_b)
        ticks_b.set_stroke(opacity=0)

        self.play(Create(square_b), Write(label_b), run_time=0.8)
        self.play(ticks_b.animate.set_stroke(opacity=1), run_time=0.4)
        self.wait(0.3)

        area_label_b = MathTex(r"\textbf{Area} = \mathbf{b}^2", font_size=34)
        area_label_b.set_color_by_gradient("#0E52DA", "#00E5FF", "#00FF88")
        area_label_b.move_to(square_b.get_center())
        self.play(Write(area_label_b))
        self.wait(0.5)
        self.play(FadeOut(area_label_b))
        self.wait(0.3)

        c = square_a.get_center()
        lx = c[0] - a / 2
        rx = c[0] + a / 2
        by = c[1] - a / 2
        ty = c[1] + a / 2
        bx = rx - b
        by2 = by + b

        right_seg = Line(
            [rx, by2, 0], [rx, ty, 0],
            color="#FFD700", stroke_width=8
        )
        label_ab_right = MathTex("a-b", font_size=36)
        label_ab_right.set_color_by_gradient("#FF4500", "#FFD700")
        label_ab_right.next_to(right_seg, RIGHT, buff=0.15)

        self.play(Create(right_seg))
        self.wait(0.3)
        self.play(Write(label_ab_right))
        self.wait(0.5)

        bottom_seg = Line(
            [lx, by, 0], [bx, by, 0],
            color="#00E5FF", stroke_width=8
        )
        label_ab_bottom = MathTex("a-b", font_size=36)
        label_ab_bottom.set_color_by_gradient("#00E5FF", "#00FF88")
        label_ab_bottom.next_to(bottom_seg, DOWN, buff=0.15)

        self.play(Create(bottom_seg))
        self.wait(0.3)
        self.play(Write(label_ab_bottom))
        self.wait(0.5)

        right_bottom_ticks_a = VGroup(ticks_a[2], ticks_a[3], ticks_a[6], ticks_a[7])
        right_bottom_ticks_b = VGroup(ticks_b[1], ticks_b[3])
        self.play(FadeOut(right_bottom_ticks_a), FadeOut(right_bottom_ticks_b))
        self.wait(0.3)

        l_left = Line([lx, by, 0], [lx, ty, 0], color=BLUE, stroke_width=5)
        l_top = Line([lx, ty, 0], [rx, ty, 0], color=BLUE, stroke_width=5)
        l_right = Line([rx, ty, 0], [rx, by2, 0], color=BLUE, stroke_width=5)
        l_b_top = Line([rx, by2, 0], [bx, by2, 0], color=BLUE, stroke_width=5)
        l_b_left = Line([bx, by2, 0], [bx, by, 0], color=BLUE, stroke_width=5)
        l_bottom = Line([bx, by, 0], [lx, by, 0], color=BLUE, stroke_width=5)
        l_shape = VGroup(l_left, l_top, l_right, l_b_top, l_b_left, l_bottom)

        self.play(Create(l_shape), run_time=1.5)
        self.wait(0.2)

        hollow_fill = Polygon(
            [lx, ty, 0], [rx, ty, 0], [rx, by2, 0],
            [bx, by2, 0], [bx, by, 0], [lx, by, 0],
            color=BLUE, fill_opacity=0.3, stroke_width=0
        )
        self.play(FadeIn(hollow_fill), run_time=0.5)
        self.play(FadeOut(square_a), FadeOut(square_b), FadeOut(right_seg), FadeOut(bottom_seg), run_time=1)
        self.wait(0.3)

        area_label_hollow = MathTex(r"\textbf{Area} = \mathbf{a}^2 - \mathbf{b}^2", font_size=36)
        area_label_hollow.set_color_by_gradient("#FF4500", "#FFD700", "#FF69B4")
        area_label_hollow.move_to([c[0] - b / 2 + 0.5, c[1] + 0.5, 0])
        self.play(Write(area_label_hollow))
        self.wait(0.5)
        self.play(FadeOut(area_label_hollow))
        self.wait(0.3)

        buff = 1.0
        lo = 1.1
        target_fill = Polygon(
            [lx - lo, by - buff, 0], [lx - lo + a + b, by - buff, 0],
            [lx - lo + a + b, by - buff - (a - b), 0], [lx - lo, by - buff - (a - b), 0],
            color=BLUE, fill_opacity=0.3, stroke_width=0
        )
        t_top_l = Line([lx - lo, by - buff, 0], [lx - lo + a, by - buff, 0], color=BLUE, stroke_width=5)
        t_top_r = Line([lx - lo + a, by - buff, 0], [lx - lo + a + b, by - buff, 0], color=BLUE, stroke_width=5)
        t_right = Line([lx - lo + a + b, by - buff, 0], [lx - lo + a + b, by - buff - (a - b), 0], color=BLUE, stroke_width=5)
        t_bot_l = Line([lx - lo, by - buff - (a - b), 0], [lx - lo + (a - b), by - buff - (a - b), 0], color=BLUE, stroke_width=5)
        t_bot_r = Line([lx - lo + (a - b), by - buff - (a - b), 0], [lx - lo + a + b, by - buff - (a - b), 0], color=BLUE, stroke_width=5)
        t_left = Line([lx - lo, by - buff - (a - b), 0], [lx - lo, by - buff, 0], color=BLUE, stroke_width=5)

        d_top = t_top_l.get_center() - l_top.get_center()
        d_top_r = t_top_r.get_center() - l_b_top.get_center()
        d_right = t_right.get_center() - l_right.get_center()
        d_bot_l = t_bot_l.get_center() - l_bottom.get_center()
        d_bot_r = t_bot_r.get_center() - l_b_left.get_center()

        la_t = label_a.copy().next_to(t_top_l, UP, buff=0.15).get_center()
        lb_t = label_b.copy().next_to(t_top_r, UP, buff=0.15).get_center()
        lab_r_t = label_ab_right.copy().next_to(t_right, RIGHT, buff=0.15).get_center()
        lab_l_t = label_ab_bottom.copy().next_to(t_left, LEFT, buff=0.15).get_center()

        self.play(Transform(hollow_fill, target_fill), run_time=1.2)
        self.wait(0.2)

        tlk = dash_len
        tof = offset_a
        nt_l1 = Line([lx - lo + a / 2 - tof, by - buff - tlk / 2, 0], [lx - lo + a / 2 - tof, by - buff + tlk / 2, 0], color=BLUE, stroke_width=4)
        nt_l2 = Line([lx - lo + a / 2 + tof, by - buff - tlk / 2, 0], [lx - lo + a / 2 + tof, by - buff + tlk / 2, 0], color=BLUE, stroke_width=4)
        nt_r = Line([lx - lo + a + b / 2, by - buff - tlk / 2, 0], [lx - lo + a + b / 2, by - buff + tlk / 2, 0], color=BLUE, stroke_width=4)
        nl_1 = Line([lx - lo - tlk / 2, by - buff - (a - b) / 2 - tof, 0], [lx - lo + tlk / 2, by - buff - (a - b) / 2 - tof, 0], color=BLUE, stroke_width=4)
        nl_2 = Line([lx - lo - tlk / 2, by - buff - (a - b) / 2 + tof, 0], [lx - lo + tlk / 2, by - buff - (a - b) / 2 + tof, 0], color=BLUE, stroke_width=4)
        nbr = Line([lx - lo + (a - b) + b / 2, by - buff - (a - b) - tlk / 2, 0], [lx - lo + (a - b) + b / 2, by - buff - (a - b) + tlk / 2, 0], color=BLUE, stroke_width=4)

        self.play(Transform(l_top, t_top_l), Transform(ticks_a[0], nt_l1), Transform(ticks_a[1], nt_l2), label_a.animate.move_to(la_t), run_time=0.7)
        self.wait(0.15)
        self.play(Transform(l_b_top, t_top_r), Transform(ticks_b[0], nt_r), label_b.animate.move_to(lb_t), run_time=0.7)
        self.wait(0.15)
        self.play(Transform(l_right, t_right), label_ab_right.animate.move_to(lab_r_t), run_time=0.7)
        self.wait(0.15)
        self.play(Transform(l_bottom, t_bot_l), run_time=0.7)
        self.wait(0.15)
        self.play(Transform(l_b_left, t_bot_r), Transform(ticks_b[2], nbr), run_time=0.7)
        self.wait(0.15)
        self.play(Transform(l_left, t_left), Transform(ticks_a[4], nl_1), Transform(ticks_a[5], nl_2), label_ab_bottom.animate.move_to(lab_l_t), run_time=0.7)
        self.wait(0.3)

        label_apb = MathTex("a+b", font_size=36, color=BLUE)
        label_apb.next_to(t_top_l, UP, buff=0.1)
        label_apb.shift(RIGHT * b / 2)
        self.play(Write(label_apb))
        self.wait(0.3)

        area_rect = MathTex(r"\textbf{Area} = (\mathbf{a} + \mathbf{b})(\mathbf{a} - \mathbf{b})", font_size=36)
        area_rect.set_color_by_gradient("#FF4500", "#FFD700", "#FF69B4")
        area_rect.move_to([lx - lo + (a + b) / 2, by - buff - (a - b) / 2, 0])
        self.play(Write(area_rect))
        self.wait(2)

        
