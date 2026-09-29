---
schema: qual/card@1
id: P-FFLLF
kind: problem
title: The Weierstrass approximation theorem
classification:
  areas:
  - real-analysis
  topics:
  - Stone-Weierstrass
  - Density
  - Uniform Convergence
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.problem}
> Note: (a) is a repeat.

Let $f: [0, 1]\to \RR$ be continuous, and prove the Weierstrass approximation theorem: for any $\eps> 0$ there exists a polynomial $P$ such that $\norm{f - P}_{\infty} < \eps$.
:::
::: {.solution}
For $n \geq 1$ let $p_{n,k}(x) = \binom{n}{k}x^k(1-x)^{n-k}$ and let $B_n(x) = \sum_{k=0}^n f(k/n)\,p_{n,k}(x)$, the Bernstein polynomial of $f$, of degree at most $n$.

::: pf

::: {.pf-step #s1}

$\sum_{k=0}^n p_{n,k}(x) = 1$ and $\sum_{k=0}^n (k - nx)^2 p_{n,k}(x) = nx(1-x)$ for $x \in [0,1]$.

::: pf-proof

The first is the binomial theorem for $(x + (1-x))^n$. The second is the variance of the binomial distribution with parameters $n$ and $x$; it follows by differentiating $\sum_k \binom nk s^k t^{n-k} = (s+t)^n$ once and twice in $s$ and setting $s = x$, $t = 1-x$.

:::

:::

::: {.pf-step #s2}

$|B_n(x) - f(x)| \le \sum_{k=0}^n |f(k/n) - f(x)|\,p_{n,k}(x)$.

::: pf-proof

By step [](#s1){.pf-ref}, $B_n(x) - f(x) = \sum_k (f(k/n) - f(x))\,p_{n,k}(x)$, and $p_{n,k}(x) \geq 0$.

:::

:::

::: {.pf-step #s3}

Given $\eps > 0$, there is $\delta > 0$ such that the terms of step [](#s2){.pf-ref} with $|k/n - x| < \delta$ sum to less than $\eps/2$.

::: pf-proof

$f$ is uniformly continuous on the compact interval $[0,1]$, so there is $\delta > 0$ with $|f(u) - f(v)| < \eps/2$ for $|u - v| < \delta$. By step [](#s1){.pf-ref} those terms sum to less than $\frac\eps2\sum_k p_{n,k}(x) = \frac\eps2$.

:::

:::

::: {.pf-step #s4}

The terms of step [](#s2){.pf-ref} with $|k/n - x| \ge \delta$ sum to at most $\frac{\|f\|_\infty}{2n\delta^2}$.

::: pf-proof

Each such term has $|f(k/n) - f(x)| \le 2\|f\|_\infty$ and $1 \le \frac{(k - nx)^2}{n^2\delta^2}$, so by step [](#s1){.pf-ref} they sum to at most $2\|f\|_\infty\cdot\frac{nx(1-x)}{n^2\delta^2} \le \frac{2\|f\|_\infty}{4n\delta^2}$.

:::

:::

::: pf-qed

For $n > \|f\|_\infty/(\eps\delta^2)$, steps [](#s2){.pf-ref}, [](#s3){.pf-ref} and [](#s4){.pf-ref} give $|B_n(x) - f(x)| < \eps$ for every $x \in [0,1]$, so $P = B_n$ works.

:::

:::

:::
