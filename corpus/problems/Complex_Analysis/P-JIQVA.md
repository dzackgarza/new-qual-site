---
schema: qual/card@1
id: P-JIQVA
kind: problem
title: Zeros of the truncated exponential $P_n$ and of $P_n-1$ in $\abs{z}<10$
classification:
  areas:
  - complex-analysis
  topics:
  - Rouché
  - Zeros
  - Polynomials
  - Uniform Convergence
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.problem}
For each $n\in \ZZ^{\geq 1}$, let
$$
P_n(z) = 1 + z + {1\over 2!} z^2 + \cdots + {1\over n!}z^n
.$$
Show that for sufficiently large $n$, the polynomial $P_n$ has no zeros in $\abs{z} < 10$, while the polynomial $P_n(z) - 1$ has precisely 3 zeros there.
:::

::: {.solution}
::: pf

::: {.pf-step #uniform-convergence}
$P_n \to e^z$ uniformly on the circle $\abs{z} = 10$.

::: pf-proof
On $\abs{z} = 10$, $\abs{e^z - P_n(z)} \leq \sum_{k=n+1}^\infty \frac{10^k}{k!}$, the tail of the convergent series $\sum_k 10^k/k! = e^{10}$.
:::

:::

::: pf-step
For all sufficiently large $n$, $P_n$ has no zeros in $\abs{z} < 10$.

::: pf-proof
On $\abs{z} = 10$, $\abs{e^z} = e^{\Re z} \geq e^{-10}$.
By step [](#uniform-convergence){.pf-ref}, for large $n$ we have $\abs{P_n - e^z} < e^{-10} \leq \abs{e^z}$ on $\abs{z} = 10$.
Rouché's theorem shows that $P_n$ and $e^z$ have equally many zeros in $\abs{z} < 10$, and $e^z$ has none.
:::

:::

::: {.pf-step #ez-minus-1-zeros}
$e^z - 1$ has exactly 3 zeros in $\abs{z} \leq 10$, all simple and in $\abs{z} < 10$.

::: pf-proof
The zeros of $e^z - 1$ are $2\pi i k$, $k \in \ZZ$, each simple since the derivative $e^z$ does not vanish.
Since $2\pi < 10 < 4\pi$, those with $\abs{z} \leq 10$ are $0, \pm 2\pi i$.
:::

:::

::: pf-step
For all sufficiently large $n$, $P_n - 1$ has exactly 3 zeros in $\abs{z} < 10$.

::: pf-proof
By step [](#ez-minus-1-zeros){.pf-ref}, the continuous function $\abs{e^z - 1}$ has a positive minimum $m$ on the compact circle $\abs{z} = 10$.
By step [](#uniform-convergence){.pf-ref}, for large $n$ we have $\abs{(P_n - 1) - (e^z - 1)} = \abs{P_n - e^z} < m$ there.
Rouché's theorem shows that $P_n - 1$ and $e^z - 1$ have equally many zeros in $\abs{z} < 10$, namely 3.
:::

:::

:::
:::
