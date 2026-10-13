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

::: {.solution}
Define
\[
\boxed{
\Lambda(f)
=
\int_0^1 f(x)\,dx
-
\int_{-1}^0 f(x)\,dx}.
\]

<1>1. The map
\[
\Lambda:V\to\mathbb R
\]
is linear.

::: {.proof}
Both integrals are linear in \(f\), so their difference is linear.
:::

<1>2. For every \(f\in V\),
\[
\boxed{
|\Lambda(f)|
\le
2\|f\|_\infty}.
\]

::: {.proof}
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

<1>3. Hence \(\Lambda\) is bounded and
\[
\boxed{
\|\Lambda\|\le2}.
\]

::: {.proof}
Step <1>2 is exactly the operator-norm estimate.
:::

We now show that the norm is exactly \(2\), but is not attained on \(B\).

For \(0<\varepsilon<1\), define
\[
f_\varepsilon(x)
=
\begin{cases}
-1,&-1\le x\le-\varepsilon,\\[4pt]
x/\varepsilon,&-\varepsilon\le x\le\varepsilon,\\[4pt]
1,&\varepsilon\le x\le1.
\end{cases}
\]

<1>4. One has
\[
\boxed{
f_\varepsilon\in B}.
\]

::: {.proof}
The function is continuous at \(\pm\varepsilon\), and
\[
|f_\varepsilon(x)|\le1
\]
for all \(x\). Hence
\[
\|f_\varepsilon\|_\infty\le1.
\]
:::

<1>5. One has
\[
\boxed{
\Lambda(f_\varepsilon)=2-\varepsilon}.
\]

::: {.proof}
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

<1>6. Hence
\[
\boxed{
\|\Lambda\|=2}.
\]

::: {.proof}
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

<1>7. Suppose \(f\in B\) and
\[
\Lambda(f)=2.
\]
Then
\[
\boxed{
f(x)=1
\text{ for almost every }x\in[0,1]}.
\]

::: {.proof}
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

<1>8. Under the same assumption,
\[
\boxed{
f(x)=-1
\text{ for almost every }x\in[-1,0]}.
\]

::: {.proof}
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

<1>9. Continuity then forces
\[
f(x)=1
\]
for every \(x\in[0,1]\) and
\[
f(x)=-1
\]
for every \(x\in[-1,0]\).

::: {.proof}
A continuous function that equals a constant almost everywhere on an interval equals that constant everywhere. Otherwise, continuity would produce a nonempty open interval on which it differs from the constant, a set of positive measure.
:::

<1>10. Step <1>9 is impossible at \(x=0\).

::: {.proof}
It would require simultaneously
\[
f(0)=1
\qquad\text{and}\qquad
f(0)=-1.
\]
:::

<1>11. Therefore
\[
\boxed{
2\notin\Lambda(B)}.
\]

::: {.proof}
The assumption that some \(f\in B\) satisfies \(\Lambda(f)=2\) led to the contradiction in step <1>10.
:::

<1>12. Likewise,
\[
\boxed{
-2\notin\Lambda(B)}.
\]

::: {.proof}
If \(\Lambda(f)=-2\), then
\[
\Lambda(-f)=2,
\]
and \(-f\in B\), contradicting step <1>11.
:::

<1>13. Hence
\[
\boxed{
\Lambda(B)\subseteq(-2,2)}.
\]

::: {.proof}
Step <1>2 gives
\[
|\Lambda(f)|\le2
\]
on \(B\), and steps <1>11--<1>12 exclude the endpoints.
:::

Now let
\[
t\in(-2,2).
\]

<1>14. There exists \(g\in B\) such that
\[
\boxed{
\Lambda(g)>|t|}.
\]

::: {.proof}
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

<1>15. Define
\[
h
=
\frac{t}{\Lambda(g)}\,g.
\]

::: {.proof}
Since
\[
\Lambda(g)>|t|\ge0,
\]
the denominator is nonzero.
:::

<1>16. One has
\[
\boxed{
h\in B}.
\]

::: {.proof}
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

<1>17. One has
\[
\boxed{
\Lambda(h)=t}.
\]

::: {.proof}
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

<1>18. Therefore
\[
\boxed{
(-2,2)\subseteq\Lambda(B)}.
\]

::: {.proof}
The number \(t\in(-2,2)\) was arbitrary, and steps <1>14--<1>17 produce \(h\in B\) with image \(t\).
:::

<1>19. Combining the two inclusions,
\[
\boxed{
\Lambda(B)=(-2,2)}.
\]

::: {.proof}
Use steps <1>13 and <1>18.
:::

<1>20. Hence \(\Lambda(B)\) is open in \(\mathbb R\).

::: {.proof}
The interval \((-2,2)\) is open.
:::

<1>21. Q.E.D.

::: {.proof}
Step <1>20 is the required conclusion.
:::
:::
