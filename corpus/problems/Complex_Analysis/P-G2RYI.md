---
schema: qual/card@1
id: P-G2RYI
kind: problem
title: Weierstrass theorem on locally uniform limits of holomorphic functions
classification:
  areas:
  - complex-analysis
  topics:
  - Uniform Convergence
  - Sequences of Functions
  - Holomorphic Functions
  - Morera
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Let $\Omega \subseteq \mathbb{C}$ be an open domain, and let $\{f_n\}$ be a sequence of holomorphic functions on $\Omega$ that converges uniformly to a function $f$ on every compact subset $K \subset \Omega$.
Prove that:
(1) The limit function $f$ is holomorphic on $\Omega$.
(2) The sequence of derivatives $\{f_n'\}$ converges uniformly to $f'$ on every compact subset $K \subset \Omega$ (Weierstrass Convergence Theorem).
:::

::: solution
**Goal:** Prove that locally uniform limits of holomorphic functions are holomorphic (via Morera's Theorem) and that derivatives converge locally uniformly (via Cauchy's Integral Formula for derivatives).

<1>1. Part 1: Holomorphicity of the Limit Function $f$:
    *Proof:*
    <2>1. **Continuity of $f$:**
        Since each $f_n$ is holomorphic, each $f_n$ is continuous.
        Since $f_n \to f$ uniformly on every compact subset $K \subset \Omega$, $f$ is continuous on every compact subset, and hence $f \in C(\Omega)$ is continuous on all of $\Omega$.
    <2>2. **Morera's Theorem:**
        Let $T \subset \Omega$ be any closed triangle whose interior $T^\circ \subset \Omega$.
        Since $T$ is a compact subset of $\Omega$, $f_n \to f$ uniformly on $T$.
        Therefore, we can interchange the integral and the limit:
        $$\oint_{\partial T} f(z) \, dz = \oint_{\partial T} \lim_{n \to \infty} f_n(z) \, dz = \lim_{n \to \infty} \oint_{\partial T} f_n(z) \, dz.$$
    <2>3. By **Cauchy's Integral Theorem**, since each $f_n$ is holomorphic on $\Omega$, $\oint_{\partial T} f_n(z) \, dz = 0$ for all $n$.
    <2>4. Thus:
        $$\oint_{\partial T} f(z) \, dz = \lim_{n \to \infty} 0 = 0.$$
    <2>5. By **Morera's Theorem**, since $f$ is continuous and its contour integral around every triangle vanishes, $f$ is **holomorphic on $\Omega$**.

<1>2. Part 2: Uniform Convergence of Derivatives on Compact Sets:
    *Proof:*
    <2>1. Let $K \subset \Omega$ be an arbitrary compact subset.
    <2>2. Since $K$ is compact and $\Omega^c = \mathbb{C} \setminus \Omega$ is closed, the distance:
        $$d \coloneqq \operatorname{dist}(K, \partial\Omega) > 0.$$
    <2>3. Choose $0 < r < d$. For each $z \in K$, the closed disk $\overline{B_r(z)} \subset \Omega$.
    <2>4. The expanded set $K_r \coloneqq \bigcup_{z \in K} \overline{B_r(z)}$ is a **compact subset of $\Omega$**.
    <2>5. By Cauchy's Integral Formula for derivatives, for any $z \in K$:
        $$f_n'(z) - f'(z) = \frac{1}{2\pi i} \oint_{|\zeta - z| = r} \frac{f_n(\zeta) - f(\zeta)}{(\zeta - z)^2} \, d\zeta.$$
    <2>6. For $\zeta$ on the circle $\partial B_r(z)$, $\zeta \in K_r$ and $|\zeta - z| = r$.
    <2>7. We estimate the contour integral using the ML-inequality:
        $$|f_n'(z) - f'(z)| \le \frac{1}{2\pi} \cdot \frac{\max_{\zeta \in K_r} |f_n(\zeta) - f(\zeta)|}{r^2} \cdot (2\pi r) = \frac{1}{r} \sup_{\zeta \in K_r} |f_n(\zeta) - f(\zeta)|.$$
    <2>8. Taking the supremum over all $z \in K$:
        $$\sup_{z \in K} |f_n'(z) - f'(z)| \le \frac{1}{r} \sup_{\zeta \in K_r} |f_n(\zeta) - f(\zeta)|.$$
    <2>9. Since $K_r \subset \Omega$ is compact, $f_n \to f$ uniformly on $K_r$, so $\sup_{\zeta \in K_r} |f_n(\zeta) - f(\zeta)| \to 0$ as $n \to \infty$.
    <2>10. Therefore, $\sup_{z \in K} |f_n'(z) - f'(z)| \to 0$ as $n \to \infty$, proving **uniform convergence of $f_n'$ to $f'$ on $K$**.

<1>3. Conclusion:
    $f$ is holomorphic on $\Omega$ and $f_n' \to f'$ uniformly on all compact subsets of $\Omega$. Q.E.D.
:::
