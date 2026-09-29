---
schema: qual/card@1
id: E-AMD-JFCWSOUA
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
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Used the abelian quotient and one explicit commutator to identify the derived subgroup.
---

::: {.exercise}
Show that $[A_4,A_4]\cong\mathbb Z_2^2$.
:::

::: {.solution}
Let
\[
V=\{1,(12)(34),(13)(24),(14)(23)\}\cong C_2\times C_2.
\]

::: pf

::: {.pf-step #derived-subgroup-le-v}
We have $[A_4,A_4]\le V$.

::: pf-proof
The subgroup $V$ is normal in $A_4$, and
\[
A_4/V\cong C_3
\]
is abelian. Therefore the commutator subgroup is contained in $V$.
:::

:::

::: {.pf-step #v-le-derived-subgroup}
We have $V\le[A_4,A_4]$.

::: pf-proof
With $x=(123)$ and $y=(124)$,
\[
[x,y]=xyx^{-1}y^{-1}=(12)(34).
\]
The commutator subgroup is normal in $A_4$, so it contains all $A_4$-conjugates of $(12)(34)$, namely the three nonidentity elements of $V$. Hence it contains $V$.
:::

:::

::: pf-qed
By steps [](#derived-subgroup-le-v){.pf-ref} and [](#v-le-derived-subgroup){.pf-ref}, thus
\[
[A_4,A_4]=V\cong\mathbb Z_2^2.
\]
:::

:::

:::
