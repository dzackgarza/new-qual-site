---
schema: qual/card@1
id: E-HAT-3.3-12
kind: problem
title: "Commutator length in free groups"
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.3, Exercise 12; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
As an algebraic application of the preceding problem, show that in a free group $F$ with basis $x_1, \ldots, x_{2k}$, the product of commutators $[x_1, x_2] \cdots [x_{2k-1}, x_{2k}]$ is not equal to a product of fewer than $k$ commutators $[\nu_i, w_i]$ of elements $\nu_i, w_i \in F$.
:::

::: {.solution}
Let
\[
r_k=[x_1,x_2]\cdots[x_{2k-1},x_{2k}]\in F(x_1,\ldots,x_{2k}).
\]
Suppose, toward a contradiction, that
\[
r_k=[v_1,w_1]\cdots[v_j,w_j]
\]
with $j<k$.

Use the standard CW structure on the genus-$j$ surface $M_j$: its $1$-skeleton is a wedge of $2j$ circles with generators $a_i,b_i$, and its $2$-cell is attached by
\[
[a_1,b_1]\cdots[a_j,b_j].
\]
Likewise $M_k$ has $1$-skeleton a wedge of $2k$ circles with generators $x_1,\ldots,x_{2k}$ and $2$-cell attaching word $r_k$.

Define a map of $1$-skeleta
\[
g:(M_j)^1\to(M_k)^1
\]
by sending the loop $a_i$ to a loop representing $v_i$ and $b_i$ to a loop representing $w_i$. The boundary of the $2$-cell of $M_j$ then maps to
\[
[v_1,w_1]\cdots[v_j,w_j]=r_k,
\]
which is exactly the attaching loop of the $2$-cell of $M_k$. Hence $g$ extends over the $2$-cell to a map
\[
f:M_j\to M_k
\]
that maps the source $2$-cell once over the target $2$-cell. Therefore $f$ has degree $1$.

By Exercise 11, a degree-$1$ map $M_j\to M_k$ can exist only if $j\ge k$. This contradicts $j<k$. Thus $r_k$ cannot be expressed as a product of fewer than $k$ commutators.
:::
