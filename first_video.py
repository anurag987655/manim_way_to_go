## Videos objective : 
# to give viewer a strong idea about what the signal is and develop mathematical understanding to define a simple signal

from manim import * 

class Video1(Scene):
    def construct(self):
        # 1. Use NumberPlane with better spacing for arrows
        axes = NumberPlane(
            x_range=[0, 5.8, 1], # Increased range from 5.1 to 6
            y_range=[-2.2, 2.8, 1], # Increased range from 2.1 to 3
            x_length=10, 
            y_length=6,
            background_line_style={
                "stroke_color": WHITE,
                "stroke_width": 2,
                "stroke_opacity": 0.2
            },
            axis_config={
                "stroke_color": GREY,
                "include_tip": True,
                "tip_width": 0.25,
                "tip_height": 0.25,
            }
        ).add_coordinates()

        # 2. Text with appropriate wait time
        text1 = Text("What really is a signal?",color=BLUE_C)
        self.play(Write(text1))
        self.wait(2) # Give viewer time to read
        self.play(FadeOut(text1))
        self.wait(1)

        # 3. Create the axes (this will animate the grid too)
        self.play(Create(axes),run_time=2)
        
        # 4. Animate the dot
        dot = Dot(color=YELLOW).scale(1.4)
        dot.move_to(axes.c2p(0, 0))
        
        self.play(FadeIn(dot))
        self.wait(0.5)
        
        # Move the dot along the axis
        self.play(dot.animate.move_to(axes.c2p(4, 2)), run_time=4)
        self.wait(2)
