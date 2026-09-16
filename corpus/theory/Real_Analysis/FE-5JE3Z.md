---
schema: qual/card@1
id: FE-5JE3Z
kind: example
title: A sequence of bounded functions with unbounded pointwise limit
prompts:
- Give a sequence of bounded functions whose pointwise limit is unbounded.
classification:
  areas:
  - real-analysis
  topics:
  - Convergence of Functions
  - Counterexamples
relations: []
review: draft
---

::: {.example}
A [[D-IYDZU|pointwise limit]] of bounded functions need not be bounded.
For $n\geq 1$ let $f_n\colon(0,1)\to\RR$, $f_n(x) \coloneqq \frac{1}{x + \frac1n}$.
Each $f_n$ is bounded, since $0 < f_n(x) \leq n$ for $x\in(0,1)$.
For each $x\in(0,1)$, $f_n(x)\to \frac1x$, and $x\mapsto\frac1x$ is unbounded on $(0,1)$.
:::
