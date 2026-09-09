---
schema: qual/card@1
id: P-L7OQW
kind: problem
title: Normality of subgroups is not transitive
classification:
  areas:
  - algebra
  topics:
  - Normal Subgroups
  - Counterexamples
  - Subgroups
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
Give an example of subgroups
\[
H\trianglelefteq K\trianglelefteq G
\]
with $H$ not normal in $G$.
:::

::: {.solution}
Take
\[
G=A_4,
\qquad
K=V_4=\{e,(12)(34),(13)(24),(14)(23)\},
\]
and
\[
H=\langle(12)(34)\rangle.
\]

The subgroup $K$ is normal in $A_4$: it consists of the identity together with all three double transpositions, and conjugation preserves cycle type.

The subgroup $H$ has order $2$. Since $K\cong C_2\times C_2$ is abelian, every subgroup of $K$ is normal, so
\[
H\trianglelefteq K.
\]

But $H$ is not normal in $A_4$. For example,
\[
(123)(12)(34)(123)^{-1}=(23)(14),
\]
which is not in $H$.

Thus
\[
H\trianglelefteq K\trianglelefteq G
\]
does not imply $H\trianglelefteq G$.
:::
