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

::: pf-qed
An algebraic closure of $K$ is a field $\overline{K}\supseteq K$ such that $\overline{K}$ is [[FD-3GZPO|algebraically closed]] and $\overline{K}/K$ is an algebraic extension.
:::

:::

:::

::: {.remark title="Example"}
$\CC$ is an algebraic closure of $\RR$ but not of $\QQ$.
$\CC$ is algebraically closed by the fundamental theorem of algebra, and $\CC=\RR(i)$ is algebraic over $\RR$.
Over $\QQ$, $\CC$ is not algebraic: the algebraic numbers form a countable set, while $\CC$ is uncountable.
:::
