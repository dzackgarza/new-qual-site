---
schema: qual/card@1
id: P-RA18M5
kind: problem
title: Equicontinuity upgrades pointwise convergence to uniform convergence, and a Holder family is equicontinuous
classification:
  areas:
  - real-analysis
  topics:
  - Equicontinuity
  - Uniform Convergence
  - Compactness
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
  note: Checked against Problem 5 of the preserved UNL May 31, 2018 real-analysis qualifying exam.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
  note: Verified the compactness argument in part (a) and the uniform Holder modulus in part (b).
---

::: {.problem}
(a) If $\{f_n\}_{n\ge1}$ is an equicontinuous sequence of functions on a compact interval and $f_n\to f$ pointwise, prove that the convergence is uniform.

(b) Let $\alpha,M>0$ be given, and suppose that $\{f_n\}_{n\ge1}$ satisfies $\abs{f_n(x)-f_n(y)}\le M\abs{x-y}^\alpha$ for all $n\ge1$ and all $x,y$ in an interval $[a,b]$.
Show that $\{f_n\}_{n\ge1}$ is equicontinuous.
:::

::: {.solution}
**Goal:** (a) Equicontinuous sequence on a compact interval, converging pointwise, converges uniformly; (b) $\abs{f_n(x) - f_n(y)} \le M\abs{x-y}^\alpha$ implies equicontinuity.

::: pf

::: pf-step
(a) $f_n \to f$ uniformly.

::: pf-proof

::: {.pf-step #s1-1}
$f$ is continuous.

::: pf-proof
fix $x_0$; equicontinuity gives $\delta$ with $\abs{f_n(x) - f_n(x_0)} < \varepsilon/3$ for all $n$ and $\abs{x - x_0} < \delta$; let $n \to \infty$: $\abs{f(x) - f(x_0)} \le \varepsilon/3$.
:::

:::

::: pf-step
Fix $\varepsilon > 0$.
By equicontinuity, for each $x$ there is $\delta_x$ with $\abs{f_n(y) - f_n(x)} < \varepsilon/3$ for all $n$ and $\abs{y - x} < \delta_x$; finitely many $\delta_{x_i}/2$-balls cover the interval (compactness).

:::

::: pf-step
For each $x_i$ choose $N_i$ with $\abs{f_n(x_i) - f(x_i)} < \varepsilon/3$ for $n \ge N_i$ (pointwise convergence); set $N = \max N_i$.

:::

::: {.pf-step #s1-4}
For $n \ge N$ and any $x$: pick $i$ with $\abs{x - x_i} < \delta_{x_i}/2$; then $\abs{f_n(x) - f(x)} \le \abs{f_n(x) - f_n(x_i)} + \abs{f_n(x_i) - f(x_i)} + \abs{f(x_i) - f(x)} < \varepsilon$.

::: pf-proof
three terms each $< \varepsilon/3$: the first by equicontinuity ($\abs{x - x_i} < \delta_{x_i}/2 < \delta_{x_i}$), the second by $n \ge N_i$, the third by letting $n \to \infty$ in the equicontinuity bound (or continuity of $f$ from step [](#s1-1){.pf-ref}).
:::

:::

::: pf-qed
step [](#s1-4){.pf-ref} gives uniform convergence (the standard compactness argument for equicontinuity upgrading pointwise to uniform).
:::

:::

:::

::: pf-step
(b) $\{f_n\}$ is equicontinuous on $[a,b]$.

::: pf-proof

::: pf-step
Given $\varepsilon > 0$, choose $\delta = (\varepsilon/M)^{1/\alpha}$.

:::

::: {.pf-step #s2-2}
For $\abs{x - y} < \delta$: $\abs{f_n(x) - f_n(y)} \le M\abs{x - y}^\alpha < M\delta^\alpha = \varepsilon$, for every $n$ simultaneously.

::: pf-proof
the Hölder hypothesis with $\delta$ as chosen; $\delta$ is independent of $n$, $x$, $y$.
:::

:::

::: pf-qed
step [](#s2-2){.pf-ref} is exactly equicontinuity.
:::

:::

:::

:::

:::
