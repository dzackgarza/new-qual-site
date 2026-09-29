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

::: pf

::: pf-step
Pointwise limit of the integrands:

::: pf-proof

::: pf-step
Define the sequence of functions $f_n: [0, \infty) \to \mathbb{R}$ by
$$f_n(x) = \chi_{[0, n]}(x) \left(1 + \frac{x^2}{n}\right)^{-(n+1)}.$$

:::

::: pf-step
For any fixed $x \ge 0$, for all $n > x$, $\chi_{[0, n]}(x) = 1$.

:::

::: pf-step
Rewrite the expression:
$$f_n(x) = \frac{1}{\left(1 + \frac{x^2}{n}\right) \left(1 + \frac{x^2}{n}\right)^n}.$$

:::

::: pf-step
Compute the component limits as $n \to \infty$:
$$\lim_{n \to \infty} \left(1 + \frac{x^2}{n}\right) = 1, \quad \lim_{n \to \infty} \left(1 + \frac{x^2}{n}\right)^n = e^{x^2}.$$

:::

::: pf-step
Thus for every $x \in [0, \infty)$:
$$\lim_{n \to \infty} f_n(x) = \frac{1}{1 \cdot e^{x^2}} = e^{-x^2}.$$

:::

:::

:::

::: pf-step
Construction of an integrable dominating function:

::: pf-proof

::: pf-step
By Bernoulli's inequality (or the binomial expansion), for any $u = \frac{x^2}{n} \ge 0$:
$$\left(1 + \frac{x^2}{n}\right)^n \ge 1 + n \left(\frac{x^2}{n}\right) = 1 + x^2.$$

:::

::: pf-step
Since $1 + \frac{x^2}{n} \ge 1$:
$$\left(1 + \frac{x^2}{n}\right)^{n+1} = \left(1 + \frac{x^2}{n}\right) \left(1 + \frac{x^2}{n}\right)^n \ge 1 \cdot (1 + x^2) = 1 + x^2.$$

:::

::: pf-step
Taking reciprocals:
$$|f_n(x)| \le \chi_{[0, n]}(x) \frac{1}{1 + x^2} \le \frac{1}{1 + x^2} =: g(x) \quad \text{for all } x \ge 0 \text{ and all } n \ge 1.$$

:::

::: pf-step
The function $g(x) = \frac{1}{1 + x^2}$ is Lebesgue integrable on $[0, \infty)$:
$$\int_0^\infty g(x) \, dx = \int_0^\infty \frac{dx}{1 + x^2} = \left[ \arctan(x) \right]_0^\infty = \frac{\pi}{2} < \infty.$$

:::

:::

:::

::: pf-step
Application of the Dominated Convergence Theorem:

::: pf-proof

::: pf-step
The sequence $(f_n)$ is dominated by the integrable function $g \in L^1([0, \infty))$ and converges pointwise to $e^{-x^2}$.

:::

::: pf-step
By the Dominated Convergence Theorem:
$$\lim_{n \to \infty} \int_0^n \left(1 + \frac{x^2}{n}\right)^{-(n+1)} \, dx = \lim_{n \to \infty} \int_0^\infty f_n(x) \, dx = \int_0^\infty \lim_{n \to \infty} f_n(x) \, dx = \int_0^\infty e^{-x^2} \, dx.$$

:::

:::

:::

::: pf-step
Evaluation of the limiting Gaussian integral:

::: pf-proof

::: pf-step
Let $I = \int_0^\infty e^{-x^2} \, dx$.

:::

::: pf-step
Since $e^{-x^2}$ is an even function, $I = \frac{1}{2} \int_{-\infty}^\infty e^{-x^2} \, dx$.

:::

::: pf-step
By Tonelli's Theorem and conversion to polar coordinates:
$$I^2 = \frac{1}{4} \int_{\mathbb{R}} e^{-x^2} \, dx \int_{\mathbb{R}} e^{-y^2} \, dy = \frac{1}{4} \int_{\mathbb{R}^2} e^{-(x^2 + y^2)} \, dx \, dy = \frac{1}{4} \int_0^{2\pi} \int_0^\infty e^{-r^2} r \, dr \, d\theta.$$

:::

::: pf-step
Compute the radial integral with $u = r^2$, $du = 2r \, dr$:
$$\int_0^\infty e^{-r^2} r \, dr = \frac{1}{2} \int_0^\infty e^{-u} \, du = \frac{1}{2} [-e^{-u}]_0^\infty = \frac{1}{2}.$$

:::

::: pf-step
Thus:
$$I^2 = \frac{1}{4} (2\pi) \left(\frac{1}{2}\right) = \frac{\pi}{4} \implies I = \frac{\sqrt{\pi}}{2}.$$

:::

:::

:::

::: pf-step
Conclusion:

::: pf-proof
$\lim_{n \to \infty} \int_0^n \left(1 + \frac{x^2}{n}\right)^{-(n+1)} \, dx = \frac{\sqrt{\pi}}{2}$.
:::

:::

:::

:::
