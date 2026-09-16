---
schema: qual/card@1
id: PR-7OT2Z
kind: proposition
title: The ideal-variety correspondence
classification:
  areas:
  - algebraic-geometry
  topics:
  - Varieties
  - Nullstellensatz
  - Prime Ideals
relations:
- kind: uses
  target: T-JRTS2
review: draft
prompts:
- Which ideals correspond to closed subsets of $\AA^n$?
- Which ideals correspond to irreducible closed subsets?
- What is the coordinate ring of a closed subset, and when is it a domain?
- Show that the algebraic sets are the closed sets of a topology on $\AA^n$.
- Show that the maximal ideals of $k[x_1,\ldots,x_n]$ are the ideals $(x_1-a_1,\ldots,x_n-a_n)$ when $k$ is algebraically closed, and that this fails otherwise.
- Show that every finitely generated $k$-algebra that is a domain is the coordinate ring of an affine variety.
---

::: {.proposition}
Over an algebraically closed field $k$, the maps $V$ and $I$ are mutually inverse, order-reversing bijections between the radical ideals of $k[x_1,\ldots,x_n]$ and the Zariski-closed subsets of $\AA^n$.
Under that bijection:

| Ideal $J$ | Closed set $V(J)$ |
| --- | --- |
| radical | closed |
| prime | irreducible |
| maximal | a point |
| $(1)$ | $\emptyset$ |
| $(0)$ | $\AA^n$ |
:::

::: {.proposition title="Operations on vanishing sets and ideals"}
Let $\mfa, \mfa_1, \mfa_2$ and $\mfa_i$ ($i \in I$) be ideals of $A \da k[x_1,\ldots,x_n]$, and let $Y_j$ ($j \in J$) be subsets of $\AA^n$.
Then
\[
\bigcap_{i \in I} V(\mfa_i) = V\Big(\sum_{i \in I} \mfa_i\Big), \qquad
V(\mfa_1) \union V(\mfa_2) = V(\mfa_1 \mfa_2), \qquad
\AA^n \sm V(\mfa) = \bigcup_{f \in \mfa} D(f), \qquad
D(fg) = D(f) \intersect D(g),
\]
\[
I\Big(\bigcup_{j \in J} Y_j\Big) = \bigcap_{j \in J} I(Y_j), \qquad
V(I(Y)) = \overline{Y} \text{ for } Y \subseteq \AA^n .
\]
If $k$ is algebraically closed, then $V(\mfa_1) \subseteq V(\mfa_2)$ if and only if $\sqrt{\mfa_1} \supseteq \sqrt{\mfa_2}$.
[@Har10a, §I.1]
:::

::: {.proposition title="Maximal ideals and coordinate rings"}
Let $k$ be algebraically closed.
The maximal ideals of $k[x_1,\ldots,x_n]$ are exactly the ideals $(x_1 - a_1, \ldots, x_n - a_n)$ with $(a_1,\ldots,a_n) \in \AA^n$, and they correspond to the points of $\AA^n$.
For an affine variety $Y$ the coordinate ring $A(Y)$ is a finitely generated $k$-algebra and a domain; conversely, every finitely generated $k$-algebra that is a domain is $A(Y)$ for some affine variety $Y$.
[@Har10a, §I.1]
:::

::: {.example}
Over $k = \RR$ the ideal $(x^2+1) \subseteq \RR[x]$ is maximal and is not of the form $(x - a)$.
:::

::: {.remark}
The correspondence is what turns a geometric question into a computation in a ring, so the useful direction on an exam is usually right to left: $V(J)$ is irreducible exactly when $J$ is prime, which is a question about $k[x_1,\ldots,x_n]/J$ being a domain.

For a closed $X \subseteq \AA^n$ the coordinate ring is $k[X] \da k[x_1,\ldots,x_n]/I(X)$, the polynomial functions restricted to $X$, and the same dictionary reappears inside it: closed subsets of $X$ correspond to radical ideals of $k[X]$, and $X$ is irreducible exactly when $k[X]$ is a domain.
:::
