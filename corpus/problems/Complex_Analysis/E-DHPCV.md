---
schema: qual/card@1
id: E-DHPCV
kind: problem
title: $\|f\|_{(\infty,s)}\le c\|f\|_{(1,r)}$ for holomorphic $f$
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
Let $f$ be holomorphic in a neighborhood of $\overline{D_r(z_0)}$. Show that for any $s < r$, there exists a constant $c > 0$ such that
$$
\|f\|_{(\infty, s)} \leq c \|f\|_{(1, r)}
,$$ 
where
$\displaystyle \|f\|_{(\infty, s)} = \sup_{z \in D_s(z_0)}|f(z)|$
and $\displaystyle \|f\|_{(1, r)} = \iint_{D_r(z_0)} |f(z)|\,dx\,dy$.
:::

::: solution
**Goal:** Prove that $\|f\|_{L^\infty(D_s(z_0))} \le c \|f\|_{L^1(D_r(z_0))}$ with $c = \frac{1}{\pi (r-s)^2}$ for any $s < r$.

<1>1. Mean Value Property on small disks:
    *Proof:*
    <2>1. Let $z \in D_s(z_0)$. The distance from $z$ to the boundary $\partial D_r(z_0)$ is at least $r - s > 0$.
    <2>2. Let $\delta = r - s$. The closed disk $\overline{D}_\delta(z)$ is contained in $D_r(z_0)$.
    <2>3. Because $f$ is holomorphic on $D_r(z_0)$, it satisfies the Mean Value Property on any disk centered at $z$. In polar coordinates, for any $\rho \in (0, \delta)$:
        $$f(z) = \frac{1}{2\pi} \int_0^{2\pi} f(z + \rho e^{i\theta}) \, d\theta.$$

<1>2. Area integration:
    *Proof:*
    <2>1. Multiply both sides by $\rho$ and integrate with respect to $\rho$ from $0$ to $\delta$:
        $$\int_0^\delta f(z) \rho \, d\rho = \frac{1}{2\pi} \int_0^\delta \int_0^{2\pi} f(z + \rho e^{i\theta}) \rho \, d\theta \, d\rho.$$
    <2>2. The left-hand side evaluates to:
        $$f(z) \left[\frac{\rho^2}{2}\right]_0^\delta = f(z) \frac{\delta^2}{2}.$$
    <2>3. The right-hand side is the area integral over the disk $D_\delta(z)$:
        $$\frac{1}{2\pi} \iint_{D_\delta(z)} f(w) \, dA(w).$$
    <2>4. Thus, dividing by $\delta^2/2$:
        $$f(z) = \frac{1}{\pi \delta^2} \iint_{D_\delta(z)} f(w) \, dA(w).$$

<1>3. Bounding $|f(z)|$:
    *Proof:*
    <2>1. Applying the triangle inequality for integrals:
        $$|f(z)| \le \frac{1}{\pi \delta^2} \iint_{D_\delta(z)} |f(w)| \, dA(w).$$
    <2>2. Since $D_\delta(z) \subseteq D_r(z_0)$ and $|f(w)| \ge 0$:
        $$\iint_{D_\delta(z)} |f(w)| \, dA(w) \le \iint_{D_r(z_0)} |f(w)| \, dA(w) = \|f\|_{(1, r)}.$$
    <2>3. Therefore, for every $z \in D_s(z_0)$:
        $$|f(z)| \le \frac{1}{\pi (r - s)^2} \|f\|_{(1, r)}.$$

<1>4. Taking the supremum over $z \in D_s(z_0)$:
    *Proof:*
    <2>1. Taking the supremum over all $z \in D_s(z_0)$ on the left-hand side:
        $$\|f\|_{(\infty, s)} = \sup_{z \in D_s(z_0)} |f(z)| \le \frac{1}{\pi (r - s)^2} \|f\|_{(1, r)}.$$
    <2>2. Setting the constant $c = \frac{1}{\pi (r - s)^2} > 0$ satisfies the inequality.

<1>5. Conclusion:
    The bound $\|f\|_{(\infty, s)} \le c \|f\|_{(1, r)}$ holds with $c = \frac{1}{\pi(r-s)^2}$. Q.E.D.
:::
