---
schema: qual/card@1
id: P-OQCJR
kind: problem
title: $Ax=0$ has a nontrivial solution iff $\rank(A)<m$
classification:
  areas:
  - algebra
  topics:
  - Rank and Nullity
  - Linear Algebra
  - Matrices
relations: []
review: draft
---

::: {.problem}
Let $A\in M_{m\times n}(F)$. Prove that the homogeneous system
$$
Ax=0
$$
has a nonzero solution if and only if
$$
\rank(A)<n.
$$
:::

::: {.solution}
Regard $A$ as the linear map $F^n\to F^m$, $x\mapsto Ax$; its nonzero kernel vectors are exactly the nonzero solutions of $Ax=0$.

::: pf

::: {.pf-step #rank-nullity}

$n=\dim\ker A+\rank(A)$.

::: pf-proof

This is the rank-nullity theorem for $A\colon F^n\to F^m$.

:::

:::

::: pf-step

$\ker A\ne0$ if and only if $\rank(A)<n$.

::: pf-proof

$\ker A\ne0$ if and only if $\dim\ker A>0$, which by step [](#rank-nullity){.pf-ref} holds if and only if $\rank(A)<n$.

:::

:::

:::

:::
