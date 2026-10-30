---
schema: qual/card@1
id: E-SS6.PR-1
kind: problem
title: Estimates for $\zeta$ and $\zeta'$ near $\Re(s)=1$
classification:
  areas:
  - complex-analysis
  topics:
  - Zeta Function
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: {.exercise}
1. This problem provides further estimates for $\zeta$ and $\zeta'$ near $\operatorname{Re}(s) = 1$.

(a) Use Proposition 2.5 and its corollary to prove
$$
\zeta(s) = \sum_{1 \leq n < N} n^{-s} + \frac{N^{1-s}}{s-1} + \sum_{n \geq N} \delta_n(s)
$$
for every integer $N \geq 2$, whenever $\operatorname{Re}(s) > 0$, where $\delta_n(s) = n^{-s} - \int_n^{n+1} x^{-s}\,dx$.

(b) Show that $\abs{\zeta(1+it)} = O(\log \abs{t})$ as $\abs{t} \to \infty$ by using the previous result with $N = \lfloor \abs{t} \rfloor$.

(c) Show that $\abs{\zeta'(1+it)} = O((\log \abs{t})^2)$ as $\abs{t} \to \infty$.

(d) Show that if $t \neq 0$ and $t$ is fixed, then the partial sums of the series $\sum_{n=1}^\infty n^{-1-it}$ are bounded, but the series does not converge.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Part 1(a): Expansion for $\zeta(s)$ with truncation parameter $N$.

::: pf-proof

::: pf-step

For $\Re(s) > 1$, the Dirichlet series converges absolutely:
    $$\zeta(s) = \sum_{n=1}^\infty n^{-s} = \sum_{n=1}^{N-1} n^{-s} + \sum_{n=N}^\infty n^{-s}.$$

:::

::: pf-step

For each $n \ge N$, write $n^{-s} = \int_n^{n+1} x^{-s}\,dx + \delta_n(s)$, where $\delta_n(s) = \int_n^{n+1} (n^{-s} - x^{-s})\,dx$.

:::

::: pf-step

Summing the integral terms gives
    $$\sum_{n=N}^\infty \int_n^{n+1} x^{-s}\,dx = \int_N^\infty x^{-s}\,dx = \left[ \frac{x^{1-s}}{1-s} \right]_N^\infty = \frac{N^{1-s}}{s-1},$$
    which converges for $\Re(s) > 1$.

:::

::: pf-step

Thus for $\Re(s) > 1$,
    $$\zeta(s) = \sum_{1 \le n < N} n^{-s} + \frac{N^{1-s}}{s-1} + \sum_{n \ge N} \delta_n(s).$$

:::

::: pf-step

By the Mean Value Theorem applied to $f(x) = x^{-s}$ on $[n, n+1]$, $\abs{n^{-s} - x^{-s}} \le \abs{s} n^{-\Re(s)-1}$, so
    $$\abs{\delta_n(s)} \le \abs{s} n^{-\Re(s)-1}.$$
    The series $\sum_{n \ge N} \delta_n(s)$ converges locally uniformly for $\Re(s) > 0$, defining a holomorphic function on $\Re(s) > 0$.

:::

::: pf-step

By analytic continuation, the identity holds for all $\Re(s) > 0$ with $s \neq 1$.

:::

:::

:::

::: {.pf-step #s2}

Part 1(b): Bound $\abs{\zeta(1+it)} = O(\log \abs{t})$ as $\abs{t} \to \infty$.

::: pf-proof

::: pf-step

Set $s = 1+it$ with $\abs{t} \ge 2$, and choose $N = \lfloor \abs{t} \rfloor \ge 2$.

:::

::: pf-step

In the expansion from step [](#s1){.pf-ref}:
    $$\abs{ \sum_{1 \le n < N} n^{-1-it} } \le \sum_{n=1}^{N-1} \frac{1}{n} \le 1 + \int_1^N \frac{dx}{x} = 1 + \log N \le 1 + \log \abs{t}.$$

:::

::: pf-step

For the pole term:
    $$\abs{ \frac{N^{1-s}}{s-1} } = \abs{ \frac{N^{-it}}{it} } = \frac{1}{\abs{t}} \le \frac{1}{2} = O(1).$$

:::

::: pf-step

For the tail: using $\abs{\delta_n(1+it)} \le \abs{1+it} n^{-2} \le (1+\abs{t}) n^{-2}$,
    $$\abs{ \sum_{n=N}^\infty \delta_n(1+it) } \le (1+\abs{t}) \sum_{n=N}^\infty \frac{1}{n^2} \le (1+\abs{t}) \frac{1}{N-1} \le \frac{1+\abs{t}}{\abs{t}-1} \le 3 = O(1).$$

:::

::: pf-step

Summing the three bounds gives $\abs{\zeta(1+it)} \le \log \abs{t} + O(1) = O(\log \abs{t})$.

:::

:::

:::

::: {.pf-step #s3}

Part 1(c): Bound $\abs{\zeta'(1+it)} = O((\log \abs{t})^2)$ as $\abs{t} \to \infty$.

::: pf-proof

::: pf-step

Differentiating the identity from step [](#s1){.pf-ref} with respect to $s$:
    $$\zeta'(s) = -\sum_{1 \le n < N} n^{-s} \log n - \frac{N^{1-s} \log N}{s-1} - \frac{N^{1-s}}{(s-1)^2} + \sum_{n=N}^\infty \delta_n'(s).$$

:::

::: pf-step

At $s = 1+it$ with $N = \lfloor \abs{t} \rfloor$:
    $$\abs{ \sum_{1 \le n < N} n^{-1-it} \log n } \le \sum_{n=1}^{N-1} \frac{\log n}{n} \le \int_1^N \frac{\log x}{x}\,dx + O(1) = \frac{1}{2} (\log N)^2 + O(1) \le \frac{1}{2}(\log \abs{t})^2 + O(1).$$

:::

::: pf-step

The terms involving $N^{1-s}$ satisfy
    $$\abs{ \frac{N^{-it} \log N}{it} } = \frac{\log N}{\abs{t}} = O(1), \qquad \abs{ \frac{N^{-it}}{(it)^2} } = \frac{1}{\abs{t}^2} = O(1).$$

:::

::: pf-step

Differentiating $\delta_n(s) = \int_n^{n+1} (n^{-s} - x^{-s})\,dx$ gives $\abs{\delta_n'(1+it)} \le C \abs{t} \frac{\log n}{n^2}$, so
    $$\abs{ \sum_{n=N}^\infty \delta_n'(1+it) } \le C \abs{t} \sum_{n=N}^\infty \frac{\log n}{n^2} = O\left(\abs{t} \frac{\log N}{N}\right) = O(\log \abs{t}).$$

:::

::: pf-step

Therefore $\abs{\zeta'(1+it)} = O((\log \abs{t})^2)$.

:::

:::

:::

::: {.pf-step #s4}

Part 1(d): Partial sums are bounded but do not converge for $t \neq 0$.

::: pf-proof

::: pf-step

Let $S_m(t) = \sum_{n=1}^m n^{-1-it}$. Applying step [](#s1){.pf-ref} with $s = 1+it$ and $N = m+1$:
    $$S_m(t) = \zeta(1+it) - \frac{(m+1)^{-it}}{it} - \sum_{n=m+1}^\infty \delta_n(1+it).$$

:::

::: pf-step

The tail satisfies $\abs{ \sum_{n=m+1}^\infty \delta_n(1+it) } \le (1+\abs{t}) \frac{1}{m} \le 1+\abs{t}$ for all $m \ge 1$.

:::

::: pf-step

Since $\abs{\zeta(1+it)}$ is a constant for fixed $t$, and $\abs{(m+1)^{-it}/(it)} = 1/\abs{t}$ is constant, $\abs{S_m(t)} \le \abs{\zeta(1+it)} + \frac{1}{\abs{t}} + (1+\abs{t})$ is uniformly bounded in $m$.

:::

::: pf-step

If $S_m(t)$ converged to $\zeta(1+it)$ as $m \to \infty$, then $(m+1)^{-it} = e^{-it \log(m+1)}$ would converge as $m \to \infty$. But for $t \neq 0$, the sequence $e^{-it \log(m+1)}$ oscillates around the unit circle and has no limit.

:::

::: pf-step

Hence the series $\sum_{n=1}^\infty n^{-1-it}$ diverges.

:::

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref}, [](#s3){.pf-ref} and [](#s4){.pf-ref} prove parts (a) to (d).

:::

:::

:::
