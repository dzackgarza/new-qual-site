---
schema: qual/card@1
id: D-NRRIT
kind: definition
title: Quadratic form
classification:
  areas:
  - algebra
  topics:
  - Quadratic Forms
  - Bilinear Forms
  - Vector Spaces
relations: []
review: draft
---

::: {.definition}
Let $k$ be a field and $V$ a $k$-vector space.
A \dfn{quadratic form} on $V$ is a function $q\colon V\to k$ such that $q(\lambda x) = \lambda^2 q(x)$ for all $\lambda\in k$ and $x\in V$, and such that
$$
b_q(x, y) \coloneqq q(x+y) - q(x) - q(y)
$$
is a bilinear form $V\times V\to k$.
:::

::: {.remark}
The form $b_q$ is symmetric and satisfies $b_q(x,x)=q(2x)-2q(x)=2q(x)$.
If $\characteristic k \neq 2$, then $q\mapsto \frac12 b_q$ is a bijection from quadratic forms on $V$ to symmetric bilinear forms on $V$, with inverse $b\mapsto \bigl(x\mapsto b(x,x)\bigr)$.
If $V$ has basis $e_1,\ldots,e_n$, then in the coordinates $x=\sum_i x_ie_i$ the form $q$ is a homogeneous polynomial of degree $2$, $q(x) = \sum_{i \leq j} a_{ij} x_i x_j$ with $a_{ii}=q(e_i)$ and $a_{ij}=b_q(e_i,e_j)$ for $i<j$.
:::

::: {.concept}
See [@Art11].
:::
