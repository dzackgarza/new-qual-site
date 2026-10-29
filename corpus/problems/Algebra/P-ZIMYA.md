---
schema: qual/card@1
id: P-ZIMYA
kind: problem
title: Algebraic closure
classification:
  areas:
  - algebra
  topics:
  - Fields
  - Field Extensions
relations: []
review: draft
---

::: {.problem}
What is an algebraic closure of a field?
:::

::: {.solution}
Let $K$ be a field.

::: pf

::: pf-step

An algebraic closure of $K$ is a field $\overline{K}\supseteq K$ such that $\overline{K}$ is algebraically closed and $\overline{K}/K$ is an algebraic extension.

:::

::: pf-step

$\CC$ is an algebraic closure of $\RR$ but not of $\QQ$.

::: pf-proof

$\CC$ is algebraically closed by the fundamental theorem of algebra, and $\CC=\RR(i)$ is algebraic over $\RR$. Over $\QQ$, $\CC$ is not algebraic: the algebraic numbers form a countable set, while $\CC$ is uncountable.

:::

:::

:::

:::
