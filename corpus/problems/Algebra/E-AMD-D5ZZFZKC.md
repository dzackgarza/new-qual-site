---
schema: qual/card@1
id: E-AMD-D5ZZFZKC
kind: problem
title: Every $p$-group has a nontrivial center
classification:
  areas:
  - algebra
  topics:
  - p-Groups
  - Class Equation
  - Centralizers and Normalizers
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
  note: 'The source states the claim for every p-group; the trivial group is a p-group with trivial center, so the statement now assumes G nontrivial and finite.'
---

::: {.exercise}
Show that every nontrivial finite $p\dash$group has a nontrivial center.
:::

::: {.solution}
Let $G$ be a nontrivial finite $p$-group. Its class equation is
$$
\abs{G}=\abs{Z(G)}+\sum_i [G:C_G(x_i)],
$$
where the $x_i$ represent the noncentral conjugacy classes.

Each index $[G:C_G(x_i)]$ is a power of $p$. Since $x_i$ is noncentral, the index is greater than $1$, hence divisible by $p$. Also $\abs{G}$ is divisible by $p$. Reducing the class equation modulo $p$ gives
$$
\abs{Z(G)}\equiv0\pmod p.
$$
Since the identity belongs to $Z(G)$, the center is nonempty, so its positive order is at least $p$. Thus
$$
Z(G)\ne1.
$$
:::
