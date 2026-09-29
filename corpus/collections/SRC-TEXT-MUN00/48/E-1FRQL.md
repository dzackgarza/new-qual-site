---
schema: qual/card@1
id: E-1FRQL
kind: problem
title: Thomae-type function continuous at each irrational
classification:
  areas:
  - topology
  topics:
  - Baire Spaces
  - Continuous Functions
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Let $g: \mathbb{Z}_+ \to \mathbb{Q}$ be a bijective function; let $x_n = g(n)$.
Define $f: \mathbb{R} \to \mathbb{R}$ as follows:

$$
\begin{array}{ll}
f(x_n) = 1/n & \text{for } x_n \in \mathbb{Q}, \\
f(x) = 0 & \text{for } x \notin \mathbb{Q}.
\end{array}
$$

Show that $f$ is continuous at each irrational and discontinuous at each rational.
Can you find a sequence of continuous functions $f_n$ converging to $f$?
:::

::: {.solution}

::: pf

::: pf-step

Continuity at every irrational point $x_0 \in \mathbb{R} \setminus \mathbb{Q}$:
    *Proof:*

::: pf-proof

::: pf-step

At an irrational point $x_0$, $f(x_0) = 0$.

:::

::: pf-step

Let $\varepsilon > 0$. Choose an integer $N \in \mathbb{Z}_+$ such that $\frac{1}{N} < \varepsilon$.

:::

::: pf-step

The set $S_N = \{x_1, x_2, \dots, x_N\}$ is finite, and since $x_0$ is irrational, $x_0 \notin S_N$.

:::

::: pf-step

Define $\delta = \min_{1 \le n \le N} |x_0 - x_n| > 0$.

:::

::: pf-step

If $|x - x_0| < \delta$, then $x \notin S_N$.

:::

::: pf-step

Case 1: If $x \notin \mathbb{Q}$, $|f(x) - f(x_0)| = |0 - 0| = 0 < \varepsilon$.

:::

::: pf-step

Case 2: If $x \in \mathbb{Q}$, then $x = x_k$ for some $k > N$, so $|f(x) - f(x_0)| = \frac{1}{k} < \frac{1}{N} < \varepsilon$.

:::

::: pf-step

Thus $|f(x) - f(x_0)| < \varepsilon$ for all $x \in (x_0 - \delta, x_0 + \delta)$, so $f$ is continuous at $x_0$.

:::

:::

:::

::: pf-step

Discontinuity at every rational point $x_m \in \mathbb{Q}$:
    *Proof:*

::: pf-proof

::: pf-step

At $x_m \in \mathbb{Q}$, $f(x_m) = \frac{1}{m} > 0$.

:::

::: pf-step

Let $\varepsilon_0 = \frac{1}{2m} > 0$.

:::

::: pf-step

For any $\delta > 0$, the interval $(x_m - \delta, x_m + \delta)$ contains an irrational number $y$ by density of $\mathbb{R} \setminus \mathbb{Q}$ in $\mathbb{R}$.

:::

::: pf-step

At this point $y$, $|f(y) - f(x_m)| = |0 - \frac{1}{m}| = \frac{1}{m} > \varepsilon_0$.

:::

::: pf-step

Hence $f$ is discontinuous at $x_m$.

:::

:::

:::

::: pf-step

Construction of continuous functions $f_k \to f$ pointwise:
    *Proof:*

::: pf-proof

::: pf-step

For each fixed $k \in \mathbb{Z}_+$, consider the first $k$ rational numbers $\{x_1, \dots, x_k\}$.

:::

::: pf-step

For each $n \in \{1, \dots, k\}$, choose $\delta_{n, k} > 0$ such that the intervals $(x_n - \delta_{n, k}, x_n + \delta_{n, k})$ are pairwise disjoint for $1 \le n \le k$ and $\delta_{n, k} < \frac{1}{k}$.

:::

::: pf-step

Define a continuous "tent" function $\phi_{n, k}: \mathbb{R} \to [0, \frac{1}{n}]$ supported on $[x_n - \delta_{n, k}, x_n + \delta_{n, k}]$ by:
        $$\phi_{n, k}(x) = \max\left\{0, \; \frac{1}{n}\left(1 - \frac{|x - x_n|}{\delta_{n, k}}\right)\right\}.$$

:::

::: pf-step

Define $f_k: \mathbb{R} \to \mathbb{R}$ by $f_k(x) = \sum_{n=1}^k \phi_{n, k}(x)$. Each $f_k$ is continuous as a finite sum of continuous functions.

:::

::: pf-step

For any rational $x_m$, for all $k \ge m$ we have $f_k(x_m) = \phi_{m, k}(x_m) = \frac{1}{m} = f(x_m)$, so $\lim_{k \to \infty} f_k(x_m) = f(x_m)$.

:::

::: pf-step

Let $x$ be irrational and $\varepsilon > 0$. Choose $N$ with $1/N < \varepsilon$ and put $\eta = \min_{1 \le n \le N} |x - x_n| > 0$. For $k > \max(N, 1/\eta)$, $\delta_{n, k} < 1/k < \eta$, so $\phi_{n, k}(x) = 0$ for $n \le N$. The supports of the tents $\phi_{1,k}, \ldots, \phi_{k,k}$ are disjoint, so $f_k(x) = \phi_{n, k}(x) \le 1/n < \varepsilon$ for at most one $n > N$, and $f_k(x) = 0$ otherwise. Hence $\lim_{k \to \infty} f_k(x) = 0 = f(x)$.

:::

::: pf-step

Thus $f_k \to f$ pointwise on $\mathbb{R}$. Q.E.D.

:::

:::

:::

:::

:::
