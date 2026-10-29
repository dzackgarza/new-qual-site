---
schema: qual/card@1
id: P-UCLAB16F-10
kind: problem
title: Point of $x^4+y^4=2$ closest to the line $y=x-100$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 10 of the retained UCLA Basic Examination Fall 2016 PDF.
---

::: {.problem}
Find the unique point $(x, y) \in \RR^2$ on the curve

$$
y^4 + x^4 = 2
$$

that is closest to the line

$$
y = x - 100.
$$

Note: Formal calculations alone do not constitute a solution.
You must justify rigorously that there is a point that is closest, that it is unique, and that it is the specific point that you claim that it is.
:::

::: {.solution}

Let
\[
C=\{(x,y)\in\RR^2:x^4+y^4=2\}.
\]

::: pf

::: {.pf-step #s1-1}

The set $C$ is compact.


::: pf-proof

The function
\[
(x,y)\longmapsto x^4+y^4
\]
is continuous, so
\[
C
=
\{(x,y):x^4+y^4=2\}
\]
is closed.

Also
\[
x^4\le2,
\qquad
y^4\le2,
\]
so
\[
|x|,|y|\le2^{1/4}.
\]
Thus $C$ is bounded.
By Heine--Borel, $C$ is compact.

:::

:::

::: {.pf-step #s1-2}

The distance from $(x,y)$ to the line
\[
y=x-100
\]
is
\[
d(x,y)
=
\frac{|y-x+100|}{\sqrt2}.
\]


::: pf-proof

The line has equation
\[
-x+y+100=0.
\]
The distance from a point $(x,y)$ to a line
\[
ax+by+c=0
\]
is
\[
\frac{|ax+by+c|}{\sqrt{a^2+b^2}}.
\]
Substitute
\[
a=-1,
\qquad
b=1,
\qquad
c=100.
\]

:::

:::

::: {.pf-step #s1-3}

For every $(x,y)\in C$,
\[
y-x+100>0.
\]


::: pf-proof

By step [](#s1-1){.pf-ref},
\[
|x|,|y|\le2^{1/4}<2.
\]
Hence
\[
y-x+100
\ge
100-|x|-|y|
>
100-4
>
0.
\]

:::

:::

::: {.pf-step #s1-4}

Minimizing the distance to the line over $C$ is equivalent to maximizing
\[
x-y
\]
over $C$.


::: pf-proof

By steps [](#s1-2){.pf-ref} through [](#s1-3){.pf-ref},
\[
d(x,y)
=
\frac{100+y-x}{\sqrt2}.
\]
The constant factor $1/\sqrt2$ and the additive constant $100$ do not affect the minimizing point.
Thus minimizing $d$ is equivalent to minimizing
\[
y-x,
\]
equivalently maximizing
\[
x-y.
\]

:::

:::

::: {.pf-step #s1-5}

A maximizing point exists.


::: pf-proof

The function
\[
(x,y)\longmapsto x-y
\]
is continuous on the compact set $C$.
The extreme value theorem therefore gives a global maximum.

:::

:::

::: pf-step

For every $(x,y)\in C$,
\[
x-y\le2.
\]


::: pf-proof

By Hölder's inequality with exponents
\[
4
\qquad\text{and}\qquad
\frac43,
\]
\[
\begin{aligned}
x-y
&\le
|x|+|y|\\
&\le
\bigl(|x|^4+|y|^4\bigr)^{1/4}
\bigl(1^{4/3}+1^{4/3}\bigr)^{3/4}\\
&=
2^{1/4}2^{3/4}\\
&=
2.
\end{aligned}
\]

:::

:::

::: {.pf-step #s1-7}

Equality
\[
x-y=2
\]
holds on $C$ only at
\[
\boxed{(x,y)=(1,-1)}.
\]


::: pf-proof

For equality in
\[
x-y\le |x|+|y|,
\]
one must have
\[
x\ge0
\qquad\text{and}\qquad
y\le0.
\]

For equality in Hölder with vectors
\[
(|x|,|y|)
\qquad\text{and}\qquad
(1,1),
\]
the quantities
\[
|x|^4
\qquad\text{and}\qquad
|y|^4
\]
must be proportional to
\[
1^{4/3}
\qquad\text{and}\qquad
1^{4/3},
\]
so
\[
|x|=|y|.
\]
The constraint
\[
x^4+y^4=2
\]
then gives
\[
2|x|^4=2,
\]
so
\[
|x|=|y|=1.
\]
Together with the sign conditions,
\[
x=1,
\qquad
y=-1.
\]
Conversely,
\[
(1,-1)\in C
\]
and
\[
1-(-1)=2.
\]
Thus it is the unique maximizer.

:::

:::

::: {.pf-step #s1-8}

Therefore the unique point on $C$ closest to the line is
\[
\boxed{(1,-1)}.
\]


::: pf-proof

By step [](#s1-4){.pf-ref}, closest points are exactly maximizers of $x-y$.
Step [](#s1-5){.pf-ref} proves existence, and step [](#s1-7){.pf-ref} proves that the unique maximizer is $(1,-1)$.

:::

:::

::: {.pf-step #s1-9}

The minimum distance itself is
\[
\boxed{49\sqrt2}.
\]


::: pf-proof

At
\[
(1,-1),
\]
step [](#s1-2){.pf-ref} gives
\[
d
=
\frac{|-1-1+100|}{\sqrt2}
=
\frac{98}{\sqrt2}
=
49\sqrt2.
\]

:::

:::

::: pf-qed

Step [](#s1-8){.pf-ref} gives the unique closest point, with existence and uniqueness justified, and step [](#s1-9){.pf-ref} gives the corresponding distance.

:::

:::

:::
