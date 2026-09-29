---
schema: qual/card@1
id: E-7DSGZ
kind: problem
title: An injective continuous map from a compact space to a Hausdorff space is an
  embedding
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Hausdorff Spaces
  - Homeomorphisms
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.exercise}
Show that an injective continuous map from a compact space to a Hausdorff space is an embedding (a homeomorphism onto its image).
:::

::: {.solution}
**Goal:** Show that an injective continuous map $f: X \to Y$ from a compact space $X$ to a Hausdorff space $Y$ is an embedding: a homeomorphism onto its image.

::: pf

::: {.pf-step #s1}
$f: X \to f(X)$ is a continuous bijection.

::: pf-proof
$f$ is injective by hypothesis, so viewed as a map onto its image it is bijective; continuity is inherited.
:::

:::

::: pf-step
$f(X)$ is Hausdorff.

::: pf-proof
Subspaces of Hausdorff spaces are Hausdorff, and $Y$ is Hausdorff.
:::

:::

::: {.pf-step #s3}
$f$ maps closed sets to closed sets (in $f(X)$).

::: pf-proof

::: pf-step
Let $C \subseteq X$ be closed; then $C$ is compact.

::: pf-proof
Closed subsets of compact spaces are compact.
:::

:::

::: pf-step
$f(C)$ is compact in $Y$.

::: pf-proof
Continuous images of compact sets are compact.
:::

:::

::: pf-step
$f(C)$ is closed in $Y$, hence closed in $f(X)$.

::: pf-proof
Compact subsets of Hausdorff spaces are closed; and closed in $Y$ implies closed in the subspace $f(X)$.
:::

:::

:::

:::

::: {.pf-step #s4}
$f^{-1}: f(X) \to X$ is continuous.

::: pf-proof
A bijective map is a homeomorphism iff it is a closed map (equivalently: $f^{-1}$ is continuous iff for every closed $C \subseteq X$, $(f^{-1})^{-1}(C) = f(C)$ is closed in $f(X)$), and step [](#s3){.pf-ref} gives closedness.
:::

:::

::: pf-qed
step [](#s1){.pf-ref} and step [](#s4){.pf-ref} show $f: X \to f(X)$ is a homeomorphism, i.e. $f$ is an embedding.
:::

:::

:::
