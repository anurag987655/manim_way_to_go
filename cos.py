

from manim import *

config.pixel_width = 1920
config.pixel_height = 1080
config.frame_rate = 60
config.background_color = "#0e0e10"

class Cosine(Scene):
    def construct(self):
        formula = MathTex(r"cos(-t)= cos(t)", color = GOLD)
        self.play(Write(formula), runtime = 2)
        self.play(FadeOut(formula))