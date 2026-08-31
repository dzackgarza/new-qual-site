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

::: problem
Let $f$ be an entire function (i.e., analytic in the entire complex plane $\mathbb{C}$). Show that the series
$$
g(z) := \sum_{n=0}^\infty \frac{1}{n!} f^{(n)}(z)
$$
defines an entire function $g$.
:::

::: {.solution}
**Goal.** Show $g(z) = \sum_{n=0}^\infty \frac{1}{n!} f^{(n)}(z)$ is entire.

<1>1. $f$ is entire, so it has a Taylor expansion $f(w) = \sum_{n=0}^\infty \frac{f^{(n)}(z)}{n!}(w - z)^n$ valid for all $w$ (entire).
::: {.proof}
an entire function has a Taylor series with infinite radius of convergence about every point.
:::

<1>2. $g(z) = \sum_{n=0}^\infty \frac{f^{(n)}(z)}{n!} = f(z + 1)$.
<2>1. Evaluate the Taylor series of $f$ at $w = z + 1$: $f(z+1) = \sum_{n=0}^\infty \frac{f^{(n)}(z)}{n!}(1)^n = \sum_{n=0}^\infty \frac{f^{(n)}(z)}{n!}$.
::: {.proof}
substitute $w = z + 1$ into the Taylor expansion about $z$.
:::
<2>2. Hence $g(z) = f(z+1)$.
::: {.proof}
<1>2.1.
:::

<1>3. $g(z) = f(z+1)$ is entire.
::: {.proof}
the composition of the entire function $f$ with the affine map $z \mapsto z + 1$ is entire.
:::

<1>4. Q.E.D.
::: {.proof}
<1>3 shows $g$ is entire.
:::
:::
