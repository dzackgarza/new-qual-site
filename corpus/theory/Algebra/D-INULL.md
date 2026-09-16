---
schema: qual/card@1
id: D-INULL
kind: definition
title: Unique factorization domain
classification:
  areas:
  - algebra
  topics:
  - Factorization
  - Integral Domains
relations: []
review: draft
---

::: {.definition}
An [[D-QJ3QL|integral domain]] $R$ is a \dfn{unique factorization domain} if every nonzero $r\in R$ admits a decomposition
$$
r = u \prod_{i=1}^n p_i
$$
with $n\geq 0$, $u\in R^{\times}$ a [[D-QQIQZ|unit]], and $p_1,\ldots,p_n$ [[D-TO3IY|irreducible]], and this decomposition is unique up to order and [[D-R4H6F|associates]]: if also $r = v\prod_{j=1}^m q_j$ with $v\in R^{\times}$ and each $q_j$ irreducible, then $m=n$ and there is a permutation $\sigma$ of $\theset{1,\ldots,n}$ such that $p_i$ and $q_{\sigma(i)}$ are associates for every $i$.
:::
