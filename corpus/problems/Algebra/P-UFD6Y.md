---
schema: qual/card@1
id: P-UFD6Y
kind: problem
title: The center of $S_3$ is trivial
classification:
  areas:
  - algebra
  topics:
  - Centralizers and Normalizers
  - Permutations
relations: []
review: draft
---

::: problem
Show that
\[
Z(S_3)=\{e\}.
\]
:::

::: solution
Let $z\in Z(S_3)$. If $z$ is a transposition, then it does not commute with a different transposition; for example,
\[
(12)(23)\ne(23)(12).
\]
So no transposition lies in the center.

If $z$ is a $3$-cycle, then it does not commute with a transposition. For instance,
\[
(123)(12)\ne(12)(123).
\]
Thus no $3$-cycle lies in the center.

The elements of $S_3$ are the identity, three transpositions, and two $3$-cycles. The only remaining possibility is the identity. Hence
\[
Z(S_3)=\{e\}.
\]
:::
