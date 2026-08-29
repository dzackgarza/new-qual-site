---
schema: qual/card@1
id: D-HRU62
kind: definition
title: Gluing Along a Map
classification:
  areas:
  - topology
  topics:
  - Quotient Spaces
  - Cell Complexes
relations: []
review: draft
---

::: {.definition}
Given spaces $X_0$ and $X_1$, a subspace $A\subseteq X_1$, and a map $f: A\to X_0$, the space obtained by **attaching $X_1$ to $X_0$ along $f$** is
\[
X_0 \disjoint_f X_1 \da \qty{X_0 \disjoint X_1}/\qty{a \sim f(a) \st a\in A}
.\]
Attaching an $n\dash$cell is the case $X_1 = D^n$ and $A = S^{n-1}$; the mapping cylinder is the case $X_1 = X\cross I$ and $A = X\cross\ts{1}$.
:::

::: {.concept}
See Hatcher, p. 13.
:::
