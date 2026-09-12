---
schema: qual/card@1
id: P-WOCSV
kind: problem
title: Classification of groups of order $4$, and which arise as Galois groups over
  $\mathbb{Q}$
classification:
  areas:
  - algebra
  topics:
  - Classification
  - Galois Theory
  - Abelian Groups
relations: []
review: draft
---

::: problem
Classify the groups of order $4$. Which of them occur as Galois groups over $\QQ$?
:::

::: solution
Let $G$ have order $4$. Every group of order $p^2$ is abelian, so $G$ is abelian. By the classification of finite abelian groups, there are exactly two possibilities:
\[
C_4,
\qquad
C_2\times C_2.
\]

Both occur as Galois groups over $\QQ$.

For $C_4$, take the cyclotomic extension
\[
\QQ(\zeta_5)/\QQ.
\]
Its Galois group is
\[
(\ZZ/5\ZZ)^\times\cong C_4.
\]

For $C_2\times C_2$, take the biquadratic extension
\[
\QQ(\sqrt2,\sqrt3)/\QQ.
\]
The independent sign changes of $\sqrt2$ and $\sqrt3$ give
\[
\operatorname{Gal}(\QQ(\sqrt2,\sqrt3)/\QQ)
\cong C_2\times C_2.
\]

Thus both isomorphism types of groups of order $4$ arise as Galois groups over $\QQ$.
:::
