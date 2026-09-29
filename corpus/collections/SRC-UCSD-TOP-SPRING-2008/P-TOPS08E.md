---
schema: qual/card@1
id: P-TOPS08E
kind: problem
title: "Every compact oriented n-manifold admits a degree-one map to S^n"
classification:
  areas:
  - topology
  topics:
  - Degree
  - Manifolds
relations: []
review: draft
---

::: {.problem}
Given a compact, oriented, boundaryless $n$-manifold $M^n$, show that there always exists a continuous map $f : M^n \to S^n$, such that $f_*([M]) = [S^n]$.
:::

::: {.solution}

::: pf

::: pf-step

Choose an orientation-preserving embedded closed $n$-disk $D\subset M$.

::: pf-proof

Take a sufficiently small closed coordinate ball inside an oriented chart of $M$.

:::

:::

::: pf-step

Collapse the complement of the interior of $D$ to a point:
$$
q:M\longrightarrow M/(M-\operatorname{int}D).
$$
The quotient is homeomorphic to $D/\partial D\cong S^n$.

::: pf-proof

All of $M-\operatorname{int}D$ is collapsed, and its intersection with $D$ is exactly $\partial D$. Thus the quotient is obtained from $D$ by collapsing its boundary to a point, which is $S^n$.

:::

:::

::: {.pf-step #s3}

The map $q$ has degree $1$.

::: pf-proof

Choose a point $y$ in the image of the interior of $D$. It has exactly one preimage, lying in $\operatorname{int}D$, and near that point $q$ is the chosen orientation-preserving chart homeomorphism. Hence its local degree is $+1$, so the global degree is $1$.

:::

:::

::: pf-step

Therefore
$$
\boxed{q_*[M]=[S^n].}
$$

::: pf-proof

This is the definition of degree applied to step [](#s3){.pf-ref}.

:::

:::

:::

:::
