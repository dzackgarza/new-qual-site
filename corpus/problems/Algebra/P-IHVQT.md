---
schema: qual/card@1
id: P-IHVQT
kind: problem
title: Tensor product
classification:
  areas:
  - algebra
  topics:
  - Tensor Products
  - Vector Spaces
  - Modules
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: problem
What is a tensor product?
What is the universal property?
What do the tensors look like in the case of vector spaces?
:::

::: {.solution}
<1>1. $V\otimes W$ is the quotient of free vector space on $V\times W$ by bilinear relations.
::: {.proof}
construction.
:::

<1>2. Universal property: bilinear $B:V\times W\to U$ factors uniquely through $V\otimes W$ via $v\otimes w\mapsto B(v,w)$.
::: {.proof}
universal property.
:::

<1>3. For vector spaces with bases $\{e_i\},\{f_j\}$, $V\otimes W$ has basis $\{e_i\otimes f_j\}$, and tensors are finite sums $\sum c_{ij}e_i\otimes f_j$.
::: {.proof}
basis.
:::

<1>4. Q.E.D.
::: {.proof}
<1>2 and <1>3.
:::
:::
