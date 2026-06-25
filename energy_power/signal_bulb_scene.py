from manim import *

config.background_color = "#1a1a2e"


class CircuitConfig:
    WIRE_COLOR = "#4a4a6a"
    WIRE_FLASH_COLOR = "#88ddff"
    BORDER_COLOR = "#8888bb"
    FILL_COLOR = "#2a2a4e"
    GLOW_COLOR = "#ffdd44"
    PULSE_COLOR = "#ffee55"
    GLASS_COLOR = "#778899"
    BULB_OFF_COLOR = "#0e0e22"
    BULB_ON_COLOR = "#ffee88"
    FILAMENT_OFF_COLOR = "#556677"
    FILAMENT_ON_COLOR = "#ffee88"
    TEXT_COLOR = "#ccddfa"
    ACCENT_COLOR = "#77bbff"

    SOURCE_X = -4.0
    SWITCH_X = 0.0
    BULB_X = 4.0
    Y = 0.0

    @property
    def SOURCE_POS(self):
        return np.array([self.SOURCE_X, self.Y, 0])

    @property
    def SWITCH_POS(self):
        return np.array([self.SWITCH_X, self.Y, 0])

    @property
    def BULB_POS(self):
        return np.array([self.BULB_X, self.Y, 0])

    @property
    def SOURCE_OUT(self):
        return self.SOURCE_POS + RIGHT * 1.4

    @property
    def SWITCH_IN(self):
        return self.SWITCH_POS + LEFT * 0.35

    @property
    def SWITCH_OUT(self):
        return self.SWITCH_POS + RIGHT * 0.35

    @property
    def BULB_IN(self):
        return self.BULB_POS + LEFT * 0.225


class SignalSource(VGroup):
    def __init__(self, config=CircuitConfig()):
        super().__init__()
        box = Rectangle(width=2.8, height=1.6, color=config.BORDER_COLOR,
                        fill_color=config.FILL_COLOR, fill_opacity=0.9, stroke_width=2.5)
        box.move_to(config.SOURCE_POS)
        label = Text("Signal Source", font_size=22, color=config.TEXT_COLOR)
        label.next_to(box, DOWN, buff=0.25)
        icon = MathTex(r"\sim", font_size=42, color=config.ACCENT_COLOR)
        icon.move_to(box)
        self.add(box, label, icon)
        self.box = box
        self.label = label
        self.icon = icon


class ToggleSwitch(VGroup):
    def __init__(self, config=CircuitConfig()):
        super().__init__()
        self.base = Rectangle(width=0.7, height=0.15, color=config.BORDER_COLOR,
                              fill_color="#3a3a5c", fill_opacity=0.9, stroke_width=2)
        self.base.move_to(config.SWITCH_POS)
        self.pivot = self.base.get_center()
        self.lever = Line(self.pivot, self.pivot + UP * 0.7,
                          color="#ddeeff", stroke_width=4)
        self.pivot_dot = Dot(self.pivot, radius=0.06, color="#aabbdd")
        label = Text("Switch", font_size=22, color=config.TEXT_COLOR)
        label.next_to(self.base, DOWN, buff=0.35)
        self.add(self.base, self.lever, self.pivot_dot, label)
        self.label = label

    def animate_toggle(self):
        return Rotate(
            self.lever, angle=-PI * 3 / 5,
            about_point=self.pivot,
            rate_func=rate_functions.ease_out_back,
        )


