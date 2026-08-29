---
schema: qual/card@1
id: P-RMM73
kind: problem
title: Holomorphic functions in a neighborhood of $D_r(z_0)$
classification:
  areas:
  - complex-analysis
  topics:
  - Holomorphic Functions
  - Cauchy Estimates
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Let $f$ be holomorphic in a neighborhood of the closed disk $\overline{D}_r(z_0)$.
Prove Cauchy's estimate for derivatives:
$$|f^{(n)}(z_0)| \le \frac{n!}{r^n} \max_{|z-z_0| = r} |f(z)|$$
and the Mean Value Property:
$$f(z_0) = \frac{1}{2\pi} \int_0^{2\pi} f(z_0 + r e^{i\theta}) \, d\theta.$$
:::

::: solution
**Goal:** Prove the Mean Value Property and Cauchy's Estimates for derivatives on disks.

<1>1. Cauchy Integral Formula for derivatives:
    *Proof:*
    <2>1. Let $\gamma(t) = z_0 + r e^{it}$ for $t \in [0, 2\pi]$ parameterize the circle $C = \partial D_r(z_0)$ with counterclockwise orientation.
    <2>2. Since $f$ is holomorphic on an open neighborhood containing $\overline{D}_r(z_0)$, by Cauchy's Integral Formula for derivatives:
        $$f^{(n)}(z_0) = \frac{n!}{2\pi i} \oint_{\gamma} \frac{f(z)}{(z - z_0)^{n+1}} \, dz \quad \text{for every } n \ge 0.$$

<1>2. Proof of the Mean Value Property ($n = 0$):
    *Proof:*
    <2>1. For $n = 0$, $f(z_0) = \frac{1}{2\pi i} \oint_\gamma \frac{f(z)}{z - z_0} \, dz$.
    <2>2. Substitute $z = z_0 + r e^{i\theta}$, so $dz = i r e^{i\theta} d\theta$:
        $$f(z_0) = \frac{1}{2\pi i} \int_0^{2\pi} \frac{f(z_0 + r e^{i\theta})}{r e^{i\theta}} (i r e^{i\theta}) \, d\theta = \frac{1}{2\pi} \int_0^{2\pi} f(z_0 + r e^{i\theta}) \, d\theta.$$
    <2>3. This establishes the Mean Value Property.

<1>3. Proof of Cauchy's Estimates ($n \ge 1$):
    *Proof:*
    <2>1. Let $M_r = \max_{|z-z_0| = r} |f(z)| = \max_{z \in C} |f(z)|$.
    <2>2. Using the standard ML-inequality for contour integrals on $f^{(n)}(z_0)$:
        $$\left| f^{(n)}(z_0) \right| = \left| \frac{n!}{2\pi i} \oint_\gamma \frac{f(z)}{(z - z_0)^{n+1}} \, dz \right| \le \frac{n!}{2\pi} \oint_\gamma \frac{|f(z)|}{|z - z_0|^{n+1}} \, |dz|.$$
    <2>3. Along the circle $\gamma$, $|z - z_0| = r$, so $\frac{|f(z)|}{|z - z_0|^{n+1}} \le \frac{M_r}{r^{n+1}}$.
    <2>4. The length of the contour $\gamma$ is $L(\gamma) = 2\pi r$.
    <2>5. Therefore:
        $$\left| f^{(n)}(z_0) \right| \le \frac{n!}{2\pi} \cdot \frac{M_r}{r^{n+1}} \cdot (2\pi r) = \frac{n! M_r}{r^n} = \frac{n!}{r^n} \max_{|z-z_0|=r} |f(z)|.$$

<1>4. Conclusion:
    The Mean Value Property and Cauchy's estimates are proved. Q.E.D.
:::
