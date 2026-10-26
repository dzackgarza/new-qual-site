---
schema: qual/card@1
id: P-UCLARA17F-04
kind: problem
title: A bounded functional on $C([-1,1])$ mapping the unit ball onto an open set
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Fall 2017, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Problem 4. Consider the Banach space $V=C([-1,1])$ of all real-valued continuous functions on $[-1,1]$, equipped with the supremum norm
\[
\|f\|=\sup\{|f(x)|:x\in[-1,1]\},\qquad f\in V.
\]
Let
\[
B=\{f\in V:\|f\|\le1\}
\]
be the closed unit ball in $V$. Show that there exists a bounded linear functional $\Lambda:V\to\mathbb R$ such that $\Lambda(B)$ is an open subset of $\mathbb R$.
:::

Define
\[
\boxed{
\Lambda(f)
=
\int_0^1 f(x)\,dx
-
\int_{-1}^0 f(x)\,dx}.
\]

::: pf

::: pf-step

The map
\[
\Lambda:V\to\mathbb R
\]
is linear.


::: pf-proof

Both integrals are linear in \(f\), so their difference is linear.

:::

:::

::: pf-step

For every \(f\in V\),
\[
\boxed{
|\Lambda(f)|
\le
2\|f\|_\infty}.
\]


::: pf-proof

By the triangle inequality,
\[
\begin{aligned}
|\Lambda(f)|
&\le
\int_0^1|f(x)|\,dx
+
\int_{-1}^0|f(x)|\,dx\\
&\le
\|f\|_\infty+\|f\|_\infty\\
&=
2\|f\|_\infty.
\end{aligned}
\]

:::

:::

::: pf-step

Hence \(\Lambda\) is bounded and
\[
\boxed{
\|\Lambda\|\le2}.
\]


::: pf-proof

Step <1>2 is exactly the operator-norm estimate.

:::

:::

::: pf-step

One has
\[
\boxed{
f_\varepsilon\in B}.
\]


::: pf-proof

The function is continuous at \(\pm\varepsilon\), and
\[
|f_\varepsilon(x)|\le1
\]
for all \(x\). Hence
\[
\|f_\varepsilon\|_\infty\le1.
\]

:::

:::

::: pf-step

One has
\[
\boxed{
\Lambda(f_\varepsilon)=2-\varepsilon}.
\]


::: pf-proof

Compute the positive-half integral:
\[
\begin{aligned}
\int_0^1 f_\varepsilon(x)\,dx
&=
\int_0^\varepsilon \frac{x}{\varepsilon}\,dx
+
\int_\varepsilon^1 1\,dx\\
&=
\frac{\varepsilon}{2}
+
1-\varepsilon\\
&=
1-\frac{\varepsilon}{2}.
\end{aligned}
\]
By odd symmetry of \(f_\varepsilon\),
\[
\int_{-1}^0 f_\varepsilon(x)\,dx
=
-\left(
1-\frac{\varepsilon}{2}
\right).
\]
Therefore
\[
\Lambda(f_\varepsilon)
=
2\left(
1-\frac{\varepsilon}{2}
\right)
=
2-\varepsilon.
\]

:::

:::

::: pf-step

Hence
\[
\boxed{
\|\Lambda\|=2}.
\]


::: pf-proof

Step <1>3 gives \(\|\Lambda\|\le2\). Step <1>5 gives values
\[
\Lambda(f_\varepsilon)=2-\varepsilon
\]
with \(\|f_\varepsilon\|_\infty\le1\), so
\[
\|\Lambda\|
\ge
2-\varepsilon
\]
for every \(\varepsilon>0\). Let \(\varepsilon\downarrow0\).

:::

:::

::: pf-step

Suppose \(f\in B\) and
\[
\Lambda(f)=2.
\]
Then
\[
\boxed{
f(x)=1
\text{ for almost every }x\in[0,1]}.
\]


::: pf-proof

