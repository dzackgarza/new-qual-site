---
schema: qual/card@1
id: E-AMD-S42H2VZL
kind: problem
title: Disjoint cycles commute
classification:
  areas:
  - algebra
  topics:
  - Permutations
relations: []
review: draft
audit:
- event: solution-written
  by: Claude Opus 5
  date: 2026-08-30
---

::: {.exercise}
Show that disjoint cycles commute.
:::

::: {.hint}
Each cycle maps its own support to itself and fixes every point outside it.
:::

::: {.solution}

::: pf

::: pf-step
Let $\sigma$ and $\tau$ be cycles with disjoint supports $A = \supp(\sigma)$ and $B = \supp(\tau)$, so $A \cap B = \emptyset$, and let $x$ be any point.
:::

::: {.pf-step #sigma-tau-preserve-own-support}
$\sigma$ maps $A$ to itself, and $\tau$ maps $B$ to itself.

::: pf-proof
If $a \in A$ then $\sigma(a) \neq a$, so $\sigma^{-1}(\sigma(a)) = a \neq \sigma(a)$, which means $\sigma(a)$ is not fixed by $\sigma^{-1}$. But $\sigma$ and $\sigma^{-1}$ have the same support (a point is moved by $\sigma$ iff it is moved by $\sigma^{-1}$), so $\sigma(a) \in A$.
:::

:::

::: {.pf-step #commute-on-a}
If $x \in A$ then $(\sigma\tau)(x) = (\tau\sigma)(x)$.

::: pf-proof

::: pf-step
$x \notin B$, so $\tau(x) = x$ and $(\sigma\tau)(x) = \sigma(x)$.
:::

::: pf-step
$\sigma(x) \in A$ by step [](#sigma-tau-preserve-own-support){.pf-ref}, so $\sigma(x) \notin B$ and $\tau(\sigma(x)) = \sigma(x)$.
:::

::: pf-step
Both composites give $\sigma(x)$.
:::

:::

:::

::: {.pf-step #commute-on-b}
If $x \in B$ then $(\sigma\tau)(x) = (\tau\sigma)(x)$.

::: pf-proof
Exchange the roles of $\sigma$ and $\tau$ in step [](#commute-on-a){.pf-ref}.
:::

:::

::: {.pf-step #commute-outside-both}
If $x \notin A \cup B$ then both composites fix $x$.

::: pf-proof
$\sigma$ and $\tau$ each fix every point outside their own support.
:::

:::

::: pf-qed
Steps [](#commute-on-a){.pf-ref} through [](#commute-outside-both){.pf-ref} cover every point, so $\sigma\tau = \tau\sigma$.
:::

:::

:::
