---
schema: qual/card@1
id: P-WK45L
kind: problem
title: Galois group of $x^2+9$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Splitting Fields
relations: []
review: draft
---

::: problem
What is the Galois group of $x^2+9$ over $\QQ$?
:::

::: solution
The roots are
\[
\pm 3i,
\]
so the splitting field is
\[
\QQ(i).
\]
Since $x^2+1$ is irreducible over $\QQ$,
\[
[\QQ(i):\QQ]=2.
\]
Thus the Galois group has two elements: the identity and complex conjugation,
\[
i\longmapsto -i.
\]
Therefore
\[
\operatorname{Gal}(x^2+9/\QQ)\cong C_2.
\]
:::
