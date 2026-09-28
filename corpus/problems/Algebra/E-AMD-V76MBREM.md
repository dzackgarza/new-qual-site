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

<1>1. $B_0$ is a Noetherian ring.

::: {.proof}
$B_0$ is a quotient of a polynomial ring in finitely many variables over the Noetherian ring $R$, so the Hilbert basis theorem applies.
:::

<1>2. $A=\sum_{j=1}^m B_0y_j$; in particular $A$ is a finitely generated $B_0$-module.

::: {.proof}
Put $M=\sum_j B_0y_j$.
Since $y_1=1$, $B_0\subseteq M$, and the relations $y_jy_k=\sum_l c_{jkl}y_l$ with $c_{jkl}\in B_0$ show that $M$ is closed under multiplication.
So $M$ is an $R$-subalgebra of $A$, and it contains each $x_i=\sum_j b_{ij}y_j$.
Hence $A=R[x_1,\dots,x_n]\subseteq M\subseteq A$.
:::

<1>3. $B$ is a finitely generated $B_0$-module.

::: {.proof}
By steps <1>1 and <1>2, $A$ is a finitely generated module over the Noetherian ring $B_0$, hence a Noetherian $B_0$-module.
Its $B_0$-submodule $B$ is therefore finitely generated.
:::

<1>4. Q.E.D.

::: {.proof}
If $B=\sum_{r=1}^pB_0z_r$ (step <1>3), then $B=R[\{b_{ij}\},\{c_{jkl}\},z_1,\dots,z_p]$ is a finitely generated $R$-algebra.
:::
:::
