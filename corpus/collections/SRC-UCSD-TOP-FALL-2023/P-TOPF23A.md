---
schema: qual/card@1
id: P-TOPF23A
kind: problem
title: "Homotopy-equivalent closed manifolds have the same dimension and orientability"
classification:
  areas:
  - topology
  topics:
  - Homotopy Type
  - Manifolds
  - Orientation
relations: []
review: draft
---

::: {.problem}
Suppose that $M$ is a closed connected $m$-manifold, that $N$ is a closed connected $n$-manifold, and that $M$ and $N$ are homotopy-equivalent.
Show that $m = n$ and that $M$ is orientable if and only if $N$ is orientable.
What happens if $M$ and $N$ are merely compact manifolds-with-boundary — that is, they are not necessarily closed?
:::

::: {.solution}
<1>1. Closed homotopy-equivalent manifolds have the same dimension.
::: {.proof}
For every closed connected $d$-manifold $P$, mod-$2$ Poincaré duality gives
$$H_d(P;\mathbb F_2)\cong\mathbb F_2,$$
while $H_i(P;\mathbb F_2)=0$ for $i>d$. Homotopy equivalence preserves homology, so the largest degree with nonzero mod-$2$ homology is both $m$ and $n$. Hence $m=n$.
:::

<1>2. For a closed connected $d$-manifold $P$,
$$P\text{ is orientable}\iff H_d(P;\mathbb Z)\cong\mathbb Z,$$
while in the nonorientable case $H_d(P;\mathbb Z)=0$.
::: {.proof}
This is the integral top-homology criterion for orientability of closed connected manifolds.
:::

<1>3. Therefore $M$ is orientable if and only if $N$ is orientable.
::: {.proof}
The homotopy equivalence induces an isomorphism on integral homology, and <1>1 identifies their common dimension.
:::

<1>4. Both conclusions fail for compact manifolds with boundary.
::: {.proof}
Dimension is not homotopy-invariant: $D^m$ and $D^n$ are contractible for arbitrary $m,n$. Orientability is not homotopy-invariant either: an annulus and a Möbius band are both homotopy equivalent to $S^1$, but the annulus is orientable and the Möbius band is not.
:::
:::
