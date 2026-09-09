---
schema: qual/card@1
id: P-CASP06F
kind: problem
title: "Jensen's inequality for zeros of an analytic function on a disk"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: problem
Let $f$ be holomorphic on the closed disc of radius $R$ and assume that $f(0) \neq 0$.
Let the zeros of $f$ in the open disc be ordered by increasing absolute value, $z_1, z_2, \ldots, z_N$, each zero being repeated according to its multiplicity.
Prove that $$|f(0)| \leq \frac{\sup_{|z|=R} |f(z)|}{R^N} |z_1 z_2 \cdots z_N|.$$
:::

::: solution
For a zero $a$ with $|a|<R$, define the radius-$R$ Blaschke factor
\[
B_a(z)=\frac{R(z-a)}{R^2-\overline a z}.
\]
It is holomorphic on a neighborhood of the closed disk, vanishes simply at
$a$, and satisfies $|B_a(z)|=1$ on $|z|=R$.

Since the zeros $z_1,\dots,z_N$ are repeated according to multiplicity,
\[
g(z)=\frac{f(z)}{\prod_{j=1}^N B_{z_j}(z)}
\]
extends holomorphically across every zero and is zero-free in the open disk.
On the boundary $|z|=R$,
\[
|g(z)|=|f(z)|.
\]
By the maximum principle,
\[
|g(0)|\le \sup_{|z|=R}|f(z)|.
\]
But
\[
|B_{z_j}(0)|=\frac{|z_j|}{R},
\]
so
\[
|g(0)|
=|f(0)|\frac{R^N}{|z_1z_2\cdots z_N|}.
\]
Rearranging yields
\[
\boxed{
|f(0)|\le
\frac{\sup_{|z|=R}|f(z)|}{R^N}
|z_1z_2\cdots z_N|}.
\]
:::
