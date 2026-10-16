---
schema: qual/card@1
id: P-D8RQW
kind: problem
title: Intermediate fields of $\QQ(2^{1/4},\zeta_8)$ and the subgroup lattice of $D_8$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Field Extensions
relations: []
review: draft
---

::: {.problem}
Compute all intermediate fields of $\QQ(2^{1/4},\zeta_8)$.
:::

::: {.solution}
Put $\alpha=2^{1/4}$. Since $\zeta_8=(1+i)/\sqrt2$,
\[
L=\QQ(\alpha,i)
\]
is the splitting field of $x^4-2$, with Galois group $D_8$.
The three quadratic intermediate fields are
\[
\QQ(i),\qquad \QQ(\sqrt2),\qquad \QQ(\sqrt{-2}).
\]
The five quartic intermediate fields are
\[
\QQ(\zeta_8),\quad
\QQ(\alpha),\quad
\QQ(i\alpha),\quad
\QQ((1+i)\alpha),\quad
\QQ((1-i)\alpha).
\]
Together with $\QQ$ and $L$, these exhaust the subgroup lattice of $D_8$.
:::