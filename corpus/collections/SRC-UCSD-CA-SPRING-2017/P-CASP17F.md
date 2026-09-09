---
schema: qual/card@1
id: P-CASP17F
kind: problem
title: "Count roots of z^87 + 36z^57 + 71z^4 + z^3 - z + 1 in the annulus 1 <= |z| <= 2"
classification:
  areas:
  - complex-analysis
  topics:
  - Argument Principle
  - Rouché
  - Polynomial Roots
relations: []
review: draft
---

::: problem
Find the number of roots of the polynomial
$$
z^{87} + 36z^{57} + 71z^4 + z^3 - z + 1
$$
in the region $1 \leq |z| \leq 2$.
:::

::: solution
Let
\[
p(z)=z^{87}+36z^{57}+71z^4+z^3-z+1.
\]
On $|z|=1$,
\[
|z^{87}+36z^{57}+z^3-z+1|
\le 1+36+1+1+1=40<71=|71z^4|.
\]
Thus $p$ has exactly $4$ zeros in $|z|<1$.

On $|z|=2$,
\[
|36z^{57}+71z^4+z^3-z+1|
\le36\,2^{57}+71\,2^4+2^3+2+1<2^{87}=|z^{87}|.
\]
Hence $p$ has exactly $87$ zeros in $|z|<2$. The strict inequalities also
show that there are no zeros on either boundary circle. Therefore
\[
\boxed{87-4=83}
\]
zeros lie in $1\le|z|\le2$.
:::
