---
schema: qual/card@1
id: T-7DICT
kind: theorem
title: Cantor's intersection theorem
classification:
  areas:
  - topology
  topics:
  - Compactness
relations: []
review: draft
---

::: {.theorem}
Let $X$ be a compact space and let $C_1 \supseteq C_2 \supseteq \cdots$ be a decreasing sequence of nonempty closed subsets of $X$.
Then $\Intersect_n C_n \neq \emptyset$ [@Mun00, Theorem 26.9].
:::

::: {.remark}
If $X$ is Hausdorff, it suffices that each $C_n$ be nonempty and compact, since compact subsets of Hausdorff spaces are closed [@Mun00, Theorem 26.3].
Without closedness the conclusion fails: in an infinite set $\NN$ with the indiscrete topology every subset is compact, and $C_n = \ts{n, n+1, \ldots}$ is a decreasing sequence of nonempty compact sets with empty intersection.
:::
