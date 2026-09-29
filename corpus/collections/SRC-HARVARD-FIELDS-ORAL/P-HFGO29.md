---
schema: qual/card@1
id: P-HFGO29
kind: problem
title: A finite simple field extension is algebraic
classification:
  areas: [algebra]
  topics: [Field Theory]
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: source-checked
  by: OpenAI
  date: 2026-09-10
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-10
---

::: {.problem}
If $F(a)/F$ is a finite field extension, prove that $a$ is algebraic over $F$.
:::

::: {.solution}

::: pf

::: pf-step

$F(a)$ is a finite-dimensional $F$-vector space.

::: pf-proof

$F(a)/F$ is finite by hypothesis, so $[F(a) : F] = n < \infty$.

:::

:::

::: pf-step

The set $\theset{1, a, a^2, \dots, a^n}$ is linearly dependent over $F$.

::: pf-proof

it has $n+1$ elements in an $n$-dimensional vector space.

:::

:::

::: {.pf-step #s3}

There is a nonzero polynomial $p \in F[x]$ with $p(a) = 0$.

::: pf-proof

linear dependence gives $c_0 + c_1 a + \cdots + c_n a^n = 0$ with not all $c_i = 0$; take $p(x) = c_0 + c_1 x + \cdots + c_n x^n$.

:::

:::

::: {.pf-step #s4}

$a$ is algebraic over $F$.

::: pf-proof

by definition, $a$ is algebraic over $F$ iff it is a root of some nonzero polynomial in $F[x]$, which is step [](#s3){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} is the claim.

:::

:::

:::
