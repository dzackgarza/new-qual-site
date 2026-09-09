---
schema: qual/card@1
id: E-HAT-1.A-14
kind: problem
title: Existence of maximal trees is equivalent to the Axiom of Choice
classification:
  areas:
  - topology
  topics:
  - Graphs
  - Axiom of Choice
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 1.A, Exercise 14; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Used Zorn for Choice implies maximal trees, and encoded an arbitrary family of nonempty sets as parallel edges from a common root to recover a choice function from a spanning tree.
---

Show that the existence of maximal trees is equivalent to the Axiom of Choice.


::: {.solution}
We prove the equivalence between the assertion

> every connected graph has a maximal tree

and the Axiom of Choice.

<1>1. Assume the Axiom of Choice. Then every connected graph $X$ has a maximal tree.
::: {.proof}
By the Axiom of Choice, Zorn's lemma holds.
Fix a vertex $v_0$ of $X$ and consider the partially ordered set of tree subgraphs of $X$ containing $v_0$, ordered by inclusion.
It is nonempty since $\{v_0\}$ is a tree.

If
\[
T_1\subseteq T_2\subseteq\cdots
\]
is more generally any chain of such trees, its union
\[
T=\bigcup_\alpha T_\alpha
\]
is connected: two vertices of $T$ lie in two members of the chain, one of which contains the other, so both lie in a single connected tree.
It is acyclic: a cycle uses only finitely many edges, hence all its edges lie in one member of the chain, contradicting that member being a tree.
Thus every chain has an upper bound.
By Zorn's lemma there is a maximal tree subgraph $T$ containing $v_0$.

Since $X$ is connected, this maximal tree contains every vertex of $X$.
Indeed, if a vertex lay outside $T$, choose a finite edge path from $v_0$ to it and take the first edge of this path leaving $T$.
Adjoining that edge and its new endpoint preserves connectedness and creates no cycle, contradicting maximality.
:::

<1>2. Conversely, assume every connected graph has a maximal tree.
Let
\[
\{A_i\}_{i\in I}
\]
be an arbitrary family of nonempty sets.
Construct a graph $X$ with vertices
\[
\{v_0\}\cup\{v_i:i\in I\}
\]
and, for each $i\in I$ and each $a\in A_i$, one edge
\[
e_{i,a}
\]
joining $v_0$ to $v_i$.
Then $X$ is connected.
::: {.proof}
For each fixed $i$, the hypothesis $A_i\ne\varnothing$ says that there exists at least one edge from $v_0$ to $v_i$.
Hence every vertex is joined to $v_0$ by a one-edge path.
This proves connectedness without making a simultaneous choice from all the $A_i$.
:::

<1>3. Let $T$ be a maximal tree in $X$.
For each $i\in I$, $T$ contains exactly one edge joining $v_0$ to $v_i$.
::: {.proof}
A maximal tree in a connected graph is spanning by the same elementary argument used at the end of <1>1, which does not use Choice once the maximal tree is given.
Thus $v_i\in T$ for every $i$.
Since every edge incident to $v_i$ joins it to $v_0$, connectedness of $T$ forces at least one edge $e_{i,a}$ to belong to $T$.

It cannot contain two distinct such edges $e_{i,a}$ and $e_{i,b}$ with $a\ne b$, since the union of these two parallel edges is a cycle homeomorphic to $S^1$.
Hence exactly one is present.
:::

<1>4. Define
\[
f:I\longrightarrow\bigcup_{i\in I}A_i
\]
by letting $f(i)$ be the unique element $a\in A_i$ for which $e_{i,a}\subseteq T$.
Then $f(i)\in A_i$ for every $i$.
::: {.proof}
Existence and uniqueness of this $a$ are <1>3.
Thus $f$ is a choice function for the arbitrary family $\{A_i\}_{i\in I}$.
:::

<1>5. Therefore the maximal-tree principle implies the Axiom of Choice, and hence the two statements are equivalent.
::: {.proof}
<1>1 proves Choice implies maximal trees, while <1>2--<1>4 construct a choice function from the maximal-tree principle for an arbitrary family of nonempty sets.
:::
:::
