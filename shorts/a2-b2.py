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
        label_a.next_to(square_a, UP, buff=0.1)

        self.play(Create(square_a),Write(label_a))
        self.wait(1)
