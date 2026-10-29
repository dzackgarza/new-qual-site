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

::: {.problem}
Compute the following limit and justify your calculations:
$$
\lim_{n \to \infty} \int_{1}^{n} \frac{d x}{\left(1+\frac{x}{n}\right)^{n} \sqrt[n]{x}}.
$$
:::

::: {.solution}

For $n \ge 1$ and $x \ge 1$, let
$$
f_n(x) \coloneqq \frac{\chi_{[1, n]}(x)}{\left(1 + \frac{x}{n}\right)^n x^{1/n}},
$$
so that the $n$th integral is $\int_1^\infty f_n(x)\,dx$.

::: pf

::: {.pf-step #pointwise}

$f_n(x) \to e^{-x}$ for every $x \ge 1$.

::: pf-proof

For fixed $x$, $\chi_{[1,n]}(x) = 1$ once $n \ge x$, $\left(1 + \frac{x}{n}\right)^n \to e^x$, and $x^{1/n} \to 1$.

:::

:::

::: {.pf-step #dominated}

$0 \le f_n(x) \le 4/x^2$ for all $n \ge 2$ and $x \ge 1$, and $\int_1^\infty 4/x^2\,dx = 4$.

::: pf-proof

Since $x \ge 1$, $x^{1/n} \ge 1$. For $n \ge 2$ the binomial theorem gives $\left(1 + \frac{x}{n}\right)^n \ge \binom n2\frac{x^2}{n^2} = \frac{n-1}{2n}x^2 \ge \frac{x^2}{4}$. Hence $f_n(x) \le 4/x^2$.

:::

:::

::: pf-step

$\displaystyle\lim_{n \to \infty} \int_{1}^{n} \frac{dx}{\left(1+\frac{x}{n}\right)^{n} \sqrt[n]{x}} = \boxed{\frac{1}{e}}$.

::: pf-proof

By steps [](#pointwise){.pf-ref} and [](#dominated){.pf-ref}, the dominated convergence theorem applies, so the limit is $\int_1^\infty e^{-x}\,dx = e^{-1}$.

:::

:::

:::

:::
