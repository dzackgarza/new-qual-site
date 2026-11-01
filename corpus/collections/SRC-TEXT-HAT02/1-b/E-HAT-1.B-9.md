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
- event: source-corrected
  by: claude-opus-5.5
  date: 2026-10-31
  note: The book writes K Gamma for the graph of spaces; the stored statement had K.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Examined the preamble and the step claims: a common multiple $N$ of the group orders, the $N$-sheeted covers of the vertex spaces, and the finite-index free subgroup they assemble.
- event: solution-reviewed
  by: claude
  date: 2026-11-01
  note: >-
    Read line by line. The construction is correct and the counting is the crux, which the card
    gets right: with `N` a common multiple of the orders, take `N/|G_v|` copies of `EG_v` over each
    vertex space and `N/|G_e|` copies of `EG_e\times I` over each edge cylinder, so both pieces
    have total degree `N`; and over one incidence the `N/|G_v|` copies of `EG_v` contribute
    `(N/|G_v|)[G_v:G_e]=N/|G_e|` boundary copies of `EG_e`, exactly matching the cylinders, the same
    at the other endpoint. Then every component upstairs has contractible vertex and edge spaces,
    so it is homotopy equivalent to a graph and has free fundamental group, and a connected
    component gives a connected cover of some finite degree `d\le N`, i.e. a free subgroup of index
    `d`. Handled correctly rather than glossed: the cover `\widehat K` need not be connected, which
    is why the card passes to a component and gets index `d\le N`. The converse is cited from
    Scott--Wall and is marked as a citation in the statement. No correction was needed.
---

::: {.problem}
If $\Gamma$ is a finite graph of finite groups with injective edge homomorphisms, show that the graph product of the groups has a free subgroup of finite index by constructing a suitable finite-sheeted covering space of $K\Gamma$ from universal covers of the mapping cylinders in $K\Gamma$.
[The converse is also true: A finitely generated group having a free subgroup of finite index is isomorphic to such a graph product. For a proof of this see [Scott & Wall 1979], Theorem 7.3.]
:::

::: {.solution}
Let $\Gamma$ be a finite connected graph of finite groups with injective edge homomorphisms.
Write $G_v$ for the vertex groups and $G_e$ for the edge groups.
Choose
$$
N
$$
to be a common multiple of the orders of all vertex and edge groups.

::: pf

::: {.pf-step #s1}

Over each vertex space $K(G_v,1)$ take
$$
\frac{N}{\cardinality{G_v}}
$$
disjoint copies of its universal cover
$$
E G_v\to K(G_v,1).
$$
The resulting map over the vertex space has total degree $N$.

::: pf-proof

Each universal cover has degree $\cardinality{G_v}$ because its deck group is the finite group $G_v$.
Hence
$$
\frac{N}{\cardinality{G_v}}\cdot \cardinality{G_v}=N.
$$

:::

:::

::: {.pf-step #s2}

Over each edge mapping cylinder take
$$
\frac{N}{\cardinality{G_e}}
$$
copies of the universal lifted edge cylinder
$$
E G_e\times I.
$$

::: pf-proof

The edge classifying space $K(G_e,1)$ has universal cover $E G_e$ of degree $\cardinality{G_e}$.
Thus the displayed number of copies again gives total degree $N$ over the interior of the edge cylinder.

:::

:::

::: {.pf-step #s3}

The boundary components of these lifted edge cylinders can be matched exactly with the inverse images of the edge subspaces in the chosen vertex covers.

::: pf-proof

Fix an incidence of an edge $e$ at a vertex $v$.
Since the edge homomorphism
$$
G_e\hookrightarrow G_v
$$
is injective, pulling the universal cover
$$
E G_v\to K(G_v,1)
$$
back along
$$
K(G_e,1)\to K(G_v,1)
$$
produces
$$
[G_v:G_e]
$$
disjoint copies of $E G_e$.
Across the $N/\cardinality{G_v}$ chosen copies of $E G_v$, the total number of such boundary copies is therefore
$$
\frac{N}{\cardinality{G_v}}[G_v:G_e]
=
\frac{N}{\cardinality{G_v}}\frac{\cardinality{G_v}}{\cardinality{G_e}}
=
\frac{N}{\cardinality{G_e}},
$$
exactly the number of lifted edge cylinders from step [](#s2){.pf-ref}.
Hence the boundary copies can be paired and glued.
The same count holds at the other endpoint of the edge.

:::

:::

::: pf-step

After performing these gluings for every edge, one obtains a finite-sheeted covering
$$
\widehat K\to K\Gamma
$$
of degree $N$.

::: pf-proof

By steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref} the local degree is $N$ on every vertex space, edge-cylinder interior, and attaching region.
The pieces are glued by lifts of the original attaching maps, so the resulting map is locally a homeomorphism and has exactly $N$ points in every fiber.
Thus it is an $N$-sheeted covering.

:::

:::

::: {.pf-step #s5}

Every connected component of $\widehat K$ has free fundamental group.

::: pf-proof

Upstairs, every vertex space $E G_v$ and every edge space $E G_e$ is contractible.
Collapsing each contractible vertex space to a point and each edge cylinder to an interval gives a homotopy equivalence from a component of $\widehat K$ to its underlying incidence graph.
The fundamental group of a graph is free.
Equivalently, the lifted graph of groups has trivial vertex and edge stabilizer groups, so Exercise 3 applies.

:::

:::

::: pf-step

Therefore the original graph product contains a free subgroup of finite index.

::: pf-proof

Choose any connected component
$$
\widehat K_0\subseteq\widehat K.
$$
Since $K\Gamma$ is connected, the restriction
$$
\widehat K_0\to K\Gamma
$$
is a connected finite-sheeted covering, of some finite degree $d\le N$.
The corresponding subgroup
$$
H=(p_*)\pi_1(\widehat K_0)
\le\pi_1(K\Gamma)
$$
has index $d$, and by step [](#s5){.pf-ref} the group $H$ is free.
Hence
$$
\boxed{\pi_1(K\Gamma)\text{ is virtually free}.}
$$

:::

:::

:::

:::
