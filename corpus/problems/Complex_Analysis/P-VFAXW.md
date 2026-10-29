---
schema: qual/card@1
id: P-VFAXW
kind: problem
title: Invert $1-z$, one coefficient at a time
classification:
  areas:
  - complex-analysis
  topics:
  - Power Series
relations: []
review: draft
audit:
- event: statement-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: 'The source reads "Use this formulation to show that if $A(z)= 1-z$ then $1/A(z) = \sum z^k$", referring to a recursion stated earlier in the source; the statement now states that recursion.'
---

::: {.exercise}
If $A(z) = \sum_{k \geq 0} a_k z^k$ is a power series with $a_0 \neq 0$, then $1/A(z) = \sum_{k \geq 0} b_k z^k$, where $b_0 = 1/a_0$ and $b_n = -\frac{1}{a_0}\sum_{k=1}^{n} a_k b_{n-k}$ for $n \geq 1$.
Use this formulation to show that if $A(z)= 1-z$ then $1/A(z) = \sum z^k$.
:::

::: {.solution}
Here $a_0 = 1$, $a_1 = -1$, and $a_k = 0$ for $k \geq 2$, so the recursion reads $b_0 = 1$ and $b_n = b_{n-1}$ for $n \geq 1$.

::: pf

::: {.pf-step #all-one}

$b_n = 1$ for every $n \geq 0$.

::: pf-proof

By induction on $n$: $b_0 = 1/a_0 = 1$, and for $n \geq 1$, $b_n = -(a_1 b_{n-1}) = b_{n-1} = 1$.

:::

:::

::: pf-step

$\dfrac{1}{1-z} = \boxed{\sum_{k \geq 0} z^k}$.

::: pf-proof

This is the series $\sum b_k z^k$ with the coefficients of step [](#all-one){.pf-ref}.

:::

:::

:::

:::
