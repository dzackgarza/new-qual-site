---
schema: qual/card@1
id: P-AEWN6
kind: problem
title: '(a) $f: D\rightarrow {\mathbb C}$ be a continuous function, where'
classification:
  areas:
  - complex-analysis
  topics:
  - Contour Integration
  - Integrals
  - Complex Logarithm
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: problem
(a) $f: D\rightarrow {\mathbb C}$ be a continuous function, where $D\subset {\mathbb C}$ is a domain.Let $\alpha:[a,b]\rightarrow D$ be a smooth curve.
Give a precise definition of the *complex line integral* $$\int_{\alpha} f.$$

(b) Assume that there exists a constant $M$ such that $|f(\tau)|\leq M$ for all $\tau\in \mbox{\textrm Image}(\alpha$). Prove that $$\big | \int_{\alpha} f \big |\leq M \times \mbox{\textrm length}(\alpha).$$

(c) Let $C_R$ be the circle $|z|=R$, described in the counterclockwise direction, where $R>1$.
Provide an upper bound for $\big | \int_{C_R} \dfrac{\log{(z)} }{z^2} \big |,$ which depends [only]{.underline} on $R$ and other constants.
:::

::: {.solution}
**Goal:**

1. State the precise definition of the complex line integral $\int_\alpha f(z)\,dz$.

2. Prove the standard $ML$-inequality $\left|\int_\alpha f\right| \leq M \cdot \text{length}(\alpha)$.

3. Provide an explicit upper bound for $\left|\int_{C_R} \frac{\log z}{z^2}\,dz\right|$ for $R > 1$ using a single-valued branch on the contour (except at the branch cut point) or along the circle.

* * *

### Part (a): Definition of Complex Line Integral

<1>1. **Definition of $\int_\alpha f(z)\,dz$.** <2>1. Let $\alpha: [a, b] \to D \subset \mathbb{C}$ be a $C^1$ (smooth) parametrization, $\alpha(t) = x(t) + i y(t)$, and let $f: D \to \mathbb{C}$ be continuous.
*Proof:* Setting hypotheses.
<2>2. The complex line integral of $f$ along $\alpha$ is defined by the Riemann integral: $$\int_\alpha f(z) \, dz \coloneqq \int_a^b f(\alpha(t)) \alpha'(t) \, dt.$$ *Proof:* Standard definition of contour integral in complex analysis.
<2>3. Writing $f = u+iv$ and $\alpha' = x'+iy'$, this corresponds to the pair of real Riemann integrals $\int_a^b (u x' - v y')\,dt + i \int_a^b (u y' + v x')\,dt$.
*Proof:* Algebraic expansion of complex multiplication.
<2>4. Q.E.D.

* * *

### Part (b): Proof of the $ML$-Inequality

<1>2. **Let $I = \int_\alpha f(z)\,dz$.
If $I = 0$, the inequality holds trivially.** <2>1. If $I = 0$, then $|I| = 0 \leq M \cdot \text{length}(\alpha)$ because $M \geq 0$ and $\text{length}(\alpha) \geq 0$.
*Proof:* Non-negativity of length and supremum norm.
<2>2. Q.E.D.

<1>3. **Suppose $I \neq 0$.
Write $I = |I| e^{i\theta}$ for some $\theta \in \mathbb{R}$.** <2>1. Then $|I| = e^{-i\theta} I = e^{-i\theta} \int_a^b f(\alpha(t)) \alpha'(t) \, dt = \int_a^b e^{-i\theta} f(\alpha(t)) \alpha'(t) \, dt$.
*Proof:* Linearity of the integral with respect to complex scalars.
<2>2. Since $|I|$ is a positive real number, $|I| = \text{Re}(|I|) = \int_a^b \text{Re}\left( e^{-i\theta} f(\alpha(t)) \alpha'(t) \right) dt$.
*Proof:* Taking real parts.
<2>3. For any complex number $w \in \mathbb{C}$, $\text{Re}(w) \leq |w|$.
Applying this to $w = e^{-i\theta} f(\alpha(t)) \alpha'(t)$: $$\text{Re}\left( e^{-i\theta} f(\alpha(t)) \alpha'(t) \right) \leq \left| e^{-i\theta} f(\alpha(t)) \alpha'(t) \right| = |e^{-i\theta}| |f(\alpha(t))| |\alpha'(t)| = |f(\alpha(t))| |\alpha'(t)|.$$ *Proof:* $|e^{-i\theta}| = 1$ and multiplicativity of complex modulus.
<2>4. By hypothesis, $|f(\alpha(t))| \leq M$ for all $t \in [a, b]$.
*Proof:* Given bound on $\text{Image}(\alpha)$.
<2>5. Integrating the inequality: $$|I| \leq \int_a^b |f(\alpha(t))| |\alpha'(t)| \, dt \leq \int_a^b M |\alpha'(t)| \, dt = M \int_a^b |\alpha'(t)| \, dt.$$ *Proof:* Monotonicity of the Riemann integral for real-valued functions.
<2>6. By definition, the arc length of the smooth curve $\alpha$ is $\text{length}(\alpha) = \int_a^b |\alpha'(t)| \, dt$.
*Proof:* Standard definition of curve length.
<2>7. Therefore, $\left| \int_\alpha f \right| \leq M \cdot \text{length}(\alpha)$.
*Proof:* Substitution of <2>6 into <2>5. <2>8. Q.E.D.

* * *

### Part (c): Upper Bound for $\left|\int_{C_R} \frac{\log z}{z^2}\,dz\right|$

<1>4. **Bound the integrand on the circle $C_R: z = R e^{i\theta}$ ($\theta \in [-\pi, \pi]$).** <2>1. On $C_R$, $|z| = R > 1$, so $|z^2| = R^2$.
*Proof:* Modulus of power.
<2>2. Using the standard branch of $\log z = \ln|z| + i \arg(z) = \ln R + i\theta$ with $\theta \in [-\pi, \pi]$: $$|\log z| = |\ln R + i\theta| = \sqrt{(\ln R)^2 + \theta^2} \leq \sqrt{(\ln R)^2 + \pi^2} \leq \ln R + \pi.$$ *Proof:* Pythagorean modulus and the triangle inequality $\sqrt{a^2+b^2} \leq |a|+|b|$.
<2>3. Therefore, for all $z \in C_R$: $$\left| \frac{\log z}{z^2} \right| \leq \frac{\sqrt{(\ln R)^2 + \pi^2}}{R^2} \leq \frac{\ln R + \pi}{R^2} \eqqcolon M.$$ *Proof:* Quotient of upper bound on numerator by exact denominator modulus.
<2>4. The length of the circle $C_R$ is $L = 2\pi R$.
*Proof:* Circumference of a circle of radius $R$.
<2>5. By the $ML$-inequality from Part (b): $$\left| \int_{C_R} \frac{\log z}{z^2} \, dz \right| \leq M \cdot L = \frac{\sqrt{(\ln R)^2 + \pi^2}}{R^2} \cdot 2\pi R = \frac{2\pi \sqrt{(\ln R)^2 + \pi^2}}{R} \leq \frac{2\pi(\ln R + \pi)}{R}.$$ *Proof:* Direct application of <1>3.<2>7. <2>6. Q.E.D.
:::
