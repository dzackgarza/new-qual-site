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

## Statement (a)

Define
\[
g(x)=f(x)-x.
\]

::: pf

::: pf-step

The function \(g\) is continuous on \([0,1]\).


::: pf-proof

The function \(f\) is continuous, and \(x\mapsto x\) is continuous. Their
difference is continuous.

:::

:::

::: pf-step

One has
\[
\boxed{
g(0)=1}.
\]


::: pf-proof

\[
g(0)
=
f(0)-0
=
1.
\]

:::

:::

::: pf-step

One has
\[
\boxed{
g(1)=-1}.
\]


::: pf-proof

\[
g(1)
=
f(1)-1
=
-1.
\]

:::

:::

::: pf-step

By the intermediate value theorem, there exists
\[
c\in(0,1)
\]
such that
\[
g(c)=0.
\]


::: pf-proof

Steps <1>2--<1>3 show that the continuous function \(g\) changes sign on
\([0,1]\).

:::

:::

::: pf-step

Therefore
\[
\boxed{
f(c)=c}.
\]


::: pf-proof

The equation
\[
g(c)=0
\]
means
\[
f(c)-c=0.
\]

:::

:::

::: pf-step

Hence statement (a) is necessarily true.


::: pf-proof

This is step <1>5.

:::

:::

::: pf-step

The mean value theorem applies to \(f\) on \([0,1]\).


::: pf-proof

The function is continuous on the closed interval and differentiable on the
open interval by hypothesis.

:::

:::

::: pf-step

Therefore there exists
\[
c\in(0,1)
\]
such that
\[
f'(c)
=
\frac{f(1)-f(0)}{1-0}.
\]


::: pf-proof

This is the mean value theorem.

:::

:::

::: pf-step

Using the endpoint values,
\[
\boxed{
f'(c)=-1}.
\]


::: pf-proof

\[
\frac{f(1)-f(0)}{1}
=
0-1
=
-1.
\]

:::

:::

::: pf-step

Hence statement (b) is necessarily true.


::: pf-proof

This is step <1>9.

:::

:::

::: pf-step

The function \(h\) is continuous on \([0,1]\) and differentiable on
\((0,1)\).


::: pf-proof

It is a sum of elementary smooth functions.

:::

:::

::: pf-step

One has
\[
\boxed{
h(0)=1}.
\]


::: pf-proof

\[
h(0)
=
1-0-2\sin0
=
1.
\]

:::

:::

::: pf-step

One has
\[
\boxed{
h(1)=0}.
\]


::: pf-proof

\[
h(1)
=
1-1-2\sin\pi
=
0.
\]

:::

:::

::: pf-step

But
\[
\boxed{
h(1/2)
=
-\frac32<0}.
\]


::: pf-proof

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

:::

::: pf-step

Therefore statement (c) is not necessarily true.


::: pf-proof

The function \(h\) satisfies all hypotheses by steps <1>11--<1>13 but
violates the proposed positivity by step <1>14.

:::

:::

::: pf-step

Thus the statements that are necessarily true are
\[
\boxed{\text{(a) and (b) only}.}
\]


::: pf-proof

Statement (a) is step <1>6, statement (b) is step <1>10, and statement (c)
is disproved in step <1>15.

:::

:::

::: pf-qed

Step <1>16 gives the required answer.

:::

:::
