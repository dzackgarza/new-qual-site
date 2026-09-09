---
schema: qual/card@1
id: E-HAT-1.B-9
kind: problem
title: "Graph products of finite groups have free subgroups of finite index"
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 1.B, Exercise 9; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Constructed an N-sheeted graph-of-spaces cover using repeated universal covers of vertex and edge classifying spaces; the edge-boundary multiplicities match by the subgroup-index formula, and each component upstairs has free fundamental group.
---

If $\Gamma$ is a finite graph of finite groups with injective edge homomorphisms, show that the graph product of the groups has a free subgroup of finite index by constructing a suitable finite-sheeted covering space of $K$ from universal covers of the mapping cylinders in $K$.
[The converse is also true: A finitely generated group having a free subgroup of finite index is isomorphic to such a graph product. For a proof of this see [Scott & Wall 1979], Theorem 7.3.]


::: {.solution}
Let $\Gamma$ be a finite connected graph of finite groups with injective edge homomorphisms.
Write $G_v$ for the vertex groups and $G_e$ for the edge groups.
Choose
\[
N
\]
to be a common multiple of the orders of all vertex and edge groups.

<1>1. Over each vertex space $K(G_v,1)$ take
\[
\frac{N}{|G_v|}
\]
disjoint copies of its universal cover
\[
E G_v\to K(G_v,1).
\]
The resulting map over the vertex space has total degree $N$.
::: {.proof}
Each universal cover has degree $|G_v|$ because its deck group is the finite group $G_v$.
Hence
\[
\frac{N}{|G_v|}\cdot |G_v|=N.
\]
:::

<1>2. Over each edge mapping cylinder take
\[
\frac{N}{|G_e|}
\]
copies of the universal lifted edge cylinder
\[
E G_e\times I.
\]
::: {.proof}
The edge classifying space $K(G_e,1)$ has universal cover $E G_e$ of degree $|G_e|$.
Thus the displayed number of copies again gives total degree $N$ over the interior of the edge cylinder.
:::

<1>3. The boundary components of these lifted edge cylinders can be matched exactly with the inverse images of the edge subspaces in the chosen vertex covers.
::: {.proof}
Fix an incidence of an edge $e$ at a vertex $v$.
Since the edge homomorphism
\[
G_e\hookrightarrow G_v
\]
is injective, pulling the universal cover
\[
E G_v\to K(G_v,1)
\]
back along
\[
K(G_e,1)\to K(G_v,1)
\]
produces
\[
[G_v:G_e]
\]
disjoint copies of $E G_e$.
Across the $N/|G_v|$ chosen copies of $E G_v$, the total number of such boundary copies is therefore
\[
\frac{N}{|G_v|}[G_v:G_e]
=
\frac{N}{|G_v|}\frac{|G_v|}{|G_e|}
=
\frac{N}{|G_e|},
\]
exactly the number of lifted edge cylinders from <1>2.
Hence the boundary copies can be paired and glued.
The same count holds at the other endpoint of the edge.
:::

<1>4. After performing these gluings for every edge, one obtains a finite-sheeted covering
\[
\widehat K\to K\Gamma
\]
of degree $N$.
::: {.proof}
By <1>1--<1>3 the local degree is $N$ on every vertex space, edge-cylinder interior, and attaching region.
The pieces are glued by lifts of the original attaching maps, so the resulting map is locally a homeomorphism and has exactly $N$ points in every fiber.
Thus it is an $N$-sheeted covering.
:::

<1>5. Every connected component of $\widehat K$ has free fundamental group.
::: {.proof}
Upstairs, every vertex space $E G_v$ and every edge space $E G_e$ is contractible.
Collapsing each contractible vertex space to a point and each edge cylinder to an interval gives a homotopy equivalence from a component of $\widehat K$ to its underlying incidence graph.
The fundamental group of a graph is free.
Equivalently, the lifted graph of groups has trivial vertex and edge stabilizer groups, so Exercise 3 applies.
:::

<1>6. Therefore the original graph product contains a free subgroup of finite index.
::: {.proof}
Choose any connected component
\[
\widehat K_0\subseteq\widehat K.
\]
Since $K\Gamma$ is connected, the restriction
\[
\widehat K_0\to K\Gamma
\]
is a connected finite-sheeted covering, of some finite degree $d\le N$.
The corresponding subgroup
\[
H=(p_*)\pi_1(\widehat K_0)
\le\pi_1(K\Gamma)
\]
has index $d$, and by <1>5 the group $H$ is free.
Hence
\[
\boxed{\pi_1(K\Gamma)\text{ is virtually free}.}
\]
:::
:::
