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
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §26 Exercise 1, printed p. 170, with Theorem 26.2
    and Theorem 26.3; both parts are stored as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 26.1, PDF p. 12. Compactness passes from a finer
    to a coarser topology; conversely two comparable compact Hausdorff topologies coincide,
    since a set closed in the finer one is compact and hence closed in the coarser.
    (tmp/sources/munkres-solutions-positron-ch3.pdf).
---

::: {.exercise}

(a) Let $\mathcal{T}$ and $\mathcal{T}'$ be two topologies on the set $X$; suppose that $\mathcal{T}' \supset \mathcal{T}$.
What does compactness of $X$ under one of these topologies imply about compactness under the other?

(b) Show that if $X$ is compact Hausdorff under both $\mathcal{T}$ and $\mathcal{T}'$, then either $\mathcal{T}$ and $\mathcal{T}'$ are equal or they are not comparable.
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 26.1, PDF p. 12** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); both parts are theirs.

(a) If $\mathcal{T}\subset\mathcal{T}'$ and $(X,\mathcal{T}')$ is compact, then every open cover of $X$ by sets of $\mathcal{T}'$ has a finite subcover; in particular every $\mathcal{T}$-cover, since $\mathcal{T}$-open sets are $\mathcal{T}'$-open. So $(X,\mathcal{T})$ is compact. The converse fails: the two-point set is compact with the indiscrete topology and not with the discrete one.

(b) Suppose $\mathcal{T}\subset\mathcal{T}'$ and both are compact Hausdorff topologies. Let $A\in\mathcal{T}'$; then $X-A$ is closed in $(X,\mathcal{T}')$, hence compact by Theorem 26.2, hence compact as a subset of $(X,\mathcal{T})$ by (a), hence closed in $(X,\mathcal{T})$ by Theorem 26.3, so $A$ is $\mathcal{T}$-open. Thus $\mathcal{T}'\subset\mathcal{T}$ and the topologies are equal.
:::
