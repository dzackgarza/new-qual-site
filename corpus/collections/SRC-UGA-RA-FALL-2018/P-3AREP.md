---
schema: qual/card@1
id: P-3AREP
kind: problem
title: $\lim_{n\to\infty}\int_1^n(1+x/n)^{-n}x^{-1/n}\,dx$
classification:
  areas:
  - real-analysis
  topics:
  - Convergence of Integrals
  - Integrals
relations: []
review: draft
---

::: problem
Compute the following limit and justify your calculations:
$$
\lim_{n \to \infty} \int_{1}^{n} \frac{d x}{\left(1+\frac{x}{n}\right)^{n} \sqrt[n]{x}}.
$$
:::

::: solution
**Goal:** Evaluate the integral limit using the Dominated Convergence Theorem on the interval $[1, \infty)$.

<1>1. Extension to $[1, \infty)$ and pointwise limit:
    *Proof:*
    <2>1. Define the sequence of functions $f_n: [1, \infty) \to \mathbb{R}$ by
    $$f_n(x) = \frac{\chi_{[1, n]}(x)}{\left(1 + \frac{x}{n}\right)^n x^{1/n}}.$$
    <2>2. Then $\int_1^n \frac{dx}{(1 + x/n)^n \sqrt[n]{x}} = \int_1^\infty f_n(x) \, dx$.
    <2>3. For each fixed $x \in [1, \infty)$:
        - For all $n > x$, $\chi_{[1, n]}(x) = 1$.
        - $\lim_{n \to \infty} \left(1 + \frac{x}{n}\right)^n = e^x$.
        - $\lim_{n \to \infty} x^{1/n} = x^0 = 1$.
    <2>4. Therefore, the pointwise limit is
    $$\lim_{n \to \infty} f_n(x) = \frac{1}{e^x \cdot 1} = e^{-x} \quad \text{for all } x \in [1, \infty).$$

<1>2. Integrable dominating function:
    *Proof:*
    <2>1. For all $x \ge 1$ and $n \ge 1$, $x^{1/n} \ge 1^{1/n} = 1$, so $\frac{1}{x^{1/n}} \le 1$.
    <2>2. For $n \ge 2$, expand $\left(1 + \frac{x}{n}\right)^n$ by the Binomial Theorem:
    $$\left(1 + \frac{x}{n}\right)^n = 1 + n \left(\frac{x}{n}\right) + \frac{n(n-1)}{2} \left(\frac{x}{n}\right)^2 + \cdots \ge 1 + x + \frac{n-1}{2n} x^2.$$
    <2>3. For all $n \ge 2$, $\frac{n-1}{2n} \ge \frac{1}{4}$, so
    $$\left(1 + \frac{x}{n}\right)^n \ge 1 + x + \frac{1}{4} x^2 > \frac{1}{4} x^2.$$
    <2>4. Thus, for all $n \ge 2$ and all $x \ge 1$:
    $$|f_n(x)| \le \frac{1}{\left(1 + \frac{x}{n}\right)^n \cdot 1} \le \frac{4}{x^2} =: g(x).$$
    <2>5. The function $g(x) = \frac{4}{x^2}$ is integrable on $[1, \infty)$:
    $$\int_1^\infty g(x) \, dx = \int_1^\infty \frac{4}{x^2} \, dx = \left[ -\frac{4}{x} \right]_1^\infty = 4 < \infty.$$

<1>3. Evaluation of the limit by Dominated Convergence:
    *Proof:*
    <2>1. By the Dominated Convergence Theorem, we may pass the limit inside the integral:
    $$\lim_{n \to \infty} \int_1^\infty f_n(x) \, dx = \int_1^\infty \lim_{n \to \infty} f_n(x) \, dx = \int_1^\infty e^{-x} \, dx.$$
    <2>2. Evaluate the integral:
    $$\int_1^\infty e^{-x} \, dx = \left[ -e^{-x} \right]_1^\infty = 0 - (-e^{-1}) = \frac{1}{e}.$$

<1>4. Conclusion:
    *Proof:*
    $\lim_{n \to \infty} \int_1^n \frac{dx}{\left(1 + \frac{x}{n}\right)^n \sqrt[n]{x}} = \frac{1}{e}$.
:::

