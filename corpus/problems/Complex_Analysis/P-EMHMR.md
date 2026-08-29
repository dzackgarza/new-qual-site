---
schema: qual/card@1
id: P-EMHMR
kind: problem
title: Uniqueness of Laurent series coefficients
classification:
  areas:
  - complex-analysis
  topics:
  - Laurent Series
  - Power Series
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Prove that if a function $f$ has two Laurent series expansions in an annulus $A = \{z \in \mathbb{C} \mid r < |z-a| < R\}$:
$$f(z) = \sum_{n=-\infty}^\infty c_n(z-a)^n \quad\text{and}\quad f(z) = \sum_{n=-\infty}^\infty c_n'(z-a)^n$$
then $c_n = c_n'$ for all $n \in \mathbb{Z}$.
:::

::: solution
**Goal:** Prove the uniqueness of Laurent series coefficients in an annulus $A = \{z \in \mathbb{C} \mid r < |z-a| < R\}$.

<1>1. Integral formula for Laurent coefficients:
    *Proof:*
    <2>1. Choose $\rho$ such that $r < \rho < R$.
    <2>2. Let $\gamma(t) = a + \rho e^{it}$ for $t \in [0, 2\pi]$ be the circle of radius $\rho$ centered at $a$, oriented counterclockwise.
    <2>3. The image of $\gamma$ is a compact subset of the annulus $A$.
    <2>4. For any integer $k \in \mathbb{Z}$, consider the contour integral:
        $$I_k = \frac{1}{2\pi i} \oint_\gamma \frac{f(z)}{(z - a)^{k+1}} \, dz.$$

<1>2. Orthogonality of powers of $(z-a)$ along the circle $\gamma$:
    *Proof:*
    <2>1. For any integer $m \in \mathbb{Z}$, compute the integral:
        $$\frac{1}{2\pi i} \oint_\gamma (z - a)^m \, dz = \frac{1}{2\pi i} \int_0^{2\pi} (\rho e^{it})^m (i \rho e^{it}) \, dt = \frac{\rho^{m+1}}{2\pi} \int_0^{2\pi} e^{i(m+1)t} \, dt.$$
    <2>2. If $m+1 \ne 0$ (i.e. $m \ne -1$):
        $$\int_0^{2\pi} e^{i(m+1)t} \, dt = \left[ \frac{e^{i(m+1)t}}{i(m+1)} \right]_0^{2\pi} = \frac{1 - 1}{i(m+1)} = 0.$$
    <2>3. If $m+1 = 0$ (i.e. $m = -1$):
        $$\int_0^{2\pi} 1 \, dt = 2\pi \implies \frac{\rho^0}{2\pi}(2\pi) = 1.$$
    <2>4. Thus:
        $$\frac{1}{2\pi i} \oint_\gamma (z - a)^m \, dz = \begin{cases} 1 & \text{if } m = -1, \\ 0 & \text{if } m \ne -1. \end{cases}$$

<1>3. Term-by-term integration of Laurent series:
    *Proof:*
    <2>1. Because the Laurent series $\sum_{n=-\infty}^\infty c_n (z-a)^n$ converges uniformly on the compact circle $\gamma$, we may interchange summation and integration:
        $$\begin{aligned}
        I_k &= \frac{1}{2\pi i} \oint_\gamma \frac{\sum_{n=-\infty}^\infty c_n (z-a)^n}{(z-a)^{k+1}} \, dz \\
        &= \sum_{n=-\infty}^\infty c_n \left( \frac{1}{2\pi i} \oint_\gamma (z-a)^{n-k-1} \, dz \right).
        \end{aligned}$$
    <2>2. By the orthogonality relation with $m = n - k - 1$:
        $$\frac{1}{2\pi i} \oint_\gamma (z-a)^{n-k-1} \, dz = \begin{cases} 1 & \text{if } n - k - 1 = -1 \iff n = k, \\ 0 & \text{if } n \ne k. \end{cases}$$
    <2>3. Therefore:
        $$I_k = c_k \cdot 1 = c_k.$$

<1>4. Uniqueness of coefficients:
    *Proof:*
    <2>1. Applying the exact same argument to the second expansion $f(z) = \sum_{n=-\infty}^\infty c_n' (z-a)^n$ yields:
        $$I_k = c_k'.$$
    <2>2. Since $I_k = \frac{1}{2\pi i}\oint_\gamma \frac{f(z)}{(z-a)^{k+1}}dz$ depends solely on the function $f$, the center $a$, and the integer $k$:
        $$c_k = I_k = c_k' \quad \text{for every } k \in \mathbb{Z}.$$

<1>5. Conclusion:
    The coefficients of a Laurent series on an annulus are uniquely determined by $c_n = \frac{1}{2\pi i}\oint_\gamma \frac{f(z)}{(z-a)^{n+1}}dz$. Q.E.D.
:::
