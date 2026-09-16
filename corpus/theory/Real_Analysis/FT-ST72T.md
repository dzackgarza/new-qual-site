---
schema: qual/card@1
id: FT-ST72T
kind: theorem
title: Minkowski's inequality
prompts:
- State Minkowski's inequality.
classification:
  areas:
  - real-analysis
  topics:
  - Norms
  - Lp Spaces
relations: []
review: draft
---

::: {.theorem}
Let $(X,\mcm,\mu)$ be a [[D-QYLPH|measure]] space, let $1 \leq p < \infty$, and let $f,g\in L^p(X,\mu)$.
Then $f+g\in L^p(X,\mu)$ and
$$
\norm{f + g}_p \leq \norm{f}_p + \norm{g}_p .
$$
:::
