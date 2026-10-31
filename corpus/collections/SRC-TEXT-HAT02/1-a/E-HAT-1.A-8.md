---
schema: qual/card@1
id: E-HAT-1.A-8
kind: problem
title: Finitely generated group has finitely many subgroups of given finite index
classification:
  areas:
  - topology
  topics:
  - Free Groups
  - Covering Spaces
  - Subgroups
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
- event: solution-reviewed
  by: claude-opus-5.5
  date: 2026-10-31
  note: Counted based covers with their maps to the rose, which is what subgroups correspond to, instead of bare graphs.
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 1.A, Exercise 8.
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 1.A, Exercise 8.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Rewrote the proof. Six of its steps carried one-line fragments as proofs
    ("a free group is the fundamental group of a finite graph", "each
    vertex/edge of Gamma has n preimages", "the correspondence theorem for the
    quotient"), and three closing steps plus the qed only named earlier steps.
    Every step now carries a complete-sentence argument, and the closing step
    says why the count for F bounds the count for G.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Rewrote the proof: six one-line fragments and four back-reference steps became complete-sentence arguments, and the finiteness of the number of based covers is now justified by the finite data of a labelled graph together with a map to $\Gamma$.
---

::: {.problem}
Show that a finitely generated group has only a finite number of subgroups of a given finite index.
[First do the case of free groups, using covering spaces of graphs. The general case then follows since every group is a quotient group of a free group.]
:::

::: {.solution}
Fix $n\ge1$. For a subgroup $H$ of a group, $[G:H]$ denotes its index.

::: pf

::: {.pf-step #free-graph}
A free group $F$ of finite rank $r$ is the fundamental group of a finite graph.

::: pf-proof
Let $\Gamma$ be the wedge of $r$ circles with its natural graph structure, a finite graph with one vertex and $r$ edges.
By Hatcher, *Algebraic Topology*, §1.2, Example 1.21, the fundamental group of a wedge of circles is free, with one generator per circle, so $\pi_1(\Gamma)\cong F$.
:::

:::

::: {.pf-step #index-covers}
Subgroups of $F$ of index $n$ correspond to connected $n$-sheeted covering spaces of $\Gamma$ with a chosen point over the basepoint, up to isomorphism over $\Gamma$ preserving that point.

::: pf-proof
The classification of covering spaces (Hatcher §1.3, Theorem 1.38) makes based connected covers of $\Gamma$ correspond bijectively to subgroups of $\pi_1(\Gamma)$, and the number of sheets of a connected cover equals the index of the subgroup.
A cover is $n$-sheeted exactly when that index is $n$.
:::

:::

::: {.pf-step #finite-data}
There are only finitely many based connected $n$-sheeted covers of $\Gamma$ up to isomorphism over $\Gamma$.

::: pf-proof
Such a cover $\widetilde\Gamma$ is a graph with $n\abs{V(\Gamma)}$ vertices and $n\abs{E(\Gamma)}$ edges, because each vertex and each edge of $\Gamma$ has exactly $n$ preimages.
A map of graphs from $\widetilde\Gamma$ to $\Gamma$ is determined by its values on the vertices and on the oriented edges, and each value is one of the finitely many vertices or oriented edges of $\Gamma$; the basepoint is one of the $n$ points over the basepoint of $\Gamma$.
A based cover is determined up to isomorphism over $\Gamma$ by this finite list of choices, so there are only finitely many of them.
:::

:::

::: {.pf-step #free-case}
A free group $F$ of finite rank has only finitely many subgroups of index $n$.

::: pf-proof
Fix a finite graph $\Gamma$ with $\pi_1(\Gamma)\cong F$, which exists by step [](#free-graph){.pf-ref}.
By step [](#index-covers){.pf-ref} the subgroups of index $n$ are in bijection with the based connected $n$-sheeted covers of $\Gamma$ up to isomorphism, and by step [](#finite-data){.pf-ref} there are finitely many of those.
:::

:::

::: {.pf-step #quotient}
If $G=F/N$ with $F$ free, then subgroups of $G$ of index $n$ correspond to subgroups $H$ of $F$ with $N\le H$ and $[F:H]=n$.

::: pf-proof
The correspondence theorem for the quotient map $F\to F/N$ bijects the subgroups of $G$ with the subgroups $H$ of $F$ containing $N$, sending $H$ to $H/N$.
For such an $H$ the third isomorphism theorem gives $[F/N:H/N]=[F:H]$, so $H/N$ has index $n$ in $G$ exactly when $H$ has index $n$ in $F$.
:::

:::

::: {.pf-step #conclusion}
A finitely generated group has only finitely many subgroups of index $n$.

::: pf-proof
Write $G=F/N$ with $F$ a free group of finite rank, which is possible because $G$ is finitely generated.
By step [](#quotient){.pf-ref} the subgroups of $G$ of index $n$ are the groups $H/N$ with $H$ a subgroup of $F$ of index $n$ containing $N$, and distinct such $H$ give distinct $H/N$.
By step [](#free-case){.pf-ref} there are only finitely many subgroups of $F$ of index $n$, so $G$ has only finitely many subgroups of index $n$ as well.
:::

:::

:::
:::
