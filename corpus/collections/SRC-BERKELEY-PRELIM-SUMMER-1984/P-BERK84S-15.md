---
schema: qual/card@1
id: P-BERK84S-15
kind: problem
title: Factorization over the field with three elements
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 15 of the vendored Berkeley Preliminary Exam, Summer 1984.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Verified the root x=2, the quotient, and irreducibility of the quadratic by its nonsquare discriminant in F_3.
---

::: {.problem}
Let $\mathbb { Z } _ { 3 }$ be the field of integers mod 3 and $\mathbb { Z } _ { 3 } [ x ]$ the corresponding polynomial ring. Decompose $x ^ { 3 } + x + 2$ into irreducible factors in $\mathbb { Z } _ { 3 } [ x ]$
:::

::: {.solution}
Let
\[
f(x)=x^3+x+2\in\mathbf F_3[x].
\]

::: pf

::: pf-step

The element $2\in\mathbf F_3$ is a root.

::: pf-proof

Modulo $3$,
\[
f(2)=2^3+2+2=12\equiv0.
\]
Hence $x-2=x+1$ divides $f(x)$.

:::

:::

::: pf-step

Dividing by $x+1$ gives
\[
f(x)=(x+1)(x^2+2x+2).
\]

::: pf-proof

A direct multiplication in $\mathbf F_3[x]$ gives
\[
(x+1)(x^2+2x+2)
=x^3+3x^2+4x+2
=x^3+x+2.
\]

:::

:::

::: pf-step

The quadratic factor is irreducible over $\mathbf F_3$.

::: pf-proof

Its discriminant is
\[
\Delta=2^2-4\cdot2=4-8=-4\equiv2\pmod3.
\]
The only squares in $\mathbf F_3$ are $0$ and $1$, so $2$ is not a square. Therefore $x^2+2x+2$ has no root in $\mathbf F_3$, and a quadratic over a field with no root is irreducible.

:::

:::

:::

Thus the irreducible factorization is
\[
\boxed{x^3+x+2=(x+1)(x^2+2x+2)}.
\]
:::
