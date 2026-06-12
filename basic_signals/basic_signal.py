## Todays objective make up a function that defines this behaviour firstly a signal name appears then it is moved to top middle and then the formula appears for both the continuosus and discrete
# case sidewise middle which also moves but below the name of signal and finally graph animation to show how the graph is made 

from signal_sts import RAMP, DELTA, SIGNUM
from templates import SignalRenderer
import numpy as np 
from manim import * 

def u(n):
    return 1 if n>=0 else 0


def delta(n):
    return 1 if n == 0 else 0


class UnitStep(Scene):
    def construct(self):
        # Displaying the name of the lecture: 
        head = Text("Basic Signal Introduction", font="Times New Roman", weight=BOLD,color=BLUE_C)
        
        self.play(Write(head))
        self.wait(2)
        self.play(FadeOut(head))

        # Displaying title first and then moving to middle: 

        text = Text("Unit Step Function", font = "Times New Roman", weight=BOLD, color=BLUE_C)
        self.play(Write(text))
        self.wait(2)
        self.play(text.animate.to_edge(UP))

        # Displaying formulas for continuous as well as discrete time signal unit step: 

        LEFT_POS = LEFT * 4 + UP * 2.5 
        RIGHT_POS = RIGHT * 4  + UP * 2.5

        cont = Text("Continuous Time", font="Times New Roman", color=GREEN_C).scale(0.75)
        disc = Text("Discrete Time", font= "Times New Roman", color= GOLD).scale(0.75)

        cont.move_to(LEFT_POS)
        disc.move_to(RIGHT_POS)

        self.play(FadeIn(cont),FadeIn(disc))

        cont_formula = MathTex(
            r"u(t) = \begin{cases}1 & t \ge 0 \\ 0 & t < 0\end{cases}",
            color=GREEN_C
        ).scale(0.85)

        disc_formula = MathTex(
            r"u[n] = \begin{cases}1 & n \ge 0 \\ 0 & n < 0\end{cases}",
            color=GOLD
        ).scale(0.85)

        cont_formula.next_to(cont, DOWN, buff=0.4)
        disc_formula.next_to(disc, DOWN, buff=0.4)

        self.play(Write(cont_formula), Write(disc_formula))

        graph_y = DOWN * 1.6

        # creating graph: 

        ct_axes = Axes(x_range=[-5,5,1], y_range=[-0.5,1.5,1],axis_config={"color":GREY_B},x_axis_config={"include_numbers":True},y_axis_config={"include_numbers":True}).scale(0.45)
        ct_axes.move_to(LEFT*4 + graph_y)

        ct_ylab = MathTex(r"u(t)").scale(0.6)
        ct_xlab= MathTex(r"t").scale(0.6)

        ## positioning the x label and y label
        ct_ylab.next_to(ct_axes.y_axis,UP,buff=0.15)
        ct_xlab.next_to(ct_axes.x_axis,RIGHT,buff=0.15)

        ct_graph_0 = Line(ct_axes.c2p(-5, 0),ct_axes.c2p(0, 0),color=GREEN_C)

        ct_jump = Line(ct_axes.c2p(0, 0),ct_axes.c2p(0, 1),color=GREEN_C)

        ct_graph_1 = Line(ct_axes.c2p(0, 1),ct_axes.c2p(5, 1),color=GREEN_C)

        self.play(Create(ct_axes))
        self.play(FadeIn(ct_xlab),FadeIn(ct_ylab))
        self.play(Create(ct_graph_0),run_time=1.5)
        self.play(Create(ct_jump),run_time=1.5)
        self.play(Create(ct_graph_1),run_time=1)

        dt_axes = Axes(x_range=[-5,5,1],y_range=[-0.5,1.5,1],axis_config={"color":GREY_B},x_axis_config={"include_numbers":True},y_axis_config={"include_numbers":True}).scale(0.45)
        dt_axes.move_to(RIGHT*4 + graph_y)
        
        #setting up dt labels 
        dt_ylab=MathTex(r"u[n]").scale(0.6)
        dt_xlab=MathTex(r"n").scale(0.6)

        #positioning at correct place in the graph
        dt_ylab.next_to(dt_axes.y_axis,UP,buff=0.15)
        dt_xlab.next_to(dt_axes.x_axis,RIGHT,buff=0.15)

        stems=[]
        dots=[]

        for n in range(-5,5):
            x=n 
            y=u(n)

            stem = Line(dt_axes.c2p(x,0),dt_axes.c2p(x,y),color=GOLD,stroke_width=2)

            dot = Dot(dt_axes.c2p(x,y),color=GOLD).scale(0.8)
            stems.append(stem)
            dots.append(dot)

        self.play(Create(dt_axes))
        self.play(FadeIn(dt_xlab),FadeIn(dt_ylab))
        self.wait(0.5)

        for stem,dot in zip(stems,dots): 
            self.play(Create(stem),FadeIn(dot),run_time=0.6)
        self.wait(2)

        self.clear()

