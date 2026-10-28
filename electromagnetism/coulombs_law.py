"""Coulomb's Law — qualitative 2D animation (Manim Community Edition).

Two acts in one continuous scene:
  1. Like charges  (+q1, +q2)  repel;  force weakens as they separate.
  2. Unlike charges (+q1, -q2) attract; force strengthens as they approach.

Physics notes:
  * Force-arrow lengths follow a *clamped inverse-square* mapping of the
    separation r:  L(r) in [F_LEN_MIN, F_LEN_MAX], so arrows never explode
    or vanish and always grow when r shrinks (and vice versa).
  * The two arrows always have identical lengths (Newton's third law).
  * Motion after "release" is illustrative, not a numerical simulation:
    repulsion uses an ease-out (decelerating) rate, attraction uses
    ease-in-out (accelerating then stopping cleanly before overlap).

Render:
    manim -qh coulombs_law.py CoulombsLaw
"""

from manim import *

# --------------------------------------------------------------------------
# Global look
# --------------------------------------------------------------------------
config.background_color = "#101018"

POSITIVE_COLOR = "#E05A5A"   # positive charges
NEGATIVE_COLOR = "#4FA8E8"   # negative charges
FORCE_COLOR = "#F5C542"      # force arrows + their labels
GUIDE_COLOR = "#8A8A9E"      # external-agent guide arrows
TEXT_COLOR = "#EAEAF0"       # headings / takeaways
GREY = "#9A9AB0"             # distance indicator

# --------------------------------------------------------------------------
# Geometry (all in Manim scene units; 16:9 frame is ~14.22 x 8)
# --------------------------------------------------------------------------
CHARGE_RADIUS = 0.55
EDGE_BUFF = 0.10             # gap between charge circle and arrow origin

R_START = 4.6                # initial center-to-center separation
R_CLOSE = 2.2                # closest approach, repel act (external agent)
R_END = 4.2                  # separation after repel release
R_CLOSE_ATTR = 3.3           # closest approach, attract act (external agent)
R_STOP = 2.8                 # stop separation, attract act (no overlap)

F_LEN_MIN = 0.45             # arrow length at r = R_START
F_LEN_MAX = 2.2              # arrow length at r = R_CLOSE

HEADING_Y = 3.15
GUIDE_Y = 1.35
AGENT_TEXT_Y = 2.05
DISTANCE_Y = -2.05

# --------------------------------------------------------------------------
# Timing (seconds) — tweak freely
# --------------------------------------------------------------------------
D_INTRO = 1.2
D_FORCES = 1.3
D_GUIDE = 0.6
D_APPROACH = 3.5
D_HOLD_CLOSE = 0.8
D_RELEASE = 4.2
W_WAIT = 0.4                 # short "let it register" pauses
W_TRANSITION = 0.5


# --------------------------------------------------------------------------
# Helpers
# --------------------------------------------------------------------------
def force_length(r: float) -> float:
    """Clamped inverse-square visual length for the force arrows.

    Maps 1/r^2 linearly onto [F_LEN_MIN, F_LEN_MAX] between r = R_START
    (minimum force in the animation) and r = R_CLOSE (maximum force),
    then clamps so out-of-range separations stay legible.
    """
    f = 1.0 / (r * r)
    f_min = 1.0 / (R_CLOSE * R_CLOSE)
    f_max = 1.0 / (R_START * R_START)
    frac = (f - f_max) / (f_min - f_max)
    frac = max(0.0, min(1.0, frac))
    return F_LEN_MIN + (F_LEN_MAX - F_LEN_MIN) * frac


def make_charge(tex: str, color: str) -> VGroup:
    """A filled circle with a centered MathTex label, e.g. '+q_1'."""
    disk = Circle(
        radius=CHARGE_RADIUS,
        color=color,
        fill_color=color,
        fill_opacity=1.0,
        stroke_width=3,
    )
    label = MathTex(tex, font_size=48, color=WHITE)
    label.move_to(disk)
    return VGroup(disk, label)


