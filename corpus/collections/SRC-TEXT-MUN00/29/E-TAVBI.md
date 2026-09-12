---
schema: qual/card@1
id: E-TAVBI
kind: problem
title: Continuity characterized by nets
classification:
  areas:
  - topology
  topics:
  - Nets
  - Continuous Functions
relations: []
review: draft
---

::: {.exercise}

Theorem.
Let $f: X \to Y$.
Then $f$ is continuous if and only if for every convergent net $(x_\alpha)$ in $X$, converging to $x$, say, the net $(f(x_\alpha))$ converges to $f(x)$.
:::

::: {.solution}
If \(f\) is continuous and \(x_\alpha\to x\), then for every neighborhood \(V\) of \(f(x)\), \(f^{-1}(V)\) is a neighborhood of \(x\), so eventually \(x_\alpha\in f^{-1}(V)\), hence eventually \(f(x_\alpha)\in V\). Thus \(f(x_\alpha)\to f(x)\).

Conversely, suppose \(f\) preserves limits of all convergent nets. If \(f\) were not continuous, there would be a closed set \(C\subset Y\) such that \(f^{-1}(C)\) is not closed in \(X\). Choose
\[
x\in\overline{f^{-1}(C)}\setminus f^{-1}(C).
\]
By the closure-net theorem, there is a net \(x_\alpha\in f^{-1}(C)\) converging to \(x\). By hypothesis, \(f(x_\alpha)\to f(x)\). Since all \(f(x_\alpha)\in C\) and \(C\) is closed, the limit \(f(x)\in C\), contradicting \(x\notin f^{-1}(C)\). Hence \(f\) is continuous.
:::
