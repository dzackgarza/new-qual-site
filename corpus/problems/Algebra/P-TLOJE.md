---
schema: qual/card@1
id: P-TLOJE
kind: problem
title: Abelian groups are nilpotent
classification:
  areas:
  - algebra
  topics:
  - Abelian Groups
  - Nilpotent Groups
relations: []
review: draft
---

::: problem
Show that every abelian group is nilpotent.
:::

::: solution
Let $G$ be abelian. Then
\[
[G,G]=1.
\]
The lower central series is
\[
\gamma_1(G)=G,
\qquad
\gamma_{i+1}(G)=[\gamma_i(G),G].
\]
Therefore
\[
\gamma_2(G)=[G,G]=1.
\]
So the lower central series reaches the identity after one nontrivial step. Hence $G$ is nilpotent of class at most $1$.

Equivalently, since $G$ is abelian,
\[
Z(G)=G,
\]
so the upper central series reaches all of $G$ immediately.
:::
