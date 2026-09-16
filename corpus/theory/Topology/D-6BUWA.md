---
schema: qual/card@1
id: D-6BUWA
kind: definition
title: Singular homology
classification:
  areas:
  - topology
  topics:
  - Homology
relations: []
review: draft
---

::: {.definition}
Let $X$ be a topological space and $n\geq 0$, and let $\Delta^n = [v_0, \ldots, v_n]$ be the standard $n$-simplex.
A \dfn{singular $n$-simplex} in $X$ is a continuous map $\sigma\colon \Delta^n \to X$.
The \dfn{singular chain group} $C_n(X)$ is the free abelian group on the singular $n$-simplices in $X$, and $C_n(X)\coloneqq 0$ for $n<0$.
The boundary map $\del_n\colon C_n(X)\to C_{n-1}(X)$ is the homomorphism with
$$
\del_n \sigma \coloneqq \sum_{i=0}^n (-1)^i \ro{\sigma}{[v_0,\ldots, \hat v_i, \ldots, v_n]}
$$
on singular simplices, each face $[v_0,\ldots, \hat v_i, \ldots, v_n]$ being identified with $\Delta^{n-1}$ by the order-preserving linear homeomorphism.
The \dfn{singular homology} of $X$ is
$$
H_n(X) \coloneqq \ker \del_n / \im \del_{n+1}
.$$
:::

::: {.remark}
The quotient is defined because $\del_n \circ \del_{n+1} = 0$.
:::

::: {.concept}
[@Hat02, §2.1, p. 108].
:::
