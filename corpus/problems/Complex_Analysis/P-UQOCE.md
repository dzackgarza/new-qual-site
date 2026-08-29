---
schema: qual/card@1
id: P-UQOCE
kind: problem
title: $\int_\gamma\frac{f'(z)}{z-z_0}\,dz=\int_\gamma\frac{f(z)}{(z-z_0)^2}\,dz$
classification:
  areas:
  - complex-analysis
  topics:
  - Cauchy Integral Formula
  - Contour Integration
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Let $f$ be analytic in a domain $D$ and $\gamma$ be a closed, piecewise smooth curve in $D$.
For any $z_0 \in D$ not lying on $\gamma$, show that:
$$\oint_\gamma \frac{f'(z)}{z - z_0} \, dz = \oint_\gamma \frac{f(z)}{(z - z_0)^2} \, dz.$$
Give a generalization of this result for higher-order derivatives and powers.
:::

::: solution
**Goal:** Prove the integral identity $\oint_\gamma \frac{f'(z)}{z - z_0} dz = \oint_\gamma \frac{f(z)}{(z - z_0)^2} dz$ and generalize to $\oint_\gamma \frac{f^{(k)}(z)}{(z - z_0)^m} dz$.

<1>1. Method 1: Integration by Parts:
    *Proof:*
    <2>1. Let $u(z) = \frac{1}{z - z_0}$ and $v(z) = f(z)$.
    <2>2. The product rule for differentials gives:
        $$d(u v) = d\left(\frac{f(z)}{z - z_0}\right) = \frac{f'(z)}{z - z_0} \, dz - \frac{f(z)}{(z - z_0)^2} \, dz.$$
    <2>3. Integrating both sides along the closed curve $\gamma$:
        $$\oint_\gamma d\left(\frac{f(z)}{z - z_0}\right) = \oint_\gamma \frac{f'(z)}{z - z_0} \, dz - \oint_\gamma \frac{f(z)}{(z - z_0)^2} \, dz.$$
    <2>4. The function $g(z) = \frac{f(z)}{z - z_0}$ is single-valued and holomorphic in a neighborhood of the curve $\gamma$ (since $z_0 \notin \gamma$).
    <2>5. By the Fundamental Theorem of Calculus for contour integrals along a closed curve $\gamma$ (starting and ending at $z_1$):
        $$\oint_\gamma d(g(z)) = g(z_1) - g(z_1) = 0.$$
    <2>6. Therefore:
        $$\oint_\gamma \frac{f'(z)}{z - z_0} \, dz - \oint_\gamma \frac{f(z)}{(z - z_0)^2} \, dz = 0 \implies \oint_\gamma \frac{f'(z)}{z - z_0} \, dz = \oint_\gamma \frac{f(z)}{(z - z_0)^2} \, dz.$$

<1>2. Method 2: Via Cauchy's Integral Formula for Derivatives:
    *Proof:*
    <2>1. Let $n(\gamma, z_0) = \frac{1}{2\pi i} \oint_\gamma \frac{1}{z - z_0} \, dz$ be the winding number of $\gamma$ around $z_0$.
    <2>2. Applying Cauchy's Integral Formula to $g(z) = f'(z)$:
        $$\oint_\gamma \frac{f'(z)}{z - z_0} \, dz = 2\pi i \, n(\gamma, z_0) \, f'(z_0).$$
    <2>3. Applying Cauchy's Integral Formula for the first derivative of $f(z)$:
        $$\oint_\gamma \frac{f(z)}{(z - z_0)^2} \, dz = \frac{2\pi i}{1!} \, n(\gamma, z_0) \, f'(z_0) = 2\pi i \, n(\gamma, z_0) \, f'(z_0).$$
    <2>4. Both integrals evaluate to $2\pi i \, n(\gamma, z_0) \, f'(z_0)$, confirming their equality.

<1>3. Generalization to higher derivatives:
    *Proof:*
    <2>1. By repeated integration by parts, for any positive integers $k \ge 0$ and $m \ge 1$:
        $$\oint_\gamma \frac{f^{(k)}(z)}{(z - z_0)^m} \, dz = \frac{m}{k+1} \oint_\gamma \frac{f^{(k-1)}(z)}{(z - z_0)^{m+1}} \, dz \quad (\text{for } k \ge 1).$$
    <2>2. In particular, shifting derivatives to poles:
        $$\oint_\gamma \frac{f^{(k)}(z)}{(z - z_0)^m} \, dz = (m)(m+1)\cdots(m+k-1) \oint_\gamma \frac{f(z)}{(z - z_0)^{m+k}} \, dz = \frac{(m+k-1)!}{(m-1)!} \oint_\gamma \frac{f(z)}{(z - z_0)^{m+k}} \, dz.$$
    <2>3. In terms of Cauchy's formula, both sides equal $\frac{2\pi i}{(m-1)!} n(\gamma, z_0) f^{(m+k-1)}(z_0)$.

<1>4. Conclusion:
    The identity holds by integrating the exact differential $d\left(\frac{f(z)}{z-z_0}\right)$ around the closed loop $\gamma$, and generalizes to $\oint_\gamma \frac{f^{(k)}(z)}{(z-z_0)^m} dz = \frac{(m+k-1)!}{(m-1)!} \oint_\gamma \frac{f(z)}{(z-z_0)^{m+k}} dz$. Q.E.D.
:::
