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
- How do you compute a fibre product in practice?
---

::: {.definition}
For morphisms $X \to S$ and $Y \to S$, the \dfn{fibre product} $\fiberprod{X}{S}{Y}$ is a scheme over $S$ with projections to $X$ and $Y$, universal among schemes mapping compatibly to both:
\[
\Hom_S(T, \fiberprod{X}{S}{Y}) \cong \Hom_S(T, X) \times \Hom_S(T, Y) .
\]
:::

::: {.theorem title="Existence"}
Fibre products exist in $\Sch$.
For affines the anti-equivalence turns the limit into a colimit of rings:
\[
\fiberprod{\Spec A}{\Spec R}{\Spec B} \cong \Spec (A \tensor_R B) .
\]
The general case is obtained by covering $X$, $Y$, $S$ by affines, building the affine pieces, and gluing.
:::

::: {.remark}
For affine schemes, every fibre-product computation reduces to the tensor-product formula above; the general construction is obtained by gluing these affine pieces.

The underlying set is *not* in general the fibre product of the underlying sets.
$\fiberprod{\Spec \CC}{\Spec \RR}{\Spec \CC} \cong \Spec (\CC \tensor_\RR \CC) \cong \Spec (\CC \times \CC)$ is two points over a one-point set product, and for $K = \FF_p(t)$ over $L = \FF_p(t^p)$, $\fiberprod{\Spec K}{\Spec L}{\Spec K} \cong \Spec K[x]/(x-t)^p$ is one point but gains nilpotents.
The Frobenius of $\FF_p$ itself is the identity, so base change along it changes nothing.
The universal property identifies the fibre product by the functor it represents.
:::
