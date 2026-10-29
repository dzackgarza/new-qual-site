---
schema: qual/card@1
id: P-MV6ZQ
kind: problem
title: The quotient by the nilradical is reduced
classification:
  areas:
  - algebra
  topics:
  - Nilpotence
  - Ideals
  - Rings
relations: []
review: draft
audit:
- event: statement-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: 'The source reads "$R/ \nilrad{R}$ has no nonzero nilpotent elements." without declaring $R$ or posing a task; the statement declares $R$ a commutative ring and asks for a proof.'
---

::: {.problem}
Let $R$ be a commutative ring. Show that $R/ \nilrad{R}$ has no nonzero nilpotent elements.
:::

::: {.solution}
::: pf

::: pf-step
If $a+\nilrad{R}$ is nilpotent in $R/\nilrad{R}$, then $a\in\nilrad{R}$, so $a+\nilrad{R}=0$.

::: pf-proof
Suppose $(a+\nilrad{R})^n=0$ for some $n\ge1$.
Then $a^n+\nilrad{R}=\nilrad{R}$, so $a^n\in\nilrad{R}$, and $(a^n)^\ell=0$ for some $\ell\ge1$.
Hence $a^{n\ell}=0$, so $a$ is nilpotent and $a\in\nilrad{R}$.
:::

:::

:::

:::
