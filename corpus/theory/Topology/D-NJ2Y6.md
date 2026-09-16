---
schema: qual/card@1
id: D-NJ2Y6
kind: definition
title: Simplicial complex
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
Let $N\geq0$ and let $v_0,\ldots,v_k\in\RR^N$ be affinely independent, meaning that $v_1-v_0,\ldots,v_k-v_0$ are linearly independent.
The \dfn{$k$-simplex} $[v_0,\ldots,v_k]\subseteq\RR^N$ is the convex hull of $v_0,\ldots,v_k$, and these points are its \dfn{vertices}.
A \dfn{face} of $[v_0,\ldots,v_k]$ is a simplex spanned by a nonempty subset of $\ts{v_0,\ldots,v_k}$; for $0\leq i\leq k$ and $k\geq1$, the $i$-th \dfn{facet} is
$$
\del_i[v_0,\ldots,v_k]\coloneqq[v_0,\ldots,\hat v_i,\ldots,v_k].
$$
A \dfn{simplicial complex} in $\RR^N$ is a set $K$ of simplices in $\RR^N$ such that:

1. every face of a simplex in $K$ belongs to $K$;

2. for $\sigma,\tau\in K$, the intersection $\sigma\cap\tau$ is either empty or a face of both $\sigma$ and $\tau$;

3. every point of $\RR^N$ has a neighborhood that meets only finitely many simplices of $K$.
:::
