---
schema: qual/card@1
id: P-6PRPK
kind: problem
title: A group of order $60$ with normal Sylow $3$-subgroup is solvable and has normal
  Sylow $5$-subgroup
classification:
  areas:
  - algebra
  topics:
  - Solvable Groups
  - Sylow Theory
  - Normal Subgroups
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: problem
Let $G$ be a group of order 60 whose Sylow 3-subgroup is normal.

a. Prove that $G$ is solvable.

b. Prove that the Sylow 5-subgroup is also normal.
:::

::: solution
Let $P$ be the normal Sylow $3$-subgroup of $G$, so $|P|=3$.

For (a), the quotient $G/P$ has order $20$. If $n_5$ denotes the number of Sylow $5$-subgroups of $G/P$, then
\[
n_5\equiv1\pmod5,
\qquad
n_5\mid4,
\]
so $n_5=1$. Hence $G/P$ has a normal subgroup $Q/P$ of order $5$, and
\[
1\triangleleft P\triangleleft Q\triangleleft G
\]
has successive quotients of orders $3$, $5$, and $4$. The first two are cyclic, and every group of order $4$ is abelian. Thus all successive quotients are abelian, so $G$ is solvable.

For (b), let $H/P$ be the unique Sylow $5$-subgroup of $G/P$. Then $H\triangleleft G$ and $|H|=15$. Inside $H$, the number of Sylow $5$-subgroups satisfies
\[
n_5(H)\equiv1\pmod5,
\qquad
n_5(H)\mid3,
\]
so $n_5(H)=1$. Let $S$ be this unique Sylow $5$-subgroup. It is characteristic in $H$ because it is uniquely determined as the Sylow $5$-subgroup, and $H\triangleleft G$; therefore $S\triangleleft G$. Hence the Sylow $5$-subgroup of $G$ is normal.
:::
