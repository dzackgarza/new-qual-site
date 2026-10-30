---
schema: qual/card@1
id: P-BKF18-1B
kind: problem
title: Integral-test error for the Basel series
classification:
  areas:
  - prelim
  topics:
  - Calculus
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.problem}
Estimate $\pi^2/6=\sum_{n=1}^{\infty}1/n^2$ by the sum of the first $N$ terms.
What is the smallest $N$ such that the error is at most $10^{-6}$?
Use the integral test.
:::

::: {.solution}

$N=10^6$.

::: pf

::: {.pf-step #s1}

The error of the $N$-term sum is $E_N=\sum_{n=N+1}^\infty n^{-2}$, and
$$
\frac1{N+1}<E_N<\frac1N.
$$

::: pf-proof

The function $t\mapsto t^{-2}$ is strictly decreasing on $(0,\infty)$. So for $n\ge1$,
$$
\int_n^{n+1}\frac{dt}{t^2}<\frac1{n^2}<\int_{n-1}^{n}\frac{dt}{t^2}\quad(n\ge2).
$$
Sum the left inequality over $n\ge N+1$ and the right inequality over $n\ge N+1$: $\int_{N+1}^\infty t^{-2}\,dt<E_N<\int_N^\infty t^{-2}\,dt$.

:::

:::

::: {.pf-step #s2}

$E_{10^6}<10^{-6}$ and $E_N>10^{-6}$ for every $N<10^6$.

::: pf-proof

By step [](#s1){.pf-ref}, $E_{10^6}<10^{-6}$. If $N\le10^6-1$, then $E_N>1/(N+1)\ge10^{-6}$.

:::

:::

::: pf-qed

The error is at most $10^{-6}$ exactly when $N\ge10^6$, by step [](#s2){.pf-ref} and because $E_N$ decreases in $N$. So the smallest $N$ is $10^6$.

:::

:::

:::
