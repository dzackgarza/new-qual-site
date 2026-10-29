---
schema: qual/card@1
id: D-1EBNU
kind: definition
title: Riemann integrable function
classification:
  areas:
  - real-analysis
  topics:
  - Riemann Integrability
  - Integrals
relations: []
review: draft
---

::: {.definition}
Let $f\colon[a,b]\to\RR$ be bounded.
For a partition $P = \theset{a = x_0 < x_1 < \cdots < x_n = b}$ of $[a,b]$, let $M_i \coloneqq \sup_{[x_{i-1},x_i]} f$ and $m_i \coloneqq \inf_{[x_{i-1},x_i]} f$, and define the \dfn{upper sum} $U(f,P)\coloneqq\sum_{i=1}^n M_i(x_i-x_{i-1})$ and the \dfn{lower sum} $L(f,P)\coloneqq\sum_{i=1}^n m_i(x_i-x_{i-1})$.
The \dfn{upper} and \dfn{lower Darboux integrals} of $f$ are $\inf_P U(f,P)$ and $\sup_P L(f,P)$, over all partitions $P$ of $[a,b]$.
The function $f$ is \dfn{Riemann integrable} on $[a,b]$ if these two numbers are equal; their common value is $\int_a^b f$.
:::
