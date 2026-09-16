---
schema: qual/card@1
id: PR-UZVC3
kind: proposition
title: Limits and integrals need not commute
classification:
  areas:
  - real-analysis
  topics:
  - Convergence of Integrals
  - Counterexamples
relations: []
review: draft
---

::: {.proposition}
For $n\geq1$ let $f_n\coloneqq n\chi_{(0,1/n)}\colon[0,1]\to\RR$.
Then $f_n(x)\to0$ for every $x\in[0,1]$, but
$$
\lim_{n\to \infty} \int_0^1 f_n(x) \,dx = 1 \neq 0 = \int_0^1 \lim_{n\to \infty} f_n(x) \,dx .
$$
:::
