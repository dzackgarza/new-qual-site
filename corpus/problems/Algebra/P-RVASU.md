---
schema: qual/card@1
id: P-RVASU
kind: problem
title: Subgroups of $F_2$
classification:
  areas:
  - algebra
  topics:
  - Free Groups
  - Subgroups
  - Normal Subgroups
relations: []
review: draft
---

::: problem
Describe subgroups of the free group $F_2=\langle a,b\rangle$. Give examples having ranks $3$, $4$, and countably infinite rank. For rank $4$, give both normal and nonnormal examples.
:::

::: solution
By the Nielsen--Schreier theorem, every subgroup of a free group is free. If $H\le F_r$ has finite index $d$, the Schreier index formula gives
\[
\operatorname{rank}(H)=1+d(r-1).
\]
For $F_2$, this becomes
\[
\operatorname{rank}(H)=d+1.
\]

<1>1. Rank $3$:
Let
\[
H_2=\ker(F_2\twoheadrightarrow C_2),\qquad a\mapsto 1,\quad b\mapsto0.
\]
Then $[F_2:H_2]=2$, so $H_2$ is free of rank $3$. It is normal because it is a kernel.

<1>2. Rank $4$, normal:
Let
\[
H_3=\ker(F_2\twoheadrightarrow C_3),\qquad a\mapsto1,\quad b\mapsto0.
\]
Then $[F_2:H_3]=3$, so $H_3$ is free of rank $4$, and it is normal.

<1>3. Rank $4$, nonnormal:
Map $F_2$ onto $S_3$ by
\[
a\mapsto(12),\qquad b\mapsto(123).
\]
Let $K$ be the inverse image of $\langle(12)\rangle$. Since that subgroup has index $3$ in $S_3$, $K$ has index $3$ in $F_2$, hence rank $4$. But $\langle(12)\rangle$ is not normal in $S_3$, so $K$ is not normal in $F_2$.

<1>4. Countably infinite rank:
The commutator subgroup
\[
[F_2,F_2]=\ker(F_2\twoheadrightarrow\ZZ^2)
\]
is normal and has infinite index. It is a nontrivial subgroup of the countable group $F_2$, hence is at most countably generated; by Nielsen--Schreier it is free. It cannot have finite rank: a nontrivial finitely generated normal subgroup of a finitely generated free group has finite index. Therefore $[F_2,F_2]$ is free of countably infinite rank.
:::
