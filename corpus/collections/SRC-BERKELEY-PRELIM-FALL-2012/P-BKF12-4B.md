---
schema: qual/card@1
id: P-BKF12-4B
kind: problem
title: Evaluation of $\int_0^\infty dx/(x^2+1)^2$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked against Problem 4B in the retained Fall 2012 Berkeley prelim exam
    and independently reviewed the retained solution packet F12_Solutions.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked the improper-integral substitution and the resulting elementary
    trigonometric integral.
---

::: {.problem}
Compute

$$
\int _ { 0 } ^ { \infty } { \frac { d x } { ( x ^ { 2 } + 1 ) ^ { 2 } } } .
$$
:::

::: {.solution}
<1>1. With the substitution $x=\tan\theta$,
$$
\int_0^\infty\frac{dx}{(1+x^2)^2}
=\int_0^{\pi/2}\cos^2\theta\,d\theta.
$$

::: {.proof}
For $R>0$, put $x=\tan\theta$ on $[0,R]$. Then
$$
dx=\sec^2\theta\,d\theta,
\qquad
1+x^2=\sec^2\theta,
$$
so
$$
\int_0^R\frac{dx}{(1+x^2)^2}
=\int_0^{\arctan R}\cos^2\theta\,d\theta.
$$
Letting $R\to\infty$ gives $\arctan R\to\pi/2$, which yields the
displayed identity.
:::

<1>2. The value of the integral is
$$
\boxed{\frac\pi4}.
$$

::: {.proof}
By step <1>1 and the identity
$$
\cos^2\theta=\frac{1+\cos(2\theta)}2,
$$
one has
$$
\begin{aligned}
\int_0^\infty\frac{dx}{(1+x^2)^2}
&=\int_0^{\pi/2}\cos^2\theta\,d\theta\\
&=\left[
\frac\theta2+\frac{\sin(2\theta)}4
\right]_0^{\pi/2}\\
&=\frac\pi4.
\end{aligned}
$$
:::

<1>3. Q.E.D.

::: {.proof}
Step <1>2 gives the requested value.
:::
:::
