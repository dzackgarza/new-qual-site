---
schema: qual/card@1
id: P-3IRB7
kind: problem
title: Whether $k[x_1,\ldots,x_n]$ is a PID
classification:
  areas:
  - algebra
  topics:
  - Principal Ideal Domains
  - Polynomials
  - Ideals
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Removed the false zero-constant-term description of (x1,x2) for n>2 and kept the common-divisor proof.
---

::: {.exercise}
For which $n$ is the polynomial ring $k[x_1,\dots,x_n]$ over a field $k$ a PID?
:::

::: {.solution}
For $n=0$, the ring is the field $k$, hence a PID. For $n=1$, the ring $k[x_1]$ is Euclidean, hence a PID.

Assume $n\ge2$ and consider
\[
I=(x_1,x_2).
\]
This is proper: evaluation at $x_1=x_2=0$ sends every element of $I$ to $0$, while it sends $1$ to $1$.

Suppose $I=(d)$ were principal. Since $x_1,x_2\in(d)$, the polynomial $d$ divides both $x_1$ and $x_2$. In the UFD $k[x_1,\dots,x_n]$, the irreducibles $x_1$ and $x_2$ are nonassociate, so their only common divisors are units. Thus $d$ is a unit, which would give
\[
I=(1),
\]
contradicting properness.

Therefore $k[x_1,\dots,x_n]$ is a PID exactly for $n\le1$.
:::
