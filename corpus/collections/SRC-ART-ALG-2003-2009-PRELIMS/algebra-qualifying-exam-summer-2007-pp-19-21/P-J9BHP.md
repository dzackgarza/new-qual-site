---
schema: qual/card@1
id: P-J9BHP
kind: problem
title: The characteristic of an integral domain is zero or prime
classification:
  areas:
  - algebra
  topics:
  - Integral Domains
  - Characteristic
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Show that the characteristic of an integral domain must be either zero or a prime.
:::

::: {.solution}
Let $R$ be an integral domain, so $1_R\ne0_R$ and $R$ has no zero divisors, and let $n=\operatorname{char}(R)$: either $n=0$, or $n$ is the least positive integer with $n\cdot1_R=0_R$.

::: pf

::: {.pf-step #s1}

If $n>0$, then $n\ge2$.

::: pf-proof

$1\cdot1_R=1_R\ne0_R$.

:::

:::

::: {.pf-step #s2}

If $n>0$, then $n$ is prime.

::: pf-proof

Suppose $n=ab$ with integers $1<a,b<n$.
Then $(a\cdot1_R)(b\cdot1_R)=(ab)\cdot1_R=n\cdot1_R=0_R$, so $a\cdot1_R=0_R$ or $b\cdot1_R=0_R$ because $R$ has no zero divisors.
Either equality contradicts the minimality of $n$.
Hence $n$, which is at least $2$ by step [](#s1){.pf-ref}, has no factorization into smaller integers greater than $1$, so $n$ is prime.

:::

:::

::: pf-qed

Either $n=0$, or $n>0$ and $n$ is prime by step [](#s2){.pf-ref}.

:::

:::

:::
