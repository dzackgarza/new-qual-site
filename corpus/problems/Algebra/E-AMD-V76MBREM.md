---
schema: qual/card@1
id: E-AMD-V76MBREM
kind: problem
title: If $A$ is finite type over Noetherian $R$ and finite over $B$, then $B$ is
  finite type over $R$
classification:
  areas:
  - algebra
  topics:
  - Noetherian Rings
  - Algebras
  - Commutative Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.exercise}
Let $R$ be a Noetherian ring and $A,B$ algebras over $R$.
Suppose $A$ is finite type over $R$ and finite over B. Then $B$ is finite type over $R$.
:::

::: {.solution}
The rings are commutative, and $R\subseteq B\subseteq A$.
Write $A=R[x_1,\dots,x_n]$ and $A=\sum_{j=1}^m By_j$ with $y_1=1$.
Choose $b_{ij},c_{jkl}\in B$ with
$$x_i=\sum_{j=1}^m b_{ij}y_j,\qquad y_jy_k=\sum_{l=1}^m c_{jkl}y_l ,$$
and let $B_0=R[\{b_{ij}\}\cup\{c_{jkl}\}]\subseteq B$.

::: pf

::: {.pf-step #b0-noetherian}
$B_0$ is a Noetherian ring.

::: pf-proof
$B_0$ is a quotient of a polynomial ring in finitely many variables over the Noetherian ring $R$, so the Hilbert basis theorem applies.
:::

:::

::: {.pf-step #a-fin-gen-b0-module}
$A=\sum_{j=1}^m B_0y_j$; in particular $A$ is a finitely generated $B_0$-module.

::: pf-proof
Put $M=\sum_j B_0y_j$.
Since $y_1=1$, $B_0\subseteq M$, and the relations $y_jy_k=\sum_l c_{jkl}y_l$ with $c_{jkl}\in B_0$ show that $M$ is closed under multiplication.
So $M$ is an $R$-subalgebra of $A$, and it contains each $x_i=\sum_j b_{ij}y_j$.
Hence $A=R[x_1,\dots,x_n]\subseteq M\subseteq A$.
:::

:::

::: {.pf-step #b-fin-gen-b0-module}
$B$ is a finitely generated $B_0$-module.

::: pf-proof
By steps [](#b0-noetherian){.pf-ref} and [](#a-fin-gen-b0-module){.pf-ref}, $A$ is a finitely generated module over the Noetherian ring $B_0$, hence a Noetherian $B_0$-module.
Its $B_0$-submodule $B$ is therefore finitely generated.
:::

:::

::: pf-qed
If $B=\sum_{r=1}^pB_0z_r$ (step [](#b-fin-gen-b0-module){.pf-ref}), then $B=R[\{b_{ij}\},\{c_{jkl}\},z_1,\dots,z_p]$ is a finitely generated $R$-algebra.
:::

:::

:::
