---
schema: qual/card@1
id: P-TOPS26A
kind: problem
title: Euler characteristic of $\RP^n$
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
Compute the Euler characteristic of $\RP^n$.
:::

::: {.solution}

::: pf

::: pf-step
The standard CW structure on $\RP^n$ has exactly one cell in each dimension $0,1,\dots,n$.

::: pf-proof
This is the usual filtration $\RP^0\subset\RP^1\subset\cdots\subset\RP^n$.
:::

:::

::: pf-step
Hence
$$\boxed{\chi(\RP^n)=\sum_{k=0}^n(-1)^k=\begin{cases}1,&n\text{ even},\\0,&n\text{ odd}.\end{cases}}$$

::: pf-proof
Euler characteristic is the alternating sum of cell counts for a finite CW complex.
:::

:::

:::

:::