class LightBulb(VGroup):
    def __init__(self, config=CircuitConfig()):
        super().__init__()
        self.glass = Circle(radius=0.65, color=config.GLASS_COLOR,
                            fill_color=config.BULB_OFF_COLOR, fill_opacity=0.7, stroke_width=2)
        self.glass.move_to(config.BULB_POS + UP * 0.5)
        self.base_rect = Rectangle(width=0.45, height=0.2, color=config.GLASS_COLOR,
                                   fill_color="#3a3a5c", fill_opacity=0.9, stroke_width=2)
        self.base_rect.move_to(config.BULB_POS + DOWN * 0.1)
        center = self.glass.get_center()
        r = 0.65
        self.filament1 = Line(center + DOWN * r * 0.7, center + UP * r * 0.7,
                              color=config.FILAMENT_OFF_COLOR, stroke_width=2)
        self.filament2 = Line(center + LEFT * r * 0.7, center + RIGHT * r * 0.7,
                              color=config.FILAMENT_OFF_COLOR, stroke_width=2)
        label = Text("Light Bulb", font_size=22, color=config.TEXT_COLOR)
        label.next_to(self.base_rect, DOWN, buff=0.35)
        self.label = label
        self.glow_layers = VGroup()
        self.glow_opacities = [0.20, 0.12, 0.06]
        for radius in [0.9, 1.1, 1.35]:
            g = Circle(radius=radius, color=config.GLOW_COLOR, fill_color=config.GLOW_COLOR,
                       fill_opacity=0, stroke_width=0)
            g.move_to(center)
            self.glow_layers.add(g)
        self.add(self.glass, self.base_rect, self.filament1, self.filament2,
                 self.label, self.glow_layers)


class CircuitWires(VGroup):
    def __init__(self, config=CircuitConfig()):
        super().__init__()
        self.wire1 = Line(config.SOURCE_OUT, config.SWITCH_IN,
                          color=config.WIRE_COLOR, stroke_width=3)
        self.wire2 = Line(config.SWITCH_OUT, config.BULB_IN,
                          color=config.WIRE_COLOR, stroke_width=3)
        self.add(self.wire1, self.wire2)


class SignalPulse(VGroup):
    def __init__(self, config=CircuitConfig()):
        super().__init__()
        self.core = Dot(radius=0.12, color=config.PULSE_COLOR)
        self.halo = Dot(radius=0.30, color=config.PULSE_COLOR, fill_opacity=0.25, stroke_width=0)
        self.add(self.halo, self.core)


def caption(text):
    t = Text(text, font_size=22, color="#ccddfa", weight=BOLD)
    t.to_edge(DOWN, buff=0.3)
    return t


