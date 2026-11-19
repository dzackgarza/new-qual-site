---
schema: qual/card@1
id: E-HAT-3.2-9
kind: problem
title: $H^*(X;\ZZ_p)\cong H^*(X;\ZZ)\otimes\ZZ_p$ as rings when homology is free
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
  date: 2026-08-30
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.2, Exercise 9; it matches the printed text.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the chain of identifications: $\operatorname{Ext}$ vanishes because $H_{n-1}$ is free, so
    $H^n(X;\ZZ_p)=\operatorname{Hom}(H_n,\ZZ_p)=\operatorname{Hom}(H_n,\ZZ)\otimes\ZZ_p=H^n(X;\ZZ)\otimes\ZZ_p$;
    the isomorphism is induced by the ring map $\ZZ\to\ZZ_p$ on coefficients, so it preserves cup
    products.
- event: solution-reviewed
  by: claude
  date: 2026-11-07
  note: >-
    Statement matches Exercise 9 (p.229). Rechecked: Ext(H_{n-1},Z_p) = 0 and Ext(H_{n-1},Z) = 0 by freeness, so H^n(X;Z_p) = Hom(H_n,Z_p) = Hom(H_n,Z) tensor Z_p = H^n(X;Z) tensor Z_p, and the identification is multiplicative because the cochain cup product formula of Lemma 3.6 p.206 is polynomial in the values, so a coefficient ring map carries cup products to cup products. Terse proofs now cite Theorem 3.2 p.195 and the properties of Ext on p.195, and the multiplicativity argument is written out instead of alluded to. Not covered: no example showing the hypothesis is needed.
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Read against Hatcher, Exercise 9 of §3.2, printed p. 229, with Theorem 3.2 and the properties of
    $\operatorname{Ext}$ on printed p. 195 and the cochain cup product formula of Lemma 3.6 on
    printed p. 206. The mathematics is right: freeness kills both Ext terms, so
    $H^n(X;\ZZ_p)=\operatorname{Hom}(H_n,\ZZ_p)=\operatorname{Hom}(H_n,\ZZ)\otimes\ZZ_p=H^n(X;\ZZ)\otimes\ZZ_p$,
    the middle step because for free $F$ both sides are $\prod_B\ZZ_p$; and the identification is
    multiplicative because the cochain cup product is polynomial in the values, so the coefficient
    map $\ZZ\to\ZZ_p$ carries cup products to cup products. Rewritten from seven steps, of which
    five were proved by naming others and one closed a `pf-qed` by label, into two steps that carry
    the two halves. Not claimed: an example showing the hypothesis is needed, and no certificate.
---

::: {.problem}
Show that if $H_n(X; \ZZ)$ is free for each $n$, then $H^*(X; \ZZ_p)$ and $H^*(X; \ZZ) \otimes \ZZ_p$ are isomorphic as rings, so in particular the ring structure with $\ZZ$ coefficients determines the ring structure with $\ZZ_p$ coefficients.
:::

::: {.solution}
Assume $H_n(X;\ZZ)$ is free for every $n$; the exercise is Exercise 9 of §3.2, printed p.~229. Coefficients $\ZZ_p$ are written for a prime $p$.

::: pf

::: {.pf-step #s1}

$H^n(X;\ZZ_p)\cong H^n(X;\ZZ)\otimes\ZZ_p$ for every $n$.

::: pf-proof

The universal coefficient sequence of Theorem 3.2 (printed p.~195) is
$$
0\to\operatorname{Ext}(H_{n-1}(X),\ZZ_p)\to H^n(X;\ZZ_p)\to\operatorname{Hom}(H_n(X),\ZZ_p)\to0,
$$
and $\operatorname{Ext}$ vanishes because $H_{n-1}(X)$ is free, by the properties of $\operatorname{Ext}$ listed on the same page. For a free $F$ with basis $B$ one has $\operatorname{Hom}(F,\ZZ_p)=\prod_B\ZZ_p=(\prod_B\ZZ)\otimes\ZZ_p=\operatorname{Hom}(F,\ZZ)\otimes\ZZ_p$, the middle equality because tensoring the exact sequence $0\to\ZZ\to\ZZ\to\ZZ_p\to0$ with the product gives $\prod_B\ZZ_p$. Applying this to $F=H_n(X)$ and using $H^n(X;\ZZ)\cong\operatorname{Hom}(H_n(X),\ZZ)$, again because the Ext term vanishes, gives the claim.

:::

:::

::: {.pf-step #s2}

The isomorphism is multiplicative, so it is an isomorphism of graded rings.

::: pf-proof

The coefficient homomorphism $\ZZ\to\ZZ_p$ induces a ring map $H^*(X;\ZZ)\to H^*(X;\ZZ_p)$: on cochains the cup product of Lemma 3.6 (printed p.~206) is a polynomial expression in the values of the two cochains, so reducing values along a ring homomorphism carries $\varphi\smile\psi$ to the cup product of the reduced cochains. Composing with the quotient map $H^*(X;\ZZ)\to H^*(X;\ZZ)\otimes\ZZ_p$ gives a ring map $H^*(X;\ZZ)\otimes\ZZ_p\to H^*(X;\ZZ_p)$, which is the isomorphism of the first step in every degree and hence an isomorphism of graded rings.

:::

:::

:::
:::
