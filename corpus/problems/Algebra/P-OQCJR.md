---
schema: qual/card@1
id: P-OQCJR
kind: problem
title: $Ax=0$ has a nontrivial solution iff $\rank(A)<m$
classification:
  areas:
  - algebra
  topics:
  - Rank and Nullity
  - Linear Algebra
  - Matrices
relations: []
review: draft
---

::: problem
We want to show that $A\vector x = \vector 0$ has a nontrivial solution $\iff \rank(A) < m$.

$\implies$: Suppose $A\vector v = \vector 0$ for some $\vector v \neq 0$.
Then $\dim \ker A \geq 1$, and by rank nullity we must have $m = \dim \ker A + \rank(A)$.
Since $\dim \ker A \ge 1$, this gives $\rank(A) = m - \dim \ker A \le m - 1$.

$\impliedby$: Suppose $\rank(A) < m$.
Then again by rank nullity, this forces $\dim \ker A \geq 1$, so $A$ has a nontrivial kernel and thus there is a nontrivial solution to $A\vector x = 0$.
:::
