---
schema: qual/card@1
id: E-AMD-E3N4BHJH
kind: problem
title: Maximal ideals are prime, and the converse fails
classification:
  areas:
  - algebra
  topics:
  - Maximal Ideals
  - Prime Ideals
  - Ideals
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: 'The source does not say what kind of ring is meant; the elementwise prime condition can fail for maximal ideals of noncommutative rings, so the statement now assumes a commutative ring with identity.'
---

::: {.exercise}
Let $R$ be a commutative ring with identity. Show that every maximal ideal of $R$ is prime, and give an example of a prime ideal that is not maximal.
:::

::: {.solution}
Let $\mm$ be a maximal ideal of $R$; it is proper by definition. Suppose $ab\in \mm$ and $b\notin \mm$. Then $\mm \subsetneq \mm + (b)$, so maximality gives $\mm + (b) = R$. Write $1 = m + rb$ with $m\in\mm$ and $r\in R$. Then
$$
a = am + r(ab).
$$
Both $am$ and $ab$ lie in $\mm$, so $a\in \mm$. Hence $\mm$ is prime.

The ideal $(0) \subset \ZZ$ is prime since $\ZZ$ is a domain, but not maximal since $(0) \subsetneq (2) \subsetneq \ZZ$.
:::
