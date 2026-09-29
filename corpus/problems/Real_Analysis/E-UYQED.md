---
schema: qual/card@1
id: E-UYQED
kind: problem
title: Uniform, pointwise, and a.e. convergence, and uniform convergence of $\sum
  x^n/n!$ on compacta
classification:
  areas:
  - real-analysis
  topics:
  - Uniform Convergence
  - Convergence of Functions
  - Series of Functions
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.exercise}
- Prove that uniform convergence implies pointwise convergence implies a.e. convergence, but none of the implications may be reversed.

- Show that $\sum {x^n \over n!}$ converges uniformly on any compact subset of $\RR$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

If $f_n \to f$ uniformly, then $f_n \to f$ pointwise.

::: pf-proof

$|f_n(x) - f(x)| \leq \sup_y|f_n(y) - f(y)| \to 0$ for each fixed $x$.

:::

:::

::: {.pf-step #s2}

If $f_n \to f$ pointwise, then $f_n \to f$ a.e.

::: pf-proof

The set where $f_n(x) \not\to f(x)$ is empty, hence null.

:::

:::

::: {.pf-step #s3}

$f_n(x) = x^n$ on $[0,1]$ converges pointwise but not uniformly.

::: pf-proof

$x^n \to 0$ for $0 \le x < 1$ and $1^n = 1$, so $f_n \to f$ pointwise with $f = 0$ on $[0,1)$ and $f(1) = 1$. At $x = 1 - 1/n$, $|f_n(x) - f(x)| = (1 - 1/n)^n \to e^{-1}$, so $\sup_{[0,1]}|f_n - f| \not\to 0$.

:::

:::

::: {.pf-step #s4}

$f_n = \chi_{[0, 1/n)}$ on $[0,1]$ converges to $0$ a.e. but not pointwise to $0$.

::: pf-proof

For every $x > 0$, $f_n(x) = 0$ once $1/n \le x$, so $f_n \to 0$ off the null set $\theset{0}$. But $f_n(0) = 1$ for every $n$.

:::

:::

::: {.pf-step #s5}

$\sum_{n=0}^\infty \frac{x^n}{n!}$ converges uniformly on every compact $K \subseteq \RR$.

::: pf-proof

Choose $M$ with $K \subseteq [-M, M]$. On $K$, $\left|\frac{x^n}{n!}\right| \le \frac{M^n}{n!}$, and $\sum_n \frac{M^n}{n!}$ converges by the ratio test, since $\frac{M^{n+1}/(n+1)!}{M^n/n!} = \frac{M}{n+1} \to 0$. The Weierstrass M-test gives uniform convergence on $K$.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref} and [](#s2){.pf-ref} are the implications, steps [](#s3){.pf-ref} and [](#s4){.pf-ref} show that neither reverses, and step [](#s5){.pf-ref} is the second part.

:::

:::

:::
