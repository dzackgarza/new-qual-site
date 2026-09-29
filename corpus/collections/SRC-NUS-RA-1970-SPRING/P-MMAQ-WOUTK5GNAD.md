---
schema: qual/card@1
id: P-MMAQ-WOUTK5GNAD
kind: problem
title: $\int_{\{f>\alpha\}}f^2\to 0$ as $\alpha\to\infty$ when $\int f^3<\infty$
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
  - Lp Spaces
  - Integrals
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
If $f$ is a nonnegative measurable function on $[0, \pi]$ and $\int_0^\pi f(x)^3~dx < \infty$, show that
\[
\lim_{\alpha\to\infty}\int_{\theset{x:f(x)>\alpha}}f(x)^2\,dx=0.
\]
:::

::: {.solution}
Let $\alpha > 0$.

::: pf

::: {.pf-step #pointwise-bound}
On the set $\theset{x : f(x) > \alpha}$, the pointwise bound $f^2 \leq \frac{1}{\alpha} f^3$ holds.

::: pf-proof
where $f > \alpha$ we have $\frac{f^2}{f^3} = \frac{1}{f} < \frac{1}{\alpha}$, so $f^2 < \frac{f^3}{\alpha}$.
:::

:::

::: {.pf-step #integral-bound}
$\int_{\theset{f > \alpha}} f^2 \leq \frac{1}{\alpha} \int_{\theset{f > \alpha}} f^3 \leq \frac{1}{\alpha} \int_0^\pi f^3$.

::: pf-proof
integrate the bound of step [](#pointwise-bound){.pf-ref} over $\theset{f > \alpha}$; then use $\theset{f > \alpha} \subseteq [0, \pi]$ and $f^3 \geq 0$ to bound the restricted integral by the full one.
:::

:::

::: pf-step
The upper bound in step [](#integral-bound){.pf-ref} tends to $0$ as $\alpha \to \infty$.

::: pf-proof
$\int_0^\pi f^3$ is a fixed finite constant, and $\frac{1}{\alpha} \to 0$.
:::

:::

:::

::: pf-qed
the integrals in question are nonnegative ($f^2\geq0$) and squeezed between $0$ and a quantity tending to $0$, so the limit is $0$.
:::

:::
