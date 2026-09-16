---
schema: qual/card@1
id: FE-GN3CF
kind: example
title: Differentiable functions converging to $\abs{x}$
prompts:
- Give a sequence of differentiable functions whose pointwise limit is not differentiable.
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
A limit of differentiable functions need not be differentiable.
For $n\geq 1$ let $f_n\colon\RR\to\RR$, $f_n(x) \coloneqq \frac{x^2}{\sqrt{x^2 + \frac1n}}$.
Each $f_n$ is differentiable on $\RR$, since $x^2+\frac1n > 0$.
For every $x\in\RR$,
$$
\abs{\abs{x} - f_n(x)} = \frac{\abs{x}}{\sqrt{x^2+\frac1n}}\qty{\sqrt{x^2+\tfrac1n} - \abs{x}} \leq \frac{1/n}{\sqrt{x^2+\frac1n} + \abs{x}} \leq \frac{1}{\sqrt n},
$$
so $f_n\to\abs{x}$ [[D-YZC3C|uniformly]], and in particular [[D-IYDZU|pointwise]], on $\RR$.
The limit $x\mapsto\abs{x}$ is not differentiable at $0$.
:::
