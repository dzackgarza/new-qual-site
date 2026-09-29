---
schema: qual/card@1
id: E-AMD-PLA4XW64
kind: problem
title: Transitive subgroups of $S_3$ are $S_3$ and $A_3$
classification:
  areas:
  - algebra
  topics:
  - Permutations
  - Subgroups
  - Group Actions
relations: []
review: draft
audit:
- event: solution-written
  by: Claude Opus 5
  date: 2026-08-30
---

::: {.exercise}
Show that the transitive subgroups of $S_3$ are $S_3, A_3$
:::

::: {.hint}
By orbit-stabilizer, $3$ divides the order of a transitive subgroup of $S_3$.
:::

::: {.solution}

::: pf

::: pf-step
Let $H \leq S_3$ act transitively on $X = \ts{1,2,3}$.
:::

::: {.pf-step #h-order-divisible-by-3}
$3$ divides $\abs H$.

::: pf-proof

::: pf-step
Transitivity says the orbit of $1$ is all of $X$, so it has $3$ elements.
:::

::: pf-step
Orbit-stabilizer gives $\abs H = 3 \cdot \abs{H_1}$, where $H_1$ is the stabilizer of $1$ in $H$.
:::

:::

:::

::: {.pf-step #h-order-three-or-six}
$\abs H \in \ts{3, 6}$.

::: pf-proof
$\abs H$ divides $\abs{S_3} = 6$ by Lagrange, and step [](#h-order-divisible-by-3){.pf-ref} rules out $1$ and $2$.
:::

:::

::: {.pf-step #order-six-is-s3}
If $\abs H = 6$ then $H = S_3$.

::: pf-proof
$H \leq S_3$ and the two have the same finite order.
:::

:::

::: {.pf-step #order-three-is-a3}
If $\abs H = 3$ then $H = A_3$.

::: pf-proof

::: pf-step
$H$ is a Sylow $3$-subgroup of $S_3$.
:::

::: pf-step
The number $n_3$ of Sylow $3$-subgroups satisfies $n_3 \equiv 1 \pmod 3$ and $n_3 \mid 2$, so $n_3 = 1$.
:::

::: pf-step
$A_3 = \gens{(1\,2\,3)}$ has order $3$, so it is that one Sylow subgroup, and $H = A_3$.
:::

:::

:::

::: {.pf-step #both-transitive}
Both $S_3$ and $A_3$ are transitive.

::: pf-proof
$(1\,2\,3) \in A_3$ carries $1$ to $2$ to $3$, so the orbit of $1$ under $A_3$, and a fortiori under $S_3$, is all of $X$.
:::

:::

::: pf-qed
Steps [](#h-order-three-or-six){.pf-ref} through [](#order-three-is-a3){.pf-ref} show a transitive subgroup is $S_3$ or $A_3$, and step [](#both-transitive){.pf-ref} shows both are.
:::

:::

:::
