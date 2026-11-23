---
schema: qual/card@1
id: D-VARBIRAT
kind: definition
title: Rational and birational maps, and the function field
classification:
  areas:
  - algebraic-geometry
  topics:
  - Rational Maps
  - Birational Geometry
  - Function Field
relations:
- kind: uses
  target: D-VARREG
- kind: related-to
  target: T-BIRINV
review: draft
prompts:
- What is a rational map?
- When are two varieties birational?
- Which varieties are birational exactly when their function fields are isomorphic?
---

::: {.definition title="rational map"}
Let $X$ and $Y$ be varieties over a field $k$.
A \dfn{rational map} $\varphi\colon X\dashrightarrow Y$ is an equivalence class of pairs $(U,\varphi_U)$ with $U\subseteq X$ a nonempty open subset and $\varphi_U\colon U\to Y$ a morphism, two pairs being equivalent when they agree on the intersection of their domains [@Har77, §I.4].
The rational map is \dfn{dominant} if its image is dense in $Y$.
:::

::: {.definition title="birational"}
A \dfn{birational map} $\varphi\colon X\dashrightarrow Y$ is a rational map admitting a rational inverse: a rational map $\psi\colon Y\dashrightarrow X$ with $\psi\circ\varphi=\id_X$ and $\varphi\circ\psi=\id_Y$.
Two varieties are \dfn{birational}, or birationally equivalent, when such a map exists between them [@Har77, §I.4, where both definitions are unnumbered].
:::

::: {.theorem title="Function fields and birational equivalence"}
Two varieties $X$ and $Y$ over $k$ are birational if and only if $k(X)\cong k(Y)$ as extensions of $k$ [@Har77, Corollary I.4.5].
The dominant rational maps $X\dashrightarrow Y$ correspond to the $k$-algebra homomorphisms $k(Y)\to k(X)$, so varieties with dominant rational maps are contravariantly equivalent to finitely generated field extensions of $k$ [@Har77, Theorem I.4.4].
:::

::: {.proposition title="Indeterminacy in codimension two"}
A rational map from a nonsingular variety $X$ to a projective variety $Y$ is defined outside a closed subset of $X$ of codimension at least two.
:::

::: {.proof}
A rational map to $\PP^n$ is given on a dense open set by an $(n+1)$-tuple of rational functions; at a point $\eta$ of codimension one the local ring $\OO_{X,\eta}$ is a discrete valuation ring, so multiplying the tuple by a common denominator gives a regular tuple at $\eta$, and a closed immersion $Y\subseteq\PP^n$ pulls the map back to $Y$ [@Vak25, Exercise 15.3.B].
:::
