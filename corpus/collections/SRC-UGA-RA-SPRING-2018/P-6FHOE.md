---
schema: qual/card@1
id: P-6FHOE
kind: problem
title: Pointwise limit, non-uniform convergence, and $\lim\int_0^\infty\frac{x}{1+x^n}\,dx$
classification:
  areas:
  - real-analysis
  topics:
  - Convergence of Functions
  - Uniform Convergence
  - Convergence of Integrals
relations: []
review: draft
---

::: problem
Let
$$
f_n(x) = \frac{x}{1 + x^n}, \quad x \ge 0.
$$

(a) Show that $(f_n)$ converges pointwise on $[0, \infty)$ and find its limit. Is the convergence uniform on $[0, \infty)$?

(b) Compute
$$
\lim_{n \to \infty} \int_0^\infty f_n(x) \, dx.
$$
:::

::: solution
**Goal:** Compute the pointwise limit function in (a), disprove uniform convergence via discontinuity, and evaluate the integral limit in (b) via the Dominated Convergence Theorem.

<1>1. Part (a): Pointwise convergence of $(f_n)$.
    *Proof:*
    <2>1. Case $x \in [0, 1)$:
        - $\lim_{n \to \infty} x^n = 0$.
        - Thus $\lim_{n \to \infty} f_n(x) = \lim_{n \to \infty} \frac{x}{1 + x^n} = \frac{x}{1 + 0} = x$.
    <2>2. Case $x = 1$:
        - For all $n \ge 1$, $f_n(1) = \frac{1}{1 + 1^n} = \frac{1}{2}$.
        - Thus $\lim_{n \to \infty} f_n(1) = \frac{1}{2}$.
    <2>3. Case $x > 1$:
        - $\lim_{n \to \infty} x^n = \infty$.
        - Thus $\lim_{n \to \infty} f_n(x) = \lim_{n \to \infty} \frac{x}{1 + x^n} = 0$.
    <2>4. Thus $(f_n)$ converges pointwise on $[0, \infty)$ to the limit function:
    $$f(x) = \begin{cases} x & \text{if } 0 \le x < 1, \\ \frac{1}{2} & \text{if } x = 1, \\ 0 & \text{if } x > 1. \end{cases}$$

<1>2. Part (a): Non-uniformity of convergence on $[0, \infty)$.
    *Proof:*
    <2>1. For each $n \ge 1$, $f_n(x) = \frac{x}{1 + x^n}$ is continuous on $[0, \infty)$ since the denominator $1 + x^n \ge 1 > 0$ never vanishes.
    <2>2. The pointwise limit function $f$ is discontinuous at $x = 1$, because:
    $$\lim_{x \to 1^-} f(x) = \lim_{x \to 1^-} x = 1 \ne \frac{1}{2} = f(1), \quad \lim_{x \to 1^+} f(x) = \lim_{x \to 1^+} 0 = 0 \ne \frac{1}{2}.$$
    <2>3. By the Uniform Limit Theorem, the uniform limit of a sequence of continuous functions on $[0, \infty)$ must be continuous on $[0, \infty)$.
    <2>4. Because $f$ is not continuous, the sequence $(f_n)$ does not converge uniformly to $f$ on $[0, \infty)$.

<1>3. Part (b): Construction of an integrable dominating function.
    *Proof:*
    <2>1. For $x \in [0, 1]$ and all $n \ge 1$:
    $$0 \le f_n(x) = \frac{x}{1 + x^n} \le x \le 1.$$
    <2>2. For $x \in (1, \infty)$ and all $n \ge 3$:
    $$0 \le f_n(x) = \frac{x}{1 + x^n} \le \frac{x}{x^n} = \frac{1}{x^{n-1}} \le \frac{1}{x^2}.$$
    <2>3. Define $g: [0, \infty) \to \mathbb{R}$ by:
    $$g(x) = \begin{cases} 1 & \text{if } 0 \le x \le 1, \\ \frac{1}{x^2} & \text{if } x > 1. \end{cases}$$
    <2>4. The function $g$ is Lebesgue integrable on $[0, \infty)$:
    $$\int_0^\infty g(x) \, dx = \int_0^1 1 \, dx + \int_1^\infty \frac{1}{x^2} \, dx = 1 + \left[ -\frac{1}{x} \right]_1^\infty = 1 + 1 = 2 < \infty.$$
    <2>5. For all $n \ge 3$ and all $x \ge 0$, $|f_n(x)| \le g(x)$.

<1>4. Part (b): Application of the Dominated Convergence Theorem.
    *Proof:*
    <2>1. The sequence $(f_n)_{n=3}^\infty$ is dominated by $g \in L^1([0, \infty))$ and converges pointwise almost everywhere to $f(x)$.
    <2>2. By the Dominated Convergence Theorem:
    $$\lim_{n \to \infty} \int_0^\infty f_n(x) \, dx = \int_0^\infty f(x) \, dx.$$
    <2>3. Evaluate the integral:
    $$\int_0^\infty f(x) \, dx = \int_0^1 x \, dx + \int_1^\infty 0 \, dx = \left[ \frac{x^2}{2} \right]_0^1 = \frac{1}{2}.$$

<1>5. Conclusion:
    *Proof:*
    $(f_n)$ converges pointwise to $f$, the convergence is not uniform, and $\lim_{n \to \infty} \int_0^\infty f_n(x) \, dx = \frac{1}{2}$.
:::

