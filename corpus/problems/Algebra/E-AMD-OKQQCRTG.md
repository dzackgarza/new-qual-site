---
schema: qual/card@1
id: E-AMD-OKQQCRTG
kind: problem
title: $p$-groups are nilpotent
classification:
  areas:
  - algebra
  topics:
  - p-Groups
  - Nilpotent Groups
relations: []
review: draft
audit:
- event: solution-written
  by: Claude Opus 5
  date: 2026-08-30
---

::: {.exercise}
Show that p-groups $\implies$ nilpotent
:::

::: solution
**Goal:** the upper central series of a finite $p$-group cannot stop below $G$, because the obstruction to continuing is a $p$-group with trivial center.

<1>1. A nontrivial finite $p$-group has nontrivial center.
::: {.proof}
<2>1. Let $P$ be a group of order $p^n$ with $n \geq 1$, and take the class equation $$\abs P = \abs{Z(P)} + \sum_i [P : C_P(x_i)]$$ over representatives $x_i$ of the conjugacy classes of size greater than $1$.
<2>2. Each such index divides $\abs P$ and exceeds $1$, so $p$ divides it.
<2>3. $p$ divides $\abs P$, so $p$ divides $\abs{Z(P)}$, and $Z(P) \neq 1$.

:::
<1>2. Let $G$ have order $p^n$ and let $1 = Z_0 \leq Z_1 \leq \cdots$ be its upper central series, where $Z_{m+1}$ is the preimage in $G$ of $Z(G/Z_m)$.

<1>3. If $Z_m \neq G$ then $Z_{m+1} \neq Z_m$.
::: {.proof}
<2>1. $G/Z_m$ is a nontrivial group whose order divides $p^n$, so it is a nontrivial $p$-group.
<2>2. By step <1>1, $Z(G/Z_m) \neq 1$.
<2>3. $Z_{m+1}/Z_m = Z(G/Z_m)$, so $Z_{m+1}$ strictly contains $Z_m$.

:::
<1>4. Q.E.D.
::: {.proof}
By step <1>3 the orders $\abs{Z_0} < \abs{Z_1} < \cdots$ strictly increase while $Z_m \neq G$, and they are bounded by $p^n$.
So $Z_m = G$ for some $m \leq n$, which is the definition of $G$ being nilpotent.
:::
:::
