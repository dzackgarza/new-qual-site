---
schema: qual/card@1
id: E-TYPSR
kind: problem
title: An entire function with bounded $n$th derivative is a polynomial of degree
  at most $n$
classification:
  areas:
  - complex-analysis
  topics:
  - Liouville's Theorem
  - Entire Functions
  - Polynomials
relations: []
review: draft
---

::: {.exercise}
Suppose $f$ is entire and $f^{(n)}$ is bounded on $\CC$.
Show that $f$ is a polynomial of degree at most $n$.
:::

::: {.solution}

::: pf

::: {.pf-step #constant}
$f^{(n)}$ is constant, so $f^{(k)}\equiv 0$ for all $k>n$.

::: pf-proof
$f^{(n)}$ is entire and bounded, hence constant by Liouville's theorem.
:::

:::

::: pf-step
$f$ is a polynomial of degree at most $n$.

::: pf-proof
The Taylor series $f(z) = \sum_{k\geq 0}\frac{f^{(k)}(0)}{k!}z^k$ converges on $\CC$, and by step [](#constant){.pf-ref} its terms with $k>n$ vanish.
:::

:::

:::

:::
