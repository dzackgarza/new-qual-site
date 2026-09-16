---
schema: qual/card@1
id: D-A3PUW
kind: definition
title: Cellular homology
classification:
  areas:
  - topology
  topics:
  - Homology
  - Cell Complexes
  - Degree
relations: []
review: draft
---

::: {.definition}
Let $X$ be a [[D-ZOU5G|CW complex]] with $n$-skeleta $X^n$, and $X^{-1}\coloneqq\emptyset$.
The \dfn{cellular chain complex} of $X$ has $C_n^{\cell}(X) \coloneqq H_n(X^n, X^{n-1})$ and differential $d_n\colon C_n^{\cell}(X)\to C_{n-1}^{\cell}(X)$ the composite
$$
H_n(X^n, X^{n-1}) \mapsvia{\del_n} H_{n-1}(X^{n-1}) \mapsvia{j_{n-1}} H_{n-1}(X^{n-1}, X^{n-2})
$$
of the boundary map of the long exact sequence of the pair $(X^n, X^{n-1})$ and the map induced by inclusion.
The \dfn{cellular homology} $H_n^{\cell}(X)$ is the homology of $(C_*^{\cell}(X), d_*)$.
:::

::: {.remark}
The group $C_n^{\cell}(X)$ is free abelian with a basis in bijection with the $n$-cells of $X$, and $d_{n-1}\circ d_n = 0$.
By the cellular boundary formula, the coefficient of the $(n-1)$-cell $e^{n-1}_\beta$ in $d_n(e^n_\alpha)$ is the degree of the composite $S^{n-1}_\alpha \to X^{n-1}\to X^{n-1}/\qty{X^{n-1}\sm e^{n-1}_\beta} \cong S^{n-1}_\beta$ of the attaching map of $e^n_\alpha$ and the quotient map.
There is an isomorphism $H_n^{\cell}(X)\cong H_n(X)$ for every $n$ [@Hat02, Theorem 2.35, p. 139].
:::

::: {.concept}
[@Hat02, §2.2, pp. 139--140].
:::
