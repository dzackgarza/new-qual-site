---
schema: qual/card@1
id: E-LEN3V
kind: problem
title: Unions of intersecting sequences of connected subspaces
classification:
  areas:
  - topology
  topics:
  - Connectedness
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

Let $\ts{A_n}$ be a sequence of connected subspaces of $X$, such that $A_n \cap A_{n+1} \neq \varnothing$ for all $n$.
Show that $\bigcup A_n$ is connected.
:::

::: {.solution}
Set
\[
B_n=A_1\cup\cdots\cup A_n.
\]
We prove inductively that $B_n$ is connected. The case $n=1$ is given. If $B_n$ is connected, then
\[
B_n\cap A_{n+1}\supseteq A_n\cap A_{n+1}\ne\varnothing,
\]
so the union $B_{n+1}=B_n\cup A_{n+1}$ of two intersecting connected sets is connected.

The sets $B_n$ form an increasing sequence of connected subspaces and all contain $A_1$. Hence their union is connected. Since
\[
\bigcup_nB_n=\bigcup_nA_n,
\]
the desired union is connected.
:::
