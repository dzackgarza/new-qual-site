---
schema: qual/card@1
id: E-HAT-3.2-9
kind: problem
title: $H^*(X;\mathbb Z_p)\cong H^*(X;\mathbb Z)\otimes\mathbb Z_p$ as rings when homology is free
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
Show that if $H_n(X; \mathbb{Z})$ is free for each $n$, then $H^*(X; \mathbb{Z}_p)$ and $H^*(X; \mathbb{Z}) \otimes \mathbb{Z}_p$ are isomorphic as rings, so in particular the ring structure with $\mathbb{Z}$ coefficients determines the ring structure with $\mathbb{Z}_p$ coefficients.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

By the universal coefficient theorem, $H^n(X; \mathbb{Z}_p) \cong \operatorname{Hom}(H_n(X), \mathbb{Z}_p) \oplus \operatorname{Ext}(H_{n-1}(X), \mathbb{Z}_p)$.

::: pf-proof

universal coefficient theorem for cohomology.

:::

:::

::: {.pf-step #s2}

Since $H_{n-1}(X)$ is free, $\operatorname{Ext}(H_{n-1}(X), \mathbb{Z}_p) = 0$.

::: pf-proof

$\operatorname{Ext}$ of a free abelian group vanishes.

:::

:::

::: {.pf-step #s3}

Hence $H^n(X; \mathbb{Z}_p) \cong \operatorname{Hom}(H_n(X), \mathbb{Z}_p)$.

::: pf-proof

Steps [](#s1){.pf-ref} and [](#s2){.pf-ref}.

:::

:::

::: {.pf-step #s4}

Since $H_n(X)$ is free, $\operatorname{Hom}(H_n(X), \mathbb{Z}_p) \cong \operatorname{Hom}(H_n(X), \mathbb{Z}) \otimes \mathbb{Z}_p \cong H^n(X; \mathbb{Z}) \otimes \mathbb{Z}_p$.

::: pf-proof

$\operatorname{Hom}(F, \mathbb{Z}_p) \cong \operatorname{Hom}(F, \mathbb{Z}) \otimes \mathbb{Z}_p$ for free $F$, and $H^n(X; \mathbb{Z}) \cong \operatorname{Hom}(H_n(X), \mathbb{Z})$ (since $\operatorname{Ext}(H_{n-1}, \mathbb{Z}) = 0$ by freeness).

:::

:::

::: {.pf-step #s5}

Hence $H^n(X; \mathbb{Z}_p) \cong H^n(X; \mathbb{Z}) \otimes \mathbb{Z}_p$ for each $n$.

::: pf-proof

Steps [](#s3){.pf-ref} and [](#s4){.pf-ref}.

:::

:::

::: {.pf-step #s6}

This isomorphism is compatible with the cup product (it is induced by the natural map $\mathbb{Z} \to \mathbb{Z}_p$ on coefficients, which is a ring homomorphism), so it is an isomorphism of rings.

::: pf-proof

the cup product is natural with respect to coefficient maps, and the reduction map $\mathbb{Z} \to \mathbb{Z}_p$ induces a ring homomorphism $H^*(X; \mathbb{Z}) \to H^*(X; \mathbb{Z}_p)$.

:::

:::

::: {.pf-step #s7}

Hence $H^*(X; \mathbb{Z}_p) \cong H^*(X; \mathbb{Z}) \otimes \mathbb{Z}_p$ as rings.

::: pf-proof

Steps [](#s5){.pf-ref} and [](#s6){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s7){.pf-ref}.

:::

:::

:::
