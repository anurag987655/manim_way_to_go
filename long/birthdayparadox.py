## videos aim to show the birthday paradox...


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
        self.wait(2)