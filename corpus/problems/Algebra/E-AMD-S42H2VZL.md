---
schema: qual/card@1
id: E-AMD-S42H2VZL
kind: exercise
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
    *Proof:* A permutation fixes every point outside its support, so it cannot carry a point of the support to one outside it without failing to be injective there.

<1>3. If $x \in A$ then $(\sigma\tau)(x) = (\tau\sigma)(x)$.
    *Proof:*
    <2>1. $x \notin B$, so $\tau(x) = x$ and $(\sigma\tau)(x) = \sigma(x)$.
    <2>2. $\sigma(x) \in A$ by step <1>2, so $\sigma(x) \notin B$ and $\tau(\sigma(x)) = \sigma(x)$.
    <2>3. Both composites give $\sigma(x)$.

<1>4. If $x \in B$ then $(\sigma\tau)(x) = (\tau\sigma)(x)$.
    *Proof:* Exchange the roles of $\sigma$ and $\tau$ in step <1>3.

<1>5. If $x \notin A \cup B$ then both composites fix $x$.
    *Proof:* $\sigma$ and $\tau$ each fix every point outside their own support.

<1>6. Q.E.D.
    *Proof:* Steps <1>3 through <1>5 cover every point, so $\sigma\tau = \tau\sigma$.
:::
