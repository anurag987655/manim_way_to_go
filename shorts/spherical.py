from manim import *
import numpy as np

config.frame_rate = 60
config.pixel_width = 1080
config.pixel_height = 1920
config.background_color = "#0E1117"


class SphericalToRectangular(ThreeDScene):
    def construct(self):
        # ── 1. Axes ──
        axes = ThreeDAxes(
            x_range=[-6, 6, 1],
            y_range=[-6, 6, 1],
            z_range=[-4, 6, 1],
            x_length=9,
            y_length=9,
            z_length=7,
        )
        axes_labels = axes.get_axis_labels(
            MathTex("x").scale(0.85),
            MathTex("y").scale(0.85),
            MathTex("z").scale(0.85),
        )

        self.set_camera_orientation(phi=65 * DEGREES, theta=-45 * DEGREES)
        self.play(Create(axes), Write(axes_labels))
        self.wait(0.5)

        # ── 2. Point P with spherical coords ──
        rho, th, ph = 4.5, 50 * DEGREES, 35 * DEGREES
        x = rho * np.sin(ph) * np.cos(th)
        y = rho * np.sin(ph) * np.sin(th)
        z = rho * np.cos(ph)

        p = np.array([x, y, z])
        p_xy = np.array([x, y, 0])

        pt = Dot3D(point=p, color=RED, radius=0.1)
        coord = MathTex("P(", "\\rho", ",", "\\theta", ",", "\\phi", ")")
        coord[1].set_color(YELLOW)
        coord[3].set_color(GREEN)
        coord[5].set_color(BLUE)
        coord.scale(0.75)
        coord.next_to(pt, UR, buff=0.1)
        self.add_fixed_orientation_mobjects(coord)

        self.play(Create(pt), Write(coord))
        self.wait(0.5)

        # ── 4. ρ line ──
        rho_line = Line(ORIGIN, p, color=YELLOW, stroke_width=4)
        rho_label = MathTex("\\rho", color=YELLOW).scale(0.8)
        rho_label.move_to((ORIGIN + p) / 2 + [-0.4, 0.3, 0])
        self.add_fixed_orientation_mobjects(rho_label)

        self.play(Create(rho_line), Write(rho_label))
        self.wait(0.5)

        # ── 5. φ arc (from z-axis to OP) ──
        z_dir = np.array([0, 0, 1])
        p_dir = p / np.linalg.norm(p)
        phi_arc = self._arc(ORIGIN, z_dir, p_dir, 1.5, BLUE)
        mid_phi = self._lerp_dir(z_dir, p_dir, 0.45)
        phi_label = MathTex("\\phi", color=BLUE).scale(0.8)
        phi_label.move_to(ORIGIN + mid_phi * 2.0)
        self.add_fixed_orientation_mobjects(phi_label)

        self.play(Create(phi_arc), Write(phi_label))
        self.wait(0.5)

        # ── 6. Drop to xy-plane (z component) ──
        z_line = DashedLine(p, p_xy, color=BLUE, stroke_width=3)

        self.play(Create(z_line))
        self.wait(0.5)

        # ── 7. P' in xy-plane ──
        pp_dot = Dot3D(point=p_xy, color=GREEN, radius=0.08)
        pp_label = MathTex("P'", color=GREEN).scale(0.8)
        pp_label.next_to(pp_dot, DOWN, buff=0.15)
        self.add_fixed_orientation_mobjects(pp_label)

        self.play(Create(pp_dot), Write(pp_label))
        self.wait(0.5)

        # ── 8. r line (ρ sin φ) ──
        r_line = Line(ORIGIN, p_xy, color=PURPLE, stroke_width=3)

        self.play(Create(r_line))
        self.wait(0.5)

        # ── 8b. Z-axis projection ──
        p_z = np.array([0, 0, z])
        z_axis_line = DashedLine(p, p_z, color=BLUE, stroke_width=3)
        z_axis_label = MathTex("z = \\rho\\cos\\phi", color=BLUE).scale(0.7)
        z_axis_label.move_to(p_z + [-0.5, -0.4, 0])
        self.add_fixed_orientation_mobjects(z_axis_label)

        self.play(Create(z_axis_line), Write(z_axis_label))
        self.wait(0.5)

        # ── 9. θ arc in xy-plane ──
        theta_arc_obj = Arc(
            radius=1.2,
            start_angle=0,
            angle=th,
            color=GREEN,
            stroke_width=3,
        )
        mid_th = th / 2
        theta_label = MathTex("\\theta", color=GREEN).scale(0.8)
        theta_label.move_to(np.array([1.7 * np.cos(mid_th), 1.7 * np.sin(mid_th), 0]))
        self.add_fixed_orientation_mobjects(theta_label)

        self.play(Create(theta_arc_obj), Write(theta_label))
        self.wait(0.5)

        # ── 10. Project to x and y axes ──
        px, py = np.array([x, 0, 0]), np.array([0, y, 0])
        x_line = DashedLine(p_xy, px, color=MAROON, stroke_width=3)
        y_line = DashedLine(p_xy, py, color=MAROON, stroke_width=3)

        x_label = MathTex(
            "x = \\rho\\sin\\phi\\cos\\theta",
            color=MAROON,
        ).scale(0.55)
        x_label.next_to(px, DOWN, buff=0.15)
        self.add_fixed_orientation_mobjects(x_label)

        self.play(Create(x_line), Write(x_label))
        self.wait(0.5)

        y_label = MathTex(
            "y = \\rho\\sin\\phi\\sin\\theta",
            color=MAROON,
        ).scale(0.55)
        y_label.next_to(py, LEFT, buff=0.15)
        self.add_fixed_orientation_mobjects(y_label)

        self.play(Create(y_line), Write(y_label))
        self.wait(0.5)

        # ── 10b. Highlight projected region ──
        region = Polygon(
            ORIGIN, np.array([x, 0, 0]), p_xy, np.array([0, y, 0]),
            color=MAROON, fill_opacity=0.15, stroke_width=0,
        )
        self.play(Create(region))
        self.wait(0.5)

        # ── 11. Summary formula ──
        summary = MathTex(
            "x = \\rho\\sin\\phi\\cos\\theta,\\quad "
            "y = \\rho\\sin\\phi\\sin\\theta,\\quad "
            "z = \\rho\\cos\\phi"
        ).scale(0.6)
        summary.to_edge(DOWN)
        self.add_fixed_in_frame_mobjects(summary)
        self.play(Write(summary))
        self.wait(1)

        # ── 12. Gentle camera rotation ──
        self.begin_ambient_camera_rotation(rate=0.15)
        self.wait(5)
        self.stop_ambient_camera_rotation()
        self.wait(1)

    # ──────────── 3D helpers ────────────

    def _rodrigues(self, v, k, a):
        return (
            v * np.cos(a)
            + np.cross(k, v) * np.sin(a)
            + k * np.dot(k, v) * (1 - np.cos(a))
        )

    def _lerp_dir(self, v1, v2, t):
        n1 = v1 / np.linalg.norm(v1)
        n2 = v2 / np.linalg.norm(v2)
        a = np.arccos(np.clip(np.dot(n1, n2), -1, 1))
        if a < 1e-8:
            return n1
        k = np.cross(n1, n2)
        k /= np.linalg.norm(k)
        return self._rodrigues(n1, k, t * a)

    def _arc(self, center, v1, v2, radius, color, n=40):
        n1 = v1 / np.linalg.norm(v1)
        n2 = v2 / np.linalg.norm(v2)
        a = np.arccos(np.clip(np.dot(n1, n2), -1, 1))
        if a < 1e-8:
            return VGroup()
        k = np.cross(n1, n2)
        k /= np.linalg.norm(k)
        arc = VGroup()
        for i in range(n):
            t1, t2 = i / n, (i + 1) / n
            p1 = center + self._rodrigues(n1, k, t1 * a) * radius
            p2 = center + self._rodrigues(n1, k, t2 * a) * radius
            arc.add(Line(p1, p2, color=color, stroke_width=2))
        return arc
