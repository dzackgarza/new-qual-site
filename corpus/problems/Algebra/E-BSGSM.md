---
schema: qual/card@1
id: E-BSGSM
kind: problem
title: Normal subgroups are unions of conjugacy classes
classification:
  areas:
  - algebra
  topics:
  - Normal Subgroups
  - Conjugacy
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Reduced the normal-subgroup statement to closure under conjugation.
---

::: {.exercise}
Show that if $N\trianglelefteq G$ and $C$ is a conjugacy class in $G$, then either $C\subseteq N$ or $C\cap N=\varnothing$.
:::

::: {.solution}
Suppose $C\cap N\ne\varnothing$, and choose $h\in C\cap N$. Since $C$ is the conjugacy class of $h$,
\[
C=\{ghg^{-1}:g\in G\}.
\]
Normality of $N$ implies $ghg^{-1}\in N$ for every $g\in G$. Hence $C\subseteq N$.

Therefore every conjugacy class is either contained in $N$ or disjoint from $N$.
:::
