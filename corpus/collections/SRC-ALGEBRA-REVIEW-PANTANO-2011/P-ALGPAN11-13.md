---
schema: qual/card@1
id: P-ALGPAN11-13
kind: problem
title: Nonempty intersection among sets of prime multiples
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the retained Pantano 2011 algebra-review source scan and verified from the stated algebraic criterion.
---

::: {.problem}
Let $P$ be the set of all primes, and for each integer $n$ let $P_n$ be the set of all prime multiples of $n$.
Which of the listed intersections is nonempty?

![Source scan for this review problem.](../../../assets/attachments/algebra-review-pantano-2011/problem-13.png)
:::

::: {.solution}
The nonempty intersection is $\boxed{\text{(C)}\;P_{12}\cap P_{20}}$.

<1>1. Exhibit an element of choice (C).
::: {.proof}
By definition $P_n=\{pn:p\text{ prime}\}$.
Since
\[
60=5\cdot12=3\cdot20,
\]
we have $60\in P_{12}\cap P_{20}$.
:::

<1>2. The other intersections are empty.
::: {.proof}
An equality $ap=bq$ with $p,q$ prime forces the prime factors of $a,b$ to match appropriately.

- $p=23q$ cannot hold with both $p,q$ prime, so $P_1\cap P_{23}=\varnothing$.

- $7p=21q$ gives $p=3q$, impossible for primes.

- $20p=24q$ gives $5p=6q$; then $q$ divides $5p$, forcing $q=5$ or $q=p$, neither satisfying the equation.

- $5p=25q$ gives $p=5q$, impossible for primes.

Thus only (C) is nonempty.
:::
:::
