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
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: 'Source gave no domain or codomain and read "continuous function"; the statement now fixes f_n, f : E -> R with E a subset of R, as the solution assumes, and reads "functions".'
---

::: {.exercise}
Let $E \subseteq \RR$ and let $f_n, f : E \to \RR$.

(a) Show that a uniform limit of bounded functions is bounded.

(b) Show that a uniform limit of continuous functions is continuous, i.e. if $f_n\to f$ uniformly with each $f_n$ continuous then $f$ is continuous.
:::

::: {.solution}
Let $f_n \to f$ uniformly on a set $E$.

::: pf

::: {.pf-step #s1}

If each $f_n$ is bounded, then $f$ is bounded.

::: pf-proof

Uniform convergence with $\eps = 1$ gives $N$ with $\norm{f - f_N}_\infty \le 1$. By the triangle inequality, $\abs{f(x)} \le \abs{f_N(x)} + 1 \le \norm{f_N}_\infty + 1$ for every $x \in E$.

:::

:::

::: {.pf-step #s2}

If each $f_n$ is continuous, then $f$ is continuous.

::: pf-proof

::: {.pf-step #s2-1}

Fix $x_0 \in E$ and $\eps > 0$. There are $n$ with $\norm{f - f_n}_\infty < \eps/3$ and $\delta > 0$ with $\abs{f_n(x) - f_n(x_0)} < \eps/3$ whenever $x \in E$ and $\abs{x - x_0} < \delta$.

::: pf-proof

The first is uniform convergence and the second is continuity of $f_n$ at $x_0$.

:::

:::

::: pf-qed

For $x \in E$ with $\abs{x - x_0} < \delta$, the triangle inequality and step [](#s2-1){.pf-ref} give $\abs{f(x) - f(x_0)} \le \abs{f(x) - f_n(x)} + \abs{f_n(x) - f_n(x_0)} + \abs{f_n(x_0) - f(x_0)} < \eps$. So $f$ is continuous at the arbitrary point $x_0$.

:::

:::

:::

:::

:::
