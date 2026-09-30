---
schema: qual/card@1
id: P-F7HCN
kind: problem
title: Convergence of $\sum nz^n$, $\sum z^n/n^2$, and $\sum z^n/n$ on the unit circle
classification:
  areas:
  - complex-analysis
  topics:
  - Power Series
  - Convergence Tests
  - Series of Functions
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.problem}
Prove the following:

a. $\sum_{n} nz^n$ does not converge at any point of $S^1$

b. $\sum_n {z^n \over n^2}$ converges at every point of $S^1$.

c. $\sum_n {z^n \over n}$ converges at every point of $S^1$ except $z=1$.
:::

::: {.solution}
**Goal:** Prove: (a) $\sum_{n} nz^n$ does not converge at any point of $S^1$; (b) $\sum_n z^n/n^2$ converges at every point of $S^1$; (c) $\sum_n z^n/n$ converges at every point of $S^1$ except $z = 1$.

::: pf

::: {.pf-step #part-a-terms-not-zero}
Part (a): for $\abs z = 1$, the terms do not tend to $0$.

::: pf-proof
$\abs{n z^n} = n \cdot \abs z^n = n \to \infty$ as $n \to \infty$; a necessary condition for convergence of a series is that its terms tend to $0$.
:::

:::

::: {.pf-step #part-b-absolute-convergence}
Part (b): $\sum_n \frac{z^n}{n^2}$ converges absolutely at every point of $S^1$.

::: pf-proof

::: {.pf-step #modulus-term-b}
$\abs{\frac{z^n}{n^2}} = \frac{1}{n^2}$ for $\abs z = 1$.

::: pf-proof
$\abs{z^n} = 1$.
:::

:::

::: {.pf-step #p-series-converges}
$\sum_n \frac{1}{n^2}$ converges.

::: pf-proof
$p$-series with $p = 2 > 1$.
:::

:::

::: pf-step
Hence the series converges absolutely, in particular converges, at every $z \in S^1$.

::: pf-proof
Absolute convergence (comparison test, steps [](#modulus-term-b){.pf-ref} and [](#p-series-converges){.pf-ref}) implies convergence.
:::

:::

:::

:::

::: {.pf-step #part-c-diverges-at-1}
Part (c) at $z = 1$: $\sum_n \frac{1}{n}$ diverges.

::: pf-proof
Harmonic series.
:::

:::

::: {.pf-step #part-c-converges-elsewhere}
Part (c) at $z \in S^1 \setminus \theset{1}$: $\sum_n \frac{z^n}{n}$ converges.

::: pf-proof

::: {.pf-step #partial-sums-bounded}
The partial sums $A_N := \sum_{n=1}^{N} z^n$ are bounded.

::: pf-proof
Geometric series: $A_N = \frac{z - z^{N+1}}{1 - z}$, so $\abs{A_N} \leq \frac{2}{\abs{1 - z}}$, a constant independent of $N$, since $z \neq 1$.
:::

:::

::: {.pf-step #terms-decrease-to-zero}
The sequence $\frac{1}{n}$ decreases to $0$.

::: pf-proof
Monotone and bounded below by $0$.
:::

:::

::: pf-step
Dirichlet's test applies: $\sum \frac{z^n}{n}$ converges.

::: pf-proof
Dirichlet's test: a series $\sum a_n b_n$ converges if the partial sums of $\sum a_n$ are bounded and $b_n \downarrow 0$; take $a_n = z^n$, $b_n = 1/n$, using steps [](#partial-sums-bounded){.pf-ref} and [](#terms-decrease-to-zero){.pf-ref}.
:::

:::

:::

:::

::: pf-qed
Step [](#part-a-terms-not-zero){.pf-ref} proves (a); step [](#part-b-absolute-convergence){.pf-ref} proves (b); steps [](#part-c-diverges-at-1){.pf-ref} and [](#part-c-converges-elsewhere){.pf-ref} prove (c).
:::

:::

:::
