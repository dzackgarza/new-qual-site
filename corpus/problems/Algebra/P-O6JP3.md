---
schema: qual/card@1
id: P-O6JP3
kind: problem
title: Polynomial rings over integral domains are integral domains
classification:
  areas:
  - algebra
  topics:
  - Integral Domains
  - Polynomials
  - Rings
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-16
- event: solution-written
  by: openai-gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Prove that if $R$ is an integral domain, then $R[t]$ is again an integral domain.
:::

::: {.solution}

::: pf

::: {.pf-step #no-zero-divisors}

If $f,g\in R[t]$ are nonzero, then $fg\neq0$ and $\deg(fg)=\deg f+\deg g$.

::: pf-proof

Write
$$
f(t)=a_nt^n+\cdots+a_0,\qquad g(t)=b_mt^m+\cdots+b_0
$$
with $a_n,b_m\neq0$. The coefficient of $t^{n+m}$ in $fg$ is $a_nb_m$, and every other coefficient of $fg$ belongs to a lower power of $t$. Since $R$ is an integral domain, $a_nb_m\neq0$.

:::

:::

::: pf-step

$R[t]$ is an integral domain.

::: pf-proof

$R[t]$ is a commutative ring with $1\neq0$ because $R$ is, and by step [](#no-zero-divisors){.pf-ref} it has no nonzero zero divisors.

:::

:::

:::

:::
