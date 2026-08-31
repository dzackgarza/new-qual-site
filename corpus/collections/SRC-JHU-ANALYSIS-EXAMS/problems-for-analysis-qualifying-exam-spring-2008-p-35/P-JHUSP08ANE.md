---
schema: qual/card@1
id: P-JHUSP08ANE
kind: problem
title: "Entire functions bounded by a nonvanishing entire function are constant multiples"
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
  - Liouville's Theorem
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

5) Prove the following statement: If f and g are entire functions, $g ( z ) \neq 0$ and $| f ( z ) | \leq | g ( z ) |$ for all $z \in \mathbf { C } .$ , then $f ( z ) = C g ( z )$ for some constant C.

::: {.solution}
<1>1. $h(z) = f(z)/g(z)$ is entire.
::: {.proof}
$g(z) \neq 0$ for all $z$, so $f/g$ has no singularities, and $f$ and $g$ are entire.
:::

<1>2. $|h(z)| = |f(z)/g(z)| \le 1$ for all $z$.
::: {.proof}
hypothesis $|f(z)| \le |g(z)|$.
:::

<1>3. Hence $h$ is a bounded entire function.
::: {.proof}
<1>2.
:::

<1>4. By Liouville's theorem, $h$ is constant, say $h(z) = C$ with $|C| \le 1$.
::: {.proof}
<1>3.
:::

<1>5. Therefore $f(z) = C g(z)$.
::: {.proof}
<1>1 and <1>4.
:::

<1>6. Q.E.D.
::: {.proof}
<1>5.
:::
:::
