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
        phi_half = phi_val / 2
        phi_label_radius = 0.5
        phi_label_pos = np.array([
            phi_label_radius * np.sin(phi_half) * np.cos(theta_b),
            phi_label_radius * np.sin(phi_half) * np.sin(theta_b),
            phi_label_radius * np.cos(phi_half)
        ])
        phi_arc_label.move_to(phi_label_pos)
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

        # ========== FINAL SCENE: WHY LINES MEET ==========

        # Fade out proof elements
        self.play(
            FadeOut(card_group, rect_highlight, proof_title,
                    z_axis, center_dot, origin_label,
                    P_dot, P_label, line_OP, R_label,
                    Cz_dot, line_r, r_label, line_oz,
                    phi_arc_label, lat_circle),
            run_time=1.5
        )

        # Move camera to optimal 3D zoomed-in perspective (Title removed per user request)
        self.move_camera(phi=68 * DEGREES, theta=-45 * DEGREES, zoom=1.5, run_time=1.5)
        self.play(sphere.animate.set_style(fill_opacity=0.18, stroke_opacity=0.5, stroke_color=BLUE_B), run_time=1)

        # Sphere radius & Longitude angles for A and B (positioned to show curved paths clearly from camera angle -45°)
        R_sphere = 2
        theta_a = -15 * DEGREES
        theta_b = 55 * DEGREES
        delta_theta = theta_b - theta_a

        # 1. Equator line (cyan baseline)
        equator = ParametricFunction(
            lambda t: np.array([R_sphere * np.cos(t), R_sphere * np.sin(t), 0]),
            t_range=[0, TAU],
            color=TEAL_C,
            stroke_width=3.5
        )
        self.play(Create(equator), run_time=1.5)

        # Starting points A and B on equator
        pos_A = np.array([R_sphere * np.cos(theta_a), R_sphere * np.sin(theta_a), 0])
        pos_B = np.array([R_sphere * np.cos(theta_b), R_sphere * np.sin(theta_b), 0])

        point_a = Dot3D(point=pos_A, color=ORANGE, radius=0.11)
        point_b = Dot3D(point=pos_B, color=TEAL_A, radius=0.11)

        label_a = MathTex("A", color=ORANGE).scale(0.85)
        label_b = MathTex("B", color=TEAL_A).scale(0.85)
        label_a.next_to(point_a, DOWN * 0.5 + LEFT * 0.3)
        label_b.next_to(point_b, DOWN * 0.5 + RIGHT * 0.3)
        self.add_fixed_orientation_mobjects(label_a, label_b)

        self.play(Create(point_a), Create(point_b), Write(label_a), Write(label_b))

        # 2. Showy Glowing Perpendicular lines (Meridians) starting at A and B going up to North Pole
        glow_a = ParametricFunction(
            lambda phi: np.array([
                R_sphere * np.sin(phi) * np.cos(theta_a),
                R_sphere * np.sin(phi) * np.sin(theta_a),
                R_sphere * np.cos(phi)
            ]),
            t_range=[0.001 * DEGREES, 90 * DEGREES],
            color=ORANGE,
            stroke_width=14,
            stroke_opacity=0.35
        )
        perpendicular_a = ParametricFunction(
            lambda phi: np.array([
                R_sphere * np.sin(phi) * np.cos(theta_a),
                R_sphere * np.sin(phi) * np.sin(theta_a),
                R_sphere * np.cos(phi)
            ]),
            t_range=[0.001 * DEGREES, 90 * DEGREES],
            color=ORANGE,
            stroke_width=6.5
        )
        line_a_group = VGroup(glow_a, perpendicular_a)

        glow_b = ParametricFunction(
            lambda phi: np.array([
                R_sphere * np.sin(phi) * np.cos(theta_b),
                R_sphere * np.sin(phi) * np.sin(theta_b),
                R_sphere * np.cos(phi)
            ]),
            t_range=[0.001 * DEGREES, 90 * DEGREES],
            color=TEAL_A,
            stroke_width=14,
            stroke_opacity=0.35
        )
        perpendicular_b = ParametricFunction(
            lambda phi: np.array([
                R_sphere * np.sin(phi) * np.cos(theta_b),
                R_sphere * np.sin(phi) * np.sin(theta_b),
                R_sphere * np.cos(phi)
            ]),
            t_range=[0.001 * DEGREES, 90 * DEGREES],
            color=TEAL_A,
            stroke_width=6.5
        )
        line_b_group = VGroup(glow_b, perpendicular_b)

        # 3. Showy Filled 3D Right Angle boxes at A and B (90° perpendicular markers)
        sq_size = 0.35
        u_A = np.array([-np.sin(theta_a), np.cos(theta_a), 0])
        u_B = np.array([-np.sin(theta_b), np.cos(theta_b), 0])
        v_up = np.array([0, 0, 1])

        right_angle_A = Polygon(
            pos_A,
            pos_A + v_up * sq_size,
            pos_A + v_up * sq_size + u_A * sq_size,
            pos_A + u_A * sq_size,
            color=YELLOW,
            fill_color=YELLOW,
            fill_opacity=0.45,
            stroke_width=3.5
        )

        right_angle_B = Polygon(
            pos_B,
            pos_B + v_up * sq_size,
            pos_B + v_up * sq_size - u_B * sq_size,
            pos_B - u_B * sq_size,
            color=YELLOW,
            fill_color=YELLOW,
            fill_opacity=0.45,
            stroke_width=3.5
        )

        perp_subtitle = MathTex(
            r"\text{Perpendicular Lines } L_A \text{ and } L_B \text{ leave Equator at } 90^\circ",
            color=GOLD
        ).to_edge(DOWN).scale(0.75)
        self.add_fixed_in_frame_mobjects(perp_subtitle)

        self.play(
            Create(line_a_group),
            Create(line_b_group),
            Create(right_angle_A),
            Create(right_angle_B),
            Write(perp_subtitle),
            run_time=2.5
        )
        self.wait(1.5)
        self.play(FadeOut(perp_subtitle))

        # 4. Sliding elements: phi tracker from 90° (Equator) up to 0° (North Pole)
        phi_tracker = ValueTracker(90 * DEGREES)

        # Dynamic parallel circle (pink ring)
        lat_circle = always_redraw(lambda: ParametricFunction(
            lambda t: np.array([
                R_sphere * np.sin(phi_tracker.get_value()) * np.cos(t),
                R_sphere * np.sin(phi_tracker.get_value()) * np.sin(t),
                R_sphere * np.cos(phi_tracker.get_value())
            ]),
            t_range=[0, TAU],
            color=PINK,
            stroke_width=2,
            stroke_opacity=0.75
        ))

        # Dynamic connector arc dab (bright yellow arc between perpendicular lines)
        connector_dab = always_redraw(lambda: ParametricFunction(
            lambda t: np.array([
                R_sphere * np.sin(phi_tracker.get_value()) * np.cos(t),
                R_sphere * np.sin(phi_tracker.get_value()) * np.sin(t),
                R_sphere * np.cos(phi_tracker.get_value())
            ]),
            t_range=[theta_a, theta_b],
            color=YELLOW,
            stroke_width=5.5
        ))

        # Dynamic dots on the perpendicular lines at current height
        dot_A_dyn = always_redraw(lambda: Dot3D(
            point=np.array([
                R_sphere * np.sin(phi_tracker.get_value()) * np.cos(theta_a),
                R_sphere * np.sin(phi_tracker.get_value()) * np.sin(theta_a),
                R_sphere * np.cos(phi_tracker.get_value())
            ]),
            color=ORANGE,
            radius=0.09
        ))

        dot_B_dyn = always_redraw(lambda: Dot3D(
            point=np.array([
                R_sphere * np.sin(phi_tracker.get_value()) * np.cos(theta_b),
                R_sphere * np.sin(phi_tracker.get_value()) * np.sin(theta_b),
                R_sphere * np.cos(phi_tracker.get_value())
            ]),
            color=TEAL_A,
            radius=0.09
        ))

        # Dynamic radius line r (from Z-axis center Cz to dot_A_dyn)
        line_r = always_redraw(lambda: Line3D(
            start=np.array([0, 0, R_sphere * np.cos(phi_tracker.get_value())]),
            end=np.array([
                R_sphere * np.sin(phi_tracker.get_value()) * np.cos(theta_a),
                R_sphere * np.sin(phi_tracker.get_value()) * np.sin(theta_a),
                R_sphere * np.cos(phi_tracker.get_value())
            ]),
            color=RED,
            thickness=0.035
        ))

        # Fixed orientation camera-facing dynamic label for dab (placed ABOVE/OUTSIDE the yellow arc)
        label_dab = MathTex(f"d_{{AB}} = {2.0 * np.sin(90*DEGREES) * delta_theta:.2f}", color=YELLOW).scale(0.7)
        self.add_fixed_orientation_mobjects(label_dab)

        def update_label_dab(m):
            p = phi_tracker.get_value()
            r_val = R_sphere * np.sin(p)
            dab_val = r_val * delta_theta
            mid_theta = (theta_a + theta_b) / 2
            pos = np.array([
                (R_sphere + 0.45) * np.sin(p) * np.cos(mid_theta),
                (R_sphere + 0.45) * np.sin(p) * np.sin(mid_theta),
                R_sphere * np.cos(p) + 0.35
            ])
            m.become(MathTex(f"d_{{AB}} = {dab_val:.2f}", color=YELLOW).scale(0.7))
            m.move_to(pos)

        label_dab.add_updater(update_label_dab)

        # Fixed orientation camera-facing dynamic label for r (placed BELOW/INSIDE the radius line r)
        label_r = MathTex(f"r = {2.0 * np.sin(90*DEGREES):.2f}", color=RED).scale(0.65)
        self.add_fixed_orientation_mobjects(label_r)

        def update_label_r(m):
            p = phi_tracker.get_value()
            r_val = R_sphere * np.sin(p)
            cz = np.array([0, 0, R_sphere * np.cos(p)])
            pt_a = np.array([
                R_sphere * np.sin(p) * np.cos(theta_a),
                R_sphere * np.sin(p) * np.sin(theta_a),
                R_sphere * np.cos(p)
            ])
            mid_pos = (cz + pt_a) * 0.5 + np.array([-0.25, -0.2, -0.35])
            m.become(MathTex(f"r = {r_val:.2f}", color=RED).scale(0.65))
            m.move_to(mid_pos)

        label_r.add_updater(update_label_r)

        # Create sliding marker elements
        self.play(
            Create(lat_circle),
            Create(connector_dab),
            Create(dot_A_dyn),
            Create(dot_B_dyn),
            Create(line_r),
            Write(label_dab),
            Write(label_r),
            run_time=1.5
        )
        self.wait(0.5)

        # 5. SLIDE UP ANIMATION: dab and r slide UP as phi decreases to 1°
        self.play(
            phi_tracker.animate.set_value(1.0 * DEGREES),
            run_time=8,
            rate_func=smooth
        )
        self.wait(0.5)

        # Remove updaters before concluding
        label_dab.clear_updaters()
        label_r.clear_updaters()

        # 6. AT THE POLE: dab = 0 and r = 0 -> Lines Meet!
        north_pole = Dot3D(point=np.array([0, 0, R_sphere]), color=GOLD, radius=0.15)
        
        pole_text = MathTex(
            r"d_{AB} = 0 \implies \text{Perpendicular Lines Meet at the Pole!}",
            color=GOLD
        ).to_edge(DOWN).scale(0.75)
        self.add_fixed_in_frame_mobjects(pole_text)

        self.play(Create(north_pole), Write(pole_text), run_time=1.5)
        self.wait(3)

        # Smooth fade out of everything
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=2)
        self.wait(1)