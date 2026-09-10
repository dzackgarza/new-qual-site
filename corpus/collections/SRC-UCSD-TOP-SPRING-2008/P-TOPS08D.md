---
schema: qual/card@1
id: P-TOPS08D
kind: problem
title: "Degree of a map that is a local orientation-preserving homeomorphism on preimages"
classification:
  areas:
  - topology
  topics:
  - Degree
  - Manifolds
relations: []
review: draft
---

::: problem
Let $M^n$ and $N^n$ be compact, oriented, boundaryless manifolds of dimension $n$ with fundamental classes $[M]$ and $[N]$ respectively.
Assume that $f : M^n \to N^n$ is a continuous map, and $U \subset N^n$ is an open set with the property that $f^{-1}(U) = \bigsqcup U_i$ is a finite disjoint union, such that $f$ restricts to an orientation preserving homeomorphism $f : U_i \to U$.
Show that $f_*([M]) = k [N]$.
:::

::: {.solution}
<1>1. Let $k$ be the number of components $U_i$ of $f^{-1}(U)$.
::: {.proof}
This number is finite by hypothesis.
:::

<1>2. Choose a point $y\in U$. Then $f^{-1}(y)$ consists of exactly one point in each $U_i$, so has $k$ points.
::: {.proof}
Each restriction $f|_{U_i}:U_i\to U$ is a homeomorphism, hence has exactly one preimage of $y$.
:::

<1>3. The local degree of $f$ at every point of $f^{-1}(y)$ is $+1$.
::: {.proof}
Each restriction $f|_{U_i}$ is an orientation-preserving homeomorphism. The induced map on the local orientation group is therefore multiplication by $+1$.
:::

<1>4. Consequently $\deg f=k$.
::: {.proof}
For a map between closed oriented $n$-manifolds, the degree is the sum of local degrees over the preimages of any point for which the map is locally a homeomorphism near every preimage. By <1>2--<1>3 this sum is $k$.
:::

<1>5. Hence
$$
\boxed{f_*[M]=k[N].}
$$
::: {.proof}
The degree is defined by $f_*[M]=(\deg f)[N]$. Apply <1>4.
:::
:::
