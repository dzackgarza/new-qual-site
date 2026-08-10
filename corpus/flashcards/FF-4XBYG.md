---
schema: qual/card@1
id: FF-4XBYG
kind: fact
title: 'Cauchy-Schwarz Inequality'
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---

::: {.fact title="Cauchy-Schwarz Inequality"}
$$
\abs{\inner{f}{g}} \leq \norm{fg}_1 \leq \norm{f}_2 \norm{g}_2, \quad\text{i.e.}\quad
\int\abs{fg} \leq \sqrt{\int \abs{f}^2} \sqrt{\int \abs{g}^2}
$$
with equality iff $f \in \spanof_\CC(g)$.
:::
