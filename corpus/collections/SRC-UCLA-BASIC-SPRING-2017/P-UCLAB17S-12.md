---
schema: qual/card@1
id: P-UCLAB17S-12
kind: problem
title: Uniqueness of the global minimizer of a quartic family
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UCLA Basic Examination, Spring 2017, `assets/attachments/basic-17S.pdf`.
---

::: {.problem}
For fixed $t\in\RR$, let
\[
F(y;t)=y^4+t y^2+t^2y.
\]
Show that $F(\,\cdot\,;t)$ attains its global minimum at a unique point $y_0(t)$.
:::

::: {.solution}

Fix
\[
t\in\RR.
\]
Write
\[
F_t(y)
=
y^4+ty^2+t^2y.
\]

::: pf

::: {.pf-step #s1-1}

The function $F_t$ attains a global minimum on $\RR$.


::: pf-proof

As
\[
|y|\to\infty,
\]
the quartic term dominates:
\[
F_t(y)
=
y^4+ty^2+t^2y
\longrightarrow
+\infty.
\]
Hence there exists $R>0$ such that
\[
F_t(y)>F_t(0)
\]
whenever
\[
|y|>R.
\]
Therefore every global minimizer lies in the compact interval $[-R,R]$.
Since $F_t$ is continuous, it attains a minimum there.

:::

:::

::: {.pf-step #s1-2}

If
\[
t=0,
\]
then
\[
\boxed{y_0(0)=0}
\]
is the unique global minimizer.


::: pf-proof

For
\[
t=0,
\]
\[
F_0(y)=y^4\ge0,
\]
with equality only at
\[
y=0.
\]

:::

:::

::: {.pf-step #s1-3}

Suppose
\[
t>0.
\]
Then
\[
F_t''(y)
=
12y^2+2t
>
0
\]
for every $y$.


::: pf-proof

Differentiate twice:
\[
F_t'(y)
=
4y^3+2ty+t^2,
\]
\[
F_t''(y)
=
12y^2+2t.
\]
If
\[
t>0,
\]
then
\[
12y^2+2t>0.
\]

:::

:::

::: {.pf-step #s1-4}

If
\[
t>0,
\]
then $F_t$ is strictly convex and therefore has a unique global minimizer.


::: pf-proof

Step [](#s1-3){.pf-ref} gives
\[
F_t''(y)>0
\]
everywhere, which implies strict convexity.
A strictly convex function can have at most one global minimizer.
Existence was proved in step [](#s1-1){.pf-ref}.

:::

:::

::: {.pf-step #s1-5}

It remains to consider
\[
t<0.
\]
Write
\[
t=-s,
\qquad
s>0.
\]
Then
\[
F_t(y)
=
y^4-sy^2+s^2y
\]
and
\[
\boxed{
F_t(-y)-F_t(y)
=
-2s^2y.
}
\]


::: pf-proof

Substitute
\[
t=-s.
\]
Then
\[
t^2=s^2.
\]
Thus
\[
F_t(-y)
=
y^4-sy^2-s^2y,
\]
while
\[
F_t(y)
=
y^4-sy^2+s^2y.
\]
Subtract.

:::

:::

::: {.pf-step #s1-6}

If
\[
t<0
\]
and
\[
y>0,
\]
then
\[
F_t(-y)<F_t(y).
\]


::: pf-proof

By step [](#s1-5){.pf-ref},
\[
F_t(-y)-F_t(y)
=
-2s^2y.
\]
Since
\[
s>0
\quad\text{and}\quad
y>0,
\]
the right-hand side is negative.

:::

:::

::: {.pf-step #s1-7}

Therefore no positive number can be a global minimizer when
\[
t<0.
\]


::: pf-proof

If
\[
y>0,
\]
step [](#s1-6){.pf-ref} exhibits the point
\[
-y
\]
with strictly smaller function value.

:::

:::

::: {.pf-step #s1-8}

Also,
\[
y=0
\]
is not a global minimizer when
\[
t<0.
\]


::: pf-proof

One has
\[
F_t'(0)
=
t^2
>
0.
\]
Hence for sufficiently small negative $h$,
\[
F_t(h)
<
F_t(0).
\]
Thus $0$ cannot minimize globally.

:::

:::

::: pf-step

For
\[
t=-s<0,
\]
the derivative is
\[
p(y)
:=
F_t'(y)
=
4y^3-2sy+s^2.
\]


::: pf-proof

Differentiate
\[
y^4-sy^2+s^2y.
\]

:::

:::

::: {.pf-step #s1-10}

The derivative of $p$ is
\[
p'(y)
=
12y^2-2s.
\]
Its negative critical point is
\[
y_-
=
-\sqrt{\frac{s}{6}},
\]
and
\[
p(y_-)>0.
\]


::: pf-proof

Solving
\[
p'(y)=0
\]
gives
\[
y=\pm\sqrt{\frac{s}{6}}.
\]
At
\[
y_-
=
-\sqrt{\frac{s}{6}},
\]
use
\[
y_-^2=\frac{s}{6}
\]
to compute
\[
\begin{aligned}
p(y_-)
&=
4y_-^3-2sy_-+s^2\\
&=
y_-
\left(
4\frac{s}{6}-2s
\right)
+s^2\\
&=
-\frac{4s}{3}y_-
+s^2\\
&>
0,
\end{aligned}
\]
because
\[
y_-<0.
\]

:::

:::

::: {.pf-step #s1-11}

The equation
\[
p(y)=0
\]
has exactly one negative solution.


::: pf-proof

As
\[
y\to-\infty,
\]
the cubic term dominates and
\[
p(y)\to-\infty.
\]
By step [](#s1-10){.pf-ref},
\[
p(y_-)>0.
\]
Thus the intermediate value theorem gives at least one root in
\[
(-\infty,y_-).
\]

On
\[
(-\infty,y_-),
\]
one has
\[
p'(y)>0,
\]
so $p$ is strictly increasing there.
Hence that root is unique on this interval.

On
\[
[y_-,0],
\]
the function first decreases, but
\[
p(y_-)>0
\]
and
\[
p(0)=s^2>0.
\]
Therefore it has no root there.
Thus there is exactly one negative root.

:::

:::

::: {.pf-step #s1-12}

Every global minimizer for
\[
t<0
\]
must equal that unique negative root of
\[
F_t'(y)=0.
\]


::: pf-proof

By step [](#s1-1){.pf-ref}, a global minimizer exists.
By steps [](#s1-7){.pf-ref} through [](#s1-8){.pf-ref}, every global minimizer is strictly negative.
Since $F_t$ is differentiable on all of $\RR$, every global minimizer is a critical point:
\[
F_t'(y)=0.
\]
Step [](#s1-11){.pf-ref} shows that there is exactly one negative critical point.
Thus every global minimizer must equal it.

:::

:::

::: {.pf-step #s1-13}

Hence for every
\[
t\in\RR,
\]
the function
\[
F(\,\cdot\,;t)
\]
has exactly one global minimizer.


::: pf-proof

Step [](#s1-2){.pf-ref} handles
\[
t=0.
\]
Step [](#s1-4){.pf-ref} handles
\[
t>0.
\]
Step [](#s1-12){.pf-ref} handles
\[
t<0.
\]
These cases exhaust all real $t$.

:::

:::

::: pf-qed

Step [](#s1-13){.pf-ref} is the required conclusion.

:::

:::

:::
