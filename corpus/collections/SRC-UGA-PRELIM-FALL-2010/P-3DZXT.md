---
schema: qual/card@1
id: P-3DZXT
kind: problem
title: The binomial theorem, $(x+y)^5\equiv x^5+y^5\pmod{5}$, and $(x+y)^{5^n}\equiv
  x^{5^n}+y^{5^n}\pmod{5}$
classification:
  areas:
  - prelim
  topics:
  - Induction
  - Combinatorics
  - Number Theory
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
a. State the binomial theorem.
b. Prove that $(x+y)^5 \equiv x^5 + y^5 \pmod 5$.
c. Prove by mathematical induction that $(x+y)^{5^n} \equiv x^{5^n} + y^{5^n} \pmod 5$ for every $n \in \mathbb{N}$.
:::

::: {.solution}
The binomial theorem states
\[
(x+y)^m=\sum_{j=0}^m\binom mj x^{m-j}y^j.
\]
For $m=5$, each intermediate binomial coefficient $\binom5j$, $1\le j\le4$, is divisible by $5$. Hence
\[
(x+y)^5\equiv x^5+y^5\pmod5.
\]

We prove the final congruence by induction on $n$. The case $n=1$ is the preceding identity. If
\[
(x+y)^{5^n}\equiv x^{5^n}+y^{5^n}\pmod5,
\]
then raising both sides to the fifth power preserves congruence, and applying the case $m=5$ with $X=x^{5^n}$ and $Y=y^{5^n}$ gives
\[
(x+y)^{5^{n+1}}
\equiv (x^{5^n}+y^{5^n})^5
\equiv x^{5^{n+1}}+y^{5^{n+1}}\pmod5.
\]
Thus the claim holds for every $n\ge1$.
:::
