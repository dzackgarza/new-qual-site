---
schema: qual/card@1
id: E-T5ERF
kind: problem
title: $\|f\|_{(\infty,s)}\le c\|f\|_{(1,r)}$ for holomorphic $f$ near $D_r(z_0)$
classification:
  areas:
  - complex-analysis
  topics:
  - Mean Value Property
  - Cauchy Estimates
  - Holomorphic Functions
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Let $f$ be holomorphic in a neighborhood of the closed disk $\overline{D}_r(z_0)$.
Show that for any $s < r$, there exists a constant $c > 0$ (depending on $r$ and $s$) such that:
$$\|f\|_{(\infty, s)} \le c \|f\|_{(1, r)}$$
where $\|f\|_{(\infty, s)} = \sup_{z \in D_s(z_0)} |f(z)|$ and $\|f\|_{(1, r)} = \iint_{D_r(z_0)} |f(z)| \, dx \, dy$.
:::

::: solution
**Goal:** Prove the $L^\infty(D_s) \le c L^1(D_r)$ bound for holomorphic functions using the Mean Value Property on small disks.

<1>1. Setting and Geometric Distance:
    *Proof:*
    <2>1. Let $0 < s < r$, and let $\delta = r - s > 0$ be the distance from the boundary of $D_s(z_0)$ to the boundary of $D_r(z_0)$.
    <2>2. For any point $w \in D_s(z_0)$, the open disk centered at $w$ with radius $\delta = r - s$:
        $$D_\delta(w) = \{\zeta \in \mathbb{C} \mid |\zeta - w| < \delta\}$$
        is entirely contained in $D_r(z_0)$:
        $$|\zeta - z_0| \le |\zeta - w| + |w - z_0| < \delta + s = (r - s) + s = r \implies D_\delta(w) \subset D_r(z_0).$$

<1>2. Area Mean Value Property for Holomorphic Functions:
    *Proof:*
    <2>1. Since $f$ is holomorphic on $D_r(z_0)$, for any $w \in D_s(z_0)$ and any $\rho \in (0, \delta]$, by Cauchy's Integral Formula on the circle $C_\rho(w)$:
        $$f(w) = \frac{1}{2\pi} \int_0^{2\pi} f(w + \rho e^{i\theta}) \, d\theta.$$
    <2>2. Multiplying by $\rho$ and integrating with respect to $\rho$ from $0$ to $\delta$:
        $$\int_0^\delta f(w) \rho \, d\rho = \frac{1}{2\pi} \int_0^\delta \int_0^{2\pi} f(w + \rho e^{i\theta}) \rho \, d\theta \, d\rho.$$
    <2>3. The left-hand side evaluates to $f(w) \frac{\delta^2}{2}$.
    <2>4. The right-hand side is the area integral of $f$ over the disk $D_\delta(w)$:
        $$f(w) \frac{\delta^2}{2} = \frac{1}{2\pi} \iint_{D_\delta(w)} f(x + iy) \, dx \, dy.$$
    <2>5. Dividing by $\frac{\delta^2}{2}$ gives the **Area Mean Value Property**:
        $$f(w) = \frac{1}{\pi \delta^2} \iint_{D_\delta(w)} f(z) \, dx \, dy.$$

<1>3. $L^\infty$ and $L^1$ Estimates:
    *Proof:*
    <2>1. Taking absolute values and using the triangle inequality for integrals:
        $$|f(w)| \le \frac{1}{\pi \delta^2} \iint_{D_\delta(w)} |f(z)| \, dx \, dy.$$
    <2>2. Since $D_\delta(w) \subset D_r(z_0)$ and $|f(z)| \ge 0$:
        $$\iint_{D_\delta(w)} |f(z)| \, dx \, dy \le \iint_{D_r(z_0)} |f(z)| \, dx \, dy = \|f\|_{(1, r)}.$$
    <2>3. Therefore:
        $$|f(w)| \le \frac{1}{\pi (r - s)^2} \|f\|_{(1, r)} \quad \text{for all } w \in D_s(z_0).$$
    <2>4. Taking the supremum over all $w \in D_s(z_0)$:
        $$\|f\|_{(\infty, s)} = \sup_{w \in D_s(z_0)} |f(w)| \le \frac{1}{\pi (r - s)^2} \|f\|_{(1, r)}.$$

<1>4. Conclusion:
    Setting $c = \frac{1}{\pi (r - s)^2} > 0$ yields $\|f\|_{(\infty, s)} \le c \|f\|_{(1, r)}$. Q.E.D.
:::
