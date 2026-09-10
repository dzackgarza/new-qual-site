---
schema: qual/card@1
id: E-Q8TYL
kind: problem
title: Compactness under comparable topologies
classification:
  areas:
  - topology
  topics:
  - Compactness
relations: []
review: draft
---

::: {.exercise}

(a) Let $\mathcal{T}$ and $\mathcal{T}'$ be two topologies on the set $X$; suppose that $\mathcal{T}' \supset \mathcal{T}$.
What does compactness of $X$ under one of these topologies imply about compactness under the other?

(b) Show that if $X$ is compact Hausdorff under both $\mathcal{T}$ and $\mathcal{T}'$, then either $\mathcal{T}$ and $\mathcal{T}'$ are equal or they are not comparable.
:::

::: {.solution}
(a) If \(\mathcal T'\supset\mathcal T\), every \(\mathcal T\)-open cover is also a \(\mathcal T'\)-open cover. Hence compactness for the finer topology \(\mathcal T'\) implies compactness for the coarser topology \(\mathcal T\). The converse need not hold; for example, an infinite set with the indiscrete topology is compact, while the discrete topology is not compact.

(b) Suppose both topologies are compact Hausdorff and are comparable, say \(\mathcal T'\supset\mathcal T\). The identity map
\[
\operatorname{id}:(X,\mathcal T')\longrightarrow (X,\mathcal T)
\]
is continuous and bijective. A continuous bijection from a compact space to a Hausdorff space is a homeomorphism, so \(\mathcal T'=\mathcal T\). Therefore, if the two compact Hausdorff topologies are distinct, they cannot be comparable.
:::
