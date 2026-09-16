---
schema: qual/card@1
id: T-GAGA
kind: theorem
title: GAGA
classification:
  areas:
  - algebraic-geometry
  topics:
  - GAGA
  - Analytification
  - Coherent Sheaves
relations:
- kind: related-to
  target: T-CARTSERRE
review: draft
prompts:
- What is GAGA?
---

::: {.theorem title="Serre's GAGA"}
Let $X$ be a projective scheme over $\CC$ and $X^{an}$ its associated complex analytic space, with the morphism of ringed spaces $h \colon X^{an} \to X$.

1. For every coherent sheaf $\mathcal{F}$ on $X$, the natural maps $H^i(X, \mathcal{F}) \to H^i(X^{an}, \mathcal{F}^{an})$ are isomorphisms, where $\mathcal{F}^{an} = h^* \mathcal{F}$.
2. The functor $\mathcal{F} \mapsto \mathcal{F}^{an}$ is an equivalence from coherent $\OO_X$-modules to coherent analytic sheaves on $X^{an}$.
:::

::: {.corollary title="Chow's theorem"}
A closed analytic subspace of $\PP^n(\CC)$ is algebraic, and a holomorphic map between projective varieties is a morphism.
:::

::: {.example}
Holomorphic line bundles on a projective variety are algebraic, so $\Pic(X) \cong H^1(X^{an}, \OO^*_{X^{an}})$.
Global meromorphic functions on a smooth projective variety are rational functions.
Projectivity cannot be dropped: on $X = \AA^1_\CC$, $H^0(X, \OO_X) = \CC[z]$ while $H^0(X^{an}, \OO_{X^{an}})$ is the ring of entire functions, and $\exp \colon \CC \to \CC^*$ is holomorphic but not a morphism $\AA^1 \to \AA^1 \setminus \{0\}$.
:::
