## The animation's objective to make understand the eulers identity 

from manim import *

# config.pixel_width = 1080
# config.pixel_height = 1920
# config.frame_width = 9
# config.frame_height = 16
# config.frame_rate = 60

# config.background_color = "#0E1117"


class Euler(ThreeDScene):
    def construct(self):
        title = Text("Eulers Identity", color = BLUE_C)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))

        self.wait(0.8)

        formula = MathTex(r"e^{i t} = \cos(t) + i \sin(t)", color= GOLD)
        formula.next_to(title,DOWN, buff = 0.3)
        self.play(Write(formula))

        self.wait(1)
        axes = ThreeDAxes(x_range=[0,3* PI +1,1], y_range=[-2,2,1], z_range=[-2,2,1]).scale(0.7)

        self.set_camera_orientation(phi=70*DEGREES,theta=45*DEGREES, frame_center=[-2, 0, 1])
        self.add_fixed_in_frame_mobjects(title, formula)


        self.play(Create(axes))

        t_label = MathTex("t").scale(0.7).move_to(LEFT*5.3 + DOWN * 2.2 )
        re_label = MathTex("Re").scale(0.7).move_to(RIGHT*4.2 + DOWN*1.5)
        im_label = MathTex("Im").scale(0.7).move_to(RIGHT*1 + UP*1.7)
        self.add_fixed_in_frame_mobjects(t_label, re_label, im_label)
        self.play(Write(t_label), Write(re_label), Write(im_label))

        cos_wave = ParametricFunction(lambda t: axes.c2p(t, np.cos(t), 0), t_range=[0, 3*PI], color=BLUE_C)
        sin_wave = ParametricFunction(lambda t: axes.c2p(t, 0, np.sin(t)), t_range=[0, 3*PI], color=GREEN)

        cos_label = MathTex(r"\cos(t)", color=BLUE_C).scale(0.5)
        cos_label.move_to(axes.c2p(PI, -1.4, 0))
        sin_label = MathTex(r"\sin(t)", color=GREEN).scale(0.5)
        sin_label.move_to(axes.c2p(PI/2, 0, 1.4))

        self.play(Create(cos_wave), run_time=2)
        self.add_fixed_orientation_mobjects(cos_label)
        self.play(Write(cos_label))
        self.wait(1)

        self.play(Create(sin_wave), run_time=2)
        self.add_fixed_orientation_mobjects(sin_label)
        self.play(Write(sin_label))
        self.wait(2)

        tracker = ValueTracker(0)

        dot = always_redraw(
            lambda: Dot3D(
                point=axes.c2p(
                    tracker.get_value(),
                    np.cos(tracker.get_value()),
                    np.sin(tracker.get_value())
                ),
                color=RED,
                radius=0.06
            )
        )

        trail = TracedPath(dot.get_center, stroke_color=YELLOW, stroke_width=5)

        self.add(trail, dot)

        self.move_camera(phi=70*DEGREES, theta=45*DEGREES, zoom=2, frame_center=dot.get_center(), run_time=1)

        cam_tracker = Dot3D(color=RED, radius=0.001).set_opacity(0)
        self.add(cam_tracker)

        def update_cam(m):
            m.move_to(dot.get_center())
            self.camera.frame_center = m.get_center()

        cam_tracker.add_updater(update_cam)

        self.play(
            tracker.animate.set_value(3 * PI),
            run_time=6,
            rate_func=linear
        )

        cam_tracker.clear_updaters()
        self.remove(cam_tracker)

        helix = ParametricFunction(
            lambda t: axes.c2p(t, np.cos(t), np.sin(t)),
            t_range=[0, 3*PI],
            color=YELLOW,
            stroke_width=5
        )
        self.remove(trail)
        self.add(helix)

        helix_label = MathTex(r"e^{it}", color=YELLOW).scale(0.7)
        helix_label.move_to(axes.c2p(PI, 0, 1.7) + UP*0.5 + RIGHT*0.3)
        self.add_fixed_orientation_mobjects(helix_label)

        self.move_camera(phi=70*DEGREES, theta=45*DEGREES, zoom=1, frame_center=[-2, 0, 1], run_time=1)
        self.play(Write(helix_label))
        self.wait(2)