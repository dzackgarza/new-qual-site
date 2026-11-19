---
schema: qual/card@1
id: D-SCHNORM
kind: definition
title: The normalization of an integral scheme
classification:
  areas:
  - algebraic-geometry
  topics:
  - Normal Schemes
  - Normalization
  - Integral Extensions
relations:
- kind: uses
  target: D-QJ5M9
review: draft
prompts:
- What is the normalization of an integral scheme?
- Why does the normalization exist?
- Which universal property characterises the normalization?
---

::: {.definition title="normalization"}
Let $X$ be an integral scheme.
For each open affine subset $U=\Spec A\subseteq X$ with quotient field $K$, let $\tilde A$ be the integral closure of $A$ in $K$, and let $\tilde U=\Spec\tilde A$.
The \dfn{normalization} of $X$ is the morphism $\nu\colon\tilde X\to X$ obtained by gluing the morphisms $\tilde U\to U$ over an affine cover [@Har77, Exercise II.3.8, p. 91].
:::

::: {.proposition}
$\tilde X$ is a normal integral scheme and $\nu$ is integral and surjective [@Har77, Exercise II.3.8, p. 91].
The normalization is characterized by a universal property: every dominant morphism $Z\to X$ from a normal integral scheme factors uniquely through $\nu$, so $\nu$ is the initial object among dominant morphisms to $X$ from normal integral schemes ([[D-QJ5M9]]).
:::
