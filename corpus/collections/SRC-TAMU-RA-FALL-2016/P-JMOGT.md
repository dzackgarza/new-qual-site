---
schema: qual/card@1
id: P-JMOGT
kind: problem
title: $\lim_{x\to 0}\int_{\RR}|f(y-x)-f(y)|\,dy=0$ for $f\in L^1(\RR)$
classification:
  areas:
  - real-analysis
  topics:
  - L¹
  - Continuity
  - Density
relations: []
review: draft
---

::: problem
Let $f \in L^1(\mathbb{R})$. Show that
$$
\lim_{x \to 0} \int_{\mathbb{R}} |f(y - x) - f(y)| \, dy = 0.
$$
:::

::: solution
**Goal:** Prove the continuity of translations in $L^1(\mathbb{R})$ using the density of $C_c(\mathbb{R})$ in $L^1(\mathbb{R})$ and the uniform continuity of compactly supported continuous functions.

<1>1. Approximation by compactly supported continuous functions:
    *Proof:*
    <2>1. Let $\varepsilon > 0$.
    <2>2. Since $C_c(\mathbb{R})$ (continuous functions with compact support) is dense in $L^1(\mathbb{R})$, there exists a function $g \in C_c(\mathbb{R})$ such that
    $$\|f - g\|_{L^1} = \int_{\mathbb{R}} |f(y) - g(y)| \, dy < \frac{\varepsilon}{3}.$$
    <2>3. Since $g$ has compact support, choose $M > 0$ such that $\operatorname{supp}(g) \subseteq [-M, M]$.

<1>2. Translation invariance of the $L^1$ norm:
    *Proof:*
    <2>1. For any $x \in \mathbb{R}$, by the translation invariance of the Lebesgue integral (substituting $u = y - x$):
    $$\int_{\mathbb{R}} |f(y - x) - g(y - x)| \, dy = \int_{\mathbb{R}} |f(u) - g(u)| \, du = \|f - g\|_{L^1} < \frac{\varepsilon}{3}.$$

<1>3. Splitting the integral via the triangle inequality:
    *Proof:*
    <2>1. For any $x \in \mathbb{R}$:
    $$|f(y - x) - f(y)| \le |f(y - x) - g(y - x)| + |g(y - x) - g(y)| + |g(y) - f(y)|.$$
    <2>2. Integrating over $\mathbb{R}$ and applying <1>1 and <1>2:
    $$\int_{\mathbb{R}} |f(y - x) - f(y)| \, dy \le \frac{\varepsilon}{3} + \int_{\mathbb{R}} |g(y - x) - g(y)| \, dy + \frac{\varepsilon}{3} = \frac{2\varepsilon}{3} + \int_{\mathbb{R}} |g(y - x) - g(y)| \, dy.$$

<1>4. Bounding the translation error for $g$:
    *Proof:*
    <2>1. Since $g$ is continuous with compact support on $\mathbb{R}$, $g$ is uniformly continuous on $\mathbb{R}$.
    <2>2. For any $|x| \le 1$, if $y \notin [-M - 1, M + 1]$, then $y \notin [-M, M]$ and $y - x \notin [-M, M]$, so $g(y) = 0$ and $g(y - x) = 0$.
    <2>3. Thus $\operatorname{supp}(g(\cdot - x) - g(\cdot)) \subseteq [-M - 1, M + 1]$ for all $|x| \le 1$.
    <2>4. By uniform continuity, there exists $\delta \in (0, 1)$ such that for all $|x| < \delta$ and all $y \in \mathbb{R}$:
    $$|g(y - x) - g(y)| < \frac{\varepsilon}{3(2M + 2)}.$$
    <2>5. Integrating over $[-M - 1, M + 1]$:
    $$\int_{\mathbb{R}} |g(y - x) - g(y)| \, dy = \int_{-M - 1}^{M + 1} |g(y - x) - g(y)| \, dy \le \frac{\varepsilon}{3(2M + 2)} \cdot (2M + 2) = \frac{\varepsilon}{3}.$$

<1>5. Conclusion:
    *Proof:*
    <2>1. For all $|x| < \delta$, combining <1>3 and <1>4:
    $$\int_{\mathbb{R}} |f(y - x) - f(y)| \, dy < \frac{2\varepsilon}{3} + \frac{\varepsilon}{3} = \varepsilon.$$
    <2>2. Since $\varepsilon > 0$ was arbitrary, $\lim_{x \to 0} \int_{\mathbb{R}} |f(y - x) - f(y)| \, dy = 0$.
:::

