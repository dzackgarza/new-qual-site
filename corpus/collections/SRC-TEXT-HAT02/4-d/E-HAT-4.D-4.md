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
- event: solution-reviewed
  by: claude
  date: 2026-11-22
  note: >-
    Correction to the preceding event. The bundle it described, dividing out the first line to get
    $\CP^{n-1}\to F_n(\C^n)\to F_{n-1}(\C^{n-1})$, is a genuine bundle but not the one the argument
    needs: $H^*(F_n)$ is not free over $H^*(F_{n-1})$, since for $n=3$ every nonzero class in
    $H^2(F_3)$ has nonzero square while the generator of $H^2(F_2)$ squares to zero, so there is no
    ring map from $H^*(F_2)=\ZZ[y]/(y^2)$ into $H^*(F_3)$ to serve as the base of a free module. The
    step now uses the bundle $F_{n-1}(\C^{n-1})\to F_n(\C^n)\to\CP^{n-1}$ given by the first line,
    over whose base $H^*(\CP^{n-1})=\ZZ[x_1]/(x_1^n)$ Leray--Hirsch applies, and concludes that
    $H^*(F_n)$ is free over $\ZZ[x_1]/(x_1^n)$ on the monomials $x_2^{a_2}\cdots x_n^{a_n}$ with
    $0\le a_i\le n-i$ — the correct statement, and the one that yields the Poincaré polynomial.
- event: solution-reviewed
  by: claude
  date: 2026-11-22
  note: >-
    Two further corrections in step `algebra`, from independent readings. The sentence justifying
    regularity said $\sigma_k$ "involves the variable $x_{n-k+1}$ to the first power"; that is not what
    makes the sequence regular. It now runs the triangular argument: as a polynomial in $x_n$,
    $\sigma_n=x_n\sigma_{n-1}(x_1,\dots,x_{n-1})$ is linear with leading coefficient
    $\sigma_{n-1}(x_1,\dots,x_{n-1})$, and the same holds one variable at a time for
    $\sigma_{n-1},\dots,\sigma_1$ after quotienting by the later ones.
- event: solution-reviewed
  by: claude
  date: 2026-11-22
  note: >-
    Third correction to this card, in step `algebra`. The triangular justification of the monomial
    basis is false: for $n=2$ one has $\sigma_2\equiv -x_2^2$ modulo $\sigma_1$, so the elementary
    symmetric functions are not a Gröbner basis and successive reduction by them does not produce the
    stated exponents. The step now names the statement for what it is — the Artin basis theorem for
    the coinvariant ring of the symmetric group, whose standard monomials are
    $x_1^{a_1}\cdots x_n^{a_n}$ with $0\le a_i\le n-i$, $n!$ of them — cites it rather than
    reproving it, and records the counterexample to the reduction argument it replaces. The Poincaré
    polynomial and the rank $n!$ follow from the basis as before.
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
Taking the first line of a flag gives a fiber bundle $F_{n-1}(\C^{n-1})\to F_n(\C^n)\xrightarrow{p}\CP^{n-1}$: the fibre over $L_1$ is the set of full flags whose first line is $L_1$, which is the flag manifold of $\C^n/L_1\cong\C^{n-1}$. The class $x_1$ restricts to a generator of $H^2(\CP^{n-1};\ZZ)$ and $H^*(\CP^{n-1};\ZZ)=\ZZ[x_1]/(x_1^n)$, the computation of projective-space cohomology in §3.2. By induction on $n$ from $F_1=\ast$, $H^*(F_{n-1};\ZZ)$ is free on the monomials $x_2^{a_2}\cdots x_n^{a_n}$ with $0\le a_i\le n-i$, and these classes restrict to a basis of the cohomology of the fibre, so the Leray--Hirsch theorem, Theorem 4D.1, gives that $H^*(F_n;\ZZ)$ is a free module over $\ZZ[x_1]/(x_1^n)$ on those monomials. Hence it is free abelian with the stated Poincaré polynomial, the factor $1+t^2+\cdots+t^{2(n-1)}$ being contributed by the base at the $n$-th step, and the classes $x_1,\dots,x_n$ generate $H^*(F_n;\ZZ)$ as a ring, which is the surjectivity of $\Phi$. (The bundle with base $F_{n-1}$ and fibre $\CP^{n-1}$, obtained by dividing out the first line, is not the one to use: $H^*(F_n)$ is not free over $H^*(F_{n-1})$, since for $n=3$ every nonzero class in $H^2(F_3)$ has nonzero square, whereas the generator of $H^2(F_2)$ squares to zero.)
:::

:::

::: {.pf-step #algebra}
$\ZZ[x_1,\dots,x_n]/(\sigma_1,\dots,\sigma_n)$ is free abelian with basis $x_1^{a_1}\cdots x_n^{a_n}$, $0\le a_i\le n-i$, hence with the same Poincaré polynomial and total rank $n!$.

::: pf-proof
The quotient is the coinvariant ring of the symmetric group acting on $\ZZ[x_1,\dots,x_n]$ by permuting the variables, and its standard monomial basis is the set of $x_1^{a_1}\cdots x_n^{a_n}$ with $0\le a_i\le n-i$, of which there are $n!$; that is the Artin basis theorem for coinvariant rings, and it is cited here rather than reproved — no source for it is retained on this machine, so it is named by author and result and not by a numbered statement. A triangular reduction by the $\sigma$'s is not available: for $n=2$ one has $\sigma_2\equiv -x_2^2$ modulo $\sigma_1$, so the elementary symmetric functions are not a Gröbner basis in any variable order, and the basis statement is genuinely a theorem about the quotient. Given it, the monomials in degree $2d$ give the polynomial $\prod_{j=1}^n(1+t^2+\cdots+t^{2(j-1)})$, and its value at $t=1$ is $\prod_{j=1}^n j=n!$.
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
