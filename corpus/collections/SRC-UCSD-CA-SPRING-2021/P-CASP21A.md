---
schema: qual/card@1
id: P-CASP21A
kind: problem
title: "Count solutions of z^3 sin z + 5z^2 + 2 = 0 in the unit disk"
classification:
  areas:
  - complex-analysis
  topics:
  - Rouché
  - Polynomial Roots
  - Argument Principle
relations: []
review: draft
---

::: problem
How many solutions, counted with multiplicities, does the equation
$$
z^3 \sin z + 5z^2 + 2 = 0
$$
have in the unit disc $|z| < 1$?
:::

::: solution
On $|z|=1$,
\[
|z^3\sin z|\le \sinh 1<2,
\]
while
\[
|5z^2+2|\ge 5-2=3.
\]
Hence Rouché's theorem shows that
$z^3\sin z+5z^2+2$ and $5z^2+2$ have the same number of zeros in
$\mathbb D$, counted with multiplicity. The latter polynomial has the two
zeros
\[
z=\pm i\sqrt{\frac25},
\]
both in $\mathbb D$. Therefore the given equation has exactly
\[
\boxed{2}
\]
solutions in the unit disk, counted with multiplicity.
:::
