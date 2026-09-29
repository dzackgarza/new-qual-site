---
schema: qual/card@1
id: P-BKF98-9
kind: problem
title: A finite group whose Sylow subgroups are all normal and abelian is abelian
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-25
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-25
  note: >-
    Distinct normal Sylow subgroups have trivial intersection, so their
    cross-commutators vanish. Their product has full group order, reducing G
    to a product of commuting abelian Sylow factors.
---

::: {.problem}
Suppose $G$ is a finite group such that every Sylow subgroup of $G$ is normal and abelian. Show that $G$ is abelian.
:::

::: {.solution}

Write
$$
\abs G
=
\prod_{i=1}^r p_i^{a_i}
$$
with distinct primes $p_i$, and let $P_i$ be a Sylow $p_i$-subgroup.

::: pf

::: {.pf-step #sylow-unique}
For each $i$, the Sylow subgroup $P_i$ is unique.

::: pf-proof
All Sylow $p_i$-subgroups are conjugate. Since $P_i$ is normal by
hypothesis, every conjugate of $P_i$ equals $P_i$. Thus there is only one.
:::

:::

::: {.pf-step #sylow-trivial-intersection}
If $i\neq j$, then
$$
P_i\cap P_j=\{1\}.
$$

::: pf-proof
The order of $P_i\cap P_j$ divides both
$$
\abs{P_i}=p_i^{a_i}
$$
and
$$
\abs{P_j}=p_j^{a_j}.
$$
These two orders are coprime, so the intersection has order $1$.
:::

:::

::: {.pf-step #sylow-elements-commute}
If $i\neq j$, then every element of $P_i$ commutes with every
element of $P_j$.

::: pf-proof
Take
$$
x\in P_i,
\qquad
y\in P_j.
$$
Since $P_i$ is normal,
$$
yx^{-1}y^{-1}\in P_i,
$$
so
$$
[x,y]
=
x(yx^{-1}y^{-1})
\in P_i.
$$
Since $P_j$ is normal,
$$
xyx^{-1}\in P_j,
$$
so
$$
[x,y]
=
(xyx^{-1})y^{-1}
\in P_j.
$$
Step [](#sylow-trivial-intersection){.pf-ref} therefore gives
$$
[x,y]=1.
$$
:::

:::

::: {.pf-step #product-full-order}
The product
$$
P_1P_2\cdots P_r
$$
is a subgroup of $G$ of order
$$
\prod_{i=1}^r\abs{P_i}
=
\abs G.
$$

::: pf-proof
Step [](#sylow-elements-commute){.pf-ref} shows that the Sylow subgroups commute elementwise, so their
setwise product is a subgroup.

Because their orders are pairwise coprime and their pairwise intersections
are trivial, multiplication gives an injective homomorphism
$$
P_1\times\cdots\times P_r
\longrightarrow
G.
$$
Its image is the product subgroup. Hence that subgroup has order
$$
\prod_{i=1}^r p_i^{a_i}
=
\abs G.
$$
:::

:::

::: {.pf-step #G-equals-product}
One has
$$
G=P_1P_2\cdots P_r.
$$

::: pf-proof
Step [](#product-full-order){.pf-ref} gives a subgroup of the finite group $G$ having the same order as
$G$, so it must equal $G$.
:::

:::

::: {.pf-step #G-abelian}
The group $G$ is abelian.

::: pf-proof
Each $P_i$ is abelian by hypothesis, and step [](#sylow-elements-commute){.pf-ref} shows that elements from
different Sylow subgroups also commute. By step [](#G-equals-product){.pf-ref}, every element of $G$
is a product of elements from the $P_i$. Therefore every pair of elements
of $G$ commutes.
:::

:::

::: pf-qed
Step [](#G-abelian){.pf-ref} proves the claim.
:::

:::

:::
