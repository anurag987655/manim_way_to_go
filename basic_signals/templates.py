from manim import *

class SignalRenderer:
    def __init__(self, scene):
        self.scene = scene

    # =========================
    # 1. BUILD SCENE (NO GRAPH)
    # =========================
    def setup_scene(self, signal):

        # -----------------
        # TITLE
        # -----------------
        title = Text(signal["name"], color=BLUE_C).scale(0.8)
        title.to_edge(UP)

        # -----------------
        # POSITIONS
        # -----------------
        LEFT_POS = LEFT * 4 + UP * 2
        RIGHT_POS = RIGHT * 4 + UP * 2
        GRAPH_Y = DOWN * 1.8

        # -----------------
        # LABELS
        # -----------------
        cont = Text(
            "Continuous Time",
            color=signal["ct_color"]
        ).scale(0.6).move_to(LEFT_POS)

        disc = Text(
            "Discrete Time",
            color=signal["dt_color"]
        ).scale(0.6).move_to(RIGHT_POS)

        cont_f = MathTex(signal["ct_formula"], color=signal["ct_color"]).scale(0.6)
        disc_f = MathTex(signal["dt_formula"], color=signal["dt_color"]).scale(0.6)

        cont_f.next_to(cont, DOWN)
        disc_f.next_to(disc, DOWN)

        # -----------------
        # AXES
        # -----------------
        ct_axes = Axes(
            x_range=signal["x_range"],
            y_range=signal["ct_y_range"],
            axis_config={"color": GREY_B},
            x_axis_config={"include_numbers": True},
            y_axis_config={"include_numbers": True},
        ).scale(0.45)

        dt_axes = Axes(
            x_range=signal["x_range"],
            y_range=signal["dt_y_range"],
            axis_config={"color": GREY_B},
            x_axis_config={"include_numbers": True},
            y_axis_config={"include_numbers": True},
        ).scale(0.45)

        ct_axes.move_to(LEFT * 4 + GRAPH_Y)
        dt_axes.move_to(RIGHT * 4 + GRAPH_Y)

        # -----------------
        # AXIS LABELS (IMPORTANT FIX)
        # -----------------
        ct_xlab = MathTex(signal["ct_xlabel"]).scale(0.5).next_to(ct_axes.x_axis, RIGHT, buff=0.1)
        ct_ylab = MathTex(signal["ct_ylabel"]).scale(0.5).next_to(ct_axes.y_axis, UP, buff=0.1)

        dt_xlab = MathTex(signal["dt_xlabel"]).scale(0.5).next_to(dt_axes.x_axis, RIGHT, buff=0.1)
        dt_ylab = MathTex(signal["dt_ylabel"]).scale(0.5).next_to(dt_axes.y_axis, UP, buff=0.1)

        # -----------------
        # RETURN ALL OBJECTS
        # -----------------
        return {
            "title": title,
            "cont": cont,
            "disc": disc,
            "cont_f": cont_f,
            "disc_f": disc_f,
            "ct_axes": ct_axes,
            "dt_axes": dt_axes,
            "ct_xlab": ct_xlab,
            "ct_ylab": ct_ylab,
            "dt_xlab": dt_xlab,
            "dt_ylab": dt_ylab,
            "graph_y": GRAPH_Y
        }

    # =========================
    # 2. ANIMATE SCENE
    # =========================
    def animate_scene(self, objs):

        self.scene.play(Write(objs["title"]))

        self.scene.play(
            FadeIn(objs["cont"]),
            FadeIn(objs["disc"])
        )

        self.scene.play(
            Write(objs["cont_f"]),
            Write(objs["disc_f"])
        )

        self.scene.play(
            Create(objs["ct_axes"]),
            Create(objs["dt_axes"])
        )

        self.scene.play(
            FadeIn(objs["ct_xlab"]),
            FadeIn(objs["ct_ylab"]),
            FadeIn(objs["dt_xlab"]),
            FadeIn(objs["dt_ylab"])
        )