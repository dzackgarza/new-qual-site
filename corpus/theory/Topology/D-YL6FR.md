---
schema: qual/card@1
id: D-YL6FR
kind: definition
title: Uniform Continuity
classification:
  areas:
  - topology
  topics:
  - Uniform Continuity
  - Metric Spaces
  - Continuity
relations:
- kind: variant-of
  target: D-WGYSB
review: draft
---

:::{.definition}
For $f: (X, d_{x}) \to (Y, d_{Y})$ metric spaces, $f$ is **uniformly continuous** iff
\[
\forall \eps > 0, ~\exists \delta > 0 \text{ such that } \quad d_{X}(x_{1}, x_{2}) < \delta \implies d_{Y}(f(x_{1}), f(x_{2})) < \eps
.\]
:::
