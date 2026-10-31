---
schema: qual/card@1
id: E-HAT-3.2-16
kind: problem
title: Torsion in products of CW complexes
classification:
  areas:
  - topology
  topics:
  - Cohomology
  - Cup Product
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
Show that if $X$ and $Y$ are finite CW complexes such that $H^*(X; \ZZ)$ and $H^*(Y; \ZZ)$ contain no elements of order a power of a given prime $p$, then the same is true for $X \times Y$.
[Apply Theorem 3.15 with coefficients in various fields.]
:::

::: {.solution}
For a finite CW complex $Z$, let $b_i$ be the rank of $H^i(Z;\ZZ)$, and let $t_i$ be the number of its cyclic summands whose order is a power of $p$. The coefficient exact sequence associated to multiplication by $p$ on integral cochains gives
$$
0\longrightarrow H^i(Z;\ZZ)/pH^i(Z;\ZZ)
\longrightarrow H^i(Z;\FF_p)
\longrightarrow H^{i+1}(Z;\ZZ)[p]\longrightarrow0.
$$
Since the integral cohomology groups are finitely generated,
$$
\dim_{\FF_p}H^i(Z;\FF_p)=b_i+t_i+t_{i+1},
\qquad
\dim_{\QQ}H^i(Z;\QQ)=b_i.
$$
The numbers $t_i$ are nonnegative. Hence equality of the two dimensions in every degree is equivalent to the absence of $p$-primary torsion in all the integral cohomology groups.

By hypothesis, the mod-$p$ and rational cohomology of each of $X$ and $Y$ have equal dimensions degree by degree. The field-coefficient Künneth theorem gives, for either field $F$,
$$
\dim_F H^n(X\times Y;F)
=\sum_{i+j=n}\dim_F H^i(X;F)\,\dim_F H^j(Y;F).
$$
The sums agree for $F=\FF_p$ and $F=\QQ$. Applying the preceding dimension criterion to the finite CW complex $X\times Y$ shows that its integral cohomology has no elements of order a power of $p$.
:::
