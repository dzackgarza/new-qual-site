---
schema: qual/card@1
id: FD-AI6XN
kind: definition
title: Limsup/Liminf of Sets
prompts:
- What are $\limsup_n A_n$ and $\liminf_n A_n$ for a sequence of sets?
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
  - Borel-Cantelli
relations: []
review: draft
---

::: {.definition}
$$\begin{align*}
\limsup_n A_n \definedas \intersect_n \union_{j\geq n} A_j&= \theset{x \suchthat x\in A_n \text{ for inf. many $n$}}  \\
\liminf_n A_n \definedas \union_n \intersect_{j\geq n} A_j &= \theset{x \suchthat x\in A_n \text{ for all except fin. many $n$}}  \\
\end{align*}$$
:::
