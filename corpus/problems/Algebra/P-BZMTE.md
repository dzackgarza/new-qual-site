---
schema: qual/card@1
id: P-BZMTE
kind: problem
title: $\phi(n)$ is even for $n>2$
classification:
  areas:
  - algebra
  topics:
  - Number Theory
  - Roots of Unity
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---


::: {.problem}
Prove that $\varphi(n)$ is even for every integer $n>2$.
:::

::: {.solution}
Write
\[
n=\prod_{i=1}^r p_i^{a_i}.
\]
Then
\[
\varphi(n)=\prod_{i=1}^r p_i^{a_i-1}(p_i-1).
\]

If some prime factor $p_i$ is odd, then $p_i-1$ is even, so the product is even.

Otherwise the only prime divisor of $n$ is $2$, so $n=2^a$. Since $n>2$, one has $a\ge2$, and
\[
\varphi(n)=\varphi(2^a)=2^{a-1},
\]
which is even.

Thus $\varphi(n)$ is even for every $n>2$.
:::
