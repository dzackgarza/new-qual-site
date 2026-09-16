---
schema: qual/card@1
id: D-G2I5Q
kind: definition
title: Limit superior of a sequence
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
Let $(x_n)_{n\geq 1}$ be a sequence of real numbers.
Its \dfn{limit superior} is
$$
\limsup_{n\to\infty} x_{n} \coloneqq \lim_{N \to \infty} \sup_{n>N} x_{n} \in [-\infty,\infty],
$$
where the limit exists in $[-\infty,\infty]$ because $\sup_{n>N}x_n$ is nonincreasing in $N$.
:::
