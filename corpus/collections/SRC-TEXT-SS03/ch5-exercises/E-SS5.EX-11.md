---
schema: qual/card@1
id: E-SS5.EX-11
kind: problem
title: "Picard's little theorem for entire functions of finite order"
classification:
  areas:
  - complex-analysis
  topics: ['Entire Functions', 'Hadamard Factorization', "Jensen's Formula"]
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.exercise}
11. Show that if f is an entire function of finite order that omits two values, then f is constant.
    This result remains true for any entire function and is known as Picard’s little theorem.

[Hint: If f misses a, then $f ( z ) - a$ is of the form $e ^ { p ( z ) }$ where p is a polynomial.]
:::

::: {.solution}
Suppose the entire function $f$ has finite order and omits two distinct values $a,b\in\mathbb C$.

Since $f-a$ is an entire finite-order function with no zeros, Hadamard's factorization theorem implies
\[
f(z)-a=e^{P(z)}
\]
for some polynomial $P$.

If $P$ were nonconstant, choose any logarithm $\lambda$ of the nonzero number $b-a$, so
\[
e^\lambda=b-a.
\]
A nonconstant complex polynomial assumes every complex value: by the fundamental theorem of algebra, $P(z)-\lambda$ has a root. Thus there would be $z_0$ with $P(z_0)=\lambda$, and then
\[
f(z_0)-a=e^{P(z_0)}=b-a,
\]
so $f(z_0)=b$, contradicting that $f$ omits $b$.

Therefore $P$ is constant, and consequently $f$ is constant.
:::
