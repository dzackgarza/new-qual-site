---
schema: qual/card@1
id: E-AMD-BBG6IC7K
kind: problem
title: Every ideal in a Noetherian ring is finitely generated
classification:
  areas:
  - algebra
  topics:
  - Noetherian Rings
  - Ideals
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-16
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.exercise}
Show that if $R$ is Noetherian then every ideal is finitely generated.
:::

::: {.solution}
Let \(I\) be an ideal of a Noetherian ring \(R\). Suppose \(I\) were not finitely generated. Choose \(x_1\in I\). Since \((x_1)\ne I\), choose
\[
x_2\in I\setminus(x_1).
\]
Inductively, having chosen \(x_1,\dots,x_n\) with
\[
I_n=(x_1,\dots,x_n)\subsetneq I,
\]
choose
\[
x_{n+1}\in I\setminus I_n.
\]
Then
\[
I_1\subsetneq I_2\subsetneq I_3\subsetneq\cdots
\]
is an infinite strictly ascending chain of ideals, contradicting the ACC on ideals.

Hence every ideal of \(R\) is finitely generated.
:::
