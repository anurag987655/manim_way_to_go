## videos aim to show the birthday paradox...


import random

from manim import *

class GenScene(Scene):
    def construct(self):
        room = Rectangle(width=6, height=4, color=WHITE)
        self.play(Create(room))

        def make_grid(n, color, rows, cols):
            cell_w = (room.width * 0.7) / cols
            cell_h = (room.height * 0.7) / rows
            return VGroup(*[Dot(color=color, radius=0.06) for _ in range(n)]).arrange_in_grid(
                rows=rows, cols=cols, cell_size=(cell_w, cell_h), buff=0.2
            ).move_to(room.get_center())

        people_100 = make_grid(100, BLUE, 10, 10)
        label_100 = Text("100 People", color=WHITE).next_to(room, UP)
        self.play(Create(people_100), Write(label_100))
        self.wait(2)

        people_50 = make_grid(50, GREEN, 10, 5)
        label_50 = Text("50 People", color=WHITE).next_to(room, UP)
        self.play(Transform(people_100, people_50), Transform(label_100, label_50))
        self.wait(2)

        people_23 = make_grid(23, RED, 6, 4)
        label_23 = Text("23 People", color=WHITE).next_to(room, UP)
        self.play(Transform(people_100, people_23), Transform(label_100, label_23))
        self.wait(2)

        birthday_paradox = Text("Birthday Paradox", gradient=(BLUE, GREEN, RED)).scale(1.5)
        self.play(FadeOut(people_100), FadeOut(label_100), FadeOut(room))
        self.play(Write(birthday_paradox))
        self.play(birthday_paradox.animate.to_edge(UP))
        self.wait(1)

        # ---- Second part: explanation with arrows ----

        room2 = Rectangle(width=6, height=4, color=WHITE).shift(DOWN)
        n = 50
        dots2 = VGroup(*[Dot(color=BLUE, radius=0.06) for _ in range(n)])
        for dot in dots2:
            dot.move_to(room2.get_center() + np.array([
                random.uniform(-room2.width/2 + 0.2, room2.width/2 - 0.2),
                random.uniform(-room2.height/2 + 0.2, room2.height/2 - 0.2),
                0
            ]))
        label2 = Text(f"n People", color=WHITE).next_to(room2, UP)
        self.play(FadeIn(room2), FadeIn(dots2), Write(label2))
        self.wait(1)

        group2 = VGroup(room2, dots2, label2)
        self.play(group2.animate.scale(0.6).shift(UP * 1.1))
        self.wait(0.5)

        arrow1 = Arrow(start=DOWN * 0.5, end=ORIGIN, color=BLUE).next_to(room2, DOWN, buff=0).shift(LEFT * 1.5)
        arrow2 = Arrow(start=DOWN * 0.5, end=ORIGIN, color=GREEN).next_to(room2, DOWN, buff=0).shift(RIGHT * 1.5)
        self.play(GrowArrow(arrow1), GrowArrow(arrow2))
        self.wait(0.5)

        case1 = Text("Case i: n > 365", color=BLUE, font_size=24).next_to(arrow1, DOWN, buff=0.5)
        prob1 = Text("P(match) = 1", color=BLUE, font_size=20).next_to(case1, DOWN, buff=0.25)
        self.play(Write(case1))
        self.wait(2)
        self.play(Write(prob1))
        self.wait(2)

        case2 = Text("Case ii: n < 365", color=GREEN, font_size=24).next_to(arrow2, DOWN, buff=0.5)
        # wont be using 
        # prob2 = MathTex(r"P = 1 - \frac{365!}{(365-n)! \cdot 365^n}", color=GREEN, font_size=28).next_to(case2, DOWN, buff=0.15)
        self.play(Write(case2))
        self.wait(3)

        # ---- Third part: solving the equation ----

        gold_rect = SurroundingRectangle(case2, color=GOLD, buff=0.15)
        self.play(Create(gold_rect))

        self.play(FadeOut(case1), FadeOut(prob1), FadeOut(arrow1), FadeOut(arrow2))
        self.wait(0.3)

        target_y = case2.get_center()[1]
        self.play(
            case2.animate.move_to([0, target_y, 0]),
            gold_rect.animate.move_to([0, target_y, 0])
        )
        self.wait(1)

        prob_label = MathTex(r"P(\text{no match}) =", color=WHITE, font_size=28).next_to(gold_rect, DOWN, buff=0.8).align_to(gold_rect, LEFT)
        self.play(Write(prob_label))
        self.wait(1)

        room_group = VGroup(room2, dots2, label2)
        self.play(room_group.animate.shift(LEFT * 3.5))
        self.wait(0.5)
