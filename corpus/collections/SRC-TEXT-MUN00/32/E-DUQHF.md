---
schema: qual/card@1
id: E-DUQHF
kind: exercise
title: Closed subspaces of normal spaces are normal
classification:
  areas:
  - topology
  topics:
  - Normal Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.exercise}

Show that a closed subspace of a normal space is normal.
:::

::: {.solution}
**Goal.** Show a closed subspace of a normal space is normal.

<1>1. Let $X$ be normal and $Y \subseteq X$ closed.
Proof: setup.

<1>2. $Y$ is $T_1$.
Proof: a subspace of a $T_1$ space is $T_1$ (singletons are closed in $X$, hence in $Y$).

<1>3. $Y$ is normal.
<2>1. Let $A, B \subseteq Y$ be disjoint closed subsets of $Y$.
Proof: take arbitrary disjoint closed sets in $Y$.
<2>2. $A$ and $B$ are closed in $X$.
Proof: $A$ is closed in $Y$ and $Y$ is closed in $X$, so $A$ is closed in $X$; same for $B$.
<2>3. By normality of $X$, there are disjoint open $U, V \subseteq X$ with $A \subseteq U$ and $B \subseteq V$.
Proof: $A, B$ are disjoint closed sets in the normal space $X$.
<2>4. Then $U \cap Y$ and $V \cap Y$ are disjoint open sets in $Y$ separating $A$ and $B$.
Proof: restrict the open sets to $Y$.

<1>4. Q.E.D.
Proof: <1>3 shows $Y$ is normal.
:::
