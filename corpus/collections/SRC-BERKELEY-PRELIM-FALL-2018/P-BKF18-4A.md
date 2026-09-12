---
schema: qual/card@1
id: P-BKF18-4A
kind: problem
title: A cosine power series
classification:
  areas:
  - prelim
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: problem
Let $a\in\mathbb R$ with $|a|<1$.
Prove that
\[
\sum_{k=1}^{\infty}a^k\cos(k\theta)
=\frac{-a^2+a\cos\theta}{1+a^2-2a\cos\theta}.
\]
:::

::: {.solution}
We use the fact that for any complex number $z = e ^ { i \theta } = \cos \theta + i \sin \theta \in \mathbb { C }$

$$
{ \frac { 1 } { 1 - a z } } = \sum _ { k = 0 } ^ { \infty } a ^ { k } z ^ { k } = \sum _ { k = 0 } ^ { \infty } a ^ { k } e ^ { i k \theta } = 1 + \sum _ { k = 1 } ^ { \infty } a ^ { k } ( \cos ( k \theta ) + i \sin ( k \theta ) ) .
$$

Therefore

$$
\begin{array} { c } { { \displaystyle \sum _ { k = 1 } ^ { \infty } a ^ { k } \cos ( k \theta ) = \Re \left( \displaystyle \frac { 1 } { 1 - a z } - 1 \right) = \Re \left( \displaystyle \frac { a z } { 1 - a z } \right) = \Re \left( \displaystyle \frac { a z ( 1 - a \bar { z } ) } { | 1 - a z | ^ { 2 } } \right) } } \\ { { = \Re \left( \displaystyle \frac { a \bar { z } - a ^ { 2 } } { ( 1 - a \cos \theta ) ^ { 2 } + ( a \sin \theta ) ^ { 2 } } \right) = \displaystyle \frac { a \cos \theta - a ^ { 2 } } { 1 + a ^ { 2 } - 2 a \cos \theta } . } } \end{array}
$$
:::
