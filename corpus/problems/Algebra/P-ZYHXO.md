---
schema: qual/card@1
id: P-ZYHXO
kind: problem
title: Algebraically closed field
classification:
  areas:
  - algebra
  topics:
  - Fields
  - Field Extensions
relations: []
review: draft
---

::: {.problem}
What does it mean to be algebraically closed?
:::

::: {.solution}
Let $K$ be a field.

::: pf

::: pf-step

$K$ is algebraically closed if every nonconstant polynomial $f\in K[x]$ has a root in $K$.

:::

::: pf-step

Equivalently, every nonconstant $f\in K[x]$ splits into linear factors over $K$, and equivalently, the only algebraic extension of $K$ is $K$ itself.

::: pf-proof

If every nonconstant polynomial has a root, then by induction on degree, dividing off a linear factor $x-a$ at each stage, every nonconstant polynomial splits. If every polynomial splits and $L/K$ is algebraic, then the minimal polynomial over $K$ of each $\alpha\in L$ is irreducible and splits, so it is linear and $\alpha\in K$. If $K$ has no proper algebraic extension and $f$ is nonconstant, then for an irreducible factor $g$ of $f$, the field $K[x]/(g)$ is an algebraic extension of degree $\deg g$, so $\deg g=1$ and $f$ has a root in $K$.

:::

:::

:::

:::
