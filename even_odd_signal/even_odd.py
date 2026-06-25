import sys
sys.path.insert(0, "/home/anurag/Desktop/manim_way_to_go")
from global_templates import ct_axes, dt_axes
from manim import *
import numpy as np 


class Scene1(Scene):
    def construct(self):
        title = Text("Even and Odd signal", color = BLUE_C)
        self.play(Write(title), run_time = 2)
        self.play(FadeOut(title))

        title1 = Text("Even Signal", color = BLUE_C)
        self.play(Write(title1, run_time = 2))
        self.play(title1.animate.to_edge(UP))
        self.wait(1)

        even_eq = MathTex(r"x(t) = x(-t)", color = GOLD)
        even_eq.next_to(title1, DOWN, buff = 0.5)
        self.play(Write(even_eq), run_time = 2)

        # Positioning the continuous axis
        caxes, x_lab, y_lab = ct_axes(y_range=[-1.2, 1.5, 0.5])
        caxes.next_to(even_eq, DOWN, buff = 0.3)
        self.play(Create(caxes), run_time = 1)
        self.wait(2)
        
        # Creating a cosine wave animation 

        axes_left = caxes[0]
        cosine_plot = axes_left.plot(lambda t : np.cos(t), x_range=[-5,5], color = GREEN_C)
        self.play(Create(cosine_plot), run_time = 2)
        self.wait(1)

        # Group everything together and move to left half
        left_group = VGroup(caxes, cosine_plot)
        self.play(left_group.animate.scale(0.5).to_edge(LEFT).shift(DOWN*0.5))
        self.wait(1)

        # Create right axes aligned with left
        rgroup, xlab2, ylab2 = ct_axes(y_range=[-1.2, 1.5, 0.5], x_label="t", y_label="x(-t)")
        rgroup.scale(0.5)
        rgroup.next_to(left_group, RIGHT, buff=1.0)
        axes_right = rgroup[0]
        self.play(Create(rgroup), run_time = 1)
        self.wait(1)

        # Animate the flip: copy wave, flip it horizontally, move to right
        cosine_copy = cosine_plot.copy()
        self.add(cosine_copy)

        # Flip and move to right axes
        self.play(
            cosine_copy.animate.scale([-1, 1, 0]).move_to(axes_right.get_center()),
            run_time=2
        )
        self.wait(1)

class Scene2(Scene):
    def construct(self):
        title2 = Text("Odd Signal", color = BLUE_C)
        self.play(Write(title2), run_time = 2)
        self.play(title2.animate.to_edge(UP))
        self.wait(1)
        
        odd_eq  = MathTex(r"x(t)=-x(-t)", color = GOLD)
        odd_eq.next_to(title2, DOWN, buff = 0.1)
        self.play(Write(odd_eq), run_time = 2)
        self.wait(1)

        caxes, x_lab, y_lab = ct_axes(y_range=[-1.5, 1.5, 0.5])
        caxes.next_to(odd_eq, DOWN, buff=0.3)
        self.play(Create(caxes), run_time=1)
        self.wait(2)

        axes_left = caxes[0]
        sine_plot = axes_left.plot(lambda t: np.sin(t), x_range=[-5, 5], color=RED_C)
        self.play(Create(sine_plot), run_time=2)
        self.wait(1)

        left_group = VGroup(caxes, sine_plot)
        self.play(left_group.animate.scale(0.5).to_edge(LEFT).shift(DOWN*0.5))
        self.wait(1)

        rgroup, xlab2, ylab2 = ct_axes(y_range=[-1.5, 1.5, 0.5], x_label="t", y_label="-x(t)")
        rgroup.scale(0.5)
        rgroup.next_to(left_group, RIGHT, buff=1.0)
        axes_right = rgroup[0]
        self.play(Create(rgroup), run_time=1)
        self.wait(1)

        sine_copy = sine_plot.copy()
        self.add(sine_copy)

        self.play(
            sine_copy.animate.rotate(PI, axis=UP).move_to(axes_right.get_center()),
            run_time=2
        )
        self.wait(1)