---
schema: qual/card@1
id: FR-EDJWQ
kind: proof
title: Relationship between continuity and differentiability
classification:
  areas:
  - real-analysis
  topics:
  - Differentiation
  - Continuity
  - Counterexamples
relations: []
review: draft
---

::: {.proof}
Differentiability $\implies$ continuity: For $x\neq x_0$,
\[
f(x)-f(x_0)
=(x-x_0)\frac{f(x)-f(x_0)}{x-x_0}.
\]
As $x\to x_0$, the first factor tends to $0$ and the second tends to $f'(x_0)$ by differentiability.
Hence $f(x)-f(x_0)\to0$, so $f$ is continuous at $x_0$.

Not conversely: $f(x) = \abs{x}$.
:::
