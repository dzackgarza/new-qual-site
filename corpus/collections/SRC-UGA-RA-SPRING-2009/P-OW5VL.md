---
schema: qual/card@1
id: P-OW5VL
kind: problem
title: $\lim_{k\to\infty}\int_0^1 kx^{k-1}f(x)\,dx=f(1)$ for continuous $f$ on $[0,1]$
classification:
  areas:
  - real-analysis
  topics:
  - Convergence of Integrals
  - Continuity
  - Stone-Weierstrass
relations: []
review: draft
---

::: problem
Prove that if $f: [0, 1] \to \mathbb{R}$ is continuous, then
$$
\lim_{k \to \infty} \int_0^1 k x^{k-1} f(x) \, dx = f(1).
$$
:::

::: solution
**Goal:** Prove that $\lim_{k \to \infty} \int_0^1 k x^{k-1} f(x) \, dx = f(1)$ using the continuity of $f$ and the approximate identity property of the kernel $k x^{k-1}$.

<1>1. Integral of the kernel:
    *Proof:*
    <2>1. For every integer $k \ge 1$, compute the integral of the weight function:
    $$\int_0^1 k x^{k-1} \, dx = \left[ x^k \right]_0^1 = 1 - 0 = 1.$$
    <2>2. Multiplying by the constant $f(1)$:
    $$f(1) = \int_0^1 k x^{k-1} f(1) \, dx.$$
    <2>3. Subtracting the two expressions gives
    $$\int_0^1 k x^{k-1} f(x) \, dx - f(1) = \int_0^1 k x^{k-1} (f(x) - f(1)) \, dx.$$

<1>2. Boundedness and continuity of $f$:
    *Proof:*
    <2>1. Since $f$ is continuous on the compact interval $[0, 1]$, the difference $|f(x) - f(1)|$ is continuous and bounded:
    $$M = \sup_{x \in [0, 1]} |f(x) - f(1)| < \infty.$$
    <2>2. If $M = 0$, $f$ is constant, and the result is immediate. Assume $M > 0$.
    <2>3. Let $\varepsilon > 0$ be given.
    <2>4. By continuity of $f$ at $x = 1$, there exists $\delta \in (0, 1)$ such that
    $$x \in [1 - \delta, 1] \implies |f(x) - f(1)| < \frac{\varepsilon}{2}.$$

<1>3. Splitting the integral:
    *Proof:*
    <2>1. Split the domain $[0, 1] = [0, 1 - \delta] \cup [1 - \delta, 1]$:
    $$\left| \int_0^1 k x^{k-1} (f(x) - f(1)) \, dx \right| \le \int_0^{1-\delta} k x^{k-1} |f(x) - f(1)| \, dx + \int_{1-\delta}^1 k x^{k-1} |f(x) - f(1)| \, dx.$$
    <2>2. Bound on the near-boundary interval $[1 - \delta, 1]$:
    $$\int_{1-\delta}^1 k x^{k-1} |f(x) - f(1)| \, dx \le \frac{\varepsilon}{2} \int_{1-\delta}^1 k x^{k-1} \, dx \le \frac{\varepsilon}{2} \int_0^1 k x^{k-1} \, dx = \frac{\varepsilon}{2}.$$
    <2>3. Bound on the away interval $[0, 1 - \delta]$:
    $$\int_0^{1-\delta} k x^{k-1} |f(x) - f(1)| \, dx \le M \int_0^{1-\delta} k x^{k-1} \, dx = M \left[ x^k \right]_0^{1-\delta} = M (1 - \delta)^k.$$
    <2>4. Since $0 < 1 - \delta < 1$, $\lim_{k \to \infty} (1 - \delta)^k = 0$.
    <2>5. Choose an integer $K \ge 1$ such that for all $k \ge K$:
    $$M (1 - \delta)^k < \frac{\varepsilon}{2}.$$
    <2>6. Combining the bounds, for all $k \ge K$:
    $$\left| \int_0^1 k x^{k-1} f(x) \, dx - f(1) \right| < \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon.$$

<1>4. Conclusion:
    *Proof:*
    Since $\varepsilon > 0$ was arbitrary, $\lim_{k \to \infty} \int_0^1 k x^{k-1} f(x) \, dx = f(1)$.
:::
