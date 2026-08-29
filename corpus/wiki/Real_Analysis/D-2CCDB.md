---
schema: qual/card@1
id: D-2CCDB
kind: definition
title: Equicontinuity
classification:
  areas:
  - real-analysis
  topics:
  - Equicontinuity
  - Function Spaces
relations: []
review: draft
---

:::{.definition}
If $\mathcal F \subset C(X)$ is a family of continuous functions on $X$, then $\mathcal F$ *equicontinuous* at $x$ iff

\[
\forall \varepsilon > 0 ~~\exists U \ni x \text{ such that } y\in U \implies \abs{f(y) - f(x)} < \varepsilon \quad \forall f\in \mathcal{F}
.\]

:::
