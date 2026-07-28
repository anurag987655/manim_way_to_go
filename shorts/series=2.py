from manim import *

config.frame_rate = 60
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16
config.background_color = "#0E1117"


class InfiniteGeometricSeries(Scene):
    def construct(self):
        t1 = Text("Infinite Geometric", gradient=(BLUE_D, "#00FFFF"), font_size=44)
        t2 = Text("Series", gradient=(BLUE_D, "#00FFFF"), font_size=44)
        title = VGroup(t1, t2).arrange(DOWN, buff=0.05)
        title.to_edge(UP, buff=0.6)
        self.add(title)

        formula = MathTex(
            r"1", r"+", r"\frac{1}{2}", r"+", r"\frac{1}{4}", r"+", r"\frac{1}{8}",
            r"+", r"\cdots", r"=", r"2",
            color=WHITE, font_size=42,
        )
        formula.next_to(title, DOWN, buff=0.5)
        self.add(formula)

        self.wait(0.8)

        VW, VH = 6.0, 4.0
        cy = -1.2

        rect = Rectangle(width=VW, height=VH, color=WHITE, stroke_width=3)
        rect.move_to([0, cy, 0])
        self.play(Create(rect))
        self.wait(0.5)

        w_brace = Brace(rect, DOWN, buff=0.1)
        w_label = w_brace.get_tex("2")
        h_brace = Brace(rect, RIGHT, buff=0.1)
        h_label = h_brace.get_tex("1")
        self.play(GrowFromCenter(w_brace), Write(w_label), GrowFromCenter(h_brace), Write(h_label))
        self.wait(0.5)

        palette = [BLUE_D, BLUE_C, BLUE_B, BLUE_A, TEAL_B, TEAL_C, TEAL_D, TEAL_E]

        rem = [-VW / 2, VW / 2, cy - VH / 2, cy + VH / 2]
        n_splits = 6
        fills = []
        labels = []

        for i in range(n_splits):
            ro = rem[:]

            if i % 2 == 0:
                mid = (rem[0] + rem[1]) / 2
                labeled = [rem[0], mid, rem[2], rem[3]]
                rem = [mid, rem[1], rem[2], rem[3]]
                div = Line([mid, ro[2], 0], [mid, ro[3], 0], color=WHITE, stroke_width=2)
            else:
                mid = (rem[2] + rem[3]) / 2
                labeled = [rem[0], rem[1], mid, rem[3]]
                rem = [rem[0], rem[1], rem[2], mid]
                div = Line([ro[0], mid, 0], [ro[1], mid, 0], color=WHITE, stroke_width=2)

            pw = labeled[1] - labeled[0]
            ph = labeled[3] - labeled[2]
            pc_x = (labeled[0] + labeled[1]) / 2
            pc_y = (labeled[2] + labeled[3]) / 2

            fill = Rectangle(
                width=pw, height=ph,
                color=palette[i % len(palette)],
                fill_opacity=0.6, stroke_width=0,
            )
            fill.move_to([pc_x, pc_y, 0])
            self.play(FadeIn(fill, scale=0.5), run_time=0.6)
            fills.append(fill)

            if i < n_splits - 1:
                self.play(GrowFromCenter(div), run_time=0.35)

            txt = "1" if i == 0 else f"\\frac{{1}}{{{2**i}}}"
            fs = max(28 - i * 3, 10)
            label = MathTex(txt, color=GOLD, font_size=fs)
            label.move_to([pc_x, pc_y, 0])
            self.play(Write(label), run_time=0.35)
            labels.append(label)

            if i < 4:
                self.play(formula[i * 2].animate.set_color(YELLOW), run_time=0.25)

            self.wait(0.6)

        tail = Rectangle(
            width=rem[1] - rem[0], height=rem[3] - rem[2],
            color=GREY_B, fill_opacity=0.4, stroke_width=0,
        )
        tail.move_to([(rem[0] + rem[1]) / 2, (rem[2] + rem[3]) / 2, 0])
        self.play(FadeIn(tail, scale=0.5), run_time=0.8)

        self.play(
            formula[-2].animate.set_color(YELLOW),
            formula[-1].animate.set_color(YELLOW),
            run_time=0.5,
        )

        self.wait(1.5)

        self.play(
            *[FadeOut(m, shift=UP * 0.3) for m in [title, formula, rect] + fills + [tail] + labels],
            run_time=1.5,
        )
        self.wait(0.5)
