---
schema: qual/card@1
id: FE-KHKC4
kind: example
title: Boxes of height $1/n$ and width $n$ converge uniformly but not in $L^1$
prompts:
- Give an example of a sequence of functions that converge uniformly but not in $L^1$.
classification:
  areas:
  - real-analysis
  topics:
  - Uniform Convergence
  - L¹
  - Counterexamples
relations: []
review: draft
---

::: {.example}
For $n\geq 1$ let $f_n\coloneqq\frac1n\chi_{[0,n]}\colon\RR\to\RR$, the box of height $\frac1n$ over $[0,n]$.
Then $\sup_{x\in\RR}\abs{f_n(x)} = \frac1n\to 0$, so $f_n\to 0$ [[D-YZC3C|uniformly]] on $\RR$, but $\int_\RR\abs{f_n - 0}\dx = 1$ for every $n$, so $f_n\not\to 0$ in $L^1(\RR)$.
:::
