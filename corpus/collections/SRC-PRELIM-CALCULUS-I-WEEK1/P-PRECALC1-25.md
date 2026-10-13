---
schema: qual/card@1
id: P-PRECALC1-25
kind: problem
title: Intermediate and mean value theorems for $f$ with $f(0)=1$ and $f(1)=0$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
Let $f : [ 0 , 1 ] \to \mathbb { R }$ be continuous and suppose that f is differentiable on (0, 1) with $f ( 0 ) = 1 , f ( 1 ) = 0$ . Which of the following are necessarily true?

(a) There is $x \in ( 0 , 1 )$ such that $f ( x ) = x$

(b) There is $x \in ( 0 , 1 )$ such that $f ^ { \prime } ( x ) = - 1$

(c) $f ( x ) > 0$ for all $x \in [ 0 , 1 )$
:::

::: {.solution}
## Statement (a)

Define
\[
g(x)=f(x)-x.
\]

<1>1. The function \(g\) is continuous on \([0,1]\).

::: {.proof}
The function \(f\) is continuous, and \(x\mapsto x\) is continuous. Their
difference is continuous.
:::

<1>2. One has
\[
\boxed{
g(0)=1}.
\]

::: {.proof}
\[
g(0)
=
f(0)-0
=
1.
\]
:::

<1>3. One has
\[
\boxed{
g(1)=-1}.
\]

::: {.proof}
\[
g(1)
=
f(1)-1
=
-1.
\]
:::

<1>4. By the intermediate value theorem, there exists
\[
c\in(0,1)
\]
such that
\[
g(c)=0.
\]

::: {.proof}
Steps <1>2--<1>3 show that the continuous function \(g\) changes sign on
\([0,1]\).
:::

<1>5. Therefore
\[
\boxed{
f(c)=c}.
\]

::: {.proof}
The equation
\[
g(c)=0
\]
means
\[
f(c)-c=0.
\]
:::

<1>6. Hence statement (a) is necessarily true.

::: {.proof}
This is step <1>5.
:::

## Statement (b)

<1>7. The mean value theorem applies to \(f\) on \([0,1]\).

::: {.proof}
The function is continuous on the closed interval and differentiable on the
open interval by hypothesis.
:::

<1>8. Therefore there exists
\[
c\in(0,1)
\]
such that
\[
f'(c)
=
\frac{f(1)-f(0)}{1-0}.
\]

::: {.proof}
This is the mean value theorem.
:::

<1>9. Using the endpoint values,
\[
\boxed{
f'(c)=-1}.
\]

::: {.proof}
\[
\frac{f(1)-f(0)}{1}
=
0-1
=
-1.
\]
:::

<1>10. Hence statement (b) is necessarily true.

::: {.proof}
This is step <1>9.
:::

## Statement (c)

Define
\[
h(x)
=
1-x-2\sin(\pi x).
\]

<1>11. The function \(h\) is continuous on \([0,1]\) and differentiable on
\((0,1)\).

::: {.proof}
It is a sum of elementary smooth functions.
:::

<1>12. One has
\[
\boxed{
h(0)=1}.
\]

::: {.proof}
\[
h(0)
=
1-0-2\sin0
=
1.
\]
:::

<1>13. One has
\[
\boxed{
h(1)=0}.
\]

::: {.proof}
\[
h(1)
=
1-1-2\sin\pi
=
0.
\]
:::

<1>14. But
\[
\boxed{
h(1/2)
=
-\frac32<0}.
\]

::: {.proof}
\[
\begin{aligned}
h(1/2)
&=
1-\frac12-2\sin\frac{\pi}{2}\\
&=
\frac12-2\\
&=
-\frac32.
\end{aligned}
\]
:::

<1>15. Therefore statement (c) is not necessarily true.

::: {.proof}
The function \(h\) satisfies all hypotheses by steps <1>11--<1>13 but
violates the proposed positivity by step <1>14.
:::

<1>16. Thus the statements that are necessarily true are
\[
\boxed{\text{(a) and (b) only}.}
\]

::: {.proof}
Statement (a) is step <1>6, statement (b) is step <1>10, and statement (c)
is disproved in step <1>15.
:::

<1>17. Q.E.D.

::: {.proof}
Step <1>16 gives the required answer.
:::
:::
