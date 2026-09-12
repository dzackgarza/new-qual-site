---
schema: qual/card@1
id: E-HAT-1.B-5
kind: problem
title: "Baumslag--Solitar group as a graph of groups"
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
  note: Checked against Hatcher, Algebraic Topology, Section 1.B, Exercise 5; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Computed the HNN presentation and described the universal cover as the Bass--Serre tree of vertex lines and edge strips, then straightened the line coordinates to obtain T times R.
---

Consider the graph of groups having one vertex, $\mathbb{Z}$, and one edge, the map $\mathbb{Z} \to \mathbb{Z}$ that is multiplication by 2, realized by the 2-sheeted covering space $S^1 \to S^1$.
Show that $\pi_1(K\Gamma)$ has presentation $\langle a, b \mid bab^{-1}a^{-2} \rangle$ and describe the universal cover of $K$ explicitly as a product $T \times \mathbb{R}$ with $T$ a tree.
[The group $\pi_1(K\Gamma)$ is the first in a family of groups called Baumslag–Solitar groups, having presentations of the form $\langle a, b \mid ba^mb^{-1}a^{-n} \rangle$. These are HNN extensions $\mathbb{Z} *_\mathbb{Z}$.]


::: {.solution}
Let the vertex group be
\[
A=\langle a\rangle\cong\mathbb Z
\]
and let the edge group be another copy
\[
C=\langle c\rangle\cong\mathbb Z.
\]
For the loop edge, take the two endpoint injections
\[
\iota_0(c)=a,
\qquad
\iota_1(c)=a^2.
\]

<1>1. The graph-of-groups fundamental group has presentation
\[
\pi_1(K\Gamma)
\cong
\langle a,b\mid bab^{-1}=a^2\rangle.
\]
::: {.proof}
Choose the unique vertex as base vertex and let $b$ be the stable letter corresponding to the loop edge.
The HNN-extension presentation identifies the two images of the edge group by
\[
b\iota_0(c)b^{-1}=\iota_1(c).
\]
Substituting the two endpoint maps gives
\[
bab^{-1}=a^2,
\]
which is equivalent to the relator
\[
bab^{-1}a^{-2}.
\]
:::

<1>2. The universal cover of the graph of spaces is a tree of spaces whose vertex spaces are copies of $\mathbb R$ and whose edge spaces are strips $\mathbb R\times I$.
::: {.proof}
The universal cover of the vertex circle $K(A,1)=S^1$ is $\mathbb R$.
The universal cover of the edge circle $K(C,1)=S^1$ is also $\mathbb R$, so the lifted mapping cylinder for an edge is a strip
\[
\mathbb R\times I.
\]
The incidence graph of these lifted vertex and edge spaces is the Bass--Serre tree $T$ of the HNN extension.
It is a tree because the full graph-of-spaces cover is simply connected and the usual normal-form theorem rules out cycles in the incidence graph.
:::

<1>3. The tree $T$ is trivalent.
::: {.proof}
At one end of an edge, the edge subgroup maps onto the full vertex group, so the index is
\[
[A:\iota_0(C)]=1.
\]
At the other end its image is $2\mathbb Z$, so
\[
[A:\iota_1(C)]=2.
\]
Thus at each vertex there is one incident edge of the first type and two of the second type, for total valence three.
:::

<1>4. Each boundary attachment of a lifted edge strip to a lifted vertex line is a homeomorphism $\mathbb R\to\mathbb R$.
::: {.proof}
The identity endpoint map lifts to an affine map
\[
t\longmapsto t+c.
\]
The degree-two map $S^1\to S^1$ lifts to an affine map
\[
t\longmapsto 2t+c.
\]
Both are homeomorphisms of the universal covering line.
:::

<1>5. The universal cover is homeomorphic to
\[
\boxed{T\times\mathbb R}.
\]
::: {.proof}
Choose an affine coordinate on one vertex line.
Since $T$ is a tree, proceed outward from this vertex.
Whenever an edge strip joins a vertex line whose coordinate has already been chosen to a new vertex line, choose the affine coordinate on the new line so that both boundary identifications of the strip become the identity in the $\mathbb R$ coordinate.
There is no compatibility obstruction because a tree has no cycles.

After making these choices, every vertex space is
\[
\{v\}\times\mathbb R
\]
and every edge strip is
\[
e\times\mathbb R,
\]
with the obvious product gluings.
Their union is exactly $T\times\mathbb R$.
Since $T$ and $\mathbb R$ are contractible, this space is simply connected and is therefore the universal cover.
:::

<1>6. Thus
\[
\boxed{\pi_1(K\Gamma)=\langle a,b\mid bab^{-1}a^{-2}\rangle}
\]
and its universal cover is the product of a trivalent tree with a line.
::: {.proof}
Combine <1>1 and <1>5.
:::
:::
