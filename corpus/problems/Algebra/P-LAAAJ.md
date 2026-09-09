---
schema: qual/card@1
id: P-LAAAJ
kind: problem
title: Whether $R$ a UFD implies $R[x]$ a UFD
classification:
  areas:
  - algebra
  topics:
  - Factorization
  - Polynomials
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
If $R$ is a UFD, is $R[x]$ again a UFD?
:::

::: {.solution}
Yes. This is Gauss's lemma.

Let $K=\operatorname{Frac}(R)$. For a nonzero polynomial $f\in R[x]$, write
\[
f=c(f)f_0,
\]
where $c(f)\in R$ is the content (a gcd of the coefficients, defined up to a unit) and $f_0$ is primitive.

Gauss's lemma says:

1. the product of primitive polynomials is primitive;
2. if a primitive polynomial in $R[x]$ factors in $K[x]$, then it factors in $R[x]$ after multiplying the factors by units of $K$.

Since $K[x]$ is a PID and therefore a UFD, every primitive polynomial factors uniquely into irreducibles in $K[x]$. By Gauss's lemma, these factors may be chosen primitive in $R[x]$, and irreducibility over $K$ agrees with irreducibility for primitive polynomials over $R$.

The content $c(f)$ factors uniquely in the UFD $R$. Combining the factorization of the content with the primitive factorization gives unique factorization in $R[x]$.

Therefore
\[
R\text{ UFD}\quad\Longrightarrow\quad R[x]\text{ UFD}.
\]
By induction, the same holds for $R[x_1,\ldots,x_n]$.
:::
