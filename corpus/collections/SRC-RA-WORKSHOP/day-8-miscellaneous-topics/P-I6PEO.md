---
schema: qual/card@1
id: P-I6PEO
kind: problem
title: $1/f$ has bounded variation on $[a,b]$ when $f$ does and $|f|\ge c>0$
classification:
  areas:
  - real-analysis
  topics:
  - Variation
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---
::: {.problem}
Let $f$ be a function of bounded variation on $[a,b]$.
Furthermore, assume that for some $c>0$, $|f(x)| \geq c$ on $[a,b]$.
Show that $g(x) = 1/f(x)$ is of bounded variation on $[a,b]$.
:::
::: {.solution}

::: pf

::: {.pf-step #s1}

For $x, y \in [a,b]$: $\left|\frac{1}{f(x)} - \frac{1}{f(y)}\right| = \frac{|f(x) - f(y)|}{|f(x)f(y)|} \le \frac{1}{c^2}|f(x) - f(y)|$.

::: pf-proof

The lower bound $|f|\geq c>0$ ensures that $g=1/f$ is defined everywhere. For any $x,y\in[a,b]$,
\[
|g(x)-g(y)|=\frac{|f(y)-f(x)|}{|f(x)f(y)|}
\leq c^{-2}|f(y)-f(x)|,
\]
since $|f(x)f(y)|\geq c^2$.

:::

:::

::: {.pf-step #s2}

For any partition $a = x_0 < \cdots < x_n = b$: $\sum_{i=1}^n \left|\frac{1}{f(x_i)} - \frac{1}{f(x_{i-1})}\right| \le \frac{1}{c^2}\sum_{i=1}^n |f(x_i) - f(x_{i-1})| \le \frac{1}{c^2}V_{[a,b]}(f)$.

::: pf-proof

Apply step [](#s1){.pf-ref} to each pair $(x_i,x_{i-1})$ and sum. By definition, every partition variation sum of $f$ is bounded above by $V_{[a,b]}(f)$.

:::

:::

::: {.pf-step #s3}

The reciprocal satisfies $\boxed{V_{[a,b]}(g)\leq c^{-2}V_{[a,b]}(f)<\infty}$.

::: pf-proof

Take the supremum of the left-hand partition sums in step [](#s2){.pf-ref} over all finite partitions of $[a,b]$. The right-hand bound is independent of the partition and finite because $f$ has bounded variation.

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} proves that $g=1/f$ is of bounded variation.

:::

:::

:::
