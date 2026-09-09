---
schema: qual/card@1
id: E-HAT-1.A-10
kind: problem
title: Finite connected subgraph of covering space extends to finite covering space
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Graphs
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 1.A, Exercise 10; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Viewed each circle label as a partial permutation of the finite vertex set and completed each partial bijection to a permutation.
---

Let $X$ be the wedge sum of $n$ circles, with its natural graph structure, and let $\widetilde{X} \to X$ be a covering space with $Y \subset \widetilde{X}$ a finite connected subgraph.
Show there is a finite graph $Z \supset Y$ having the same vertices as $Y$, such that the projection $Y \to X$ extends to a covering space $Z \to X$.


::: {.solution}
Write the rose as
\[
X=S^1_1\vee\cdots\vee S^1_n
\]
and orient and label the $i$th circle by $a_i$.
The covering graph $\widetilde X$ inherits these oriented labels.
Let $V$ be the finite vertex set of $Y$.

<1>1. For each label $a_i$, the $a_i$-edges already present in $Y$ define a partial bijection
\[
\sigma_i:D_i\longrightarrow R_i
\]
between subsets $D_i,R_i\subseteq V$.
::: {.proof}
At each vertex of a covering of the rose there is exactly one outgoing and exactly one incoming edge labeled $a_i$.
Thus among the $a_i$-edges lying in $Y$, no two have the same initial vertex and no two have the same terminal vertex.
Sending the initial vertex of each such edge to its terminal vertex therefore gives an injective map $D_i\to V$ with image $R_i$, hence a bijection $D_i\to R_i$.
:::

<1>2. The complements $V\setminus D_i$ and $V\setminus R_i$ have the same finite cardinality.
::: {.proof}
Since $\sigma_i:D_i\to R_i$ is a bijection,
\[
|D_i|=|R_i|.
\]
Subtracting from the finite number $|V|$ gives
\[
|V\setminus D_i|=|V\setminus R_i|.
\]
:::

<1>3. Extend each partial bijection $\sigma_i$ to a permutation
\[
\bar\sigma_i:V\longrightarrow V.
\]
::: {.proof}
Choose any bijection
\[
V\setminus D_i\longrightarrow V\setminus R_i
\]
and combine it with $\sigma_i$.
Because the two domains are disjoint and the two images are disjoint, the result is a permutation of $V$ extending $\sigma_i$.
:::

<1>4. Form a graph $Z$ with vertex set $V$ by retaining every edge of $Y$ and, for every $v\in V\setminus D_i$, adding one oriented $a_i$-edge from $v$ to $ar\sigma_i(v)$.
Then $Y\subseteq Z$ and $Z$ has exactly the same vertices as $Y$.
::: {.proof}
For $v\in D_i$, the edge prescribed by $ar\sigma_i$ is precisely the existing edge of $Y$, since $ar\sigma_i$ extends $\sigma_i$.
For the missing initial vertices we add exactly the missing edges.
No new vertices are introduced.
:::

<1>5. The evident label-preserving map
\[
Z\longrightarrow X
\]
is a finite-sheeted covering map.
::: {.proof}
For each vertex $v\in V$ and each $i$, there is exactly one outgoing $a_i$-edge, namely the edge from $v$ to $ar\sigma_i(v)$.
Since $ar\sigma_i$ is a permutation, there is also exactly one incoming $a_i$-edge at $v$.
This is precisely the local covering condition at the unique vertex of the rose.
On edge interiors the map is a homeomorphism to the corresponding open edge of $X$.
Hence $Z\to X$ is a covering.
Its number of sheets is $|V|<\infty$.
:::

<1>6. Therefore the projection $Y\to X$ extends to the required finite covering
\[
\boxed{Z\to X}
\]
with $V(Z)=V(Y)$.
::: {.proof}
The construction in <1>4 agrees with the original projection on all vertices and edges of $Y$, and <1>5 proves the covering property.
:::
:::
