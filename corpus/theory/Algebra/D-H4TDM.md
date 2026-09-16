---
schema: qual/card@1
id: D-H4TDM
kind: definition
title: Gram matrix of a bilinear form
classification:
  areas:
  - algebra
  topics:
  - Bilinear Forms
  - Matrices
relations: []
review: draft
---

::: {.definition}
Let $k$ be a field, let $V$ be a finite-dimensional $k$-vector space with ordered basis $\mathcal B = (e_1, \ldots, e_n)$, and let $b\colon V\times V\to k$ be a bilinear form.
The \dfn{Gram matrix} of $b$ with respect to $\mathcal B$ is
$$
G \coloneqq \qty{ b(e_i, e_j) }_{1\leq i,j\leq n}.
$$
:::

::: {.proposition}
Let $k$, $V$, $\mathcal B$, $b$, and $G$ be as in the definition, and write $[x]_{\mathcal B}\in k^n$ for the coordinate vector of $x\in V$.

1. For all $x, y\in V$, $b(x, y) = [x]_{\mathcal B}^t\, G\, [y]_{\mathcal B}$.

2. If $\mathcal B'$ is another ordered basis and $P\in\GL_n(k)$ satisfies $[x]_{\mathcal B} = P[x]_{\mathcal B'}$ for all $x\in V$, then the Gram matrix of $b$ with respect to $\mathcal B'$ is $P^t G P$. In particular, $\det G$ is well defined up to multiplication by the square of a nonzero element of $k$.

3. $b$ is [[D-O4WWN|nondegenerate]] if and only if $G$ is invertible.
:::

::: {.concept}
See [@Art11].
:::
