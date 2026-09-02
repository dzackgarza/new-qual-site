---
schema: qual/card@1
id: P-MMAQ-ZTRBMIG65D
kind: problem
title: Cauchy integral formula for holomorphic functions
classification:
  areas:
  - complex-analysis
  topics:
  - Cauchy Integral Formula
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: problem
State and prove the Cauchy integral formula for holomorphic functions.
:::

::: {.solution}
**Goal:** State and prove the Cauchy Integral Formula for holomorphic functions.

* * *

### Statement of the Cauchy Integral Formula

**Theorem:** Let $\Omega \subseteq \mathbb{C}$ be an open domain, and let $f: \Omega \to \mathbb{C}$ be a holomorphic function.
Let $\gamma$ be a positively oriented, simple closed rectifiable curve in $\Omega$ whose interior $\text{Int}(\gamma)$ is contained in $\Omega$.
Then for every point $z_0 \in \text{Int}(\gamma)$: $$f(z_0) = \frac{1}{2\pi i} \oint_\gamma \frac{f(z)}{z - z_0} \, dz.$$

* * *

### Proof

<1>1. **Isolate the singularity at $z_0$ using a small circle $C_\varepsilon$.** <2>1. Since $z_0 \in \text{Int}(\gamma)$ and $\text{Int}(\gamma)$ is open, there exists $\varepsilon_0 > 0$ such that the closed disk $\overline{D}(z_0, \varepsilon_0) \subset \text{Int}(\gamma)$.
*Proof:* $\text{Int}(\gamma)$ is an open neighborhood of $z_0$.
<2>2. For any $\varepsilon \in (0, \varepsilon_0)$, let $C_\varepsilon$ denote the circle $\{z \in \mathbb{C} : |z - z_0| = \varepsilon\}$, oriented counterclockwise.
*Proof:* Standard circular contour definition.
<2>3. The function $g(z) \coloneqq \frac{f(z)}{z - z_0}$ is holomorphic in the region $\Omega' = \text{Int}(\gamma) \setminus \overline{D}(z_0, \varepsilon)$.
*Proof:* Quotient of holomorphic functions with non-vanishing denominator on $\Omega'$.
<2>4. By Cauchy's Integral Theorem for multiply connected domains: $$\oint_\gamma \frac{f(z)}{z - z_0} \, dz = \oint_{C_\varepsilon} \frac{f(z)}{z - z_0} \, dz.$$ *Proof:* The boundary of $\Omega'$ is $\gamma - C_\varepsilon$, and $\oint_{\partial \Omega'} g(z)\,dz = 0$.
<2>5. Q.E.D.

<1>2. **Evaluate the constant-numerator integral on $C_\varepsilon$.** <2>1. Parametrize $C_\varepsilon$ by $z(\theta) = z_0 + \varepsilon e^{i\theta}$ for $\theta \in [0, 2\pi]$, so $dz = i \varepsilon e^{i\theta} d\theta$.
*Proof:* Definition of circular parametrization.
<2>2. The integral of $\frac{1}{z - z_0}$ evaluates to: $$\oint_{C_\varepsilon} \frac{dz}{z - z_0} = \int_0^{2\pi} \frac{i \varepsilon e^{i\theta}}{\varepsilon e^{i\theta}} \, d\theta = i \int_0^{2\pi} d\theta = 2\pi i.$$ *Proof:* Direct cancellation of $\varepsilon e^{i\theta}$.
<2>3. Multiplying by the constant $f(z_0)$: $$\oint_{C_\varepsilon} \frac{f(z_0)}{z - z_0} \, dz = f(z_0) \oint_{C_\varepsilon} \frac{dz}{z - z_0} = 2\pi i f(z_0).$$ *Proof:* Linearity of integration.
<2>4. Q.E.D.

<1>3. **Split the integral into the value at $z_0$ and an error term.** <2>1. Subtracting the identity from <1>2.<2>3: $$\oint_\gamma \frac{f(z)}{z - z_0} \, dz - 2\pi i f(z_0) = \oint_{C_\varepsilon} \frac{f(z) - f(z_0)}{z - z_0} \, dz.$$ *Proof:* Follows from <1>1.<2>4 and <1>2.<2>3. <2>2. Q.E.D.

<1>4. **Show that the error term vanishes as $\varepsilon \to 0^+$.** <2>1. Since $f$ is holomorphic at $z_0$, $f$ is continuous at $z_0$: for any $\delta > 0$, there exists $\varepsilon > 0$ such that $|z - z_0| = \varepsilon \implies |f(z) - f(z_0)| \leq \delta$.
*Proof:* Continuity of $f$ at $z_0$.
<2>2. On $C_\varepsilon$, the integrand is bounded by: $$\left| \frac{f(z) - f(z_0)}{z - z_0} \right| = \frac{|f(z) - f(z_0)|}{\varepsilon} \leq \frac{\delta}{\varepsilon}.$$ *Proof:* $|z - z_0| = \varepsilon$.
<2>3. The length of $C_\varepsilon$ is $2\pi \varepsilon$.
*Proof:* Circumference of circle of radius $\varepsilon$.
<2>4. By the $ML$-inequality: $$\left| \oint_{C_\varepsilon} \frac{f(z) - f(z_0)}{z - z_0} \, dz \right| \leq \frac{\delta}{\varepsilon} \cdot (2\pi \varepsilon) = 2\pi \delta.$$ *Proof:* $ML$-inequality for contour integrals.
<2>5. Since the LHS of <1>3.<2>1 is independent of $\varepsilon$, and $\delta > 0$ can be made arbitrarily small by choosing $\varepsilon$ small, the error integral must be identically 0: $$\oint_\gamma \frac{f(z)}{z - z_0} \, dz - 2\pi i f(z_0) = 0.$$ *Proof:* A non-negative quantity bounded by $2\pi\delta$ for all $\delta > 0$ is 0. <2>6. Q.E.D.

<1>5. **Conclusion.** <2>1. Dividing by $2\pi i$ gives: $$f(z_0) = \frac{1}{2\pi i} \oint_\gamma \frac{f(z)}{z - z_0} \, dz.$$ *Proof:* Rearrangement of <1>4.<2>5. <2>2. Q.E.D.
:::
