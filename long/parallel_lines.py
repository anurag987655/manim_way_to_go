from manim import *

class ParallelLines(Scene):
    def construct(self):
        line_ab = Line(LEFT *2, RIGHT*2)

        ## Adding label A and B at respective end points: 

        label_a = MathTex("A")
        label_b = MathTex("B")

        label_a.next_to(line_ab.get_start(), LEFT)
        label_b.next_to(line_ab.get_end(), RIGHT)

        ## Creating the scene AB

        self.play(Create(line_ab))
        self.play(Write(label_a),Write(label_b))
        self.wait(2)

        ## Creating two perpendicular lines at A and B 

        perpendicular_a = Line(line_ab.get_start() + UP *2, line_ab.get_start() + DOWN * 2)
        perpendicular_b = Line(line_ab.get_end() + UP *2, line_ab.get_end() + DOWN * 2) 


        # Creating a right angle labels 

        right_a = RightAngle(perpendicular_a, line_ab, quadrant= (-1,1))
        right_b = RightAngle(perpendicular_b, line_ab, quadrant = (-1,-1))

        # perpendicular Scene

        self.play(Create(perpendicular_a))
        self.play(Create(right_a))
        self.play(Create(perpendicular_b))
        self.play(Create(right_b))

        self.wait(1)

        # Introducing horizental connector

        connector = DashedLine(line_ab.get_start() + UP * 1.5, line_ab.get_end() + UP * 1.5)
        connector_label = MathTex("d_{AB}")
        connector_label.next_to(connector, UP)

        self.play(Create(connector))
        self.play(Write(connector_label))

        distance_marker = VGroup(connector, connector_label)

        self.play(distance_marker.animate.shift(DOWN * 3), runtime = 3)
        self.wait(1)
