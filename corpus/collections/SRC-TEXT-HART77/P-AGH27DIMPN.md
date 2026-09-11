---
schema: qual/card@1
id: P-AGH27DIMPN
kind: problem
title: $\dim \PP^n = n$, and a quasi-projective variety has the dimension of its closure
classification:
  areas:
  - algebraic-geometry
  topics:
  - Dimension
  - Projective Varieties
  - Quasi-Projective Varieties
relations:
- kind: uses
  target: P-AGH26HOMDIM
review: draft
---

::: problem
1. Show that $\dim \PP^n = n$.

2. If $Y \subseteq \PP^n$ is a quasi-projective variety, show that $\dim Y = \dim \bar{Y}$.
:::

::: solution
**Part 1.** By the previous exercise, $\dim S(\PP^n) = \dim \PP^n + 1$, and
\[
\dim S(\PP^n) = \trdeg_k k[x_0,\ldots,x_n] = n+1 ,
\]
so $\dim \PP^n = n$.

Alternatively, take the standard open cover $\ts{U_i} \covers \PP^n$.
Each chart satisfies $\dim U_i = \dim U_0 = \dim \AA^n = n$, using the identification $\tv{x_0 : \cdots : x_n} \mapsto \qty{x_1/x_0, \ldots, x_n/x_0}$, and $\dim \PP^n = \sup_i \dim U_i = n$.

**Part 2.** Pass to the affine cone.
Since $\dim C(Y) = \dim Y + 1$, it suffices to prove $\dim C(Y) = \dim \overline{C(Y)}$, and $C(Y)$ is quasi-affine, so this is the affine statement.

That affine statement goes as follows.
Pick a chain $Z_0 < Z_1 < \cdots < Z_n$ of irreducible closed subsets witnessing $\dim Y = n$, and take closures to get a chain $\bar{Z}_0 < \cdots < \bar{Z}_n$ in $\bar{Y}$, which gives $\dim Y \leq \dim \bar{Y}$.
Now $Z_0 = \bar{Z}_0 = P$ is a point, corresponding to a maximal ideal $\mfm \in \mspec A(\bar{Y})$, and the $\bar{Z}_i$ correspond to primes $\mfp_i \in \spec A(\bar{Y})$ with $\mfp_i \subset \mfm$.
The chain has length $n$, so $\height \mfm = n$.
Apply the height-quotient formula:
\[
\height \mfm + \dim A(\bar{Y})/\mfm = \dim A(\bar{Y})
\implies n + \dim k = \dim A(\bar{Y})
\implies \dim A(\bar{Y}) = n .
\]
:::
