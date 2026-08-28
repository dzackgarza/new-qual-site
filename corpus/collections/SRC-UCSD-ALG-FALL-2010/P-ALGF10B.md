---
schema: qual/card@1
id: P-ALGF10B
kind: problem
title: "A group of order 2010 is solvable"
classification:
  areas:
  - algebra
  topics:
  - Group Theory
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
Show that a group of order $2010 = 2 \cdot 3 \cdot 5 \cdot 67$ is solvable.
:::

::: {.solution}
**Goal.** Show every group of order $2010 = 2 \cdot 3 \cdot 5 \cdot 67$ is solvable.

<1>1. $G$ has a normal Sylow $67$-subgroup $P$.
<2>1. $n_{67} \equiv 1 \pmod{67}$ and $n_{67} \mid 2 \cdot 3 \cdot 5 = 30$.
Proof: Sylow's theorem.
<2>2. The divisors of $30$ that are $\equiv 1 \pmod{67}$: only $1$.
Proof: $1, 2, 3, 5, 6, 10, 15, 30$ are all $< 67$ and $> 1$, so none is $\equiv 1 \pmod{67}$ except $1$.
<2>3. Hence $n_{67} = 1$, so $P$ is normal.
Proof: a unique Sylow subgroup is normal.

<1>2. $P \cong \ZZ/67$ is cyclic, hence solvable.
Proof: a group of prime order is cyclic, hence abelian, hence solvable.

<1>3. $G/P$ has order $30 = 2 \cdot 3 \cdot 5$.
<2>1. $|G/P| = 2010/67 = 30$.
Proof: quotient order.

<1>4. $G/P$ is solvable.
<2>1. Every group of order $30$ is solvable.
Proof: a group of order $30$ has a normal Sylow $5$-subgroup (since $n_5 \equiv 1 \pmod 5$ and $n_5 \mid 6$, so $n_5 = 1$ or $6$; if $n_5 = 6$ then there are $6 \cdot 4 = 24$ elements of order $5$, leaving $6$ elements, forcing a unique Sylow $3$-subgroup, which is normal). In any case, $G/P$ has a normal subgroup of prime index, and by induction (groups of order $2, 3, 5, 6, 10, 15$ are all solvable) it is solvable.
<2>2. More directly: $G/P$ has a normal subgroup $N$ of order $15$ (or $5$ or $3$), and both $N$ and $(G/P)/N$ are solvable (orders $15$ and $2$, or $5$ and $6$, etc.).
Proof: standard solvability of groups of order $30$.

<1>5. Hence $G$ is solvable.
<2>1. $P$ is solvable and $G/P$ is solvable.
Proof: <1>2 and <1>4.
<2>2. An extension of a solvable group by a solvable group is solvable.
Proof: if $N \normal G$ with $N$ and $G/N$ solvable, then $G$ is solvable.
<2>3. Hence $G$ is solvable.
Proof: <1>5.1 and <1>5.2.

<1>6. Q.E.D.
Proof: <1>5.3 is the claim.
:::
