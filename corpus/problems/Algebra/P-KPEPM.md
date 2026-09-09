---
schema: qual/card@1
id: P-KPEPM
kind: problem
title: Pairs $(n,p)$ for which $\SL_n(\FF_p)$ is solvable
classification:
  areas:
  - algebra
  topics:
  - Solvable Groups
  - Matrix Groups
  - Finite Fields
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
Let $p$ be prime and $n\ge1$. Determine all pairs $(n,p)$ for which
\[
\SL_n(\FF_p)
\]
is solvable.
:::

::: {.solution}
The solvable cases are
\[
n=1\quad\text{for every prime }p,
\]
and
\[
(n,p)=(2,2),(2,3).
\]

<1>1. If $n=1$, then $\SL_1(\FF_p)=1$, so it is solvable.

<1>2. The groups $\SL_2(\FF_2)$ and $\SL_2(\FF_3)$ are solvable.
::: {.proof}
We have
\[
\SL_2(\FF_2)\cong S_3,
\]
which is solvable.

For $p=3$, the center of $\SL_2(\FF_3)$ is $\{\pm I\}$ and
\[
\PSL_2(\FF_3)\cong A_4.
\]
Thus $\SL_2(\FF_3)$ is an extension of the solvable group $A_4$ by the abelian group $C_2$, hence is solvable.
:::

<1>3. All other cases with $n\ge2$ are nonsolvable.
::: {.proof}
The classical simplicity theorem for projective special linear groups says that
\[
\PSL_n(\FF_p)
\]
is nonabelian simple for $n\ge2$, except for
\[
(n,p)=(2,2),(2,3).
\]
Since $\PSL_n(\FF_p)$ is a quotient of $\SL_n(\FF_p)$, solvability of $\SL_n(\FF_p)$ would force solvability of $\PSL_n(\FF_p)$. A nonabelian simple group is not solvable, so no other pair occurs.
:::
:::
