---
schema: qual/card@1
id: D-R4ZCL
kind: definition
title: Smash product
classification:
  areas:
  - topology
  topics:
  - Cell Complexes
  - Homotopy
  - Quotient Spaces
relations: []
review: draft
---

::: {.definition}
Let $(X,x_0)$ and $(Y,y_0)$ be based spaces.
Identify the [[D-IGUUS|wedge sum]] $X\vee Y$ with the subspace $X\times\ts{y_0}\cup\ts{x_0}\times Y$ of $X\times Y$.
The \dfn{smash product} is the quotient space
$$
X\wedge Y\coloneqq(X\times Y)/(X\vee Y),
$$
based at the image of $X\vee Y$ [@Hat02].
:::

::: {.proposition}
For $m,n\geq0$ there is a homeomorphism $S^m\wedge S^n\cong S^{m+n}$, and for a based space $X$ the reduced suspension satisfies $\Sigma X\cong S^1\wedge X$ [@Hat02].
:::
