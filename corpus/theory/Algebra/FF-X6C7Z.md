---
schema: qual/card@1
id: FF-X6C7Z
kind: fact
title: A projective morphism is an isomorphism iff its differential is injective
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
If $f\colon X\to Y$ is a projective morphism between quasiprojective varieties, then $f$ is an isomorphism if and only if $df_p$ is injective for all $p\in X$.
:::

::: {.remark}
Erratum: the statement is false as written.
The linear embedding $f\colon\PP^1\to\PP^2$, $[x:y]\mapsto[x:y:0]$, is projective and $df_p$ is injective for every $p\in\PP^1$, but $f$ is not surjective, so it is not an isomorphism.
The injectivity of $df_p$ must be combined with a hypothesis on $f$ itself, such as injectivity on points (giving a closed immersion) or bijectivity onto $Y$; the intended hypothesis is unrecovered.
:::
