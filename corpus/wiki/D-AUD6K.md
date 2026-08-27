---
schema: qual/card@1
id: D-AUD6K
kind: definition
title: Poles (and associated terminology)
classification:
  areas:
  - complex-analysis
  topics:
  - Poles
  - Laurent Series
  - Singularities
relations: []
review: draft
---

:::{.definition}
Let $f$ be a meromorphic function with an isolated singularity at $z_0$.
TFAE:

- $z_0$ is a pole of $f$ of order $n$.
- $\abs{f(z)}\convergesto{z\to z_0} \infty$
- $z_0$ is a zero of order $n$ of $g(z) \da {1\over f(z)}$, and $g$ is holomorphic in a neighborhood of $z_0$
- $f(z) = (z-z_0)^{-n}h(z)$ where $h$ is holomorphic in a punctured neighborhood of $z_0$.
- $f$ admits a Laurent expansion of the form
\[
f(z) = \sum_{k\geq -n} c_k (z-z_0)^k, && c_{-n}\neq 0
.\]

:::
