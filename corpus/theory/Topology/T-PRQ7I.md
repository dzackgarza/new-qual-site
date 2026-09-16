---
schema: qual/card@1
id: T-PRQ7I
kind: theorem
title: Cantor's nested intervals theorem
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Completeness
  - Metric Spaces
relations: []
review: draft
---

::: {.theorem}
Let $[a_0, b_0]\supseteq[a_1, b_1]\supseteq\cdots$ be a decreasing sequence of closed bounded intervals in $\RR$.
Then $\Intersect_n [a_n, b_n]\neq\emptyset$ [@Rud76, Theorem 2.38], and if $b_n - a_n\to 0$, the intersection is a single point.
:::

::: {.proposition}
Let $X$ be a complete metric space and $E_0\supseteq E_1\supseteq\cdots$ nonempty closed bounded subsets with $\diam E_n\to 0$.
Then $\Intersect_n E_n$ consists of exactly one point [@Rud76, Exercise 3.21].
:::
