---
schema: qual/card@1
id: P-AGXGATHPRODIRR
kind: problem
title: Products of irreducible affine varieties are irreducible
classification:
  areas:
  - algebraic-geometry
  topics:
  - Irreducibility
  - Products of Varieties
  - Fibers
relations: []
review: draft
---

::: {.problem}
Let $X \subset \AA^n,\, Y\subset \AA^m$ be irreducible affine varieties, and show that $X\cross Y\subset \AA^{n+m}$ is irreducible.
:::

::: {.solution}
Write $X=V(I)\subseteq\AA^n$ and $Y=V(J)\subseteq\AA^m$. Then $X\cross Y=V(I+J)$ in $\AA^{n+m}$, where $I$ and $J$ are extended to $k[x_1,\dots,x_n,y_1,\dots,y_m]$; so $X\cross Y$ is an affine variety, and it is nonempty because $X$ and $Y$ are. For $x\in X$ and $y\in Y$, the maps $\iota_x\colon Y\to X\cross Y$, $y'\mapsto(x,y')$, and $j_y\colon X\to X\cross Y$, $x'\mapsto(x',y)$, are given by polynomials, hence are continuous for the Zariski topologies.

::: pf

::: {.pf-step #fibre-in-one}
Let $X\cross Y=Z_1\union Z_2$ with $Z_1,Z_2$ closed. Then for each $x\in X$, the fibre $\theset{x}\cross Y$ lies in $Z_1$ or in $Z_2$.

::: pf-proof
We have $Y=\iota_x^{-1}(Z_1)\union\iota_x^{-1}(Z_2)$, a union of two closed subsets of $Y$. Since $Y$ is irreducible, one of them is all of $Y$, so $\theset{x}\cross Y=\iota_x(Y)$ lies in the corresponding $Z_l$.
:::

:::

::: {.pf-step #G-closed}
For $l=1,2$, the set $G_l\coloneqq\theset{x\in X\st \theset{x}\cross Y\subseteq Z_l}$ is closed in $X$.

::: pf-proof
A point $x$ lies in $G_l$ exactly when $(x,y)\in Z_l$ for every $y\in Y$, so
$$
G_l=\Intersect_{y\in Y} j_y^{-1}(Z_l)
.$$
Each $j_y^{-1}(Z_l)$ is closed in $X$ because $j_y$ is continuous, and an intersection of closed sets is closed.
:::

:::

::: {.pf-step #X-is-G}
$X=G_1$ or $X=G_2$.

::: pf-proof
By step [](#fibre-in-one){.pf-ref}, $X=G_1\union G_2$. By step [](#G-closed){.pf-ref} both are closed, and $X$ is irreducible, so one of them equals $X$.
:::

:::

::: pf-qed
By step [](#X-is-G){.pf-ref}, say $X=G_1$. Then every fibre $\theset{x}\cross Y$ with $x\in X$ lies in $Z_1$, and these fibres cover $X\cross Y$, so $X\cross Y=Z_1$. Hence the nonempty space $X\cross Y$ is not a union of two proper closed subsets, so it is irreducible.
:::

:::
:::
