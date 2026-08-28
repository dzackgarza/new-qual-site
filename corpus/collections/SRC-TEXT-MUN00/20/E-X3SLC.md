---
schema: qual/card@1
id: E-X3SLC
kind: exercise
title: A bounded metric giving the same topology
classification:
  areas:
  - topology
  topics:
  - Metric Spaces
relations: []
review: draft
---

::: {.exercise}

Show that if $d$ is a metric for $X$, then

$$
d'(x, y) = d(x, y) / (1 + d(x, y))
$$

is a bounded metric that gives the topology of $X$.
[Hint: If $f(x) = x/(1+x)$ for $x > 0$, use the mean-value theorem to show that $f(a+b) - f(b) \leq f(a)$.]
:::
