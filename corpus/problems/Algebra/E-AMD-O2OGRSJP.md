---
schema: qual/card@1
id: E-AMD-O2OGRSJP
kind: problem
title: $Z(S_n)=1$ for $n\geq 4$
classification:
  areas:
  - algebra
  topics:
  - Centralizers and Normalizers
  - Permutations
relations: []
review: draft
audit:
- event: solution-written
  by: Claude Opus 5
  date: 2026-08-30
---

::: {.exercise}
Show that the center of $S_n$ for $n\geq 4$ is trivial.
:::

::: solution
**Goal:** given a permutation that moves some point, produce a transposition it does not commute with.
A third point is needed to build that transposition, and $n \geq 4$ supplies one.

<1>1. Let $\sigma \in S_n$ with $\sigma \neq \id$, and fix $i$ with $\sigma(i) = j \neq i$.

<1>2. There is a point $k \notin \ts{i, j}$.
::: {.proof}
$\ts{1, \dots, n}$ has $n \geq 4$ elements and $\ts{i,j}$ has two.
:::

<1>3. $\sigma$ does not commute with the transposition $\tau = (j\, k)$.
::: {.proof}
<2>1. $(\sigma\tau)(i) = \sigma(\tau(i)) = \sigma(i) = j$, since $i \notin \ts{j,k}$ and so $\tau$ fixes $i$.
<2>2. $(\tau\sigma)(i) = \tau(\sigma(i)) = \tau(j) = k$.
<2>3. $j \neq k$ by the choice of $k$, so $\sigma\tau \neq \tau\sigma$.

:::
<1>4. Q.E.D.
::: {.proof}
Steps <1>1 through <1>3 show that no $\sigma \neq \id$ is central, so $Z(S_n) = 1$.
:::
:::
