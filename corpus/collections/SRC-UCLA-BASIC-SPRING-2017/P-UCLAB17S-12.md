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
For fixed $t\in\mathbb R$, let
\[
F(y;t)=y^4+t y^2+t^2y.
\]
Show that $F(\,\cdot\,;t)$ attains its global minimum at a unique point $y_0(t)$.
:::

::: {.solution}
Fix
\[
t\in\mathbb R.
\]
Write
\[
F_t(y)
=
y^4+ty^2+t^2y.
\]

<1>1. The function $F_t$ attains a global minimum on $\mathbb R$.

::: {.proof}
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

<1>2. If
\[
t=0,
\]
then
\[
\boxed{y_0(0)=0}
\]
is the unique global minimizer.

::: {.proof}
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

<1>3. Suppose
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

::: {.proof}
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

<1>4. If
\[
t>0,
\]
then $F_t$ is strictly convex and therefore has a unique global minimizer.

::: {.proof}
Step <1>3 gives
\[
F_t''(y)>0
\]
everywhere, which implies strict convexity.
A strictly convex function can have at most one global minimizer.
Existence was proved in step <1>1.
:::

<1>5. It remains to consider
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

::: {.proof}
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

<1>6. If
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

::: {.proof}
By step <1>5,
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

<1>7. Therefore no positive number can be a global minimizer when
\[
t<0.
\]

::: {.proof}
If
\[
y>0,
\]
step <1>6 exhibits the point
\[
-y
\]
with strictly smaller function value.
:::

<1>8. Also,
\[
y=0
\]
is not a global minimizer when
\[
t<0.
\]

::: {.proof}
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

<1>9. For
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

::: {.proof}
Differentiate
\[
y^4-sy^2+s^2y.
\]
:::

<1>10. The derivative of $p$ is
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

::: {.proof}
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

<1>11. The equation
\[
p(y)=0
\]
has exactly one negative solution.

::: {.proof}
As
\[
y\to-\infty,
\]
the cubic term dominates and
\[
p(y)\to-\infty.
\]
By step <1>10,
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

<1>12. Every global minimizer for
\[
t<0
\]
must equal that unique negative root of
\[
F_t'(y)=0.
\]

::: {.proof}
By step <1>1, a global minimizer exists.
By steps <1>7--<1>8, every global minimizer is strictly negative.
Since $F_t$ is differentiable on all of $\mathbb R$, every global minimizer is a critical point:
\[
F_t'(y)=0.
\]
Step <1>11 shows that there is exactly one negative critical point.
Thus every global minimizer must equal it.
:::

<1>13. Hence for every
\[
t\in\mathbb R,
\]
the function
\[
F(\,\cdot\,;t)
\]
has exactly one global minimizer.

::: {.proof}
Step <1>2 handles
\[
t=0.
\]
Step <1>4 handles
\[
t>0.
\]
Step <1>12 handles
\[
t<0.
\]
These cases exhaust all real $t$.
:::

<1>14. Q.E.D.

::: {.proof}
Step <1>13 is the required conclusion.
:::
:::
