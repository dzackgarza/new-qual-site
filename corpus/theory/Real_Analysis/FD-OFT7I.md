---
schema: qual/card@1
id: FD-OFT7I
kind: definition
title: Lebesgue and Borel measurable functions
prompts:
- Which preimages must be measurable for $f$ to be a measurable function?
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
relations: []
review: draft
---

::: {.definition}
Let $\mathcal{M}_L$ and $\mathcal{M}_B$ be the $\sigma$-algebras of [[D-MDJII|Lebesgue measurable]] and Borel subsets of $\RR$, let $E\in\mathcal{M}_L$, and let $f\colon E \to [-\infty,\infty]$.
The function $f$ is \dfn{Lebesgue measurable} if
$$
\theset{x \in E \suchthat f(x)>a}=f^{-1}((a, \infty]) \in \mathcal{M}_L \quad\text{for every } a\in\RR.
$$
When $E\in\mathcal{M}_B$, the function $f$ is \dfn{Borel measurable} if $f^{-1}((a, \infty]) \in \mathcal{M}_B$ for every $a\in\RR$.
:::
