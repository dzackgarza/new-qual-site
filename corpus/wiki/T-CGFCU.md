---
schema: qual/card@1
id: T-CGFCU
kind: theorem
title: "Lusin's Theorem"
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---

::: {.theorem title="Lusin's Theorem"}
If $f$ is measurable and finite-valued on $E$ with $\mu(E) < \infty$ then for every $\eps>0$ there exists a closed set $F_\eps$ with
\[
F_\eps \subset F && \mu(E - F_\eps) \leq \eps
\]
where $f$ restricted to $F_\eps$ is continuous.

> Note: this means that the separate function $\tilde f \da \ro{f}{F_\eps}$ is continuous, not that the function $f$ defined on all of $E$ is continuous at points of $F_\eps$.
:::
