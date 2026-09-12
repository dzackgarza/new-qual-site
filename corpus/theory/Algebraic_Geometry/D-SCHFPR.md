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
For morphisms $X \to S$ and $Y \to S$, the **fibre product** $\fiberprod{X}{S}{Y}$ is a scheme over $S$ with projections to $X$ and $Y$, universal among schemes mapping compatibly to both:
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
The underlying set need not be the fibre product of sets.
$\fiberprod{\Spec \CC}{\Spec \RR}{\Spec \CC} \cong \Spec (\CC \tensor_\RR \CC) \cong \Spec (\CC \times \CC)$ has two points, whereas the set-theoretic fibre product has one.
Nilpotents can also appear: for $k=\FF_p(t)$ and $L=k(u)$ with $u^p=t$, $L\tensor_k L\cong L[\eps]/(\eps^p)$.
:::
