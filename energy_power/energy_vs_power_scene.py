from manim import *
import numpy as np

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
        self._config = config
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

    def animate_change_label(self, new_text):
        new_label = Text(new_text, font_size=22, color=self._config.TEXT_COLOR)
        new_label.next_to(self.box, DOWN, buff=0.25)
        return Transform(self.label, new_label)

    def animate_deplete(self):
        return AnimationGroup(
            self.icon.animate.set_opacity(0.1),
            self.box.animate.set_fill(opacity=0.3),
            run_time=2.5,
        )

    def animate_revive(self):
        return AnimationGroup(
            self.icon.animate.set_opacity(1.0),
            self.box.animate.set_fill(opacity=0.9),
            run_time=0.5,
        )


class ToggleSwitch(VGroup):
    OFF_ANGLE = 0
    ON_ANGLE = -PI / 2

    def __init__(self, config=CircuitConfig()):
        super().__init__()
        self._config = config
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
        self._is_on = False

    def reset(self):
        if self._is_on:
            self.lever.rotate(-self.ON_ANGLE, about_point=self.pivot)
            self._is_on = False

    def animate_toggle(self):
        angle = self.ON_ANGLE if not self._is_on else -self.ON_ANGLE
        self._is_on = not self._is_on
        return Rotate(
            self.lever, angle=angle,
            about_point=self.pivot,
            rate_func=rate_functions.ease_out_back,
        )


class LightBulb(VGroup):
    def __init__(self, config=CircuitConfig()):
        super().__init__()
        self._config = config
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

    def animate_turn_on(self):
        c = self._config
        return AnimationGroup(
            self.glass.animate.set_fill(color=c.BULB_ON_COLOR, opacity=0.85).set_stroke(color=c.GLOW_COLOR),
            self.filament1.animate.set_color(c.FILAMENT_ON_COLOR),
            self.filament2.animate.set_color(c.FILAMENT_ON_COLOR),
            *[glow.animate.set_fill(opacity=op)
              for glow, op in zip(self.glow_layers, self.glow_opacities)],
            rate_func=rate_functions.ease_in_out_sine,
        )

    def animate_turn_off(self):
        c = self._config
        return AnimationGroup(
            self.glass.animate.set_fill(color=c.BULB_OFF_COLOR, opacity=0.7).set_stroke(color=c.GLASS_COLOR),
            self.filament1.animate.set_color(c.FILAMENT_OFF_COLOR),
            self.filament2.animate.set_color(c.FILAMENT_OFF_COLOR),
            *[glow.animate.set_fill(opacity=0) for glow in self.glow_layers],
            rate_func=rate_functions.ease_in_out_sine,
        )

    def animate_dim(self):
        c = self._config
        dim_opacities = [op * 0.15 for op in self.glow_opacities]
        return AnimationGroup(
            self.glass.animate.set_fill(color="#887744", opacity=0.45).set_stroke(color="#665533"),
            self.filament1.animate.set_color("#887744"),
            self.filament2.animate.set_color("#887744"),
            *[glow.animate.set_fill(opacity=op)
              for glow, op in zip(self.glow_layers, dim_opacities)],
            rate_func=rate_functions.ease_in_out_sine,
        )


class CircuitWires(VGroup):
    def __init__(self, config=CircuitConfig()):
        super().__init__()
        self._config = config
        self.wire1 = Line(config.SOURCE_OUT, config.SWITCH_IN,
                          color=config.WIRE_COLOR, stroke_width=3)
        self.wire2 = Line(config.SWITCH_OUT, config.BULB_IN,
                          color=config.WIRE_COLOR, stroke_width=3)
        self.add(self.wire1, self.wire2)

    def animate_energize(self):
        c = self._config
        return AnimationGroup(
            self.wire1.animate.set_color(c.WIRE_FLASH_COLOR),
            self.wire2.animate.set_color(c.WIRE_FLASH_COLOR),
            run_time=0.6,
        )

    def animate_de_energize(self):
        return AnimationGroup(
            self.wire1.animate.set_color(self._config.WIRE_COLOR),
            self.wire2.animate.set_color(self._config.WIRE_COLOR),
            run_time=0.4,
        )


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


def top_title(text):
    t = Text(text, font_size=30, color="#aabbee", weight=BOLD)
    t.to_edge(UP, buff=0.4)
    return t


