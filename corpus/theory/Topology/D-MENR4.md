---
schema: qual/card@1
id: D-MENR4
kind: definition
title: Eilenberg--MacLane space
classification:
  areas:
  - topology
  topics:
  - Homotopy
  - Cohomology
  - Cell Complexes
relations: []
review: draft
---

::: {.definition}
Let $n\geq 1$ and let $G$ be a group, abelian if $n\geq 2$.
An \dfn{Eilenberg--MacLane space} $K(G, n)$ is a path connected [[D-ZOU5G|CW complex]] $X$ with [[D-EUX36|homotopy groups]]
$$
\pi_i(X)\cong
\begin{cases}
G & i = n, \\
0 & i\neq n.
\end{cases}
$$
:::

::: {.theorem}
Let $n\geq 1$ and $G$ a group, abelian if $n\geq 2$.
A CW complex $K(G, n)$ exists, and any two are homotopy equivalent.
If $G$ is abelian, then for every CW complex $X$ there is a natural bijection
$$
H^n(X; G)\cong\langle X, K(G, n)\rangle
$$
with the set of basepoint-preserving homotopy classes of basepoint-preserving maps $X\to K(G, n)$.
:::

::: {.example}
The circle $S^1$ is a $K(\ZZ, 1)$, $\CP^\infty$ is a $K(\ZZ, 2)$, and $\RP^\infty$ is a $K(\ZZ/2, 1)$.
:::

::: {.concept}
[@Hat02].
:::
