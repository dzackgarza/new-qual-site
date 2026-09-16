---
schema: qual/card@1
id: P-AGH3104ETALECOMPL
kind: problem
title: Etale morphisms via completed local rings
classification:
  areas:
  - algebraic-geometry
  topics:
  - Etale Morphisms
  - Complete Local Rings
  - Separable Extensions
relations: []
review: draft
---

::: {.problem}
Show that a morphism $f: X \to Y$ of schemes of finite type over $k$ is étale if and only if the following condition is satisfied.
For each $x \in X$, let $y = f(x)$.
Let $\hat{\mco}_x$ and $\hat{\mco}_y$ be the completions of the local rings at $x$ and $y$.
Choose fields of representatives (II, 8.25A) $k(x) \subseteq \hat{\mco}_x$ and $k(y) \subseteq \hat{\mco}_y$ so that $k(y) \subseteq k(x)$ via the natural map $\hat{\mco}_y \to \hat{\mco}_x$.

The condition is that for every $x \in X$, the field $k(x)$ is a separable algebraic extension of $k(y)$, and the natural map
\[
\hat{\mco}_y \tensor_{k(y)} k(x) \to \hat{\mco}_x
\]
is an isomorphism.
:::
