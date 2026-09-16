---
schema: qual/card@1
id: FF-X6C7Z
kind: fact
title: Closed immersion criterion for morphisms of smooth projective varieties
prompts:
- Give a geometric application of Nakayama's lemma.
classification:
  areas:
  - algebra
  topics:
  - Nakayama's Lemma
  - Geometry
relations: []
review: draft
---

::: {.fact}
Let $k$ be an algebraically closed field and $f\colon X\to Y$ a morphism of smooth projective varieties over $k$.
Then $f$ is a closed immersion if and only if $f$ is injective on closed points and the differential $df_p\colon T_pX\to T_{f(p)}Y$ is injective for every closed point $p\in X$ [@Har10a].
:::

::: {.remark}
The application of Nakayama's lemma is in the local step: a local homomorphism $\mathcal O_{Y,f(p)}\to\mathcal O_{X,p}$ of Noetherian local rings that is an isomorphism on residue fields, surjective on cotangent spaces and makes $\mathcal O_{X,p}$ a finitely generated module is surjective [@Har10a].
:::
