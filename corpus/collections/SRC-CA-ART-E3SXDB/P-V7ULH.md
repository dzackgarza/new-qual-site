---
schema: qual/card@1
id: P-V7ULH
kind: problem
title: A power series has an expansion about every point of its disc of convergence
classification:
  areas:
  - complex-analysis
  topics:
  - Power Series
  - Cauchy Integral Formula
relations: []
review: draft
---

::: problem
Let $f(z) = \sum_{n=0}^\infty a_n z^n$ be a power series centered at the origin with radius of convergence $R > 0$. Prove that $f$ has a power series expansion about any point $z_0$ in its disc of convergence $D_R(0)$.
:::

::: solution
**Goal:** Prove that if $f$ is represented by a power series on $D_R(0)$, then for every $z_0 \in D_R(0)$, $f$ has a power series expansion $f(z) = \sum_{k=0}^\infty b_k (z - z_0)^k$ converging in the disc $D_{R - |z_0|}(z_0)$.

<1>1. Holomorphy and setup of the contour:
    *Proof:*
    <2>1. The power series $\sum_{n=0}^\infty a_n z^n$ converges absolutely and uniformly on compact subsets of the open disc $D_R(0) = \{z \in \mathbb{C} : |z| < R\}$, defining a holomorphic function $f: D_R(0) \to \mathbb{C}$.
    <2>2. Fix $z_0 \in D_R(0)$, so $|z_0| < R$. Let $r$ be any positive radius with $0 < r < R - |z_0|$.
    <2>3. Choose $\rho$ such that $|z_0| + r < \rho < R$.
    <2>4. The circular contour $\Gamma = \{\xi \in \mathbb{C} : |\xi| = \rho\}$, oriented counterclockwise, lies entirely within $D_R(0)$.
    <2>5. For any point $z \in D_r(z_0)$, the triangle inequality gives $|z| \le |z_0| + |z - z_0| < |z_0| + r < \rho$, so $z$ lies in the interior of $\Gamma$.

<1>2. Cauchy's Integral Formula representation:
    *Proof:*
    <2>1. Since $f$ is holomorphic on $D_R(0)$ and $\overline{D}_\rho(0) \subset D_R(0)$, Cauchy's Integral Formula applies for every $z \in D_r(z_0)$:
    $$f(z) = \frac{1}{2\pi i} \oint_\Gamma \frac{f(\xi)}{\xi - z} \, d\xi.$$

<1>3. Uniform expansion of the Cauchy kernel:
    *Proof:*
    <2>1. Decompose the Cauchy kernel about $z_0$:
    $$\frac{1}{\xi - z} = \frac{1}{(\xi - z_0) - (z - z_0)} = \frac{1}{\xi - z_0} \cdot \frac{1}{1 - \frac{z - z_0}{\xi - z_0}}.$$
    <2>2. For all $\xi \in \Gamma$, $|\xi - z_0| \ge |\xi| - |z_0| = \rho - |z_0|$.
    <2>3. For $z \in D_r(z_0)$, $|z - z_0| \le r < \rho - |z_0|$, so
    $$\left| \frac{z - z_0}{\xi - z_0} \right| \le \frac{r}{\rho - |z_0|} = c < 1.$$
    <2>4. By the Weierstrass $M$-test, the geometric series
    $$\frac{1}{1 - \frac{z - z_0}{\xi - z_0}} = \sum_{k=0}^\infty \left( \frac{z - z_0}{\xi - z_0} \right)^k$$
    converges uniformly with respect to $\xi \in \Gamma$.
    <2>5. Multiplying by $\frac{f(\xi)}{\xi - z_0}$, which is continuous and bounded on $\Gamma$, the series
    $$\frac{f(\xi)}{\xi - z} = \sum_{k=0}^\infty \frac{f(\xi)}{(\xi - z_0)^{k+1}} (z - z_0)^k$$
    converges uniformly on the contour $\Gamma$.

<1>4. Term-by-term integration:
    *Proof:*
    <2>1. By uniform convergence on $\Gamma$, we may interchange summation and integration:
    $$f(z) = \frac{1}{2\pi i} \oint_\Gamma \frac{f(\xi)}{\xi - z} \, d\xi = \sum_{k=0}^\infty \left( \frac{1}{2\pi i} \oint_\Gamma \frac{f(\xi)}{(\xi - z_0)^{k+1}} \, d\xi \right) (z - z_0)^k.$$
    <2>2. Define the coefficients $b_k = \frac{1}{2\pi i} \oint_\Gamma \frac{f(\xi)}{(\xi - z_0)^{k+1}} \, d\xi = \frac{f^{(k)}(z_0)}{k!}$.
    <2>3. Then $f(z) = \sum_{k=0}^\infty b_k (z - z_0)^k$ holds for all $z \in D_r(z_0)$.
    <2>4. Since $r < R - |z_0|$ was arbitrary, the power series expansion converges on the entire open disc $D_{R - |z_0|}(z_0)$.

<1>5. Conclusion:
    *Proof:*
    $f$ has a power series expansion centered at every point $z_0$ in its disc of convergence $D_R(0)$.
:::

