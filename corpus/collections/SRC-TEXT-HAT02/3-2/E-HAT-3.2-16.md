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
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read against Hatcher, Exercise 16 of §3.2, printed p. 230, with Theorem 3.15 (printed p. 216).
    Correct. The coefficient sequence $0\to\ZZ\to\ZZ\to\FF_p\to0$ gives
    $0\to H^i(Z;\ZZ)/pH^i(Z;\ZZ)\to H^i(Z;\FF_p)\to H^{i+1}(Z;\ZZ)[p]\to0$, and for a finitely
    generated $A$ one has $\dim A/pA=\operatorname{rank}A+(\text{number of }p\text{-power summands})$
    and $\dim A[p]=(\text{number of }p\text{-power summands})$, so
    $\dim_{\FF_p}H^i(Z;\FF_p)=b_i+t_i+t_{i+1}$ while $\dim_\QQ H^i(Z;\QQ)=b_i$; since the $t_i$ are
    non-negative, equality in every degree is exactly the vanishing of all $p$-primary torsion.
    Künneth over a field makes the dimension sequence of $X\times Y$ the convolution of those of
    $X$ and $Y$, the same convolution for $\FF_p$ and for $\QQ$ by the hypothesis, and the criterion
    applied to $X\times Y$ concludes. Nothing changed. Not claimed: a certificate.
---

::: {.problem}
Show that if $X$ and $Y$ are finite CW complexes such that $H^*(X; \ZZ)$ and $H^*(Y; \ZZ)$ contain no elements of order a power of a given prime $p$, then the same is true for $X \times Y$.
[Apply Theorem 3.15 with coefficients in various fields.]
:::

::: {.solution}

No separate retained solution set is needed here: the card's own argument is complete and is set out as steps, the criterion on $p$-primary torsion and the field-coefficient Künneth computation being the two ingredients.

Throughout, $Z$ is a finite CW complex, $b_{i}=\operatorname{rank}H^{i}(Z;\ZZ)$ and $t_{i}$ is the number of cyclic summands of $H^{i}(Z;\ZZ)$ whose order is a power of the fixed prime $p$.

::: pf

::: {.pf-step #criterion}
$\dim_{\FF_{p}}H^{i}(Z;\FF_{p})=b_{i}+t_{i}+t_{i+1}$ and $\dim_{\QQ}H^{i}(Z;\QQ)=b_{i}$; hence $Z$ has no $p$-primary torsion exactly when these two dimensions agree in every degree.

::: pf-proof
The coefficient sequence $0\to\ZZ\to\ZZ\to\FF_{p}\to0$ (the first map multiplication by $p$) induces the exact sequence $0\to H^{i}(Z;\ZZ)/pH^{i}(Z;\ZZ)\to H^{i}(Z;\FF_{p})\to H^{i+1}(Z;\ZZ)[p]\to0$. For a finitely generated abelian group $A$ the group $A/pA$ has dimension (over $\FF_{p}$) equal to the number of free summands plus the number of $p$-power summands, and $A[p]$ has dimension the number of $p$-power summands, so the two outer terms have dimensions $b_{i}+t_{i}$ and $t_{i+1}$; exactness gives the first formula, and the universal coefficient theorem gives $\dim_{\QQ}H^{i}(Z;\QQ)=b_{i}$. Since each $t_{i}\ge0$, equality in all degrees holds exactly when all $t_{i}=0$.
:::

:::

::: {.pf-step #hypothesis}
For $F=\FF_{p}$ and for $F=\QQ$, $\dim_{F}H^{i}(X;F)=\dim_{F}H^{i}(Y;F)=\dim_{\QQ}H^{i}(X;\QQ)$ and $\dim_{\QQ}H^{i}(Y;\QQ)$ respectively, in every degree.

::: pf-proof
By the hypothesis that $H^{*}(X;\ZZ)$ and $H^{*}(Y;\ZZ)$ have no elements of order a power of $p$, the criterion of step [](#criterion){.pf-ref} gives $\dim_{\FF_{p}}H^{i}(X;\FF_{p})=\dim_{\QQ}H^{i}(X;\QQ)$ and likewise for $Y$, in every degree.
:::

:::

::: {.pf-step #kunneth}
For any field $F$ and every $n$, $\dim_{F}H^{n}(X\times Y;F)=\sum_{i+j=n}\dim_{F}H^{i}(X;F)\dim_{F}H^{j}(Y;F)$.

::: pf-proof
Over a field the Künneth formula is the isomorphism $H^{n}(X\times Y;F)\cong\bigoplus_{i+j=n}H^{i}(X;F)\otimes_{F}H^{j}(Y;F)$ (Theorem 3.15, printed p. 216), whose right side has the stated dimension because dimensions multiply under tensor products over a field.
:::

:::

::: {.pf-step #convolve}
$\dim_{\FF_{p}}H^{n}(X\times Y;\FF_{p})=\dim_{\QQ}H^{n}(X\times Y;\QQ)$ for every $n$.

::: pf-proof
By steps [](#hypothesis){.pf-ref} and [](#kunneth){.pf-ref} both sides are the convolution $\sum_{i+j=n}d_{i}e_{j}$ of the same two sequences $(d_{i})$ and $(e_{j})$, namely the rational Betti numbers of $X$ and of $Y$.
:::

:::

::: {.pf-qed}
$X\times Y$ is again a finite CW complex, and step [](#convolve){.pf-ref} says the criterion of step [](#criterion){.pf-ref} is met in every degree, so $H^{*}(X\times Y;\ZZ)$ has no elements of order a power of $p$.
:::

:::

:::
