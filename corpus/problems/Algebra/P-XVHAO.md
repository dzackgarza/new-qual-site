---
schema: qual/card@1
id: P-XVHAO
kind: problem
title: $[A_4,A_4]\cong\ZZ_2^2$
classification:
  areas:
  - algebra
  topics:
  - Commutators
  - Permutations
relations: []
review: draft
---

::: {.problem}
Show that
\[
[A_4,A_4]\cong C_2\times C_2.
\]
:::

::: {.solution}
Let
\[
V_4=\{1,(12)(34),(13)(24),(14)(23)\}\trianglelefteq A_4.
\]
Since
\[
A_4/V_4\cong C_3
\]
is abelian, the commutator subgroup satisfies
\[
[A_4,A_4]\le V_4.
\]

It remains to show that the commutator subgroup is nontrivial. Let
\[
a=(123),\qquad b=(124).
\]
Then
\[
[a,b]=aba^{-1}b^{-1}=(12)(34).
\]
Thus
\[
(12)(34)\in[A_4,A_4].
\]
The commutator subgroup is normal in $A_4$, and the three nonidentity elements of $V_4$ are conjugate in $A_4$. Hence all three double transpositions lie in $[A_4,A_4]$.

Therefore
\[
[A_4,A_4]=V_4\cong C_2\times C_2.
\]
:::
