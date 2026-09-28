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

<1>1. If each $f_n$ is bounded, then $f$ is bounded.

::: {.proof}
Uniform convergence with $\eps = 1$ gives $N$ with $\|f - f_N\|_\infty \le 1$. By the triangle inequality, $|f(x)| \le |f_N(x)| + 1 \le \|f_N\|_\infty + 1$ for every $x \in E$.
:::

<1>2. If each $f_n$ is continuous, then $f$ is continuous.

<2>1. Fix $x_0 \in E$ and $\eps > 0$. There are $n$ with $\|f - f_n\|_\infty < \eps/3$ and $\delta > 0$ with $|f_n(x) - f_n(x_0)| < \eps/3$ whenever $x \in E$ and $|x - x_0| < \delta$.

::: {.proof}
The first is uniform convergence and the second is continuity of $f_n$ at $x_0$.
:::

<2>2. Q.E.D.

::: {.proof}
For $x \in E$ with $|x - x_0| < \delta$, the triangle inequality and step <2>1 give $|f(x) - f(x_0)| \le |f(x) - f_n(x)| + |f_n(x) - f_n(x_0)| + |f_n(x_0) - f(x_0)| < \eps$. So $f$ is continuous at the arbitrary point $x_0$.
:::

<1>3. Q.E.D.

::: {.proof}
Steps <1>1 and <1>2.
:::
:::
