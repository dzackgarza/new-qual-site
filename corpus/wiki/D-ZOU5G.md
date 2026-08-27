---
schema: qual/card@1
id: D-ZOU5G
kind: definition
title: CW Complex
classification:
  areas:
  - topology
  topics:
  - Cell Complexes
relations: []
review: draft
---

::: {.definition}
A space built from cells by induction on dimension:

1. Start with a discrete set $X^0$, whose points are the $0\dash$cells.
2. Form the $n\dash$skeleton $X^n$ from $X^{n-1}$ by attaching $n\dash$cells $e^n_\alpha$ along maps $\varphi_\alpha: S^{n-1}\to X^{n-1}$, so
\[
X^n = \qty{X^{n-1} \disjoint \Disjoint_\alpha D^n_\alpha} / \qty{x \sim \varphi_\alpha(x) \st x \in \del D^n_\alpha}
.\]
3. Either stop at a finite stage and set $X = X^n$, or set $X = \Union_n X^n$ with the weak topology: $A\subseteq X$ is closed iff $A \intersect X^n$ is closed in $X^n$ for every $n$.
:::

::: {.concept}
See Hatcher, p. 5.
:::
