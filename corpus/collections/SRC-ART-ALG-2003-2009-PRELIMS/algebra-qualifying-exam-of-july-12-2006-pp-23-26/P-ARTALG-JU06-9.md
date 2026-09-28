---
schema: qual/card@1
id: P-ARTALG-JU06-9
kind: problem
title: Structure theorem for finitely generated abelian groups
classification:
  areas:
  - algebra
  topics:
  - Group Theory
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared both parts and the factorization of 300 with July 2006 Rings and modules 9 in the retained extraction."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked all partitions of the primary exponents, the orders of all four products, and their distinct group exponents."
---

::: {.problem}
(a) State the structure theorem for finitely generated Abelian groups.

(b) Up to isomorphism, what are the Abelian groups of order $300 = 2^2 \cdot 3 \cdot 5^2$?
:::

::: {.solution}
Write $C_m=\mathbb Z/m\mathbb Z$.

<1>1. The elementary-divisor form of the structure theorem is as follows.

Every finitely generated abelian group $A$ has a decomposition
$$
A\cong\mathbb Z^r\oplus
\bigoplus_{p\ \mathrm{prime}}
\bigoplus_{j=1}^{t_p} C_{p^{e_{p,j}}},
$$
where $r$ and the $t_p$ are nonnegative integers,
only finitely many $t_p$ are nonzero, and
$1\leq e_{p,1}\leq\cdots\leq e_{p,t_p}$.
The integer $r$ and the lists of exponents for each prime are
uniquely determined by $A$. This is the structure theorem for
finitely generated abelian groups [@DF04]. Empty sums are allowed.

<1>2. The four groups of order $300$ are the following.

| Group | Exponent |
| --- | --- |
| $C_4\oplus C_3\oplus C_{25}$ | $300$ |
| $C_2\oplus C_2\oplus C_3\oplus C_{25}$ | $150$ |
| $C_4\oplus C_3\oplus C_5\oplus C_5$ | $60$ |
| $C_2\oplus C_2\oplus C_3\oplus C_5\oplus C_5$ | $30$ |

::: {.proof}
Finiteness forces $r=0$ in step <1>1. For each prime $p$, the
sum $\sum_j e_{p,j}$ is the exponent of $p$ in the group order.
For $p=2$ that sum is $2$, with exactly the partitions $(2)$
and $(1,1)$. For $p=3$ it is $1$, with only the partition $(1)$.
For $p=5$ it is $2$, again with the partitions $(2)$ and $(1,1)$.
No other prime occurs. The two independent choices for the
$2$-part and the $5$-part give precisely the four displayed groups.
Each has order $4\cdot3\cdot25=300$.

The exponent of a finite abelian group is the least positive integer
that annihilates every element. For a direct sum of cyclic groups,
it is the least common multiple of their orders: an integer kills
the whole group exactly when it kills a generator in every summand.
This gives the four exponents displayed in the table. They are
distinct and invariant under isomorphism, so no two listed groups
are isomorphic. The primary-decomposition argument proves that
every abelian group of order $300$ appears on the list.
:::
:::
