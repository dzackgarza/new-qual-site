---
schema: qual/card@1
id: P-VYRJF
kind: problem
title: $\lim_{n\to\infty}\int_0^n(1+x^2/n)^{-(n+1)}\,dx$
classification:
  areas:
  - real-analysis
  topics:
  - Convergence of Integrals
  - Integrals
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
  note: Checked against Problem 5 of the official UGA Spring 2020 Real Analysis qualifying examination DOCX.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-11
  note: Reviewed the Bernoulli domination, pointwise limit, dominated convergence step, and Gaussian integral evaluation; the proof is correct.
---

::: {.problem}
Compute the following limit and justify all calculations:
$$
\lim_{n \to \infty} \int_0^n \left(1 + \frac{x^2}{n}\right)^{-(n+1)} \, dx.
$$
:::

::: {.hint}
Bernoulli's inequality gives $\left(1+\frac{x^2}{n}\right)^{n+1}\ge 1+x^2$, so $\frac{1}{1+x^2}$ dominates the integrands; the pointwise limit is $e^{-x^2}$.
:::

::: {.solution}

For $n \ge 1$ and $x \ge 0$, let $f_n(x) \coloneqq \chi_{[0, n]}(x) \left(1 + \frac{x^2}{n}\right)^{-(n+1)}$, so that the $n$th integral is $\int_0^\infty f_n(x)\,dx$.

::: pf

::: {.pf-step #pointwise}

$f_n(x) \to e^{-x^2}$ for every $x \ge 0$.

::: pf-proof

For fixed $x$, $\chi_{[0,n]}(x) = 1$ once $n \ge x$, and $f_n(x) = \left(1 + \frac{x^2}{n}\right)^{-1}\left(1 + \frac{x^2}{n}\right)^{-n}$ with $1 + \frac{x^2}{n} \to 1$ and $\left(1 + \frac{x^2}{n}\right)^n \to e^{x^2}$.

:::

:::

::: {.pf-step #dominated}

$0 \le f_n(x) \le \frac{1}{1+x^2}$ for all $n \ge 1$ and $x \ge 0$, and $\int_0^\infty \frac{dx}{1+x^2} = \frac{\pi}{2}$.

::: pf-proof

By Bernoulli's inequality, $\left(1 + \frac{x^2}{n}\right)^{n+1} \ge \left(1 + \frac{x^2}{n}\right)^n \ge 1 + x^2$. Take reciprocals.

:::

:::

::: {.pf-step #gaussian}

$\int_0^\infty e^{-x^2}\,dx = \frac{\sqrt\pi}{2}$.

::: pf-proof

Let $I = \int_0^\infty e^{-x^2}\,dx$. Since the integrand is even, Tonelli's theorem and polar coordinates give
$$
I^2 = \frac14\int_{\RR^2} e^{-(x^2+y^2)}\,dx\,dy = \frac14\int_0^{2\pi}\int_0^\infty e^{-r^2}r\,dr\,d\theta = \frac14\cdot 2\pi\cdot\frac12 = \frac{\pi}{4},
$$
and $I > 0$.

:::

:::

::: pf-step

$\displaystyle\lim_{n \to \infty} \int_0^n \left(1 + \frac{x^2}{n}\right)^{-(n+1)} \, dx = \boxed{\frac{\sqrt{\pi}}{2}}$.

::: pf-proof

By steps [](#pointwise){.pf-ref} and [](#dominated){.pf-ref}, the dominated convergence theorem gives the limit $\int_0^\infty e^{-x^2}\,dx$, which step [](#gaussian){.pf-ref} evaluates.

:::

:::

:::

:::
