---
schema: qual/card@1
id: P-V6YDP
kind: problem
title: $\sqrt{IJ}=\sqrt I\cap\sqrt J$
classification:
  areas:
  - algebra
  topics:
  - Prime Ideals
  - Ideals
relations: []
review: draft
audit:
- event: statement-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: The source leaves R, I and J undeclared; the statement declares I and J as ideals of a commutative ring R.
---

::: {.problem}
Let $I$ and $J$ be ideals of a commutative ring $R$. Show that
$$
\sqrt{IJ}=\sqrt I\cap\sqrt J.
$$
:::

::: {.solution}

::: pf

::: pf-step

$\sqrt{IJ}\subseteq\sqrt I\cap\sqrt J$.

::: pf-proof

Since $IJ\subseteq I$ and $IJ\subseteq J$, if $x^n\in IJ$ then $x^n\in I$ and $x^n\in J$.

:::

:::

::: pf-step

$\sqrt I\cap\sqrt J\subseteq\sqrt{IJ}$.

::: pf-proof

If $x\in\sqrt I\cap\sqrt J$, choose $m,n$ with $x^m\in I$ and $x^n\in J$. Then $x^{m+n}=x^mx^n\in IJ$, so $x\in\sqrt{IJ}$.

:::

:::

:::

:::
