---
schema: qual/card@1
id: T-D8DMU
kind: theorem
title: Ext of a locally free sheaf is cohomology of the tensor twist
slogan: 'For $L$ locally free of finite rank, $\Ext^i(L,\mcf)\cong H^i(X,\mcf\tensor L^\vee)$.'
classification:
  areas:
  - algebraic-geometry
  topics:
  - Ext
  - Coherent Sheaves
  - Sheaf Cohomology
relations:
- kind: uses
  target: D-DEFEXT
- kind: uses
  target: D-COHDER
review: draft
prompts:
- Express $\Ext^i$ of a locally free sheaf as a cohomology group.
- Why does local freeness move the tensor product to the other variable?
---

::: {.theorem}
Let $X$ be a ringed space, let $\mcl$ be a locally free $\OO_X$-module of finite rank with dual $\dualof{\mcl}=\sheafhom_{\OO_X}(\mcl,\OO_X)$, and let $\mcf$ be an $\OO_X$-module.
Then for every $i\ge0$,
$$
\Ext^i(\mcl,\mcf)\cong H^i(X,\mcf\tensor_{\OO_X}\dualof{\mcl}),
$$
and in particular
$$
\Ext^1(\mcl,\mcf)\cong H^1(X,\mcf\tensor_{\OO_X}\dualof{\mcl}).
$$
[@Har77, Proposition III.6.7 and Proposition III.6.3]
:::

::: {.remark}
The two propositions compose to give the statement: Proposition III.6.7 applied with the first variable $\OO_X$ reads $\Ext^i(\OO_X\tensor\mcl,\mcg)\cong\Ext^i(\OO_X,\dualof{\mcl}\tensor\mcg)$, and Proposition III.6.3 identifies $\Ext^i(\OO_X,-)$ with $H^i(X,-)$.
The two propositions give the statement together: Proposition III.6.7 applied with the first variable $\OO_X$ reads $\Ext^i(\OO_X\tensor\mcl,\mcg)\cong\Ext^i(\OO_X,\dualof{\mcl}\tensor\mcg)$, and Proposition III.6.3 identifies $\Ext^i(\OO_X,-)$ with $H^i(X,-)$.
:::
