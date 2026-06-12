from manim import *

RAMP = {
    "name": "Unit Ramp Function",

    "ct_formula": r"r(t)=\begin{cases}t & t \ge 0 \\0 & t < 0\end{cases}",
    "dt_formula": r"r[n]=\begin{cases}n & n \ge 0 \\0 & n < 0\end{cases}",

    "ct_xlabel": r"t",
    "ct_ylabel": r"r(t)",

    "dt_xlabel": r"n",
    "dt_ylabel": r"r[n]",

    "ct_color": GREEN_C,
    "dt_color": GOLD,

    "x_range": [-5, 5, 1],
    "ct_y_range": [-0.5, 5, 1],
    "dt_y_range": [-0.5, 5, 1],

    "dt_func": lambda n: n if n >= 0 else 0
}

DELTA = {
    "name": "Unit Impulse (Delta)",

    "ct_formula": r"\delta(t)=\begin{cases}0, & t \neq 0 \\ \infty, & t = 0\end{cases}\quad \text{with}\quad \int_{-\infty}^{\infty} \delta(t)\,dt = 1",

    "dt_formula": r"\delta[n]=\begin{cases}1, & n = 0 \\ 0, & n \neq 0\end{cases}",

    "ct_xlabel": r"t",
    "ct_ylabel": r"\delta(t)",

    "dt_xlabel": r"n",
    "dt_ylabel": r"\delta[n]",

    "ct_color": GREEN_C,
    "dt_color": GOLD,

    "x_range": [-5, 5, 1],
    "ct_y_range": [-0.5, 2, 1],
    "dt_y_range": [-0.5, 1.5, 1],

    "dt_func": lambda n: 1 if n == 0 else 0
}

SIGNUM = {
    "name": "Signum Function",

    "ct_formula": r"\operatorname{sgn}(t)=\begin{cases}1 & t>0 \\ 0 & t=0 \\ -1 & t<0\end{cases}",
    "dt_formula": r"\operatorname{sgn}[n]=\begin{cases}1 & n>0 \\ 0 & n=0 \\ -1 & n<0\end{cases}",

    "ct_xlabel": r"t",
    "ct_ylabel": r"\operatorname{sgn}(t)",

    "dt_xlabel": r"n",
    "dt_ylabel": r"\operatorname{sgn}[n]",

    "ct_color": GREEN_C,
    "dt_color": GOLD,

    "x_range": [-5, 5, 1],
    "ct_y_range": [-1.5, 1.5, 1],
    "dt_y_range": [-1.5, 1.5, 1],

    "dt_func": lambda n: 1 if n > 0 else (-1 if n < 0 else 0)
}