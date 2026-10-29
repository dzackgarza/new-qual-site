---
schema: qual/card@1
id: P-AT75W
kind: problem
title: A continuous bijection from a compact space to a Hausdorff space is a homeomorphism
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Hausdorff Spaces
  - Homeomorphisms
  - Counterexamples
relations: []
review: draft
---

::: {.problem}
\envlist

(a) Show that a continuous bijection from a compact space to a Hausdorff space is a homeomorphism.

(b) Give an example that shows that the "Hausdorff" hypothesis in part (a) is necessary.
:::

::: {.concept}
\envlist

- Continuous bijection + open map (or closed map) $\implies$ homeomorphism.

- **Closed** subsets of compact sets are compact.

- The continuous image of a compact set is compact.

- Compact subsets of Hausdorff spaces are closed.
:::

::: {.solution}
Let $f\colon X \to Y$ be a continuous bijection.

::: pf

::: pf-step
(a) If $X$ is compact and $Y$ is Hausdorff, then $f$ is a homeomorphism.

::: pf-proof

::: {.pf-step #closed-map}
$f$ is a closed map.

::: pf-proof
Let $C \subseteq X$ be closed.
A closed subset of a compact space is compact, so $C$ is compact.
The continuous image of a compact set is compact, so $f(C)$ is compact.
A compact subset of a Hausdorff space is closed, so $f(C)$ is closed in $Y$.
:::

:::

::: pf-step
$f^{-1}$ is continuous.

::: pf-proof
For closed $C \subseteq X$, the preimage of $C$ under $f^{-1}$ is $f(C)$, which is closed by step [](#closed-map){.pf-ref}.
:::

:::

:::

:::

::: pf-step
(b) The identity map $f\colon (\theset{1, 2}, \tau_{\mathrm{disc}}) \to (\theset{1, 2}, \tau_{\mathrm{indisc}})$, from the discrete to the indiscrete topology, is a continuous bijection from a compact space that is not a homeomorphism.

::: pf-proof
A finite space has finitely many open sets, so it is compact.
The only open sets of the codomain are $\emptyset$ and $\theset{1, 2}$, whose preimages are open, so $f$ is continuous; it is clearly bijective.
The set $\theset{1}$ is open in the domain, but its image $\theset{1}$ is not open in the codomain, so $f^{-1}$ is not continuous.
The codomain is not Hausdorff, since the only open set containing $1$ also contains $2$.
:::

:::

:::
:::
