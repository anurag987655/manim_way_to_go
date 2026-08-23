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

        self.play(distance_marker.animate.shift(DOWN * 3), run_time = 2)
        self.play(distance_marker.animate.shift(UP * 3), run_time = 2)
        self.wait(1)

        ## constant distance indication

        distance_constant = MathTex("d = \\text{constant}")
        distance_constant.move_to(connector_label)

        self.play(Transform(connector_label,distance_constant), run_time = 1.5)
        self.wait(1)

        ## fading out everything a part from line
        
        self.play(FadeOut(line_ab,label_a,label_b,right_a,right_b,distance_marker))
        self.wait(1)

        ## constructing the parallel chevron

        P = perpendicular_a.get_center() + UP * 0.3

        shift_val = 0.2
        p1_line = Line(P, P + DOWN * shift_val + RIGHT * shift_val)
        p2_line = Line(P, P + DOWN *  shift_val+ LEFT * shift_val)

        parallel_mark_a = VGroup(p1_line, p2_line)
        self.play(Create(parallel_mark_a))


        s = perpendicular_b.get_center() + UP * 0.3 
        p3_line = Line(s, s + DOWN * shift_val + RIGHT * shift_val)
        p4_line = Line(s, s + DOWN * shift_val + LEFT * shift_val) 

        parallel_mark_b = VGroup(p3_line, p4_line)
        self.play(Create(parallel_mark_b))
        self.wait(1)

        ## removing every remaining object from flat world
        self.play(FadeOut(perpendicular_a, perpendicular_b, parallel_mark_a, parallel_mark_b), run_time = 1)

        question = Text("But What if space isn't flat?")
        self.play(Write(question), run_time = 1)
        self.wait(1.5)

        self.play(FadeOut(question), run_time = 1)
