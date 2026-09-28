---
schema: qual/card@1
id: P-BKF98-2
kind: problem
title: A decaying solution of $y^{(4)}+y=0$ with prescribed initial data
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-25
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-25
  note: >-
    Selected the two characteristic roots with negative real part and imposed
    the initial conditions on the resulting real decaying two-dimensional
    solution space.
---

::: {.problem}
Find a function $y(x)$ for $x\ge0$ such that
\[
y^{(4)}+y=0,
\qquad
y(0)=0,
\qquad
y'(0)=1,
\]
and
\[
\lim_{x\to\infty}y(x)=
\lim_{x\to\infty}y'(x)=0.
\]
:::

::: {.solution}
<1>1. The characteristic equation is
$$
r^4+1=0,
$$
with roots
$$
e^{i\pi/4},
\quad
e^{3i\pi/4},
\quad
e^{5i\pi/4},
\quad
e^{7i\pi/4}.
$$

::: {.proof}
The equation $r^4=-1$ has the four solutions
$$
r
=
\exp\left(
\frac{(2k+1)\pi i}{4}
\right),
\qquad
k=0,1,2,3.
$$
:::

<1>2. The roots with negative real part are
$$
\frac{-1+i}{\sqrt2}
\qquad\text{and}\qquad
\frac{-1-i}{\sqrt2}.
$$

::: {.proof}
These are
$$
e^{3i\pi/4}
\qquad\text{and}\qquad
e^{5i\pi/4}.
$$
Their real part is $-1/\sqrt2$, while the other two roots have positive
real part.
:::

<1>3. Every real solution whose value and first derivative tend to zero as
$x\to\infty$ has the form
$$
y(x)
=
e^{-x/\sqrt2}
\left(
A\cos\frac{x}{\sqrt2}
+B\sin\frac{x}{\sqrt2}
\right)
$$
for real constants $A,B$.

::: {.proof}
The two roots from step <1>2 give the real basis
$$
e^{-x/\sqrt2}\cos\frac{x}{\sqrt2},
\qquad
e^{-x/\sqrt2}\sin\frac{x}{\sqrt2}.
$$
Both functions and their first derivatives tend to zero. The other two
characteristic roots have positive real part; any nonzero contribution from
them grows exponentially along an unbounded sequence and cannot satisfy the
two decay conditions. Thus precisely the displayed two-dimensional real
space consists of decaying solutions.
:::

<1>4. The condition
$$
y(0)=0
$$
forces
$$
A=0.
$$

::: {.proof}
Substitution of $x=0$ in step <1>3 gives $y(0)=A$.
:::

<1>5. With $A=0$,
$$
y'(0)
=
\frac{B}{\sqrt2}.
$$

::: {.proof}
Write
$$
a=\frac1{\sqrt2}.
$$
Then
$$
y(x)=B e^{-ax}\sin(ax),
$$
so
$$
y'(x)
=
Ba e^{-ax}
\bigl(
\cos(ax)-\sin(ax)
\bigr).
$$
At $x=0$ this gives $y'(0)=Ba=B/\sqrt2$.
:::

<1>6. The condition
$$
y'(0)=1
$$
forces
$$
B=\sqrt2.
$$

::: {.proof}
Apply step <1>5.
:::

<1>7. The required function is
$$
\boxed{
y(x)
=
\sqrt2\,e^{-x/\sqrt2}
\sin\frac{x}{\sqrt2}
}.
$$

::: {.proof}
Steps <1>3--<1>6 determine this solution. It solves the differential
equation because it is built from characteristic roots of $r^4+1$, and its
value and first derivative tend to zero because they are bounded
trigonometric factors times $e^{-x/\sqrt2}$.
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>7 verifies all requested conditions.
:::
:::
