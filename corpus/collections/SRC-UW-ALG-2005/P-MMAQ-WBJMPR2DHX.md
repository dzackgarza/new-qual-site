---
schema: qual/card@1
id: P-MMAQ-WBJMPR2DHX
kind: problem
title: Order of $\mathrm{GL}_3(\mathbb{F}_2)$ and the number of elements of order
  $7$
classification:
  areas:
  - algebra
  topics:
  - Matrix Groups
  - Simple Groups
  - Finite Fields
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
---

::: {.problem}
Let $\mathbb F_2$ be the field with two elements.

- What is the order of $\text{GL}_3(\mathbb F_2)$?

- Use the fact that $\text{GL}_3(\mathbb F_2)$ is a simple group (which you should not prove) to find the number of elements of order 7 in $\text{GL}_3(\mathbb F_2)$.
:::

::: {.solution}
<1>1. The order of $\operatorname{GL}_3(\mathbb F_2)$ is
\[
(2^3-1)(2^3-2)(2^3-2^2)=7\cdot6\cdot4=168.
\]
::: {.proof}
The first column of an invertible $3\times3$ matrix may be any nonzero vector of $\mathbb F_2^3$, giving $8-1=7$ choices. The second column may be any vector outside the span of the first, giving $8-2=6$ choices. The third may be any vector outside the $2$-dimensional span of the first two, giving $8-4=4$ choices. Multiplying gives $168$.
:::

<1>2. The number $n_7$ of Sylow $7$-subgroups is $8$.
::: {.proof}
Since
\[
168=2^3\cdot3\cdot7,
\]
the Sylow theorems give
\[
n_7\equiv1\pmod7,
\qquad
n_7\mid24.
\]
The only divisors of $24$ congruent to $1$ modulo $7$ are $1$ and $8$. If $n_7=1$, the unique Sylow $7$-subgroup would be normal. Because $\operatorname{GL}_3(\mathbb F_2)$ is simple and has order greater than $7$, this is impossible. Hence $n_7=8$.
:::

<1>3. There are exactly $48$ elements of order $7$ in $\operatorname{GL}_3(\mathbb F_2)$.
::: {.proof}
Every Sylow $7$-subgroup has order $7$, hence is cyclic and has exactly $6$ nonidentity elements, all of order $7$. Distinct subgroups of order $7$ intersect only in the identity, since their intersection is a subgroup whose order divides $7$. Thus the $8$ Sylow $7$-subgroups contribute disjoint sets of $6$ elements of order $7$, giving
\[
8\cdot6=48.
\]
:::
:::
