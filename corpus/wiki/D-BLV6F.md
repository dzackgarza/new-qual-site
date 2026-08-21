---
schema: qual/card@1
id: D-BLV6F
kind: definition
title: Cyclotomic Polynomials
classification:
  areas:
  - algebra
  topics:
  - Roots of Unity
  - Polynomials
  - Galois Theory
relations: []
review: draft
---

:::{.definition title="Cyclotomic Polynomials"}
Let $\zeta_n = e^{2\pi i/n}$, then the **$n$th cyclotomic polynomial** is given by
$$
\Phi_{n}(x)=\prod_{k=1 \atop (j, n)=1}^{n}\left(x- \zeta_n^k\right) \in \ZZ[x]
,$$

which is a product over primitive roots of unity.
It is the unique irreducible polynomial which is a divisor of $x^n - 1$ but *not* a divisor of $x^k-1$ for any $k<n$.


Note that $\deg \Phi_n(x) = \phi(n)$ for $\phi$ the totient function.
:::
