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

::: {.problem}
If $R$ is a UFD, is $R[x]$ again a UFD?
:::

::: {.solution}
Let $K=\Frac(R)$. For nonzero $f\in R[x]$ write $f=c(f)f_0$, where the content $c(f)\in R$ is a gcd of the coefficients, defined up to a unit, and $f_0$ is primitive.

::: pf

::: {.pf-step #gauss}
A product of primitive polynomials is primitive, and a primitive $f\in R[x]$ of positive degree is irreducible in $R[x]$ if and only if it is irreducible in $K[x]$.

::: pf-proof
This is Gauss's lemma. For the first claim, if a prime $\pi$ of $R$ divided every coefficient of $gh$, then $gh=0$ in the domain $(R/\pi)[x]$, so $\pi$ divides $g$ or $h$. For the second, if $f=gh$ in $K[x]$, clearing denominators and taking contents with the first claim gives $f=u\,g_0h_0$ with $u\in R^\times$, a factorization in $R[x]$ of the same degrees.
:::

:::

::: {.pf-step #exist}
Every nonzero nonunit of $R[x]$ is a product of irreducibles.

::: pf-proof
Write $f=c(f)f_0$. The content factors into primes of $R$, which remain irreducible in $R[x]$. Factor $f_0$ in the PID $K[x]$ into irreducibles and, as in step [](#gauss){.pf-ref}, rescale the factors to primitive polynomials of $R[x]$ whose product is $f_0$ up to a unit of $R$; each is irreducible in $R[x]$ by step [](#gauss){.pf-ref}.
:::

:::

::: pf-step
$\boxed{\text{Yes}}$: $R[x]$ is a UFD, and by induction so is $R[x_1,\ldots,x_n]$.

::: pf-proof
By step [](#exist){.pf-ref}, factorizations exist. The irreducibles of $R[x]$ are the primes of $R$ and the primitive polynomials irreducible in $K[x]$. Given two factorizations of $f$, the products of the constant factors both equal $c(f)$ up to a unit, by step [](#gauss){.pf-ref}, so they agree up to units and order because $R$ is a UFD. The products of the primitive factors both equal $f_0$ up to a unit of $R$, so they agree up to units of $K$ and order because $K[x]$ is a UFD; two primitive polynomials that differ by a unit of $K$ differ by a unit of $R$.
:::

:::

:::

:::
