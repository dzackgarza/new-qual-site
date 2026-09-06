---
schema: qual/card@1
id: P-TOPOLOGY-PHD-F08-05
kind: problem
title: Closed subsets of compact spaces and compact subsets of Hausdorff spaces
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Hausdorff Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-06
  note: Checked against Part One, question 5 of the Topology Ph.D. Qualifying Exam dated January 17, 2009 in assets/attachments/F08phdtop.pdf.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-06
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    For a closed subspace, adjoined its open complement to an arbitrary open
    cover and used compactness of the ambient space. For a compact subset of a
    Hausdorff space, separated an exterior point from each point of the compact
    set and extracted a finite subcover.
---

::: {.problem}
Prove that a closed subset of a compact topological space is compact.
Prove that in a Hausdorff topological space a compact subset is closed.
:::

::: {.solution}
<1>1. A closed subset of a compact topological space is compact.
::: {.proof}
Let $X$ be compact and let $F\subseteq X$ be closed.
Suppose
\[
F\subseteq\bigcup_{i\in I}U_i,
\]
where every $U_i$ is open in the subspace $F$.
For each $i$, choose an open set $V_i\subseteq X$ such that
\[
U_i=F\cap V_i.
\]
Then
\[
\{V_i:i\in I\}\cup\{X\setminus F\}
\]
is an open cover of $X$.
By compactness of $X$, finitely many members cover $X$.
Discarding $X\setminus F$ if it occurs, the corresponding finitely many $V_i$ still cover $F$.
Intersecting with $F$, the corresponding finitely many $U_i$ cover $F$.
Thus every open cover of $F$ has a finite subcover, so $F$ is compact.
:::

<1>2. Let $X$ be Hausdorff, let $K\subseteq X$ be compact, and let
\[
x\in X\setminus K.
\]
For each $y\in K$, choose disjoint open sets $U_y,V_y\subseteq X$ with
\[
y\in U_y,
\qquad
x\in V_y.
\]
::: {.proof}
For every $y\in K$, we have $x\ne y$.
Since $X$ is Hausdorff, the two distinct points $x$ and $y$ have disjoint open neighborhoods.
Name the neighborhood of $y$ by $U_y$ and the neighborhood of $x$ by $V_y$.
:::

<1>3. The point $x$ has an open neighborhood disjoint from $K$.
::: {.proof}
The family
\[
\{U_y:y\in K\}
\]
is an open cover of $K$.
Compactness gives points
\[
y_1,\ldots,y_n\in K
\]
such that
\[
K\subseteq U_{y_1}\cup\cdots\cup U_{y_n}.
\]
Set
\[
V=V_{y_1}\cap\cdots\cap V_{y_n}.
\]
Then $V$ is an open neighborhood of $x$.
If $z\in V\cap K$, then some $i$ satisfies $z\in U_{y_i}$, while $z\in V$ implies $z\in V_{y_i}$.
This contradicts
\[
U_{y_i}\cap V_{y_i}=\varnothing.
\]
Hence
\[
V\cap K=\varnothing.
\]
:::

<1>4. Every compact subset of a Hausdorff space is closed.
::: {.proof}
By <1>3, every point of $X\setminus K$ has an open neighborhood contained in $X\setminus K$.
Therefore $X\setminus K$ is open, and hence $K$ is closed.
:::
:::
