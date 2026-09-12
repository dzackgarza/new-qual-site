---
schema: qual/card@1
id: P-HCAO10
kind: problem
title: Every maximal ideal in a commutative ring is prime
classification:
  areas:
  - algebra
  topics:
  - Prime Ideals
  - Maximal Ideals
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the preserved Harvard Commutative Algebra oral-question extraction.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Show that every maximal ideal in a commutative ring with identity is prime.
:::

::: solution
Let $R$ be a commutative ring with identity and let $\mathfrak m$ be a maximal
ideal.

<1>1. The quotient $R/\mathfrak m$ is a field.
::: proof
Let $a+\mathfrak m$ be a nonzero class, so $a\notin\mathfrak m$. The ideal
\[
\mathfrak m+(a)
\]
strictly contains $\mathfrak m$. By maximality it equals $R$. Hence there are
$m\in\mathfrak m$ and $r\in R$ with
\[
m+ra=1.
\]
Modulo $\mathfrak m$ this gives
\[
(r+\mathfrak m)(a+\mathfrak m)=1+\mathfrak m.
\]
Thus every nonzero class is invertible.
:::

<1>2. The ideal $\mathfrak m$ is prime.
::: proof
Suppose $ab\in\mathfrak m$. Then in the field $R/\mathfrak m$,
\[
(a+\mathfrak m)(b+\mathfrak m)=0.
\]
A field has no zero divisors, so either $a+\mathfrak m=0$ or
$b+\mathfrak m=0$. Equivalently, $a\in\mathfrak m$ or $b\in\mathfrak m$.
This is exactly the definition of a prime ideal.
:::
:::
