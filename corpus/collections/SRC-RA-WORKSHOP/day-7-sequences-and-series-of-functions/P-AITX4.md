---
schema: qual/card@1
id: P-AITX4
kind: problem
title: If $f:[0,1]\to\mathbb{R}$ is
classification:
  areas:
  - real-analysis
  topics:
  - Convergence of Integrals
  - Continuity
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
If $f:[0,1]\to\mathbb{R}$ is continuous, prove that $$\displaystyle\lim_{n\to\infty}\int_0^1 f(x^n)\,dx=f(0).$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

$f(x^n) \to f(0)$ pointwise for every $x \in [0,1)$.

::: pf-proof

$x^n \to 0$ for $0 \le x < 1$; $f$ is continuous, so $f(x^n) \to f(0)$.

:::

:::

::: {.pf-step #s2}

$f(x^n) \to f(0)$ for almost every $x \in [0,1]$.

::: pf-proof

Step [](#s1){.pf-ref} covers all $x$ except $x = 1$, a null set.

:::

:::

::: {.pf-step #s3}

The family is dominated: $|f(x^n)| \le \|f\|_\infty$ for all $n$ and all $x$.

::: pf-proof

$f$ is continuous on the compact interval $[0,1]$, hence bounded; $x^n \in [0,1]$.

:::

:::

::: pf-qed

dominated convergence (steps [](#s2){.pf-ref} and [](#s3){.pf-ref}) gives $\lim_n\int_0^1 f(x^n)\,dx = \int_0^1 f(0)\,dx = f(0)$.

:::

:::

:::
