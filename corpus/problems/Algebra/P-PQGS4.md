---
schema: qual/card@1
id: P-PQGS4
kind: problem
title: $\rank(F_1\oplus F_2)=\rank F_1+\rank F_2$ for free modules with the invariant
  dimension property
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
$$\rank(F_1\oplus F_2)=\rank(F_1)+\rank(F_2).$$
:::

::: {.solution}
Let $\mathcal B_1$ and $\mathcal B_2$ be bases of $F_1$ and $F_2$, and let
$$\mathcal B=\{(v,0):v\in\mathcal B_1\}\cup\{(0,w):w\in\mathcal B_2\}\subseteq F_1\oplus F_2.$$

::: pf

::: {.pf-step #basis}
$\mathcal B$ is a basis of $F_1\oplus F_2$.

::: pf-proof
Let $(x,y)\in F_1\oplus F_2$. The element $x$ has a unique expansion $x=\sum_i r_iv_i$ with $v_i\in\mathcal B_1$, and $y$ a unique expansion $y=\sum_j s_jw_j$ with $w_j\in\mathcal B_2$. Then
$$(x,y)=\sum_i r_i(v_i,0)+\sum_j s_j(0,w_j),$$
and any expansion of $(x,y)$ in $\mathcal B$ gives, by comparing components, expansions of $x$ and $y$, so it is this one. Hence $\mathcal B$ spans and is linearly independent.
:::

:::

::: pf-step
$\rank(F_1\oplus F_2)=\rank(F_1)+\rank(F_2)$, as cardinals.

::: pf-proof
The two pieces of $\mathcal B$ are disjoint, since $\mathcal B_1$ and $\mathcal B_2$ consist of nonzero elements. By step [](#basis){.pf-ref} and the well-definedness of rank,
$$\rank(F_1\oplus F_2)=\abs{\mathcal B}=\abs{\mathcal B_1}+\abs{\mathcal B_2}=\rank(F_1)+\rank(F_2).$$
:::

:::

:::

:::
