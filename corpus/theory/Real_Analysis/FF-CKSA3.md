---
schema: qual/card@1
id: FF-CKSA3
kind: fact
title: Minkowski's inequality
prompts:
- What is Minkowski's inequality?
classification:
  areas:
  - real-analysis
  topics:
  - Norms
  - Lp Spaces
relations: []
review: draft
---

::: {.fact}
Let $(X,\mcm,\mu)$ be a [[D-QYLPH|measure]] space, let $1 \leq p < \infty$, and let $f, g\in L^p(\mu)$.
Then $f+g\in L^p(\mu)$ and
$$
\norm{f + g}_p \leq \norm{f}_p + \norm{g}_p.
$$
:::