Since \(\|f\|_\infty\le1\),
\[
\int_0^1 f(x)\,dx\le1
\]
and
\[
-\int_{-1}^0f(x)\,dx\le1.
\]
Their sum is \(2\). Therefore both inequalities must be equalities:
\[
\int_0^1 f(x)\,dx=1.
\]
Because
\[
f(x)\le1
\]
everywhere,
\[
\int_0^1(1-f(x))\,dx=0
\]
with nonnegative integrand. Hence
\[
f(x)=1
\]
almost everywhere on \([0,1]\).

:::

:::

::: pf-step

Under the same assumption,
\[
\boxed{
f(x)=-1
\text{ for almost every }x\in[-1,0]}.
\]


::: pf-proof

Equality in the second estimate from step <1>7 gives
\[
\int_{-1}^0f(x)\,dx=-1.
\]
Since
\[
f(x)\ge-1,
\]
\[
\int_{-1}^0(f(x)+1)\,dx=0
\]
with nonnegative integrand, so
\[
f=-1
\]
almost everywhere there.

:::

:::

::: pf-step

Continuity then forces
\[
f(x)=1
\]
for every \(x\in[0,1]\) and
\[
f(x)=-1
\]
for every \(x\in[-1,0]\).


::: pf-proof

A continuous function that equals a constant almost everywhere on an interval equals that constant everywhere. Otherwise, continuity would produce a nonempty open interval on which it differs from the constant, a set of positive measure.

:::

:::

::: pf-step

Step <1>9 is impossible at \(x=0\).


::: pf-proof

It would require simultaneously
\[
f(0)=1
\qquad\text{and}\qquad
f(0)=-1.
\]

:::

:::

::: pf-step

Therefore
\[
\boxed{
2\notin\Lambda(B)}.
\]


::: pf-proof

The assumption that some \(f\in B\) satisfies \(\Lambda(f)=2\) led to the contradiction in step <1>10.

:::

:::

::: pf-step

Likewise,
\[
\boxed{
-2\notin\Lambda(B)}.
\]


::: pf-proof

If \(\Lambda(f)=-2\), then
\[
\Lambda(-f)=2,
\]
and \(-f\in B\), contradicting step <1>11.

:::

:::

::: pf-step

Hence
\[
\boxed{
\Lambda(B)\subseteq(-2,2)}.
\]


::: pf-proof

Step <1>2 gives
\[
|\Lambda(f)|\le2
\]
on \(B\), and steps <1>11--<1>12 exclude the endpoints.

:::

:::

::: pf-step

There exists \(g\in B\) such that
\[
\boxed{
\Lambda(g)>|t|}.
\]


::: pf-proof

Choose \(\varepsilon>0\) so small that
\[
2-\varepsilon>|t|.
\]
Then take
\[
g=f_\varepsilon
\]
from step <1>5.

:::

:::

::: pf-step

Define
\[
h
=
\frac{t}{\Lambda(g)}\,g.
\]


::: pf-proof

Since
\[
\Lambda(g)>|t|\ge0,
\]
the denominator is nonzero.

:::

:::

::: pf-step

One has
\[
\boxed{
h\in B}.
\]


::: pf-proof

Since \(g\in B\),
\[
\|g\|_\infty\le1.
\]
Also
\[
\left|
\frac{t}{\Lambda(g)}
\right|
<1
\]
by step <1>14. Therefore
\[
\|h\|_\infty
<
1.
\]

:::

:::

::: pf-step

One has
\[
\boxed{
\Lambda(h)=t}.
\]


::: pf-proof

By linearity,
\[
\Lambda(h)
=
\frac{t}{\Lambda(g)}
\Lambda(g)
=
t.
\]

:::

:::

::: pf-step

Therefore
\[
\boxed{
(-2,2)\subseteq\Lambda(B)}.
\]


::: pf-proof

The number \(t\in(-2,2)\) was arbitrary, and steps <1>14--<1>17 produce \(h\in B\) with image \(t\).

:::

:::

::: pf-step

Combining the two inclusions,
\[
\boxed{
\Lambda(B)=(-2,2)}.
\]


::: pf-proof

Use steps <1>13 and <1>18.

:::

:::

::: pf-step

Hence \(\Lambda(B)\) is open in \(\mathbb R\).


::: pf-proof

The interval \((-2,2)\) is open.

:::

:::

::: pf-qed

Step <1>20 is the required conclusion.

:::

:::
