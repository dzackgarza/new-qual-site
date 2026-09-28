---
schema: qual/card@1
id: D-HOKQD
kind: definition
title: Limit superior and limit inferior of a sequence
classification:
  areas:
  - real-analysis
  topics:
  - Sequences of Numbers
  - Limits
relations: []
review: draft
---

::: {.definition}
Let $(a_n)_{n\geq 0}$ be a sequence of real numbers.
Its \dfn{limit superior} and \dfn{limit inferior} are
$$
\begin{aligned}
\limsup_{n\to\infty} a_n &\coloneqq \lim_{n\to \infty} \sup_{j\geq n} a_j = \inf_{n\geq 0} \sup_{j\geq n} a_j, \\
\liminf_{n\to\infty} a_n &\coloneqq \lim_{n\to \infty} \inf_{j\geq n} a_j = \sup_{n\geq 0} \inf_{j\geq n} a_j,
\end{aligned}
$$
with values in $[-\infty,\infty]$; the limits exist and equal the infimum and supremum because $\sup_{j\geq n}a_j$ is nonincreasing and $\inf_{j\geq n}a_j$ is nondecreasing in $n$.
:::
