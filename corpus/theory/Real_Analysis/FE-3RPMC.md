---
schema: qual/card@1
id: FE-3RPMC
kind: example
title: A sequence converging uniformly to $0$ on $\RR$ but not in $L^1(\RR)$
prompts:
- Give a sequence that converges uniformly, pointwise, and a.e., but not in $L^1$.
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
[[D-YZC3C|Uniform convergence]] on $\RR$, which implies [[D-IYDZU|pointwise convergence]] and convergence almost everywhere, does not imply convergence in $L^1(\RR)$.
For $n\geq 1$ let
$$
f_n \coloneqq \frac{1}{n} \chi_{[0, n]}\colon\RR\to\RR.
$$
Then $\norm{f_n}_\infty = \frac1n\to 0$, so $f_n\to 0$ uniformly on $\RR$.
But $\int_\RR \abs{f_n - 0}\dx = \frac1n\cdot n = 1$ for every $n$, so $f_n\not\to 0$ in $L^1(\RR)$.
:::
