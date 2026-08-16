---
schema: qual/card@1
id: P-YIXSO
kind: problem
title: "Prove that if $f : [0, 1] \\to \\mathbb{R}$ is continuous then"
classification:
  areas:
  - real-analysis
  topics:
  - convergence-of-integrals
  - continuity
  - stone-weierstrass
relations: []
review: draft
---

::: {.problem title="?"}
Prove that if $f : [0, 1] \to \mathbb{R}$ is continuous then

$$\lim_{k\to\infty} \int_0^1 kx^{k-1} f(x)\, dx = f(1).$$
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

Note that for any $k \geq 1$:
$$
\int_0^1 k x^{k-1}\, dx = \left[ x^k \right]_0^1 = 1.
$$
Therefore:
$$
\int_0^1 k x^{k-1} f(x)\, dx - f(1) = \int_0^1 k x^{k-1} (f(x) - f(1))\, dx.
$$

Let $\varepsilon > 0$.
Since $f$ is continuous on $[0, 1]$ (and hence at $x = 1$), there exists $\delta \in (0, 1)$ such that:
$$
|f(x) - f(1)| < \frac{\varepsilon}{2} \quad \text{whenever } x \in [1 - \delta, 1].
$$
Also, since $f$ is continuous on the compact interval $[0, 1]$, $f$ is bounded: there exists $M > 0$ such that $|f(x) - f(1)| \leq 2M$ for all $x \in [0, 1]$.

Split the integral into two regions $[0, 1 - \delta]$ and $[1 - \delta, 1]$:
$$
\left| \int_0^1 k x^{k-1} (f(x) - f(1))\, dx \right| \leq \int_0^{1-\delta} k x^{k-1} |f(x) - f(1)|\, dx + \int_{1-\delta}^1 k x^{k-1} |f(x) - f(1)|\, dx.
$$

Estimate the second term:
$$
\int_{1-\delta}^1 k x^{k-1} |f(x) - f(1)|\, dx \leq \frac{\varepsilon}{2} \int_{1-\delta}^1 k x^{k-1}\, dx = \frac{\varepsilon}{2} (1 - (1 - \delta)^k) < \frac{\varepsilon}{2}.
$$

Estimate the first term:
$$
\int_0^{1-\delta} k x^{k-1} |f(x) - f(1)|\, dx \leq 2M \int_0^{1-\delta} k x^{k-1}\, dx = 2M (1 - \delta)^k.
$$

Since $0 < 1 - \delta < 1$, we have $\lim_{k \to \infty} (1 - \delta)^k = 0$.
Thus, there exists $K \in \mathbb{N}$ such that for all $k \geq K$:
$$
2M (1 - \delta)^k < \frac{\varepsilon}{2}.
$$

Combining the two estimates, for all $k \geq K$:
$$
\left| \int_0^1 k x^{k-1} f(x)\, dx - f(1) \right| < \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon.
$$
This proves that:
$$
\lim_{k \to \infty} \int_0^1 k x^{k-1} f(x)\, dx = f(1).
$$
:::
