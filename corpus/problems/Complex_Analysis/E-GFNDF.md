---
schema: qual/card@1
id: E-GFNDF
kind: problem
title: The family $\{z^k\}$ on $[0,1]$ is not equicontinuous
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
Take $f_k(x)=x^k$ on $[0,1]$ and test equicontinuity at the endpoint $1$.
Set $\varepsilon=1/2$.
Given any $\delta>0$, choose $x\in[0,1)$ with $|1-x|<\delta$.
Since $x<1$, choose $k$ large enough that $x^k<1/2$.
Then
\[
|f_k(1)-f_k(x)|=1-x^k>{1\over2}=\varepsilon.
\]
Thus no single $\delta$ works for the whole family at $1$, so $\{f_k\}$ is not equicontinuous.
:::
