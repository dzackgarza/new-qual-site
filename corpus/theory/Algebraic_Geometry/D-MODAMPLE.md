---
schema: qual/card@1
id: D-MODAMPLE
kind: definition
title: Ample and very ample invertible sheaves
classification:
  areas:
  - algebraic-geometry
  topics:
  - Ampleness
  - Line Bundles
  - Projective Morphisms
relations:
- kind: uses
  target: D-MODGG
- kind: uses
  target: D-MODPULL
review: draft
prompts:
- Define ample and very ample.
- What is the relation between the two?
- Why is a proper scheme with a very ample sheaf projective?
---

::: {.definition title="Very ample"}
Let $f:X\to Y$ be a morphism of schemes and let $\mcl$ be an invertible sheaf on $X$.
It is \dfn{very ample} over $Y$ if there is a $Y$-immersion $\iota:X\to\PP_Y^n$, for some finite $n$, with $\iota^*\OO(1)\cong\mcl$ [@Har10a, Chapter II, §7].
:::

::: {.definition title="Ample"}
Let $X$ be a noetherian scheme and let $\mcl$ be an invertible sheaf on $X$.
It is \dfn{ample} if for every coherent $\mcf$ there is an integer $N_0$ such that $\mcf\tensor\mcl^{\otimes n}$ is [[D-MODGG|globally generated]] for every $n\ge N_0$ [@Har10a, Chapter II, §7].
:::

::: {.theorem}
Let $X$ be of finite type over a noetherian ring $A$ and let $\mcl$ be invertible.
Then $\mcl$ is ample if and only if $\mcl^{\otimes m}$ is very ample over $\Spec A$ for some $m>0$ [@Har10a, Theorem II.7.6].
:::

::: {.remark}
If $f:X\to Y$ is proper and $\mcl$ is very ample over $Y$, its immersion into $\PP_Y^n$ is proper, hence a closed immersion.
Thus $f$ is projective in the sense of admitting a closed immersion into some $\PP_Y^n$.
Conversely, such a closed immersion gives a very ample sheaf by pulling back $\OO(1)$ [@Har10a, Chapter II, §§4 and 7].
:::

::: {.proposition title="Ampleness on a complete curve"}
Let $X$ be a complete nonsingular curve over an algebraically closed field, and let $\mcl$ be an invertible sheaf.
Then $\mcl$ is ample if and only if $\deg\mcl>0$ [@Har10a, Corollary IV.3.3].
The completeness hypothesis is part of this degree criterion; the general noetherian definition is the global-generation condition.
:::
