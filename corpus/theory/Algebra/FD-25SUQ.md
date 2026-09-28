---
schema: qual/card@1
id: FD-25SUQ
kind: definition
title: Unique factorization domain
prompts:
- What does it mean for a ring to be a unique factorization domain?
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
An [[D-QJ3QL|integral domain]] $R$ is a \dfn{unique factorization domain} if every nonzero $x\in R$ can be written as
$$
x=u\prod_{i=1}^n p_i
$$
with $n\geq 0$, $u\in R^\times$ a [[D-QQIQZ|unit]], and $p_1,\ldots,p_n$ irreducible, and this decomposition is unique up to units and order: if also $x=v\prod_{j=1}^m q_j$ with $v\in R^\times$ and each $q_j$ irreducible, then $m=n$ and there is a permutation $\sigma$ of $\theset{1,\ldots,n}$ such that $p_i$ and $q_{\sigma(i)}$ are [[D-R4H6F|associates]] for every $i$.
:::