def make_force_arrow(r_tracker: ValueTracker, side: int, attractive: bool) -> VGroup:
    """Dynamically sized force arrow + F_12 / F_21 label for one charge.

    side = -1: left charge (q1);  side = +1: right charge (q2).
    Repel: arrows point away from the partner (dir = side).
    Attract: arrows point toward the partner (dir = -side).
    Attraction arrows are additionally clamped so they never reach the
    other charge's circle.
    """

    def build() -> VGroup:
        r = r_tracker.get_value()
        length = force_length(r)
        # Attraction arrows sit slightly off the center line (q1 above,
        # q2 below) so the two vectors never merge visually; they are
        # clamped only so they cannot reach the other charge's circle.
        y = 0.0
        label_dy = 0.45
        if attractive:
            y = -0.28 * side
            label_dy = 0.42 if side == -1 else -0.42
            max_len = r - 2 * CHARGE_RADIUS - EDGE_BUFF - 0.25
            length = min(length, max(0.30, max_len))

        direction = side if not attractive else -side
        charge_x = side * r / 2
        start_x = charge_x + direction * (CHARGE_RADIUS + EDGE_BUFF)
        end_x = start_x + direction * length

        arrow = Arrow(
            start=[start_x, y, 0],
            end=[end_x, y, 0],
            buff=0,
            color=FORCE_COLOR,
            stroke_width=7,
            max_tip_length_to_length_ratio=0.45,
        )
        tex = r"F_{12}" if side == -1 else r"F_{21}"
        label = MathTex(tex, font_size=42, color=FORCE_COLOR)
        label.move_to([(start_x + end_x) / 2, y + label_dy, 0])
        return VGroup(arrow, label)

    return always_redraw(build)


def make_distance_indicator(r_tracker: ValueTracker) -> VGroup:
    """Dashed separation line with end ticks and an 'r' label below."""

    def build() -> VGroup:
        r = r_tracker.get_value()
        line = DashedLine(
            [-r / 2, DISTANCE_Y, 0],
            [r / 2, DISTANCE_Y, 0],
            color=GREY,
            dash_length=0.15,
            stroke_width=3,
        )
        tick_l = Line(
            [-r / 2, DISTANCE_Y - 0.12, 0],
            [-r / 2, DISTANCE_Y + 0.12, 0],
            color=GREY,
            stroke_width=3,
        )
        tick_r = Line(
            [r / 2, DISTANCE_Y - 0.12, 0],
            [r / 2, DISTANCE_Y + 0.12, 0],
            color=GREY,
            stroke_width=3,
        )
        label = MathTex("r", font_size=36, color=GREY)
        label.next_to([0, DISTANCE_Y, 0], DOWN, buff=0.18)
        return VGroup(line, tick_l, tick_r, label)

    return always_redraw(build)


def make_guides(r_tracker: ValueTracker) -> VGroup:
    """Subtle dashed inward arrows = external agent pushing charges together."""

    def build() -> VGroup:
        r = r_tracker.get_value()
        left = Arrow(
            [-r / 2, GUIDE_Y, 0],
            [-r / 2 + 0.75, GUIDE_Y, 0],
            buff=0,
            color=GUIDE_COLOR,
            stroke_width=5,
            max_tip_length_to_length_ratio=0.4,
        )
        right = Arrow(
            [r / 2, GUIDE_Y, 0],
            [r / 2 - 0.75, GUIDE_Y, 0],
            buff=0,
            color=GUIDE_COLOR,
            stroke_width=5,
            max_tip_length_to_length_ratio=0.4,
        )
        for a in (left, right):
            a.set_opacity(0.75)
        return VGroup(left, right)

    return always_redraw(build)


