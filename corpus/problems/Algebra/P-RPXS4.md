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

::: {.problem}
How many irreducible polynomials are there of degree 4 over $\FF_2$?
:::

::: {.solution}
Let $N_q(n)$ be the number of monic irreducible polynomials of degree $n$ over $\FF_q$. Over $\FF_2$ the only unit is $1$, so every irreducible polynomial is monic.

::: pf

::: {.pf-step #count}
$q^n=\sum_{d\mid n}d\,N_q(d)$.

::: pf-proof
$x^{q^n}-x$ is the product of all monic irreducible polynomials over $\FF_q$ whose degree divides $n$, each once. Compare degrees.
:::

:::

::: pf-step
$N_2(4)=\boxed{3}$.

::: pf-proof
By step [](#count){.pf-ref} with $q=2$: $N_2(1)=2$, $2+2N_2(2)=4$ gives $N_2(2)=1$, and $2+2\cdot1+4N_2(4)=16$ gives $N_2(4)=3$. They are $x^4+x+1$, $x^4+x^3+1$ and $x^4+x^3+x^2+x+1$.
:::

:::

:::
:::
