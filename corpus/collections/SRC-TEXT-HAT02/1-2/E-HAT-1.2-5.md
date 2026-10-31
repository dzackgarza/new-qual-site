---
schema: qual/card@1
id: E-HAT-1.2-5
kind: problem
title: Fundamental group of planar graph is free on boundary loops of complementary regions
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Free Groups
  - Planar Graphs
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: solution-reviewed
  by: claude-opus-5.5
  date: 2026-10-31
  note: The old solution concluded that independent loops equal in number to the rank form a basis, which is false in a free group; rewritten as an induction that deletes an outer edge and uses a Nielsen substitution.
---

::: {.problem}
Let $X \subset \RR^2$ be a connected graph that is the union of a finite number of straight line segments.
Show that $\pi_1(X)$ is free with a basis consisting of loops formed by the boundaries of the bounded complementary regions of $X$, joined to a basepoint by suitably chosen paths in $X$.
[Assume the Jordan curve theorem for polygonal simple closed curves, which is equivalent to the case that $X$ is homeomorphic to $S^1$.]
:::

::: {.solution}
Subdivide the segments at their intersection points, so that $X$ is a finite connected graph whose edges are straight segments meeting only at endpoints.
For a bounded complementary region $U$, its boundary loop is the closed edge path that walks once around $U$, keeping $U$ on its left.
We induct on the number $n$ of bounded complementary regions.

::: pf

::: {.pf-step #s1}

If an edge $e$ has two different complementary regions on its two sides, then $X\setminus\operatorname{int}e$ is connected.

::: pf-proof

Suppose instead that $X\setminus\operatorname{int}e=X_1\sqcup X_2$ with $X_1,X_2$ disjoint closed subgraphs, and $e$ joins $x_1\in X_1$ to $x_2\in X_2$.
Let $e'\subset e$ be the closed subsegment from $x_2$ to a point at distance $\delta$ from $x_1$, with $\delta$ small.
For $\varepsilon$ small compared with $\delta$, the $\varepsilon$-neighbourhood $N$ of the compact set $X_2\cup e'$ misses $X_1$.
The boundary component of $N$ that runs along one side of $e'$ turns around its free end and returns along the other side.
It is a path in $\RR^2-X$ joining points on the two sides of $e$, so these points lie in one region.

:::

:::

::: {.pf-step #s2}

If $n=0$, then $X$ is a tree and $\pi_1(X)=1$.

::: pf-proof

A simple cycle in $X$ would by the Jordan curve theorem bound a bounded component of $\RR^2-C$, which contains a bounded complementary region of $X$.
So $X$ has no cycle, and a finite tree is contractible.

:::

:::

::: {.pf-step #s3}

If $n\ge1$, there is an edge $e$ with the unbounded region $W$ on one side and a bounded region $U$ on the other.

::: pf-proof

At least one edge borders $W$, and since $n\ge1$ at least one edge borders a bounded region.
Suppose no edge has $W$ on one side and a bounded region on the other.
Then the edges split into a set $A$ of edges with $W$ on both sides and a nonempty set $B$ of edges with bounded regions on both sides.
Since $X$ is connected, some vertex $v$ meets an edge of $A$ and an edge of $B$.
Going around $v$, the edges at $v$ occur in a cyclic order, and the sector between two consecutive edges lies in one region; so some consecutive pair $f\in A$, $f'\in B$ shares a sector that is both in $W$ and in a bounded region, a contradiction.

:::

:::

::: {.pf-step #s4}

Let $X'=X\setminus\operatorname{int}e$.
Then $X'$ is connected, its bounded complementary regions are those of $X$ other than $U$, and their boundary loops are unchanged.

::: pf-proof

By step [](#s1){.pf-ref}, $X'$ is connected.
Deleting the interior of $e$ joins $U$ and $W$ through $e$ into one unbounded region and changes no other region, because $e$ borders only $U$ and $W$.

:::

:::

::: {.pf-step #s5}

If $X'$ is a connected subgraph of $X$ with $X=X'\cup e$ for one edge $e$, and $c$ is a loop in $X$ that crosses $e$ exactly once, then a free basis of $\pi_1(X')$ together with $c$ is a free basis of $\pi_1(X)$.

::: pf-proof

Choose a maximal tree $T$ of $X'$; it is also a maximal tree of $X$.
Collapsing $T$ is a homotopy equivalence from $X$ to a wedge of circles, one for each edge not in $T$, and $\pi_1(X)$ is free on these edges, with $\pi_1(X')$ the free factor on the edges other than $e$.
The loop $c$ maps to a word that contains $e^{\pm1}$ exactly once, so $c=u\,e^{\pm1}v$ with $u,v\in\pi_1(X')$.
The substitution replacing $e$ by $c$ is an automorphism of the free group, so the claim holds.

:::

:::

::: pf-qed

Induct on $n$, with base case step [](#s2){.pf-ref}.
For $n\ge1$, take $e$, $U$ and $X'$ as in steps [](#s3){.pf-ref} and [](#s4){.pf-ref}.
By induction $\pi_1(X')$ is free on the boundary loops of the bounded regions other than $U$, joined to a basepoint.
The boundary loop of $U$ crosses $e$ exactly once, because $W$ lies on the other side of $e$.
By step [](#s5){.pf-ref}, adding it gives a free basis of $\pi_1(X)$ consisting of the boundary loops of all $n$ bounded regions.

:::

:::

:::