class SignalBulbCircuit(Scene):
    def construct(self):
        config = CircuitConfig()
        source = SignalSource(config)
        switch = ToggleSwitch(config)
        bulb = LightBulb(config)
        wires = CircuitWires(config)
        pulse = SignalPulse(config)

        # Phase 1: Title
        title = Text("Signal Flow in a Circuit", font_size=32,
                     color="#aabbee", weight=BOLD).to_edge(UP, buff=0.4)
        self.play(Write(title), run_time=0.8)
        self.wait(0.6)
        self.play(FadeOut(title, shift=UP * 0.1), run_time=0.3)
        self.wait(0.2)

        # Phase 2: Signal Source
        c = caption("The signal source generates energy")
        self.play(Write(c), run_time=0.3)
        self.play(
            DrawBorderThenFill(source.box), Write(source.label), Write(source.icon),
            lag_ratio=0.25, run_time=1.5
        )
        self.wait(1.2)
        self.play(FadeOut(c, shift=DOWN * 0.05), run_time=0.2)

        # Phase 3: First wire
        self.play(Create(wires.wire1), run_time=0.8)
        self.wait(0.4)

        # Phase 4: Switch
        c2 = caption("A switch controls the flow of signal")
        self.play(Write(c2), run_time=0.3)
        self.play(
            DrawBorderThenFill(switch.base), Create(switch.lever),
            Create(switch.pivot_dot), Write(switch.label),
            lag_ratio=0.25, run_time=1.5
        )
        self.wait(1.0)
        self.play(FadeOut(c2, shift=DOWN * 0.05), run_time=0.2)

        # Phase 5: Second wire
        self.play(Create(wires.wire2), run_time=0.8)
        self.wait(0.4)

        # Phase 6: Light bulb
        c3 = caption("The bulb converts signal into light")
        self.play(Write(c3), run_time=0.3)
        status_off = Text("OFF", font_size=18, color="#556677")
        status_off.next_to(bulb.label, DOWN, buff=0.15)
        self.play(
            DrawBorderThenFill(bulb.glass), DrawBorderThenFill(bulb.base_rect),
            Create(bulb.filament1), Create(bulb.filament2),
            Write(bulb.label), Write(status_off),
            lag_ratio=0.2, run_time=2.0
        )
        self.wait(1.0)
        self.play(FadeOut(c3, shift=DOWN * 0.05), run_time=0.2)

        # Phase 7: Anticipation + switch flip
        c4 = caption("Closing the circuit\u2026")
        self.play(Write(c4), run_time=0.4)
        self.wait(0.8)
        self.play(switch.animate_toggle(), run_time=0.6)
        self.wait(0.8)
        self.play(FadeOut(c4, shift=DOWN * 0.05), run_time=0.2)
        self.wait(0.3)

        # Phase 8: Signal travels through wire 1
        c5 = caption("Signal flows through the wire")
        self.play(Write(c5), run_time=0.3)
        pulse.move_to(wires.wire1.get_start())
        self.add(pulse)
        flash_copy1 = wires.wire1.copy().set_stroke(
            color=config.WIRE_FLASH_COLOR, width=6, opacity=0.9
        )
        self.play(
            MoveAlongPath(pulse, wires.wire1),
            ShowPassingFlash(flash_copy1, time_width=0.4),
            rate_func=linear,
            run_time=0.9,
        )

        # Phase 9: Pulse crosses the switch
        switch_highlight = Dot(radius=0.4, color=config.PULSE_COLOR, fill_opacity=0.3)
        switch_highlight.move_to(config.SWITCH_POS)
        self.play(
            pulse.animate.move_to(wires.wire2.get_start()),
            FadeIn(switch_highlight, scale=0.5),
            run_time=0.3,
        )
        self.play(FadeOut(switch_highlight, scale=2), run_time=0.2)
        self.wait(0.15)

        # Phase 10: Signal travels through wire 2
        flash_copy2 = wires.wire2.copy().set_stroke(
            color=config.WIRE_FLASH_COLOR, width=6, opacity=0.9
        )
        self.play(
            MoveAlongPath(pulse, wires.wire2),
            ShowPassingFlash(flash_copy2, time_width=0.4),
            rate_func=linear,
            run_time=0.9,
        )
        self.wait(0.3)

        # Phase 11: Wires become energized
        self.play(
            wires.wire1.animate.set_color(config.WIRE_FLASH_COLOR),
            wires.wire2.animate.set_color(config.WIRE_FLASH_COLOR),
            run_time=0.6,
        )
        self.remove(pulse)
        self.wait(0.3)
        self.play(FadeOut(c5, shift=DOWN * 0.05), run_time=0.2)

        # Phase 12: Bulb lights up
        c6 = caption("Energy reaches the bulb")
        self.play(Write(c6), run_time=0.3)
        flash = Circle(radius=1.0, color="#ffffff", fill_opacity=0.15, stroke_width=0)
        flash.move_to(bulb.glass.get_center())
        self.play(
            flash.animate.set_fill(opacity=0.3).scale(1.5),
            rate_func=rate_functions.ease_out_sine,
            run_time=0.25,
        )
        self.play(FadeOut(flash), run_time=0.2)
        self.play(
            bulb.glass.animate.set_fill(color=config.BULB_ON_COLOR, opacity=0.85),
            bulb.glass.animate.set_stroke(color=config.GLOW_COLOR),
            bulb.filament1.animate.set_color(config.FILAMENT_ON_COLOR),
            bulb.filament2.animate.set_color(config.FILAMENT_ON_COLOR),
            *[glow.animate.set_fill(opacity=op)
              for glow, op in zip(bulb.glow_layers, bulb.glow_opacities)],
            rate_func=rate_functions.ease_in_out_sine,
            run_time=1.8,
        )
        self.play(
            FadeOut(status_off, shift=UP * 0.1),
            FadeOut(c6, shift=DOWN * 0.05),
            run_time=0.3,
        )
        self.wait(0.5)

        # Phase 13: Summary
        summary = Text("Signal Source  \u2192  Switch  \u2192  Light Bulb",
                       font_size=26, color="#aabbee")
        summary.to_edge(DOWN, buff=0.3)
        self.play(Write(summary), run_time=0.6)
        self.wait(2.5)
