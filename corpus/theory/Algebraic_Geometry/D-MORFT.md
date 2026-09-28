---
schema: qual/card@1
id: D-MORFT
kind: definition
title: Locally of finite type, finite type, and finite presentation
classification:
  areas:
  - algebraic-geometry
  topics:
  - Finite Type Morphisms
  - Finite Presentation
  - Morphisms
relations:
- kind: related-to
  target: D-MORAFF
review: draft
prompts:
- What is a morphism locally of finite type?
- What is a finite type morphism?
- What is a finitely presented morphism, and when does it differ from finite type?
---

::: {.definition title="Finite type"}
$f : X \to Y$ is \dfn{locally of finite type} if $Y$ has an affine cover by $\Spec B_i$ such that $f^{-1}(\Spec B_i)$ has an affine cover by $\Spec A_{ij}$ with each $A_{ij}$ a finitely generated $B_i$-algebra.
It is \dfn{of finite type} if in addition each $f^{-1}(\Spec B_i)$ is covered by finitely many of the $\Spec A_{ij}$, that is, locally of finite type and quasicompact.
:::

::: {.definition title="Finite presentation"}
$f$ is \dfn{locally of finite presentation} if each $B_i \to A_{ij}$ is of finite presentation: $B_i[x_1, \dots, x_n] \surjects A_{ij}$ with finitely generated kernel.
It is \dfn{of finite presentation} if it is also quasicompact and quasi-separated.
:::

::: {.remark}
Finite type is a hypothesis of the valuative criterion of properness and part of the definition of a proper morphism.
Over a locally Noetherian base $Y$, locally of finite type and locally of finite presentation coincide, because every ideal of $B[x_1, \dots, x_n]$ is finitely generated for $B$ Noetherian; for $Y$ Noetherian, finite type and finite presentation coincide.
Over the non-Noetherian ring $B=k[x_1,x_2,\ldots]$, the quotient $B\to B/(x_1,x_2,\ldots)\cong k$ is of finite type and not of finite presentation.
Finite presentation is the finiteness condition in the definition of smooth and étale morphisms and in limit arguments.
:::
