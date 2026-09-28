---
schema: qual/card@1
id: P-BERK84S-09
kind: problem
title: A planar ODE trajectory crosses x equals 1
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
  note: Checked against Problem 9 of the vendored Berkeley Preliminary Exam, Summer 1984.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Verified the positivity barrier at x=0 and the differential inequality x'>1/2 before the first crossing of x=1.
---

::: {.problem}
Consider the solution curve $( x ( t ) , y ( t ) )$ to the equations

$$
{ \begin{array} { l } { { \frac { d x } { d t } } = 1 + { \frac { 1 } { 2 } } x ^ { 2 } \sin y } \\ { { \frac { d y } { d t } } = 3 - x ^ { 2 } } \end{array} }
$$

with initial conditions $x ( 0 ) = 0$ and $y ( 0 ) = 0$ . Prove that the solution must cross the line $x = 1$ in the xy plane by the time $t = 2$
:::


::: {.solution}
We argue by contradiction.

<1>1. The solution cannot cross from $x\ge0$ into $x<0$.
::: {.proof}
Whenever $x(t_0)=0$, the first differential equation gives
\[
x'(t_0)=1+\frac12\,0^2\sin y(t_0)=1.
\]
Thus
\[
x(t_0+h)=h+o(h)>0
\]
for all sufficiently small $h>0$. Since $x(0)=0$, the trajectory cannot have a first passage from the half-plane $x\ge0$ into $x<0$. Hence
\[
x(t)\ge0
\]
for as long as the solution exists forward in time.
:::

<1>2. Before the first crossing of $x=1$, one has $x'(t)>1/2$.
::: {.proof}
Suppose the trajectory has not crossed the line $x=1$ by time $t$. By <1>1 and continuity,
\[
0\le x(s)<1
\qquad(0\le s\le t).
\]
Using $\sin y\ge-1$,
\[
x'(s)
=1+\frac12x(s)^2\sin y(s)
\ge1-\frac12x(s)^2
>\frac12.
\]
:::

<1>3. The trajectory must cross $x=1$ before or at time $2$.
::: {.proof}
Assume it does not cross $x=1$ for $0\le t\le2$. Then <1>2 holds throughout $[0,2]$, so
\[
x(2)-x(0)=\int_0^2x'(s)\,ds
>\int_0^2\frac12\,ds=1.
\]
Since $x(0)=0$, this gives $x(2)>1$, contradicting the assumption that the trajectory never crossed $x=1$ on $[0,2]$.

Therefore the solution curve crosses the line $x=1$ at some time
\[
\boxed{t\le2}.
\]
:::
:::
