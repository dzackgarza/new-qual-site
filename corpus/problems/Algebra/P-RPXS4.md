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
<1>1. The number of monic irreducible polynomials of degree $n$ over $\FF_q$ is
$$N_q(n) = \frac{1}{n}\sum_{d \mid n} \mu(d)\, q^{n/d}.$$
::: {.proof}
standard formula (Möbius inversion on the factorization $x^{q^n} - x = \prod_{d \mid n} \prod_{\text{irred. deg } d} f$).
:::

<1>2. For $q = 2$, $n = 4$: the divisors of $4$ are $1, 2, 4$, with $\mu(1) = 1$, $\mu(2) = -1$, $\mu(4) = 0$.
::: {.proof}
values of the Möbius function.
:::

<1>3. Hence $N_2(4) = \frac{1}{4}(2^4 - 2^2 + 0) = \frac{1}{4}(16 - 4) = 3$.
::: {.proof}
<1>1 and <1>2.
:::

<1>4. Q.E.D.
::: {.proof}
there are $3$ irreducible polynomials of degree $4$ over $\FF_2$ (<1>3).
:::
:::
