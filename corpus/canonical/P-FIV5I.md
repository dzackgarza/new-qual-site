---
schema: qual/card@1
id: P-FIV5I
kind: problem
title: Let Show that this sequence converges pointwise and find its limit. Is...
classification:
  areas:
  - real-analysis
  topics:
  - uniform-convergence
  - integrals
  - convergence-of-integrals
relations: []
review: draft
solved: true
---

::: problem
Let
$$
f_{n}(x):=\frac{x}{1+x^{n}}, \quad x \geq 0.
$$

a.  Show that this sequence converges pointwise and find its limit. Is the convergence uniform on $[0, \infty)$?

b.  Compute
    $$
    \lim _{n \rightarrow \infty} \int_{0}^{\infty} f_{n}(x) d x
    $$
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**(a) Pointwise convergence and uniformity:**

For $x \geq 0$:
- If $0 \leq x < 1$, then $x^n \to 0$ as $n \to \infty$, so $f_n(x) \to \frac{x}{1+0} = x$.
- If $x = 1$, then $f_n(1) = \frac{1}{1+1} = \frac{1}{2}$ for all $n \geq 1$, so $f_n(1) \to \frac{1}{2}$.
- If $x > 1$, then $x^n \to \infty$ as $n \to \infty$, so $f_n(x) = \frac{x}{1+x^n} \to 0$.

Thus, $f_n$ converges pointwise to the function:
$$
f(x) = \begin{cases} x & \text{if } 0 \leq x < 1, \\ 1/2 & \text{if } x = 1, \\ 0 & \text{if } x > 1. \end{cases}
$$
Each $f_n(x) = \frac{x}{1+x^n}$ is continuous on $[0, \infty)$, but the pointwise limit $f(x)$ is discontinuous at $x = 1$ (since $\lim_{x \to 1^-} f(x) = 1 \neq f(1) = 1/2$).
Since the uniform limit of continuous functions must be continuous, the convergence **cannot be uniform** on $[0, \infty)$ (nor on any interval containing $1$).

**(b) Computing $\lim_{n \to \infty} \int_0^\infty f_n(x) \, dx$:**

Split the domain into $[0, 1]$ and $[1, \infty)$:
$$
\int_0^\infty f_n(x) \, dx = \int_0^1 \frac{x}{1+x^n} \, dx + \int_1^\infty \frac{x}{1+x^n} \, dx.
$$

1. On $[0, 1]$: $0 \leq f_n(x) = \frac{x}{1+x^n} \leq x \leq 1$. The constant function $g(x) = 1$ is integrable on $[0, 1]$.
   By the Dominated Convergence Theorem:
   $$
   \lim_{n \to \infty} \int_0^1 f_n(x) \, dx = \int_0^1 f(x) \, dx = \int_0^1 x \, dx = \frac{1}{2}.
   $$

2. On $[1, \infty)$ for $n \geq 4$:
   $$
   0 \leq f_n(x) = \frac{x}{1+x^n} \leq \frac{x}{x^n} = \frac{1}{x^{n-1}} \leq \frac{1}{x^3}.
   $$
   Since $g(x) = \frac{1}{x^3}$ is integrable on $[1, \infty)$ (with $\int_1^\infty x^{-3} \, dx = 1/2 < \infty$), by the Dominated Convergence Theorem:
   $$
   \lim_{n \to \infty} \int_1^\infty f_n(x) \, dx = \int_1^\infty \lim_{n \to \infty} f_n(x) \, dx = \int_1^\infty 0 \, dx = 0.
   $$

Combining the two parts gives:
$$
\lim_{n \to \infty} \int_0^\infty f_n(x) \, dx = \frac{1}{2} + 0 = \frac{1}{2}.
$$
:::
