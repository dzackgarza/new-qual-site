---
schema: qual/card@1
id: P-KZZ7M
kind: problem
title: $\lim_{n\to\infty}\int_{1/n}^1 f_n=\int_0^1 f$ for uniform limits of continuous
  functions on $[0,1]$
classification:
  areas:
  - real-analysis
  topics:
  - Uniform Convergence
  - Convergence of Integrals
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: problem
Suppose $f_n:[0,1]\to\mathbb{R}$ are continuous functions converging uniformly to $f:[0,1]\to\mathbb{R}$.
Either prove that $\displaystyle\lim_{n\to\infty}\int_{1/n}^1 f_n(x)\,dx=\int_0^1 f(x)\,dx$ or give a counterexample.
:::
::: {.solution}
<1>1. Claim: $\lim_{n\to\infty}\int_{1/n}^1 f_n(x)\,dx = \int_0^1 f(x)\,dx$.
Proof: split the difference into the convergence part (uniform) and the endpoint part (small interval).

<1>2. $\int_{1/n}^1 f_n = \int_{1/n}^1 f + \int_{1/n}^1 (f_n - f)$, and $\left|\int_{1/n}^1 (f_n - f)\right| \le \|f_n - f\|_\infty \cdot 1 \to 0$.
Proof: uniform convergence $f_n \to f$ means $\|f_n - f\|_\infty \to 0$; the interval has length $\le 1$.

<1>3. $\int_{1/n}^1 f \to \int_0^1 f$.
Proof: $f$ is continuous on $[0,1]$ (uniform limit of continuous functions), hence bounded, $|f| \le M$; then $\left|\int_0^{1/n} f\right| \le M/n \to 0$, so $\int_{1/n}^1 f = \int_0^1 f - \int_0^{1/n} f \to \int_0^1 f$.

<1>4. Q.E.D. Proof: <1>2 and <1>3 combine: $\int_{1/n}^1 f_n = \int_{1/n}^1 f + o(1) \to \int_0^1 f$.
:::
