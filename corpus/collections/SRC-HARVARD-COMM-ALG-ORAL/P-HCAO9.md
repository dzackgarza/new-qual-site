---
schema: qual/card@1
id: P-HCAO9
kind: problem
title: A prime ideal with finite quotient is maximal
classification:
  areas:
  - algebra
  topics:
  - Prime Ideals
  - Maximal Ideals
  - Finite Fields
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
Let $R$ be a commutative ring with identity, and let $P$ be a prime ideal of $R$.
If $R/P$ is finite, show that $P$ is maximal.
:::

::: solution
Because $P$ is prime, the quotient $R/P$ is an integral domain.

<1>1. Every finite integral domain is a field.
::: proof
Let $D$ be a finite integral domain and let $0\ne a\in D$. Multiplication by
$a$ defines
\[
D\to D,
\qquad
x\mapsto ax.
\]
This map is injective because $D$ has no zero divisors, hence bijective because
$D$ is finite. Therefore $1$ lies in its image, so $ab=1$ for some $b\in D$.
Thus every nonzero element of $D$ is invertible.
:::

<1>2. The quotient $R/P$ is a field.
::: proof
It is a finite integral domain, so <1>1 applies.
:::

<1>3. Therefore $P$ is maximal.
::: proof
For a commutative ring with identity, an ideal $I$ is maximal if and only if
$R/I$ is a field. Apply this criterion to $I=P$ and use <1>2.
:::
:::
