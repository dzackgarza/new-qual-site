---
schema: qual/card@1
id: P-TOP-WORKSHOP-D3-W2
kind: problem
title: '$T_4\Rightarrow T_3\Rightarrow T_2\Rightarrow T_1\Rightarrow T_0$'
classification:
  areas:
  - topology
  topics:
  - Separation Axioms
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into numbered steps for issue #2: the conventions recorded once, then the four
    implications separately. No retained solution set covers this exercise (the collection retains the
    problem packets, not solutions), so the argument is the card's own; it was re-read for this pass
    and each implication names the definition it uses.
---

::: {.problem}
$$T_4\Longrightarrow T_3\Longrightarrow T_2\Longrightarrow T_1\Longrightarrow T_0.$$
:::

::: {.solution}
No retained solution set covers this exercise; the argument is the card's own. The conventions used are those of the worksheet: $T_{1}$ means that singletons are closed, $T_{2}$ means Hausdorff, $T_{3}$ means regular and $T_{1}$, and $T_{4}$ means normal and $T_{1}$. Regularity is the separation of a point from a closed set not containing it, and normality the separation of two disjoint closed sets, by disjoint open sets.

::: pf

::: {.pf-step #t4-t3}
$T_{4}\Rightarrow T_{3}$.

::: pf-proof
Let $X$ be normal and $T_{1}$, let $F\subset X$ be closed and let $x\notin F$. Then $\{x\}$ is closed because $X$ is $T_{1}$, and $\{x\}$ is disjoint from $F$, so normality gives disjoint open sets $U\ni x$ and $V\supset F$. That is exactly regularity, so $X$ is regular and $T_{1}$, that is $T_{3}$.
:::

:::

::: {.pf-step #t3-t2}
$T_{3}\Rightarrow T_{2}$.

::: pf-proof
Let $X$ be regular and $T_{1}$ and let $x\ne y$. Since singletons are closed, $\{y\}$ is closed and does not contain $x$; regularity gives disjoint open sets $U\ni x$ and $V\supset\{y\}$. So distinct points have disjoint neighbourhoods and $X$ is Hausdorff.
:::

:::

::: {.pf-step #t2-t1}
$T_{2}\Rightarrow T_{1}$.

::: pf-proof
Let $X$ be Hausdorff and $y\in X$. For each $x\ne y$ the Hausdorff property gives an open $U_{x}\ni x$ with $y\notin U_{x}$, and every point of $X\setminus\{y\}$ occurs as such an $x$. Hence $X\setminus\{y\}=\bigcup_{x\ne y}U_{x}$ is open, so $\{y\}$ is closed. As $y$ was arbitrary, all singletons are closed and $X$ is $T_{1}$.
:::

:::

::: {.pf-step}
$T_{1}\Rightarrow T_{0}$, so $T_{4}\Rightarrow T_{3}\Rightarrow T_{2}\Rightarrow T_{1}\Rightarrow T_{0}$.

::: pf-proof
Let $X$ be $T_{1}$ and $x\ne y$. Then $\{y\}$ is closed, so $X\setminus\{y\}$ is open, contains $x$ and omits $y$: the two points are topologically distinguishable, which is $T_{0}$. Chaining this with steps [](#t4-t3){.pf-ref}, [](#t3-t2){.pf-ref} and [](#t2-t1){.pf-ref} gives the whole chain displayed in the problem.
:::

:::

:::
:::
