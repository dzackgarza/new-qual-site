---
schema: qual/card@1
id: P-PADO6
kind: problem
title: Conjugating a cycle relabels its entries
classification:
  areas:
  - algebra
  topics:
  - Conjugacy
  - Permutations
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hungerford I.6.3 as reproduced in ETSU notes and an independent statement of the exercise.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
If $\sigma = (i_1 i_2 \cdots i_r) \in S_n$ and $\tau \in S_n$, then show that $\tau\sigma\tau^{-1} = (\tau(i_1) \tau(i_2) \cdots \tau(i_r))$.
:::

::: solution
Set
\[
\rho=(\tau(i_1)\ \tau(i_2)\ \cdots\ \tau(i_r)).
\]
We prove that $\tau\sigma\tau^{-1}$ and $\rho$ agree on every element of
$\{1,\ldots,n\}$.

<1>1. For $1\le j<r$,
\[
(\tau\sigma\tau^{-1})(\tau(i_j))=\tau(i_{j+1}),
\]
and
\[
(\tau\sigma\tau^{-1})(\tau(i_r))=\tau(i_1).
\]
::: proof
For $j<r$,
\[
(\tau\sigma\tau^{-1})(\tau(i_j))
=\tau(\sigma(i_j))
=\tau(i_{j+1}),
\]
while
\[
(\tau\sigma\tau^{-1})(\tau(i_r))
=\tau(\sigma(i_r))
=\tau(i_1).
\]
These are exactly the values of $\rho$ on its support.
:::

<1>2. Every point outside $\{\tau(i_1),\ldots,\tau(i_r)\}$ is fixed by
$\tau\sigma\tau^{-1}$.
::: proof
Let $x\notin\{\tau(i_1),\ldots,\tau(i_r)\}$. Since $\tau$ is bijective,
$\tau^{-1}(x)\notin\{i_1,\ldots,i_r\}$, so $\sigma$ fixes
$\tau^{-1}(x)$. Therefore
\[
(\tau\sigma\tau^{-1})(x)
=\tau(\tau^{-1}(x))
=x.
\]
The cycle $\rho$ fixes the same points.
:::

<1>3. Hence
\[
\tau\sigma\tau^{-1}
=(\tau(i_1)\ \tau(i_2)\ \cdots\ \tau(i_r)).
\]
::: proof
By <1>1 and <1>2 the two permutations agree on every point.
:::
:::
