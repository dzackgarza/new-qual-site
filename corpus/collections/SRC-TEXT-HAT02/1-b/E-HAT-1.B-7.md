---
schema: qual/card@1
id: E-HAT-1.B-7
kind: problem
title: "Bipartite realization of graph products"
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
  note: Checked against Hatcher, Algebraic Topology, Section 1.B, Exercise 7; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Subdivided each original edge by a midpoint carrying the edge group, replacing it by two edges whose midpoint-side homomorphisms are identities.
---

::: {.problem}
Show that every graph product of groups can be realized by a graph whose vertices are partitioned into two subsets, with every oriented edge going from a vertex in the first subset to a vertex in the second subset.
:::

::: {.solution}
Let $\Gamma$ be an arbitrary graph of groups.
For each unoriented edge $e$ with edge group $G_e$ and endpoint homomorphisms
\[
\alpha_e:G_e\to G_{o(e)},
\qquad
\omega_e:G_e\to G_{t(e)},
\]
subdivide $e$ once by inserting a new midpoint vertex $m_e$.

::: pf

::: {.pf-step #s1}

Give the new vertex $m_e$ the group
\[
G_{m_e}=G_e.
\]
Replace the original edge by two new edges, each also carrying the group $G_e$.

::: pf-proof

For the half-edge from $m_e$ to $o(e)$, use the identity map
\[
G_e\to G_{m_e}=G_e
\]
at the midpoint and the original map $\alpha_e$ at the old endpoint.
For the half-edge from $m_e$ to $t(e)$, use the identity at the midpoint and $\omega_e$ at the old endpoint.
Thus the new graph-of-groups data are well defined.

:::

:::

::: {.pf-step #s2}

The new underlying graph is bipartite.

::: pf-proof

Let
\[
V_0=\{m_e:e\in E(\Gamma)\}
\]
be the set of new midpoint vertices and let
\[
V_1=V(\Gamma)
\]
be the set of original vertices.
Every new edge joins a midpoint vertex to an original vertex.
Orient every edge from $V_0$ to $V_1$.
Then every oriented edge goes from the first part to the second part.

:::

:::

::: {.pf-step #s3}

The graph product of the subdivided graph of groups is canonically isomorphic to the original graph product.

::: pf-proof

In the graph-of-spaces model, the mapping-cylinder piece associated to an original edge is simply subdivided across its middle level.
The inserted vertex space is the same $K(G_e,1)$ that already occurs as the cross-section of the edge cylinder, and the new identity attachment introduces no new homotopical relation.
Thus the total space $K\Gamma$ is unchanged up to the evident homeomorphism obtained by subdividing each edge cylinder.
Consequently its fundamental group is unchanged.

:::

:::

::: pf-step

Hence every graph product can be realized by a graph whose vertices split into two classes and whose oriented edges all run from the first class to the second.

::: pf-proof

The construction in steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref} has exactly these properties.

:::

:::

:::

:::
