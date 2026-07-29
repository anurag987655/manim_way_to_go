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
        self.wait(1)

        
