---
schema: qual/card@1
id: P-7KDF2
kind: problem
title: The parallelogram identity for complex numbers and its geometric meaning
classification:
  areas:
  - complex-analysis
  topics:
  - Geometry
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
Prove that $\abs{z_1 + z_2}^2 + \abs{z_1 - z_2}^2 = 2(\abs{z_1}^2 + \abs{z_2}^2)$ for any two complex numbers $z_1, z_2 \in \CC$, and explain the geometric meaning of this identity.
:::

::: {.solution}

::: pf

::: pf-step
$\abs{z_1 + z_2}^2 + \abs{z_1 - z_2}^2 = 2(\abs{z_1}^2 + \abs{z_2}^2)$.

::: pf-proof
Using $\abs{w}^2=w\overline w$,
$$
\abs{z_1\pm z_2}^2 = (z_1\pm z_2)(\overline z_1\pm\overline z_2) = \abs{z_1}^2+\abs{z_2}^2\pm\bigl(z_1\overline z_2+z_2\overline z_1\bigr).
$$
Adding the two cases cancels the cross terms.
:::

:::

::: pf-step
The identity says that in a parallelogram the sum of the squares of the two diagonals equals the sum of the squares of the four sides.

::: pf-proof
The points $0$, $z_1$, $z_1+z_2$, $z_2$ are the vertices of the parallelogram spanned by $z_1$ and $z_2$.
Its diagonals have lengths $\abs{z_1+z_2}$ and $\abs{z_1-z_2}$, and its sides have lengths $\abs{z_1}$, $\abs{z_2}$, $\abs{z_1}$, $\abs{z_2}$.
:::

:::

:::

:::
