---
schema: qual/card@1
id: P-PC6ZW
kind: problem
title: A finite free module remains free of the same rank after reducing modulo an
  ideal
classification:
  areas:
  - algebra
  topics:
  - Free Modules
  - Bases
  - Tensor Products
relations: []
review: draft
---

::: {.problem}
Let $R$ be a commutative ring with 1.
Suppose that $M$ is a free $R\dash$module with a finite basis $X$.

a.
Let $I \normal R$ be a proper ideal.
Prove that $M/IM$ is a free $R/I\dash$module with basis $X'$, where $X'$ is the image of $X$ under the canonical map $M\to M/IM$.

b.
Prove that any two bases of $M$ have the same number of elements.
You may assume that the result is true when $R$ is a field.

:::


::: {.solution}

Write $X=\{x_1,\ldots,x_n\}$ and $\bar m$ for the image of $m\in M$ in $M/IM$.

::: pf

::: {.pf-step #module}

$M/IM$ is an $R/I$-module, with $(r+I)\bar m=\overline{rm}$.

::: pf-proof

If $r-r'\in I$, then $rm-r'm\in IM$, so the action is well defined. The module axioms follow from those of $M$.

:::

:::

::: {.pf-step #span}

$X'=\{\bar x_1,\ldots,\bar x_n\}$ spans $M/IM$ over $R/I$.

::: pf-proof

Every $m\in M$ is $\sum_ir_ix_i$, so $\bar m=\sum_i(r_i+I)\bar x_i$.

:::

:::

::: {.pf-step #indep}

$X'$ is linearly independent over $R/I$, and the $\bar x_i$ are distinct.

::: pf-proof

Suppose $\sum_i(r_i+I)\bar x_i=0$, so $\sum_ir_ix_i\in IM$. Every element of $IM$ is a finite sum $\sum_k a_km_k$ with $a_k\in I$; expanding each $m_k$ in the basis $X$ writes it as $\sum_is_ix_i$ with all $s_i\in I$. Since $X$ is a basis of $M$, comparing coefficients gives $r_i=s_i\in I$, so $r_i+I=0$ for all $i$. If $\bar x_i=\bar x_j$ with $i\neq j$, then $1\cdot\bar x_i-1\cdot\bar x_j=0$ and independence gives $1\in I$, contradicting that $I$ is proper.

:::

:::

::: {.pf-step #rank}

Any two bases of $M$ have the same number of elements.

::: pf-proof

If $R=0$, then $M=0$ and every basis is empty. Otherwise choose a maximal ideal $\mathfrak m$ of $R$, so $k=R/\mathfrak m$ is a field. Let $Y$ be a basis of $M$. Then $\cardinality{Y}$ is finite: the finitely many elements of $X$ are combinations of finitely many elements of $Y$, so a finite subset of $Y$ spans $M$, and a basis has no proper spanning subset. Steps [](#span){.pf-ref} and [](#indep){.pf-ref} with $I=\mathfrak m$ show that $M/\mathfrak mM$ is a $k$-vector space with bases of $\cardinality{X}$ and of $\cardinality{Y}$ elements. By the result for fields, $\cardinality{X}=\cardinality{Y}$.

:::

:::

::: pf-qed

Steps [](#module){.pf-ref}, [](#span){.pf-ref} and [](#indep){.pf-ref} prove part (a), and Step [](#rank){.pf-ref} proves part (b).

:::

:::

:::
