---
schema: qual/card@1
id: P-ALI5T
kind: problem
title: A holomorphic function real-valued on a closed curve is constant
classification:
  areas:
  - complex-analysis
  topics:
  - Open Mapping Theorem
  - Maximum Modulus Principle
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Assume $f(z)$ is analytic in a region $D$ and $\Gamma$ is a simple closed rectifiable curve in $D$ whose interior $\Omega$ is contained in $D$.
Prove that if $f(z)$ is real-valued for all $z \in \Gamma$, then $f(z)$ is constant on $D$.
:::

::: solution
**Goal:** Prove that if $f$ is holomorphic on $D \supset \overline{\Omega}$ and $\operatorname{Im}(f|_\Gamma) = 0$, then $f$ is constant.

<1>1. Method 1: Maximum and Minimum Principles for harmonic functions:
    *Proof:*
    <2>1. Write $f(z) = u(z) + iv(z)$ where $u = \operatorname{Re}(f)$ and $v = \operatorname{Im}(f)$ are real harmonic functions on $D$.
    <2>2. Let $\Omega$ be the bounded interior domain enclosed by $\Gamma = \partial\Omega$. Since $\overline{\Omega} = \Omega \cup \Gamma \subset D$, $v$ is continuous on $\overline{\Omega}$ and harmonic on $\Omega$.
    <2>3. By hypothesis, $v(z) = 0$ for all $z \in \Gamma = \partial\Omega$.
    <2>4. By the Maximum Modulus Principle (or Maximum Principle for harmonic functions):
        $$\max_{z \in \overline{\Omega}} v(z) = \max_{z \in \partial\Omega} v(z) = 0, \qquad \min_{z \in \overline{\Omega}} v(z) = \min_{z \in \partial\Omega} v(z) = 0.$$
    <2>5. Therefore, $v(z) \equiv 0$ on all of $\overline{\Omega}$.

<1>2. Constancy on $\Omega$ and identity principle on $D$:
    *Proof:*
    <2>1. Since $v(x, y) \equiv 0$ on the open set $\Omega$, its partial derivatives vanish: $v_x \equiv 0$ and $v_y \equiv 0$ on $\Omega$.
    <2>2. By the Cauchy–Riemann equations, $u_x = v_y = 0$ and $u_y = -v_x = 0$ on $\Omega$.
    <2>3. Since $\Omega$ is connected, $u$ is constant on $\Omega$, so $f(z) = u(z) + i \cdot 0 = c$ is constant on $\Omega$.
    <2>4. By the Identity Theorem for holomorphic functions on the connected domain $D$, since $f$ is constant on the non-empty open subset $\Omega \subset D$, $f(z) \equiv c$ on the entire region $D$.

<1>3. Conclusion:
    $f$ is constant on $D$. Q.E.D.
:::
