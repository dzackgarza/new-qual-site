---
schema: qual/card@1
id: P-YR75I
kind: problem
title: Entire functions converging uniformly on line segments converge uniformly on
  compacta
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
  - Uniform Convergence
  - Sequences of Functions
  - Normal Families
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.problem}
Suppose $\theset{f_n}_{n\in \NN}$ is a sequence of entire functions where

- $f_n \to g$ pointwise for some $g:\CC\to\CC$.

- On every line segment in $\CC$, $f_n \to g$ uniformly.

Show that

- $g$ is entire, and

- $f_n\to g$ uniformly on every compact subset of $\CC$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

$g$ is holomorphic on $\CC$.

::: pf-proof

::: pf-step

It suffices to show $\oint_\gamma g = 0$ for every closed polygonal path $\gamma$.

::: pf-proof

This is Morera's theorem.

:::

:::

::: {.pf-step #s1-2}

For a closed polygonal path $\gamma$ (a finite union of line segments), $\int_\gamma g = \lim_n \int_\gamma f_n$.

::: pf-proof

$\gamma$ is a finite union of line segments; on each, $f_n \to g$ uniformly by hypothesis, so the integrals converge.

:::

:::

::: pf-step

$\int_\gamma g = 0$.

::: pf-proof

Each $f_n$ is entire, so $\oint_\gamma f_n = 0$ (Cauchy's theorem); step [](#s1-2){.pf-ref} gives the limit $0$.

:::

:::

:::

:::

::: {.pf-step #s2}

$f_n \to g$ uniformly on compact sets.

::: pf-proof

::: pf-step

Let $K \subset \CC$ be compact; choose a bounded polygonal domain $\Omega$ with $K \subset \Omega$ and $\dist(K, \bd\Omega) > 0$.

::: pf-proof

Take a large open square containing $K$; its boundary is a finite union of line segments.

:::

:::

::: {.pf-step #s2-2}

For $z \in K$: $f_n(z) - g(z) = \frac{1}{2\pi i}\oint_{\bd\Omega} \frac{f_n(\zeta) - g(\zeta)}{\zeta - z}\, d\zeta$.

::: pf-proof

Cauchy integral formula applied to the holomorphic functions $f_n$ and $g$ (entire by step [](#s1){.pf-ref}) on the domain $\Omega$.

:::

:::

::: pf-step

$\sup_{z \in K}\abs{f_n(z) - g(z)} \le \frac{\operatorname{length}(\bd\Omega)}{2\pi\, d} \sup_{\zeta \in \bd\Omega}\abs{f_n(\zeta) - g(\zeta)}$ where $d = \dist(K, \bd\Omega)$.

::: pf-proof

Bound the integral in step [](#s2-2){.pf-ref}, using $\abs{\zeta - z} \ge d$.

:::

:::

::: pf-step

The right-hand side tends to $0$.

::: pf-proof

$\bd\Omega$ is a finite union of line segments, and $f_n \to g$ uniformly on each, so $\sup_{\bd\Omega}\abs{f_n - g} \to 0$.

:::

:::

:::

:::

:::

:::
