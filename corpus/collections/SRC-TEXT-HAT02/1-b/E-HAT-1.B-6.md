---
schema: qual/card@1
id: E-HAT-1.B-6
kind: problem
title: "Graph of groups with universal cover $T \\times \\RR$"
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
  note: Checked against Hatcher, Algebraic Topology, Section 1.B, Exercise 6; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Used the Bass--Serre tree of lines for the general product statement and identified the ray example with the direct limit union of 1/n! Z; replacing every map by times 2 gives the dyadic subgroup.
---

::: {.problem}
Show that for a graph of groups all of whose edge homomorphisms are injective maps $\ZZ \to \ZZ$, we can choose $K$ to have universal cover a product $T \times \RR$ with $T$ a tree.
Work out in detail the case that the graph of groups is the infinite sequence $\ZZ \xrightarrow{2} \ZZ \xrightarrow{3} \ZZ \xrightarrow{4} \ZZ \to \cdots$ where the map $\ZZ \xrightarrow{n} \ZZ$ is multiplication by $n$.
Show that $\pi_1(K\Gamma)$ is isomorphic to $\QQ$ in this case.
How would one modify this example to get $\pi_1(K\Gamma)$ isomorphic to the subgroup of $\QQ$ consisting of rational numbers with denominator a power of 2?
:::

::: {.solution}
Consider first an arbitrary graph of groups in which every vertex and edge group is infinite cyclic and every edge homomorphism is injective.
After choosing generators, every edge homomorphism has the form
$$
\ZZ\longrightarrow\ZZ,
\qquad
k\longmapsto m k
$$
for some nonzero integer $m$.

::: pf

::: pf-step

Its universal graph-of-spaces cover is a tree of copies of $\RR$ joined by strips $\RR\times I$.

::: pf-proof

The classifying space of each cyclic vertex or edge group can be chosen to be $S^1$.
Its universal cover is $\RR$.
Hence each lifted vertex space is a line and each lifted edge mapping cylinder is a strip.
The incidence graph of the lifted pieces is the Bass--Serre tree $T$.

:::

:::

::: {.pf-step #s2}

Every lifted boundary map of an edge strip is an affine homeomorphism of $\RR$.

::: pf-proof

A map $S^1\to S^1$ inducing multiplication by a nonzero integer $m$ on fundamental groups lifts to
$$
t\longmapsto mt+c
$$
on universal covers.
This is a homeomorphism of $\RR$.

:::

:::

::: pf-step

The universal cover is homeomorphic to
$$
\boxed{T\times\RR}.
$$

::: pf-proof

Choose a coordinate on one vertex line and propagate coordinates across adjacent edge strips.
By step [](#s2){.pf-ref}, each boundary attachment can be straightened to the identity by an affine reparametrization of the new vertex line.
Since the incidence graph $T$ is a tree, each new vertex is reached by a unique path from the initial vertex, so no conflicting coordinate choices arise.
The resulting tree of lines and strips is exactly the product cell structure on $T\times\RR$.

Now specialize to the ray
$$
G_1\xrightarrow{\times2}G_2\xrightarrow{\times3}G_3\xrightarrow{\times4}\cdots,
\qquad
G_k\cong\ZZ.
$$

:::

:::

::: pf-step

Since the underlying graph is a tree, the graph product is the direct limit
$$
\pi_1(K\Gamma)
\cong
\varinjlim
\bigl(
\ZZ\xrightarrow{2}\ZZ\xrightarrow{3}\ZZ\xrightarrow{4}\cdots
\bigr).
$$

::: pf-proof

There are no stable letters because a maximal tree is the whole underlying ray.
The fundamental group presentation therefore takes the free product of the vertex groups and imposes exactly the edge identifications.
This is the colimit of the displayed directed system.

:::

:::

::: pf-step

This direct limit is isomorphic to $\QQ$.

::: pf-proof

Embed the $k$th copy of $\ZZ$ into $\QQ$ by
$$
\phi_k(r)=\frac{r}{k!}.
$$
These maps are compatible because
$$
\phi_{k+1}((k+1)r)
=\frac{(k+1)r}{(k+1)!}
=\frac r{k!}
=\phi_k(r).
$$
Thus the direct limit identifies with
$$
\bigcup_{k\ge1}\frac1{k!}\ZZ.
$$
Every rational number $a/b$ lies in this union because $b$ divides $k!$ for all sufficiently large $k$.
Hence
$$
\varinjlim G_k\cong\QQ.
$$

:::

:::

::: pf-step

To obtain the subgroup of rationals whose denominator is a power of $2$, replace the sequence by
$$
\ZZ\xrightarrow{2}\ZZ\xrightarrow{2}\ZZ\xrightarrow{2}\cdots.
$$

::: pf-proof

The same direct-limit calculation embeds the $k$th copy as
$$
2^{-(k-1)}\ZZ.
$$
Therefore the limit is
$$
\bigcup_{k\ge0}2^{-k}\ZZ
=\ZZ[1/2]
=\left\{\frac a{2^k}:a\in\ZZ,\ k\ge0\right\}.
$$

:::

:::

:::

:::
