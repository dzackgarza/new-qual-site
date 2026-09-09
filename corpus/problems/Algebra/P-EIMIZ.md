---
schema: qual/card@1
id: P-EIMIZ
kind: problem
title: Groups of order 35
classification:
  areas:
  - algebra
  topics:
  - Classification
  - Sylow Theory
  - Cyclic Groups
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
Classify groups of order 35.
:::


::: {.solution}
Let $|G|=35=5\cdot7$.

<1>1. The Sylow $7$-subgroup is unique and normal.
::: {.proof}
Sylow gives
\[
n_7\mid5,
\qquad
n_7\equiv1\pmod7.
\]
Thus $n_7=1$.
:::

<1>2. The Sylow $5$-subgroup is unique and normal.
::: {.proof}
Sylow gives
\[
n_5\mid7,
\qquad
n_5\equiv1\pmod5.
\]
The divisors of $7$ are $1$ and $7$, and $7\not\equiv1\pmod5$. Hence $n_5=1$.
:::

<1>3. Therefore $G\cong C_{35}$.
::: {.proof}
Let $P$ and $Q$ be the normal Sylow subgroups of orders $5$ and $7$. Their intersection is trivial and $|PQ|=35$, so $G=PQ$. For $p\in P$ and $q\in Q$, the commutator lies in both $P$ and $Q$ because both subgroups are normal, hence is trivial. Thus $P$ and $Q$ commute, so
\[
G\cong P\times Q\cong C_5\times C_7\cong C_{35}.
\]
:::

Thus there is exactly one group of order $35$ up to isomorphism, and it is cyclic.
:::
