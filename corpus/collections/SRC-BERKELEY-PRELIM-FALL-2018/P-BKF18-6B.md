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
\[
|a_{ii}|>\sum_{j\ne i}|a_{ij}|
\]
for all $i\in\{1,\dots,n\}$, then $A$ is invertible.
:::

::: {.solution}
Assume $A x = 0$ and choose i such that $\left| x _ { i } \right| = \operatorname* { m a x } _ { j } \left| x _ { j } \right|$ . Then

$$
| a _ { i i } | | x _ { i } | \leq \sum _ { j \neq i } | a _ { i j } | | x _ { j } | \leq \sum _ { j \neq i } | a _ { i j } | | x _ { i } |
$$

so that

$$
\left( \left| a _ { i i } \right| - \sum _ { j \neq i } \left| a _ { i j } \right| \right) \left| x _ { i } \right| \leq 0 .
$$

Since the first factor is positive by assumption and the second is nonnegative, we must have $x _ { i } = 0$ . By choice of i we must have $x = 0$ so A is invertible.
:::
