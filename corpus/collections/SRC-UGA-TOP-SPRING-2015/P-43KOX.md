---
schema: qual/card@1
id: P-43KOX
kind: problem
title: The product of two connected spaces is connected
classification:
  areas:
  - topology
  topics:
  - Connectedness
  - Product Topology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Checked the statement verbatim against problem 1 of the official UGA Spring 2015 topology exam.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Added the empty-product case and verified the common-point union argument for the nonempty case.
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Checked the second appearance against problem 1 of the official UGA Spring 2016 topology exam; it is the same connected-product theorem.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Rechecked the empty-product case and common-point union proof for the Spring 2016 appearance; no mathematical change was needed.
---

::: {.problem}
Prove that the product of two connected topological spaces is connected.
:::

::: {.solution}

::: pf

::: pf-step

If $X\times Y=\emptyset$, then $X\times Y$ is connected.
Henceforth assume $X\times Y\ne\emptyset$ and fix $(a,b)\in X\times Y$.

::: pf-proof

The empty space has no separation into two nonempty disjoint open subsets, so it is connected.
Thus only the nonempty case remains.

:::

:::

::: {.pf-step #s2}

The horizontal slice
\[
X_b=X\times\{b\}
\]
and every vertical slice
\[
Y_x=\{x\}\times Y
\]
are connected.

::: pf-proof

The projection $X_b\to X$ is a homeomorphism, and the projection $Y_x\to Y$ is a homeomorphism.
The spaces $X$ and $Y$ are connected by hypothesis.

:::

:::

::: {.pf-step #s3}

For every $x\in X$, the subspace
\[
T_x=X_b\cup Y_x
\]
is connected.

::: pf-proof

By step [](#s2){.pf-ref}, both $X_b$ and $Y_x$ are connected.
They meet at the point $(x,b)$, so their union is connected.

:::

:::

::: {.pf-step #s4}

The family $\{T_x:x\in X\}$ has a common point.

::: pf-proof

For every $x\in X$, the point $(a,b)$ lies in the horizontal slice $X_b\subseteq T_x$.

:::

:::

::: {.pf-step #s5}

The union of the $T_x$ is all of $X\times Y$.

::: pf-proof

If $(x,y)\in X\times Y$, then $(x,y)\in Y_x\subseteq T_x$.
Hence
\[
X\times Y=\bigcup_{x\in X}T_x.
\]

:::

:::

::: pf-step

$X\times Y$ is connected.

::: pf-proof

By step [](#s3){.pf-ref} each $T_x$ is connected, by step [](#s4){.pf-ref} they share a common point, and by step [](#s5){.pf-ref} their union is $X\times Y$.
A union of connected subspaces with a common point is connected.

:::

:::

:::

![Image](../../assets/figures/2020-01-21-20%3A53.png)
:::
