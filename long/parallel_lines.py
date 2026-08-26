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

        # creating a right angle label a

        size = 0.2 
        P_a = point_a.get_center()

        u_a = np.array([-np.sin(theta_a), np.cos(theta_a),0])
        v = np.array([0,0,1])

        right_angle_a = VMobject()
        right_angle_a.set_points_as_corners([P_a + u_a * size, P_a + u_a * size + v * size , P_a + v * size])

        self.play(Create(right_angle_a))

        ## Creating a curved b

        self.play(Create(curve_b))

        ## Creating a rt angle at B

        p_b = point_b.get_center()

        u_b = np.array([-np.sin(theta_b), np.cos(theta_b), 0])

        right_angle_b = VMobject()
        right_angle_b.set_points_as_corners([p_b - u_b * size, p_b - u_b * size + v * size, p_b + v * size])
        self.play(Create(right_angle_b))
        self.wait(1)

        # --- PROOF SECTION: R = r sin(phi) ---

        # 1. Fade out everything apart from the sphere
        self.play(
            FadeOut(point_a, point_b, label_a, label_b, line_ab, curve_a, curve_b, right_angle_a, right_angle_b),
            run_time=1.5
        )
        self.wait(0.5)

        # 2. Camera orientation so the 3D triangle is facing camera face-on (perpendicular to longitude theta_b=20 deg)
        self.move_camera(phi=75 * DEGREES, theta=-70 * DEGREES, frame_center=ORIGIN, run_time=2)
        self.play(
            sphere.animate.set_style(fill_opacity=0.15, stroke_opacity=0.3, stroke_color=BLUE_B),
            run_time=1.5
        )
        self.wait(0.5)

        # Fixed title on screen
        proof_title = MathTex(r"\text{Proof: Parallel Circle Radius } r = R \sin\phi", color=YELLOW)
        proof_title.to_corner(UL).scale(0.8)
        self.add_fixed_in_frame_mobjects(proof_title)
        self.play(Write(proof_title))

        # Central vertical Z-axis
        z_axis = Line3D(start=np.array([0, 0, -2.5]), end=np.array([0, 0, 2.5]), color=WHITE)
        center_dot = Dot3D(point=ORIGIN, color=WHITE, radius=0.07)
        origin_label = MathTex("O", color=WHITE)
        origin_label.next_to(center_dot, LEFT * 0.5 + DOWN * 0.5)
        self.add_fixed_orientation_mobjects(origin_label)

        self.play(Create(z_axis), Create(center_dot), Write(origin_label))

        # Choose initial colatitude phi_val (50 degrees) and sphere radius R_sphere
        phi_val = 50 * DEGREES
        R_sphere = 2  # Radius of sphere (R)

        # Sliding pink circle: starts at colatitude phi_val, slides down to equator (O, phi=90 deg) with growing circumference, then back
        phi_tracker = ValueTracker(phi_val)

        lat_circle = always_redraw(lambda: ParametricFunction(
            lambda t: np.array([
                R_sphere * np.sin(phi_tracker.get_value()) * np.cos(t),
                R_sphere * np.sin(phi_tracker.get_value()) * np.sin(t),
                R_sphere * np.cos(phi_tracker.get_value())
            ]),
            t_range=[0, TAU],
            color=PINK
        ))

        self.play(Create(lat_circle), run_time=1.5)
        self.wait(0.5)

        # Slide down to equator (center O) - circumference grows as it travels down to O
        self.play(phi_tracker.animate.set_value(90 * DEGREES), run_time=2.5, rate_func=smooth)
        self.wait(0.5)

        # Slide back up to initial position (phi_val)
        self.play(phi_tracker.animate.set_value(phi_val), run_time=2.5, rate_func=smooth)
        self.wait(1)

        # Values at phi_val
        r_circle = R_sphere * np.sin(phi_val)  # Radius of parallel circle (r)
        z_val = R_sphere * np.cos(phi_val)

        # Point P on sphere surface (at longitude theta_b = 20 deg)
        P_coord = np.array([r_circle * np.cos(theta_b), r_circle * np.sin(theta_b), z_val])
        P_dot = Dot3D(point=P_coord, color=ORANGE, radius=0.09)
        P_label = MathTex("P", color=ORANGE)
        P_label.next_to(P_dot, RIGHT * 0.4 + UP * 0.4)
        self.add_fixed_orientation_mobjects(P_label)

        # Axis point Cz at height z_val
        Cz_coord = np.array([0, 0, z_val])
        Cz_dot = Dot3D(point=Cz_coord, color=TEAL, radius=0.07)

        # Sphere radius line OP (hypotenuse R)
        line_OP = Line3D(start=ORIGIN, end=P_coord, color=YELLOW)
        R_label = MathTex("R", color=YELLOW).move_to((ORIGIN + P_coord)/2 + DOWN * 0.8 + RIGHT * 0.8)
        self.add_fixed_orientation_mobjects(R_label)

        # Parallel circle radius line CzP (opposite side r)
        line_r = Line3D(start=Cz_coord, end=P_coord, color=RED)
        r_label = MathTex("r", color=RED).move_to((Cz_coord + P_coord)/2 + UP * 0.9)
        self.add_fixed_orientation_mobjects(r_label)

        # Vertical segment OCz (adjacent side)
        line_oz = Line3D(start=ORIGIN, end=Cz_coord, color=BLUE_A)

        self.play(
            Create(P_dot), Write(P_label),
            Create(line_OP), Write(R_label),
            Create(Cz_dot), Create(line_r), Write(r_label),
            Create(line_oz)
        )
        self.wait(1)

        # Angle phi label at Origin between Z-axis and OP
        phi_arc_label = MathTex(r"\phi", color=GREEN_B)
        phi_arc_label.move_to(ORIGIN + UP * 1.2 + RIGHT * 0.05)
        self.add_fixed_orientation_mobjects(phi_arc_label)
        self.play(Write(phi_arc_label))

        # Derivation card in fixed frame
        step1 = MathTex(r"\phi = \text{Colatitude (angle from North Pole)}", color=WHITE)
        step2 = MathTex(r"\sin\phi = \frac{\text{Opposite}}{\text{Hypotenuse}} = \frac{r}{R}", color=YELLOW)
        step3 = MathTex(r"r = R \sin\phi", color=GOLD)
        step4 = MathTex(r"\text{(If } \theta \text{ is latitude from Equator: } r = R \cos\theta\text{)}", color=GRAY)

        derivation_box = VGroup(step1, step2, step3, step4).arrange(DOWN, aligned_edge=LEFT, buff=0.2).scale(0.65).to_corner(UR)

        bg_card = Rectangle(
            width=derivation_box.width + 0.3,
            height=derivation_box.height + 0.3,
            fill_color=BLACK,
            fill_opacity=0.75,
            stroke_color=GOLD
        ).move_to(derivation_box)

        card_group = VGroup(bg_card, derivation_box)
        self.add_fixed_in_frame_mobjects(card_group)
        self.play(FadeIn(card_group, shift=LEFT))
        self.wait(1.5)

        # Highlight ONLY the essential formula r = R sin(phi)
        rect_highlight = SurroundingRectangle(step3, color=YELLOW, buff=0.08, stroke_width=2)
        self.add_fixed_in_frame_mobjects(rect_highlight)
        self.play(Create(rect_highlight))
        self.wait(3)