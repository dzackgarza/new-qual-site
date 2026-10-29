---
schema: qual/card@1
id: P-6QME4
kind: problem
title: The proper nontrivial normal subgroups of $S_4$ are $A_4$ and $V_4\cong\ZZ_2^2$
classification:
  areas:
  - algebra
  topics:
  - Normal Subgroups
  - Permutations
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
- event: source-corrected
  by: claude-opus-5-5
  date: 2026-10-29
  note: 'Source read "Show that $S_4$ has two normal subgroups: $A_4, \ZZ_2^2$", which is false as written ($1$ and $S_4$ are also normal); the statement restricts to proper nontrivial normal subgroups and identifies the second one up to isomorphism.'
---

::: {.problem}
Show that $S_4$ has exactly two proper nontrivial normal subgroups: $A_4$ and a subgroup isomorphic to $\ZZ_2^2$.
:::

::: {.solution}
Let $V_4=\{e,(12)(34),(13)(24),(14)(23)\}$.

::: pf

::: {.pf-step #both-normal}
$V_4$ and $A_4$ are normal subgroups of $S_4$, and $V_4\cong\ZZ_2^2$.

::: pf-proof
$A_4$ is the kernel of the sign map. $V_4$ is closed under products, for example $(12)(34)\cdot(13)(24)=(14)(23)$, and it is the identity together with the whole conjugacy class of double transpositions, so it is normal. Its three nonidentity elements have order $2$, so $V_4\cong\ZZ_2^2$.
:::

:::

::: {.pf-step #class-sizes}
The conjugacy classes of $S_4$ have sizes $1,6,3,8,6$, for the cycle types $1^4$, $2\,1^2$, $2^2$, $3\,1$, $4$.

::: pf-proof
Conjugacy classes in $S_4$ are the cycle types. The counts are $1$, $\binom42=6$, $3$, $4\cdot2=8$ and $3!=6$.
:::

:::

::: pf-step
Every proper nontrivial normal subgroup of $S_4$ is $V_4$ or $A_4$.

::: pf-proof
A normal subgroup $N$ is a union of conjugacy classes that contains the class $\{e\}$, and its order divides $24$. For $1<\abs N<24$, the possible orders are $2,3,4,6,8,12$. By step [](#class-sizes){.pf-ref}, the only sums $1+\sum(\text{other class sizes})$ among these values are $1+3=4$ and $1+3+8=12$. The first union is $V_4$, and the second is the set of even permutations, $A_4$.
:::

:::

:::

:::
