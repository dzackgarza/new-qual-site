---
schema: qual/card@1
id: P-ZGEFJ
kind: problem
title: $IS$ is a submodule of $A$
classification:
  areas:
  - algebra
  topics:
  - Modules
  - Ideals
relations: []
review: draft
---

::: problem
Let $R$ be a ring, let $I\le R$ be a left ideal, let $A$ be a left $R$-module, and let $S\subseteq A$ be nonempty. Define
\[
IS=\left\{\sum_{i=1}^n r_i a_i:n\ge1,\ r_i\in I,\ a_i\in S\right\}.
\]
Show that $IS$ is a submodule of $A$.
:::

::: solution
Since $S$ is nonempty, choose $a\in S$. Then
\[
0=0\cdot a\in IS,
\]
so $IS$ is nonempty.

Let
\[
x=\sum_{i=1}^n r_i a_i,
\qquad
y=\sum_{j=1}^m s_j b_j
\]
be elements of $IS$. Concatenating the two sums gives
\[
x+y
=\sum_{i=1}^n r_i a_i+
\sum_{j=1}^m s_j b_j\in IS.
\]

If
\[
x=\sum_i r_i a_i,
\]
then, because $I$ is an additive subgroup,
\[
-x=\sum_i (-r_i)a_i\in IS.
\]
Hence $IS$ is an additive subgroup of $A$.

Finally, for $r\in R$,
\[
rx
=r\sum_i r_i a_i
=\sum_i (rr_i)a_i.
\]
Since $I$ is a left ideal,
\[
rr_i\in I.
\]
Therefore
\[
rx\in IS.
\]
Thus $IS$ is closed under the $R$-action and is a submodule of $A$.
:::
