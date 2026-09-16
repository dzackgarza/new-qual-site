---
schema: qual/card@1
id: FD-CVEAI
kind: definition
title: Rank of a free module
prompts:
- What is the rank of a free module?
classification:
  areas:
  - algebra
  topics:
  - Free Modules
  - Bases
relations: []
review: draft
---

::: {.definition}
Let $R$ be a nonzero commutative [[D-GURUB|ring]] and $M$ a [[D-LIEMF|free]] $R$-module.
The \dfn{rank} of $M$ is the cardinality of a basis of $M$.
:::

::: {.proposition}
Let $R$ be a nonzero commutative ring and $M$ a free $R$-module.
Any two bases of $M$ have the same cardinality.
:::

::: {.proof}
Since $R\neq0$, $R$ has a [[D-7XH2R|maximal ideal]] $\mfm$, and $k\coloneqq R/\mfm$ is a field.
If $(e_i)_{i\in I}$ is a basis of $M$, then $M\cong R^{(I)}$, so $M/\mfm M\cong (R/\mfm)^{(I)}$ and the images of the $e_i$ form a basis of the $k$-vector space $M/\mfm M$.
Hence $\abs{I}=\dim_k M/\mfm M$, which does not depend on the basis.
:::

::: {.remark}
If $R$ is an [[D-QJ3QL|integral domain]], the rank of $M$ is the supremum of the cardinalities of $R$-linearly independent families in $M$.
With $K$ the field of fractions of $R$ and $(e_i)_{i\in I}$ a basis, $M\cong R^{(I)}\subseteq K^{(I)}$; a family that is $R$-linearly independent in $R^{(I)}$ is $K$-linearly independent in $K^{(I)}$, after clearing denominators in a $K$-linear relation, so it has at most $\abs{I}$ elements, and the basis itself is an independent family of cardinality $\abs{I}$.
:::
