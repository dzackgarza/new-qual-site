---
schema: qual/card@1
id: E-4NU4A
kind: problem
title: Injective continuous maps from compact spaces to Hausdorff spaces are embeddings
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
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: exercise
Show that an injective continuous map from a compact space to a Hausdorff space is an embedding (a homeomorphism onto its image).
:::

::: solution
Let $f:X\to Y$ be continuous and injective, with $X$ compact and $Y$ Hausdorff.

<1>1. The corestriction
$$
f:X\longrightarrow f(X)
$$
is a continuous bijection.

<1>2. It is a closed map.
::: proof
If $C\subseteq X$ is closed, then $C$ is compact. Hence $f(C)$ is compact in $Y$, and compact subsets of a Hausdorff space are closed. Therefore $f(C)$ is closed in the subspace $f(X)$.
:::

<1>3. A bijective closed map has continuous inverse. Hence $f:X\to f(X)$ is a homeomorphism, so $f:X\to Y$ is an embedding.
:::
