---
schema: qual/card@1
id: E-AMD-CM4ZVMMU
kind: problem
title: Groups of prime order are cyclic
classification:
  areas:
  - algebra
  topics:
  - Classification
  - Cyclic Groups
  - Cosets and Lagrange
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-16
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: 'The source does not say that p is prime; the statement now does.'
---

::: {.exercise}
Let $p$ be a prime. Show that every group of order $p$ is cyclic.
:::

::: {.solution}
Let $\abs{G}=p$, and choose $g\in G$ with $g\ne e$. By Lagrange's theorem, the order of $g$ divides $p$. Since $g$ is not the identity, its order is not $1$, so
$$
\abs{g}=p.
$$
Hence the cyclic subgroup $\langle g\rangle$ has $p$ elements. Since $\abs{G}=p$ as well,
$$
\langle g\rangle=G.
$$
Thus every group of prime order is cyclic (and therefore isomorphic to $\ZZ/p\ZZ$).
:::
