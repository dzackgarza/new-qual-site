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

::: pf

::: {.pf-step #characteristic-roots}
The characteristic equation is
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

::: pf-proof
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

:::

::: {.pf-step #roots-with-negative-real-part}
The roots with negative real part are
$$
\frac{-1+i}{\sqrt2}
\qquad\text{and}\qquad
\frac{-1-i}{\sqrt2}.
$$

::: pf-proof
These are
$$
e^{3i\pi/4}
\qquad\text{and}\qquad
e^{5i\pi/4}.
$$
Their real part is $-1/\sqrt2$, while the other two roots have positive
real part.
:::

:::

::: {.pf-step #decaying-solution-form}
Every real solution whose value and first derivative tend to zero as
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

::: pf-proof
The two roots from step [](#roots-with-negative-real-part){.pf-ref} give the real basis
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

:::

::: {.pf-step #A-zero}
The condition
$$
y(0)=0
$$
forces
$$
A=0.
$$

::: pf-proof
Substitution of $x=0$ in step [](#decaying-solution-form){.pf-ref} gives $y(0)=A$.
:::

:::

::: {.pf-step #y-prime-zero-formula}
With $A=0$,
$$
y'(0)
=
\frac{B}{\sqrt2}.
$$

::: pf-proof
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

:::

::: {.pf-step #B-value}
The condition
$$
y'(0)=1
$$
forces
$$
B=\sqrt2.
$$

::: pf-proof
Apply step [](#y-prime-zero-formula){.pf-ref}.
:::

:::

::: {.pf-step #explicit-solution}
The required function is
$$
\boxed{
y(x)
=
\sqrt2\,e^{-x/\sqrt2}
\sin\frac{x}{\sqrt2}
}.
$$

::: pf-proof
Steps [](#decaying-solution-form){.pf-ref}, [](#A-zero){.pf-ref}, [](#y-prime-zero-formula){.pf-ref} and [](#B-value){.pf-ref} determine this solution. It solves the differential
equation because it is built from characteristic roots of $r^4+1$, and its
value and first derivative tend to zero because they are bounded
trigonometric factors times $e^{-x/\sqrt2}$.
:::

:::

::: pf-qed
Step [](#explicit-solution){.pf-ref} verifies all requested conditions.
:::

:::

:::
