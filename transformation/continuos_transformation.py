# continuos_transformation.py
from manim import *
from base_signal import *

class Shift(Scene):
    def construct(self):
        axes = make_axes()
        labels = add_axis_labels(axes, "t", "x(t)")
        signal = build_custom_signal(axes)

        formula = create_formula_label("x(t)")
        next_label_anchor = formula

        self.play(Create(axes))
        self.play(Create(labels))
        self.play(Create(signal), run_time=3)
        self.play(Write(formula))
        self.wait(0.5)

        sample_points = [(-1, 0), (0, 1), (1, 1), (2, 0)]

        # One line replaces the whole loop
        animate_sample_points(
            scene=self,
            axes=axes,
            sample_points=sample_points,
            next_label_anchor=next_label_anchor,
            dot_color=YELLOW,
            label_color=GOLD,
            label_scale=0.7,
            dot_radius=0.08
        )

        self.wait(1)

        ## Creating first scene for defining the input shift: 
        label2= create_formula_label("x(t+2)",UR)
        self.play(Write(label2))

       
        
        tex4=MathTex(r"t=-3, x(-3+2)=x(-1)",color=GOLD).scale(0.7).next_to(label2,DOWN,aligned_edge=RIGHT)
        tex3=MathTex(r"t=-2, x(-2+2)=x(0)",color=GOLD).scale(0.7).next_to(tex4,DOWN,aligned_edge=LEFT)
        tex2=MathTex(r"t=0, x(0+2)=x(2)",color=GOLD).scale(0.7).next_to(tex3,DOWN,aligned_edge=LEFT)
        tex1=MathTex(r"t=-1, x(-1+2)=x(1)",color=GOLD).scale(0.7).next_to(tex2,DOWN,aligned_edge=LEFT)
        

        self.play(Write(tex4))
        self.play(Write(tex3))
        self.play(Write(tex2))
        self.play(Write(tex1))