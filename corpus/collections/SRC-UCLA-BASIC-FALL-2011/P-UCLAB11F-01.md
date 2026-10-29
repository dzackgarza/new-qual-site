---
schema: qual/card@1
id: P-UCLAB11F-01
kind: problem
title: Fixed point for a strict contraction on a compact metric space
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
  note: Checked against Problem 1 of the retained UCLA Basic Examination, Fall 2011.
---

::: {.problem}
Problem 1. Let $(X,d)$ be a compact metric space and let $f:X\to X$ satisfy
\[
d(f(x),f(y))<d(x,y)\qquad\text{for all }x\ne y.
\]
Prove that there is a unique point $x\in X$ such that $f(x)=x$.
:::

::: {.solution}

Define
\[
h:X\to\RR,
\qquad
h(x)=d(x,f(x)).
\]

::: pf

::: {.pf-step #s1-1}

The map $f$ is continuous.


::: pf-proof

For $x\ne y$,
\[
d(f(x),f(y))<d(x,y),
\]
and for $x=y$ both sides are zero. Hence for all $x,y\in X$,
\[
d(f(x),f(y))\le d(x,y).
\]
Thus $f$ is $1$-Lipschitz, and therefore continuous.

:::

:::

::: {.pf-step #s1-2}

The function $h$ is continuous.


::: pf-proof

The map
\[
x\longmapsto (x,f(x))
\]
from $X$ to $X\times X$ is continuous by step [](#s1-1){.pf-ref}. The metric
\[
d:X\times X\to\RR
\]
is continuous, because
\[
|d(x,y)-d(x',y')|
\le
d(x,x')+d(y,y').
\]
Therefore their composition
\[
h(x)=d(x,f(x))
\]
is continuous.

:::

:::

::: {.pf-step #s1-3}

There exists $x_0\in X$ such that
\[
h(x_0)=\min_{x\in X}h(x).
\]


::: pf-proof

The space $X$ is compact and $h$ is continuous by step [](#s1-2){.pf-ref}. The extreme value theorem therefore gives a minimizer $x_0$.

:::

:::

::: {.pf-step #s1-4}

One has
\[
h(x_0)=0.
\]


::: pf-proof

Suppose instead that
\[
h(x_0)>0.
\]
Then
\[
x_0\ne f(x_0).
\]
Applying the strict contraction hypothesis to the distinct points $x_0$ and $f(x_0)$ gives
\[
d(f(x_0),f(f(x_0)))
<
d(x_0,f(x_0)).
\]
Equivalently,
\[
h(f(x_0))<h(x_0),
\]
contradicting the minimality of $x_0$ from step [](#s1-3){.pf-ref}.
Thus $h(x_0)=0$.

:::

:::

::: {.pf-step #s1-5}

The point $x_0$ is a fixed point of $f$.


::: pf-proof

By step [](#s1-4){.pf-ref},
\[
d(x_0,f(x_0))=0.
\]
Since $d$ is a metric,
\[
\boxed{f(x_0)=x_0}.
\]

:::

:::

::: {.pf-step #s1-6}

The fixed point is unique.


::: pf-proof

Suppose $x$ and $y$ are distinct fixed points. Then
\[
d(x,y)
=
d(f(x),f(y))
<
d(x,y),
\]
an impossibility. Hence no two distinct fixed points exist.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} proves existence, and step [](#s1-6){.pf-ref} proves uniqueness.

:::

:::

:::
