---
schema: qual/card@1
id: P-CAFA17E
kind: problem
title: "The Riemann surface of the logarithm is simply connected"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: {.problem}
Prove that the Riemann surface of the complete analytic function associated to a branch of $\log z$ is simply connected.
:::

::: {.solution}
The complete analytic continuation of a local branch of $\log z$ may be modeled by
\[
\mathcal R=\{(z,w)\in\mathbb C^*\times\mathbb C:e^w=z\}.
\]
The projection to the first coordinate is the covering map underlying the multivalued logarithm, while the logarithm itself is the single-valued holomorphic function
\[
L(z,w)=w.
\]

Define
\[
\Phi:\mathbb C\longrightarrow\mathcal R,
\qquad
\Phi(w)=(e^w,w).
\]
This is a holomorphic bijection, and its inverse is simply the second-coordinate projection
\[
(z,w)\longmapsto w.
\]
Hence $\mathcal R$ is biholomorphic to $\mathbb C$. Since $\mathbb C$ is simply connected, so is the Riemann surface of the complete logarithm.
:::
