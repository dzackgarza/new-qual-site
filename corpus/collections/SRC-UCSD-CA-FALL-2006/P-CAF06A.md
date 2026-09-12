---
schema: qual/card@1
id: P-CAF06A
kind: problem
title: "An analytic function on the disk with unit modulus on the boundary is rational"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: problem
If $f(z)$ is analytic in $|z| < 1$, continuous on $|z| \leq 1$ and satisfies $|f| = 1$ on $|z| = 1$, show that $f(z)$ is rational.

Hint: First consider the case that $f(z)$ has no zero.
:::

::: solution
Because $|f|=1$ on the unit circle and $f$ is continuous on the closed disk,
there is an annulus near $|z|=1$ on which $f$ has no zeros. Thus all zeros of
$f$ lie in a smaller closed disk, and hence there are only finitely many of
them, say $a_1,\dots,a_m$, repeated according to multiplicity.

For each $a_j$ let
\[
B_{a_j}(z)=\frac{z-a_j}{1-\overline{a_j}z}.
\]
Each $B_{a_j}$ is rational, holomorphic on the unit disk, has its only zero at
$a_j$, and satisfies $|B_{a_j}(z)|=1$ for $|z|=1$. Set
\[
B(z)=\prod_{j=1}^m B_{a_j}(z).
\]
Then
\[
h(z)=\frac{f(z)}{B(z)}
\]
extends holomorphically and without zeros across the zeros of $f$. Moreover
$|h|=1$ on $|z|=1$.

By the maximum modulus principle, $|h|\le1$ in the disk. Since $h$ is zero-free,
$1/h$ is holomorphic, and the same argument gives $|h|\ge1$. Hence $|h|=1$
throughout the disk, so $h$ is constant by the open mapping theorem. Therefore
\[
f(z)=c\prod_{j=1}^m\frac{z-a_j}{1-\overline{a_j}z},
\qquad |c|=1,
\]
which is rational.
:::
