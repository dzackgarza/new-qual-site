---
schema: qual/card@1
id: P-CASP04F
kind: problem
title: "Interpolation by analytic functions with prescribed values and derivatives"
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
solved: false
---

::: problem
Let $G$ be an open region in $\mathbb{C}$ and $\{z_n\}$ a sequence of distinct points in $G$ without limit points in $G$. Suppose that for each $n$, you are given an integer $m_n$ and a sequence of complex numbers $\{w_{n,k}\}_{k=0}^{m_n}$. Show that there is $f \in H(G)$ such that, for every $n$,
$$f^{(k)}(z_n) = w_{n,k}, \quad k = 0, 1, \ldots, m_n.$$

Hint: First show that, given an integer $m$, complex numbers $w_k$ for $k = 1, \ldots, m$, a point $z = a$, and an analytic function $g$ which vanishes to order $m+1$ at $z = a$, then one can find a rational function
$$S(z) = \sum_{k=1}^{m+1} \frac{b_k}{(z-a)^k}$$
such that the product $f(z) = S(z)g(z)$ has a removable singularity at $z = a$ and $f^{(k)}(a) = w_k$ for $k = 0, 1, \ldots, m$.
:::
