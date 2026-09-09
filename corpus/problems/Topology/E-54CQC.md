---
schema: qual/card@1
id: E-54CQC
kind: problem
title: Local homeomorphisms of compact Hausdorff spaces are covering maps
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Compactness
  - Homeomorphisms
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: exercise
Show that a surjective local homeomorphism between compact Hausdorff spaces is a covering map.
:::

::: solution
Let $p:E\to B$ be a surjective local homeomorphism, with $E$ compact and $B$ Hausdorff.

<1>1. Every fiber $p^{-1}(b)$ is finite.
::: proof
The fiber is closed in compact $E$, hence compact. For each $x\in p^{-1}(b)$, local homeomorphy gives an open neighborhood $U_x$ on which $p$ is injective, so $U_x\cap p^{-1}(b)=\{x\}$. Thus the fiber is compact and discrete, hence finite.
:::

<1>2. Fix $b\in B$ and write
$$
p^{-1}(b)=\{x_1,\dots,x_r\}.
$$
Choose pairwise disjoint open neighborhoods $U_i$ of the $x_i$ such that each restriction
$$
p|_{U_i}:U_i\longrightarrow p(U_i)
$$
is a homeomorphism onto an open neighborhood of $b$.
::: proof
Local homeomorphy gives such neighborhoods individually, and the Hausdorff property together with finiteness of the fiber allows them to be shrunk to be pairwise disjoint.
:::

<1>3. Put
$$
K=E\setminus\bigcup_{i=1}^r U_i.
$$
Then $K$ is compact, so $p(K)$ is compact and therefore closed in Hausdorff $B$. Since no point of the fiber lies in $K$, we have $b\notin p(K)$.

<1>4. Define
$$
V=(B\setminus p(K))\cap\bigcap_{i=1}^r p(U_i).
$$
Then $V$ is an open neighborhood of $b$ and
$$
p^{-1}(V)=\bigsqcup_{i=1}^r (U_i\cap p^{-1}(V)).
$$
For each $i$, the restriction
$$
p:U_i\cap p^{-1}(V)\longrightarrow V
$$
is a homeomorphism.

<1>5. Thus every $b\in B$ has an evenly covered neighborhood, so $p$ is a covering map.
:::
