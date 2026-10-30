---
schema: qual/card@1
id: P-TOIEK
kind: problem
title: Uniformly convergent sequences of bounded functions are uniformly bounded
classification:
  areas:
  - prelim
  topics:
  - Uniform Convergence
  - Sequences of Functions
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Suppose $(f_n)$ is a sequence of bounded functions from $\RR$ to $\RR$ that converges uniformly to a function $f$. Prove that there is an $M>0$ such that
$$
\abs{f_n(x)}\le M
$$
for all natural numbers $n$ and all real numbers $x$.
:::

::: {.solution}

::: pf

::: {.pf-step #tail}

There is $N \in \NN$ such that $\abs{f_n(x)} < \abs{f_N(x)} + 2$ for all $n \ge N$ and all $x \in \RR$.

::: pf-proof

By uniform convergence with $\varepsilon = 1$, there is $N$ such that $\abs{f_n(x) - f(x)} < 1$ for all $n \ge N$ and all $x$.
For $n \ge N$ the triangle inequality gives
$$
\abs{f_n(x)} \le \abs{f_N(x)} + \abs{f_N(x) - f(x)} + \abs{f(x) - f_n(x)} < \abs{f_N(x)} + 2.
$$

:::

:::

::: {.pf-step #heads}

For each $k \in \{1, \dots, N\}$ there is $M_k \ge 0$ with $\abs{f_k(x)} \le M_k$ for all $x \in \RR$.

::: pf-proof

Each $f_k$ is bounded by hypothesis.

:::

:::

::: pf-step

The number $M = \max\{M_1, \dots, M_{N-1}, M_N + 2\} > 0$ satisfies $\abs{f_n(x)} \le M$ for all $n \in \NN$ and all $x \in \RR$.

::: pf-proof

We have $M \ge M_N + 2 > 0$.
If $n < N$, then $\abs{f_n(x)} \le M_n \le M$ by step [](#heads){.pf-ref}.
If $n \ge N$, then $\abs{f_n(x)} < M_N + 2 \le M$ by steps [](#tail){.pf-ref} and [](#heads){.pf-ref}.

:::

:::

:::

:::
