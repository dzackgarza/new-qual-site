---
schema: qual/card@1
id: P-3OUVI
kind: problem
title: Isomorphic subgroups need not have isomorphic quotients
classification:
  areas:
  - algebra
  topics:
  - Subgroups
  - Normal Subgroups
  - Counterexamples
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
- Let $H, K \leq G$ be subgroups with $H\cong K$.
  Is it true that $G/H \cong G/K$?

  > Hint: consider a group with distinct subgroups of order 2 whose quotients have order 4.
:::


::: {.solution}
No.

<1>1. Let
\[
G=C_4\oplus C_2,
\]
and write elements additively. Define
\[
H=\langle(2,0)angle,
\qquad
K=\langle(0,1)angle.
\]
Then $H\cong K\cong C_2$.
::: {.proof}
Both displayed generators have order $2$. Since $G$ is abelian, both subgroups are normal, so both quotients are defined.
:::

<1>2. The quotient $G/H$ is isomorphic to $C_2\oplus C_2$.
::: {.proof}
Quotienting the $C_4$ factor by its subgroup of order $2$ gives $C_2$, while the second factor survives unchanged:
\[
G/H\cong (C_4/\langle2angle)\oplus C_2\cong C_2\oplus C_2.
\]
:::

<1>3. The quotient $G/K$ is isomorphic to $C_4$.
::: {.proof}
The subgroup $K$ is exactly the second direct factor, so
\[
G/K\cong C_4.
\]
:::

<1>4. Hence $G/H
ot\cong G/K$.
::: {.proof}
The group $C_4$ contains an element of order $4$, whereas every nonzero element of $C_2\oplus C_2$ has order $2$. Thus the quotients are not isomorphic even though $H\cong K$.
:::
:::