class BatteryMeter(VGroup):
    def __init__(self, config=CircuitConfig()):
        super().__init__()
        self._config = config
        self.casing = Rectangle(width=0.3, height=0.65, color=WHITE, stroke_width=2)
        self.cap = Rectangle(width=0.12, height=0.08, color=WHITE, stroke_width=2)
        self.cap.next_to(self.casing, UP, buff=0)
        body_height = 0.61
        self.fill_bar = Rectangle(width=0.26, height=body_height, color=GREEN,
                                  fill_color=GREEN, fill_opacity=0.85, stroke_width=0)
        self.fill_bar.align_to(self.casing, DOWN)
        self.fill_bar.shift(UP * 0.02)
        label = Text("Remaining", font_size=12, color=config.TEXT_COLOR)
        label.next_to(self.casing, DOWN, buff=0.06)
        self.add(self.casing, self.cap, self.fill_bar, label)
        self.full_height = body_height

    def animate_deplete(self):
        return self.fill_bar.animate.set_height(0.01).align_to(self.casing, DOWN).shift(UP * 0.02)


class Clock(VGroup):
    def __init__(self):
        super().__init__()
        self.face = Circle(radius=0.35, color=WHITE, stroke_width=2)
        self.hand = Line(ORIGIN, UP * 0.28, color=YELLOW, stroke_width=2.5)
        self.hand.move_to(self.face.get_center())
        center_dot = Dot(radius=0.03, color=WHITE)
        center_dot.move_to(self.face.get_center())
        label = Text("Time", font_size=12, color="#ccddfa")
        label.next_to(self.face, DOWN, buff=0.06)
        self.add(self.face, self.hand, center_dot, label)

    def animate_tick(self, n_rotations=1):
        return Rotate(
            self.hand, angle=n_rotations * 2 * PI,
            about_point=self.face.get_center(),
            rate_func=linear,
        )


