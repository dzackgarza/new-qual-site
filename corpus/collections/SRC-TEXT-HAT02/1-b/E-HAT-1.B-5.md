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
- event: source-corrected
  by: claude-opus-5.5
  date: 2026-10-31
  note: The book writes K Gamma for the graph of spaces; the stored statement had K.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Examined the preamble, the step claims and the construction of the tree of spaces; the presentation and the product structure were checked, the gluing details of the strips only at the level of the step claims.
- event: solution-reviewed
  by: claude
  date: 2026-11-01
  note: >-
    Read line by line. The presentation is right: with the loop edge `e`, the HNN relation
    `b\iota_0(c)b^{-1}=\iota_1(c)` becomes `bab^{-1}=a^2`, i.e. the relator `bab^{-1}a^{-2}`. The
    valence count is right, and the card now says where the two numbers come from: vertices of the
    Bass--Serre tree are the cosets `G/A` and edges the cosets `G/C`, so the number of edge-ends at
    a vertex is `[A:\iota_0(C)]+[A:\iota_1(C)]=1+2=3`. The straightening argument is the correct
    one — a degree-`m` self-map of `S^1` lifts to `t\mapsto mt+c`, a homeomorphism of the universal
    line, so each boundary attachment can be made the identity in the `\RR` coordinate, and the tree
    is what makes the choices consistent — giving `T\times\RR` with `T` trivalent. Cited and not
    proved here: the normal-form theorem that the incidence graph of the lifted pieces is a tree,
    which the card names. No correction was needed.
---

::: {.problem}
Consider the graph of groups having one vertex, $\ZZ$, and one edge, the map $\ZZ \to \ZZ$ that is multiplication by 2, realized by the 2-sheeted covering space $S^1 \to S^1$.
Show that $\pi_1(K\Gamma)$ has presentation $\langle a, b \mid bab^{-1}a^{-2} \rangle$ and describe the universal cover of $K\Gamma$ explicitly as a product $T \times \RR$ with $T$ a tree.
[The group $\pi_1(K\Gamma)$ is the first in a family of groups called Baumslag–Solitar groups, having presentations of the form $\langle a, b \mid ba^mb^{-1}a^{-n} \rangle$. These are HNN extensions $\ZZ *_\ZZ$.]
:::

::: {.solution}
Let the vertex group be
$$
A=\langle a\rangle\cong\ZZ
$$
and let the edge group be another copy
$$
C=\langle c\rangle\cong\ZZ.
$$
For the loop edge, take the two endpoint injections
$$
\iota_0(c)=a,
\qquad
\iota_1(c)=a^2.
$$

::: pf

::: {.pf-step #s1}

The graph-of-groups fundamental group has presentation
$$
\pi_1(K\Gamma)
\cong
\langle a,b\mid bab^{-1}=a^2\rangle.
$$

::: pf-proof

Choose the unique vertex as base vertex, let $b$ be the stable letter of the loop edge, and take
$$
\varphi=\iota_0=1,
\qquad
\psi=\iota_1\ \text{multiplication by }2.
$$
This is the one-vertex one-loop-edge graph of groups of Example 1B.13 (p. 93), whose $K_\Gamma$ is obtained from $K(A,1)$ by attaching $K(C,1)\times I$ along $K(C,1)\times\partial I$ by maps realizing $\varphi$ and $\psi$; with $K(C,1)$ having a single $0$-cell this is the one-vertex one-edge complex of Example 1B.13.
The relation of that extension is stated there, at p. 93, as
$$
t\,\varphi(c)\,t^{-1}=\psi(c),
$$
and its proof is deferred to Exercise 4 of §1.B (p. 96), which is [[E-HAT-1.B-4|Exercise 1.B.4]].
With $\varphi(c)=a$, $\psi(c)=a^2$ and the stable letter named $b$ it reads
$$
bab^{-1}=a^2,
$$
which is equivalent to the relator
$$
bab^{-1}a^{-2}.
$$

:::

:::

::: pf-step

The universal cover of the graph of spaces is a tree of spaces whose vertex spaces are copies of $\RR$ and whose edge spaces are strips $\RR\times I$.

::: pf-proof

The universal cover of the vertex circle $K(A,1)=S^1$ is $\RR$.
Both edge homomorphisms are injective, so by Theorem 1B.11 (p. 92) $K_\Gamma$ is a $K(G,1)$ and the inclusion of the edge circle $K(C,1)=S^1$ induces an injection on $\pi_1$.
The lifted edge space is therefore the universal cover $\RR$ of that circle, and the lifted mapping cylinder for an edge is a strip
$$
\RR\times I.
$$
The incidence graph of these lifted vertex and edge spaces is the tree $T_\Gamma$ constructed on p. 95: it has one vertex for each lifted vertex space, two vertices being joined when the corresponding lines are joined by a lifted segment of an edge cylinder, and it is built there as a union
$$
T_1\subset T_2\subset\cdots
$$
of subtrees, each step attaching an asterisk at every outer vertex of the previous one. A union of an increasing chain of trees along single new vertices is a tree, and the action of $\pi_1(K_\Gamma)$ on it has orbit space the underlying graph $\Gamma$ (p. 95).

:::

:::

::: pf-step

The tree $T$ is trivalent.

::: pf-proof

At one end of an edge, the edge subgroup maps onto the full vertex group, so the index is
$$
[A:\iota_0(C)]=1.
$$
At the other end its image is $2\ZZ$, so
$$
[A:\iota_1(C)]=2.
$$
Thus at each vertex there is one incident edge of the first type and two of the second type, for total valence three.

:::

:::

::: pf-step

Each boundary attachment of a lifted edge strip to a lifted vertex line is a homeomorphism $\RR\to\RR$.

::: pf-proof

The identity endpoint map lifts to an affine map
$$
t\longmapsto t+c.
$$
The degree-two map $S^1\to S^1$ lifts to an affine map
$$
t\longmapsto 2t+c.
$$
Both are homeomorphisms of the universal covering line.

:::

:::

::: {.pf-step #s5}

The universal cover is homeomorphic to
$$
\boxed{T\times\RR}.
$$

::: pf-proof

Choose an affine coordinate on one vertex line.
Since $T$ is a tree, proceed outward from this vertex.
Whenever an edge strip joins a vertex line whose coordinate has already been chosen to a new vertex line, choose the affine coordinate on the new line so that both boundary identifications of the strip become the identity in the $\RR$ coordinate.
There is no compatibility obstruction because a tree has no cycles.

After making these choices, every vertex space is
$$
\{v\}\times\RR
$$
and every edge strip is
$$
e\times\RR,
$$
with the obvious product gluings.
Their union is exactly $T\times\RR$.
Since $T$ and $\RR$ are contractible, this space is simply connected and is therefore the universal cover.

:::

:::

::: pf-step

Thus
$$
\boxed{\pi_1(K\Gamma)=\langle a,b\mid bab^{-1}a^{-2}\rangle}
$$
and its universal cover is the product of a trivalent tree with a line.

::: pf-proof

Step [](#s1){.pf-ref} computes the graph-of-groups fundamental group from the single vertex and edge, giving the presentation $\langle a,b\mid bab^{-1}a^{-2}\rangle$, and step [](#s5){.pf-ref} identifies a simply connected space covering $K\Gamma$ with $T\times\RR$, where $T$ is the trivalent tree of the lifted vertex lines.

:::

:::

:::

:::
