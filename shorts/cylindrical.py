from manim import *

config.frame_rate = 60
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

config.background_color = "#0E1117"


class CylindricalCoordinates(ThreeDScene):
    def construct(self):
        x, y, z = 3, 4, 2
        r_val = np.sqrt(x**2 + y**2)
        theta_val = np.arctan2(y, x)

        # ── 4. Question ──
        question = Tex(
            "How does $(3, 4, 2)$ map to\\\\cylindrical coordinates?",
        )
        question.set_color_by_gradient(BLUE, PURPLE, PINK)
        question.to_edge(UP)
        self.add_fixed_in_frame_mobjects(question)

        self.play(Write(question), run_time=1.5)
        self.wait(1)

        # ── 1. 3D Axes ──
        axes = ThreeDAxes(
            x_range=[-6, 6, 1],
            y_range=[-6, 6, 1],
            z_range=[-3, 4, 1],
            x_length=6,
            y_length=6,
            z_length=5,
        )
        axis_labels = axes.get_axis_labels(
            MathTex("x"), MathTex("y"), MathTex("z")
        )

        O = axes.c2p(0, 0, 0)
        p_pos = axes.c2p(x, y, z)
        xy_pos = axes.c2p(x, y, 0)
        px = axes.c2p(x, 0, 0)
        py = axes.c2p(0, y, 0)

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
        path_x = Line(O, px, color=BLUE, stroke_width=3)
        path_y = Line(px, xy_pos, color=BLUE, stroke_width=3)
        path_z = Line(xy_pos, p_pos, color=BLUE, stroke_width=3)

        label_x = MathTex(f"{x}", color=BLUE).scale(0.6)
        label_x.move_to(axes.c2p(x * 0.5, -0.5, 0))
        self.add_fixed_orientation_mobjects(label_x)

        label_y = MathTex(f"{y}", color=BLUE).scale(0.6)
        label_y.move_to(axes.c2p(x + 0.5, y * 0.5, 0))
        self.add_fixed_orientation_mobjects(label_y)

        label_z = MathTex(f"{z}", color=BLUE).scale(0.6)
        label_z.move_to(axes.c2p(x + 0.5, y, z * 0.5))
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



        # ── 5. Compute r → draw circle ──
        r_formula = MathTex(
            r"r = \sqrt{x^2 + y^2}",
            r"= \sqrt{" + f"{x}^2 + {y}^2" + r"}",
            r"= " + f"{r_val:.0f}",
            color=GOLD,
        ).scale(0.55).set_opacity(0.8)
        r_formula.next_to(question, DOWN, buff=0.3)
        self.add_fixed_in_frame_mobjects(r_formula)
        self.play(Write(r_formula), run_time=1.5)
        self.wait(0.5)

        r_scene = np.linalg.norm(axes.c2p(r_val, 0, 0) - O)
        circle = VGroup()
        n = 60
        for i in range(n):
            a1 = 2 * PI * i / n
            a2 = 2 * PI * (i + 1) / n
            p1 = O + r_scene * np.array([np.cos(a1), np.sin(a1), 0])
            p2 = O + r_scene * np.array([np.cos(a2), np.sin(a2), 0])
            circle.add(Line(p1, p2, color=BLUE, stroke_width=2, stroke_opacity=0.6))

        self.play(Create(circle), run_time=1.5)
        self.wait(0.5)

        r_label_circle = MathTex(f"r = {r_val:.0f}", color=BLUE).scale(0.65)
        r_label_circle.move_to(axes.c2p(r_val * 0.5, -r_val * 0.5 - 0.4, 0))
        self.add_fixed_orientation_mobjects(r_label_circle)
        self.play(Write(r_label_circle))
        self.wait(1)

        # ── 6. Compute θ → arc + sweep ──
        theta_deg = np.degrees(theta_val)
        theta_formula = MathTex(
            r"\theta = \arctan\left(\frac{y}{x}\right)",
            r"= \arctan\left(\frac{" + f"{y}" + r"}{" + f"{x}" + r"}\right)",
            rf"\approx {theta_deg:.1f}^\circ",
            color=GOLD,
        ).scale(0.55).set_opacity(0.8)
        theta_formula.next_to(r_formula, DOWN, buff=0.2)
        self.add_fixed_in_frame_mobjects(theta_formula)
        self.play(Write(theta_formula), run_time=1.5)
        # ── 7. Arc + line sweep to xy-plane point ──

        angle_tracker = ValueTracker(0)

        growing_arc = always_redraw(
            lambda: VGroup(*[
                Line(
                    axes.c2p(1.5 * np.cos(a), 1.5 * np.sin(a), 0),
                    axes.c2p(1.5 * np.cos(a + 0.04), 1.5 * np.sin(a + 0.04), 0),
                    color=GREEN, stroke_width=4,
                )
                for a in np.linspace(0, angle_tracker.get_value(), max(2, int(angle_tracker.get_value() / 0.04)))
            ])
        )

        sweeping_line = always_redraw(
            lambda: Line(
                O,
                axes.c2p(
                    r_val * np.cos(angle_tracker.get_value()),
                    r_val * np.sin(angle_tracker.get_value()),
                    0,
                ),
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
        theta_label.move_to(axes.c2p(
            2.0 * np.cos(mid_angle),
            2.0 * np.sin(mid_angle),
            0,
        ))
        self.add_fixed_orientation_mobjects(theta_label)
        self.play(Write(theta_label))
        self.wait(1)

        # ── 8. Vertical line: z units up from xy-plane to P ──
        vert_line = Line(xy_pos, p_pos, color=PURPLE, stroke_width=4)
        z_label = MathTex(f"z = {z}", color=PURPLE).scale(0.65)
        z_label.next_to(vert_line.get_center(), RIGHT, buff=0.15)
        self.add_fixed_orientation_mobjects(z_label)

        self.play(Create(vert_line), Write(z_label), run_time=1)
        self.wait(0.5)

        # Replace point label with cylindrical coordinates at point position
        cyl_at_point = MathTex(
            f"({r_val:.0f},", r"\theta", f", {z})",
            color=GOLD,
        ).scale(0.7)
        cyl_at_point.move_to(point_label.get_center())
        self.add_fixed_orientation_mobjects(cyl_at_point)
        self.play(
            FadeOut(point_label),
            Write(cyl_at_point),
            run_time=1,
        )
        self.wait(1)


        annotation = MathTex(
            r"(\underbrace{r}_{\text{radius}},"
            r"\underbrace{\theta}_{\text{angle}},"
            r"\underbrace{z}_{\text{height}})",
            color=GOLD,
        ).scale(0.7)
        annotation.next_to(axes, DOWN, buff=0.2)
        self.add_fixed_in_frame_mobjects(annotation)
        self.play(Write(annotation), run_time=1.5)
        self.wait(2)

        # ── 10. Hold with gentle camera motion ──
        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(5)
        self.stop_ambient_camera_rotation()
        self.wait(1)
