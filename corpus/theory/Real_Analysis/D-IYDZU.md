---
schema: qual/card@1
id: D-IYDZU
kind: definition
title: Pointwise convergence
classification:
  areas:
  - real-analysis
  topics:
  - Convergence of Functions
  - Sequences of Functions
relations: []
review: draft
---

::: {.definition}
Let $S$ be a set, and let $f_n\colon S\to\CC$ for $n\geq 1$ and $f\colon S\to\CC$ be functions.
The sequence $(f_n)$ \dfn{converges pointwise} to $f$ on $S$ if
$$
(\forall \varepsilon>0)\,(\forall x \in S)\,(\exists n_0 = n_0(x, \varepsilon))\,(\forall n>n_0)\quad \abs{f_n(x)-f(x)}<\varepsilon.
$$
:::
