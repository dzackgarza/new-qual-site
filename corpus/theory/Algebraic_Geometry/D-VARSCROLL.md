---
schema: qual/card@1
id: D-VARSCROLL
kind: definition
title: Rational normal scrolls
classification:
  areas:
  - algebraic-geometry
  topics:
  - Scrolls
  - Rational Normal Curves
  - Projective Bundles
relations: []
review: draft
prompts:
- What is a scroll?
---

::: {.definition title="Rational normal scroll"}
Let $a_1, \ldots, a_k \geq 1$ and $N = \sum_i a_i + k - 1$.
Choose complementary linear subspaces $\PP^{a_1}, \ldots, \PP^{a_k} \subseteq \PP^N$, a rational normal curve $C_i \subseteq \PP^{a_i}$ of degree $a_i$, and isomorphisms $\phi_i \colon \PP^1 \to C_i$.
The \dfn{rational normal scroll} $S(a_1, \ldots, a_k) \subseteq \PP^N$ is the union over $t \in \PP^1$ of the $(k-1)$-planes spanned by $\phi_1(t), \ldots, \phi_k(t)$.
:::

::: {.proposition}
$S(a_1, \ldots, a_k)$ is the image of the projective bundle $\PP\big(\OO_{\PP^1}(a_1) \oplus \cdots \oplus \OO_{\PP^1}(a_k)\big)$ under the complete linear system of its tautological bundle $\OO(1)$.
It is a smooth variety of dimension $k$ and degree $\sum_i a_i$, and its projective equivalence class depends only on the multiset $\{a_1, \ldots, a_k\}$.
:::

::: {.example}
$S(1,1) \subseteq \PP^3$ is the smooth quadric surface, ruled by the lines joining corresponding points of two skew lines.
$S(1,2) \subseteq \PP^4$ is the cubic scroll, the blowup of $\PP^2$ at a point embedded by the conics through that point.
Allowing $a_i = 0$ gives cones: $S(0,2)$ is the quadric cone over a conic.
:::

::: {.remark}
More generally, a \dfn{scroll} is a projective variety $X \subseteq \PP^N$ with a morphism $X \to B$ onto a variety $B$ whose fibres are linear subspaces of $\PP^N$ of a fixed dimension.
:::
