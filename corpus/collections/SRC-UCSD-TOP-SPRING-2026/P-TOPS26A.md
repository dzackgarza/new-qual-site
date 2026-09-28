---
schema: qual/card@1
id: P-TOPS26A
kind: problem
title: Euler characteristic of $\mathbb{RP}^n$
classification:
  areas:
  - topology
  topics:
  - Homology
  - Cell Complexes
relations: []
review: draft
---

::: {.problem}
Compute the Euler characteristic of $\mathbb{RP}^n$.
:::

::: {.solution}
<1>1. The standard CW structure on $\mathbb{RP}^n$ has exactly one cell in each dimension $0,1,\dots,n$.
::: {.proof}
This is the usual filtration $\mathbb{RP}^0\subset\mathbb{RP}^1\subset\cdots\subset\mathbb{RP}^n$.
:::

<1>2. Hence
$$\boxed{\chi(\mathbb{RP}^n)=\sum_{k=0}^n(-1)^k=\begin{cases}1,&n\text{ even},\\0,&n\text{ odd}.\end{cases}}$$
::: {.proof}
Euler characteristic is the alternating sum of cell counts for a finite CW complex.
:::
:::
