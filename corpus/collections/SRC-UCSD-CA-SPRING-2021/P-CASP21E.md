---
schema: qual/card@1
id: P-CASP21E
kind: problem
title: "No bounded holomorphic functions on D with zeros at a_n = 1 - 1/n for n >= 2"
classification:
  areas:
  - complex-analysis
  topics:
  - Blaschke Products
  - Bounded Holomorphic Functions
  - Zeros
relations: []
review: draft
---

::: problem
Let $a_n = 1 - \frac{1}{n}$ for $n \geq 2$.
Show that there are no bounded holomorphic functions $f : \Delta \to \mathbb{C}$ with zeros only at the $a_n$'s.
:::

::: solution
Suppose that a bounded nonzero holomorphic function $f$ on $\mathbb D$ has
zeros at all
\[
a_n=1-\frac1n,
\qquad n\ge2.
\]
The zeros of a bounded nonzero holomorphic function satisfy the Blaschke
condition
\[
\sum_n(1-|a_n|)<\infty.
\]
But here
\[
\sum_{n=2}^\infty(1-|a_n|)
=\sum_{n=2}^\infty\frac1n
=\infty.
\]
This contradiction proves that no such nonzero bounded holomorphic function
exists. The zero function is excluded because its zero set is all of
$\mathbb D$, not only the points $a_n$.
:::
