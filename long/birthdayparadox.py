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

        cal_days = VGroup(*[Square(side_length=0.15, color=GREY, fill_opacity=0.25) for _ in range(365)])
        cal_days.arrange_in_grid(cols=15, cell_size=(0.2, 0.2), buff=0.02)
        cal_days.move_to(RIGHT * 3.2 )
        self.play(FadeIn(cal_days, shift=UP, lag_ratio=0.01))
        self.wait(0.5)

        cal_label = Text("365 days", color=WHITE,font_size=25).next_to(cal_days, UP, buff=0.1)
        self.play(Write(cal_label))
        self.wait(2)

        # ---- Fourth part: one person jumps through days ----

        person = random.choice(dots2.submobjects)
        person.set_color(YELLOW)

        days_pos = [d.get_center() for d in cal_days.submobjects]
        first = random.choice(days_pos)
        jumps = random.choices(days_pos, k=6)
        final = random.choice(days_pos)

        self.play(person.animate.move_to(first).set_color(YELLOW), run_time=1.5)
        for p in jumps:
            self.play(person.animate.move_to(p), run_time=0.5)
        self.play(person.animate.move_to(final), run_time=3)
        self.wait(1)

        # ---- Fifth part: probability tracking ----

        frac = MathTex(r"\frac{365}{365}", color=WHITE, font_size=28).next_to(prob_label, RIGHT, buff=0.2)
        self.play(Write(frac))
        self.wait(1)

        available = [p for p in days_pos if not np.allclose(p, final)]

        person2 = random.choice([d for d in dots2.submobjects if d is not person])
        person2.set_color(ORANGE)

        first2 = random.choice(available)
        jumps2 = random.choices(available, k=6)
        final2 = random.choice(available)

        self.play(person2.animate.move_to(first2).set_color(ORANGE), run_time=0.8)
        for p in jumps2:
            self.play(person2.animate.move_to(p), run_time=0.12)
        self.play(person2.animate.move_to(final2), run_time=0.4)
        self.wait(0.5)

        new_frac = MathTex(r"\frac{365}{365} \times \frac{364}{365}", color=WHITE, font_size=28).next_to(prob_label, RIGHT, buff=0.2)
        self.play(Transform(frac, new_frac))
        self.wait(1)

        # ---- Sixth part: third person, then shuffle all ----

        occupied = [final, final2]
        available3 = [p for p in days_pos if not any(np.allclose(p, o) for o in occupied)]

        person3 = random.choice([d for d in dots2.submobjects if d not in (person, person2)])
        person3.set_color(RED)

        first3 = random.choice(available3)
        jumps3 = random.choices(available3, k=6)
        final3 = random.choice(available3)

        self.play(person3.animate.move_to(first3).set_color(RED), run_time=0.8)
        for p in jumps3:
            self.play(person3.animate.move_to(p), run_time=0.12)
        self.play(person3.animate.move_to(final3), run_time=0.4)
        self.wait(0.5)

        new_frac2 = MathTex(r"\frac{365}{365} \times \frac{364}{365} \times \frac{363}{365}", color=WHITE, font_size=28).next_to(prob_label, RIGHT, buff=0.2)
        self.play(Transform(frac, new_frac2))
        self.wait(1)

        # ---- Seventh part: move everyone to calendar ----

        on_cal = [person, person2, person3]
        cal_centers = [d.get_center() for d in cal_days.submobjects]
        taken = [p.get_center() for p in on_cal]
        empty = [c for c in cal_centers if not any(np.allclose(c, t) for t in taken)]

        rest = [d for d in dots2.submobjects if d not in on_cal]
        to_move = rest[:-1]
        stay = rest[-1]

        positions = random.sample(empty, len(to_move))
        for d, pos in zip(to_move, positions):
            self.play(d.animate.move_to(pos), run_time=0.25)

        frac_dots = MathTex(r"\frac{365}{365} \times \frac{364}{365} \times \frac{363}{365} \times \cdots", color=WHITE, font_size=28).next_to(prob_label, RIGHT, buff=0.2)
        self.play(Transform(frac, frac_dots))
        self.wait(1)

        # ---- Eighth part: last person moves to calendar ----

        all_on_cal = [person, person2, person3] + to_move
        taken_centers = [d.get_center() for d in all_on_cal]
        vacant = [c for c in cal_centers if not any(np.allclose(c, t) for t in taken_centers)]

        target = random.choice(vacant)
        self.play(stay.animate.move_to(target), run_time=2)
        self.wait(0.5)

        total = len(all_on_cal) + 1
        final_frac = MathTex(
            rf"\frac{{365}}{{365}} \times \frac{{364}}{{365}} \times \frac{{363}}{{365}} \times \cdots \times \frac{{365-(n-1)}}{{365}}",
            color=WHITE, font_size=28
        ).next_to(prob_label, RIGHT, buff=0.2)
        self.play(Transform(frac, final_frac))
        self.wait(1)

        # ---- Ninth part: cleanup and refocus ----

        self.play(
            FadeOut(room2), FadeOut(label2), FadeOut(cal_days), FadeOut(cal_label),
            FadeOut(dots2)
        )
        self.wait(0.5)

        title_bottom = birthday_paradox.get_bottom()[1]
        case2_target = [0, title_bottom - 0.5, 0]
        self.play(
            case2.animate.move_to(case2_target),
            gold_rect.animate.move_to(case2_target)
        )
        self.wait(0.5)

        eq_group = VGroup(prob_label, frac)
        eq_target = gold_rect.get_center() + DOWN * 0.9
        self.play(eq_group.animate.move_to(eq_target))
        self.wait(1)

        # ---- Tenth part: match formula and table ----

        match_label = MathTex(r"P(\text{match}) = 1 - P(\text{no match})", color=WHITE, font_size=24)
        match_label.next_to(eq_group, DOWN, buff=0.4)
        self.play(Write(match_label))
        self.wait(1)

        def p_match(n):
            p = 1.0
            for i in range(n):
                p *= (365 - i) / 365
            return 1 - p

        ns = [1, 10, 15, 23, 50, 60]
        rows = [["People", "P(match)"]]
        for n in ns:
            rows.append([str(n), f"{p_match(n):.4f}"])

        table = Table(rows, include_outer_lines=True).scale(0.35)
        table.next_to(match_label, DOWN, buff=0.4)
        self.play(Create(table))
        self.wait(2)

        # ---- Eleventh part: graph ----

        self.play(FadeOut(eq_group), FadeOut(match_label))
        self.play(table.animate.next_to(gold_rect, DOWN, buff=0.3).shift(LEFT * 3))
        self.wait(0.5)

        axes = Axes(
            x_range=[0, 110, 10],
            y_range=[0, 1.1, 0.1],
            x_length=5.5,
            y_length=3,
            axis_config={"color": WHITE},
        )
        axes.next_to(gold_rect, DOWN, buff=0.5).shift(RIGHT * 2.5)
        axes.add_coordinates(font_size=18)
        

        x_label = Text("People (n)", font_size=18).next_to(axes.get_x_axis(), RIGHT, buff=0.3)
        y_label = Text("Probability (P)", font_size=18).next_to(axes.get_y_axis(), UP, buff=0.1)

        self.play(Create(axes), Write(x_label), Write(y_label))
        self.wait(0.5)

        def p_curve(x):
            n = int(x)
            if n <= 0:
                return 0
            p = 1.0
            for i in range(n):
                p *= (365 - i) / 365
            return 1 - p

        graph = axes.plot(p_curve, x_range=[1, 100], color=GOLD)
        self.play(Create(graph), run_time=3)
        self.wait(2)

