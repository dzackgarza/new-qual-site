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

::: problem
Let $X \subset \AA^n,\, Y\subset \AA^m$ be irreducible affine varieties, and show that $X\cross Y\subset \AA^{n+m}$ is irreducible.
:::

::: solution
That $X\cross Y$ is again an affine variety follows from writing $X=V(I)$ and $Y=V(J)$; then $X\cross Y = V(I+J)$ where $I+J\normal k[x_1, \cdots, x_n, y_1, \cdots, y_m]$.
So let
\[
X\cross Y = U \union V
\]
with $U, V$ proper and closed, and let $\pi_X, \pi_Y$ be the projections onto the factors.

**Claim**: for each $x\in X$, $\pi_X^{-1}(x) \cong Y$ is contained in only one of $U$ or $V$.

If this is true, we can write $X = G_U \union G_V$ where
\[
G_U\da \ts{x\in X \st \pi_X^{-1}(x) \subseteq U}
\]
are the points for which the entire fiber lies in $U$, and similarly $G_V$ are those for which the fiber lies in $V$.
If we can then show that $G_U, G_V$ are closed, irreducibility of $X$ forces (without loss of generality) $G_V = \emptyset$ and $X = G_U$.
But then
\[
\pi_X^{-1}(X) = X\cross Y \text{ and }\pi_X^{-1}(G_U) = U  \implies X\cross Y = U
,\]
which shows that $X\cross Y$ is irreducible.

*Every fiber is contained in one irreducible component*:
for any fixed $x$,
\[
\pi_X^{-1}(x) = \qty{\pi_X^{-1}(x) \intersect U } \union \qty{\pi_X^{-1}(x) \intersect V}
.\]
Since points are closed in the Zariski topology and $\pi_X$ is continuous, each $\pi_X^{-1}(x)$ is closed, and thus $\pi_X^{-1}(x)\intersect U$ is closed (and similarly for $V$).
Noting that $\pi_X^{-1}(x) \cong \ts{x}\cross Y \cong Y$, where $Y$ was assumed irreducible, we conclude without loss of generality that $\pi_X^{-1}(x) \intersect V = \emptyset$.

*$G_U, G_V$ are closed*:
without loss of generality consider $G_U \subseteq X$.
Fixing any point $y_0 \in Y$,
\[
X\cong X_{y_0} \da X\cross \ts{y_0} \subseteq X\cross Y
,\]
so we can identify $G_U \subset X$ with $G_U\subset X_{y_0}$ inside a $Y\dash$fiber of the product.
But then
\[
G_U = X_{y_0} \intersect U \subseteq X\cross Y
,\]
where $U$ is closed in $X\cross Y$ and thus closed in $X_{y_0}$, and $X_{y_0}$ is trivially closed in itself.
This exhibits $G_U$ as the intersection of two sets closed in $X_{y_0} \cong X$.
:::
