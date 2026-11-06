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
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against Hungerford, Algebra (1974), Chapter I, section 6, exercise 3
    (checked-in extraction tmp/sources/hungerford-1974-algebra.md, line 1916):
    "If sigma = (i_1 i_2 ... i_r) in S_n and tau in S_n, then tau sigma tau^{-1}
    is the r-cycle (tau(i_1) tau(i_2) ... tau(i_r))." The card states exactly
    this and its I.6.3 locator is the printed number. The proof was read and
    checked: it evaluates tau sigma tau^{-1} at tau(i_j) and gets tau(i_{j+1}),
    cyclically, and at the points outside {tau(i_j)}, where tau^{-1} lands
    outside {i_j} so sigma fixes the point. A complete pointwise identification
    of two permutations; no defect.
---

::: {.problem}
If $\sigma = (i_1 i_2 \cdots i_r) \in S_n$ and $\tau \in S_n$, then show that $\tau\sigma\tau^{-1} = (\tau(i_1) \tau(i_2) \cdots \tau(i_r))$.
:::

::: {.solution}
Set
$$
\rho=(\tau(i_1)\ \tau(i_2)\ \cdots\ \tau(i_r)).
$$
We prove that $\tau\sigma\tau^{-1}$ and $\rho$ agree on every element of
$\{1,\ldots,n\}$.

::: pf

::: {.pf-step #s1}

For $1\le j<r$,
$$
(\tau\sigma\tau^{-1})(\tau(i_j))=\tau(i_{j+1}),
$$
and
$$
(\tau\sigma\tau^{-1})(\tau(i_r))=\tau(i_1).
$$

::: pf-proof

For $j<r$,
$$
(\tau\sigma\tau^{-1})(\tau(i_j))
=\tau(\sigma(i_j))
=\tau(i_{j+1}),
$$
while
$$
(\tau\sigma\tau^{-1})(\tau(i_r))
=\tau(\sigma(i_r))
=\tau(i_1).
$$
These are exactly the values of $\rho$ on its support.

:::

:::

::: {.pf-step #s2}

Every point outside $\{\tau(i_1),\ldots,\tau(i_r)\}$ is fixed by
$\tau\sigma\tau^{-1}$.

::: pf-proof

Let $x\notin\{\tau(i_1),\ldots,\tau(i_r)\}$. Since $\tau$ is bijective,
$\tau^{-1}(x)\notin\{i_1,\ldots,i_r\}$, so $\sigma$ fixes
$\tau^{-1}(x)$. Therefore
$$
(\tau\sigma\tau^{-1})(x)
=\tau(\tau^{-1}(x))
=x.
$$
The cycle $\rho$ fixes the same points.

:::

:::

::: pf-step

Hence
$$
\tau\sigma\tau^{-1}
=(\tau(i_1)\ \tau(i_2)\ \cdots\ \tau(i_r)).
$$

::: pf-proof

By steps [](#s1){.pf-ref} and [](#s2){.pf-ref} the two permutations agree on every point.

:::

:::

:::

:::
