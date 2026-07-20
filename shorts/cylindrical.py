from manim import *

config.background_color = "#0E1117"


class CylindricalCoordinates(ThreeDScene):
    def construct(self):
        x, y, z = 3, 4, 2
        r_val = np.sqrt(x**2 + y**2)
        theta_val = np.arctan2(y, x)
        p_pos = np.array([x, y, z])
        xy_pos = np.array([x, y, 0])

        # ── 1. 3D Axes ──
        axes = ThreeDAxes(
            x_range=[-6, 6, 1],
            y_range=[-6, 6, 1],
            z_range=[-3, 4, 1],
            x_length=9,
            y_length=9,
            z_length=7,
        )
        axis_labels = axes.get_axis_labels(
            MathTex("x"), MathTex("y"), MathTex("z")
        )

        self.set_camera_orientation(phi=65 * DEGREES, theta=-45 * DEGREES)
        self.play(Create(axes), Write(axis_labels))
        self.wait(0.5)

        # ── 2. Point P ──
        point = Dot3D(point=p_pos, color=RED, radius=0.1)
        point_label = MathTex(
            f"P({x}, {y}, {z})", color=RED
        ).scale(0.6)
        point_label.next_to(point, UP + RIGHT, buff=0.1)
        self.add_fixed_orientation_mobjects(point_label)

        self.play(Create(point), Write(point_label))
        self.wait(0.5)

        # ── 3. Cartesian path: 3 along x → 4 parallel to y → 2 parallel to z ──
        path_x = Line(ORIGIN, np.array([x, 0, 0]), color=BLUE, stroke_width=3)
        path_y = Line(np.array([x, 0, 0]), np.array([x, y, 0]), color=BLUE, stroke_width=3)
        path_z = Line(np.array([x, y, 0]), p_pos, color=BLUE, stroke_width=3)

        label_x = MathTex(f"{x}", color=BLUE).scale(0.6)
        label_x.move_to(np.array([x * 0.5, -0.5, 0]))
        self.add_fixed_orientation_mobjects(label_x)

        label_y = MathTex(f"{y}", color=BLUE).scale(0.6)
        label_y.move_to(np.array([x + 0.5, y * 0.5, 0]))
        self.add_fixed_orientation_mobjects(label_y)

        label_z = MathTex(f"{z}", color=BLUE).scale(0.6)
        label_z.move_to(np.array([x + 0.5, y, z * 0.5]))
        self.add_fixed_orientation_mobjects(label_z)

        self.play(Create(path_x), Write(label_x), run_time=0.8)
        self.wait(0.3)
        self.play(Create(path_y), Write(label_y), run_time=0.8)
        self.wait(0.3)
        self.play(Create(path_z), Write(label_z), run_time=0.8)
        self.wait(1.5)

        self.play(
            FadeOut(path_x), FadeOut(path_y), FadeOut(path_z),
            FadeOut(label_x), FadeOut(label_y), FadeOut(label_z),
        )
        self.wait(0.3)

        # ── 4. Question ──
        q_how = Tex("How does ", color=WHITE)
        q_point = Tex(f"({x}, {y}, {z})", color=RED)
        q_map = Tex(" map to cylindrical coordinates?", color=WHITE)
        question = VGroup(q_how, q_point, q_map).arrange(RIGHT, buff=0.05)
        question.to_edge(UP)
        self.add_fixed_in_frame_mobjects(question)

        self.play(Write(question), run_time=1.5)
        self.wait(2)
        self.play(FadeOut(question))
        self.wait(0.3)

        # ── 5. Compute r → draw circle on xy-plane ──
        r_formula = MathTex(
            r"r = \sqrt{x^2 + y^2}",
            r"= \sqrt{" + f"{x}^2 + {y}^2" + r"}",
            r"= " + f"{r_val:.0f}",
            color=GOLD,
        ).set_opacity(0.8)
        r_formula.to_edge(UP)
        self.add_fixed_in_frame_mobjects(r_formula)
        self.play(Write(r_formula), run_time=1.5)
        self.wait(0.5)

        r_scene = np.linalg.norm(axes.c2p(r_val, 0, 0) - axes.c2p(0, 0, 0))
        circle = Circle(
            radius=r_scene,
            color=BLUE,
            stroke_width=2,
            stroke_opacity=0.4,
        ).move_to(axes.c2p(0, 0, 0))

        self.play(Create(circle), run_time=1.5)
        self.wait(0.5)

        r_label_circle = MathTex(f"r = {r_val:.0f}", color=BLUE).scale(0.65)
        r_label_circle.move_to(axes.c2p(r_val * 0.5, -r_val * 0.5 - 0.4, 0))
        self.add_fixed_orientation_mobjects(r_label_circle)
        self.play(Write(r_label_circle))
        self.wait(1)

        # ── 6. Compute θ → arc + line sweep to xy-plane point ──
        theta_deg = np.degrees(theta_val)
        theta_formula = MathTex(
            r"\theta = \arctan\left(\frac{y}{x}\right)",
            r"= \arctan\left(\frac{" + f"{y}" + r"}{" + f"{x}" + r"}\right)",
            rf"\approx {theta_deg:.1f}^\circ",
            color=GOLD,
        ).set_opacity(0.8)
        theta_formula.next_to(r_formula, DOWN, buff=0.3)
        self.add_fixed_in_frame_mobjects(theta_formula)
        self.play(Write(theta_formula), run_time=1.5)
        self.wait(0.5)

        angle_tracker = ValueTracker(0)

        growing_arc = always_redraw(
            lambda: Arc(
                radius=1.5,
                angle=angle_tracker.get_value(),
                color=GREEN,
                stroke_width=4,
            )
        )

        sweeping_line = always_redraw(
            lambda: Line(
                ORIGIN,
                np.array([
                    r_val * np.cos(angle_tracker.get_value()),
                    r_val * np.sin(angle_tracker.get_value()),
                    0,
                ]),
                color=BLUE,
                stroke_width=4,
            )
        )

        self.add(growing_arc, sweeping_line)
        self.play(
            angle_tracker.animate.set_value(theta_val),
            run_time=2.5,
            rate_func=smooth,
        )
        self.wait(0.3)

        mid_angle = theta_val / 2
        theta_label = MathTex(r"\theta", color=GREEN).scale(0.7)
        theta_label.move_to(np.array([
            2.0 * np.cos(mid_angle),
            2.0 * np.sin(mid_angle),
            0,
        ]))
        self.add_fixed_orientation_mobjects(theta_label)
        self.play(Write(theta_label))
        self.wait(1)

        # ── 7. Vertical line: z units up from xy-plane to P ──
        vert_line = Line(xy_pos, p_pos, color=PURPLE, stroke_width=4)
        z_label = MathTex(f"z = {z}", color=PURPLE).scale(0.65)
        z_label.next_to(vert_line.get_center(), RIGHT, buff=0.15)
        self.add_fixed_orientation_mobjects(z_label)

        self.play(Create(vert_line), Write(z_label), run_time=1)
        self.wait(1)

        # ── 8. Reveal cylindrical coordinates ──
        self.play(
            FadeOut(r_formula),
            FadeOut(theta_formula),
            FadeOut(r_label_circle),
        )

        cylindrical_label = MathTex(
            f"({r_val:.0f},", r"\theta", f", {z})",
            color=GOLD,
        ).scale(0.7)
        cylindrical_label.next_to(point_label, DOWN, buff=0.4)
        self.add_fixed_orientation_mobjects(cylindrical_label)
        self.play(Write(cylindrical_label), run_time=1)
        self.wait(0.5)

        annotation = MathTex(
            r"(\underbrace{r}_{\text{radius}},"
            r"\underbrace{\theta}_{\text{angle}},"
            r"\underbrace{z}_{\text{height}})",
            color=GOLD,
        ).scale(0.55)
        annotation.to_edge(DOWN, buff=0.4)
        self.add_fixed_in_frame_mobjects(annotation)
        self.play(Write(annotation), run_time=1.5)
        self.wait(2)

        # ── 9. Hold with gentle camera motion ──
        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(5)
        self.stop_ambient_camera_rotation()
        self.wait(1)
