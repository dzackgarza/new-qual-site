---
schema: qual/card@1
id: P-DB72D
kind: problem
title: Abelian groups of order 200
classification:
  areas:
  - algebra
  topics:
  - Classification
  - Abelian Groups
  - Structure Theorem
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
- event: solution-written
  by: Claude Opus 5.5
  date: 2026-10-29
  note: Converted the prose solution to a STYLE-08 structured proof.
---

::: {.problem}
Determine the number of abelian groups of order $200$ up to isomorphism, and list all isomorphism classes in invariant factor and elementary divisor forms.
:::

::: {.solution}

::: pf

::: {.pf-step #count}
There are $\boxed{6}$ abelian groups of order $200$ up to isomorphism.

::: pf-proof
Since $200=2^3 5^2$, a finite abelian group of order $200$ is the product of its Sylow $2$-subgroup, of order $2^3$, and its Sylow $5$-subgroup, of order $5^2$.
Abelian groups of order $p^k$ correspond to partitions of $k$.
The partitions of $3$ are $3$, $2+1$, $1+1+1$, and the partitions of $2$ are $2$, $1+1$, so there are $p(3)p(2)=3\cdot2=6$ isomorphism classes.
:::

:::

::: {.pf-step #elementary}
The elementary-divisor forms are
$$
\boxed{\begin{aligned}
&\ZZ_8\times\ZZ_{25}, &&\ZZ_8\times\ZZ_5\times\ZZ_5, &&\ZZ_4\times\ZZ_2\times\ZZ_{25},\\
&\ZZ_4\times\ZZ_2\times\ZZ_5\times\ZZ_5, &&\ZZ_2^3\times\ZZ_{25}, &&\ZZ_2^3\times\ZZ_5^2.
\end{aligned}}
$$

::: pf-proof
These are the products of one group from each partition list of step [](#count){.pf-ref}.
:::

:::

::: pf-step
The corresponding invariant-factor forms, in the same order, are
$$
\boxed{\begin{aligned}
&\ZZ_{200}, &&\ZZ_5\times\ZZ_{40}, &&\ZZ_2\times\ZZ_{100},\\
&\ZZ_{10}\times\ZZ_{20}, &&\ZZ_2\times\ZZ_2\times\ZZ_{50}, &&\ZZ_2\times\ZZ_{10}\times\ZZ_{10}.
\end{aligned}}
$$

::: pf-proof
By the Chinese remainder theorem, combine the largest $2$-primary and largest $5$-primary factors of each group in step [](#elementary){.pf-ref} into the last invariant factor, then the next largest, and so on.
In each resulting decomposition, each factor divides the next.
:::

:::

:::

:::
