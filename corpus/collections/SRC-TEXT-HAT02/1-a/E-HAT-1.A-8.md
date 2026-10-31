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
    says why the count for F bounds the count for G. This replacement proof is a
    repair awaiting machine certification; no artifact covers it yet.
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
There are only finitely many based connected $n$-sheeted covers of the rose $\Gamma$ up to isomorphism over $\Gamma$.

::: pf-proof
Let $\Gamma$ be the rose with $r$ circles $a_1,\ldots,a_r$ and basepoint $v_0$, and let $p\colon\widetilde\Gamma\to\Gamma$ be a connected $n$-sheeted cover with a chosen point $\widetilde x_0$ over $v_0$.
The fibre $F_0=p^{-1}(v_0)$ has $n$ elements; label them by $\{1,\ldots,n\}$ so that $\widetilde x_0$ receives the label $1$.
Lifting the loop $a_i$ from a point of the fibre ends at a point of the fibre, and lifting it from different points gives a bijection $\sigma_i\colon F_0\to F_0$, because the lift of the reversed loop is the inverse map; so $\sigma_i\in S_n$.

Conversely, let $(\sigma_1,\ldots,\sigma_r)\in S_n^r$.
Form the graph with vertex set $\{1,\ldots,n\}$ and, for each $i$ and each $j$, one edge $e_{i,j}$ from $j$ to $\sigma_i(j)$ labelled $a_i$, and map it to $\Gamma$ by sending every vertex to $v_0$ and carrying $e_{i,j}$ around $a_i$.
At every vertex there is exactly one outgoing and one incoming edge of each label, so this map is a covering.
It is connected exactly when the $\sigma_i$ generate a transitive subgroup, and it is based because the vertex $1$ sits over $v_0$.

These two constructions are inverse: lifting recovers the $\sigma_i$ from the cover, and the cover built from a tuple has that tuple as its monodromy, with two tuples giving isomorphic based covers only if they are equal.
There are $\abs{S_n}^r=(n!)^r$ tuples, so there are only finitely many based connected $n$-sheeted covers of $\Gamma$.
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
The correspondence theorem for $F\to F/N=G$ bijects the subgroups of $G$ with the subgroups $H$ of $F$ containing $N$, sending $H$ to $H/N$.
Fix such an $H$ and consider the map
$$
\varphi\colon F/H\longrightarrow G/(H/N),\qquad \varphi(gH)=(gN)(H/N).
$$
It is well defined: if $gH=g'H$ then $g'^{-1}g\in H$, hence $(g'N)^{-1}(gN)=g'^{-1}gN\in H/N$ and the two cosets of $H/N$ agree.
It is injective, with the same implication read backwards, and it is surjective because every coset of $H/N$ in $G$ is $(gN)(H/N)$ for some $g\in F$.
So $\varphi$ is a bijection between the cosets of $H$ in $F$ and the cosets of $H/N$ in $G$, which gives $[G:H/N]=[F:H]$ without any normality assumption on $H$.
Hence $H/N$ has index $n$ in $G$ exactly when $H$ has index $n$ in $F$.
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
