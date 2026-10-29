---
schema: qual/card@1
id: P-OLLG3
kind: problem
title: Elementary matrices preserve solutions of $Ax=b$
classification:
  areas:
  - algebra
  topics:
  - Linear Algebra
  - Matrices
relations: []
review: draft
---

::: {.problem}
Let $A\in M_{m\times n}(F)$ and $b\in F^m$. Show that applying the same sequence of elementary row operations to $A$ and $b$ does not change the solution set of
$$
Ax=b.
$$
:::

::: {.solution}
Let $E_1,\ldots,E_k$ be the elementary matrices of the row operations, in order, and set
$$
E\coloneqq E_k\cdots E_1,\qquad A'\coloneqq EA,\qquad b'\coloneqq Eb.
$$

::: pf

::: {.pf-step #invertible}

$E$ is invertible.

::: pf-proof

Each elementary matrix is invertible, its inverse being the elementary matrix of the inverse row operation, and a product of invertible matrices is invertible.

:::

:::

::: pf-step

For every $x\in F^n$, $Ax=b$ if and only if $A'x=b'$.

::: pf-proof

If $Ax=b$, then multiplying by $E$ gives $A'x=EAx=Eb=b'$. Conversely, if $A'x=b'$, then multiplying by $E^{-1}$, which exists by step [](#invertible){.pf-ref}, gives $Ax=b$.

:::

:::

:::

:::