# --------------------------------------------------------------------------
# Scene
# --------------------------------------------------------------------------
class CoulombsLaw(Scene):
    def construct(self):
        self.act_like_charges()
        self.transition()
        self.act_unlike_charges()

    # ---------------- public acts ----------------
    def act_like_charges(self):
        self.run_case(attractive=False)

    def act_unlike_charges(self):
        self.run_case(attractive=True)

    # ---------------- shared implementation ----------------
    def run_case(self, attractive: bool):
        if attractive:
            heading = Text("UNLIKE CHARGES", font_size=42, weight=BOLD, color=TEXT_COLOR)
            q2_tex, q2_color = "-q_2", NEGATIVE_COLOR
            r_close, r_end = R_CLOSE_ATTR, R_STOP
            release_rate = rate_functions.ease_in_out_sine
        else:
            heading = Text("LIKE CHARGES", font_size=42, weight=BOLD, color=TEXT_COLOR)
            q2_tex, q2_color = "+q_2", POSITIVE_COLOR
            r_close, r_end = R_CLOSE, R_END
            release_rate = rate_functions.ease_out_sine

        heading.to_edge(UP, buff=0.35)

        r_tracker = ValueTracker(R_START)
        q1 = make_charge(r"+q_1", POSITIVE_COLOR)
        q2 = make_charge(q2_tex, q2_color)
        q1.add_updater(lambda m: m.move_to([-r_tracker.get_value() / 2, 0, 0]))
        q2.add_updater(lambda m: m.move_to([r_tracker.get_value() / 2, 0, 0]))

        arrows = VGroup(
            make_force_arrow(r_tracker, side=-1, attractive=attractive),
            make_force_arrow(r_tracker, side=+1, attractive=attractive),
        )
        distance = make_distance_indicator(r_tracker)
        guides = make_guides(r_tracker)
        agent_text = (
            Text("external agent", font_size=26, color=GUIDE_COLOR)
            .move_to([0, AGENT_TEXT_Y, 0])
        )

        # ---- Step 1: introduce charges + heading ----
        self.play(FadeIn(q1, shift=UP * 0.3), FadeIn(q2, shift=UP * 0.3),
                  FadeIn(heading, shift=DOWN * 0.2), run_time=D_INTRO)
        self.wait(W_WAIT)

        # ---- Step 2: show the electric forces ----
        self.add(arrows, distance)
        self.play(
            GrowArrow(arrows[0][0]), GrowArrow(arrows[1][0]),
            FadeIn(arrows[0][1]), FadeIn(arrows[1][1]),
            FadeIn(distance),
            run_time=D_FORCES,
        )
        self.wait(W_WAIT)

        # ---- Step 3: external agent brings charges closer ----
        self.play(FadeIn(guides), FadeIn(agent_text), run_time=D_GUIDE)
        self.wait(W_WAIT * 0.5)
        self.play(
            r_tracker.animate.set_value(r_close),
            run_time=D_APPROACH,
            rate_func=smooth,
        )
        self.wait(D_HOLD_CLOSE)

        # ---- Step 4: release ----
        self.play(FadeOut(guides), FadeOut(agent_text), run_time=0.4)
        if attractive:
            # mutual attraction: charges move toward each other, stop safely
            self.play(
                r_tracker.animate.set_value(r_end),
                run_time=D_RELEASE,
                rate_func=release_rate,
            )
        else:
            # repulsion: ease-out drift apart (weakening force, decelerating)
            self.play(
                r_tracker.animate.set_value(r_end),
                run_time=D_RELEASE,
                rate_func=release_rate,
            )
        self.wait(W_WAIT)

        # ---- clear the act ----
        dynamic = [q1, q2, arrows, distance, guides]
        for mob in dynamic:
            mob.clear_updaters()
        self.play(
            FadeOut(q1), FadeOut(q2), FadeOut(arrows), FadeOut(distance),
            FadeOut(heading),
            run_time=0.7,
        )

    def transition(self):
        self.wait(W_TRANSITION)
