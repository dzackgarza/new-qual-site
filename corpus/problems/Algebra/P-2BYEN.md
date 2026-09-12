---
schema: qual/card@1
id: P-2BYEN
kind: problem
title: Sylow subgroups for distinct primes intersect trivially
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - p-Groups
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-16
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Removed malformed p-group notation and used the coprime-order argument directly.
---

::: {.exercise}
Show that Sylow $p$- and $q$-subgroups for distinct primes $p\ne q$ intersect trivially.
:::

::: {.solution}
Let $P$ be a Sylow $p$-subgroup and $Q$ a Sylow $q$-subgroup, with $p\ne q$. Then
\[
P\cap Q\le P\quad\text{and}\quad P\cap Q\le Q.
\]
Hence $|P\cap Q|$ divides both a power of $p$ and a power of $q$. Since these powers are coprime, $|P\cap Q|=1$. Thus
\[
P\cap Q=1.
\]
:::
