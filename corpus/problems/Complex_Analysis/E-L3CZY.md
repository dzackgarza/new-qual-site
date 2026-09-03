---
schema: qual/card@1
id: E-L3CZY
kind: problem
title: Compactly convergent series of holomorphic functions are holomorphic
classification:
  areas:
  - complex-analysis
  topics:
  - Uniform Convergence
  - Series of Functions
  - Holomorphic Functions
  - Morera
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: {.exercise}
Show that if each $f_n$ is holomorphic on an open set $\Omega \subseteq \mathbb{C}$ and $F \coloneqq \sum_{n=1}^\infty f_n$ converges uniformly on every compact subset of $\Omega$, then $F$ is holomorphic on $\Omega$.
:::

::: solution
**Goal:** Prove Weierstrass's Theorem on uniform limits of holomorphic functions using Morera's Theorem and Cauchy's Theorem.

<1>1. Continuity of the sum function $F$:
    *Proof:*
    <2>1. Let $S_N(z) = \sum_{n=1}^N f_n(z)$ be the $N$-th partial sum.
    <2>2. As a finite sum of holomorphic functions, each $S_N$ is holomorphic, hence continuous on $\Omega$.
    <2>3. Let $z_0 \in \Omega$. Choose a closed disk $\overline{D}(z_0, r) \subset \Omega$.
    <2>4. Because $\overline{D}(z_0, r)$ is compact, $S_N \to F$ uniformly on $\overline{D}(z_0, r)$.
    <2>5. The uniform limit of continuous functions is continuous. Therefore, $F$ is continuous on $\overline{D}(z_0, r)$, and since $z_0 \in \Omega$ was arbitrary, $F$ is continuous on all of $\Omega$.

<1>2. Application of Morera's Theorem:
    *Proof:*
    <2>1. Let $T \subset \Omega$ be any solid closed triangle whose interior is also contained in $\Omega$.
    <2>2. Let $\partial T$ be the boundary path of $T$. The image of $\partial T$ is a compact subset of $\Omega$.
    <2>3. Because each $S_N$ is holomorphic on the simply connected domain containing $T$, by Cauchy's Integral Theorem:
        $$\oint_{\partial T} S_N(z) \, dz = 0 \quad \text{for every } N \ge 1.$$
    <2>4. Because $S_N \to F$ uniformly on the compact path $\partial T$, we may interchange the limit and the integral:
        $$\oint_{\partial T} F(z) \, dz = \oint_{\partial T} \lim_{N \to \infty} S_N(z) \, dz = \lim_{N \to \infty} \oint_{\partial T} S_N(z) \, dz = \lim_{N \to \infty} 0 = 0.$$
    <2>5. **Morera's Theorem:** Since $F$ is continuous on $\Omega$ and $\oint_{\partial T} F(z) \, dz = 0$ for every closed triangle $T \subset \Omega$, $F$ is holomorphic on $\Omega$.

<1>3. Derivative property (bonus/extension):
    *Proof:*
    <2>1. Furthermore, by Cauchy's Integral Formula for derivatives, for each $k \ge 1$, $F^{(k)}(z) = \sum_{n=1}^\infty f_n^{(k)}(z)$, and the series of derivatives converges uniformly on every compact subset of $\Omega$.

<1>4. Conclusion:
    $F = \sum_{n=1}^\infty f_n$ is holomorphic on $\Omega$. Q.E.D.
:::
