---
schema: qual/card@1
id: P-CAF05A
kind: problem
title: "Analytic functions with prescribed boundary modulus and zeros in a disk"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: problem
Find all functions $f \in H(B(0; 2))$ such that:

(a) $|f(z)| = 1$ if $|z| = 1$.

(b) $f$ has a zero of multiplicity 2 at $z = 1/2$ and no other zeroes.

Hint: Consider first the case where $f$ satisfies (a), but has no zeroes.
:::

::: solution
Let
\[
B(z)=\frac{z-\frac12}{1-\frac12 z}.
\]
The denominator vanishes only at $z=2$, so $B$ is holomorphic on $B(0,2)$.
It has a simple zero at $1/2$, and for $|z|=1$ one has $|B(z)|=1$.
Therefore
\[
h(z)=\frac{f(z)}{B(z)^2}
\]
extends holomorphically across $z=1/2$ and is zero-free on $B(0,2)$. On the unit
circle, $|h|=1$.

Apply the maximum modulus principle to $h$ on the unit disk to obtain
$|h(z)|\le1$ for $|z|<1$. Since $h$ is zero-free there, $1/h$ is holomorphic,
and applying the same argument to $1/h$ gives $|h(z)|\ge1$. Hence
$|h(z)|=1$ throughout the unit disk. By the open mapping theorem, $h$ is
constant there, and therefore constant on all of $B(0,2)$ by the identity
theorem.

Thus every solution has the form
\[
\boxed{\displaystyle
f(z)=c\left(\frac{z-\frac12}{1-\frac12z}\right)^2,
\qquad |c|=1.}
\]
Conversely, every such function is holomorphic on $B(0,2)$, has exactly the
required double zero, and has modulus $1$ on $|z|=1$.
:::
