---
schema: qual/card@1
id: P-AT75W
kind: problem
title: Spring 2009, 31
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

a. Show that a continuous bijection from a compact space to a Hausdorff space is a homeomorphism.

b. Give an example that shows that the "Hausdorff" hypothesis in part (a) is necessary.
:::

::: {.concept}
\envlist

- Continuous bijection + open map (or closed map) $\implies$ homeomorphism.

- **Closed** subsets of compact sets are compact.

- The continuous image of a compact set is compact.

- Compact subsets of Hausdorff spaces are closed.
:::

::: {.solution}
\envlist

::: {.proof title="of a"}
We'll show that $f$ is a closed map.

Let $U \in X$ be closed.

- Since $X$ is compact, $U$ is compact

- Since $f$ is continuous, $f(U)$ is compact

- Since $Y$ is Hausdorff, $f(U)$ is closed.
:::

::: {.proof title="of b"}
Note that any finite space is compact: a finite set has only finitely many open sets, so every open cover is finite and admits a finite subcover (the cover itself).

Take $f: ([2], \tau_1) \to ([2], \tau_2)$ to be the identity map, where $\tau_1$ is the discrete topology and $\tau_2$ is the indiscrete topology.
Any map into an indiscrete topology is continuous, since the only open sets in the codomain are $\emptyset$ and $[2]$, whose preimages ($\emptyset$ and $[2]$) are open in $\tau_1$.
The identity map is a bijection.

Let $g$ be the inverse map; then note that $1 \in \tau_1$ but $g\inv(1) = 1$ is not in $\tau_2$, so $g$ is not continuous.
:::
:::
