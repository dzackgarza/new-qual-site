---
schema: qual/card@1
id: PR-5ZSSQ
kind: proposition
title: "Contraction principle"
classification:
  areas:
  - complex-analysis
  topics:
  - fixed-points
  - metric-spaces
  - completeness
relations: []
review: draft
---
:::{.proposition title="Contraction principle"}
If $(X, \abs{\wait})$ is a metric space and $f: X\to X$ with
\[
\abs{f(x) - f(y)} \leq c \abs{x-y} \text{ for some }c < 1, \forall x, y\in X
,\]
then $f$ is a **contraction**.
If $X$ is complete, then $f$ has a unique fixed point $x_0$ such that $f(x_0) = x_0$.
:::
