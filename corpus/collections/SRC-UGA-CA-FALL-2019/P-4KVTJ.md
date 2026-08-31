---
schema: qual/card@1
id: P-4KVTJ
kind: problem
title: Cauchy integral of $f$ on a simple closed curve, equal to $A$ inside and $-f(z)+A$
  outside, when $\lim_{z\to\infty}f(z)=A$
classification:
  areas:
  - complex-analysis
  topics:
  - Cauchy Integral Formula
  - Residues
  - Contour Integration
relations: []
review: draft
---

::: problem
Let $\gamma$ be a positively oriented (counterclockwise) piecewise smooth simple closed curve in $\mathbb{C}$ with interior $\Omega_1$ and exterior $\Omega_2$.
Assume $f$ is holomorphic on an open set containing $\gamma \cup \Omega_2$, with $\lim_{z \to \infty} f(z) = A$.

Prove that the Cauchy integral
$$
F(z) = \frac{1}{2\pi i} \int_{\gamma} \frac{f(\xi)}{\xi - z} \, d\xi = \begin{cases} A & \text{if } z \in \Omega_1, \\ -f(z) + A & \text{if } z \in \Omega_2. \end{cases}
$$
:::

::: solution
**Goal:** Compute $F(z)$ for $z \in \Omega_1$ and $z \in \Omega_2$ by applying Cauchy's theorem on the annular domain between $\gamma$ and a large circle $C_R = \{|\xi| = R\}$, and taking the limit as $R \to \infty$.

<1>1. Asymptotic limit of the integral along a large circle $C_R$:
::: {.proof}
    <2>1. Let $C_R$ denote the circle $\{|\xi| = R\}$, oriented counterclockwise, for $R > 0$ sufficiently large such that $\gamma \subset \mathbb{D}_R$ and (if $z \in \Omega_2$) $|z| < R$.
    <2>2. Split the integral along $C_R$:
    $$\frac{1}{2\pi i} \int_{C_R} \frac{f(\xi)}{\xi - z} \, d\xi = \frac{A}{2\pi i} \int_{C_R} \frac{d\xi}{\xi - z} + \frac{1}{2\pi i} \int_{C_R} \frac{f(\xi) - A}{\xi - z} \, d\xi.$$
    <2>3. Since $|z| < R$, the winding number of $C_R$ around $z$ is 1:
    $$\frac{1}{2\pi i} \int_{C_R} \frac{d\xi}{\xi - z} = 1.$$
    <2>4. Bound the error term:
        - Let $\varepsilon > 0$. Since $\lim_{\xi \to \infty} f(\xi) = A$, there exists $R_0 > 0$ such that $|f(\xi) - A| < \varepsilon$ for all $|\xi| \ge R_0$.
        - For $R \ge R_0$ with $R > |z|$:
        $$\left| \frac{1}{2\pi i} \int_{C_R} \frac{f(\xi) - A}{\xi - z} \, d\xi \right| \le \frac{1}{2\pi} \cdot \frac{\varepsilon}{R - |z|} \cdot 2\pi R = \varepsilon \frac{R}{R - |z|}.$$
        - Taking $R \to \infty$, the upper bound approaches $\varepsilon$. Since $\varepsilon > 0$ was arbitrary:
        $$\lim_{R \to \infty} \frac{1}{2\pi i} \int_{C_R} \frac{f(\xi) - A}{\xi - z} \, d\xi = 0.$$
    <2>5. Therefore:
    $$\lim_{R \to \infty} \frac{1}{2\pi i} \int_{C_R} \frac{f(\xi)}{\xi - z} \, d\xi = A \cdot 1 + 0 = A.$$

:::

<1>2. Case $z \in \Omega_1$:
::: {.proof}
    <2>1. Let $z \in \Omega_1$.
    <2>2. Choose $R > 0$ large enough that $\gamma \subset \mathbb{D}_R$.
    <2>3. Consider the bounded region $U_R = \mathbb{D}_R \cap \Omega_2$ between $\gamma$ and $C_R$.
    <2>4. The boundary is $\partial U_R = C_R - \gamma$ (where $-\gamma$ indicates that the inner boundary is oriented clockwise relative to $U_R$).
    <2>5. Since $z \in \Omega_1$, $z \notin U_R$. Thus the function $\xi \mapsto \frac{f(\xi)}{\xi - z}$ is holomorphic on an open neighborhood of $\overline{U_R}$.
    <2>6. By Cauchy's Integral Theorem on $U_R$:
    $$\frac{1}{2\pi i} \int_{C_R} \frac{f(\xi)}{\xi - z} \, d\xi - \frac{1}{2\pi i} \int_\gamma \frac{f(\xi)}{\xi - z} \, d\xi = 0.$$
    <2>7. Thus:
    $$F(z) = \frac{1}{2\pi i} \int_\gamma \frac{f(\xi)}{\xi - z} \, d\xi = \frac{1}{2\pi i} \int_{C_R} \frac{f(\xi)}{\xi - z} \, d\xi.$$
    <2>8. Since the left-hand side $F(z)$ is independent of $R$, take $R \to \infty$ and apply <1>1:
    $$F(z) = A.$$

:::

<1>3. Case $z \in \Omega_2$:
::: {.proof}
    <2>1. Let $z \in \Omega_2$.
    <2>2. Choose $R > |z|$ large enough that $\gamma \subset \mathbb{D}_R$.
    <2>3. Now the point $z$ lies in the interior of the bounded region $U_R = \mathbb{D}_R \cap \Omega_2$.
    <2>4. The function $\xi \mapsto \frac{f(\xi)}{\xi - z}$ is holomorphic on $\overline{U_R} \setminus \{z\}$ with a simple pole at $\xi = z$.
    <2>5. The residue at $\xi = z$ is:
    $$\operatorname{Res}_{\xi = z} \frac{f(\xi)}{\xi - z} = f(z).$$
    <2>6. By the Residue Theorem / Cauchy's Integral Formula on $U_R$:
    $$\frac{1}{2\pi i} \int_{C_R} \frac{f(\xi)}{\xi - z} \, d\xi - \frac{1}{2\pi i} \int_\gamma \frac{f(\xi)}{\xi - z} \, d\xi = f(z).$$
    <2>7. Rearranging for $F(z)$:
    $$F(z) = \frac{1}{2\pi i} \int_\gamma \frac{f(\xi)}{\xi - z} \, d\xi = -f(z) + \frac{1}{2\pi i} \int_{C_R} \frac{f(\xi)}{\xi - z} \, d\xi.$$
    <2>8. Taking $R \to \infty$ and applying <1>1:
    $$F(z) = -f(z) + A.$$

:::

<1>4. Conclusion:
::: {.proof}
    $F(z) = A$ for $z \in \Omega_1$ and $F(z) = -f(z) + A$ for $z \in \Omega_2$.
:::
:::
