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

::: solution
**Goal:** transitivity forces $3$ to divide the order of the subgroup, which leaves only the two subgroups of $S_3$ of order divisible by $3$.

<1>1. Let $H \leq S_3$ act transitively on $X = \ts{1,2,3}$.

<1>2. $3$ divides $\abs H$.
::: {.proof}
<2>1. Transitivity says the orbit of $1$ is all of $X$, so it has $3$ elements.
<2>2. Orbit-stabilizer gives $\abs H = 3 \cdot \abs{H_1}$, where $H_1$ is the stabilizer of $1$ in $H$.

:::
<1>3. $\abs H \in \ts{3, 6}$.
::: {.proof}
$\abs H$ divides $\abs{S_3} = 6$ by Lagrange, and step <1>2 rules out $1$ and $2$.
:::

<1>4. If $\abs H = 6$ then $H = S_3$.
::: {.proof}
$H \leq S_3$ and the two have the same finite order.
:::

<1>5. If $\abs H = 3$ then $H = A_3$.
::: {.proof}
<2>1. $H$ is a Sylow $3$-subgroup of $S_3$.
<2>2. The number $n_3$ of Sylow $3$-subgroups satisfies $n_3 \equiv 1 \pmod 3$ and $n_3 \mid 2$, so $n_3 = 1$.
<2>3. $A_3 = \gens{(1\,2\,3)}$ has order $3$, so it is that one Sylow subgroup, and $H = A_3$.

:::
<1>6. Both $S_3$ and $A_3$ are transitive.
::: {.proof}
$(1\,2\,3) \in A_3$ carries $1$ to $2$ to $3$, so the orbit of $1$ under $A_3$, and a fortiori under $S_3$, is all of $X$.
:::

<1>7. Q.E.D.
::: {.proof}
Steps <1>3 through <1>5 show a transitive subgroup is $S_3$ or $A_3$, and step <1>6 shows both are.
:::
:::
