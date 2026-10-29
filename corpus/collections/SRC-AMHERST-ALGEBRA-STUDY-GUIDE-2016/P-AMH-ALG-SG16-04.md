---
schema: qual/card@1
id: P-AMH-ALG-SG16-04
kind: problem
title: Intersections of normal subgroups are normal
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored Amherst College Study Guide for Algebra (September 2016).
---

::: {.problem}
Let $G$ be a group, and let $H,K\subseteq G$ be normal subgroups of $G$.
Prove that $H\cap K$ is a normal subgroup of $G$.
You may assume without proof that $H\cap K$ is a subgroup.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}
The intersection $H\cap K$ is invariant under conjugation by every element of $G$.

::: pf-proof
Let
$$
a\in H\cap K
$$
and let $g\in G$. Since $H\trianglelefteq G$ and $a\in H$,
$$
gag^{-1}\in H.
$$
Likewise, since $K\trianglelefteq G$ and $a\in K$,
$$
gag^{-1}\in K.
$$
Therefore
$$
gag^{-1}\in H\cap K.
$$
:::

:::

::: pf-step
Therefore
$$
\boxed{H\cap K\trianglelefteq G}.
$$

::: pf-proof
By hypothesis, $H\cap K$ is already a subgroup of $G$. Step [](#s1-1){.pf-ref} shows it is invariant under conjugation by every element of $G$, which is exactly normality.
:::

:::

:::

:::
