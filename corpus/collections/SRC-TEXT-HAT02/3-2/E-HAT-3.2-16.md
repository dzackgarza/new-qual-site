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
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.2, Exercise 16; it matches the printed text.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the criterion and its use: $\dim_F H^i(Z;F_p)=b_i+t_i+t_{i+1}$ with $t_i$ the number of
    $p$-power summands, so equality with $\dim_\QQ H^i(Z;\QQ)=b_i$ in every degree is exactly the
    absence of $p$-primary torsion; Künneth over $\FF_p$ and over $\QQ$ gives the same convolution
    on both sides for $X\times Y$, and the criterion then applies to $X\times Y$.
- event: solution-reviewed
  by: claude
  date: 2026-11-07
  note: >-
    Statement matches Exercise 16 (p.230) including the bracketed hint. Rechecked the criterion and its use: for a finite CW complex the coefficient sequence of 0 -> Z -> Z -> F_p -> 0 gives dim_Fp H^i(Z;F_p) = b_i + t_i + t_{i+1} with t_i the number of p-power summands, while dim_Q H^i(Z;Q) = b_i, so equality in every degree is exactly the vanishing of all t_i; Künneth over a field (Theorem 3.15 p.216) makes the dimension sequences of X x Y the convolutions of those of X and Y, which agree for F_p and for Q, so X x Y has no p-primary torsion. Citations added for Theorem 3.15. Not covered: the exercise leaves the field-coefficient Künneth to the reader and so does the card.
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

By hypothesis, the mod-$p$ and rational cohomology of each of $X$ and $Y$ have equal dimensions degree by degree. Theorem 3.15 (p.216) with field coefficients gives, for either field $F$ and in every degree $n$,
$$
\dim_F H^n(X\times Y;F)
=\sum_{i+j=n}\dim_F H^i(X;F)\,\dim_F H^j(Y;F).
$$
The sums agree for $F=\FF_p$ and $F=\QQ$. Applying the preceding dimension criterion to the finite CW complex $X\times Y$ shows that its integral cohomology has no elements of order a power of $p$.
:::
