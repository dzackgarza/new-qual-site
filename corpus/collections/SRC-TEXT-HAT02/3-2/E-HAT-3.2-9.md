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
---

::: {.problem}
Show that if $H_n(X; \ZZ)$ is free for each $n$, then $H^*(X; \ZZ_p)$ and $H^*(X; \ZZ) \otimes \ZZ_p$ are isomorphic as rings, so in particular the ring structure with $\ZZ$ coefficients determines the ring structure with $\ZZ_p$ coefficients.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

By the universal coefficient theorem, $H^n(X; \ZZ_p) \cong \operatorname{Hom}(H_n(X), \ZZ_p) \oplus \operatorname{Ext}(H_{n-1}(X), \ZZ_p)$.

::: pf-proof

universal coefficient theorem for cohomology.

:::

:::

::: {.pf-step #s2}

Since $H_{n-1}(X)$ is free, $\operatorname{Ext}(H_{n-1}(X), \ZZ_p) = 0$.

::: pf-proof

$\operatorname{Ext}$ of a free abelian group vanishes.

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

$\operatorname{Hom}(F, \ZZ_p) \cong \operatorname{Hom}(F, \ZZ) \otimes \ZZ_p$ for free $F$, and $H^n(X; \ZZ) \cong \operatorname{Hom}(H_n(X), \ZZ)$ (since $\operatorname{Ext}(H_{n-1}, \ZZ) = 0$ by freeness).

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

the cup product is natural with respect to coefficient maps, and the reduction map $\ZZ \to \ZZ_p$ induces a ring homomorphism $H^*(X; \ZZ) \to H^*(X; \ZZ_p)$.

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
