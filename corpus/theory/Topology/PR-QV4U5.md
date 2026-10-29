---
schema: qual/card@1
id: PR-QV4U5
kind: proposition
title: Inclusion-exclusion for Euler characteristic
slogan: 'Euler characteristic obeys inclusion-exclusion for finite CW subcomplexes.'
classification:
  areas:
  - topology
  topics:
  - Euler Characteristic
  - Mayer-Vietoris
relations: []
review: draft
---

::: {.proposition}
Let $X$ be a finite CW complex and $U, V\subseteq X$ subcomplexes with $X = U\cup V$.
Then
$$
\chi(X) = \chi(U) + \chi(V) - \chi (U\cap V)
.$$
:::

For a finite CW complex $Y$, write $c_n(Y)$ for the number of $n$-cells of $Y$, so that $\chi(Y) = \sum_{n\geq0}(-1)^n c_n(Y)$ by the definition of the [[D-QK5BM|Euler characteristic]] [@Hat02].

::: pf

::: {.pf-step #cells-intersection}
$U\cap V$ is a subcomplex of $X$ whose $n$-cells are exactly the $n$-cells of $X$ that lie in both $U$ and $V$.

::: pf-proof
A subcomplex is a closed subspace that is a union of cells of $X$.
The intersection of two closed subspaces is closed.
Because the open cells of $X$ are pairwise disjoint, an open cell lies in $U\cap V$ exactly when it lies in $U$ and in $V$, and every point of $U\cap V$ lies in such a cell.
So $U\cap V$ is a closed union of cells, that is, a subcomplex with the stated cells.
:::

:::

::: {.pf-step #cell-count}
For each $n$, $c_n(X) = c_n(U) + c_n(V) - c_n(U\cap V)$.

::: pf-proof
An open cell of $X$ that meets a subcomplex lies in that subcomplex, because a subcomplex is a union of cells and the open cells are pairwise disjoint.
Every $n$-cell of $X$ meets $X = U\cup V$, so it is an $n$-cell of $U$ or of $V$.
Inclusion--exclusion for these finite sets of $n$-cells, with their intersection identified in step [](#cells-intersection){.pf-ref}, gives the count.
:::

:::

::: pf-step
$\chi(X) = \chi(U) + \chi(V) - \chi(U\cap V)$.

::: pf-proof
Multiply the identity of step [](#cell-count){.pf-ref} by $(-1)^n$ and sum over $n$.
:::

:::

:::
