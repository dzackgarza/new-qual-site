---
schema: qual/card@1
id: P-ALGS16F
kind: problem
title: Solvability by radicals of $x^5 - 16x + 2 = 0$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: problem
Is the equation $x^5 - 16x + 2 = 0$ solvable in radicals?
:::

::: solution
**Goal:** Show this quintic is not solvable by radicals.

<1> Get the Galois group.
    *Proof:*
    <2>1. By Eisenstein at $2$, $f(x)=x^5-16x+2$ is irreducible over $\QQ$.
    <2>2. Hence its Galois group $G$ acts transitively on five roots.
    <2>3. Reduce mod $3$:
        $$\bar f(x)=x^5-x-1\in\mathbb F_3[x],$$
        which is irreducible, so Frobenius at $3$ gives a $5$-cycle in $G$.
    <2>4. Reduce mod $11$:
        $$\bar f(x)=x^5-5x+2\equiv (x-5)(x^4+5x^3+3x^2+4x+4)\in\mathbb F_{11}[x],$$
        where the quartic factor is irreducible, so Frobenius at $11$ gives a cycle of type $(4)(1)$.
    <2>5. A transitive subgroup of $S_5$ containing a $5$-cycle and a $4$-cycle is $S_5$.

<1> Conclude non-solvability.
    *Proof:*
    <2>1. Therefore $G\cong S_5$.
    <2>2. $S_5$ is not solvable.
    <2>3. By Galois theory, if $G$ is non-solvable, $f$ is not solvable by radicals.

Authored by **Codex 5.3 Spark Extra High**.
:::
