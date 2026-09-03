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

::: solution
**Goal:** each cycle moves only its own support and fixes the other's, so both composites act the same on every point.

<1>1. Let $\sigma$ and $\tau$ be cycles with disjoint supports $A = \supp(\sigma)$ and $B = \supp(\tau)$, so $A \cap B = \emptyset$, and let $x$ be any point.

<1>2. $\sigma$ maps $A$ to itself, and $\tau$ maps $B$ to itself.
::: {.proof}
If $a \in A$ then $\sigma(a) \neq a$, so $\sigma^{-1}(\sigma(a)) = a \neq \sigma(a)$, which means $\sigma(a)$ is not fixed by $\sigma^{-1}$. But $\sigma$ and $\sigma^{-1}$ have the same support (a point is moved by $\sigma$ iff it is moved by $\sigma^{-1}$), so $\sigma(a) \in A$.
:::

<1>3. If $x \in A$ then $(\sigma\tau)(x) = (\tau\sigma)(x)$.
::: {.proof}
<2>1. $x \notin B$, so $\tau(x) = x$ and $(\sigma\tau)(x) = \sigma(x)$.
<2>2. $\sigma(x) \in A$ by step <1>2, so $\sigma(x) \notin B$ and $\tau(\sigma(x)) = \sigma(x)$.
<2>3. Both composites give $\sigma(x)$.

:::
<1>4. If $x \in B$ then $(\sigma\tau)(x) = (\tau\sigma)(x)$.
::: {.proof}
Exchange the roles of $\sigma$ and $\tau$ in step <1>3.
:::

<1>5. If $x \notin A \cup B$ then both composites fix $x$.
::: {.proof}
$\sigma$ and $\tau$ each fix every point outside their own support.
:::

<1>6. Q.E.D.
::: {.proof}
Steps <1>3 through <1>5 cover every point, so $\sigma\tau = \tau\sigma$.
:::
:::
