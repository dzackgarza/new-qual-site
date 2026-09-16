---
schema: qual/card@1
id: PR-SCTER
kind: proposition
title: Pointwise limits of continuous functions need not be continuous
classification:
  areas:
  - real-analysis
  topics:
  - Convergence of Functions
  - Continuity
  - Counterexamples
relations: []
review: draft
---

::: {.proposition}
For $n\geq1$ let $f_n\colon[0,1]\to\RR$, $f_n(x)\coloneqq x^n$.
Each $f_n$ is continuous, and $f_n$ converges pointwise to the discontinuous function $f$ with $f(x)=0$ for $0\leq x<1$ and $f(1)=1$.
For $x_k\coloneqq1-1/k$, the iterated limits differ:
$$
\lim_{k\to \infty} \lim_{n\to\infty} f_n(x_k) = 0 \neq 1 =
\lim_{n\to \infty} \lim_{k\to\infty} f_n(x_k) .
$$
:::
