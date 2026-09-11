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
$f : X \to Y$ is **locally of finite type** if $Y$ has an affine cover by $\Spec B_i$ such that $f^{-1}(\Spec B_i)$ has an affine cover by $\Spec A_{ij}$ with each $A_{ij}$ a finitely generated $B_i$-algebra.
It is **of finite type** if in addition each $f^{-1}(\Spec B_i)$ is covered by finitely many of the $\Spec A_{ij}$, that is, locally of finite type and quasicompact.
:::

::: {.definition title="Finite presentation"}
$f$ is **locally of finite presentation** if each $B_i \to A_{ij}$ is of finite presentation: $B_i[x_1, \dots, x_n] \surjects A_{ij}$ with finitely generated kernel.
It is **of finite presentation** if it is also quasicompact and quasi-separated.
:::

::: {.remark}
Finite type is the condition that makes a scheme a geometric object of finite size, and it is a hypothesis in the valuative criteria and in properness.
Finite presentation is finite type plus a condition on relations, and over a Noetherian base the two coincide, because every ideal of $B[x_1, \dots, x_n]$ is finitely generated.
So the distinction is invisible on the exam and is exactly why "locally of finite presentation" appears in the definition of smooth: it is the condition under which the cotangent complex behaves and limit arguments work over an arbitrary base.
:::
