---
schema: qual/card@1
id: D-KC4BS
kind: definition
title: Moore space
classification:
  areas:
  - topology
  topics:
  - Homology
  - Cell Complexes
relations: []
review: draft
---

::: {.definition}
Let $G$ be an abelian group and $n\geq 1$.
A \dfn{Moore space} $M(G, n)$ is a [[D-ZOU5G|CW complex]] $X$ with
$$
\tilde H_i(X;\ZZ)\cong
\begin{cases}
G & i = n, \\
0 & i\neq n.
\end{cases}
$$
:::

::: {.proposition}
For every abelian group $G$ and $n\geq 1$ a Moore space $M(G, n)$ exists: choose a presentation of $G$ by generators and relations, take a [[D-IGUUS|wedge]] of $n$-spheres with one sphere for each generator, and attach one $(n+1)$-cell for each relation along a map representing that relation.
:::

::: {.example}
The sphere $S^n$ is an $M(\ZZ, n)$.
For $m\geq 2$, the space $S^n\cup_m e^{n+1}$ obtained by attaching an $(n+1)$-cell to $S^n$ along a map $S^n\to S^n$ of degree $m$ is an $M(\ZZ/m, n)$.
:::

::: {.concept}
See [@Hat02, §2.2, Example 2.40, p. 143].
:::
