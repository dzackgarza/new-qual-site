---
schema: qual/card@1
id: D-EBNUE
kind: definition
title: "Fundamental Group"
classification:
  areas:
  - topology
  topics: []
relations: []
review: draft
---

::: {.definition title="Fundamental Group"}
For $x_0 \in X$, the **fundamental group** $\pi_1(X, x_0)$ is the set of homotopy classes rel $\ts{0,1}$ of loops $\gamma: I \to X$ based at $x_0$, with multiplication
\[
[\gamma][\eta] \da [\gamma \cdot \eta]
\]
given by concatenation.
This is a group: the constant loop is the identity, and $[\gamma]\inv = [\bar\gamma]$ for $\bar\gamma(s) \da \gamma(1-s)$.
A path $h$ from $x_0$ to $x_1$ induces an isomorphism $\beta_h: \pi_1(X, x_1)\mapsvia{\sim} \pi_1(X, x_0)$, so for path-connected $X$ the group is well defined up to isomorphism.
:::

::: {.concept}
See Hatcher, §1.1, p. 26.
:::
