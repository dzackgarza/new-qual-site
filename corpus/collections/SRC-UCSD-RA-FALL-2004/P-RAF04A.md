---
schema: qual/card@1
id: P-RAF04A
kind: problem
title: Three Fubini and dominated-convergence limits and integrals
classification:
  areas:
  - real-analysis
  topics:
  - Fubini Theorem
  - Dominated Convergence
  - Improper Integrals
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Problem 1 of the official UCSD Fall 2004 real-analysis qualifying exam.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Find, with justification, the values of the following limits and integrals:

(a) $\displaystyle\lim_{n \to \infty} \int_0^\infty \cos\left(\frac{x}{n}\right) e^{-x} \, dx$

(b) $\displaystyle\int_0^\infty \left[\int_0^\infty \frac{x}{1 + x^2} e^{-xt} \, dx\right] dt$

(c) $\displaystyle\lim_{n \to \infty} \int_{-\infty}^\infty e^{-|x+n|} \, dx$
:::

::: {.solution}

::: pf

::: {.pf-step #s1}
Part (a): Evaluation of $\lim_{n \to \infty} \int_0^\infty \cos\left(\frac{x}{n}\right) e^{-x} \, dx$:

::: pf-proof

::: pf-step
Let $f_n(x) = \cos(x/n) e^{-x}$ on $(0, \infty)$.
For each fixed $x \in (0, \infty)$, $\lim_{n \to \infty} x/n = 0$, so:
\[
\lim_{n \to \infty} f_n(x) = \cos(0) e^{-x} = e^{-x}.
\]

::: pf-proof
continuity of cosine at 0.
:::

:::

::: pf-step
For all $n \ge 1$ and $x > 0$:
\[
|f_n(x)| = \left| \cos\left(\frac{x}{n}\right) \right| e^{-x} \le e^{-x} =: g(x).
\]
The dominating function $g(x) = e^{-x}$ is integrable on $(0, \infty)$ since $\int_0^\infty e^{-x} \, dx = 1 < \infty$.

::: pf-proof
$|\cos \theta| \le 1$.
:::

:::

::: pf-step
By the Lebesgue Dominated Convergence Theorem:
\[
\lim_{n \to \infty} \int_0^\infty \cos\left(\frac{x}{n}\right) e^{-x} \, dx = \int_0^\infty \lim_{n \to \infty} f_n(x) \, dx = \int_0^\infty e^{-x} \, dx = 1.
\]

::: pf-proof
Lebesgue Dominated Convergence Theorem.
:::

:::

:::

:::

::: pf-step
Part (b): Evaluation of $\int_0^\infty \left[ \int_0^\infty \frac{x}{1 + x^2} e^{-xt} \, dx \right] dt$:

::: pf-proof

::: pf-step
The integrand $f(x, t) = \frac{x}{1 + x^2} e^{-xt}$ is non-negative and measurable on the product domain $(0, \infty) \times (0, \infty)$.
By Tonelli’s Theorem, the order of integration can be exchanged:
\[
\int_0^\infty \left[ \int_0^\infty \frac{x}{1 + x^2} e^{-xt} \, dx \right] dt = \int_0^\infty \frac{x}{1 + x^2} \left[ \int_0^\infty e^{-xt} \, dt \right] dx.
\]

::: pf-proof
Tonelli’s Theorem for non-negative measurable functions.
:::

:::

::: pf-step
For each fixed $x > 0$, evaluating the inner integral over $t$:
\[
\int_0^\infty e^{-xt} \, dt = \left[ -\frac{e^{-xt}}{x} \right]_{t=0}^{t=\infty} = \frac{1}{x}.
\]

::: pf-proof
antiderivative of exponential function.
:::

:::

::: pf-step
Substituting into the outer integral:
\[
\int_0^\infty \frac{x}{1 + x^2} \cdot \frac{1}{x} \, dx = \int_0^\infty \frac{1}{1 + x^2} \, dx = \Big[ \arctan(x) \Big]_0^\infty = \frac{\pi}{2} - 0 = \frac{\pi}{2}.
\]

::: pf-proof
standard antiderivative of $\frac{1}{1+x^2}$.
:::

:::

:::

:::

::: {.pf-step #s3}
Part (c): Evaluation of $\lim_{n \to \infty} \int_{-\infty}^\infty e^{-|x+n|} \, dx$:

::: pf-proof

::: pf-step
For each $n \in \mathbb{N}$, make the linear substitution $u = x + n$, so $du = dx$.
The integral becomes:
\[
\int_{-\infty}^\infty e^{-|x+n|} \, dx = \int_{-\infty}^\infty e^{-|u|} \, du.
\]

::: pf-proof
translation invariance of Lebesgue integration.
:::

:::

::: pf-step
Evaluating the integral by symmetry:
\[
\int_{-\infty}^\infty e^{-|u|} \, du = 2 \int_0^\infty e^{-u} \, du = 2 \Big[ -e^{-u} \Big]_0^\infty = 2(1) = 2.
\]

::: pf-proof
symmetry of even function.
:::

:::

::: pf-step
Since the integral is constant and equal to $2$ for every $n \in \mathbb{N}$, its limit is:
\[
\lim_{n \to \infty} \int_{-\infty}^\infty e^{-|x+n|} \, dx = \lim_{n \to \infty} 2 = 2.
\]

::: pf-proof
limit of a constant sequence.
:::

:::

:::

:::

::: pf-step
Conclusion: The values are (a) $1$, (b) $\frac{\pi}{2}$, and (c) $2$.

::: pf-proof
step [](#s1){.pf-ref} through step [](#s3){.pf-ref}.
:::

:::

:::
:::
