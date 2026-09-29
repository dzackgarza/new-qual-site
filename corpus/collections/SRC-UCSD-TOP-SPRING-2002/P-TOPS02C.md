---
schema: qual/card@1
id: P-TOPS02C
kind: problem
title: "Homology, cohomology, and cup product of a space from edge identifications of a square"
classification:
  areas:
  - topology
  topics:
  - Homology
  - Cohomology
  - Cup Product
  - Cell Complexes
relations: []
review: draft
---

::: {.problem}
Consider the space $X$ obtained by identifying the edges of the unit square in the following manner: edges labeled $a$ are identified with matching orientation, and edges labeled $b$ are identified with matching orientation.

(a) Compute $H_*(X; \mathbb{Z})$ and $H^*(X; \mathbb{Z})$.

(b) Prove $X$ is an orientable manifold.

(c) Compute the ring structure of $H^*(X; \mathbb{Z})$.
:::

::: {.solution}

::: pf

::: pf-step

The quotient is the torus $T^2$.

::: pf-proof

Identifying each pair of opposite edges of the square with matching orientations gives the standard square model of $S^1\times S^1$.

:::

:::

::: pf-step

With the standard CW structure having one $0$-cell, two $1$-cells $a,b$, and one $2$-cell, all cellular boundary maps vanish.

::: pf-proof

The $1$-cells are loops, so $\partial_1=0$. The attaching word of the $2$-cell is $aba^{-1}b^{-1}$, whose exponent sum in each $1$-cell is zero, so $\partial_2=0$.

:::

:::

::: {.pf-step #s3}

Hence
$$
H_k(X;\mathbb Z)\cong H^k(X;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&k=0,2,\\
\mathbb Z^2,&k=1,\\
0,&\text{otherwise}.
\end{cases}
$$

::: pf-proof

Take homology of the cellular chain complex, and then apply the universal coefficient theorem; all homology groups are free.

:::

:::

::: pf-step

The quotient is an orientable $2$-manifold.

::: pf-proof

It is homeomorphic to $T^2=S^1\times S^1$, a product of oriented $1$-manifolds, hence an orientable surface.

:::

:::

::: {.pf-step #s5}

If $\alpha,\beta\in H^1(X;\mathbb Z)$ are the classes dual to the two circle factors and $\omega\in H^2(X;\mathbb Z)$ is the orientation class, then
$$
\alpha^2=\beta^2=0,\qquad \alpha\smile\beta=\omega,\qquad \beta\smile\alpha=-\omega.
$$

::: pf-proof

By the Künneth theorem, $\alpha$ and $\beta$ are pulled back from the two factors. Their squares vanish because $H^2(S^1)=0$. Their product is the external product of the two degree-one generators and evaluates as $1$ on the product fundamental class. Graded commutativity gives the final sign.

:::

:::

::: pf-step

Thus
$$
\boxed{H^*(X;\mathbb Z)\cong \Lambda_{\mathbb Z}(\alpha,\beta),\qquad |\alpha|=|\beta|=1.}
$$

::: pf-proof

The additive groups and products are exactly those described in steps [](#s3){.pf-ref} and [](#s5){.pf-ref}.

:::

:::

:::

:::
