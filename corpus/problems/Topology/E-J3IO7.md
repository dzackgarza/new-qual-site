---
schema: qual/card@1
id: E-J3IO7
kind: problem
title: Compact versus sequentially compact spaces
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Counterexamples
relations: []
review: draft
---

::: exercise
Give an example of a space that is compact but not sequentially compact, and vice versa.
:::

::: {.solution}
<1>1. A compact space need not be sequentially compact.
::: {.proof}
Let
$$X=\{0,1\}^{\mathcal P(\mathbb N)}$$
with the product topology. It is compact by Tychonoff's theorem. For each $n\in\mathbb N$, define $x_n\in X$ by
$$x_n(A)=\mathbf 1_{\{n\in A\}}.$$
Given any subsequence $x_{n_k}$, take $A=\{n_{2k}:k\ge1\}$. Then the $A$-coordinate of $x_{n_k}$ alternates $0,1,0,1,\dots$, so the subsequence cannot converge. Thus $X$ is not sequentially compact.
:::

<1>2. A sequentially compact space need not be compact.
::: {.proof}
Let $\omega_1$ be the space of all countable ordinals with the order topology. Every sequence in $\omega_1$ is bounded above by a countable ordinal $\alpha<\omega_1$; its range lies in the compact metrizable ordinal interval $[0,\alpha]$, hence has a convergent subsequence. Thus $\omega_1$ is sequentially compact. It is not compact because the open cover
$$\{[0,\alpha):\alpha<\omega_1\}$$
(or equivalently a suitable increasing family of initial open sets) has no finite subcover.
:::
:::
