---
schema: qual/card@1
id: P-UCTOP290-S6-3
kind: problem
title: Top homology of a connected simplicial pseudomanifold
classification:
  areas:
  - topology
  topics:
  - Simplicial Homology
  - Manifolds
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-10-31
  note: Read sheet 6, Problem 3 in its checked-in extraction and page image.
---

::: {.problem}
Let $K$ be an $n$-dimensional simplicial complex,
$n\ge1$. Suppose every $(n-1)$-simplex belongs
to exactly two $n$-simplices, and any two
$n$-simplices can be joined by a sequence in
which consecutive simplices share an
$(n-1)$-face. Show that $H_n(K;\ZZ)$ is either
$0$ or $\ZZ$. In the second case describe a
generator.
:::

::: {.solution}

There are no $(n+1)$-simplices, so $H_n(K;\ZZ)$
is the kernel of the simplicial boundary
$\partial_n$. Choose orientations for all
$n$-simplices and fix one simplex $\sigma_0$.
If $z=\sum_\sigma c_\sigma\sigma$ is a cycle,
then on a face shared by $\sigma$ and $\tau$,
the coefficient of $\partial_n z$ is
$\varepsilon_\sigma c_\sigma+
\varepsilon_\tau c_\tau$, with each
$\varepsilon$ equal to $+1$ or $-1$.
Thus $c_\tau=\pm c_\sigma$.

The adjacency hypothesis propagates this
relation from $\sigma_0$ to every top simplex.
Consequently a cycle is determined by its
integer coefficient on $\sigma_0$, and the
map $H_n(K;\ZZ)\to\ZZ$ taking that coefficient
is injective. Its image is a subgroup of
$\ZZ$, hence is either zero or infinite cyclic.

If a nonzero cycle exists, every top simplex
has coefficient of the same absolute value.
Dividing all coefficients by that common
positive integer gives a cycle whose
coefficients are $\pm1$. It is the oriented
sum of all $n$-simplices and generates $H_n$.
In an infinite complex this sum is a
simplicial chain only if it has finite support;
otherwise the nonzero case cannot occur.
:::
