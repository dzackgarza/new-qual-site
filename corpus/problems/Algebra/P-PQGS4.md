---
schema: qual/card@1
id: P-PQGS4
kind: problem
title: $\operatorname{rank}(F_1\oplus F_2)=\operatorname{rank} F_1+\operatorname{rank}
  F_2$ for free modules with the invariant dimension property
classification:
  areas:
  - algebra
  topics:
  - Free Modules
  - Bases
  - Direct Products
relations: []
review: draft
---

::: {.problem}
Let $F_1,F_2$ be free modules over a ring for which free-module rank is well-defined. Prove
\[
\operatorname{rank}(F_1\oplus F_2)
=
\operatorname{rank}(F_1)+\operatorname{rank}(F_2).
\]
:::

::: {.solution}
Let $\mathcal B_1$ and $\mathcal B_2$ be bases of $F_1$ and $F_2$. Define
\[
\mathcal B
=
\{(v,0):v\in\mathcal B_1\}
\cup
\{(0,w):w\in\mathcal B_2\}.
\]

Every $(x,y)\in F_1\oplus F_2$ can be written uniquely as
\[
(x,y)
=
\sum_i r_i(v_i,0)+\sum_j s_j(0,w_j),
\]
using the unique basis expansions of $x$ and $y$. Thus $\mathcal B$ spans and is linearly independent, hence is a basis.

Therefore
\[
\operatorname{rank}(F_1\oplus F_2)
=|\mathcal B|
=|\mathcal B_1|+|\mathcal B_2|
=\operatorname{rank}(F_1)+\operatorname{rank}(F_2).
\]
For finite ranks this is ordinary integer addition; in general it is cardinal addition.
:::
