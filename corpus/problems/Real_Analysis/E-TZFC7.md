---
schema: qual/card@1
id: E-TZFC7
kind: problem
title: Uniform limits preserve boundedness and continuity
classification:
  areas:
  - real-analysis
  topics:
  - Uniform Convergence
  - Continuity
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.exercise}
- Show that a uniform limit of bounded functions is bounded.

- Show that a uniform limit of continuous function is continuous.

  - I.e. if $f_n\to f$ uniformly with each $f_n$ continuous then $f$ is continuous.
:::

::: {.solution}
Let $f_n \to f$ uniformly on a set $E$.

::: pf

::: {.pf-step #s1}

If each $f_n$ is bounded, then $f$ is bounded.

::: pf-proof

Uniform convergence with $\eps = 1$ gives $N$ with $\|f - f_N\|_\infty \le 1$. By the triangle inequality, $|f(x)| \le |f_N(x)| + 1 \le \|f_N\|_\infty + 1$ for every $x \in E$.

:::

:::

::: {.pf-step #s2}

If each $f_n$ is continuous, then $f$ is continuous.

::: pf-proof

::: {.pf-step #s2-1}

Fix $x_0 \in E$ and $\eps > 0$. There are $n$ with $\|f - f_n\|_\infty < \eps/3$ and $\delta > 0$ with $|f_n(x) - f_n(x_0)| < \eps/3$ whenever $x \in E$ and $|x - x_0| < \delta$.

::: pf-proof

The first is uniform convergence and the second is continuity of $f_n$ at $x_0$.

:::

:::

::: pf-qed

For $x \in E$ with $|x - x_0| < \delta$, the triangle inequality and step [](#s2-1){.pf-ref} give $|f(x) - f(x_0)| \le |f(x) - f_n(x)| + |f_n(x) - f_n(x_0)| + |f_n(x_0) - f(x_0)| < \eps$. So $f$ is continuous at the arbitrary point $x_0$.

:::

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref} and [](#s2){.pf-ref}.

:::

:::

:::
