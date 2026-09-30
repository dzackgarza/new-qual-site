---
schema: qual/card@1
id: P-MMAQ-GSHH4MRFJW
kind: problem
title: Uniform convergence need not pass to integrals; $L^p$ convergence implies an
  a.e. subsequence
classification:
  areas:
  - real-analysis
  topics:
  - Integrals
  - Convergence of Functions
  - Lp Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Prove or disprove each of the following statements.

(b) If ${f_n}$ is a sequence of measurable functions that converges uniformly to $f$ on $\mathbb{R}$, then $\int{f}=\lim_{k\to \infty} \int f_k$

(c) If $\{f_k\}$ is a sequence of function in $L_p[0,\infty)$ that converges to a function $f \in L_p [0,\infty)$, then $\{f_k\}$ has a subsequence that converges to $f$ almost everywhere.
:::

::: {.solution}

::: pf

::: {.pf-step #b-is-false}
(b) is false.

::: pf-proof

::: {.pf-step #fk-definition}
Let $f_k \definedas \frac{1}{k} \chi_{[0,k]}$ on $\RR$.

::: pf-proof
Each $f_k$ is measurable (indicator of an interval), and $\int_\RR f_k = \frac{1}{k} \cdot k = 1$ for every $k$.
:::

:::

::: pf-step
$f_k \to 0$ uniformly on $\RR$.

::: pf-proof
$\sup_{x \in \RR} \abs{f_k(x) - 0} = \frac{1}{k} \to 0$.
:::

:::

::: pf-step
$\lim_k \int f_k = 1 \neq 0 = \int 0$.

::: pf-proof
Each integral $\int f_k$ is $1$ by step [](#fk-definition){.pf-ref}, while the uniform limit $f = 0$ has integral $0$.
:::

:::

::: pf-qed
The counterexample of step [](#fk-definition){.pf-ref} satisfies the hypotheses but not the conclusion, so (b) is false.
:::

:::

:::

::: {.pf-step #c-is-true}
(c) is true: convergence in $L_p$ implies a.e.\ convergence along a subsequence (for $1 \leq p < \infty$).

::: pf-proof

::: pf-step
Choose a subsequence $\theset{f_{k_j}}$ with $\norm{f_{k_j} - f}_p \leq 2^{-j}$.

::: pf-proof
Since $\norm{f_k - f}_p \to 0$ by hypothesis, pick $k_j$ recursively so the $L_p$ distance is $\leq 2^{-j}$.
:::

:::

::: pf-step
For each $j$, $\mu\theset{x : \abs{f_{k_j}(x) - f(x)} > 2^{-j/2}} \leq \left(2^{-j/2}\right)^{-p} \norm{f_{k_j} - f}_p^p \leq 2^{jp/2} 2^{-jp} = 2^{-jp/2}$.

::: pf-proof
Chebyshev's (Markov's) inequality applied to $\abs{f_{k_j} - f}^p$ with threshold $2^{-jp/2}$.
:::

:::

::: {.pf-step #measure-sum-finite}
$\sum_j \mu\theset{x : \abs{f_{k_j}(x) - f(x)} > 2^{-j/2}} \leq \sum_j 2^{-jp/2} < \infty$.

::: pf-proof
Geometric series, since $p \geq 1$ implies $p/2 > 0$.
:::

:::

::: {.pf-step #ae-bound-holds}
By Borel–Cantelli, for almost every $x$, $\abs{f_{k_j}(x) - f(x)} \leq 2^{-j/2}$ for all but finitely many $j$.

::: pf-proof
The sets in step [](#measure-sum-finite){.pf-ref} have summable measure, so almost every $x$ lies in only finitely many of them.
:::

:::

::: {.pf-step #fkj-converges-pointwise}
For such $x$, $f_{k_j}(x) \to f(x)$.

::: pf-proof
$2^{-j/2} \to 0$.
:::

:::

::: pf-qed
By steps [](#ae-bound-holds){.pf-ref} and [](#fkj-converges-pointwise){.pf-ref}, the subsequence $f_{k_j}$ converges to $f$ almost everywhere.
:::

:::

:::

::: pf-qed
Conclusion: (b) is false and (c) is true.

By steps [](#b-is-false){.pf-ref} and [](#c-is-true){.pf-ref}.
:::

:::

:::
