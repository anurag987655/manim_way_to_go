# Signal Transformation

A signal can be transformed by changing the input value, which in most cases is $t$. The basic transformations are scale, shift, and reversal.

# Some Background Theory
For a signal $x(t)$, we define it in coordinates as a point $(t, x(t))$, where $x(t)$ is the signal amplitude and $t$ is time. The transformations we are about to see occur for time.

## Shift
A shift generally means a shift in time. A shifted input is characterized by $t + \text{shift}$. 

Given a signal $x(t)$, how can we know where the point $(t, x(t))$ maps when the input is shifted by $\tau$? 

In the new shifted signal, the input is $t+\tau$. The input in the initial signal is given by $t$. If the value of $t$ is 1, then to get the value of 1 in the shifted input, we need to subtract $\tau$ from the time variable. For example, let's say $x(1) = 5$ (where $t = 1$). In the shifted signal $x(t+\tau)$, to get the value of $x(1)$, we need the inner part $t+\tau$ to equal 1. This gives $t = 1 - \tau$, meaning the point has moved from $t=1$ to $t=1-\tau$.
