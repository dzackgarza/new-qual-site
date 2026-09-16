---
schema: qual/card@1
id: FF-OQ6YZ
kind: fact
title: Hölder's inequality
prompts:
- State Holder's inequality.
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
Let $(X,\mcm,\mu)$ be a [[D-QYLPH|measure]] space, let $1\leq p, q\leq\infty$ with $\frac1p + \frac1q = 1$, and let $f\in L^p(\mu)$ and $g\in L^q(\mu)$.
Then $fg\in L^1(\mu)$ and
$$
\norm{fg}_1 \leq \norm{f}_p \norm{g}_q.
$$
:::
