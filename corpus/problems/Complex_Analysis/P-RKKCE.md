---
schema: qual/card@1
id: P-RKKCE
kind: problem
title: $\int_{-\infty}^{\infty}\frac{e^{-2\pi ix\xi}}{\cosh\pi x}\,dx$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Contour Integration
  - Integrals
  - Hyperbolic Functions
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Compute the Fourier transform integral:
$$I(\xi) = \int_{-\infty}^{\infty} \frac{e^{-2\pi i x \xi}}{\cosh(\pi x)} \, dx$$
where $\xi \in \mathbb{R}$ and $\cosh z = \frac{e^z + e^{-z}}{2}$.
:::

::: solution
**Goal:** Compute $I(\xi) = \int_{-\infty}^\infty \frac{e^{-2\pi i x \xi}}{\cosh(\pi x)} dx = \frac{1}{\cosh(\pi \xi)}$ using a rectangular contour shifting by the period $i$.

<1>1. Holomorphic integrand and contour setup:
    *Proof:*
    <2>1. Let $f(z) = \frac{e^{-2\pi i z \xi}}{\cosh(\pi z)}$.
    <2>2. Note that $\cosh(\pi(z + i)) = \cosh(\pi z + i\pi) = -\cosh(\pi z)$.
    <2>3. Consider the rectangular contour $\Gamma_R$ with vertices at $-R, R, R + i, -R + i$ oriented counterclockwise:
        - Bottom edge $\gamma_1$: from $-R$ to $R$ along the real line ($z = x$).
        - Right edge $\gamma_2$: from $R$ to $R + i$ ($z = R + iy, y \in [0, 1]$).
        - Top edge $\gamma_3$: from $R + i$ to $-R + i$ ($z = x + i, x$ from $R$ down to $-R$).
        - Left edge $\gamma_4$: from $-R + i$ to $-R$ ($z = -R + iy, y$ from $1$ down to $0$).

<1>2. Singularities and Residues inside the contour $\Gamma_R$:
    *Proof:*
    <2>1. The poles of $f(z)$ occur where $\cosh(\pi z) = 0 \iff e^{2\pi z} = -1 \iff \pi z = i\frac{\pi}{2} + i k\pi \iff z = i(k + 1/2)$ for $k \in \mathbb{Z}$.
    <2>2. Inside the strip $0 < \operatorname{Im}(z) < 1$, there is exactly **one simple pole**, located at $z_0 = \frac{i}{2}$.
    <2>3. Compute the residue at $z_0 = i/2$:
        $$\operatorname{Res}\left(f, \frac{i}{2}\right) = \frac{e^{-2\pi i (i/2) \xi}}{\pi \sinh(\pi (i/2))} = \frac{e^{\pi \xi}}{\pi \sinh(i\pi/2)} = \frac{e^{\pi \xi}}{\pi (i \sin(\pi/2))} = \frac{e^{\pi \xi}}{i\pi} = -\frac{i}{\pi} e^{\pi \xi}.$$
    <2>4. By the Cauchy Residue Theorem:
        $$\oint_{\Gamma_R} f(z) \, dz = 2\pi i \operatorname{Res}\left(f, \frac{i}{2}\right) = 2\pi i \left( -\frac{i}{\pi} e^{\pi \xi} \right) = 2 e^{\pi \xi}.$$

<1>3. Evaluation along the sides and limit as $R \to \infty$:
    *Proof:*
    <2>1. **Vertical edges $\gamma_2, \gamma_4$:**
        For $z = \pm R + iy$ ($y \in [0, 1]$):
        $$|\cosh(\pi(\pm R + iy))| \ge \frac{1}{2}(e^{\pi R} - e^{-\pi R}), \qquad |e^{-2\pi i (\pm R + iy) \xi}| = e^{2\pi y \xi} \le e^{2\pi |\xi|}.$$
        Thus $\left| \int_{\gamma_{2, 4}} f(z) \, dz \right| \le \frac{e^{2\pi |\xi|}}{\frac{1}{2}(e^{\pi R} - e^{-\pi R})} \xrightarrow{R \to \infty} 0$.
    <2>2. **Top edge $\gamma_3$:**
        Parameterize with $z = x + i$ for $x \in [R, -R]$:
        $$\int_{\gamma_3} f(z) \, dz = \int_R^{-R} \frac{e^{-2\pi i (x + i) \xi}}{\cosh(\pi (x + i))} \, dx = \int_R^{-R} \frac{e^{-2\pi i x \xi} e^{2\pi \xi}}{-\cosh(\pi x)} \, dx = e^{2\pi \xi} \int_{-R}^R \frac{e^{-2\pi i x \xi}}{\cosh(\pi x)} \, dx.$$
    <2>3. Combining the top and bottom edges as $R \to \infty$:
        $$\lim_{R \to \infty} \oint_{\Gamma_R} f(z) \, dz = (1 + e^{2\pi \xi}) \int_{-\infty}^\infty \frac{e^{-2\pi i x \xi}}{\cosh(\pi x)} \, dx = (1 + e^{2\pi \xi}) I(\xi).$$

<1>4. Solving for $I(\xi)$:
    *Proof:*
    <2>1. Equating the contour integral to the residue value:
        $$(1 + e^{2\pi \xi}) I(\xi) = 2 e^{\pi \xi}.$$
    <2>2. Dividing both sides by $e^{\pi \xi} (e^{\pi \xi} + e^{-\pi \xi}) = 1 + e^{2\pi \xi}$:
        $$I(\xi) = \frac{2 e^{\pi \xi}}{1 + e^{2\pi \xi}} = \frac{2}{e^{-\pi \xi} + e^{\pi \xi}} = \frac{1}{\cosh(\pi \xi)}.$$

<1>5. Conclusion:
    $$\int_{-\infty}^{\infty} \frac{e^{-2\pi i x \xi}}{\cosh(\pi x)} \, dx = \frac{1}{\cosh(\pi \xi)}.$$ Q.E.D.
:::
