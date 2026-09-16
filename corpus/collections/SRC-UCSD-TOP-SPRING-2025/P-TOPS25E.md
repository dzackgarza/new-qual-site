---
schema: qual/card@1
id: P-TOPS25E
kind: problem
title: Cohomology of $S^2 \times S^3$ versus $S^2 \vee S^3 \vee S^5$
classification:
  areas:
  - topology
  topics:
  - Cohomology
  - Higher Homotopy Groups
relations: []
review: draft
---

::: {.problem}
Let $X = S^2 \times S^3$ and let $Y = S^2 \vee S^3 \vee S^5$.
Explain why the spaces have isomorphic integral cohomology groups in each degree.
Is $X$ homotopy-equivalent to $Y$?
:::

::: {.solution}
<1>1. Both $X=S^2\times S^3$ and $Y=S^2\vee S^3\vee S^5$ have integral cohomology groups
$$H^k\cong\begin{cases}\mathbb Z,&k=0,2,3,5,\\0,&\text{otherwise.}\end{cases}$$
::: {.proof}
For $X$, use Künneth. For $Y$, reduced cohomology of a finite wedge is the direct sum of the reduced cohomologies of its summands.
:::

<1>2. They are not homotopy equivalent.
::: {.proof}
Let $a\in H^2(X)$ and $b\in H^3(X)$ be the factor generators. Then $a\smile b$ generates $H^5(X)$. In a wedge, every product between positive-degree classes supported on distinct wedge summands is zero, and the individual sphere summands have no nontrivial positive-degree products. Thus all positive-degree cup products in $H^*(Y)$ vanish. The cohomology rings are not isomorphic, so no homotopy equivalence exists.
:::
:::
