---
schema: qual/card@1
id: E-PUNDP
kind: problem
title: Convergence of integrals does not imply an integrable dominant
classification:
  areas:
  - real-analysis
  topics:
  - Convergence of Integrals
  - Counterexamples
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.exercise}
- Is it true that the converse to the DCT holds?
  I.e. if $\int f_n \to \int f$, is there a $g\in L^p$ such that $f_n < g$ a.e. for every $n$?
:::

::: {.solution}
The answer is no. Let $f \equiv 0$ and $f_n = n\chi_{[1/(n+1), 1/n)}$ on $\RR$ for $n \ge 1$.

::: pf

::: {.pf-step #s1}

$f_n \geq 0$ and $f_n \to 0$ pointwise.

::: pf-proof

For $x \leq 0$ or $x \geq 1$, $f_n(x) = 0$ for all $n$. For $0 < x < 1$, $f_n(x) = 0$ once $1/n < x$.

:::

:::

::: {.pf-step #s2}

$\int f_n = n\left(\frac{1}{n} - \frac{1}{n+1}\right) = \frac{1}{n+1} \to 0 = \int f$.

::: pf-proof

This is the integral of a constant over an interval of length $\frac1n - \frac1{n+1}$.

:::

:::

::: pf-step

$\int \sup_n f_n = \infty$.

::: pf-proof

The intervals $[1/(n+1), 1/n)$ are pairwise disjoint and $f_n$ is supported on its own interval, so $\sup_n f_n = n$ on $[1/(n+1), 1/n)$; hence $\int \sup_n f_n = \sum_{n=1}^\infty n \cdot \frac{1}{n(n+1)} = \sum_{n=1}^\infty \frac{1}{n+1} = \infty$.

:::

:::

::: {.pf-step #s4}

No $g \in L^p$ with $1 \leq p < \infty$ satisfies $f_n \leq g$ a.e. for every $n$.

::: pf-proof

Such a $g$ satisfies $g \ge \sup_n f_n \geq 0$ a.e., so $\int g^p \ge \int (\sup_n f_n)^p = \sum_n n^p \cdot \frac{1}{n(n+1)} \ge \frac{1}{2}\sum_n n^{p-2} = \infty$.

:::

:::

::: pf-qed

By steps [](#s1){.pf-ref} and [](#s2){.pf-ref}, $f_n \to f$ pointwise and $\int f_n \to \int f$, while step [](#s4){.pf-ref} shows that no $L^p$ function dominates the $f_n$.

:::

:::

:::
