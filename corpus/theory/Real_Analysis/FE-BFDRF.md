---
schema: qual/card@1
id: FE-BFDRF
kind: example
title: A sequence converging pointwise on $\RR$ but neither uniformly nor in $L^1(\RR)$
prompts:
- Give a sequence that converges pointwise and a.e. but not uniformly or in $L^1$.
classification:
  areas:
  - real-analysis
  topics:
  - Convergence of Functions
  - L¹
  - Counterexamples
relations: []
review: draft
---

::: {.example}
For $n\geq 1$ let $f_n \coloneqq \chi_{(n, n+1)}\colon\RR\to\RR$.

- For each $x\in\RR$, $f_n(x) = 0$ for all $n > x$, so $f_n\to 0$ [[D-IYDZU|pointwise]] on $\RR$, and in particular almost everywhere.

- $\sup_{x\in\RR}\abs{f_n(x)} = 1$ for every $n$, so $f_n\not\to 0$ [[D-YZC3C|uniformly]] on $\RR$.

- $\int_\RR\abs{f_n - 0}\dx = 1$ for every $n$, so $f_n\not\to 0$ in $L^1(\RR)$.
:::
