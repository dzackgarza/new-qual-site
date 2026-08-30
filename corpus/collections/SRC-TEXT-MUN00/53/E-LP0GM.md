---
schema: qual/card@1
id: E-LP0GM
kind: exercise
title: Uniqueness of the slicing over connected evenly covered sets
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: {.exercise}

Let $p: E \to B$ be continuous and surjective.
Suppose that $U$ is an open set of $B$ that is evenly covered by $p$.
Show that if $U$ is connected, then the partition of $p^{-1}(U)$ into slices is unique.
:::

::: solution
**Goal:** Show that connectedness of $U$ forces the slices over $U$ to be exactly the connected components of $p^{-1}(U)$.

<1> By assumption, there is a family of slices $\{V_\alpha\}_{\alpha\in A}$ such that
    $$
    p^{-1}(U)=\bigsqcup_{\alpha\in A}V_\alpha,\qquad p|_{V_\alpha}:V_\alpha\to U\ \text{homeomorphism}.
    $$

<1> Each $V_\alpha$ is connected because $U$ is connected and $p|_{V_\alpha}$ is a homeomorphism.
    Each $V_\alpha$ is also open and closed in $p^{-1}(U)$, since it is one piece of a disjoint open union.

<1> Let $C$ be a connected component of $p^{-1}(U)$ and choose $x\in C$.
    $x$ lies in a unique slice $V_\beta$.
    Because $C$ is connected and $V_\beta$ is clopen, $C\subseteq V_\beta$.
    Since $V_\beta$ itself is connected and contains $C$, we get $C=V_\beta$.

<1> Therefore the components of $p^{-1}(U)$ and the slices are the same partition.
    The connected-component partition is unique, hence the slicing partition is unique.

Authored by **Codex 5.3 Spark Extra High**.
:::
