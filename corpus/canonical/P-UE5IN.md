---
schema: qual/card@1
id: P-UE5IN
kind: problem
title: "Compute the following limit and justify your calculations: $\\lim_{n \\rightarrow \\infty} \\int_{1}^{n} \\frac{d x}{\\left(1+\\frac{x}{n}\\right)^{n} \\sqrt[n]{x}}$"
classification:
  areas:
  - real-analysis
  topics:
  - integrals
  - convergence-of-integrals
relations: []
review: draft
solved: true
---

::: problem
Compute the following limit and justify your calculations:
$$
\lim_{n \rightarrow \infty} \int_{1}^{n} \frac{d x}{\left(1+\frac{x}{n}\right)^{n} \sqrt[n]{x}}
$$
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

Rewrite the integral over $[1, \infty)$ using the characteristic function:
$$
I_n = \int_1^\infty f_n(x) \, dx, \qquad \text{where } f_n(x) = \frac{\mathbf{1}_{[1, n]}(x)}{\left(1 + \frac{x}{n}\right)^n x^{1/n}}.
$$

1. **Pointwise limit:** For each fixed $x \geq 1$, as $n \to \infty$:

   - $\mathbf{1}_{[1, n]}(x) \to 1$,

   - $\left(1 + \frac{x}{n}\right)^n \to e^x$,

   - $x^{1/n} = e^{\frac{1}{n} \ln x} \to e^0 = 1$.

   Therefore, the pointwise limit of $f_n(x)$ for all $x \geq 1$ is:
   $$
   f(x) = \lim_{n \to \infty} f_n(x) = \frac{1}{e^x} = e^{-x}.
   $$

2. **Dominating function:** For all $n \geq 2$ and $x \in [1, n]$:

   - Since $x \geq 1$, $x^{1/n} \geq 1$, so $\frac{1}{x^{1/n}} \leq 1$.

   - By the binomial theorem or Bernoulli's inequality, for $n \geq 2$ and $x \geq 1$:
     $$
     \left(1 + \frac{x}{n}\right)^n = 1 + x + \frac{n(n-1)}{2n^2} x^2 + \cdots \geq 1 + x + \frac{1}{4} x^2 \geq \frac{1}{4} x^2.
     $$
     Alternatively, $(1 + x/n)^n \geq 1 + x + x^2/4$ for all $n \geq 2$.

   - For a cleaner integrable bound on $[1, \infty)$, note that $(1 + x/n)^n$ increases monotonically to $e^x$, and for $n \geq 2$, $(1 + x/n)^n \geq (1 + x/2)^2 = 1 + x + x^2/4$.

   Define $g(x) = \frac{1}{1 + x^2/4}$.
   Then $|f_n(x)| \leq g(x)$ for all $x \in [1, \infty)$ and all $n \geq 2$.
   Since $\int_1^\infty g(x) \, dx = \int_1^\infty \frac{4}{4 + x^2} \, dx = 2 \left[\arctan(x/2)\right]_1^\infty = 2(\pi/2 - \arctan(1/2)) < \infty$, the dominating function $g$ is integrable on $[1, \infty)$.

3. **Application of the Dominated Convergence Theorem:** By the Lebesgue Dominated Convergence Theorem:
   $$
   \lim_{n \to \infty} \int_1^n \frac{dx}{\left(1 + \frac{x}{n}\right)^n \sqrt[n]{x}} = \int_1^\infty \lim_{n \to \infty} f_n(x) \, dx = \int_1^\infty e^{-x} \, dx = \left[-e^{-x}\right]_1^\infty = e^{-1} = \frac{1}{e}.
   $$
:::
