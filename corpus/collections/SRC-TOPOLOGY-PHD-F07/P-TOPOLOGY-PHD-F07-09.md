---
schema: qual/card@1
id: P-TOPOLOGY-PHD-F07-09
kind: problem
title: Closed subspaces of locally compact Hausdorff spaces
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Hausdorff Spaces
  - Subspace Topology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-06
  note: Checked against Part One, question 9 of the Topology Ph.D. Qualifying Exam in assets/attachments/F07phdtop.pdf.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-06
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    For a point a of the closed subspace A, intersected a compact neighborhood
    K in X with A. The intersection is compact because it is closed in K, and
    it is a neighborhood in A because K contains an ambient open neighborhood
    of a. Also recorded that Hausdorffness passes to subspaces.
---

::: {.problem}
A Hausdorff topological space is known to be locally compact if every point has a compact neighborhood.
Prove that every closed subspace of a locally compact Hausdorff space is locally compact.
:::

::: {.solution}
Let $X$ be locally compact Hausdorff, and let $A\subseteq X$ be closed.

<1>1. The subspace $A$ is Hausdorff.
::: {.proof}
Take distinct points $a,b\in A$.
Since $X$ is Hausdorff, there are disjoint open sets $U,V\subseteq X$ with
\[
a\in U,
\qquad
b\in V.
\]
Then $U\cap A$ and $V\cap A$ are disjoint open neighborhoods of $a$ and $b$ in the subspace topology on $A$.
Thus $A$ is Hausdorff.
:::

<1>2. Fix $a\in A$.
There is a compact neighborhood $K$ of $a$ in $X$ and an open set $U\subseteq X$ such that
\[
a\in U\subseteq K.
\]
::: {.proof}
Since $X$ is locally compact, $a$ has a compact neighborhood $K$.
By the definition of neighborhood, $K$ contains an open set $U$ containing $a$.
:::

<1>3. The set $K\cap A$ is compact.
::: {.proof}
Because $A$ is closed in $X$, the intersection
\[
K\cap A
\]
is closed in the subspace $K$.
A closed subspace of a compact space is compact, and $K$ is compact by <1>2. Therefore $K\cap A$ is compact.
:::

<1>4. The set $K\cap A$ is a neighborhood of $a$ in the subspace $A$.
::: {.proof}
By <1>2,
\[
a\in U\subseteq K.
\]
Hence
\[
a\in U\cap A\subseteq K\cap A.
\]
The set $U\cap A$ is open in $A$ by the definition of the subspace topology.
Thus $K\cap A$ contains an open neighborhood of $a$ in $A$, so it is a neighborhood of $a$ in $A$.
:::

<1>5. Therefore $A$ is locally compact.
::: {.proof}
The point $a\in A$ was arbitrary.
By <1>3--<1>4, every point of $A$ has a compact neighborhood in $A$.
Together with the Hausdorff property from <1>1, this is precisely local compactness in the sense stated in the problem.
:::
:::
