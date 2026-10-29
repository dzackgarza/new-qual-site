---
schema: qual/card@1
id: P-CZEY5
kind: problem
title: The integers $n$ with $\phi(n)=2$ are $3,4,6$
classification:
  areas:
  - algebra
  topics:
  - Number Theory
  - Cyclic Groups
relations: []
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
- event: source-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: 'The source reads "Suppose $\phi(n) = 2$." and asks nothing; the statement asks for every positive integer n with this property, which the title and solution answer.'
review: draft
---

::: {.problem}
Suppose $\phi(n) = 2$. Find all such positive integers $n$.
:::

::: {.solution}
Write $n=\prod_{i=1}^r p_i^{\alpha_i}$ with distinct primes $p_i$ and $\alpha_i\ge1$, so that
$$
\phi(n)=\prod_{i=1}^r p_i^{\alpha_i-1}(p_i-1).
$$

::: pf

::: {.pf-step #factors}

Each factor $p_i^{\alpha_i-1}(p_i-1)$ is $1$ or $2$, and exactly one factor is $2$.

::: pf-proof

The factors are positive integers whose product is $2$.

:::

:::

::: {.pf-step #one}

A factor equals $1$ exactly when $p_i^{\alpha_i}=2$.

::: pf-proof

If $p_i^{\alpha_i-1}(p_i-1)=1$ then $p_i-1=1$ and $\alpha_i-1=0$, so $p_i^{\alpha_i}=2$; conversely $\phi(2)=1$.

:::

:::

::: {.pf-step #two}

A factor equals $2$ exactly when $p_i^{\alpha_i}$ is $3$ or $4$.

::: pf-proof

If $p_i$ is odd then $p_i-1\ge2$ is even, so $p_i-1=2$ and $\alpha_i=1$, giving $p_i^{\alpha_i}=3$.
If $p_i=2$ then $2^{\alpha_i-1}=2$, so $\alpha_i=2$ and $p_i^{\alpha_i}=4$.
Conversely $\phi(3)=\phi(4)=2$.

:::

:::

::: pf-step

$n\in\boxed{\{3,4,6\}}$, and each of these satisfies $\phi(n)=2$.

::: pf-proof

By steps [](#factors){.pf-ref}, [](#one){.pf-ref} and [](#two){.pf-ref}, $n$ has one prime-power factor equal to $3$ or $4$, and at most one further factor, equal to $2$.
The further factor is impossible beside $4$, since $4$ and $2$ are powers of the same prime.
So $n$ is $3$, $4$, or $3\cdot2=6$, and $\phi(3)=\phi(4)=\phi(6)=2$.

:::

:::

:::

:::
