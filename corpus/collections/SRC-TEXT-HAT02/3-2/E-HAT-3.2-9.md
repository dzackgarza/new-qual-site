---
schema: qual/card@1
id: E-HAT-3.2-9
kind: problem
title: Hatcher Section 3.2 Exercise 9
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

# E-HAT-3.2-9

Show that if $H_n(X; \mathbb{Z})$ is free for each $n$, then $H^*(X; \mathbb{Z}_p)$ and $H^*(X; \mathbb{Z}) \otimes \mathbb{Z}_p$ are isomorphic as rings, so in particular the ring structure with $\mathbb{Z}$ coefficients determines the ring structure with $\mathbb{Z}_p$ coefficients.

::: {.solution}
<1>1. By the universal coefficient theorem, $H^n(X; \mathbb{Z}_p) \cong \operatorname{Hom}(H_n(X), \mathbb{Z}_p) \oplus \operatorname{Ext}(H_{n-1}(X), \mathbb{Z}_p)$.
::: {.proof}
universal coefficient theorem for cohomology.
:::

<1>2. Since $H_{n-1}(X)$ is free, $\operatorname{Ext}(H_{n-1}(X), \mathbb{Z}_p) = 0$.
::: {.proof}
$\operatorname{Ext}$ of a free abelian group vanishes.
:::

<1>3. Hence $H^n(X; \mathbb{Z}_p) \cong \operatorname{Hom}(H_n(X), \mathbb{Z}_p)$.
::: {.proof}
<1>1 and <1>2.
:::

<1>4. Since $H_n(X)$ is free, $\operatorname{Hom}(H_n(X), \mathbb{Z}_p) \cong \operatorname{Hom}(H_n(X), \mathbb{Z}) \otimes \mathbb{Z}_p \cong H^n(X; \mathbb{Z}) \otimes \mathbb{Z}_p$.
::: {.proof}
$\operatorname{Hom}(F, \mathbb{Z}_p) \cong \operatorname{Hom}(F, \mathbb{Z}) \otimes \mathbb{Z}_p$ for free $F$, and $H^n(X; \mathbb{Z}) \cong \operatorname{Hom}(H_n(X), \mathbb{Z})$ (since $\operatorname{Ext}(H_{n-1}, \mathbb{Z}) = 0$ by freeness).
:::

<1>5. Hence $H^n(X; \mathbb{Z}_p) \cong H^n(X; \mathbb{Z}) \otimes \mathbb{Z}_p$ for each $n$.
::: {.proof}
<1>3 and <1>4.
:::

<1>6. This isomorphism is compatible with the cup product (it is induced by the natural map $\mathbb{Z} \to \mathbb{Z}_p$ on coefficients, which is a ring homomorphism), so it is an isomorphism of rings.
::: {.proof}
the cup product is natural with respect to coefficient maps, and the reduction map $\mathbb{Z} \to \mathbb{Z}_p$ induces a ring homomorphism $H^*(X; \mathbb{Z}) \to H^*(X; \mathbb{Z}_p)$.
:::

<1>7. Hence $H^*(X; \mathbb{Z}_p) \cong H^*(X; \mathbb{Z}) \otimes \mathbb{Z}_p$ as rings.
::: {.proof}
<1>5 and <1>6.
:::

<1>8. Q.E.D.
::: {.proof}
<1>7.
:::
:::
