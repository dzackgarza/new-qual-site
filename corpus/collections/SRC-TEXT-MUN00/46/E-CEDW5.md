---
schema: qual/card@1
id: E-CEDW5
kind: problem
title: Partial sums of $\sum k x^k$ converge compactly but not uniformly on $(-1,1)$
classification:
  areas:
  - topology
  topics:
  - Function Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.exercise}

Consider the sequence of functions $f_n: (-1, 1) \to \mathbb{R}$, defined by

$$
f_n(x) = \sum_{k=1}^{n} k x^k.
$$

(a) Show that $(f_n)$ converges in the topology of compact convergence; conclude that the limit function is continuous.
(This is a standard fact about power series.)

(b) Show that $(f_n)$ does not converge in the uniform topology.
:::

::: {.solution}

::: pf

::: pf-step

For $x \in (-1, 1)$, $f_n(x) \to f(x) = \dfrac{x}{(1-x)^2}$.

::: pf-proof

For $\abs{x} < 1$, differentiating the geometric series $\sum_{k \ge 0} x^k = \frac{1}{1-x}$ term by term gives $\sum_{k \ge 1} k x^{k-1} = \frac{1}{(1-x)^2}$; multiply by $x$.

:::

:::

::: {.pf-step #s2}

(a) $f_n \to f$ uniformly on every compact $K \subseteq (-1, 1)$, and $f$ is continuous.

::: pf-proof

Since $K$ is compact and $\abs{x} < 1$ on $K$, $r = \max_{x \in K} \abs{x} < 1$. For $x \in K$,
$$\abs{f(x) - f_n(x)} = \abs{\sum_{k=n+1}^\infty k x^k} \le \sum_{k=n+1}^\infty k r^k.$$
The series $\sum_k k r^k$ converges by the ratio test, since $\frac{(k+1) r^{k+1}}{k r^k} \to r < 1$. So its tails tend to $0$, and $\sup_{x \in K} \abs{f(x) - f_n(x)} \to 0$. Each $f_n$ is a polynomial, hence continuous, and $f$ is continuous on each compact $K$ as a uniform limit of continuous functions. Every point of $(-1, 1)$ has a compact neighborhood $[-r, r]$ in $(-1, 1)$, so $f$ is continuous.

:::

:::

::: {.pf-step #s3}

(b) $(f_n)$ does not converge in the uniform topology.

::: pf-proof

Convergence in the uniform topology implies pointwise convergence, so a uniform limit would equal $f$. For fixed $n$, as $x \to 1^-$, $f_n(x) \to n(n+1)/2$ while $f(x) \to +\infty$. Hence $\sup_{x \in (-1, 1)} \abs{f(x) - f_n(x)} = \infty$, and the uniform distance $\bar{\rho}(f_n, f) = 1$ for every $n$.

:::

:::

::: pf-qed

Steps [](#s2){.pf-ref} and [](#s3){.pf-ref} prove parts (a) and (b).

:::

:::

:::
