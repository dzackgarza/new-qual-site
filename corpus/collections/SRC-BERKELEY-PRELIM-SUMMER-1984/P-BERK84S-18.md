---
schema: qual/card@1
id: P-BERK84S-18
kind: problem
title: A Fredholm-type integral equation on the unit interval
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 18 of the vendored Berkeley Preliminary Exam, Summer 1984.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Verified the rank-one reduction of the integral equation to a scalar equation with coefficient strictly less than one.
---

::: {.problem}
Show there is a unique continuous real valued function $f :$ $[ 0 , 1 ] \to \mathbb { R }$ such that

$$
f ( x ) = \sin x + \int _ { 0 } ^ { 1 } { \frac { f ( y ) } { e ^ { x + y + 1 } } } d y .
$$
:::


::: {.solution}
Set
\[
A:=\int_0^1 e^{-y}\sin y\,dy,
\qquad
k:=e^{-1}\int_0^1 e^{-2y}\,dy=\frac{e^{-1}-e^{-3}}2.
\]
Then $0<k<1$.

<1>1. Every continuous solution must have the form
\[
f(x)=\sin x+I e^{-(x+1)}
\]
for a scalar $I\in\mathbb R$.
::: {.proof}
If $f$ solves the integral equation, define
\[
I:=\int_0^1 e^{-y}f(y)\,dy.
\]
Since
\[
\frac1{e^{x+y+1}}=e^{-(x+1)}e^{-y},
\]
the integral term is
\[
e^{-(x+1)}\int_0^1 e^{-y}f(y)\,dy=I e^{-(x+1)}.
\]
Hence the displayed form is necessary.
:::

<1>2. The scalar $I$ is uniquely determined by
\[
I=A+kI.
\]
::: {.proof}
Substitute the expression from <1>1 into the definition of $I$:
\[
\begin{aligned}
I
&=\int_0^1 e^{-y}\bigl(\sin y+I e^{-(y+1)}\bigr)\,dy\\
&=A+I e^{-1}\int_0^1 e^{-2y}\,dy\\
&=A+kI.
\end{aligned}
\]
Since $k<1$, one has $1-k\neq0$, so necessarily
\[
I=\frac{A}{1-k}.
\]
Thus at most one continuous solution can exist.
:::

<1>3. This value of $I$ produces a continuous solution.
::: {.proof}
Let
\[
I_0:=\frac{A}{1-k}
\qquad	ext{and}\qquad
f_0(x):=\sin x+I_0e^{-(x+1)}.
\]
The function $f_0$ is continuous on $[0,1]$. Moreover, the calculation in <1>2, read in reverse, gives
\[
\int_0^1 e^{-y}f_0(y)\,dy=A+kI_0=I_0.
\]
Therefore
\[
\sin x+\int_0^1\frac{f_0(y)}{e^{x+y+1}}\,dy
=\sin x+e^{-(x+1)}I_0
=f_0(x).
\]
So $f_0$ is a solution. Together with uniqueness from <1>2, it is the unique continuous real-valued solution.
:::
:::
