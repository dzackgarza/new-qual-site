---
schema: qual/card@1
id: FE-73BWZ
kind: example
title: A uniformly convergent sequence of differentiable functions whose derivatives do not converge pointwise
prompts:
- Give a sequence of differentiable functions whose derivatives do not converge pointwise.
classification:
  areas:
  - real-analysis
  topics:
  - Differentiation
  - Convergence of Functions
  - Counterexamples
relations: []
review: draft
---

::: {.example}
For $n\geq 1$ let $f_n\colon\RR\to\RR$, $f_n(x) \coloneqq \frac{\sin(nx)}{n}$.
Then $\abs{f_n(x)}\leq\frac1n$ for all $x$, so $f_n\to 0$ [[D-YZC3C|uniformly]] on $\RR$.
Each $f_n$ is differentiable with $f_n'(x) = \cos(nx)$, and $f_n'(\pi) = \cos(n\pi) = (-1)^n$, so the sequence $(f_n'(\pi))$ diverges and $(f_n')$ does not [[D-IYDZU|converge pointwise]] on $\RR$.
:::
