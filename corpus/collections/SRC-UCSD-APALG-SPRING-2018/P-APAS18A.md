---
schema: qual/card@1
id: P-APAS18A
kind: problem
title: Similarity of $8\times 8$ matrices with prescribed ranks of powers
classification:
  areas:
  - applied-algebra
  topics:
  - Linear Algebra
  - Jordan Canonical Form
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
Let $A,B\in\CC^{8\times 8}$ be two matrices such that
$$
\operatorname{rank} A=\operatorname{rank} B=6,\quad
\operatorname{rank} A^2=\operatorname{rank} B^2=4,\quad
\operatorname{rank} A^3=\operatorname{rank} B^3=2,\quad
\operatorname{rank} A^4=\operatorname{rank} B^4=0.
$$
Determine whether $A$ and $B$ are similar to each other or not.
If yes, explain why; if no, give a counterexample.
:::

::: {.solution}

::: pf

::: {.pf-step #blocks}

For a nilpotent $N\in\CC^{8\times8}$, the number of Jordan blocks of size at least $k$ is $\operatorname{rank}N^{k-1}-\operatorname{rank}N^k$.

::: pf-proof

On a nilpotent Jordan block of size $m$, $\operatorname{rank}J^{j}=\max(m-j,0)$, so passing from $J^{k-1}$ to $J^k$ lowers the rank by $1$ exactly when $m\ge k$. Summing over the blocks gives the count.

:::

:::

::: {.pf-step #jordan-form}

$A$ and $B$ are each nilpotent with exactly two Jordan blocks, both of size $4$.

::: pf-proof

$\operatorname{rank}A^4=0$ gives $A^4=0$. By step [](#blocks){.pf-ref}, the numbers of blocks of size at least $1,2,3,4$ are $8-6$, $6-4$, $4-2$, $2-0$, all equal to $2$, and none has size $5$ since $A^4=0$. The ranks for $B$ are the same.

:::

:::

::: pf-step

$A$ and $B$ are $\boxed{\text{similar}}$.

::: pf-proof

Two complex matrices with the same Jordan form are similar, and step [](#jordan-form){.pf-ref} gives both the Jordan form $J_4(0)\oplus J_4(0)$.

:::

:::

:::
:::
