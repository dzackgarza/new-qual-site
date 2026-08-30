---
schema: qual/card@1
id: P-RASP18D
kind: problem
title: "Riemann-Lebesgue lemma for derivatives of dilated functions"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: problem
Let $\varphi : \mathbb{R} \to \mathbb{R}$ be a $C^1$-function such that $M := \sup_{x \in \mathbb{R}} [|\varphi(x)| + |\varphi'(x)|] < \infty$.

1. If $f \in C_c^1(\mathbb{R})$, show
$$
\left|\int_{\mathbb{R}} f(x) \varphi'(\lambda x)\,dx\right| \leq M \cdot \|f'\|_{L^1(\mathbb{R}, m)} |\lambda|^{-1} \quad \text{for all } \lambda > 0.
$$

2. If $f \in L^1(\mathbb{R}, m)$, show
$$
\lim_{\lambda \to \infty} \int_{\mathbb{R}} f(x) \varphi'(\lambda x)\,dx = 0.
$$
:::

::: {.solution}
<1>1. Part 1: Bound for $f \in C_c^1(\mathbb{R})$ via integration by parts:
<2>1. Since $f \in C_c^1(\mathbb{R})$, $f$ and $f'$ have compact support contained in some interval $[-R, R]$.
Using integration by parts with $u = f(x)$ and $dv = \varphi'(\lambda x)\,dx$ (so $v = \frac{1}{\lambda} \varphi(\lambda x)$):
\[
\int_{-\infty}^\infty f(x) \varphi'(\lambda x) \, dx = \left[ \frac{1}{\lambda} f(x) \varphi(\lambda x) \right]_{-\infty}^\infty - \frac{1}{\lambda} \int_{-\infty}^\infty f'(x) \varphi(\lambda x) \, dx.
\]
Proof: integration by parts for $C^1$ functions with compact support.
<2>2. The boundary term vanishes because $f(x) = 0$ outside $[-R, R]$ and $\varphi$ is bounded:
\[
\left[ \frac{1}{\lambda} f(x) \varphi(\lambda x) \right]_{-\infty}^\infty = 0.
\]
Proof: compact support of $f$.
<2>3. Taking absolute values and using $|\varphi(y)| \le M$:
\[
\left| \int_{-\infty}^\infty f(x) \varphi'(\lambda x) \, dx \right| \le \frac{1}{\lambda} \int_{-\infty}^\infty |f'(x)| |\varphi(\lambda x)| \, dx \le \frac{M}{\lambda} \int_{-\infty}^\infty |f'(x)| \, dx = M \|f'\|_{L^1(\mathbb{R})} \lambda^{-1}.
\]
Proof: integral triangle inequality and supremum bound $|\varphi| \le M$.

<1>2. Part 2: Limit for $f \in L^1(\mathbb{R})$ via density of $C_c^1(\mathbb{R})$:
<2>1. Let $\varepsilon > 0$ be given.
By the density of $C_c^1(\mathbb{R})$ in $L^1(\mathbb{R})$, there exists a function $g \in C_c^1(\mathbb{R})$ such that:
\[
\|f - g\|_{L^1(\mathbb{R})} < \frac{\varepsilon}{2M}.
\]
Proof: density of test functions in $L^1(\mathbb{R})$.
<2>2. For any $\lambda > 0$, decompose the integral:
\[
\int_\mathbb{R} f(x) \varphi'(\lambda x) \, dx = \int_\mathbb{R} (f(x) - g(x)) \varphi'(\lambda x) \, dx + \int_\mathbb{R} g(x) \varphi'(\lambda x) \, dx.
\]
Proof: linearity of the Lebesgue integral.
<2>3. Bound the approximation error:
\[
\left| \int_\mathbb{R} (f(x) - g(x)) \varphi'(\lambda x) \, dx \right| \le \sup_{y \in \mathbb{R}} |\varphi'(y)| \|f - g\|_{L^1} \le M \cdot \frac{\varepsilon}{2M} = \frac{\varepsilon}{2}.
\]
Proof: Hölder's inequality with $|\varphi'| \le M$.
<2>4. By Part 1, for the $C_c^1$ function $g$:
\[
\left| \int_\mathbb{R} g(x) \varphi'(\lambda x) \, dx \right| \le \frac{M \|g'\|_{L^1}}{\lambda}.
\]
Choosing $\Lambda = \frac{2 M \|g'\|_{L^1}}{\varepsilon}$, for all $\lambda > \Lambda$ we have:
\[
\left| \int_\mathbb{R} g(x) \varphi'(\lambda x) \, dx \right| < \frac{\varepsilon}{2}.
\]
Proof: Archimedean property.
<2>5. Combining bounds for all $\lambda > \Lambda$:
\[
\left| \int_\mathbb{R} f(x) \varphi'(\lambda x) \, dx \right| \le \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon.
\]
Since $\varepsilon > 0$ was arbitrary, $\lim_{\lambda \to \infty} \int_\mathbb{R} f(x) \varphi'(\lambda x) \, dx = 0$.
Proof: definition of limit.

<1>3. Conclusion:
Both parts 1 and 2 are proven. Q.E.D.
Proof: <1>1 and <1>2.
:::
