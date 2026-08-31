---
schema: qual/card@1
id: P-XL7MP
kind: problem
title: $L^2([0,1])\subseteq L^1([0,1])$, $\ell^1(\ZZ)\subseteq\ell^2(\ZZ)$, and uniform
  Fourier reconstruction when $\hat f\in\ell^1$
classification:
  areas:
  - real-analysis
  topics:
  - Fourier Analysis
  - Lp Spaces
  - Uniform Convergence
  - Series of Functions
relations: []
review: draft
---

::: problem
(a) Show that
$$
L^2([0, 1]) \subseteq L^1([0, 1]) \quad \text{and} \quad \ell^1(\mathbb{Z}) \subseteq \ell^2(\mathbb{Z}).
$$

(b) For $f \in L^1([0, 1])$, define the Fourier coefficients by
$$
\hat{f}(n) = \int_0^1 f(x) e^{-2\pi i n x} \, dx \quad (n \in \mathbb{Z}).
$$
Prove that if $f \in L^1([0, 1])$ and $(\hat{f}(n))_{n \in \mathbb{Z}} \in \ell^1(\mathbb{Z})$, then the partial sums
$$
S_N f(x) = \sum_{|n| \le N} \hat{f}(n) e^{2\pi i n x}
$$
converge uniformly on $[0, 1]$ to a continuous function $g$ such that $g(x) = f(x)$ almost everywhere.
:::

::: solution
**Goal:** Prove space inclusions in (a) via Hölder's inequality and norm inequalities, and prove uniform convergence to an almost-everywhere representative in (b) via the Weierstrass $M$-test and Fourier uniqueness.

<1>1. Part (a): $L^2([0, 1]) \subseteq L^1([0, 1])$.
::: {.proof}
    <2>1. Let $f \in L^2([0, 1])$.
    <2>2. Apply Cauchy–Schwarz (Hölder's inequality with $p = q = 2$) to $|f|$ and the constant function $1 \in L^2([0, 1])$:
    $$\|f\|_{L^1} = \int_0^1 |f(x)| \cdot 1 \, dx \le \left( \int_0^1 |f(x)|^2 \, dx \right)^{1/2} \left( \int_0^1 1^2 \, dx \right)^{1/2} = \|f\|_{L^2} \cdot 1.$$
    <2>3. Since $\|f\|_{L^2} < \infty$, $\|f\|_{L^1} < \infty$, so $f \in L^1([0, 1])$.

:::

<1>2. Part (a): $\ell^1(\mathbb{Z}) \subseteq \ell^2(\mathbb{Z})$.
::: {.proof}
    <2>1. Let $c = (c_n)_{n \in \mathbb{Z}} \in \ell^1(\mathbb{Z})$, so $\sum_{n \in \mathbb{Z}} |c_n| < \infty$.
    <2>2. The convergence of the series implies $\|c\|_{\ell^\infty} = \sup_{n \in \mathbb{Z}} |c_n| \le \sum_{n \in \mathbb{Z}} |c_n| = \|c\|_{\ell^1} < \infty$.
    <2>3. Estimate the $\ell^2$ norm:
    $$\|c\|_{\ell^2}^2 = \sum_{n \in \mathbb{Z}} |c_n|^2 = \sum_{n \in \mathbb{Z}} |c_n| \cdot |c_n| \le \|c\|_{\ell^\infty} \sum_{n \in \mathbb{Z}} |c_n| = \|c\|_{\ell^\infty} \|c\|_{\ell^1} \le \|c\|_{\ell^1}^2 < \infty.$$
    <2>4. Thus $c \in \ell^2(\mathbb{Z})$.

:::

<1>3. Part (b): Uniform convergence to a continuous function $g$.
::: {.proof}
    <2>1. For each $n \in \mathbb{Z}$, define the continuous function $u_n(x) = \hat{f}(n) e^{2\pi i n x}$ on $[0, 1]$.
    <2>2. For all $x \in [0, 1]$:
    $$|u_n(x)| = |\hat{f}(n)| \cdot |e^{2\pi i n x}| = |\hat{f}(n)| =: M_n.$$
    <2>3. By hypothesis, $\sum_{n \in \mathbb{Z}} M_n = \sum_{n \in \mathbb{Z}} |\hat{f}(n)| = \|\hat{f}\|_{\ell^1} < \infty$.
    <2>4. By the Weierstrass $M$-test, the Fourier series $\sum_{n=-\infty}^\infty \hat{f}(n) e^{2\pi i n x}$ converges absolutely and uniformly on $[0, 1]$.
    <2>5. As the uniform limit of continuous partial sums $S_N f(x)$, the limit function $g(x) = \lim_{N \to \infty} S_N f(x)$ is continuous on $[0, 1]$.

:::

<1>4. Part (b): Fourier coefficients of $g$ match those of $f$.
::: {.proof}
    <2>1. Since $S_N f \to g$ uniformly on $[0, 1]$, we can interchange summation and integration.
    <2>2. For any $k \in \mathbb{Z}$:
    $$\hat{g}(k) = \int_0^1 g(x) e^{-2\pi i k x} \, dx = \lim_{N \to \infty} \int_0^1 \left( \sum_{|n| \le N} \hat{f}(n) e^{2\pi i n x} \right) e^{-2\pi i k x} \, dx.$$
    <2>3. By orthogonality of the complex exponentials on $[0, 1]$ ($\int_0^1 e^{2\pi i (n - k) x} \, dx = \delta_{n k}$):
    $$\int_0^1 \left( \sum_{|n| \le N} \hat{f}(n) e^{2\pi i n x} \right) e^{-2\pi i k x} \, dx = \hat{f}(k) \quad \text{for all } N \ge |k|.$$
    <2>4. Thus $\hat{g}(k) = \hat{f}(k)$ for every $k \in \mathbb{Z}$.

:::

<1>5. Part (b): $f = g$ almost everywhere.
::: {.proof}
    <2>1. Define $h = f - g \in L^1([0, 1])$.
    <2>2. By linearity of the integral, $\hat{h}(k) = \hat{f}(k) - \hat{g}(k) = 0$ for all $k \in \mathbb{Z}$.
    <2>3. Consider the Fejér means $\sigma_N h(x) = \frac{1}{N+1} \sum_{j=0}^N S_j h(x) = \sum_{|n| \le N} \left(1 - \frac{|n|}{N+1}\right) \hat{h}(n) e^{2\pi i n x}$.
    <2>4. Since $\hat{h}(n) = 0$ for all $n$, $\sigma_N h(x) \equiv 0$ for all $N \ge 0$.
    <2>5. By Fejér's Theorem for $L^1([0, 1])$, $\lim_{N \to \infty} \|\sigma_N h - h\|_{L^1} = 0$.
    <2>6. Since $\sigma_N h = 0$, $\|h\|_{L^1} = 0$.
    <2>7. Thus $h(x) = 0$ almost everywhere, so $f(x) = g(x)$ almost everywhere on $[0, 1]$.

:::

<1>6. Conclusion:
::: {.proof}
    $L^2([0, 1]) \subseteq L^1([0, 1])$ by Cauchy–Schwarz, $\ell^1(\mathbb{Z}) \subseteq \ell^2(\mathbb{Z})$ by $\ell^\infty$ bounding, and $S_N f \to g$ uniformly with $g = f$ a.e. by the $M$-test and Fejér uniqueness.
:::
:::

