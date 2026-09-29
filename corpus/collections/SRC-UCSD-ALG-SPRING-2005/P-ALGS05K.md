---
schema: qual/card@1
id: P-ALGS05K
kind: problem
title: "In a ring where every element satisfies x^n = x, every prime ideal is maximal"
classification:
  areas:
  - algebra
  topics:
  - Commutative Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
Let $R$ be a commutative ring with identity element.
Suppose that for each $x \in R$ there is an $n(x) > 1$ such that $x^{n(x)} = x$.
Show that every prime ideal of $R$ is maximal.
:::

::: {.solution}

::: pf

::: pf-step

Let $P$ be a prime ideal of $R$, and consider the integral domain $D = R/P$.

::: pf-proof

the quotient of a ring by a prime ideal is an integral domain.

:::

:::

::: pf-step

For each $\bar x \in D$ (with $\bar x \neq 0$), there is $n > 1$ with $\bar x^n = \bar x$.

::: pf-proof

the condition $x^{n(x)} = x$ descends to the quotient.

:::

:::

::: {.pf-step #s3}

Hence $\bar x^{n-1} = 1$ in $D$ (since $\bar x \neq 0$ and $D$ is a domain, we can cancel $\bar x$).

::: pf-proof

$\bar x^n = \bar x$ gives $\bar x(\bar x^{n-1} - 1) = 0$; since $\bar x \neq 0$ and $D$ is a domain, $\bar x^{n-1} = 1$.

:::

:::

::: pf-step

Hence every nonzero element of $D$ is a unit.

::: pf-proof

Step [](#s3){.pf-ref} shows $\bar x$ has inverse $\bar x^{n-2}$.

:::

:::

::: pf-step

Therefore $D$ is a field.

::: pf-proof

an integral domain in which every nonzero element is a unit is a field.

:::

:::

::: {.pf-step #s6}

Hence $P$ is maximal.

::: pf-proof

$R/P$ is a field iff $P$ is maximal.

:::

:::

::: pf-qed

Step [](#s6){.pf-ref}.

:::

:::

:::
