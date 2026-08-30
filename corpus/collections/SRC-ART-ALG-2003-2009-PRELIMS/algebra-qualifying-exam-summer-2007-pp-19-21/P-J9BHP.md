---
schema: qual/card@1
id: P-J9BHP
kind: problem
title: The characteristic of an integral domain is zero or prime
classification:
  areas:
  - algebra
  topics:
  - Integral Domains
  - Characteristic
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: problem
Show that the characteristic of an integral domain must be either zero or a prime.
:::

::: {.solution}
<1>1. Let $R$ be an integral domain with identity $1_R \neq 0$, and let $n = \operatorname{char}(R)$.
Proof: setup and definition of an integral domain (non-zero ring with no zero divisors).

<1>2. If $n = 0$, the claim holds.
Proof: zero is one of the allowed alternatives.

<1>3. If $n > 0$, then $n$ must be a prime integer.
<2>1. By definition of characteristic, $n$ is the smallest positive integer such that $n \cdot 1_R = 0_R$.
Proof: definition of characteristic for a ring with unity.
<2>2. Since $1_R \neq 0_R$, $1 \cdot 1_R = 1_R \neq 0_R$, so $n \ge 2$.
Proof: <1>1. <2>3. Suppose for contradiction that $n$ is composite: $n = ab$ for integers $a, b$ with $1 < a < n$ and $1 < b < n$.
Proof: hypothesis for contradiction.
<2>4. In the ring $R$, $(a \cdot 1_R)(b \cdot 1_R) = (ab) \cdot 1_R = n \cdot 1_R = 0_R$.
Proof: ring multiplication of integer multiples of unity.
<2>5. Since $R$ is an integral domain, it has no zero divisors, so $a \cdot 1_R = 0_R$ or $b \cdot 1_R = 0_R$.
Proof: definition of an integral domain.
<2>6. But $1 \le a < n$ and $1 \le b < n$, so $a \cdot 1_R = 0_R$ or $b \cdot 1_R = 0_R$ contradicts the minimality of $n$ in <2>1. Proof: $n$ is the least positive integer annihilating $1_R$.
<2>7. Thus $n$ cannot be composite, so $n$ is prime.
Proof: <2>2 and <2>6.

<1>4. Conclusion: The characteristic of an integral domain is either zero or a prime.
Q.E.D. Proof: <1>2 and <1>3.
:::
