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
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Every step now carries a pf-proof: the two containers state why their subclaims suffice, and the 12
    leaf steps that asserted a claim with no justification each carry a sentence deriving it. The
    mathematics is unchanged and was re-read: the reduced cohomology of a wedge as the direct sum of the
    summands with componentwise products, Poincare duality over F_2 forcing n = 5 and a nondegenerate
    pairing H^2 x H^3 -> H^5, the contradiction with the vanishing products on X, and the regular
    neighbourhood of a finite complex as a compact manifold with boundary collapsing onto it. Checked
    against the statement on the card, from the UCSD Spring 2022 topology qualifying exam. No published
    solution is cited, so the argument is the card's own. Nothing in the statement was changed.
---

::: {.problem}
Determine whether $X = S^2 \vee S^3 \vee S^5$ is homotopy equivalent to:

(a) a **closed manifold** (compact, without boundary),
(b) a **manifold** (with or without boundary).
:::

::: {.solution}

::: pf

::: pf-step
With coefficients in $\FF_2$, the only nonzero reduced cohomology groups of
$X=S^2\vee S^3\vee S^5$ occur in degrees $2,3,5$, and every cup product of two positive-degree classes is zero.

::: pf-proof
For a wedge the reduced cohomology is the direct sum of the reduced cohomology of the summands, so $\tilde H^*(X;\FF_2)$ is $\FF_2$ in degrees $2,3,5$ and vanishes elsewhere. Under this decomposition the cup product is computed summand by summand, and the cohomology of each summand is concentrated in a single positive degree, so the product of two classes of positive degree vanishes.
:::

:::

::: pf-step
Part (a): $X$ is not homotopy equivalent to a closed manifold.

::: pf-proof
The subclaims pin the dimension a closed model would have to have, and then contradict Poincaré duality with the vanishing products computed above.

::: pf-step
Suppose that $X\simeq M$ for a connected closed $n$-manifold $M$.

::: pf-proof
This is the hypothesis of part (a): $M$ is a connected closed $n$-manifold and the homotopy equivalence is the one whose existence is to be refuted.
:::

:::

::: pf-step
Poincaré duality over $\FF_2$ gives $H_n(M;\FF_2)\cong\FF_2$, independently of orientability. Since $H_k(X;\FF_2)=0$ for $k>5$, this forces $n\le5$.

::: pf-proof
For a closed connected $n$-manifold $H_n(M;\FF_2)\cong\FF_2$ whether or not $M$ is orientable. A homotopy equivalence gives $H_n(M;\FF_2)\cong H_n(X;\FF_2)$, which vanishes for $n>5$ by the first step of the proof, so $n\le5$.
:::

:::

::: pf-step
Since $H_5(X;\FF_2)\ne0$ and an $n$-manifold has no homology above degree $n$, we also have $n\ge5$. Thus $n=5$.

::: pf-proof
An $n$-manifold has $H_k(M;\FF_2)=0$ for $k>n$; since $H_5(X;\FF_2)\ne0$ and $X\simeq M$, the degree $5$ does not exceed $n$. With $n\le5$ this gives $n=5$.
:::

:::

::: pf-step
Poincaré duality then makes the pairing
$$
H^2(M;\FF_2)\times H^3(M;\FF_2)
\xrightarrow{\smile} H^5(M;\FF_2)\cong\FF_2
$$
nondegenerate.

::: pf-proof
Poincaré duality over the field $\FF_2$ identifies $H^k(M;\FF_2)$ with the dual of $H^{5-k}(M;\FF_2)$ through the cup product pairing into $H^5(M;\FF_2)\cong\FF_2$, which is precisely the nondegeneracy of the displayed pairing.
:::

:::

::: pf-step
But the corresponding product on $X$ is identically zero. Since a homotopy equivalence induces an isomorphism of cohomology rings, this is impossible.

::: pf-proof
The first step of the proof shows that every product of two positive-degree classes in $H^*(X;\FF_2)$ vanishes. The groups $H^2(M;\FF_2)\cong H_3(X;\FF_2)$ and $H^3(M;\FF_2)\cong H_2(X;\FF_2)$ are non-zero, so a nondegenerate pairing between them cannot be identically zero; a homotopy equivalence preserves cup products, so the two pairings cannot differ.
:::

:::

::: pf-step
Hence the answer to (a) is **no**.

::: pf-proof
The supposition that a closed manifold is homotopy equivalent to $X$ led to a contradiction, so no such manifold exists.
:::

:::

:::

:::

::: pf-step
Part (b): $X$ is homotopy equivalent to a manifold with boundary.

::: pf-proof
The subclaims use a closed regular neighbourhood of a finite complex, which is a compact manifold with boundary collapsing onto the complex.

::: pf-step
The wedge $X$ is a finite simplicial complex after choosing compatible triangulations of the three spheres.

::: pf-proof
Each $S^k$ is the boundary of a $(k+1)$-simplex, hence a finite simplicial complex; identifying one vertex of each gives a finite simplicial complex whose underlying space is the wedge.
:::

:::

::: pf-step
Embed this finite complex piecewise-linearly in some Euclidean space $\RR^N$ of sufficiently large dimension.

::: pf-proof
A finite simplicial complex with $n_0$ vertices embeds piecewise-linearly in $\RR^{2n_0+1}$ by a simplexwise-linear general-position map, so some $N$ suffices.
:::

:::

::: pf-step
A closed regular neighborhood $N(X)$ of the embedded complex is a compact PL manifold with boundary and collapses onto $X$.

::: pf-proof
This is the regular neighbourhood theorem: a finite complex embedded piecewise-linearly in $\RR^N$ has a closed regular neighbourhood, which is a compact PL manifold with boundary carrying a collapse onto the complex.
:::

:::

::: pf-step
Therefore the inclusion $X\hookrightarrow N(X)$ is a homotopy equivalence.

::: pf-proof
A collapse is a homotopy equivalence, and the collapse of $N(X)$ onto $X$ restricts to the identity on $X$, so the inclusion is a homotopy inverse to it.
:::

:::

::: pf-step
Hence the answer to (b) is **yes**.

::: pf-proof
$N(X)$ is a compact manifold with boundary and the inclusion of $X$ into it is a homotopy equivalence, which is exactly what part (b) asks for.
:::

:::

:::

:::

:::

:::
