---
schema: qual/card@1
id: FE-MDTXW
kind: example
title: $x^n$ converges pointwise but not uniformly on $[0,1]$
prompts:
- Give a sequence that converges pointwise but not uniformly.
classification:
  areas:
  - real-analysis
  topics:
  - Convergence of Functions
  - Uniform Convergence
  - Counterexamples
relations: []
review: draft
---

::: {.example}
For $n\geq 1$ let $f_n\colon[0,1]\to\RR$, $f_n(x)\coloneqq x^n$.
Then $f_n\to f\coloneqq\chi_{\theset{1}}$ [[D-IYDZU|pointwise]] on $[0,1]$, since $x^n\to 0$ for $0\leq x<1$ and $1^n = 1$.
The convergence is not [[D-YZC3C|uniform]]: for every $n$, $\sup_{x\in[0,1]}\abs{f_n(x) - f(x)} = \sup_{0\leq x<1} x^n = 1$.
:::
