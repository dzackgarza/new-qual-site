---
schema: qual/card@1
id: PR-H4CYN
kind: proposition
title: Sufficient condition for Taylor convergence
classification:
  areas:
  - real-analysis
  topics:
  - Differentiation
  - Series of Functions
relations: []
review: draft
---

::: {.proposition title="Sufficient condition for Taylor convergence"}
Given a point $c$ and some $\varepsilon>0$, if $f \in C^\infty(I)$ and there exists an $M$ such that
$$
x \in N_\varepsilon(c) \implies \abs{f^{(n)}(x)} \leq M^n
$$
then the Taylor expansion about $c$ converges on $N_\varepsilon(c)$.
:::
