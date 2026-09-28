---
schema: qual/card@1
id: D-PAEDW
kind: definition
title: Limit superior and limit inferior of a sequence of sets
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
Let $(E_n)_{n\geq 1}$ be a sequence of subsets of a set $X$.
Its \dfn{limit inferior} and \dfn{limit superior} are
$$
\begin{aligned}
\liminf_{n\to\infty} E_{n} &\coloneqq \bigcup_{N=1}^\infty \bigcap_{n=N}^\infty E_{n} = \theset{x\in X \suchthat x\in E_{n} \text{ for all but finitely many } n}, \\
\limsup_{n\to\infty} E_{n} &\coloneqq \bigcap_{N=1}^\infty \bigcup_{n=N}^{\infty} E_{n} = \theset{x\in X \suchthat x\in E_{n} \text{ for infinitely many } n}.
\end{aligned}
$$
:::
