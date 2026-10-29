---
schema: qual/card@1
id: D-2IO6Q
kind: definition
title: Jacobson radical
classification:
  areas:
  - algebra
  topics:
  - Jacobson Radical
  - Ideals
  - Commutative Algebra
relations: []
review: draft
---

::: {.definition}
Let $R$ be a commutative ring.
The \dfn{Jacobson radical} of $R$ is the intersection of all [[D-7XH2R|maximal ideals]] of $R$:
$$
\jacobsonrad{R} \coloneqq \Intersect_{\mfm \in \mspec R} \mfm,
$$
where $\mspec R$ is the [[D-NX4KW|max spectrum]] of $R$.
:::

::: {.remark}
For a ring $R$ with identity that need not be commutative, $\jacobsonrad{R}$ is the intersection of the maximal left ideals of $R$. It is a two-sided ideal, it equals the intersection of the maximal right ideals, and for commutative $R$ it is the ideal defined above.
:::
