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

::: {.problem}
Show that Sylow $p$- and $q$-subgroups for distinct primes $p\ne q$ intersect trivially.
:::

::: {.solution}
Let $P$ be a Sylow $p$-subgroup and $Q$ a Sylow $q$-subgroup of a finite group $G$, with $p\ne q$.

::: pf

::: {.pf-step #divides}

The order $\abs{P\cap Q}$ divides both $\abs P$, a power of $p$, and $\abs Q$, a power of $q$.

::: pf-proof

Since $P\cap Q\le P$ and $P\cap Q\le Q$, Lagrange's theorem gives both divisibilities.

:::

:::

::: pf-step

$P\cap Q=1$.

::: pf-proof

By step [](#divides){.pf-ref}, $\abs{P\cap Q}$ is simultaneously a power of $p$ and a power of $q$. Since $p\ne q$, the only such positive integer is $1$.

:::

:::

:::

:::
