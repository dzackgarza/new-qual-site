---
schema: qual/card@1
id: FE-LJRG2
kind: example
title: The spikes $n\chi_{(0,1/n)}$ converge pointwise but not in $L^1$
prompts:
- Give an example of a function that converge almost everywhere but not pointwise or in $L^1$.
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
For $n\geq 1$ let $f_n\coloneqq n\chi_{(0, 1/n)}\colon\RR\to\RR$.

- For $x\leq 0$, $f_n(x) = 0$ for all $n$; for $x>0$, $f_n(x) = 0$ for all $n > 1/x$. Hence $f_n\to 0$ [[D-IYDZU|pointwise]] on $\RR$.

- $\int_\RR\abs{f_n - 0}\dx = n\cdot\frac1n = 1$ for every $n$, so $f_n\not\to 0$ in $L^1(\RR)$.
:::
