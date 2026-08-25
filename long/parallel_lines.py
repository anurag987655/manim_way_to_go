from manim import *
import numpy as np

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


class CurvedLines(ThreeDScene):
    def construct(self):

        sphere = Sphere(radius = 2)
        self.set_camera_orientation(phi = 70 * DEGREES , theta= 0 * DEGREES)

        self.play(Create(sphere), run_time = 2)
        self.wait(1)

        ## Creating point and label

        theta_a = -20 * DEGREES
        theta_b = 20 * DEGREES

        point_a = Dot3D(point= np.array([2 * np.cos(theta_a), 2 * np.sin(theta_a), 0]))
        point_b = Dot3D(point = np.array([2 * np.cos(theta_b), 2* np.sin(theta_b), 0]))

        self.play(Create(point_a))
        self.play(Create(point_b))


        shift = 0.3
        label_a = MathTex("A")
        label_a.move_to(point_a.get_center() + np.array([0.1 , -shift, 0]))

        label_b = MathTex("B")
        label_b.next_to(point_b.get_center() + np.array([0.1 , shift, 0]))

        self.add_fixed_orientation_mobjects(label_a, label_b)

        self.play(Write(label_a), Write(label_b))

        ## Creating parametric curve connecting two points A and B 

        line_ab = ParametricFunction(lambda theta:np.array([2 * np.cos(theta), 2 * np.sin(theta), 0]), t_range= [-20 * DEGREES, 20 * DEGREES])

        self.play(Create(line_ab))
        self.wait(1)

        curve_a = ParametricFunction(lambda phi : np.array([2 * np.sin(phi) * np.cos(theta_a), 2 * np.sin(phi) * np.sin(theta_a), 2 * np.cos(phi)]), t_range=[0 , 90 * DEGREES ])

        curve_b = ParametricFunction(lambda phi : np.array([2 * np.sin(phi) * np.cos(theta_b), 2 * np.sin(phi) * np.sin(theta_b), 2 * np.cos(phi)]), t_range=[0 , 90 * DEGREES ])

        self.play(Create(curve_a))
        self.play(Create(curve_b))

        # creating a right angle label 

        size = 0.2 
        P_a = point_a.get_center()

        u_a = np.array([-np.sin(theta_a), np.cos(theta_a),0])
        v = np.array([0,0,1])

        right_angle_a = VMobject()
        right_angle_a.set_points_as_corners([P_a + u_a * size, P_a + u_a * size + v * size , P_a + v * size])

        self.play(Create(right_angle_a))

        p_b = point_b.get_center()

        u_b = np.array([-np.sin(theta_b), np.cos(theta_b), 0])

        right_angle_b = VMobject()
        right_angle_b.set_points_as_corners([p_b - u_b * size, p_b - u_b * size + v * size, p_b + v * size])

        self.play(Create(right_angle_b))