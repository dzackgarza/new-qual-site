---
schema: qual/card@1
id: P-BKF18-6B
kind: problem
title: Strict diagonal dominance implies invertibility
classification:
  areas:
  - prelim
  topics:
  - Linear Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.problem}
Show that if $A=(a_{ij})$ is an $n\times n$ complex matrix satisfying
$$
\abs{a_{ii}}>\sum_{j\ne i}\abs{a_{ij}}
$$
for all $i\in\{1,\dots,n\}$, then $A$ is invertible.
:::

::: {.solution}
Assume $A x = 0$ and choose i such that $\abs{ x _ { i } } = \operatorname* { m a x } _ { j } \abs{ x _ { j } }$ . Then

$$
\abs{ a _ { i i } } \abs{ x _ { i } } \leq \sum _ { j \neq i } \abs{ a _ { i j } } \abs{ x _ { j } } \leq \sum _ { j \neq i } \abs{ a _ { i j } } \abs{ x _ { i } }
$$

so that

$$
\left( \abs{ a _ { i i } } - \sum _ { j \neq i } \abs{ a _ { i j } } \right) \abs{ x _ { i } } \leq 0 .
$$

Since the first factor is positive by assumption and the second is nonnegative, we must have $x _ { i } = 0$ . By choice of i we must have $x = 0$ so A is invertible.
:::
