---
schema: qual/card@1
id: P-SHNTG
kind: problem
title: Definition of an ideal, the join $I\vee J$, the product $IJ\subseteq I\cap
  J$, and whether every ideal contained in $I$ and $J$ lies in $IJ$
classification:
  areas:
  - prelim
  topics:
  - Ideals
  - Rings
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---
::: {.problem}
Let $R$ be a ring (with unit).

(a) What is an ideal of $R$?

(b) If $I$ and $J$ are ideals of $R$, prove that there is a least (with respect to inclusion) ideal of $R$ that contains both $I$ and $J$ as subsets.
This new ideal is called the join of $I$ with $J$: $I \vee J$.

(c) If $I$ and $J$ are ideals of $R$, let $$IJ = \left\{\sum_{i=1}^n x_i y_i : n > 0, x_1,\dots,x_n \in I, \text{ and } y_1,\dots,y_n \in J\right\}.$$ Show that $IJ$ is an ideal of $R$ that is contained in both $I$ and $J$.
If $K$ is any ideal of $R$ that is contained in both $I$ and $J$, must $K$ be contained in $IJ$?
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

An ideal of $R$ is an additive subgroup $I\le (R,+)$ such that
$$
rI\subseteq I
\qquad\text{and}\qquad
Ir\subseteq I
$$
for every $r\in R$.

::: pf-proof

Equivalently, a subset $I\subseteq R$ is a two-sided ideal when
$0\in I$, $x-y\in I$ for all $x,y\in I$, and
$rx,xr\in I$ for all $r\in R$ and $x\in I$. This is the definition
required in part (a).

:::

:::

::: {.pf-step #s2}

For ideals $I,J\subseteq R$, the join exists and is
$$
I\vee J=I+J
=\{x+y:x\in I, y\in J\}.
$$

::: pf-proof

First, $I+J$ is an additive subgroup: $0=0+0$ lies in it, and
$$
(x_1+y_1)-(x_2+y_2)
=(x_1-x_2)+(y_1-y_2)\in I+J.
$$
For $r\in R$,
$$
r(x+y)=rx+ry\in I+J,
\qquad
(x+y)r=xr+yr\in I+J,
$$
so $I+J$ is an ideal.

Moreover, $x=x+0\in I+J$ for every $x\in I$, and similarly
$J\subseteq I+J$. If $M$ is any ideal containing both $I$ and $J$, then
$x+y\in M$ whenever $x\in I$ and $y\in J$, so $I+J\subseteq M$.
Thus $I+J$ is the least ideal containing both $I$ and $J$.

:::

:::

::: {.pf-step #s3}

The set
$$
IJ=
\left\{
\sum_{i=1}^n x_i y_i:
n>0, x_i\in I, y_i\in J
\right\}
$$
is an ideal of $R$.

::: pf-proof

The zero element lies in $IJ$, for example as $0\cdot0$. If
$$
u=\sum_{i=1}^m x_i y_i,
\qquad
v=\sum_{j=1}^n x'_j y'_j,
$$
then
$$
u-v
=\sum_{i=1}^m x_i y_i
+\sum_{j=1}^n (-x'_j)y'_j\in IJ,
$$
because $-x'_j\in I$. Hence $IJ$ is an additive subgroup.

For $r\in R$,
$$
ru=\sum_{i=1}^m (rx_i)y_i\in IJ
$$
because $rx_i\in I$, and
$$
ur=\sum_{i=1}^m x_i(y_ir)\in IJ
$$
because $y_ir\in J$. Therefore $IJ$ is a two-sided ideal.

:::

:::

::: {.pf-step #s4}

One has
$$
IJ\subseteq I\cap J.
$$

::: pf-proof

For each product $x_iy_i$ with $x_i\in I$ and $y_i\in J$, ideal
absorption gives
$$
x_iy_i\in I
\qquad\text{and}\qquad
x_iy_i\in J.
$$
Both $I$ and $J$ are additively closed, so every finite sum defining an
element of $IJ$ lies in both ideals.

:::

:::

::: {.pf-step #s5}

It is false in general that every ideal
$K\subseteq I\cap J$ must satisfy $K\subseteq IJ$.

::: pf-proof

Take
$$
R=\ZZ,
\qquad
I=J=2\ZZ,
\qquad
K=2\ZZ.
$$
Then $K\subseteq I$ and $K\subseteq J$, while
$$
IJ=(2\ZZ)(2\ZZ)=4\ZZ.
$$
Since $2\in K$ but $2\notin4\ZZ$, one has
$K\nsubseteq IJ$.

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} answers part (a), step [](#s2){.pf-ref} proves part (b), and
steps [](#s3){.pf-ref}, [](#s4){.pf-ref} and [](#s5){.pf-ref} prove all assertions in part (c).

:::

:::

:::
