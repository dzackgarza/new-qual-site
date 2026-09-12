---
schema: qual/card@1
id: P-UCTOP-SU11-1
kind: problem
title: Map from simply-connected CW complex to RP^{n+1} is null-homotopic
classification:
  areas:
  - topology
  topics:
  - Homotopy
relations: []
review: draft
---

Let $M$ be a simply connected $n$-dimensional CW complex.
Show that any map from $M$ to $\mathbb{RP}^{n+1}$ is homotopic to the constant map.

::: {.solution}
<1>1. Any map $f:M\to\mathbb{RP}^{n+1}$ lifts to a map $\widetilde f:M\to S^{n+1}$.
::: {.proof}
The universal covering map $p:S^{n+1}\to\mathbb{RP}^{n+1}$ has fundamental group subgroup $p_*\pi_1(S^{n+1})=0$. Since $M$ is simply connected, $f_*\pi_1(M)=0$, so the covering-space lifting criterion gives a lift $p\circ\widetilde f=f$.
:::

<1>2. Every map from the $n$-dimensional CW complex $M$ to $S^{n+1}$ is null-homotopic.
::: {.proof}
The sphere $S^{n+1}$ is $n$-connected: $\pi_i(S^{n+1})=0$ for $i\le n$. By cellular approximation, $\widetilde f$ is homotopic to a cellular map. But the $n$-skeleton of the standard CW structure on $S^{n+1}$ is a point, so every cellular map from an $n$-dimensional CW complex lands at that point.
:::

<1>3. Therefore $f$ is null-homotopic.
::: {.proof}
By <1>2, $\widetilde f\simeq *$. Composing the null-homotopy with the covering projection $p$ gives $f=p\circ\widetilde f\simeq *$.
:::
:::
