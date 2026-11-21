---
schema: qual/card@1
id: P-TOP-WORKSHOP-2020-WS2A-HW2
kind: problem
title: A $T_n$ space that is not $T_{n+1}$
classification:
  areas:
  - topology
  topics:
  - Separation Axioms
  - Counterexamples
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into numbered steps for issue #2: the space defined, its $T_{0}$ property, and the
    failure of $T_{1}$. No retained solution set covers this exercise (the collection retains the
    worksheets, not solutions), so the argument is the card's own; it was re-read for this pass.
---

::: {.problem}
Pick an $n\in\{0,1,2,3\}$, and give an example of a space that is $T_n$, but not $T_{n+1}$.
:::

::: {.solution}
No retained solution set covers this exercise; the argument is the card's own. The example given is for $n=0$: a space that is $T_{0}$ but not $T_{1}$.

::: pf

::: {.pf-step #space}
$X=\{0,1\}$ with the topology $\tau=\{\varnothing,\{1\},X\}$ is a topological space.

::: pf-proof
The family $\tau$ contains $\varnothing$ and $X$, and it is closed under finite intersections and arbitrary unions: the only nonempty proper open set is $\{1\}$, and $\{1\}\cap\{1\}=\{1\}$, $\{1\}\cup X=X$. So $\tau$ satisfies the axioms for a topology, called the Sierpiński topology on two points.
:::

:::

::: {.pf-step #t0}
$X$ is $T_{0}$.

::: pf-proof
The two points must be topologically distinguishable: an open set containing exactly one of them. The open set $\{1\}$ contains $1$ and not $0$, so the pair is distinguished (in the other order, every open set containing $0$, namely $X$ alone, also contains $1$).
:::

:::

::: {.pf-step}
$X$ is not $T_{1}$.

::: pf-proof
If $X$ were $T_{1}$ its singletons would be closed. But $X\setminus\{1\}=\{0\}$ is not in $\tau$, so $\{1\}$ is not closed; equivalently, the only open neighbourhood of $0$ is $X$ itself, which contains $1$, so no open set contains $0$ and omits $1$. Hence $X$ is $T_{0}$ and not $T_{1}$, which is the required example for $n=0$.
:::

:::

:::
:::
