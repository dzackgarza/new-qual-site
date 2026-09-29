---
schema: qual/card@1
id: P-CIAF4
kind: problem
title: Finite-index subgroups of finitely generated free groups are free; infinite-index
  normal subgroups are not finitely generated
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Groups
  - Fundamental Group
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Checked both parts against problem 5 of the official UGA Spring 2017 topology exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-05
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Verified the covering-graph proof, including the finite-core criterion and the use of normality to make a nontrivial reduced loop close at every vertex.
---

::: {.problem}
a.
Show that any finite index subgroup of a finitely generated free group is free. 
State clearly any facts you use about the fundamental groups of graphs.

b.  
Prove that if $N$ is a nontrivial normal subgroup of infinite index in a finitely generated free group $F$ , then $N$ is not finitely generated.
:::

::: {.solution}
Write
\[
F\cong F_r=\pi_1(R_r,*),
\qquad
R_r=\bigvee_{i=1}^r S^1.
\]
We use the following standard graph facts.

::: pf

::: {.pf-step #s1}

For a connected graph $G$, the group $\pi_1(G)$ is free; if $T\subset G$ is a maximal tree, the oriented edges of $G\setminus T$ give a free basis after choosing paths in $T$ to their endpoints.

::: pf-proof

Collapsing the maximal tree $T$ to a point is a homotopy equivalence from $G$ to a wedge of one circle for each edge of $G\setminus T$. The fundamental group of such a wedge is free on those circles.

:::

:::

::: {.pf-step #s2}

If $G$ is connected and locally finite, then $\pi_1(G)$ is finitely generated if and only if the core
\[
\operatorname{core}(G),
\]
the union of all cyclically reduced closed edge paths in $G$, is a finite graph.

::: pf-proof

Choose a maximal tree $T\subset G$. By step [](#s1){.pf-ref}, $\pi_1(G)$ has a free basis indexed by the edges of $G\setminus T$. Hence $\pi_1(G)$ is finitely generated exactly when $G\setminus T$ has finitely many edges.

Assume first that $G\setminus T$ is finite. For each edge $e\in G\setminus T$, adjoin to $e$ the unique finite path in $T$ joining its endpoints. The union $K$ of these finitely many finite circuits is a finite subgraph. Every cyclically reduced closed edge path must use an edge outside $T$, and every tree segment between successive such edges is the unique path in $T$ joining the corresponding endpoints. Therefore every cyclically reduced closed edge path lies in $K$, so $\operatorname{core}(G)$ is finite.

Conversely, every edge of $G\setminus T$ lies on the circuit formed by that edge together with the unique path in $T$ joining its endpoints. Hence
\[
G\setminus T\subseteq\operatorname{core}(G).
\]
If the core is finite, then $G\setminus T$ is finite, so step [](#s1){.pf-ref} again shows that $\pi_1(G)$ is finitely generated.

:::

:::

::: {.pf-step #s3}

Let $H\le F$. The subgroup $H$ is realized by a connected covering
\[
p:(Y,y_0)\longrightarrow(R_r,*),
\]
with
\[
p_*\pi_1(Y,y_0)=H,
\]
and the number of sheets is $[F:H]$.

::: pf-proof

The rose $R_r$ is connected, locally path-connected, and semilocally simply connected, so the classification of connected covering spaces applies. Under the usual correspondence, the fiber over $*$ is naturally identified with the coset set $F/H$, hence has cardinality $[F:H]$.

:::

:::

::: pf-step

Every finite-index subgroup $H\le F$ is free.

::: pf-proof

Let $Y\to R_r$ be the covering from step [](#s3){.pf-ref}. Since $[F:H]<\infty$, the cover has finitely many vertices over the unique vertex of $R_r$ and finitely many edges over its finitely many edges. Thus $Y$ is a finite connected graph. By step [](#s1){.pf-ref},
\[
H\cong\pi_1(Y,y_0)
\]
is free.

:::

:::

::: {.pf-step #s5}

Now let $N\triangleleft F$ be nontrivial. In the covering
\[
p:(Y,y_0)\longrightarrow(R_r,*)
\]
corresponding to $N$, every vertex of $Y$ lies in $\operatorname{core}(Y)$.

::: pf-proof

Choose a nontrivial element $w\in N$ and represent it by a nonempty cyclically reduced word in a free basis of $F$ after replacing $w$ by a conjugate if necessary. Because $N$ is normal, every conjugate
\[
g^{-1}wg
\]
also belongs to $N$.

Vertices of $Y$ correspond to cosets of $N$. Let $v$ be the vertex represented by the coset $Ng$. The lift at $v$ of the reduced loop in $R_r$ labeled by $w$ is closed exactly when
\[
Ngw=Ng,
\]
equivalently when
\[
gwg^{-1}\in N.
\]
This holds by normality. Since $w$ is a nonempty reduced word and a covering of graphs preserves the local edge labels, its lift is a nontrivial reduced closed edge path through $v$. Hence $v\in\operatorname{core}(Y)$.

:::

:::

::: pf-step

If $N$ also has infinite index, then $N$ is not finitely generated.

::: pf-proof

By step [](#s3){.pf-ref}, infinite index means that the fiber $p^{-1}(*)$ has infinitely many points, so $Y$ has infinitely many vertices. By step [](#s5){.pf-ref} every one of these vertices belongs to $\operatorname{core}(Y)$, and therefore the core is infinite.

The graph $Y$ is locally finite because it covers the finite rose $R_r$. By step [](#s2){.pf-ref}, an infinite core implies that
\[
\pi_1(Y,y_0)
\]
is not finitely generated. Since
\[
N\cong\pi_1(Y,y_0),
\]
the subgroup $N$ is not finitely generated.

:::

:::

:::

:::
