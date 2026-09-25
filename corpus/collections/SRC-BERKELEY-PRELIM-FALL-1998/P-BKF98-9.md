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

<1>1. For each $i$, the Sylow subgroup $P_i$ is unique.

::: {.proof}
All Sylow $p_i$-subgroups are conjugate. Since $P_i$ is normal by
hypothesis, every conjugate of $P_i$ equals $P_i$. Thus there is only one.
:::

<1>2. If $i\neq j$, then
$$
P_i\cap P_j=\{1\}.
$$

::: {.proof}
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

<1>3. If $i\neq j$, then every element of $P_i$ commutes with every
element of $P_j$.

::: {.proof}
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
Step <1>2 therefore gives
$$
[x,y]=1.
$$
:::

<1>4. The product
$$
P_1P_2\cdots P_r
$$
is a subgroup of $G$ of order
$$
\prod_{i=1}^r\abs{P_i}
=
\abs G.
$$

::: {.proof}
Step <1>3 shows that the Sylow subgroups commute elementwise, so their
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

<1>5. One has
$$
G=P_1P_2\cdots P_r.
$$

::: {.proof}
Step <1>4 gives a subgroup of the finite group $G$ having the same order as
$G$, so it must equal $G$.
:::

<1>6. The group $G$ is abelian.

::: {.proof}
Each $P_i$ is abelian by hypothesis, and step <1>3 shows that elements from
different Sylow subgroups also commute. By step <1>5, every element of $G$
is a product of elements from the $P_i$. Therefore every pair of elements
of $G$ commutes.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 proves the claim.
:::
:::
