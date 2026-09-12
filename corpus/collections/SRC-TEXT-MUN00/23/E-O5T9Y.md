---
schema: qual/card@1
id: E-O5T9Y
kind: problem
title: The lower limit line is disconnected
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

Is the space $\mathbb{R}_\ell$ connected?
Justify your answer.
:::

::: {.solution}
No. In the lower-limit topology,
\[
(-\infty,0)=\bigcup_{n\ge1}[-n,0)
\]
and
\[
[0,\infty)=\bigcup_{n\ge1}[0,n)
\]
are both open. They are nonempty, disjoint, and their union is $\mathbb R$. Hence they form a separation of $\mathbb R_\ell$, so $\mathbb R_\ell$ is disconnected.
:::
