# Videos objective : to make learner familiar with discrete and continuous time singal. How discrete time signal exists in integer space and reveal a basic difference between them.
import numpy as np 
from manim import *

class Continuous(Scene):
    def construct(self):

        text1 = Text(
            "Introducing discrete and continuous time signal",
            color=BLUE_C
        )

        self.play(Write(text1), run_time=2)
        self.play(FadeOut(text1))

        text2 = Text("Continous time?",color=BLUE_C)
        self.play(Write(text2),run_time=2)
        self.play(FadeOut(text2))

        Caxis = NumberLine(
            x_range=[-6,6,1],
            include_ticks=False,
            include_numbers=False
        ).set_stroke(width=6, opacity=0.6)

        highlight = Line(Caxis.n2p(-4),Caxis.n2p(4),color=BLUE,stroke_width=8)
        highlight.set_opacity(0.6)

        left = MathTex("-4").next_to(Caxis.n2p(-4),DOWN)
        right = MathTex("4").next_to(Caxis.n2p(4),DOWN)

        label = MathTex("t").next_to(Caxis, RIGHT)

        self.play(Create(Caxis), Write(label), run_time=2)
        self.play(Create(highlight),Write(left),Write(right),run_time=2)

        dot = Dot(color=YELLOW).scale(1.5)
        dot.move_to(Caxis.n2p(-4))

        self.play(FadeIn(dot))

        time_label = MathTex(r"t=-4\,s",color=GREEN).next_to(dot, DOWN,buff=0.6)
        self.play(Write(time_label))
        self.wait(2)
        self.play(FadeOut(time_label))

        points = [-1.22, 2.999, 4.0]

        for p in points:

            # 1. move dot
            self.play(
                dot.animate.move_to(Caxis.n2p(p)),
                run_time=2,
                rate_func=linear
            )

            self.wait(2)

            
            time_label = MathTex(rf"t={p}\,s",color=GREEN).next_to(dot, DOWN,buff=0.6)

            self.play(Write(time_label))

          
            self.wait(1)
            self.play(FadeOut(time_label))

        self.wait(1)

        # Introducing discrete time: 
        Daxis = NumberLine(
            x_range=[-6,6,1],
            include_ticks=True,
            include_numbers=False
        ).set_stroke(width=6, opacity=0.6)

        highlight = Line(Daxis.n2p(-4),Daxis.n2p(4),color=BLUE,stroke_width=8)
        highlight.set_opacity(0.6)

        self.clear()

        text3=Text("Discrete time?")

        self.play(Write(text3),run_time=2)
        self.wait(1)
        self.play(FadeOut(text3))

        label1 = MathTex("n").next_to(Caxis,RIGHT)
        self.play(Create(Daxis),Write(label1),run_time=2)
        self.play(Create(highlight),run_time=2)
        highlight.set_opacity(0.6)

        ## creating the interval in  highlighted region: 

        labels = VGroup()

        for i in range(-4,5):
            lbl = MathTex(str(i),font_size=30).next_to(Caxis.n2p(i),DOWN,buff=0.2)
            labels.add(lbl)

        self.play(LaggedStart(*[Write(l) for l in labels],lag_ratio=0.1))
        
        self.wait(2)
       
        points = [-4,-3,-2,-1,0,1,2,3,4]

        dot = Dot(color=YELLOW).scale(1.5).move_to(Daxis.n2p(points[0]))

        self.play(FadeIn(dot))

        for p in points[1:]:
            new_dot=Dot(color=YELLOW).scale(1.5).move_to(Daxis.n2p(p))

            self.play(FadeOut(dot),FadeIn(new_dot),run_time=1)
            dot=new_dot

        self.clear()
        text4=Text("what about signals in discrete and continuous time?", font="Times New Roman", color=BLUE_C)
        self.play(Write(text4))

        self.play(FadeOut(text4))
        
        # Creating a axes for plotting continuous time sine wave

        text5=Text("Continuous time signal", font="Times New Roman", color= BLUE_C)
        self.play(Write(text5))
        self.wait(1)


        self.play(text5.animate.to_edge(UP))
        self.wait(1)

        # defining sine animation for the continuous singal: 

        axes = Axes(x_range=[0,9,1],y_range=[-2,2,1],x_length=10,y_length=5,tips=True)

        graph = axes.plot(lambda t : np.sin(t),x_range=[0,8],color=YELLOW)


        axes.x_axis.get_tip().scale(0.5)
        axes.y_axis.get_tip().scale(0.5)

        x_labels= axes.get_x_axis().add_numbers([0,1,2,3,4,5,6,7,8])
        y_labels = axes.get_y_axis().add_numbers([-1,0,1])

        self.play(Create(axes))
        self.wait(2)
        ## creating a label 
        t_label = MathTex(r"t")
        x_label = MathTex(r"x(t)")

        t_label.next_to(axes.x_axis.get_end(),DOWN)
        x_label.next_to(axes.y_axis.get_end(),UP)

        self.play(Write(t_label),Write(x_label))

        self.play(Create(graph),run_time=3)

        self.wait(1)

        self.clear()

        text6=Text("Discrete time signal", font = "Times New Roman", color= BLUE_C)

        self.play(Write(text6), run_time=3)
        
        self.play(text6.animate.to_edge(UP))
        self.wait(1)


        d_axis = Axes(x_range=[0,9,1],y_range=[-2,2,1],x_length=10,y_length=5,tips=True)

        d_axis.x_axis.get_tip().scale(0.5)
        d_axis.y_axis.get_tip().scale(0.5)

        x_labels= d_axis.get_x_axis().add_numbers([0,1,2,3,4,5,6,7,8])
        y_labels = d_axis.get_y_axis().add_numbers([-1,0,1])

        n_label= MathTex(r"n")
        x_label=MathTex(r"x[n]")

        n_label.next_to(d_axis.x_axis.get_end(), DOWN)
        x_label.next_to(d_axis.y_axis.get_end(), UP)


        self.play(Create(d_axis))

        self.play(Write(n_label),Write(x_label))

        n_values= np.arange(0,9,1)
        y_values= np.sin(n_values)


        ball = Dot(d_axis.c2p(0,0),color=YELLOW, radius=0.1)
        self.add(ball)

        stems = VGroup()
        dots = VGroup()

        for n,y in zip(n_values,y_values):
            target_top = d_axis.c2p(n,y)
            target_bottom= d_axis.c2p(n,0)

            self.play(ball.animate.move_to(d_axis.c2p(n,0)),run_time=0.3)

            stem = Line(target_bottom,target_top,color=BLUE)

            self.play(Create(stem),run_time=0.3)

            self.play(ball.animate.move_to(target_top),run_time=0.3)

            dot = Dot(target_top,color=YELLOW)
            self.add(dot)
            
            stems.add(stem)
            dots.add(dot)