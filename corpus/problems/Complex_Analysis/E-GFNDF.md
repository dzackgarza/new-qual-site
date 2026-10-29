---
schema: qual/card@1
id: E-GFNDF
kind: problem
title: The family $\{x^k\}$ on $[0,1]$ is not equicontinuous
classification:
  areas:
  - complex-analysis
  topics:
  - Equicontinuity
  - Counterexamples
  - Sequences of Functions
relations: []
review: draft
---

::: {.exercise}
Give an example of a non-equicontinuous family.
:::

::: {.solution}
Let $f_k(x)\coloneqq x^k$ on $[0,1]$ for $k\ge1$.

::: pf

::: pf-step
The family $\theset{f_k}$ is not equicontinuous at $1$.

::: pf-proof
Set $\varepsilon=1/2$ and let $\delta>0$.
Choose $x\in[0,1)$ with $1-x<\delta$, and, since $x<1$, choose $k$ with $x^k<1/2$.
Then $\abs{f_k(1)-f_k(x)}=1-x^k>1/2=\varepsilon$, so no $\delta$ serves every $f_k$ at the point $1$.
:::

:::

:::

:::
