---
schema: qual/card@1
id: P-C3MKZ
kind: problem
title: 'Convergence of $\sum_{n=1}^\infty \frac{x^n}{1+n|x|^n}$'
classification:
  areas:
  - real-analysis
  topics:
  - Series of Functions
  - Convergence of Functions
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Determine the values of $x\in\mathbb{R}$ for which $\displaystyle\sum_{n=1}^\infty \frac{x^n}{1+n|x|^n}$ converges, justifying your answer carefully.
:::
::: {.solution}
::: pf

::: {.pf-step #s1}
For $|x| < 1$: the series converges absolutely.

::: pf-proof
$\left|\dfrac{x^n}{1 + n|x|^n}\right| \le |x|^n$ (denominator $\ge 1$), and $\sum |x|^n$ is a convergent geometric series.
:::

:::

::: {.pf-step #s2}
At $x = 1$: the series diverges to $+\infty$.

::: pf-proof
every term is positive and $\dfrac{1}{1+n} \ge \dfrac{1}{2n}$, so the series dominates a divergent harmonic tail.
:::

:::

::: {.pf-step #s3}
At $x = -1$: the series converges.

::: pf-proof
$\sum \dfrac{(-1)^n}{1+n}$ is an alternating series whose terms decrease to $0$; Leibniz's test applies.
:::

:::

::: {.pf-step #s4}
For $x > 1$: the series diverges to $+\infty$.

::: pf-proof
every term is positive and $\dfrac{x^n}{1 + nx^n} = \dfrac{1}{n + x^{-n}} \ge \dfrac{1}{n+1}$, so the series dominates $\sum \dfrac{1}{n+1} = \infty$.
:::

:::

::: {.pf-step #s5}
For $x < -1$: the series converges (conditionally).

::: pf-proof

::: {.pf-step #s5-1}
Write the terms as $(-1)^n a_n$ with $a_n = \dfrac{|x|^n}{1 + n|x|^n} = \dfrac{1}{n + |x|^{-n}}$.

::: pf-proof
$x^n = (-1)^n|x|^n$; divide numerator and denominator by $|x|^n$.
:::

:::

::: {.pf-step #s5-2}
$a_n \downarrow 0$.

::: pf-proof
$n + |x|^{-n} \uparrow \infty$; the increment $\big((n+1) + |x|^{-(n+1)}\big) - \big(n + |x|^{-n}\big) = 1 - |x|^{-n}(1 - 1/|x|) > 0$ since $|x|^{-n}(1 - 1/|x|) < 1$ for $|x| > 1$.
:::

:::

::: pf-step
$\sum (-1)^n a_n$ converges.

::: pf-proof
alternating series test with step [](#s5-2){.pf-ref}.
:::

:::

::: pf-step
The convergence is not absolute.

::: pf-proof
$a_n \ge \dfrac{1}{n+1}$ (by step [](#s5-1){.pf-ref}), so $\sum a_n$ diverges.
:::

:::

:::

:::

:::

::: pf-qed
the series converges for $x \in (-\infty, 1)$ — absolutely for $|x| < 1$, conditionally for $x \le -1$ — and diverges for $x \ge 1$.

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref}, [](#s3){.pf-ref}, [](#s4){.pf-ref}, and [](#s5){.pf-ref} cover all real $x$.
:::

:::
:::
