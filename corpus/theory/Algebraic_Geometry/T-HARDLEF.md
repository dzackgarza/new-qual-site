---
schema: qual/card@1
id: T-HARDLEF
kind: theorem
title: The hard Lefschetz theorem
classification:
  areas:
  - algebraic-geometry
  topics:
  - Lefschetz Theorems
  - Hodge Theory
  - Cohomology of Varieties
relations:
- kind: related-to
  target: T-LEFHYP
review: draft
prompts:
- What are the weak and hard Lefschetz theorems?
---

::: {.theorem title="Hard Lefschetz"}
Let $X$ be a smooth projective complex variety of dimension $n$, and let $\omega \in H^2(X, \QQ)$ be the class of a hyperplane section.
For every $0 \leq k \leq n$, cup product with $\omega^k$ is an isomorphism
\[
L^k \colon H^{n-k}(X, \QQ) \xrightarrow{\ \sim\ } H^{n+k}(X, \QQ) .
\]
:::

::: {.corollary}
The Betti numbers satisfy $b_{i-2} \leq b_i$ for $i \leq n$, and $H^\bullet(X, \QQ)$ has the \dfn{Lefschetz decomposition} into primitive classes $P^{n-k} = \ker\big(L^{k+1} \colon H^{n-k} \to H^{n+k+2}\big)$:
\[
H^m(X, \QQ) = \bigoplus_{j \geq 0} L^j P^{m-2j} .
\]
:::

::: {.remark}
The weak Lefschetz theorem is the Lefschetz hyperplane theorem [[T-LEFHYP]]: restriction to a smooth hyperplane section $Y$ is an isomorphism $H^i(X) \to H^i(Y)$ for $i < n-1$ and injective for $i = n-1$.
The hard Lefschetz theorem fails for compact complex manifolds that are not Kähler, and for singular projective varieties unless ordinary cohomology is replaced by intersection cohomology.
On a smooth projective curve it says $H^0 \cong H^2$ via the class of a point; on a surface it says $H^1 \cong H^3$ via a hyperplane class, so $b_1 = b_3$, which Poincaré duality also gives.
:::
