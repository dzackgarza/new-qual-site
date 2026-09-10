---
schema: qual/card@1
id: P-F05BN
kind: problem
title: Binomial theorem and $(x+y)^p \equiv x^p+y^p \pmod{p}$
classification:
  areas:
  - prelim
  topics:
  - Number Theory
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: problem
i) State the binomial theorem.

ii) Prove that if $p$ is a prime number, then $(x+y)^p \equiv x^p + y^p \pmod p$.
:::

::: solution
The binomial theorem states that for every nonnegative integer $n$,
\[
(x+y)^n=\sum_{k=0}^n\binom nk x^{n-k}y^k.
\]

Let $p$ be prime. For $1\le k\le p-1$,
\[
\binom pk=\frac{p!}{k!(p-k)!}
\]
is divisible by $p$: the numerator contains the prime factor $p$, while neither $k!$ nor $(p-k)!$ does. Hence modulo $p$ every intermediate binomial coefficient vanishes. Therefore, as a polynomial identity over $\mathbb Z/p\mathbb Z$,
\[
(x+y)^p\equiv x^p+y^p\pmod p.
\]
In particular the congruence holds after substituting any integers for $x$ and $y$.
:::
