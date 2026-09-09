---
schema: qual/card@1
id: P-HGRO8
kind: problem
title: Sylow subgroups are conjugate
classification:
  areas: [algebra]
  topics: [Sylow Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the preserved Harvard group-theory oral-question extraction, Basic Group Theory, question on conjugacy of Sylow p-subgroups.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Prove that any two Sylow $p$-subgroups of a finite group are conjugate.
:::

::: solution
Let $P$ and $Q$ be Sylow $p$-subgroups of a finite group $G$.

<1>1. Let $P$ act by left multiplication on $G/Q$.
::: proof
Define
\[
x\cdot gQ=(xg)Q
\qquad(x\in P,\ gQ\in G/Q).
\]
This is a group action.
:::

<1>2. The action has a fixed coset $gQ$.
::: proof
Because $Q$ is Sylow, the index $[G:Q]$ is not divisible by $p$. Every orbit
of the $p$-group $P$ has size a power of $p$. If every orbit had size greater
than $1$, then every orbit size would be divisible by $p$, and hence so would
$[G:Q]$. Therefore some orbit has size $1$.
:::

<1>3. The fixed-point condition implies $P=gQg^{-1}$.
::: proof
Since $gQ$ is fixed by $P$, for every $x\in P$ we have
$xgQ=gQ$, hence $g^{-1}xg\in Q$. Thus
\[
P\le gQg^{-1}.
\]
Both groups have the same order, namely the largest power of $p$ dividing
$|G|$. Therefore the inclusion is equality:
\[
P=gQg^{-1}.
\]
Hence any two Sylow $p$-subgroups are conjugate.
:::
:::
