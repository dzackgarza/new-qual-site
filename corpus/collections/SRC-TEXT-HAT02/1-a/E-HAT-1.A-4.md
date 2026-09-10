---
schema: qual/card@1
id: E-HAT-1.A-4
kind: problem
title: Loop $Y$ in finite graph is element of a basis for $\pi_1$
classification:
  areas:
  - topology
  topics:
  - Graphs
  - Fundamental Group
  - Free Groups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 1.A, Exercise 4; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Extended the cycle with one edge deleted to a maximal tree so the omitted edge gives the prescribed basis loop.
---

If $X$ is a finite graph and $Y$ is a subgraph homeomorphic to $S^1$ and containing the basepoint $x_0$, show that $\pi_1(X, x_0)$ has a basis in which one element is represented by the loop $Y$.


::: {.solution}
Let $Y\subseteq X$ be the given subgraph homeomorphic to $S^1$ and containing the basepoint $x_0$.
Choose an edge
\[
e\subseteq Y.
\]

<1>1. The subgraph
\[
Y\setminus \mathring e
\]
is a tree.
::: {.proof}
Removing the interior of one edge from a circle leaves a closed interval subdivided into finitely many edges.
Thus it is connected and contains no cycle.
:::

<1>2. Extend
\[
Y\setminus \mathring e
\]
to a maximal tree
\[
T\subseteq X.
\]
::: {.proof}
Since $X$ is finite, repeatedly adjoin edges that connect the current tree to a new vertex or otherwise enlarge it without creating a cycle.
The process terminates at a maximal tree containing the original subgraph.
:::

<1>3. The edge $e$ does not lie in $T$.
::: {.proof}
If $e$ also belonged to $T$, then $T$ would contain all of $Y$.
But $Y$ is a cycle, contradicting that $T$ is a tree.
:::

<1>4. The standard free basis of $\pi_1(X,x_0)$ associated to the maximal tree $T$ contains the loop $Y$.
::: {.proof}
For every edge $f$ of $X\setminus T$, the associated basis loop starts at $x_0$, follows the unique path in $T$ to one endpoint of $f$, traverses $f$, then returns to $x_0$ along the unique tree path from the other endpoint.

Take $f=e$.
Because
\[
Y\setminus\mathring e\subseteq T,
\]
the unique path in $T$ between the endpoints of $e$ is exactly the complementary arc of $Y$.
Hence the basis loop associated to $e$ traverses precisely the circle $Y$, up to orientation.
Thus one basis element is represented by $Y$.
:::
:::
