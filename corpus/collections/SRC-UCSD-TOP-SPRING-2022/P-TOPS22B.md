---
schema: qual/card@1
id: P-TOPS22B
kind: problem
title: 'Manifold realizability of $S^2\vee S^3\vee S^5$'
classification:
  areas:
  - topology
  topics:
  - Homotopy Type
  - Manifolds
  - Wedge Product
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: source-checked
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
Determine whether $X = S^2 \vee S^3 \vee S^5$ is homotopy equivalent to:

(a) a **closed manifold** (compact, without boundary),
(b) a **manifold** (with or without boundary).
:::

::: {.solution}

::: pf

::: pf-step
With coefficients in $\mathbb F_2$, the only nonzero reduced cohomology groups of
$X=S^2\vee S^3\vee S^5$ occur in degrees $2,3,5$, and every cup product of two positive-degree classes is zero.

:::

::: pf-step
Part (a): $X$ is not homotopy equivalent to a closed manifold.

::: pf-proof

::: pf-step
Suppose that $X\simeq M$ for a connected closed $n$-manifold $M$.
:::

::: pf-step
Poincaré duality over $\mathbb F_2$ gives $H_n(M;\mathbb F_2)\cong\mathbb F_2$, independently of orientability. Since $H_k(X;\mathbb F_2)=0$ for $k>5$, this forces $n\le5$.
:::

::: pf-step
Since $H_5(X;\mathbb F_2)\ne0$ and an $n$-manifold has no homology above degree $n$, we also have $n\ge5$. Thus $n=5$.
:::

::: pf-step
Poincaré duality then makes the pairing
$$
H^2(M;\mathbb F_2)\times H^3(M;\mathbb F_2)
\xrightarrow{\smile} H^5(M;\mathbb F_2)\cong\mathbb F_2
$$
nondegenerate.
:::

::: pf-step
But the corresponding product on $X$ is identically zero. Since a homotopy equivalence induces an isomorphism of cohomology rings, this is impossible.
:::

::: pf-step
Hence the answer to (a) is **no**.
:::

:::

:::

::: pf-step
Part (b): $X$ is homotopy equivalent to a manifold with boundary.

::: pf-proof

::: pf-step
The wedge $X$ is a finite simplicial complex after choosing compatible triangulations of the three spheres.
:::

::: pf-step
Embed this finite complex piecewise-linearly in some Euclidean space $\mathbb R^N$ of sufficiently large dimension.
:::

::: pf-step
A closed regular neighborhood $N(X)$ of the embedded complex is a compact PL manifold with boundary and collapses onto $X$.
:::

::: pf-step
Therefore the inclusion $X\hookrightarrow N(X)$ is a homotopy equivalence.
:::

::: pf-step
Hence the answer to (b) is **yes**.
:::

:::

:::

:::

:::
