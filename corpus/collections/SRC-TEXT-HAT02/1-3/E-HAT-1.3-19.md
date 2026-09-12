---
schema: qual/card@1
id: E-HAT-1.3-19
kind: problem
title: "Abelian covering spaces of closed orientable surfaces"
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
  note: Checked against Hatcher, Algebraic Topology, Section 1.3, Exercise 19; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Used epimorphisms from the surface-group abelianization to Z^n, and for n=3 realized the pullback cover as a Z^3-periodic embedded surface in R^3 coming from a genus-three handlebody spine in T^3.
---

Use the preceding problem to show that a closed orientable surface $M_g$ of genus $g$ has a connected normal covering space with deck transformation group isomorphic to $\mathbb{Z}^n$ (the product of $n$ copies of $\mathbb{Z}$) if $n \leq 2g$.
For $n = 3$ and $g \geq 3$, describe such a covering space explicitly as a subspace of $\mathbb{R}^3$ with translations of $\mathbb{R}^3$ as deck transformations.
Show that such a covering space in $\mathbb{R}^3$ exists if there is an embedding of $M_g$ in the 3-torus $T^3 = S^1 \times S^1 \times S^1$ such that the induced map $\pi_1(M_g) \to \pi_1(T^3)$ is surjective.

::: {.solution}
<1>1. The abelianization of the genus-$g$ surface group is
\[
H_1(M_g;\mathbb Z)
\cong
\pi_1(M_g)_{\mathrm{ab}}
\cong
\mathbb Z^{2g}.
\]
::: {.proof}
Using the standard presentation
\[
\pi_1(M_g)
=
\left\langle
a_1,b_1,\dots,a_g,b_g
\ \middle|\
[a_1,b_1]\cdots[a_g,b_g]=1
\right\rangle,
\]
abelianization kills every commutator, so the single defining relation becomes trivial.
The $2g$ generators therefore freely generate the abelianization.
:::

<1>2. For every $n\le2g$ there is a surjective homomorphism
\[
\phi:\pi_1(M_g)\twoheadrightarrow\mathbb Z^n.
\]
::: {.proof}
Compose the abelianization map
\[
\pi_1(M_g)\twoheadrightarrow\mathbb Z^{2g}
\]
with projection onto any $n$ coordinate factors.
:::

<1>3. Let
\[
H=\ker\phi.
\]
The connected covering corresponding to $H$ is normal and has deck group
\[
\mathbb Z^n.
\]
::: {.proof}
The kernel $H$ is normal.
For the associated connected normal cover
\[
p:\widetilde M_g\to M_g,
\]
the deck group is
\[
\pi_1(M_g)/H
\cong
\operatorname{im}\phi
\cong\mathbb Z^n.
\]
This proves the first assertion for every $n\le2g$.
:::

<1>4. Suppose now that
\[
i:M_g\hookrightarrow T^3
\]
is an embedding such that
\[
i_*:\pi_1(M_g)\twoheadrightarrow\pi_1(T^3)\cong\mathbb Z^3
\]
is surjective.
Then the inverse image
\[
\widetilde M_g:=\pi^{-1}(i(M_g))\subset\mathbb R^3,
\]
where
\[
\pi:\mathbb R^3\to T^3=\mathbb R^3/\mathbb Z^3,
\]
is connected.
::: {.proof}
The restriction
\[
\pi|_{\widetilde M_g}:\widetilde M_g\to M_g
\]
is the pullback of the universal cover of $T^3$.
The components of this pullback correspond to cosets of the subgroup
\[
i_*\pi_1(M_g)
\]
in
\[
\pi_1(T^3)=\mathbb Z^3.
\]
Since $i_*$ is surjective, there is one coset, hence one component.
:::

<1>5. The restriction
\[
\widetilde M_g\to M_g
\]
is a connected normal covering with deck group $\mathbb Z^3$, acting by integer translations of $\mathbb R^3$.
::: {.proof}
The universal cover
\[
\mathbb R^3\to T^3
\]
has deck group $\mathbb Z^3$, acting by
\[
x\longmapsto x+v,
\qquad v\in\mathbb Z^3.
\]
Since $\widetilde M_g$ is the full inverse image of $M_g$, it is invariant under every integer translation.
By <1>4 it is connected, so these translations are precisely the deck transformations of the restricted cover.
Equivalently, the corresponding subgroup is
\[
\ker i_*.
\]
:::

<1>6. For $g=3$, such an embedding $M_3\hookrightarrow T^3$ is obtained as the boundary of a regular neighborhood of the wedge of the three coordinate circles in $T^3$.
::: {.proof}
Let
\[
\Gamma
=
(S^1\times\{1\}\times\{1\})
\cup
(\{1\}\times S^1\times\{1\})
\cup
(\{1\}\times\{1\}\times S^1).
\]
This is a wedge of three circles.
A sufficiently small regular neighborhood $N(\Gamma)$ is a genus-three handlebody, so
\[
\partial N(\Gamma)\cong M_3.
\]

The inclusion
\[
\partial N(\Gamma)\hookrightarrow N(\Gamma)
\]
induces a surjection on fundamental groups: the three standard handlebody generators can be represented by loops on the boundary.
The deformation retraction
\[
N(\Gamma)\simeq\Gamma
\]
followed by inclusion into $T^3$ sends these three generators to the three coordinate generators of
\[
\pi_1(T^3)=\mathbb Z^3.
\]
Hence the composite
\[
\pi_1(M_3)\to\pi_1(T^3)
\]
is surjective.
:::

<1>7. The resulting cover in $\mathbb R^3$ is the boundary of a regular neighborhood of the standard cubic lattice graph.
::: {.proof}
The full inverse image of $\Gamma$ under
\[
\mathbb R^3\to T^3
\]
is the graph with vertex set $\mathbb Z^3$ and edges joining nearest-neighbor lattice points in the three coordinate directions.
Pulling back the regular neighborhood $N(\Gamma)$ gives a $\mathbb Z^3$-periodic regular neighborhood of this cubic lattice graph.
Therefore
\[
\widetilde M_3
=
\partial\widetilde{N(\Gamma)}
\subset\mathbb R^3
\]
is an explicit connected periodic surface, and integer translations are its deck transformations.
:::

<1>8. For every $g>3$, add $g-3$ handles to $M_3$ inside a small ball in $T^3$ disjoint from the three loops that realize the coordinate generators.
The resulting embedded surface is $M_g$ and still induces a surjection on $\pi_1$.
::: {.proof}
Attaching a local surface handle in a ball increases the genus by one.
Because the modification is disjoint from the three loops on the original surface whose images generate $\pi_1(T^3)$, those loops persist on the new surface and still map to the three coordinate generators.
Thus surjectivity is preserved.

In the lifted picture in $\mathbb R^3$, the same operation adds $g-3$ handles in every fundamental cube, periodically under the $\mathbb Z^3$ translation action.
:::

<1>9. Hence for $n=3$ and every $g\ge3$ there is an explicit connected normal cover
\[
\widetilde M_g\subset\mathbb R^3
\]
with deck group $\mathbb Z^3$ acting by translations.
::: {.proof}
Combine <1>4--<1>8.
:::
:::
