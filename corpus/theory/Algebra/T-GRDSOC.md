---
schema: qual/card@1
id: T-GRDSOC
kind: proposition
title: The top graded piece of a Gorenstein algebra is one-dimensional
slogan: 'In a finite-dimensional graded Gorenstein algebra with R_0 = k, the top degree has dimension one.'
classification:
  areas:
  - algebra
  topics:
  - Gorenstein Rings
  - Graded Rings
relations: []
review: draft
---

::: {.proposition}
Let $k$ be a field and let $R = \bigoplus_{i=0}^{n} R_i$ be a finite-dimensional graded commutative $k$-algebra with $R_0 = k$ and $R_n\neq0$.
If $R$ is [[D-DU4UQ|Gorenstein]], then $\dim_k R_n = 1$.
:::

::: {.proof}
Because $R_0 = k$ and $R$ is finite-dimensional over $k$, the ideal $\mfm\coloneqq\bigoplus_{i\geq1}R_i$ is the unique maximal ideal of $R$, so $R$ is a local ring with residue field $k$, and it is zero-dimensional.

A zero-dimensional Gorenstein local ring has one-dimensional socle $\theset{r\in R \st \mfm r=0}$, as recorded on [[D-SCHCMGOR]].

The top graded piece lies in the socle: $\mfm R_n\subseteq\bigoplus_{i>n}R_i = 0$, so $R_n\subseteq\theset{r\st \mfm r=0}$ and $\dim_k R_n\leq 1$.
Since $R_n\neq0$, $\dim_k R_n = 1$.
:::
