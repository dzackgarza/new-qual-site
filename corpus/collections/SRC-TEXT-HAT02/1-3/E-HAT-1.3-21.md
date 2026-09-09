---
schema: qual/card@1
id: E-HAT-1.3-21
kind: problem
title: "Torus with Möbius band attached"
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
  note: Checked against Hatcher, Algebraic Topology, Section 1.3, Exercise 21; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Computed both amalgam presentations; described the torus case as a Bass-Serre tree of planes and strips and the RP2 case as a four-sheeted annulus-plus-two-spheres universal cover with its deck action.
---

Let $X$ be the space obtained from a torus $S^1 \times S^1$ by attaching a Möbius band via a homeomorphism from the boundary circle of the Möbius band to the circle $S^1 \times \{x_0\}$ in the torus.
Compute $\pi_1(X)$, describe the universal cover of $X$, and describe the action of $\pi_1(X)$ on the universal cover.
Do the same for the space $Y$ obtained by attaching a Möbius band to $\mathbb{RP}^2$ via a homeomorphism from its boundary circle to the circle in $\mathbb{RP}^2$ formed by the 1-skeleton of the usual CW structure on $\mathbb{RP}^2$.

::: {.solution}
Let $M$ denote the Möbius band and let $c$ generate
\[
\pi_1(M)\cong\mathbb Z.
\]
The boundary circle of $M$ represents
\[
c^2\in\pi_1(M).
\]

<1>1. For the torus space $X$,
\[
\pi_1(X)
\cong
\left\langle a,b,c\ \middle|\ [a,b]=1,\ a=c^2\right\rangle
\cong
\left\langle b,c\ \middle|\ [b,c^2]=1\right\rangle.
\]
::: {.proof}
Let $a,b$ be the standard generators of
\[
\pi_1(S^1\times S^1)=\langle a,b\mid[a,b]=1\rangle,
\]
with $a$ represented by the attaching circle $S^1\times\{x_0\}$.
Van Kampen for the union of the torus and Möbius band identifies the boundary generator $c^2$ with $a$.
Eliminating $a$ gives the second presentation.
:::

<1>2. Equivalently,
\[
\pi_1(X)
\cong
A*_{D}C,
\]
where
\[
A=\langle a,b\mid[a,b]=1\rangle\cong\mathbb Z^2,
\quad
C=\langle c\rangle\cong\mathbb Z,
\quad
D=\langle a\rangle=\langle c^2\rangle\cong\mathbb Z.
\]
::: {.proof}
This is exactly the van Kampen pushout from <1>1, and both maps from the edge group $D$ are injective in this case.
:::

<1>3. Construct a simply connected space $\widetilde X$ as follows.
Its incidence graph is the Bass--Serre tree $T$ for the amalgam $A*_D C$.
For each $A$-vertex take a copy of $\mathbb R^2$, for each $C$-vertex take a copy of the universal cover of the Möbius band, an infinite strip $\mathbb R\times I$, and glue each incident strip boundary line to the corresponding lift of the $a$-circle in the adjacent plane.
::: {.proof}
The vertices of $T$ are the cosets
\[
G/A\quad\text{and}\quad G/C,
\qquad G=\pi_1(X),
\]
and its edges are the cosets $G/D$, with $gD$ joining $gA$ to $gC$.
Since $G=A*_D C$, the normal-form theorem for amalgamated products says that this incidence graph is a tree.

The plane is the universal cover of the torus.
The infinite strip is the universal cover of the Möbius band.
Each lift of the attaching circle is a line, so the edge-space gluings are homeomorphisms between boundary lines and these lifted lines.
:::

<1>4. The natural piecewise map
\[
\widetilde X\to X
\]
is the universal covering map.
::: {.proof}
On every plane and strip it is the standard universal covering map of the corresponding piece.
Near a point of an attaching line, a small neighborhood is obtained by gluing a half-neighborhood in the strip to a neighborhood of the corresponding line in the plane exactly as in $X$, so the map is locally a homeomorphism there as well.
Thus it is a covering map.

