---
schema: qual/card@1
id: D-RU2GC
kind: definition
title: Simplicial map
classification:
  areas:
  - topology
  topics:
  - Cell Complexes
  - Homology
relations: []
review: draft
---

::: {.definition}
Let $K$ and $L$ be [[D-NJ2Y6|simplicial complexes]] with vertex sets $V(K)$ and $V(L)$.
A \dfn{simplicial map} $f\colon K\to L$ is a map $f\colon V(K)\to V(L)$ such that whenever $v_0,\ldots,v_k$ are the vertices of a simplex of $K$, the points $f(v_0),\ldots,f(v_k)$, not necessarily distinct, are the vertices of a simplex of $L$.
:::

::: {.remark}
A simplicial map extends to a continuous map $\abs{K}\to\abs{L}$ of underlying spaces that is affine on each simplex: $\sum_it_iv_i\mapsto\sum_it_if(v_i)$ for $t_i\geq0$ with $\sum_it_i=1$ [@Mun84, sec. 2].
:::
