---
schema: qual/card@1
id: E-AMD-XFC4PD2E
kind: problem
title: $S_4$ has two normal subgroups $A_4$ and $\ZZ_2^2$
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
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: {.exercise}
Show that $S_4$ has two normal subgroups: $A_4, \ZZ_2^2$.
:::


::: {.solution}
<1>1. The alternating group $A_4$ is normal in $S_4$.
::: {.proof}
The sign map
\[
\operatorname{sgn}:S_4\longrightarrow\{\pm1\}
\]
is a group homomorphism, and $A_4=\ker(\operatorname{sgn})$. Every kernel is normal, so $A_4\trianglelefteq S_4$.
:::

<1>2. The set
\[
V=\{1,(12)(34),(13)(24),(14)(23)\}
\]
is a subgroup isomorphic to $\ZZ_2^2$.
::: {.proof}
Each nonidentity element of $V$ has order $2$, and the product of any two distinct nonidentity elements is the third; for example,
\[
(12)(34)(13)(24)=(14)(23).
\]
Thus $V$ is closed under products and inverses, so $V\le S_4$. Since $V$ has order $4$ and every nonidentity element has order $2$, it is isomorphic to $\ZZ_2^2$.
:::

<1>3. The subgroup $V$ is normal in $S_4$.
::: {.proof}
For $\sigma\in S_4$ and a double transposition $(ab)(cd)$,
\[
\sigma(ab)(cd)\sigma^{-1}
=(\sigma(a)\,\sigma(b))(\sigma(c)\,\sigma(d)),
\]
which is again a double transposition. There are exactly three double transpositions in $S_4$, namely the three nonidentity elements of $V$. Hence conjugation by every $\sigma\in S_4$ preserves $V$, so $V\trianglelefteq S_4$.
:::

<1>4. Therefore $S_4$ has the two stated normal subgroups $A_4$ and $\ZZ_2^2$.
::: {.proof}
Combine <1>1--<1>3, identifying $V\cong\ZZ_2^2$.
:::
:::
