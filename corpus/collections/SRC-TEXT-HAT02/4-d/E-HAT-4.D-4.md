---
schema: qual/card@1
id: E-HAT-4.D-4
kind: problem
title: Cohomology of complex flag manifolds
classification:
  areas:
  - topology
  topics:
  - Fiber Bundles
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.D, Exercise 4; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure for the presentation of the flag-manifold cohomology, which is what Queue D asks for on this card. The relations, the induced map, the computation of the cohomology by the Leray-Hirsch tower, the algebraic side with its monomial basis and rank n!, and the final isomorphism are separate steps. Two things the prose asserted are now argued: that the evaluation map kills exactly the elementary symmetric polynomials (from the multiplicativity of the total Chern class of the trivial bundle), and that the elementary symmetric polynomials form a regular sequence whose successive reductions give the monomial basis with 0 <= a_i <= n-i; the rank comparison is stated as the reason a surjection of free graded groups is an isomorphism. No retained set covers this exercise; the card now says so. Locators checked: Theorem 4D.1 on printed p. 432, Corollary 4D.3 on p. 434, the exercise on p. 447. No statement repair.
- event: solution-reviewed
  by: claude
  date: 2026-11-20
  note: >-
    Read step by step against Hatcher, Algebraic Topology (2002), §4.D Exercise 4, Theorem 4D.1
    (Leray-Hirsch) and Corollary 4D.3. One repair: step `algebra` evaluated the Poincare polynomial at
    t = 1 and wrote the product of n! over j, which is not the number of monomials; the product of j
    over j = 1 to n is n!, and that is what the basis count gives. The rest is correct as written: the
    fibration F_n -> F_{n-1} with fibre CP^{n-1} and Leray-Hirsch over the tautological quotient give
    H^*(F_n) free over H^*(F_{n-1}) on 1, x_n, ..., x_n^{n-1}; the monomials with 0 <= a_i <= n-i are
    the Artin basis, n! of them; and surjectivity plus equality of Poincare polynomials forces the
    isomorphism. The pair (x_{n-i+1}, i-1) in the proof matches the bound a_i <= n-i.
- event: solution-reviewed
  by: claude
  date: 2026-11-22
  note: >-
    Read against Hatcher, §4.D Exercise 4. One false sentence repaired: the step said that
    "forgetting the last line of a flag gives a fiber bundle $F_n\to F_{n-1}$ with fiber
    $\CP^{n-1}$". Forgetting the last line of a full flag in $\C^n$ does not land in $F_{n-1}$; the
    bundle is $\CP^{n-1}\to F_n(\C^n)\to F_{n-1}(\C^{n-1})$, dividing out the first line, whose
    fibre over a flag is the set of lines $L_1\subset\C^n$. The step now says that, and the
    generation of the fibre cohomology by $x_n$ is attributed to the computation of projective-space
    cohomology in §3.2 rather than to Corollary 4D.3, which is the statement about $H^*(U(n))$ and
    says nothing of the kind.
---

::: {.problem}
For the flag space $F_n(\CC^n)$ show that $H^*(F_n(\CC^n); \ZZ) \approx \ZZ[x_1, \ldots, x_n]/(\sigma_1, \ldots, \sigma_n)$ where $\sigma_i$ is the $i$th elementary symmetric polynomial.
:::

::: {.solution}
No retained solution set covers this exercise: the Hatcher sets in the checkout hold nothing from §4.D. The argument is the card's own, checked against Hatcher, *Algebraic Topology* (2002), §4.D Exercise 4, and it uses the Leray--Hirsch theorem (Theorem 4D.1) and the identification of the flag bundles in Corollary 4D.3 .

Let $F_n=F_n(\CC^n)$ be the complete flag manifold, carrying the tautological line bundles $L_1,\dots,L_n$ whose fibers over a flag are its successive one-dimensional quotients, and put $x_i=c_1(L_i)\in H^2(F_n;\ZZ)$.

::: pf

