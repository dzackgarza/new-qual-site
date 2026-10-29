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
Let $f : [ 0 , 1 ] \to \RR$ be continuous and suppose that f is differentiable on (0, 1) with $f ( 0 ) = 1 , f ( 1 ) = 0$ . Which of the following are necessarily true?

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

::: pf

::: pf-step

The function \(g\) is continuous on \([0,1]\).


::: pf-proof

The function \(f\) is continuous, and \(x\mapsto x\) is continuous. Their
difference is continuous.

:::

:::

::: {.pf-step #s1-2}

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

::: {.pf-step #s1-3}

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

Steps [](#s1-2){.pf-ref} through [](#s1-3){.pf-ref} show that the continuous function \(g\) changes sign on
\([0,1]\).

:::

:::

::: {.pf-step #s1-5}

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

::: {.pf-step #s1-6}

Hence statement (a) is necessarily true.


::: pf-proof

This is step [](#s1-5){.pf-ref}.

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

::: {.pf-step #s1-9}

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

::: {.pf-step #s1-10}

Hence statement (b) is necessarily true.


::: pf-proof

This is step [](#s1-9){.pf-ref}.

:::

:::

::: {.pf-step #s1-11}

The function \(h\) is continuous on \([0,1]\) and differentiable on
\((0,1)\).


::: pf-proof

It is a sum of elementary smooth functions.

:::

:::

::: {.pf-step #s1-12}

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

::: {.pf-step #s1-13}

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

::: {.pf-step #s1-14}

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

::: {.pf-step #s1-15}

Therefore statement (c) is not necessarily true.


::: pf-proof

The function \(h\) satisfies all hypotheses by steps [](#s1-11){.pf-ref} through [](#s1-13){.pf-ref} but
violates the proposed positivity by step [](#s1-14){.pf-ref}.

:::

:::

::: {.pf-step #s1-16}

Thus the statements that are necessarily true are
\[
\boxed{\text{(a) and (b) only}.}
\]


::: pf-proof

Statement (a) is step [](#s1-6){.pf-ref}, statement (b) is step [](#s1-10){.pf-ref}, and statement (c)
is disproved in step [](#s1-15){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-16){.pf-ref} gives the required answer.

:::

:::

:::
