---
schema: qual/card@1
id: E-SS2.EX-11
kind: exercise
title: "Cauchy estimates on a smaller disk"
classification:
  areas:
  - complex-analysis
  topics: ["Cauchy's Theorem", 'Contour Integration', 'Residues']
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: exercise
Let $f$ be a holomorphic function on the disk $D_{R_0}(0) \subset \mathbb{C}$ of radius $R_0 > 0$.

(a) Prove that whenever $0 < R < R_0$ and $|z| < R$,
$$
f(z) = \frac{1}{2\pi} \int_0^{2\pi} f(R e^{i\varphi}) \operatorname{Re}\left( \frac{R e^{i\varphi} + z}{R e^{i\varphi} - z} \right) d\varphi.
$$

(b) Show that for $z = r \in [0, R)$ (and in general with $\gamma = \varphi - \theta$ where $z = r e^{i\theta}$):
$$
\operatorname{Re}\left( \frac{R e^{i\gamma} + r}{R e^{i\gamma} - r} \right) = \frac{R^2 - r^2}{R^2 - 2Rr\cos\gamma + r^2}.
$$
:::

::: solution
**Goal:** Prove the Poisson integral formula for holomorphic functions and compute the explicit real part of the Schwarz kernel (Poisson kernel).

<1>1. Part (b): Real Part of the Schwarz Kernel (Poisson Kernel):
    *Proof:*
    <2>1. Let $w = R e^{i\gamma} = R(\cos\gamma + i\sin\gamma)$ and $r \in \mathbb{R}$.
    <2>2. Consider the quotient:
        $$\frac{R e^{i\gamma} + r}{R e^{i\gamma} - r} = \frac{(R e^{i\gamma} + r)(R e^{-i\gamma} - r)}{|R e^{i\gamma} - r|^2}.$$
    <2>3. Expand the denominator:
        $$|R e^{i\gamma} - r|^2 = (R\cos\gamma - r)^2 + (R\sin\gamma)^2 = R^2\cos^2\gamma - 2Rr\cos\gamma + r^2 + R^2\sin^2\gamma = R^2 - 2Rr\cos\gamma + r^2.$$
    <2>4. Expand the numerator:
        $$(R e^{i\gamma} + r)(R e^{-i\gamma} - r) = R^2 - R r e^{i\gamma} + R r e^{-i\gamma} - r^2 = (R^2 - r^2) - R r (e^{i\gamma} - e^{-i\gamma}) = (R^2 - r^2) - 2 i R r \sin\gamma.$$
    <2>5. Taking the real part:
        $$\operatorname{Re}\left( \frac{R e^{i\gamma} + r}{R e^{i\gamma} - r} \right) = \frac{R^2 - r^2}{R^2 - 2Rr\cos\gamma + r^2}.$$

<1>2. Part (a): Cauchy Integral Formula with Reflected Point $w = R^2 / \bar{z}$:
    *Proof:*
    <2>1. Let $|z| < R < R_0$. By the standard **Cauchy Integral Formula** on the circle $\partial D_R = \{ \zeta \in \mathbb{C} \mid |\zeta| = R \}$:
        $$f(z) = \frac{1}{2\pi i} \oint_{|\zeta|=R} \frac{f(\zeta)}{\zeta - z} \, d\zeta.$$
    <2>2. Consider the point $w \coloneqq \frac{R^2}{\bar{z}}$, which is the geometric reflection of $z$ across the circle $|\zeta| = R$.
    <2>3. Since $|z| < R$, we have $|w| = \frac{R^2}{|z|} > R$.
    <2>4. Thus $w$ lies strictly outside the closed disk $\overline{D_R}$.
    <2>5. Since $\zeta \mapsto \frac{f(\zeta)}{\zeta - w}$ is holomorphic on an open neighborhood of $\overline{D_R}$, by **Cauchy's Theorem**:
        $$0 = \frac{1}{2\pi i} \oint_{|\zeta|=R} \frac{f(\zeta)}{\zeta - w} \, d\zeta.$$
    <2>6. Subtracting this zero integral from the Cauchy Integral Formula for $f(z)$:
        $$f(z) = \frac{1}{2\pi i} \oint_{|\zeta|=R} f(\zeta) \left( \frac{1}{\zeta - z} - \frac{1}{\zeta - w} \right) d\zeta.$$

<1>3. Simplifying the Kernel Along the Circle $|\zeta| = R$:
    *Proof:*
    <2>1. Parameterize the circle $\zeta = R e^{i\varphi}$ with $d\zeta = i R e^{i\varphi} d\varphi = i \zeta \, d\varphi$, so $\frac{d\zeta}{i\zeta} = d\varphi$.
    <2>2. Notice that on $|\zeta| = R$, $\bar{\zeta} \zeta = R^2$, so $w = \frac{R^2}{\bar{z}} = \frac{\zeta \bar{\zeta}}{\bar{z}}$.
    <2>3. We evaluate the expression multiplying $f(\zeta) \frac{d\zeta}{2\pi i}$:
        $$\frac{1}{\zeta - z} - \frac{1}{\zeta - w} = \frac{1}{\zeta - z} + \frac{1}{w - \zeta} = \frac{1}{\zeta - z} + \frac{1}{\frac{R^2}{\bar{z}} - \zeta} = \frac{1}{\zeta - z} + \frac{\bar{z}}{R^2 - \zeta\bar{z}}.$$
    <2>4. Multiplying by $\zeta$ (to match $d\zeta = i\zeta\,d\varphi$):
        $$\zeta \left( \frac{1}{\zeta - z} + \frac{\bar{z}}{R^2 - \zeta\bar{z}} \right) = \frac{\zeta}{\zeta - z} + \frac{\zeta \bar{z}}{\bar{\zeta}\zeta - \zeta\bar{z}} = \frac{\zeta}{\zeta - z} + \frac{\bar{z}}{\bar{\zeta} - \bar{z}}.$$
    <2>5. Notice that the second term is the complex conjugate of $\frac{z}{\zeta - z}$:
        $$\frac{\zeta}{\zeta - z} + \overline{\left( \frac{z}{\zeta - z} \right)} = 1 + \frac{z}{\zeta - z} + \overline{\left( \frac{z}{\zeta - z} \right)} = 1 + 2\operatorname{Re}\left( \frac{z}{\zeta - z} \right) = \operatorname{Re}\left( 1 + \frac{2z}{\zeta - z} \right) = \operatorname{Re}\left( \frac{\zeta + z}{\zeta - z} \right).$$
    <2>6. Substituting $\zeta = R e^{i\varphi}$ and $d\zeta = i \zeta \, d\varphi$ into the integral:
        $$f(z) = \frac{1}{2\pi} \int_0^{2\pi} f(R e^{i\varphi}) \operatorname{Re}\left( \frac{R e^{i\varphi} + z}{R e^{i\varphi} - z} \right) d\varphi.$$

<1>4. Conclusion:
    The formula holds via Cauchy integral formula combined with the reflected pole point $w = R^2/\bar{z}$, and the real part evaluates to the Poisson kernel $\frac{R^2 - r^2}{R^2 - 2Rr\cos\gamma + r^2}$. Q.E.D.
:::
