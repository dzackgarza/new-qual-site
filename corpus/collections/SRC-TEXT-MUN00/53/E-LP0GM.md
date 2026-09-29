---
schema: qual/card@1
id: E-LP0GM
kind: problem
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

::: {.solution}

::: pf

::: pf-step

Slices over an evenly covered set:
    *Proof:*

::: pf-proof

::: pf-step

By the definition of an evenly covered open set, there exists a partition of $p^{-1}(U)$ into a collection of pairwise disjoint open sets $\{V_\alpha\}_{\alpha \in A}$ in $E$:
    $$p^{-1}(U) = \bigsqcup_{\alpha \in A} V_\alpha,$$
    such that for each $\alpha \in A$, the restriction $p|_{V_\alpha}: V_\alpha \to U$ is a homeomorphism.

:::

::: pf-step

The open sets $V_\alpha$ are called the *slices* of $p^{-1}(U)$.

:::

:::

:::

::: pf-step

Connectedness and clopen property of slices:
    *Proof:*

::: pf-proof

::: pf-step

Because $U$ is connected and $p|_{V_\alpha}: V_\alpha \to U$ is a homeomorphism, the topological property of connectedness is preserved: each slice $V_\alpha$ is a connected subspace of $E$.

:::

::: pf-step

Since $p^{-1}(U) \setminus V_\alpha = \bigcup_{\beta \neq \alpha} V_\beta$ is a union of open sets, it is open in $p^{-1}(U)$.

:::

::: pf-step

Therefore each slice $V_\alpha$ is both open and closed (clopen) in the subspace $p^{-1}(U)$.

:::

:::

:::

::: pf-step

Characterization of slices as connected components:
    *Proof:*

::: pf-proof

::: pf-step

Let $C$ be any connected component of the subspace $p^{-1}(U)$.

:::

::: pf-step

Pick a point $x \in C$. Since the slices partition $p^{-1}(U)$, there exists a unique $\alpha \in A$ such that $x \in V_\alpha$.

:::

::: pf-step

Since $V_\alpha$ is clopen in $p^{-1}(U)$, the intersection $V_\alpha \cap C$ is clopen in the subspace $C$.

:::

::: pf-step

Since $x \in V_\alpha \cap C$, $V_\alpha \cap C \neq \emptyset$. By connectedness of $C$, the only non-empty clopen subset of $C$ is $C$ itself, so $C \subseteq V_\alpha$.

:::

::: pf-step

Conversely, $V_\alpha$ is a connected subset of $p^{-1}(U)$ containing $x$. Since $C$ is the maximal connected subset containing $x$, $V_\alpha \subseteq C$.

:::

::: pf-step

Thus $C = V_\alpha$.

:::

:::

:::

:::

    *Proof:*
    By step [](#s3){.pf-ref}, the slices $\{V_\alpha\}_{\alpha \in A}$ of $p^{-1}(U)$ are precisely the connected components of the topological subspace $p^{-1}(U)$. Because the partition of any topological space into its connected components is uniquely determined, the partition of $p^{-1}(U)$ into slices is unique.
:::
