---
schema: qual/card@1
id: P-WPFNX
kind: problem
title: No simple group of order $40$
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Simple Groups
relations: []
review: draft
audit:
- event: solution-reviewed
  by: claude
  date: 2026-11-06
  note: >-
    Rewritten as a Lamport structured proof. What was checked: the statement (a
    standard Sylow argument, no repair needed), and the existing prose against a fresh
    re-derivation: a Sylow 5-subgroup has order 5 and index 8, so n_5 divides 8 and is
    1 mod 5; the divisors of 8 are 1, 2, 4, 8 with residues 1, 2, 4, 3 modulo 5, so
    n_5 = 1; a unique Sylow subgroup is normal because its conjugates are Sylow
    subgroups; and a normal subgroup of order 5 is neither trivial nor all of a group
    of order 40, so the group is not simple. Correct. The prose's step from uniqueness
    to normality is now argued via conjugates, and the properness and nontriviality of
    P are stated with their orders rather than left implicit. No source solution is
    retained for this card, so no source comparison was made. What was not checked:
    any printed source.
---

::: {.problem}
Prove that there is no simple group of order $40$.
:::

::: {.solution}
Let $G$ be a group with $\abs{G}=40=2^3\cdot5$, and let $n_5$ be the number of its Sylow $5$-subgroups. A group is simple when it has no proper nontrivial normal subgroup.

::: pf

::: {.pf-step #sylow}
$n_5\mid 8$ and $n_5\equiv1\pmod 5$.

::: pf-proof
By the Sylow theorems, the number of Sylow $p$-subgroups of a finite group divides the index of such a subgroup and is congruent to $1$ modulo $p$. Here a Sylow $5$-subgroup has order $5$, so its index is $40/5=8$, giving $n_5\mid8$, and the congruence is $n_5\equiv1\pmod 5$.
:::

:::

::: {.pf-step #count}
$n_5=1$.

::: pf-proof
The positive divisors of $8$ are $1,2,4,8$, whose residues modulo $5$ are $1,2,4,3$; only $1\equiv1\pmod5$. So $n_5$, being a divisor of $8$ congruent to $1$ modulo $5$, equals $1$.
:::

:::

::: {.pf-step #normal}
The Sylow $5$-subgroup $P$ is normal in $G$, and it is neither trivial nor all of $G$.

::: pf-proof
$n_5=1$ by step [](#count){.pf-ref}, so $G$ has exactly one Sylow $5$-subgroup $P$; the conjugates of $P$ are again Sylow $5$-subgroups, so they all equal $P$, which is precisely the normality of $P$. Its order is $5$, so it contains a nonidentity element and is not the trivial subgroup, and $\abs{P}=5<40=\abs{G}$, so it is not all of $G$.
:::

:::

::: {.pf-step}
There is no simple group of order $40$.

::: pf-proof
Suppose $G$ has order $40$. Step [](#normal){.pf-ref} produces a normal subgroup $P$ with $1\neq P\neq G$, which is exactly a proper nontrivial normal subgroup; a simple group has none. Hence no such $G$ is simple.
:::

:::

:::
:::
