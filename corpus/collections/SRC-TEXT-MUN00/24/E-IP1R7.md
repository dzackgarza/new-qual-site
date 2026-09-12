---
schema: qual/card@1
id: E-IP1R7
kind: problem
title: The plane minus countably many points is path connected
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

Assume that $\mathbb{R}$ is uncountable.
Show that if $A$ is a countable subset of $\mathbb{R}^2$, then $\mathbb{R}^2 - A$ is path connected.
[Hint: How many lines are there passing through a given point of $\mathbb{R}^2$?]
:::

::: {.solution}
Let $p,q\in\mathbb R^2-A$. There are uncountably many lines through $p$, while only countably many of them contain a point of $A$; also at most one contains $q$. Choose a line $L$ through $p$ that contains neither $q$ nor any point of $A$.

For each $a\in A$, the line through $q$ and $a$ meets $L$ in at most one point. The line through $p$ and $q$ also meets $L$ in only the point $p$. Hence only countably many points $r\in L$ have the property that the segment from $q$ to $r$ could pass through a point of $A$ (or pass through $p$). Since $L$ is uncountable, choose $r\in L$ outside this countable set.

The segment $[p,r]$ lies in $L$ and therefore avoids $A$. If $[q,r]$ met $A$ at $a$, then $r$ would lie on the line through $q$ and $a$, contrary to the choice of $r$. Thus the broken line
\[
p\longrightarrow r\longrightarrow q
\]
is a path in $\mathbb R^2-A$. Therefore $\mathbb R^2-A$ is path connected.
:::
