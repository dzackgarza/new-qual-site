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
Find the unique point $( x , y ) \in \mathbb { R } ^ { 2 }$ on the curve

$$
y ^ { 4 } + x ^ { 4 } = 2
$$

that is closest to the line

$$
y = x - 100 .
$$

Note: Formal calculations alone do not constitute a solution.
You must justify rigorously that there is a point that is closest, that it is unique, and that it is the specific point that you claim that it is.
:::

::: {.solution}
Let
\[
C=\{(x,y)\in\mathbb R^2:x^4+y^4=2\}.
\]

<1>1. The set $C$ is compact.

::: {.proof}
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

<1>2. The distance from $(x,y)$ to the line
\[
y=x-100
\]
is
\[
d(x,y)
=
\frac{|y-x+100|}{\sqrt2}.
\]

::: {.proof}
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

<1>3. For every $(x,y)\in C$,
\[
y-x+100>0.
\]

::: {.proof}
By step <1>1,
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

<1>4. Minimizing the distance to the line over $C$ is equivalent to maximizing
\[
x-y
\]
over $C$.

::: {.proof}
By steps <1>2--<1>3,
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

<1>5. A maximizing point exists.

::: {.proof}
The function
\[
(x,y)\longmapsto x-y
\]
is continuous on the compact set $C$.
The extreme value theorem therefore gives a global maximum.
:::

<1>6. For every $(x,y)\in C$,
\[
x-y\le2.
\]

::: {.proof}
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

<1>7. Equality
\[
x-y=2
\]
holds on $C$ only at
\[
\boxed{(x,y)=(1,-1)}.
\]

::: {.proof}
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

<1>8. Therefore the unique point on $C$ closest to the line is
\[
\boxed{(1,-1)}.
\]

::: {.proof}
By step <1>4, closest points are exactly maximizers of $x-y$.
Step <1>5 proves existence, and step <1>7 proves that the unique maximizer is $(1,-1)$.
:::

<1>9. The minimum distance itself is
\[
\boxed{49\sqrt2}.
\]

::: {.proof}
At
\[
(1,-1),
\]
step <1>2 gives
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

<1>10. Q.E.D.

::: {.proof}
Step <1>8 gives the unique closest point, with existence and uniqueness justified, and step <1>9 gives the corresponding distance.
:::
:::