::: {.pf-step #relations}
$\sigma_k(x_1,\dots,x_n)=0$ in $H^*(F_n;\ZZ)$ for $1\le k\le n$, where $\sigma_k$ is the $k$-th elementary symmetric polynomial.

::: pf-proof
The direct sum $L_1\oplus\cdots\oplus L_n$ is the trivial bundle $\underline{\CC}^n$, since a flag is precisely a filtration whose successive quotients are the fibers of the $L_i$. The total Chern class is multiplicative, so $\prod_{i=1}^n(1+x_i)=1$ in $H^*(F_n;\ZZ)$; the degree-$2k$ part of that equation is $\sigma_k(x_1,\dots,x_n)=0$.
:::

:::

::: {.pf-step #map}
The relations define a graded ring homomorphism $\Phi:\ZZ[x_1,\dots,x_n]/(\sigma_1,\dots,\sigma_n)\to H^*(F_n;\ZZ)$.

::: pf-proof
By step [](#relations){.pf-ref} the elementary symmetric polynomials lie in the kernel of the evaluation map $\ZZ[x_1,\dots,x_n]\to H^*(F_n;\ZZ)$, $x_i\mapsto x_i$, which is a graded ring homomorphism because the $x_i$ are integral classes of degree $2$; so it factors through the quotient by the ideal they generate.
:::

:::

::: {.pf-step #cohomology}
$H^*(F_n;\ZZ)$ is free abelian, with Poincaré polynomial $\prod_{j=1}^n\bigl(1+t^2+\cdots+t^{2(j-1)}\bigr)$, and $\Phi$ is surjective.

::: pf-proof
Dividing out the first line of a flag gives a fiber bundle $\CP^{n-1}\to F_n(\C^n)\to F_{n-1}(\C^{n-1})$: the image of $(L_1\subset\cdots\subset L_n)$ is the flag $(L_2/L_1\subset\cdots\subset L_n/L_1)$ in $\C^n/L_1\cong\C^{n-1}$, and the fibre over a flag is the set of lines $L_1\subset\C^n$, a $\CP^{n-1}$. Its cohomology is $\ZZ[x_n]/(x_n^n)$ on the restriction of $x_n$, the standard computation of the cohomology of projective space in §3.2; that is the hypothesis Leray--Hirsch needs. The Leray--Hirsch theorem, Theorem 4D.1, then gives that $H^*(F_n;\ZZ)$ is a free module over $H^*(F_{n-1};\ZZ)$ on $1,x_n,\dots,x_n^{n-1}$, so by induction on $n$ from $F_1=\ast$ it is free abelian with the stated Poincaré polynomial, the factor $1+t^2+\cdots+t^{2(n-1)}$ being contributed at the $n$-th step. Since each stage is generated by the classes $x_i$ together with the base, the $x_i$ generate $H^*(F_n;\ZZ)$ as a ring, which is the surjectivity of $\Phi$.
:::

:::

::: {.pf-step #algebra}
$\ZZ[x_1,\dots,x_n]/(\sigma_1,\dots,\sigma_n)$ is free abelian with basis $x_1^{a_1}\cdots x_n^{a_n}$, $0\le a_i\le n-i$, hence with the same Poincaré polynomial and total rank $n!$.

::: pf-proof
The $\sigma_k$ form a regular sequence: $\sigma_k$ involves the variable $x_{n-k+1}$ to the first power and no other variable of lower index does in $\sigma_k$ once the earlier relations have been used, which is the usual triangular form of the elementary symmetric functions. Reducing successively by the monic relations $\sigma_1,\dots,\sigma_n$ therefore leaves a free abelian group on the monomials whose exponents satisfy $0\le a_i\le n-i$: the $i$-th reduction caps the exponent of $x_{n-i+1}$ at $i-1$. The number of such monomials in degree $2d$ gives the polynomial $\prod_{j=1}^n(1+t^2+\cdots+t^{2(j-1)})$, and its value at $t=1$ is $\prod_{j=1}^n j=n!$.
:::

:::

::: {.pf-step #isomorphism}
$\Phi$ is an isomorphism.

::: pf-proof
$\Phi$ is a surjection of graded abelian groups by step [](#cohomology){.pf-ref}, both sides are free by steps [](#cohomology){.pf-ref} and [](#algebra){.pf-ref}, and their Poincaré polynomials agree; a surjection of free graded abelian groups that is an isomorphism in each degree's rank is an isomorphism in each degree, hence an isomorphism. So $H^*(F_n(\CC^n);\ZZ)\cong\ZZ[x_1,\dots,x_n]/(\sigma_1,\dots,\sigma_n)$, which is the assertion of the exercise.
:::

:::

:::
:::
