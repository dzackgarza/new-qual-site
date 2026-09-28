---
schema: qual/card@1
id: P-6FFAX
kind: problem
title: Groups of order $45$ are abelian
classification:
  areas:
  - algebra
  topics:
  - Classification
  - Abelian Groups
  - Sylow Theory
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
- Show that all groups of order 45 are abelian.
:::

::: {.solution}
Let $|G|=45=3^2\cdot5$. Sylow's theorem gives
\[
n_5\mid9,\qquad n_5\equiv1\pmod5,
\]
so $n_5=1$. Likewise
\[
n_3\mid5,\qquad n_3\equiv1\pmod3,
\]
so $n_3=1$. Hence the Sylow subgroups $P$ of order $9$ and $Q$ of order $5$ are both normal.

Their orders are coprime, so $P\cap Q=1$, and
\[
|PQ|=|P||Q|=45,
\]
thus $G=PQ$. Since both $P$ and $Q$ are normal, $[P,Q]\subseteq P\cap Q=1$, so
\[
G\cong P\times Q.
\]
Every group of order $9$ is abelian, and $Q\cong C_5$, hence $G$ is abelian. Consequently
\[
G\cong C_9\times C_5\cong C_{45}
\]
or
\[
G\cong (C_3\times C_3)\times C_5\cong C_3\times C_{15}.
\]
:::
