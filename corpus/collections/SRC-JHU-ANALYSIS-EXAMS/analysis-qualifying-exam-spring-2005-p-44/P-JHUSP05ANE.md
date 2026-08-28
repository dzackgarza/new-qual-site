---
schema: qual/card@1
id: P-JHUSP05ANE
kind: problem
title: "Nonzero C_c^∞ function with compactly supported Fourier transform"
classification:
  areas:
  - real-analysis
  topics:
  - Fourier Transform
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: problem
Do there exist functions $f \in \mathcal{C}_c^{\infty}(\mathbb{R})$ such that $f$ is not identically zero and $\widehat{f} \in \mathcal{C}_c^{\infty}(\mathbb{R})$?
If so, find one.
If not, prove that none exist.

Notation: $\mathcal{C}_c^{\infty}(\mathbb{R})$ denotes the compactly supported functions in $\mathcal{C}^{\infty}(\mathbb{R})$, and $\widehat{f}$ denotes the Fourier transform of $f$.
:::

::: solution
**Claim:** No such function exists. If $f \in \mathcal{C}_c^{\infty}(\mathbb{R})$ and $\widehat{f} \in \mathcal{C}_c^{\infty}(\mathbb{R})$, then $f \equiv 0$.

<1>1. Complex extension of the Fourier transform:
    Let $f \in \mathcal{C}_c^{\infty}(\mathbb{R})$. Then there exists $M > 0$ such that $\operatorname{supp}(f) \subseteq [-M, M]$. The Fourier transform $\widehat{f}(\xi) = \int_{-M}^M f(x) e^{-i x \xi} \, dx$ extends to a function on the complex plane $\mathbb{C}$:
    $$F(z) = \int_{-M}^M f(x) e^{-i x z} \, dx, \quad z \in \mathbb{C}.$$

<1>2. $F(z)$ is an entire function on $\mathbb{C}$:
    *Proof:*
    <2>1. The integrand $h(x, z) = f(x) e^{-i x z}$ is continuous on $[-M, M] \times \mathbb{C}$, and for each fixed $x$, $z \mapsto h(x, z)$ is holomorphic with derivative $\frac{\partial h}{\partial z}(x, z) = -i x f(x) e^{-i x z}$.
    <2>2. For any compact subset $K \subset \mathbb{C}$, $\sup_{z \in K, x \in [-M, M]} |\frac{\partial h}{\partial z}(x, z)| \le M \|f\|_\infty e^{M \sup_{z \in K}|\operatorname{Im}(z)|} < \infty$.
    <2>3. By differentiation under the integral sign (or Morera's Theorem and Fubini's Theorem), $F(z)$ is complex differentiable everywhere on $\mathbb{C}$. Thus $F$ is entire.

<1>3. If $\widehat{f} \in \mathcal{C}_c^\infty(\mathbb{R})$, the zero set of $F$ contains an accumulation point in $\mathbb{C}$:
    *Proof:*
    <2>1. If $\widehat{f}$ is compactly supported, there exists $R > 0$ such that $\widehat{f}(\xi) = 0$ for all $|\xi| > R$.
    <2>2. On the real line, $F(\xi) = \widehat{f}(\xi)$ for all $\xi \in \mathbb{R}$.
    <2>3. Hence $F(\xi) = 0$ for all $\xi \in (R, \infty)$.
    <2>4. The interval $(R, \infty)$ is an infinite set of real numbers with accumulation points in $\mathbb{C}$.

<1>4. $F \equiv 0$ on all of $\mathbb{C}$:
    *Proof:* By the Identity Theorem for holomorphic functions, an entire function whose zero set contains an accumulation point must vanish identically on $\mathbb{C}$. Since $F|_{(R, \infty)} \equiv 0$, $F(z) = 0$ for all $z \in \mathbb{C}$.

<1>5. Conclusion: $f \equiv 0$ on $\mathbb{R}$.
    *Proof:* Since $F \equiv 0$, we have $\widehat{f}(\xi) = F(\xi) = 0$ for all $\xi \in \mathbb{R}$. Since $f \in L^1(\mathbb{R})$ (being smooth and compactly supported) and $\widehat{f} \equiv 0 \in L^1(\mathbb{R})$, the Fourier Inversion Theorem implies:
    $$f(x) = \frac{1}{2\pi} \int_{-\infty}^\infty \widehat{f}(\xi) e^{i x \xi} \, d\xi = 0 \quad \text{for all } x \in \mathbb{R}.$$
    Thus $f$ is identically zero. Therefore, no nonzero function in $\mathcal{C}_c^\infty(\mathbb{R})$ has a compactly supported Fourier transform. Q.E.D.
:::
