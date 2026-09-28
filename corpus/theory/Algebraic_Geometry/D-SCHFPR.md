---
schema: qual/card@1
id: D-SCHFPR
kind: definition
title: The fibre product of schemes
classification:
  areas:
  - algebraic-geometry
  topics:
  - Fibre Products
  - Schemes
  - Base Change
relations:
- kind: uses
  target: D-AN662
review: draft
prompts:
- What is the fibre product of schemes?
- Why does the fibre product exist?
- How is a fibre product computed from affine pieces?
---

::: {.definition}
For morphisms $X \to S$ and $Y \to S$, the \dfn{fibre product} $\fiberprod{X}{S}{Y}$ is a scheme over $S$ with projections to $X$ and $Y$, universal among schemes mapping compatibly to both:
$$
\Hom_S(T, \fiberprod{X}{S}{Y}) \cong \Hom_S(T, X) \times \Hom_S(T, Y) .
$$
:::

::: {.theorem title="Existence"}
Fibre products exist in $\Sch$.
For affines the anti-equivalence turns the limit into a colimit of rings:
$$
\fiberprod{\Spec A}{\Spec R}{\Spec B} \cong \Spec (A \tensor_R B) .
$$
The general case is obtained by covering $X$, $Y$, $S$ by affines, building the affine pieces, and gluing.
:::

::: {.remark}
The underlying set of $\fiberprod{X}{S}{Y}$ is in general not the fibre product of the underlying sets.
$\fiberprod{\Spec \CC}{\Spec \RR}{\Spec \CC} \cong \Spec (\CC \tensor_\RR \CC) \cong \Spec (\CC \times \CC)$ has two points, while the fibre product of the underlying sets has one.
For $K = \FF_p(t)$ over $L = \FF_p(t^p)$, $\fiberprod{\Spec K}{\Spec L}{\Spec K} \cong \Spec K[x]/(x-t)^p$ has one point and a nonreduced structure sheaf.
:::
