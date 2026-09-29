---
schema: qual/card@1
id: P-BH66D
kind: problem
title: Equivalence of $\varepsilon$-$\delta$ and sequential continuity at a point
classification:
  areas:
  - real-analysis
  topics:
  - Continuity
  - Metric Spaces
relations: []
review: draft
---

::: {.problem}
Let $(X, d)$ and $(Y, \rho)$ be metric spaces, let $f: X \to Y$ be a function, and let $x_0 \in X$. Prove that the following two statements are equivalent:

1. For every $\varepsilon > 0$, there exists $\delta > 0$ such that $\rho(f(x), f(x_0)) < \varepsilon$ whenever $d(x, x_0) < \delta$.
2. For every sequence $(x_n)_{n=1}^\infty$ in $X$ with $\lim_{n \to \infty} x_n = x_0$, the image sequence satisfies $\lim_{n \to \infty} f(x_n) = f(x_0)$ in $Y$.
:::

::: {.solution}
**Goal:** Prove the equivalence between $\varepsilon$-$\delta$ continuity and sequential continuity of $f$ at a point $x_0$.

::: pf

::: pf-step

Statement (1) implies Statement (2):
    *Proof:*

::: pf-proof

::: pf-step

Assume Statement (1) holds. Let $(x_n)_{n=1}^\infty$ be a sequence in $X$ with $\lim_{n \to \infty} x_n = x_0$.

:::

::: pf-step

Let $\varepsilon > 0$ be given.

:::

::: pf-step

By (1), there exists $\delta > 0$ such that for all $x \in X$, $d(x, x_0) < \delta \implies \rho(f(x), f(x_0)) < \varepsilon$.

:::

::: pf-step

Since $x_n \to x_0$ in $(X, d)$, there exists an integer $N \ge 1$ such that $d(x_n, x_0) < \delta$ for all $n \ge N$.

:::

::: pf-step

Therefore, for all $n \ge N$, $\rho(f(x_n), f(x_0)) < \varepsilon$.

:::

::: pf-step

This proves $\lim_{n \to \infty} f(x_n) = f(x_0)$ in $(Y, \rho)$, establishing Statement (2).

:::

:::

:::

::: pf-step

Statement (2) implies Statement (1):
    *Proof:*

::: pf-proof

::: pf-step

We prove the contrapositive: suppose Statement (1) does not hold.

:::

::: {.pf-step #s2-2}

The logical negation of Statement (1) states: there exists $\varepsilon_0 > 0$ such that for every $\delta > 0$, there exists a point $x \in X$ satisfying $d(x, x_0) < \delta$ and $\rho(f(x), f(x_0)) \ge \varepsilon_0$.

:::

::: pf-step

For each positive integer $n \ge 1$, set $\delta = 1/n > 0$.

:::

::: pf-step

By step [](#s2-2){.pf-ref}, there exists a point $x_n \in X$ such that
    $$d(x_n, x_0) < \frac{1}{n} \quad \text{and} \quad \rho(f(x_n), f(x_0)) \ge \varepsilon_0.$$

:::

::: pf-step

Since $0 \le d(x_n, x_0) < 1/n$ for all $n \ge 1$, the Squeeze Theorem implies $\lim_{n \to \infty} d(x_n, x_0) = 0$, so $x_n \to x_0$ in $X$.

:::

::: pf-step

However, since $\rho(f(x_n), f(x_0)) \ge \varepsilon_0 > 0$ for all $n \ge 1$, the sequence $(f(x_n))_{n=1}^\infty$ cannot converge to $f(x_0)$ in $Y$.

:::

::: pf-step

Thus Statement (2) fails.

:::

::: pf-step

By contraposition, Statement (2) implies Statement (1).

:::

:::

:::

::: pf-step

Conclusion:

:::

:::

    *Proof:*
    Statements (1) and (2) are logically equivalent.
:::
