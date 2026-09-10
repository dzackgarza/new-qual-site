---
schema: qual/card@1
id: P-RPXS4
kind: problem
title: The number of irreducible polynomials of degree $4$ over $\FF_2$
classification:
  areas:
  - algebra
  topics:
  - Finite Fields
  - Irreducibility Criteria
  - Factorization
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
How many irreducible polynomials are there of degree 4 over \( \FF_2 \)?
:::

::: {.solution}
Let $N_q(n)$ denote the number of monic irreducible polynomials of degree $n$ over $\mathbb F_q$. From
\[
x^{q^n}-x=\prod_{d\mid n}\prod_{\substack{f\text{ monic irreducible}\\ \deg f=d}}f(x)
\]
we get
\[
q^n=\sum_{d\mid n}d\,N_q(d).
\]
Möbius inversion gives
\[
N_q(n)=\frac1n\sum_{d\mid n}\mu(d)q^{n/d}.
\]
Hence
\[
N_2(4)=\frac14\bigl(2^4-2^2\bigr)=3,
\]
because $\mu(4)=0$.

Thus there are exactly
\[
\boxed{3}
\]
monic irreducible quartics over $\mathbb F_2$.
:::