class EnergyVsPower(Scene):
    def construct(self):
        config = CircuitConfig()

        source = SignalSource(config)
        switch = ToggleSwitch(config)
        bulb = LightBulb(config)
        wires = CircuitWires(config)
        pulse = SignalPulse(config)

        self.part_1(source, switch, bulb, wires, pulse, config)
        self.part_2(source, switch, bulb, wires, pulse, config)

    # ------------------------------------------------------------------ 
    # PART 1: Signal 1 — finite energy, bulb dies
    # ------------------------------------------------------------------ 
    def part_1(self, source, switch, bulb, wires, pulse, config):
        title = top_title("Experiment 1")
        self.play(Write(title), run_time=0.6)
        self.wait(0.3)

        self.play(
            DrawBorderThenFill(source.box), Write(source.icon),
            lag_ratio=0.25, run_time=1.0,
        )
        self.play(source.animate_change_label("Signal 1"), run_time=0.3)
        self.wait(0.4)

        self.play(Create(wires.wire1), run_time=0.5)

        self.play(
            DrawBorderThenFill(switch.base), Create(switch.lever),
            Create(switch.pivot_dot), Write(switch.label),
            lag_ratio=0.25, run_time=1.2,
        )

        self.play(Create(wires.wire2), run_time=0.5)

        status_off = Text("OFF", font_size=18, color="#556677")
        status_off.next_to(bulb.label, DOWN, buff=0.15)
        self.play(
            DrawBorderThenFill(bulb.glass), DrawBorderThenFill(bulb.base_rect),
            Create(bulb.filament1), Create(bulb.filament2),
            Write(bulb.label), Write(status_off),
            lag_ratio=0.2, run_time=1.5,
        )
        self.wait(0.5)

        battery = BatteryMeter(config)
        battery.next_to(source.box, UP, buff=0.25).shift(RIGHT * 0.2)
        self.play(FadeIn(battery, scale=0.8), run_time=0.4)

        timer = Clock()
        timer.scale(0.6)
        timer.next_to(battery, RIGHT, buff=0.15).shift(DOWN * 0.05)
        self.play(FadeIn(timer, scale=0.8), run_time=0.3)
        self.wait(0.5)

        self.play(switch.animate_toggle(), run_time=0.6)
        self.wait(0.5)

        pulse.move_to(wires.wire1.get_start())
        self.add(pulse)
        fc1 = wires.wire1.copy().set_stroke(color=config.WIRE_FLASH_COLOR, width=6, opacity=0.9)
        self.play(
            MoveAlongPath(pulse, wires.wire1),
            ShowPassingFlash(fc1, time_width=0.4),
            rate_func=linear, run_time=0.8,
        )
        sh = Dot(radius=0.4, color=config.PULSE_COLOR, fill_opacity=0.3)
        sh.move_to(config.SWITCH_POS)
        self.play(
            pulse.animate.move_to(wires.wire2.get_start()),
            FadeIn(sh, scale=0.5), run_time=0.25,
        )
        self.play(FadeOut(sh, scale=2), run_time=0.15)
        fc2 = wires.wire2.copy().set_stroke(color=config.WIRE_FLASH_COLOR, width=6, opacity=0.9)
        self.play(
            MoveAlongPath(pulse, wires.wire2),
            ShowPassingFlash(fc2, time_width=0.4),
            rate_func=linear, run_time=0.8,
        )
        self.play(
            wires.wire1.animate.set_color(config.WIRE_FLASH_COLOR),
            wires.wire2.animate.set_color(config.WIRE_FLASH_COLOR),
            run_time=0.4,
        )
        self.remove(pulse)
        self.wait(0.2)

        flash_in = Circle(radius=1.0, color="#ffffff", fill_opacity=0.15, stroke_width=0)
        flash_in.move_to(bulb.glass.get_center())
        self.play(
            flash_in.animate.set_fill(opacity=0.3).scale(1.5),
            rate_func=rate_functions.ease_out_sine, run_time=0.2,
        )
        self.play(FadeOut(flash_in), run_time=0.15)
        self.play(bulb.animate_turn_on(), run_time=1.5)
        self.play(
            FadeOut(status_off, shift=UP * 0.1),
            run_time=0.2,
        )
        self.wait(0.8)

        self.play(
            bulb.animate_dim(),
            battery.animate_deplete(),
            source.animate_deplete(),
            timer.animate_tick(2),
            run_time=3.0,
        )
        self.play(bulb.animate_turn_off(), run_time=0.6)
        self.play(
            wires.wire1.animate.set_color(config.WIRE_COLOR),
            wires.wire2.animate.set_color(config.WIRE_COLOR),
            run_time=0.3,
        )
        self.wait(1.0)

        self.play(
            FadeOut(title, shift=UP * 0.05),
            FadeOut(battery),
            FadeOut(timer),
            source.icon.animate.set_opacity(0),
            source.label.animate.set_opacity(0),
            run_time=0.3,
        )

    # ------------------------------------------------------------------ 
    # PART 2: Signal 2 — continuous power, bulb stays on
    # ------------------------------------------------------------------ 
    def part_2(self, source, switch, bulb, wires, pulse, config):
        switch.reset()
        self.play(source.animate_revive(), run_time=0.3)
        self.play(source.animate_change_label("Signal 2"), run_time=0.2)

        status_off = Text("OFF", font_size=18, color="#556677")
        status_off.next_to(bulb.label, DOWN, buff=0.15)
        self.play(FadeIn(status_off, scale=0.8), run_time=0.2)
        self.wait(0.3)

        clock = Clock()
        clock.next_to(source.box, UP, buff=0.25).shift(RIGHT * 0.2)
        self.play(FadeIn(clock, scale=0.8), run_time=0.4)
        self.wait(0.3)

        self.play(switch.animate_toggle(), run_time=0.6)
        self.wait(0.5)

        full_path = VMobject(stroke_width=0)
        full_path.set_points_as_corners([
            config.SOURCE_OUT, config.SWITCH_IN,
            config.SWITCH_OUT, config.BULB_IN,
        ])

        pulse.move_to(full_path.get_start())
        self.add(pulse)
        fc1 = wires.wire1.copy().set_stroke(color=config.WIRE_FLASH_COLOR, width=6, opacity=0.9)
        self.play(
            MoveAlongPath(pulse, wires.wire1),
            ShowPassingFlash(fc1, time_width=0.4),
            rate_func=linear, run_time=0.8,
        )
        sh = Dot(radius=0.4, color=config.PULSE_COLOR, fill_opacity=0.3)
        sh.move_to(config.SWITCH_POS)
        self.play(
            pulse.animate.move_to(wires.wire2.get_start()),
            FadeIn(sh, scale=0.5), run_time=0.25,
        )
        self.play(FadeOut(sh, scale=2), run_time=0.15)
        fc2 = wires.wire2.copy().set_stroke(color=config.WIRE_FLASH_COLOR, width=6, opacity=0.9)
        self.play(
            MoveAlongPath(pulse, wires.wire2),
            ShowPassingFlash(fc2, time_width=0.4),
            rate_func=linear, run_time=0.8,
        )
        self.play(
            wires.wire1.animate.set_color(config.WIRE_FLASH_COLOR),
            wires.wire2.animate.set_color(config.WIRE_FLASH_COLOR),
            run_time=0.4,
        )
        self.remove(pulse)
        self.wait(0.2)

        flash_in = Circle(radius=1.0, color="#ffffff", fill_opacity=0.15, stroke_width=0)
        flash_in.move_to(bulb.glass.get_center())
        self.play(
            flash_in.animate.set_fill(opacity=0.3).scale(1.5),
            rate_func=rate_functions.ease_out_sine, run_time=0.2,
        )
        self.play(FadeOut(flash_in), run_time=0.15)
        self.play(bulb.animate_turn_on(), run_time=1.5)
        self.play(
            FadeOut(status_off, shift=UP * 0.1),
            run_time=0.2,
        )
        self.wait(0.5)

        self.play(clock.animate_tick(5), run_time=2.5)
        self.wait(0.3)

        self.play(clock.animate_tick(3), run_time=1.5)
        self.wait(0.5)

        self.play(
            FadeOut(clock),
            run_time=0.2,
        )
