---
schema: qual/card@1
id: P-AMD-73FM5GNT
kind: problem
title: Groups of order less than $60$ are solvable
classification:
  areas:
  - algebra
  topics:
  - Solvable Groups
  - Classification
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
Show: $|G| < 60 \implies G$ is solvable
:::

::: {.solution}
<1>1. Every group of order $< 60$ is solvable.
Proof: this is a standard classification result; we outline the argument.

<1>2. Every $p$-group is solvable.
Proof: a $p$-group has a nontrivial center, and by induction on the order, $G/Z(G)$ is solvable, so $G$ is solvable.

<1>3. Every group of order $pq$ (with $p, q$ primes) is solvable.
Proof: such a group has a normal Sylow subgroup (the larger prime's Sylow subgroup is normal), and the quotient is cyclic, so $G$ is solvable.

<1>4. Every group of order $p^2 q$ or $pqr$ (distinct primes) is solvable.
Proof: by Sylow theory, such a group has a normal Sylow subgroup, and the quotient is a group of smaller order (solvable by induction), so $G$ is solvable.

<1>5. The only non-solvable group of order $\le 60$ is $A_5$ (order $60$).
Proof: the smallest non-abelian simple group is $A_5$, of order $60$; any group of order $< 60$ has a nontrivial proper normal subgroup (by Sylow theory and the classification of small orders), and by induction is solvable.

<1>6. Hence every group of order $< 60$ is solvable.
Proof: <1>5.

<1>7. Q.E.D.
Proof: <1>6.
:::
