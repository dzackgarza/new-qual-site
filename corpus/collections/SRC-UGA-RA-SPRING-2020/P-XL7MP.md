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
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
  note: Checked against Problem 6 of the official UGA Spring 2020 Real Analysis qualifying examination DOCX.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-11
  note: Reviewed the L2-to-L1 and ell1-to-ell2 inclusions, M-test uniform convergence, coefficient identification, and Fejer uniqueness argument; the proof is correct.
---

::: {.problem}
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

::: {.hint}
For (a), $\norm{f}_{L^1}\le\norm{f}_{L^2}$ on $[0,1]$ by Cauchy–Schwarz, and $\norm{c}_{\ell^2}^2\le\norm{c}_{\ell^\infty}\norm{c}_{\ell^1}\le\norm{c}_{\ell^1}^2$. For (b), the Weierstrass $M$-test with $M_n=\abs{\hat f(n)}$ gives uniform convergence, and an $L^1$ function whose Fourier coefficients all vanish is $0$ almost everywhere.
:::

::: {.solution}

::: pf

::: pf-step
Part (a): $L^2([0, 1]) \subseteq L^1([0, 1])$.

::: pf-proof

::: pf-step
Let $f \in L^2([0, 1])$.

:::

::: pf-step
Apply Cauchy–Schwarz (Hölder's inequality with $p = q = 2$) to $|f|$ and the constant function $1 \in L^2([0, 1])$:
$$\|f\|_{L^1} = \int_0^1 |f(x)| \cdot 1 \, dx \le \left( \int_0^1 |f(x)|^2 \, dx \right)^{1/2} \left( \int_0^1 1^2 \, dx \right)^{1/2} = \|f\|_{L^2} \cdot 1.$$

:::

::: pf-step
Since $\|f\|_{L^2} < \infty$, $\|f\|_{L^1} < \infty$, so $f \in L^1([0, 1])$.

:::

:::

:::

::: pf-step
Part (a): $\ell^1(\mathbb{Z}) \subseteq \ell^2(\mathbb{Z})$.

::: pf-proof

::: pf-step
Let $c = (c_n)_{n \in \mathbb{Z}} \in \ell^1(\mathbb{Z})$, so $\sum_{n \in \mathbb{Z}} |c_n| < \infty$.

:::

::: pf-step
The convergence of the series implies $\|c\|_{\ell^\infty} = \sup_{n \in \mathbb{Z}} |c_n| \le \sum_{n \in \mathbb{Z}} |c_n| = \|c\|_{\ell^1} < \infty$.

:::

::: pf-step
Estimate the $\ell^2$ norm:
$$\|c\|_{\ell^2}^2 = \sum_{n \in \mathbb{Z}} |c_n|^2 = \sum_{n \in \mathbb{Z}} |c_n| \cdot |c_n| \le \|c\|_{\ell^\infty} \sum_{n \in \mathbb{Z}} |c_n| = \|c\|_{\ell^\infty} \|c\|_{\ell^1} \le \|c\|_{\ell^1}^2 < \infty.$$

:::

::: pf-step
Thus $c \in \ell^2(\mathbb{Z})$.

:::

:::

:::

::: pf-step
Part (b): Uniform convergence to a continuous function $g$.

::: pf-proof

::: pf-step
For each $n \in \mathbb{Z}$, define the continuous function $u_n(x) = \hat{f}(n) e^{2\pi i n x}$ on $[0, 1]$.

:::

::: pf-step
For all $x \in [0, 1]$:
$$|u_n(x)| = |\hat{f}(n)| \cdot |e^{2\pi i n x}| = |\hat{f}(n)| =: M_n.$$

:::

::: pf-step
By hypothesis, $\sum_{n \in \mathbb{Z}} M_n = \sum_{n \in \mathbb{Z}} |\hat{f}(n)| = \|\hat{f}\|_{\ell^1} < \infty$.

:::

::: pf-step
By the Weierstrass $M$-test, the Fourier series $\sum_{n=-\infty}^\infty \hat{f}(n) e^{2\pi i n x}$ converges absolutely and uniformly on $[0, 1]$.

:::

::: pf-step
As the uniform limit of continuous partial sums $S_N f(x)$, the limit function $g(x) = \lim_{N \to \infty} S_N f(x)$ is continuous on $[0, 1]$.

:::

:::

:::

::: pf-step
Part (b): Fourier coefficients of $g$ match those of $f$.

::: pf-proof

::: pf-step
Since $S_N f \to g$ uniformly on $[0, 1]$, we can interchange summation and integration.

:::

::: pf-step
For any $k \in \mathbb{Z}$:
$$\hat{g}(k) = \int_0^1 g(x) e^{-2\pi i k x} \, dx = \lim_{N \to \infty} \int_0^1 \left( \sum_{|n| \le N} \hat{f}(n) e^{2\pi i n x} \right) e^{-2\pi i k x} \, dx.$$

:::

::: pf-step
By orthogonality of the complex exponentials on $[0, 1]$ ($\int_0^1 e^{2\pi i (n - k) x} \, dx = \delta_{n k}$):
$$\int_0^1 \left( \sum_{|n| \le N} \hat{f}(n) e^{2\pi i n x} \right) e^{-2\pi i k x} \, dx = \hat{f}(k) \quad \text{for all } N \ge |k|.$$

:::

::: pf-step
Thus $\hat{g}(k) = \hat{f}(k)$ for every $k \in \mathbb{Z}$.

:::

:::

:::

::: pf-step
Part (b): $f = g$ almost everywhere.

::: pf-proof

::: pf-step
Define $h = f - g \in L^1([0, 1])$.

:::

::: pf-step
By linearity of the integral, $\hat{h}(k) = \hat{f}(k) - \hat{g}(k) = 0$ for all $k \in \mathbb{Z}$.

:::

::: pf-step
Consider the Fejér means $\sigma_N h(x) = \frac{1}{N+1} \sum_{j=0}^N S_j h(x) = \sum_{|n| \le N} \left(1 - \frac{|n|}{N+1}\right) \hat{h}(n) e^{2\pi i n x}$.

:::

::: pf-step
Since $\hat{h}(n) = 0$ for all $n$, $\sigma_N h(x) \equiv 0$ for all $N \ge 0$.

:::

::: pf-step
By Fejér's Theorem for $L^1([0, 1])$, $\lim_{N \to \infty} \|\sigma_N h - h\|_{L^1} = 0$.

:::

::: pf-step
Since $\sigma_N h = 0$, $\|h\|_{L^1} = 0$.

:::

::: pf-step
Thus $h(x) = 0$ almost everywhere, so $f(x) = g(x)$ almost everywhere on $[0, 1]$.

:::

:::

:::

::: pf-step
Conclusion:

::: pf-proof
$L^2([0, 1]) \subseteq L^1([0, 1])$ by Cauchy–Schwarz, $\ell^1(\mathbb{Z}) \subseteq \ell^2(\mathbb{Z})$ by $\ell^\infty$ bounding, and $S_N f \to g$ uniformly with $g = f$ a.e. by the $M$-test and Fejér uniqueness.
:::

:::

:::

:::
