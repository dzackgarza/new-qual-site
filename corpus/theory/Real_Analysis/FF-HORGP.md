---
schema: qual/card@1
id: FF-HORGP
kind: fact
title: Completeness of a normed space via absolutely convergent series
prompts:
- Give several equivalent characterizations of completeness.
classification:
  areas:
  - real-analysis
  topics:
  - Completeness
  - Series of Numbers
relations: []
review: draft
---

::: {.fact}
Let $(V,\norm{\cdot})$ be a normed vector space.
Then $V$ is [[D-G5N6I|complete]] if and only if every absolutely convergent series in $V$ converges: whenever $x_n\in V$ and $\sum_{n=1}^\infty\norm{x_n}<\infty$, the series $\sum_{n=1}^\infty x_n$ converges in $V$.
:::

::: {.proof}
This is the equivalence proved in [[FD-WN55Z]].
:::
