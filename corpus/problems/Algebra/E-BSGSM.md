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

::: pf

::: pf-step
If $C\cap N\ne\varnothing$, then $C\subseteq N$.

::: pf-proof
Choose $h\in C\cap N$. Since $C$ is the conjugacy class of $h$, $C=\{ghg^{-1}:g\in G\}$. Normality of $N$ gives $ghg^{-1}\in N$ for every $g\in G$, so $C\subseteq N$.
:::

:::

:::

:::

::: {.remark title="Variations"}
The converse holds: a subgroup $N\le G$ that is a union of conjugacy classes is normal, since for $h\in N$ and $g\in G$ the conjugate $ghg^{-1}$ lies in the class of $h$, which is contained in $N$. So a subgroup is normal if and only if it is a union of conjugacy classes, and then $N$ is the disjoint union of the classes of $G$ it contains.
:::
