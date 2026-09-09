---
schema: qual/card@1
id: P-DUUFY
kind: problem
title: $NH$ is a subgroup when $N$ is normal
classification:
  areas:
  - algebra
  topics:
  - Subgroups
  - Normal Subgroups
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
- Let $H\leq G$ be a subgroup and $N\normal G$ be a normal subgroup.
  Show that $NH \leq G$ is a subgroup.
:::


::: {.solution}
We use the one-step subgroup criterion.

<1>1. The set $NH$ is nonempty.
::: {.proof}
Since $e\in N\cap H$, one has $e=ee\in NH$.
:::

<1>2. If $n_1h_1,n_2h_2\in NH$, then
\[
(n_1h_1)(n_2h_2)^{-1}\in NH.
\]
::: {.proof}
Compute
\[
(n_1h_1)(n_2h_2)^{-1}
=n_1h_1h_2^{-1}n_2^{-1}.
\]
Put $h=h_1h_2^{-1}\in H$. Since $N\trianglelefteq G$,
\[
hn_2^{-1}h^{-1}\in N.
\]
Hence
\[
n_1h n_2^{-1}
=n_1(hn_2^{-1}h^{-1})h,
\]
which is a product of an element of $N$ and an element of $H$, so it lies in $NH$.
:::

<1>3. Therefore $NH\le G$.
::: {.proof}
Apply the subgroup criterion using <1>1 and <1>2.
:::
:::
