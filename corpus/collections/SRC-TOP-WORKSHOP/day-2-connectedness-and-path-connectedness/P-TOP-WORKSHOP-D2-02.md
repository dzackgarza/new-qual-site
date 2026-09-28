---
schema: qual/card@1
id: P-TOP-WORKSHOP-D2-02
kind: problem
title: Removing a product of proper subsets from a product of connected spaces
classification:
  areas:
  - topology
  topics:
  - Connectedness
  - Product Topology
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Show that if $A$ is a proper subset of a connected space $X$ and $B$ is a proper subset of a connected space $Y$, then $(X\times Y)\setminus(A\times B)$ is connected.
:::

::: {.solution}
Since $A$ and $B$ are proper, choose $x_0\in X\setminus A$ and $y_0\in Y\setminus B$. We use that a union of connected subspaces each of which meets a fixed connected subspace $S$, together with $S$, is connected.

<1>1. $(X \times Y) \setminus (A \times B) = \bigl((X \setminus A) \times Y\bigr) \cup \bigl(X \times (Y \setminus B)\bigr)$.
::: {.proof}
$(x, y) \notin A \times B$ if and only if $x \notin A$ or $y \notin B$.
:::

<1>2. $S = (\{x_0\} \times Y) \cup (X \times \{y_0\})$ is a connected subset of $(X \times Y) \setminus (A \times B)$.
::: {.proof}
The slices $\{x_0\} \times Y \cong Y$ and $X \times \{y_0\} \cong X$ are connected and share the point $(x_0, y_0)$, so their union is connected. It lies in the complement by step <1>1, since $x_0\notin A$ and $y_0\notin B$.
:::

<1>3. Each slice $\{x\} \times Y$ with $x \in X \setminus A$ and each slice $X \times \{y\}$ with $y \in Y \setminus B$ is a connected subset of the complement meeting $S$.
::: {.proof}
These slices are homeomorphic to $Y$ and $X$, hence connected, and lie in the complement by step <1>1. The slice $\{x\} \times Y$ contains $(x, y_0) \in S$, and $X \times \{y\}$ contains $(x_0, y) \in S$.
:::

<1>4. Q.E.D.
::: {.proof}
By step <1>1, the complement is the union of the slices in step <1>3, and it contains $S$. Each slice is connected and meets the connected set $S$ of step <1>2, so the union of $S$ and all the slices, which is the complement, is connected.
:::
:::
