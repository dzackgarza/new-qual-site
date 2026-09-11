---
schema: qual/card@1
id: P-AGXHWSPECZTERM
kind: problem
title: $\Spec \ZZ$ is terminal in the category of schemes
classification:
  areas:
  - algebraic-geometry
  topics:
  - Affine Schemes
  - Terminal Objects
  - Adjunctions
relations: []
review: draft
---

::: problem
Describe $\Spec \ZZ$ and show it is terminal in $\Sch$, i.e. each $X\in \Sch$ admits a unique morphism $X\to \Spec \ZZ$.
:::

::: remark
Strategy: use the adjunction inducing an equivalence
\[
\adjunction{\Gamma({-})}{\Spec({-})}{\Sch^{\op}}{\CRing}
\]
so that
\[
\Mor_{\Sch}(X, \Spec(R)) \cong \Mor_{\CRing}(R, \Gamma(X;\OO_X))
.\]
:::
