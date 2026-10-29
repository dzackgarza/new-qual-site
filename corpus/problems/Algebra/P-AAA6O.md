---
schema: qual/card@1
id: P-AAA6O
kind: problem
title: Rational roots of monic polynomials in $\ZZ[x]$ are integers
classification:
  areas:
  - algebra
  topics:
  - Polynomials
  - Factorization
  - Number Theory
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-16
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
Show that if $p(x)\in\ZZ[x]$ is monic and $r\in\QQ$ is a root of $p$, then $r\in\ZZ$.
:::

::: {.solution}
Write $p(x)=x^n+a_{n-1}x^{n-1}+\cdots+a_0$ and $r=a/b$ in lowest terms with $b>0$.

::: pf

::: {.pf-step #divides}

$b\mid a^n$.

::: pf-proof

Multiplying $p(a/b)=0$ by $b^n$ gives
$$
a^n+b(a_{n-1}a^{n-1}+a_{n-2}a^{n-2}b+\cdots+a_0b^{n-1})=0.
$$

:::

:::

::: pf-step

$r\in\ZZ$.

::: pf-proof

Since $\gcd(a,b)=1$, also $\gcd(a^n,b)=1$, so step [](#divides){.pf-ref} forces $b=1$. Therefore $r=a\in\ZZ$.

:::

:::

:::

:::
