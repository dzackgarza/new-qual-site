---
schema: qual/card@1
id: P-UCLAB09F-03
kind: problem
title: A multivariable-calculus proof of the arithmetic-geometric mean inequality
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
  note: Checked against Problem 3 of the retained UCLA Basic Examination, Fall 2009.
---
::: {.problem}
Let
\[
f(x_1,\ldots,x_n)=x_1+\cdots+x_n+\frac1{x_1x_2\cdots x_n}
\]
on the positive orthant $\RR_+^n$.

::: pf

::: pf-step

Explain carefully why $f$ attains a global minimum at some $p\in\RR_+^n$.
(Consider what happens as some $x_i\to0$ or $x_i\to\infty$.)

:::

::: pf-step

Find $p$.

:::

::: pf-step

Deduce that if $x_1,\ldots,x_n>0$ and $\prod_i x_i=1$, then

:::

:::

\[
\sum_i x_i\ge n,
\]
with equality if and only if $x_i=1$ for every $i$.
:::

::: {.solution}
Let
\[
P(x_1,\ldots,x_n)=x_1x_2\cdots x_n.
\]

::: pf

::: {.pf-step #p2-s1}

The sublevel set
\[
K=
\left\{
x\in\RR_+^n:
f(x)\le n+1
\right\}
\]
is nonempty and compact.

::: pf-proof

The point
\[
\mathbf1=(1,\ldots,1)
\]
belongs to $K$ because
\[
f(\mathbf1)=n+1.
\]
Thus $K$ is nonempty.

If $x\in K$, then every coordinate is positive and
\[
x_i\le
x_1+\cdots+x_n
\le
f(x)
\le
n+1.
\]
Also
\[
\frac1{P(x)}
\le
n+1,
\]
so
\[
P(x)\ge\frac1{n+1}.
\]
Since every coordinate other than $x_i$ is at most $n+1$,
\[
P(x)
=
x_i\prod_{j\ne i}x_j
\le
x_i(n+1)^{n-1}.
\]
Therefore
\[
x_i\ge\frac1{(n+1)^n}.
\]
Hence
\[
K\subseteq
\left[
\frac1{(n+1)^n},\,n+1
\right]^n.
\]
On this closed box, $f$ is continuous. Thus
\[
K=f^{-1}((-\infty,n+1])
\]
relative to the box is closed. Hence $K$ is a closed subset of a compact box, so it is compact.

:::

:::

::: {.pf-step #p2-s2}

The function $f$ attains a global minimum at some point
\[
p\in\RR_+^n.
\]

::: pf-proof

By step [](#p2-s1){.pf-ref}, the continuous function $f$ attains a minimum on the compact nonempty set $K$.
Outside $K$ one has
\[
f(x)>n+1=f(\mathbf1).
\]
Since $\mathbf1\in K$, no point outside $K$ can have smaller value than the minimum on $K$. Therefore the minimum on $K$ is the global minimum on $\RR_+^n$.

:::

:::

::: {.pf-step #p2-s3}

At every global minimizer $p=(p_1,\ldots,p_n)$,
\[
\frac{\partial f}{\partial x_i}(p)=0
\]
for each $i$.

::: pf-proof

The positive orthant $\RR_+^n$ is open. Hence a global minimizer $p$ is an interior point of the domain. Since $f$ is differentiable, the gradient must vanish at an interior local minimum.

:::

:::

::: {.pf-step #p2-s4}

For each $i$,
\[
\frac{\partial f}{\partial x_i}(x)
=
1-\frac1{x_iP(x)}.
\]

::: pf-proof

The derivative of the linear term $x_i$ is $1$. Since
\[
\frac1{P(x)}
=
\frac1{x_i}
\prod_{j\ne i}\frac1{x_j},
\]
differentiating with respect to $x_i$ gives
\[
-\frac1{x_i^2}
\prod_{j\ne i}\frac1{x_j}
=
-\frac1{x_iP(x)}.
\]
Adding the two contributions yields the formula.

:::

:::

::: {.pf-step #p2-s5}

Every critical point of $f$ in $\RR_+^n$ equals
\[
\boxed{(1,\ldots,1)}.
\]

::: pf-proof

At a critical point, step [](#p2-s4){.pf-ref} gives
\[
x_iP(x)=1
\]
for every $i$. Hence
\[
x_1=x_2=\cdots=x_n=:c.
\]
Then
\[
P(x)=c^n,
\]
and the equation $x_iP(x)=1$ becomes
\[
c^{n+1}=1.
\]
Since $c>0$,
\[
c=1.
\]
Thus the only critical point is $\mathbf1=(1,\ldots,1)$.

:::

:::

::: {.pf-step #p2-s6}

The global minimizer is
\[
\boxed{p=(1,\ldots,1)}
\]
and the minimum value is
\[
\boxed{f(p)=n+1}.
\]

::: pf-proof

By steps [](#p2-s2){.pf-ref} and [](#p2-s3){.pf-ref}, every global minimizer is a critical point. Step [](#p2-s5){.pf-ref} shows that the only critical point is $\mathbf1$. Therefore it is the unique global minimizer. Direct substitution gives
\[
f(\mathbf1)=n+\frac1{1}=n+1.
\]

:::

:::

::: {.pf-step #p2-s7}

If $x_1,\ldots,x_n>0$ and
\[
\prod_{i=1}^n x_i=1,
\]
then
\[
\boxed{\sum_{i=1}^n x_i\ge n}.
\]

::: pf-proof

Under the product condition,
\[
f(x_1,\ldots,x_n)
=
\sum_{i=1}^n x_i+1.
\]
By step [](#p2-s6){.pf-ref},
\[
f(x)\ge n+1.
\]
Therefore
\[
\sum_{i=1}^n x_i+1\ge n+1,
\]
which gives the stated inequality.

:::

:::

::: {.pf-step #p2-s8}

Equality in step [](#p2-s7){.pf-ref} holds if and only if
\[
x_1=\cdots=x_n=1.
\]

::: pf-proof

Equality
\[
\sum_i x_i=n
\]
under the product condition is equivalent to
\[
f(x)=n+1.
\]
By step [](#p2-s6){.pf-ref}, the global minimum $n+1$ is attained only at
\[
\mathbf1=(1,\ldots,1).
\]
Conversely, at $\mathbf1$ the product is $1$ and the sum is $n$.

:::

:::

::: pf-qed

Steps [](#p2-s1){.pf-ref} and [](#p2-s2){.pf-ref} prove existence of a global minimizer, steps [](#p2-s3){.pf-ref}, [](#p2-s4){.pf-ref}, [](#p2-s5){.pf-ref} and [](#p2-s6){.pf-ref} identify it, and steps [](#p2-s7){.pf-ref} and [](#p2-s8){.pf-ref} prove the stated arithmetic-geometric mean inequality and its equality condition.

:::

:::

:::
