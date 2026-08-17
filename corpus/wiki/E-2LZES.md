---
schema: qual/card@1
id: E-2LZES
kind: exercise
title: "Show that for $X$ metrizable, compactness, limit point compactness and sequential compactness agree"
classification:
  areas:
  - topology
  topics:
  - metric-spaces
  - compactness
relations: []
review: draft
solved: false
---

Show that for $X$ metrizable, the following are equivalent:

- $X$ is compact;

- $X$ is limit point compact;

- $X$ is sequentially compact.

::: {.remark}
Munkres, *Topology*, §28, Theorem 28.2.

As printed upstream this exercise read "Show that if $X$ is metrizable, then $X$ is compact", which is false: $\RR$ is metrizable and not compact.
A hypothesis is missing, and the surrounding exercises do not say which — the neighbouring items ask for a space that is compact but not sequentially compact, and for sequentially compact $\implies$ totally bounded.
In a metrizable space all three conditions above coincide, so stating the equivalence repairs the exercise without choosing between the possible missing hypotheses.
:::
