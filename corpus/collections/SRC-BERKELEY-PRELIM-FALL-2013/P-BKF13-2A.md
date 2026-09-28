---
schema: qual/card@1
id: P-BKF13-2A
kind: problem
title: Grönwall's inequality
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
    Checked against Problem 2A in the retained Fall 2013 Berkeley prelim exam
    and independently reviewed the retained solution packet F13_Solutions.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked the integrating-factor derivative and the sign-preserving
    multiplication used to recover the stated inequality.
---

::: {.problem}
Suppose that x is a smooth real-valued function of the real number t, satisfying $d x / d t \leq$ $b ( t ) x ( t )$ for some continuous function b. Prove that if $s \leq t$ then $\begin{array} { r } { x ( t ) \leq x ( s ) \exp { \int _ { s } ^ { t } b ( t ) d t } . } \end{array}$
:::

::: {.solution}
Fix $s$, and for $u\ge s$ define
$$
B(u)\coloneqq\int_s^u b(v)\,dv,
\qquad
y(u)\coloneqq x(u)e^{-B(u)}.
$$

<1>1. The function $y$ is nonincreasing on $[s,\infty)$.

::: {.proof}
Since $b$ is continuous,
$$
B'(u)=b(u).
$$
Therefore
$$
\begin{aligned}
y'(u)
&=e^{-B(u)}
\left(x'(u)-b(u)x(u)\right).
\end{aligned}
$$
The exponential factor is positive, while the hypothesis gives
$$
x'(u)-b(u)x(u)\le0.
$$
Hence $y'(u)\le0$, so $y$ is nonincreasing.
:::

<1>2. If $s\le t$, then
$$
\boxed{
x(t)
\le
x(s)\exp\left(\int_s^t b(u)\,du\right)
}.
$$

::: {.proof}
By step <1>1,
$$
y(t)\le y(s).
$$
Since $B(s)=0$, this is
$$
x(t)e^{-B(t)}\le x(s).
$$
Multiplying by the positive number $e^{B(t)}$ gives
$$
x(t)\le x(s)e^{B(t)}
=x(s)\exp\left(\int_s^t b(u)\,du\right).
$$
:::

<1>3. Q.E.D.

::: {.proof}
Step <1>2 is the required inequality.
:::
:::
