---
schema: qual/card@1
id: P-TOPS02J
kind: problem
title: "Restriction of a covering map to a connected component is a covering map"
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: 'Source put no hypothesis on X, and the identity of X_1 ⊔ X_2 restricted to X_1 is not surjective; the statement now assumes X connected and locally path-connected.'
---

::: {.problem}
Let $X$ be connected and locally path-connected, let $p : E \to X$ be a covering space and let $C \subset E$ be a connected component of $E$.
Prove $p\restrict_C : C \to X$ is also a covering space.
:::

::: {.solution}
Call an open set $U \subseteq X$ evenly covered if $p^{-1}(U)$ is a disjoint union of open sets each mapped homeomorphically onto $U$ by $p$.

::: pf

::: {.pf-step #good-nbhd}

Every $x \in X$ has a path-connected evenly covered open neighborhood $U$, and every sheet over such a $U$ is path-connected.

::: pf-proof

Take an evenly covered neighborhood $W$ of $x$ and, by local path-connectedness, a path-connected open $U$ with $x \in U \subseteq W$. Then $U$ is evenly covered by the intersections of the sheets over $W$ with $p^{-1}(U)$, and each such sheet is homeomorphic to $U$, hence path-connected.

:::

:::

::: {.pf-step #sheets-in-c}

If $U$ is as in step [](#good-nbhd){.pf-ref}, then $C \cap p^{-1}(U)$ is the union of the sheets over $U$ that meet $C$.

::: pf-proof

A sheet is connected, so a sheet meeting the component $C$ lies in $C$.

:::

:::

::: {.pf-step #onto}

$p(C) = X$.

::: pf-proof

$X$ is connected and locally path-connected, hence path-connected. Fix $c_0 \in C$. For $x \in X$, choose a path $\gamma$ from $p(c_0)$ to $x$. Its lift starting at $c_0$ is a connected set containing $c_0$, so it lies in $C$, and it ends at a point of $C$ over $x$.

:::

:::

::: pf-qed

$C$ is open in $E$: for $c \in C$, the sheet over a neighborhood $U$ of $p(c)$ as in step [](#good-nbhd){.pf-ref} that contains $c$ lies in $C$ by step [](#sheets-in-c){.pf-ref}. By step [](#sheets-in-c){.pf-ref}, $(p\restrict_C)^{-1}(U)$ is a disjoint union of open subsets of $C$ each mapped homeomorphically onto $U$, for every such $U$, and by step [](#onto){.pf-ref} this union is nonempty. These $U$ cover $X$, so $p\restrict_C$ is a covering map.

:::

:::

:::
