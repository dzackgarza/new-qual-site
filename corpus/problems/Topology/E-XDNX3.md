---
schema: qual/card@1
id: E-XDNX3
kind: problem
title: Compact subspaces of Hausdorff spaces are closed
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Hausdorff Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.exercise}
Let $A$ be a compact subspace of a Hausdorff space $X$.
Show that $A$ is closed.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

It suffices to show $X \setminus A$ is open.

::: pf-proof

a set is closed iff its complement is open.

:::

:::

::: pf-step

Let $x \in X \setminus A$.

::: pf-proof

take an arbitrary point outside $A$.

:::

:::

::: pf-step

For each $a \in A$, there are disjoint open sets $U_a \ni x$ and $V_a \ni a$.

::: pf-proof

$X$ is Hausdorff and $x \neq a$.

:::

:::

::: pf-step

$\{V_a\}_{a \in A}$ is an open cover of $A$.

::: pf-proof

each $a \in A$ lies in $V_a$.

:::

:::

::: {.pf-step #s5}

Since $A$ is compact, there is a finite subcover $A \subseteq V_{a_1} \cup \cdots \cup V_{a_k}$.

::: pf-proof

compactness.

:::

:::

::: pf-step

Let $U = U_{a_1} \cap \cdots \cap U_{a_k}$.

::: pf-proof

define a neighborhood of $x$.

:::

:::

::: {.pf-step #s7}

$U$ is open, contains $x$, and is disjoint from $A$.

::: pf-proof

$U$ is a finite intersection of open sets containing $x$; and $U \cap V_{a_i} = \varnothing$ for each $i$ (since $U \subseteq U_{a_i}$ and $U_{a_i} \cap V_{a_i} = \varnothing$), so $U \cap A = \varnothing$ by step [](#s5){.pf-ref}.

:::

:::

::: {.pf-step #s8}

Hence $x$ is an interior point of $X \setminus A$, so $X \setminus A$ is open.

::: pf-proof

Step [](#s7){.pf-ref} holds for every $x \in X \setminus A$.

:::

:::

::: {.pf-step #s9}

Therefore $A$ is closed.

::: pf-proof

Steps [](#s1){.pf-ref} and [](#s8){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s9){.pf-ref}.

:::

:::

:::
