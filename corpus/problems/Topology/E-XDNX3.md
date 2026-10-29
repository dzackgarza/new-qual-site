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

We show that $X\setminus A$ is open. Fix $x \in X \setminus A$.

::: pf

::: {.pf-step #finite-subcover}

There are $a_1,\ldots,a_k\in A$ and open sets $U_{a_i}\ni x$, $V_{a_i}\ni a_i$ with $U_{a_i}\cap V_{a_i}=\varnothing$ and $A \subseteq V_{a_1} \cup \cdots \cup V_{a_k}$.

::: pf-proof

Since $X$ is Hausdorff and $x\neq a$ for each $a \in A$, there are disjoint open sets $U_a \ni x$ and $V_a \ni a$. The sets $\{V_a\}_{a \in A}$ cover $A$, and compactness of $A$ gives a finite subcover.

:::

:::

::: {.pf-step #nbhd}

$U \coloneqq U_{a_1} \cap \cdots \cap U_{a_k}$ is an open neighborhood of $x$ disjoint from $A$.

::: pf-proof

$U$ is a finite intersection of open sets containing $x$. For each $i$, $U\subseteq U_{a_i}$ is disjoint from $V_{a_i}$, so $U$ is disjoint from $V_{a_1}\cup\cdots\cup V_{a_k}\supseteq A$ by step [](#finite-subcover){.pf-ref}.

:::

:::

::: pf-step

$A$ is closed.

::: pf-proof

By step [](#nbhd){.pf-ref}, every point of $X\setminus A$ is an interior point of $X\setminus A$, so $X\setminus A$ is open.

:::

:::

:::

:::
