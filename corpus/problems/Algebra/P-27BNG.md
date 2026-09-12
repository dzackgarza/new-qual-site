---
schema: qual/card@1
id: P-27BNG
kind: problem
title: Intermediate fields of a finite cyclic Galois extension
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Field Extensions
relations: []
review: draft
---

::: problem
Let $K/F$ be a finite Galois extension and suppose $\Gal(K/F)$ is cyclic. Let $F\subseteq E\subseteq K$.

1. Show that both $K/E$ and $E/F$ are cyclic Galois extensions.
2. If $[K:F]=n$, show that for every divisor $d\mid n$ there is a unique intermediate field $E_d$ with
\[
[E_d:F]=d.
\]
:::

::: {.solution}
Let
\[
G=\Gal(K/F),
\qquad
H=\Gal(K/E).
\]
Since $G$ is cyclic, every subgroup of $G$ is cyclic and normal.

<1>1. Both intermediate extensions are cyclic Galois.
Because $H\le G$ and $G$ is cyclic, $H$ is cyclic. Hence
\[
\Gal(K/E)=H
\]
is cyclic, so $K/E$ is cyclic Galois.

Because every subgroup of a cyclic group is normal,
\[
H\trianglelefteq G.
\]
By the fundamental theorem of Galois theory, this is equivalent to $E/F$ being Galois, and restriction gives
\[
\Gal(E/F)\cong G/H.
\]
A quotient of a cyclic group is cyclic, so $E/F$ is cyclic Galois as well.

<1>2. There is a unique intermediate field of every divisor degree.
Write
\[
G=\langle g\rangle,
\qquad |G|=n.
\]
For each divisor $d\mid n$, a cyclic group has a unique subgroup of index $d$, namely
\[
H_d=\langle g^d\rangle,
\qquad |H_d|=n/d.
\]
Let
\[
E_d=K^{H_d}
\]
be its fixed field. By Galois correspondence,
\[
[E_d:F]=[G:H_d]=d.
\]
Uniqueness of $H_d$ gives uniqueness of $E_d$.

Thus the intermediate-field lattice of a finite cyclic Galois extension is exactly the divisor lattice of $[K:F]$.
:::
