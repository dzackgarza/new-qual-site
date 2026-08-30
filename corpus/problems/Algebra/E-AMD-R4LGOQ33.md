---
schema: qual/card@1
id: E-AMD-R4LGOQ33
kind: exercise
title: $p$-groups are solvable
classification:
  areas:
  - algebra
  topics:
  - p-Groups
  - Solvable Groups
relations: []
review: draft
audit:
- event: solution-written
  by: Claude Opus 5
  date: 2026-08-30
---

::: {.exercise}
Show that every $p\dash$group is solvable.
:::

::: solution
**Goal:** induct on the order, splitting $G$ by its center: the center is abelian, the quotient is a smaller $p$-group, and solvability passes through such an extension.

<1>1. Argue by induction on $\abs G = p^n$.

<1>2. Base case: if $n \leq 1$ then $G$ is trivial or of prime order, hence abelian, hence solvable.

<1>3. Inductive step: let $n \geq 2$ and assume every $p$-group of order less than $p^n$ is solvable.
*Proof:* <2>1. The class equation $$\abs G = \abs{Z(G)} + \sum_i [G : C_G(x_i)]$$ over representatives of the conjugacy classes of size greater than $1$ has every index divisible by $p$, so $p$ divides $\abs{Z(G)}$ and $Z(G) \neq 1$.
<2>2. $Z(G) \normal G$, and $Z(G)$ is abelian, hence solvable.
<2>3. $\abs{G/Z(G)} = \abs G / \abs{Z(G)} < p^n$, and it is a power of $p$, so $G/Z(G)$ is solvable by the inductive hypothesis.
<2>4. If $N \normal G$ with $N$ and $G/N$ solvable, then $G$ is solvable: lifting a subnormal series of $G/N$ with abelian quotients through $G \to G/N$ and appending a subnormal series of $N$ produces one for $G$.
<2>5. Applying step <2>4 with $N = Z(G)$ makes $G$ solvable.

<1>4. Q.E.D. *Proof:* Steps <1>2 and <1>3 complete the induction, so every $p$-group is solvable.
:::
