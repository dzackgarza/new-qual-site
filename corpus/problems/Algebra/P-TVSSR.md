---
schema: qual/card@1
id: P-TVSSR
kind: problem
title: Galois group of $x^3+6x+3$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Polynomials
  - Permutations
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
Compute the Galois group of the cubic polynomial $f(x) = x^3 + 6x + 3$ over $\QQ$.
:::

::: {.solution}

::: pf

::: {.pf-step #transitive}
$\Gal(f/\QQ)$ is $A_3$ or $S_3$.

::: pf-proof
$f$ is Eisenstein at $3$, hence irreducible over $\QQ$, so its Galois group is a transitive subgroup of $S_3$.
:::

:::

::: {.pf-step #discriminant}
The discriminant of $f$ is $-1107=-3^3\cdot41$, which is not a square in $\QQ$.

::: pf-proof
The discriminant of $x^3+px+q$ is $-4p^3-27q^2$, which here is $-4\cdot6^3-27\cdot3^2=-864-243=-1107$.
It is negative, so it is not a rational square.
:::

:::

::: pf-step
$\Gal(f/\QQ)\cong\boxed{S_3}$.

::: pf-proof
For an irreducible cubic, the Galois group lies in $A_3$ exactly when the discriminant is a square, so steps [](#transitive){.pf-ref} and [](#discriminant){.pf-ref} give $S_3$.
:::

:::

:::

:::

::: {.remark}
Alternatively, $f'(x)=3x^2+6>0$, so $f$ has one real root and a pair of nonreal conjugate roots, and complex conjugation is a transposition in the transitive Galois group.
:::
