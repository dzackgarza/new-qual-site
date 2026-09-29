---
schema: qual/card@1
id: P-CASP26A
kind: problem
title: "The series of f^{(n)}/n! defines an entire function"
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
  - Taylor Series
  - Convergence
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
Let $f$ be an entire function (i.e., analytic in the entire complex plane $\mathbb{C}$). Show that the series
$$
g(z) := \sum_{n=0}^\infty \frac{1}{n!} f^{(n)}(z)
$$
defines an entire function $g$.
:::

::: {.solution}
**Goal.** Show $g(z) = \sum_{n=0}^\infty \frac{1}{n!} f^{(n)}(z)$ is entire.

::: pf

::: pf-step
$f$ is entire, so it has a Taylor expansion $f(w) = \sum_{n=0}^\infty \frac{f^{(n)}(z)}{n!}(w - z)^n$ valid for all $w$ (entire).

::: pf-proof
an entire function has a Taylor series with infinite radius of convergence about every point.
:::

:::

::: pf-step
$g(z) = \sum_{n=0}^\infty \frac{f^{(n)}(z)}{n!} = f(z + 1)$.

::: pf-proof

::: {.pf-step #s2-1}
Evaluate the Taylor series of $f$ at $w = z + 1$: $f(z+1) = \sum_{n=0}^\infty \frac{f^{(n)}(z)}{n!}(1)^n = \sum_{n=0}^\infty \frac{f^{(n)}(z)}{n!}$.

::: pf-proof
substitute $w = z + 1$ into the Taylor expansion about $z$.
:::

:::

::: pf-step
Hence $g(z) = f(z+1)$.

::: pf-proof
step [](#s2-1){.pf-ref}.
:::

:::

:::

:::

::: {.pf-step #s3}
$g(z) = f(z+1)$ is entire.

::: pf-proof
the composition of the entire function $f$ with the affine map $z \mapsto z + 1$ is entire.
:::

:::

::: pf-qed
step [](#s3){.pf-ref} shows $g$ is entire.
:::

:::
:::