Every vertex space is simply connected and adjacent vertex spaces meet in a line, which is contractible.
The incidence graph $T$ is a tree.
Van Kampen over finite subtrees gives trivial fundamental group for every finite union, and every loop has compact image and meets only finitely many pieces.
Hence
\[
\pi_1(\widetilde X)=1.
\]
:::

<1>5. The action of $G=\pi_1(X)$ on $\widetilde X$ is the left-translation action on the tree of spaces.
::: {.proof}
For $g,h\in G$, the deck transformation corresponding to $g$ sends
\[
P_{hA}\longrightarrow P_{ghA},
\qquad
S_{hC}\longrightarrow S_{ghC},
\qquad
L_{hD}\longrightarrow L_{ghD},
\]
using the compatible deck translations inside the plane and strip pieces.
This action is free, preserves all gluings, and the quotient identifies all $A$-pieces to the torus and all $C$-pieces to the Möbius band, recovering $X$.
:::

<1>6. For the second space $Y$,
\[
\pi_1(Y)
\cong
\langle a,c\mid a^2=1,\ a=c^2\rangle
\cong
\langle c\mid c^4=1\rangle
\cong\mathbb Z/4.
\]
::: {.proof}
The usual CW structure on $\mathbb{RP}^2$ has one $1$-cell $a$ and one $2$-cell attached by $a^2$.
The attaching circle for the Möbius band is this $1$-skeleton circle, while the boundary of the Möbius band represents $c^2$.
Van Kampen therefore gives
\[
a=c^2,
\qquad a^2=1,
\]
which is equivalent to $c^4=1$.
:::

<1>7. The universal cover $\widetilde Y$ is a four-sheeted cover built from one annulus and two spheres.
::: {.proof}
Restrict the universal cover to the Möbius-band subspace.
The subgroup of
\[
\pi_1(M)=\langle c\rangle\cong\mathbb Z
\]
that maps trivially to
\[
\pi_1(Y)=\mathbb Z/4
\]
is $4\mathbb Z$.
The corresponding four-sheeted connected cover of the Möbius band is an annulus $A$.
Its two boundary circles each map two-to-one onto the boundary of the Möbius band.

The image of
\[
\pi_1(\mathbb{RP}^2)=\langle a\mid a^2=1\rangle
\]
inside $\mathbb Z/4$ is the order-two subgroup
\[
\langle c^2\rangle.
\]
Thus the inverse image of the projective-plane piece has two connected components, each the universal double cover
\[
S^2\to\mathbb{RP}^2.
\]
In each sphere the inverse image of the $1$-skeleton circle is an equator mapping two-to-one onto that circle.

Glue the two boundary circles of the annulus respectively to these two equators.
The resulting space is the full four-sheeted cover $\widetilde Y$.
:::

<1>8. The space $\widetilde Y$ is simply connected, hence is the universal cover.
::: {.proof}
The annulus has fundamental group generated by either boundary circle.
After gluing the first sphere along its equator, that boundary loop becomes nullhomotopic because it bounds a hemisphere in the sphere.
Thus van Kampen kills the annulus fundamental group.
Attaching the second sphere cannot create fundamental group.
Hence
\[
\pi_1(\widetilde Y)=1.
\]
:::

<1>9. The deck group of $\widetilde Y\to Y$ is cyclic of order four.
Its generator acts on the annulus by the deck transformation induced by one unit of translation in the universal strip of the Möbius band; this interchanges the two boundary circles and therefore interchanges the two sphere components.
Its square preserves each sphere and acts there by the antipodal deck transformation of $S^2\to\mathbb{RP}^2$.
::: {.proof}
The universal-cover deck group is canonically
\[
\pi_1(Y)\cong\mathbb Z/4.
\]
The stated action is exactly the restriction of the generator $c$ to the lifted Möbius and projective-plane pieces.
After four iterations it is the identity, while no smaller positive power fixes every point.
:::

<1>10. This gives the requested fundamental groups, universal covers, and fundamental-group actions for both $X$ and $Y$.
::: {.proof}
The torus case is <1>1--<1>5 and the projective-plane case is <1>6--<1>9.
:::
:::
