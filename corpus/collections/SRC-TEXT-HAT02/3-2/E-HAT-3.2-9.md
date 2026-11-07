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
---

::: {.problem}
Show that if $H_n(X; \ZZ)$ is free for each $n$, then $H^*(X; \ZZ_p)$ and $H^*(X; \ZZ) \otimes \ZZ_p$ are isomorphic as rings, so in particular the ring structure with $\ZZ$ coefficients determines the ring structure with $\ZZ_p$ coefficients.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

By the universal coefficient theorem, $H^n(X; \ZZ_p) \cong \operatorname{Hom}(H_n(X), \ZZ_p) \oplus \operatorname{Ext}(H_{n-1}(X), \ZZ_p)$.

::: pf-proof

Theorem 3.2 (p.195), applied to the singular chain complex, whose terms are free abelian.

:::

:::

::: {.pf-step #s2}

Since $H_{n-1}(X)$ is free, $\operatorname{Ext}(H_{n-1}(X), \ZZ_p) = 0$.

::: pf-proof

The second of the three properties of Ext listed on p.195: $\operatorname{Ext}(H,G)=0$ if $H$ is free.

:::

:::

::: {.pf-step #s3}

Hence $H^n(X; \ZZ_p) \cong \operatorname{Hom}(H_n(X), \ZZ_p)$.

::: pf-proof

Steps [](#s1){.pf-ref} and [](#s2){.pf-ref}.

:::

:::

::: {.pf-step #s4}

Since $H_n(X)$ is free, $\operatorname{Hom}(H_n(X), \ZZ_p) \cong \operatorname{Hom}(H_n(X), \ZZ) \otimes \ZZ_p \cong H^n(X; \ZZ) \otimes \ZZ_p$.

::: pf-proof

For a free abelian $F$ with basis $B$, $\operatorname{Hom}(F,\ZZ_p)=\prod_B\ZZ_p=\operatorname{Hom}(F,\ZZ)\otimes\ZZ_p$; and $H^n(X;\ZZ)\cong\operatorname{Hom}(H_n(X),\ZZ)$ by Theorem 3.2 (p.195), again because $\operatorname{Ext}(H_{n-1},\ZZ)=0$.

:::

:::

::: {.pf-step #s5}

Hence $H^n(X; \ZZ_p) \cong H^n(X; \ZZ) \otimes \ZZ_p$ for each $n$.

::: pf-proof

Steps [](#s3){.pf-ref} and [](#s4){.pf-ref}.

:::

:::

::: {.pf-step #s6}

This isomorphism is compatible with the cup product (it is induced by the natural map $\ZZ \to \ZZ_p$ on coefficients, which is a ring homomorphism), so it is an isomorphism of rings.

::: pf-proof

The cochain formula of Lemma 3.6 (p.206) is polynomial in the two cochain values, so a ring homomorphism $R\to R'$ carries $\varphi\smile\psi$ to the cup product of the reduced cochains and gives a ring map $H^*(X;R)\to H^*(X;R')$; in particular $\ZZ\to\ZZ_p$ makes $H^*(X;\ZZ_p)$ a $\ZZ_p$-algebra. The isomorphism above is exactly this map followed by the identification with $H^*(X;\ZZ)\otimes\ZZ_p$.

:::

:::

::: {.pf-step #s7}

Hence $H^*(X; \ZZ_p) \cong H^*(X; \ZZ) \otimes \ZZ_p$ as rings.

::: pf-proof

Steps [](#s5){.pf-ref} and [](#s6){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s7){.pf-ref}.

:::

:::

:::
