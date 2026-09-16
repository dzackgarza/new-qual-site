---
schema: qual/card@1
id: FD-AI6XN
kind: definition
title: Limit superior and limit inferior of a sequence of sets
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
Let $(A_n)_{n\geq 1}$ be a sequence of subsets of a set $X$.
Its \dfn{limit superior} and \dfn{limit inferior} are
$$
\begin{aligned}
\limsup_{n\to\infty} A_n &\coloneqq \bigcap_{n\geq 1} \bigcup_{j\geq n} A_j = \theset{x\in X \suchthat x\in A_n \text{ for infinitely many } n}, \\
\liminf_{n\to\infty} A_n &\coloneqq \bigcup_{n\geq 1} \bigcap_{j\geq n} A_j = \theset{x\in X \suchthat x\in A_n \text{ for all but finitely many } n}.
\end{aligned}
$$
:::
