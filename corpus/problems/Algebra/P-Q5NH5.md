---
schema: qual/card@1
id: P-Q5NH5
kind: problem
title: Group rings
classification:
  areas:
  - algebra
  topics:
  - Group Rings
  - Representation Theory
  - Algebras
relations: []
review: draft
---

::: {.problem}
Define the group ring $R[G]$ and describe its basic structure and relation to representations.
:::

::: {.solution}
Let $R$ be a unital ring and $G$ a group. The **group ring** $R[G]$ consists of finite formal sums
\[
\sum_{g\in G} r_g g,
\qquad r_g\in R,
\]
with coefficientwise addition and multiplication determined by
\[
(rg)(sh)=(rs)(gh)
\]
and distributivity.

As a left $R$-module, $R[G]$ is free with basis $G$. If $R$ is commutative, then $R[G]$ is an $R$-algebra. It is commutative exactly when $R$ is commutative and $G$ is abelian.

There is an augmentation homomorphism
\[
\varepsilon:R[G]\to R,
\qquad
\sum r_g g\longmapsto \sum r_g,
\]
whose kernel is the augmentation ideal.

Most importantly, left $R[G]$-modules are exactly $R$-modules equipped with an $R$-linear action of $G$. In particular, if $k$ is a field, linear representations
\[
\rho:G\to GL(V)
\]
are equivalent to left $k[G]$-module structures on $V$.

When $G$ is finite and $\operatorname{char}k\nmid |G|$, Maschke's theorem says that $k[G]$ is semisimple. Over an algebraically closed field of characteristic not dividing $|G|$, Artin–Wedderburn therefore decomposes $k[G]$ as a product of matrix algebras indexed by irreducible representations.
:::
