---
schema: qual/card@1
id: P-ALGS14H
kind: problem
title: Irreducible factors of $X^{64}-X$ over $\mathbb{F}_2$ by degree
classification:
  areas:
  - algebra
  topics:
  - Finite Fields
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-08
- event: solution-written
  by: OpenAI
  date: 2026-09-08
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-08
---

::: {.problem}
In the factorization of $X^{64} - X$ into irreducible terms, how many terms of each degree appear over the field $K = \mathbb{F}_2$?
(e.g. $5$ terms of degree $1$, $4$ terms of degree $7$, etc.) Justify your answer, but you do not have to actually find the factorization.
:::

::: {.solution}
Over $\mathbb F_2$, the polynomial
\[
X^{64}-X=X^{2^6}-X
\]
is the product of all monic irreducible polynomials whose degrees divide $6$, each occurring once.
Thus only degrees $1,2,3,$ and $6$ can occur.

::: pf

::: {.pf-step #s1}

Let $N_d$ be the number of monic irreducible polynomials of degree $d$ over $\mathbb F_2$.
Then
\[
2^n=\sum_{d\mid n} dN_d,
\]
because $X^{2^n}-X$ is the product of all monic irreducibles whose degrees divide $n$.

::: pf-proof

The roots of $X^{2^n}-X$ are exactly the elements of $\mathbb F_{2^n}$.
An irreducible polynomial of degree $d$ over $\mathbb F_2$ splits in $\mathbb F_{2^n}$ exactly when $d\mid n$, and contributes its $d$ distinct roots.

:::

:::

::: {.pf-step #s2}

For $d=1$,
\[
2=1\cdot N_1,
\]
so $N_1=2$.

::: pf-proof

The two linear factors are $X$ and $X+1$.

:::

:::

::: {.pf-step #s3}

For $d=2$,
\[
4=N_1+2N_2=2+2N_2,
\]
so $N_2=1$.

::: pf-proof

Apply the formula of step [](#s1){.pf-ref} with $n=2$.

:::

:::

::: {.pf-step #s4}

For $d=3$,
\[
8=N_1+3N_3=2+3N_3,
\]
so $N_3=2$.

::: pf-proof

Apply the formula of step [](#s1){.pf-ref} with $n=3$.

:::

:::

::: {.pf-step #s5}

For $d=6$,
\[
64=N_1+2N_2+3N_3+6N_6
   =2+2+6+6N_6,
\]
so $N_6=9$.

::: pf-proof

The positive divisors of $6$ are $1,2,3,6$.
Substituting the preceding values gives $64=10+6N_6$.

:::

:::

::: pf-step

Therefore the factorization of $X^{64}-X$ over $\mathbb F_2$ contains exactly
\[
\boxed{2\text{ factors of degree }1,\quad
1\text{ of degree }2,\quad
2\text{ of degree }3,\quad
9\text{ of degree }6,}
\]
and no irreducible factors of any other degree.

::: pf-proof

By the factorization theorem in step [](#s1){.pf-ref}, the possible degrees are precisely the divisors of $6$, and the counts are those computed in steps [](#s2){.pf-ref}, [](#s3){.pf-ref}, [](#s4){.pf-ref} and [](#s5){.pf-ref}.

:::

:::

:::

:::
