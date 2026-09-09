---
schema: qual/card@1
id: P-VTSE7
kind: problem
title: Normal Sylow subgroups split a finite group as their direct product
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Direct Products
  - Normal Subgroups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against an independent reproduction of Hungerford II.5.8.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Show that if every Sylow $p$-subgroup of a finite group $G$ is normal for every prime $p$, then $G$ is the direct product of its Sylow subgroups.
:::

::: solution
Let
\[
|G|=p_1^{a_1}\cdots p_r^{a_r},
\]
and let $P_i$ be the Sylow $p_i$-subgroup. By hypothesis each $P_i$ is normal.

<1>1. If $i\ne j$, then $P_i\cap P_j=\{e\}$.
::: proof
The order of $P_i\cap P_j$ divides both $|P_i|=p_i^{a_i}$ and
$|P_j|=p_j^{a_j}$. Since $p_i\ne p_j$, these orders are coprime, so
$|P_i\cap P_j|=1$.
:::

<1>2. If $i\ne j$, then every element of $P_i$ commutes with every element of
$P_j$.
::: proof
Let $x\in P_i$ and $y\in P_j$. Because $P_i\trianglelefteq G$,
\[
[x,y]=xyx^{-1}y^{-1}\in P_i.
\]
Because $P_j\trianglelefteq G$, the same commutator lies in $P_j$. Hence
\[
[x,y]\in P_i\cap P_j=\{e\}
\]
by <1>1, so $xy=yx$.
:::

<1>3. The multiplication map
\[
\mu:P_1\times\cdots\times P_r\longrightarrow G,
\qquad
(x_1,\ldots,x_r)\longmapsto x_1\cdots x_r
\]
is a homomorphism.
::: proof
By <1>2, elements belonging to distinct factors commute. Therefore componentwise
multiplication in the direct product is carried by $\mu$ to multiplication in
$G$.
:::

<1>4. The homomorphism $\mu$ is injective.
::: proof
Suppose $x_1\cdots x_r=e$ with $x_i\in P_i$. Fix $i$. Then
\[
x_i=\left(\prod_{j\ne i}x_j\right)^{-1}.
\]
The left side has $p_i$-power order. The right side belongs to the product of
the other Sylow subgroups, whose order divides
\(\prod_{j\ne i}p_j^{a_j}\), which is coprime to $p_i$. Hence $x_i=e$.
Since this holds for every $i$, the kernel is trivial.
:::

<1>5. The homomorphism $\mu$ is surjective.
::: proof
Its domain has order
\[
\prod_{i=1}^r|P_i|
=\prod_{i=1}^rp_i^{a_i}
=|G|.
\]
By <1>4, $\mu$ is injective between finite groups of the same order, hence
surjective.
:::

<1>6. Therefore
\[
G\cong P_1\times\cdots\times P_r.
\]
::: proof
By <1>3--<1>5, $\mu$ is an isomorphism.
:::
:::
