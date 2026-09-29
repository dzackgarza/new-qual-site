---
schema: qual/card@1
id: P-QUXEB
kind: problem
title: Convergence of $\sum nz^n$, $\sum z^n/n^2$, and $\sum z^n/n$ on $S^1$
classification:
  areas:
  - complex-analysis
  topics:
  - Power Series
  - Convergence Tests
  - Series of Functions
relations: []
review: draft
---

::: {.problem}
Prove the following statements concerning the convergence of power series on the unit circle $S^1 = \{z \in \mathbb{C} : |z| = 1\}$:

(a) $\sum_{n=1}^\infty n z^n$ does not converge at any point of $S^1$.

(b) $\sum_{n=1}^\infty \frac{z^n}{n^2}$ converges at every point of $S^1$.

(c) $\sum_{n=1}^\infty \frac{z^n}{n}$ converges at every point of $S^1$ except $z = 1$, where it diverges.
:::

::: {.solution}
Throughout, $z\in S^1$, so $\abs{z}=1$.

::: pf

::: {.pf-step #s1}

(a) $\sum_{n=1}^\infty n z^n$ diverges.

::: pf-proof

The terms satisfy $\abs{nz^n} = n\abs{z}^n = n \to \infty$, so they do not tend to $0$. A series whose terms do not tend to $0$ diverges.

:::

:::

::: {.pf-step #s2}

(b) $\sum_{n=1}^\infty z^n/n^2$ converges absolutely.

::: pf-proof

The terms satisfy $\abs{z^n/n^2} = 1/n^2$, and $\sum_{n\ge1} 1/n^2$ converges. By comparison the series converges absolutely, hence converges.

:::

:::

::: {.pf-step #s3}

(c) At $z=1$, $\sum_{n=1}^\infty z^n/n$ diverges.

::: pf-proof

At $z=1$ the series is the harmonic series $\sum_{n\ge1}1/n$, which diverges to $+\infty$.

:::

:::

::: {.pf-step #s4}

(c) If $z\neq1$, then $\sum_{n=1}^\infty z^n/n$ converges.

::: pf-proof

::: {.pf-step #s4-1}

The partial sums $B_N \coloneqq \sum_{k=1}^N z^k$, with $B_0\coloneqq0$, satisfy $\abs{B_N}\le M_z \coloneqq 2/\abs{1-z}$ for all $N\ge0$.

::: pf-proof

For $N\ge1$, the geometric sum is $B_N = z(1-z^N)/(1-z)$, so
$$\abs{B_N} = \frac{\abs{1 - z^N}}{\abs{1 - z}} \le \frac{1 + \abs{z}^N}{\abs{1 - z}} = \frac{2}{\abs{1 - z}}.$$
The bound is finite because $z\neq1$.

:::

:::

::: {.pf-step #s4-2}

For $N > M \ge 1$, with $a_n\coloneqq 1/n$,
$$\sum_{n=M}^N a_n z^n = a_N B_N - a_M B_{M-1} + \sum_{n=M}^{N-1} (a_n - a_{n+1}) B_n.$$

::: pf-proof

This is summation by parts, using $z^n = B_n - B_{n-1}$.

:::

:::

::: {.pf-step #s4-3}

For $N > M \ge 1$,
$$\left| \sum_{n=M}^N \frac{z^n}{n} \right| \le \frac{2 M_z}{M}.$$

::: pf-proof

The sequence $a_n=1/n$ is positive and decreasing, so $a_n - a_{n+1}\ge0$. Steps [](#s4-1){.pf-ref} and [](#s4-2){.pf-ref} give
$$\left| \sum_{n=M}^N a_n z^n \right| \le M_z a_N + M_z a_M + M_z \sum_{n=M}^{N-1} (a_n - a_{n+1}) = 2 M_z a_M.$$

:::

:::

::: pf-qed

By step [](#s4-3){.pf-ref}, the partial sums of $\sum z^n/n$ satisfy the Cauchy criterion, so the series converges.

:::

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} proves (a), step [](#s2){.pf-ref} proves (b), and steps [](#s3){.pf-ref} and [](#s4){.pf-ref} prove (c).

:::

:::

:::
