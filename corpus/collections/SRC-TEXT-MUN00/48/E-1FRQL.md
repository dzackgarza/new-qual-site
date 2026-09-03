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

::: solution
**Goal:** Prove that the modified Thomae function $f: \mathbb{R} \to \mathbb{R}$ is continuous on $\mathbb{R} \setminus \mathbb{Q}$ and discontinuous on $\mathbb{Q}$, and construct a sequence of continuous functions converging pointwise to $f$.

<1>1. Continuity at every irrational point $x_0 \in \mathbb{R} \setminus \mathbb{Q}$:
    *Proof:*
    <2>1. At an irrational point $x_0$, $f(x_0) = 0$.
    <2>2. Let $\varepsilon > 0$. Choose an integer $N \in \mathbb{Z}_+$ such that $\frac{1}{N} < \varepsilon$.
    <2>3. The set $S_N = \{x_1, x_2, \dots, x_N\}$ is finite, and since $x_0$ is irrational, $x_0 \notin S_N$.
    <2>4. Define $\delta = \min_{1 \le n \le N} |x_0 - x_n| > 0$.
    <2>5. If $|x - x_0| < \delta$, then $x \notin S_N$.
    <2>6. Case 1: If $x \notin \mathbb{Q}$, $|f(x) - f(x_0)| = |0 - 0| = 0 < \varepsilon$.
    <2>7. Case 2: If $x \in \mathbb{Q}$, then $x = x_k$ for some $k > N$, so $|f(x) - f(x_0)| = \frac{1}{k} < \frac{1}{N} < \varepsilon$.
    <2>8. Thus $|f(x) - f(x_0)| < \varepsilon$ for all $x \in (x_0 - \delta, x_0 + \delta)$, so $f$ is continuous at $x_0$.

<1>2. Discontinuity at every rational point $x_m \in \mathbb{Q}$:
    *Proof:*
    <2>1. At $x_m \in \mathbb{Q}$, $f(x_m) = \frac{1}{m} > 0$.
    <2>2. Let $\varepsilon_0 = \frac{1}{2m} > 0$.
    <2>3. For any $\delta > 0$, the interval $(x_m - \delta, x_m + \delta)$ contains an irrational number $y$ by density of $\mathbb{R} \setminus \mathbb{Q}$ in $\mathbb{R}$.
    <2>4. At this point $y$, $|f(y) - f(x_m)| = |0 - \frac{1}{m}| = \frac{1}{m} > \varepsilon_0$.
    <2>5. Hence $f$ is discontinuous at $x_m$.

<1>3. Construction of continuous functions $f_k \to f$ pointwise:
    *Proof:*
    <2>1. For each fixed $k \in \mathbb{Z}_+$, consider the first $k$ rational numbers $\{x_1, \dots, x_k\}$.
    <2>2. For each $n \in \{1, \dots, k\}$, choose $\delta_{n, k} > 0$ such that the intervals $(x_n - \delta_{n, k}, x_n + \delta_{n, k})$ are pairwise disjoint for $1 \le n \le k$ and $\delta_{n, k} < \frac{1}{k}$.
    <2>3. Define a continuous "tent" function $\phi_{n, k}: \mathbb{R} \to [0, \frac{1}{n}]$ supported on $[x_n - \delta_{n, k}, x_n + \delta_{n, k}]$ by:
        $$\phi_{n, k}(x) = \max\left\{0, \; \frac{1}{n}\left(1 - \frac{|x - x_n|}{\delta_{n, k}}\right)\right\}.$$
    <2>4. Define $f_k: \mathbb{R} \to \mathbb{R}$ by $f_k(x) = \sum_{n=1}^k \phi_{n, k}(x)$. Each $f_k$ is continuous as a finite sum of continuous functions.
    <2>5. For any rational $x_m$, for all $k \ge m$ we have $f_k(x_m) = \phi_{m, k}(x_m) = \frac{1}{m} = f(x_m)$, so $\lim_{k \to \infty} f_k(x_m) = f(x_m)$.
    <2>6. For any irrational $x$, since $\delta_{n, k} \to 0$ as $k \to \infty$, $x$ belongs to the support of at most a transient set of tents with heights bounded by $\sup \{1/n : |x - x_n| < \delta_{n, k}\} \to 0$, giving $\lim_{k \to \infty} f_k(x) = 0 = f(x)$.
    <2>7. Thus $f_k \to f$ pointwise on $\mathbb{R}$. Q.E.D.
:::
