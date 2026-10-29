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

::: {.solution}
Let $\sigma \in S_n$ with $\sigma \neq \id$, and fix $i$ with $\sigma(i) = j \neq i$.

::: pf

::: pf-step
There is a point $k \notin \theset{i, j}$.

::: pf-proof
$\theset{1, \ldots, n}$ has $n \geq 4$ elements and $\theset{i,j}$ has two.
:::

:::

::: {.pf-step #sigma-noncommutes-with-tau}
$\sigma$ does not commute with the transposition $\tau = (j\, k)$.

::: pf-proof

::: pf-step
$(\sigma\tau)(i) = \sigma(\tau(i)) = \sigma(i) = j$, since $i \notin \theset{j,k}$ and so $\tau$ fixes $i$.
:::

::: pf-step
$(\tau\sigma)(i) = \tau(\sigma(i)) = \tau(j) = k$.
:::

::: pf-step
$j \neq k$ by the choice of $k$, so $\sigma\tau \neq \tau\sigma$.
:::

:::

:::

::: pf-qed
Since $\sigma \neq \id$ was arbitrary, step [](#sigma-noncommutes-with-tau){.pf-ref} shows that no $\sigma \neq \id$ is central, so $Z(S_n) = 1$.
:::

:::

:::
