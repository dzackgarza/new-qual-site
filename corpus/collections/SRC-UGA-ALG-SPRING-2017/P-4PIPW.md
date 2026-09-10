---
schema: qual/card@1
id: P-4PIPW
kind: problem
title: 'Groups of order $56$: abelian classification and Sylow normality'
classification:
  areas:
  - algebra
  topics:
  - Classification
  - Structure Theorem
  - Sylow Theory
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: problem
a. How many isomorphism classes of abelian groups of order 56 are there?
Give a representative for one of each class.

b. Prove that if $G$ is a group of order 56, then either the Sylow-2 subgroup or the Sylow-7 subgroup is normal.

c. Give two non-isomorphic groups of order 56 where the Sylow-7 subgroup is normal and the Sylow-2 subgroup is *not* normal.
Justify that these two groups are not isomorphic.
:::

::: solution
Since $56=2^3\cdot7$, an abelian group of order $56$ is the product of $C_7$ with an abelian group of order $8$. The latter are $C_8$, $C_4\times C_2$, and $C_2^3$. Thus there are three classes:
\[
C_{56},\qquad C_{28}\times C_2,\qquad C_{14}\times C_2\times C_2.
\]

Let $n_7$ be the number of Sylow $7$-subgroups. Sylow gives $n_7\mid8$ and $n_7\equiv1\pmod7$, so $n_7=1$ or $8$. If $n_7=1$, we are done. Suppose $n_7=8$. Distinct Sylow $7$-subgroups meet trivially, so their nonidentity elements account for $8\cdot6=48$ elements. Hence only $8$ elements remain. A Sylow $2$-subgroup has exactly $8$ elements, so it is precisely this remaining set (including the identity). Therefore there can be only one Sylow $2$-subgroup, and it is normal.

For part (c), let $N=C_7=\langle a\rangle$. Since $\operatorname{Aut}(C_7)\cong C_6$ has a unique subgroup of order $2$, inversion defines a nontrivial action of any group admitting a quotient $C_2$ on $N$.

Take
\[
G_1=C_7\rtimes C_8,
\]
where a generator of $C_8$ acts by inversion, and
\[
G_2=C_7\rtimes (C_4\times C_2),
\]
where the $C_4$ generator acts by inversion and the $C_2$ factor acts trivially. In both groups $N$ is normal. The Sylow $2$-subgroup is not normal: if $H$ were a normal complement to $N$, then $[N,H]\subseteq N\cap H=1$, so the action of $H$ on $N$ would be trivial, contrary to construction.

Finally $G_1$ contains an element of order $8$ (the generator of its $C_8$ complement), whereas every element of the Sylow $2$-subgroup of $G_2$ has order at most $4$. Any element of $G_2$ of $2$-power order lies in some Sylow $2$-subgroup, so $G_2$ has no element of order $8$. Hence $G_1\not\cong G_2$.
:::