class RampScene(Scene):
    def construct(self):

        engine = SignalRenderer(self)

        objs = engine.setup_scene(RAMP)
        engine.animate_scene(objs)

        ct_axes = objs["ct_axes"]
        dt_axes = objs["dt_axes"]

        # -------------------------
        # CONTINUOUS RAMP
        # -------------------------
        ct_left = Line(
            ct_axes.c2p(-5, 0),
            ct_axes.c2p(0, 0),
            color=GREEN_C
        )

        ct_right = ParametricFunction(
            lambda t: ct_axes.c2p(t, t),
            t_range=[0, 4],
            color=GREEN_C
        )

        self.play(Create(ct_left))
        self.play(Create(ct_right), run_time=2)

        # -------------------------
        # DISCRETE RAMP
        # -------------------------
        for n in range(-5, 5):

            y = n if n >= 0 else 0

            stem = Line(
                dt_axes.c2p(n, 0),
                dt_axes.c2p(n, y),
                color=GOLD
            )

            dot = Dot(
                dt_axes.c2p(n, y),
                color=GOLD
            ).scale(0.8)

            self.play(Create(stem), FadeIn(dot), run_time=0.2)

        self.wait(2)


class DeltaScene(Scene):
    def construct(self):

        engine = SignalRenderer(self)

        objs = engine.setup_scene(DELTA)
        engine.animate_scene(objs)

        ct_axes = objs["ct_axes"]
        dt_axes = objs["dt_axes"]

        # =========================
        # CONTINUOUS-TIME DELTA
        # =========================

        impulse_arrow = Arrow(
            start=ct_axes.c2p(0, 0),
            end=ct_axes.c2p(0, 2),
            buff=0,
            color=GREEN_C,
            stroke_width=6
        )

        impulse_label = MathTex(r"\delta(t)", color=GREEN_C).scale(0.6)
        impulse_label.next_to(impulse_arrow.get_end(), UP, buff=0.1)

        self.play(
            GrowArrow(impulse_arrow),
            FadeIn(impulse_label),
            run_time=2
        )

        # =========================
        # DISCRETE-TIME DELTA
        # =========================

        for n in range(-5, 5):

            y = 1 if n == 0 else 0

            stem = Line(
                dt_axes.c2p(n, 0),
                dt_axes.c2p(n, y),
                color=GOLD,
                stroke_width=4
            )

            dot = Dot(
                dt_axes.c2p(n, y),
                color=GOLD
            ).scale(0.8)

            self.play(
                Create(stem),
                FadeIn(dot),
                run_time=0.3
            )

        self.wait(2)

class Signum(Scene):
    def construct(self):

        engine = SignalRenderer(self)

        objs = engine.setup_scene(SIGNUM)
        engine.animate_scene(objs)

        ct_axes = objs["ct_axes"]
        dt_axes = objs["dt_axes"]

        # =========================
        # CONTINUOUS SIGNUM
        # =========================

        left_part = Line(
            ct_axes.c2p(-5, -1),
            ct_axes.c2p(0, -1),
            color=GREEN_C
        )

        right_part = Line(
            ct_axes.c2p(0, 1),
            ct_axes.c2p(5, 1),
            color=GREEN_C
        )

        jump_line = Line(
            ct_axes.c2p(0, -1),
            ct_axes.c2p(0, 1),
            color=GREEN_C,
            stroke_width=2
        )

        self.play(Create(left_part), run_time=1.5)
        self.play(Create(jump_line), run_time=0.8)
        self.play(Create(right_part), run_time=1.5)
        

        # =========================
        # DISCRETE SIGNUM
        # =========================

        for n in range(-5, 5):

            if n > 0:
                y = 1
            elif n < 0:
                y = -1
            else:
                y = 0

            stem = Line(
                dt_axes.c2p(n, 0),
                dt_axes.c2p(n, y),
                color=GOLD,
                stroke_width=3
            )

            dot = Dot(
                dt_axes.c2p(n, y),
                color=GOLD
            ).scale(0.9)

            self.play(
                Create(stem),
                FadeIn(dot),
                run_time=0.3
            )

        self.wait(2)