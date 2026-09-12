---
schema: qual/card@1
id: E-SS8.EX-3
kind: problem
title: "Simple connectedness is a conformal invariant"
classification:
  areas:
  - complex-analysis
  topics: ['Conformal Mappings', 'Riemann Mapping Theorem', 'Automorphisms']
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: exercise
3. Suppose $U$ and V are conformally equivalent.
   Prove that if U is simply connected, then so is V . Note that this conclusion remains valid if we merely assume that there exists a continuous bijection between U and $V .$
:::

::: solution
Let $\Phi:U\to V$ be a conformal equivalence. Since $\Phi$ and $\Phi^{-1}$ are holomorphic, they are continuous, so $\Phi$ is a homeomorphism.

Assume $U$ is simply connected. Let $\gamma:[0,1]\to V$ be a closed curve. Then $\Phi^{-1}\circ\gamma$ is a closed curve in $U$, so there is a homotopy
\[
H:[0,1]^2\to U
\]
from $\Phi^{-1}\circ\gamma$ to a constant curve. Composing with $\Phi$ gives a homotopy $\Phi\circ H$ in $V$ from $\gamma$ to a constant curve. Hence every closed curve in $V$ is null-homotopic, so $V$ is simply connected.

More generally, suppose only that $\Phi:U\to V$ is a continuous bijection. Since $U,V$ are open subsets of $\mathbb R^2$, invariance of domain implies that the continuous injective map $\Phi$ is open. Therefore $\Phi^{-1}$ is continuous, so $\Phi$ is again a homeomorphism, and the same homotopy argument applies.
:::
