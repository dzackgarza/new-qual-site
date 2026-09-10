---
schema: qual/card@1
id: E-W5KED
kind: problem
title: Realizing finitely generated abelian groups and cyclic free products
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
---

::: {.exercise}

Find spaces whose fundamental groups are isomorphic to the following groups.
(Here $\mathbb{Z}/n$ denotes the additive group of integers modulo $n$.)

(a) $\mathbb{Z}/n \times \mathbb{Z}/m$

(b) $\mathbb{Z}/n_1 \times \mathbb{Z}/n_2 \times \cdots \times \mathbb{Z}/n_k$

(c) $\mathbb{Z}/n * \mathbb{Z}/m$.
(See [[E-5DDIL]].)

(d) $\mathbb{Z}/n_1 * \mathbb{Z}/n_2 * \cdots * \mathbb{Z}/n_k$
:::

::: {.solution}
For \(n\ge1\), let \(M_n\) be the space obtained from a circle by attaching a 2-cell by a degree-\(n\) map. The adjoining-a-two-cell theorem gives
\[
\pi_1(M_n)\cong\langle a\mid a^n=1\rangle\cong\mathbb Z/n.
\]

(a) Take
\[
X=M_n\times M_m.
\]
For path-connected spaces, \(\pi_1(X\times Y)\cong\pi_1(X)\times\pi_1(Y)\), hence
\[
\pi_1(X)\cong\mathbb Z/n\times\mathbb Z/m.
\]

(b) More generally, take
\[
X=M_{n_1}\times\cdots\times M_{n_k}.
\]
Then
\[
\pi_1(X)\cong\mathbb Z/n_1\times\cdots\times\mathbb Z/n_k.
\]

(c) Take the wedge
\[
X=M_n\vee M_m
\]
at ordinary CW basepoints. The wedge theorem gives
\[
\pi_1(X)\cong\pi_1(M_n)*\pi_1(M_m)
\cong \mathbb Z/n * \mathbb Z/m.
\]

(d) Likewise,
\[
X=M_{n_1}\vee\cdots\vee M_{n_k}
\]
has
\[
\pi_1(X)\cong
\mathbb Z/n_1*\cdots*\mathbb Z/n_k.
\]
These spaces are finite two-dimensional CW complexes.
:::
