---
schema: qual/card@1
id: E-IHJ56
kind: problem
title: A compact subset of a Hausdorff space is closed
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
  date: 2026-08-17
---

::: exercise
Show that if $X$ is Hausdorff and $A\subseteq X$ is compact then $A$ is closed.
:::

::: {.solution}
**Goal:** Show that if $X$ is Hausdorff and $A \subseteq X$ is compact, then $A$ is closed.

<1>1. Fix $x \in X \setminus A$; it suffices to find an open neighborhood of $x$ disjoint from $A$.
::: {.proof}
Then $X \setminus A$ is a union of open sets, hence open, so $A$ is closed.
:::

<1>2. For each $a \in A$, choose disjoint open sets $U_a \ni a$ and $V_a \ni x$.
::: {.proof}
$X$ is Hausdorff, and $a \neq x$ since $x \notin A$.
:::

<1>3. $\theset{U_a}_{a \in A}$ is an open cover of $A$, so it has a finite subcover $U_{a_1}, \ldots, U_{a_n}$.
::: {.proof}
$A$ is compact.
:::

<1>4. Define $V := V_{a_1} \cap \cdots \cap V_{a_n}$; then $V$ is open, contains $x$, and is disjoint from $A$.
<2>1. $V$ is open and $x \in V$.
::: {.proof}
Finite intersection of open sets, each containing $x$ (<1>2). <2>2. $V \cap A = \emptyset$.
:::
::: {.proof}
If $y \in V \cap A$, then $y \in U_{a_j}$ for some $j$ (<1>3), but $y \in V \subseteq V_{a_j}$ contradicts $U_{a_j} \cap V_{a_j} = \emptyset$ (<1>2).
:::

<1>5. Q.E.D.
::: {.proof}
<1>1 and <1>4 show every $x \notin A$ has a neighborhood avoiding $A$; hence $A$ is closed.
:::
:::
