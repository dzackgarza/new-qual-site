---
schema: qual/card@1
id: P-BXBHJ
kind: problem
title: Euler totient of primes and composites
classification:
  areas:
  - algebra
  topics:
  - Number Theory
  - Cyclic Groups
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

::: problem
- How do you compute the totient $\phi(p)$ for $p$ prime?
  Or $\phi(n)$ for $n$ composite?
:::


::: {.solution}
<1>1. If $p$ is prime, then
\[
\varphi(p)=p-1.
\]
::: {.proof}
Every nonzero residue modulo $p$ is relatively prime to $p$, so the invertible residue classes are exactly $1,2,\ldots,p-1$.
:::

<1>2. For a prime power $p^a$ with $a\ge1$,
\[
\varphi(p^a)=p^a-p^{a-1}=p^{a-1}(p-1).
\]
::: {.proof}
Among the $p^a$ residue classes modulo $p^a$, exactly the $p^{a-1}$ multiples of $p$ fail to be relatively prime to $p^a$.
:::

<1>3. Euler's totient is multiplicative on coprime integers.
::: {.proof}
If $\gcd(m,n)=1$, the Chinese remainder theorem gives
\[
\ZZ/mn\ZZ\cong \ZZ/m\ZZ\times\ZZ/n\ZZ.
\]
Taking unit groups gives
\[
(\ZZ/mn\ZZ)^\times\cong(\ZZ/m\ZZ)^\times\times(\ZZ/n\ZZ)^\times,
\]
so
\[
\varphi(mn)=\varphi(m)\varphi(n).
\]
:::

<1>4. Therefore, if
\[
n=\prod_{i=1}^r p_i^{a_i}
\]
is the prime factorization, then
\[
\varphi(n)=\prod_{i=1}^r p_i^{a_i-1}(p_i-1)
=n\prod_{p\mid n}\left(1-\frac1p\right).
\]
::: {.proof}
Apply <1>2 to each prime-power factor and then <1>3.
:::
:::
