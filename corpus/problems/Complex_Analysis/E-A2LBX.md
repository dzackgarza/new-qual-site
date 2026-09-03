---
schema: qual/card@1
id: E-A2LBX
kind: problem
title: '$f: D\rightarrow {\mathbb C}$ be a continuous function, where'
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
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: exercise
a. $f: D\rightarrow {\mathbb C}$ be a continuous function, where $D\subset {\mathbb C}$ is a domain.Let $\alpha:[a,b]\rightarrow D$ be a smooth curve.
Give a precise definition of the *complex line integral* $$\int_{\alpha} f.$$

b. Assume that there exists a constant $M$ such that $|f(\tau)|\leq M$ for all $\tau\in \mbox{\textrm Image}(\alpha$). Prove that $$\big | \int_{\alpha} f \big |\leq M \times \mbox{\textrm length}(\alpha).$$

c. Let $C_R$ be the circle $|z|=R$, described in the counterclockwise direction, where $R>1$.
Provide an upper bound for $\big | \int_{C_R} \dfrac{\log{(z)} }{z^2} \big |,$ which depends *only* on $R$ and other constants.
:::

::: solution
**Goal:** Define the complex line integral, prove the Estimation Lemma ($ML$-inequality), and compute an explicit upper bound for $\left| \int_{C_R} \frac{\log z}{z^2} \, dz \right|$ on the circle $|z| = R$.

<1>1. Part (a): Definition of complex line integral: Let $D \subset \mathbb{C}$ be a domain, $f: D \to \mathbb{C}$ a continuous function, and $\alpha: [a, b] \to D$ a smooth (or piecewise $C^1$) curve.
The **complex line integral** of $f$ along $\alpha$ is defined by: $$\int_\alpha f(z) \, dz = \int_a^b f(\alpha(t)) \alpha'(t) \, dt,$$ where the right-hand side is the standard Riemann integral of the complex-valued function of a real variable $t \mapsto f(\alpha(t)) \alpha'(t) = u(t) + i v(t)$.

<1>2. Part (b): Proof of the $ML$-inequality: *Proof:* <2>1. Let $I = \int_\alpha f(z) \, dz = \int_a^b f(\alpha(t)) \alpha'(t) \, dt \in \mathbb{C}$.
<2>2. If $I = 0$, then $|I| = 0 \le M \cdot \operatorname{length}(\alpha)$ holds since $M \ge 0$ and $\operatorname{length}(\alpha) \ge 0$.
<2>3. If $I \neq 0$, write $I$ in polar form as $I = |I| e^{i\theta}$ for some $\theta \in [0, 2\pi)$.
<2>4. Multiplying both sides by $e^{-i\theta}$: $$|I| = e^{-i\theta} \int_a^b f(\alpha(t)) \alpha'(t) \, dt = \int_a^b e^{-i\theta} f(\alpha(t)) \alpha'(t) \, dt.$$ <2>5. Since $|I|$ is real, it equals the real part of the integral: $$|I| = \operatorname{Re}\left( \int_a^b e^{-i\theta} f(\alpha(t)) \alpha'(t) \, dt \right) = \int_a^b \operatorname{Re}\left( e^{-i\theta} f(\alpha(t)) \alpha'(t) \right) \, dt.$$ <2>6. Using the inequality $\operatorname{Re}(w) \le |w|$ for all $w \in \mathbb{C}$: $$|I| \le \int_a^b \left| e^{-i\theta} f(\alpha(t)) \alpha'(t) \right| \, dt = \int_a^b |f(\alpha(t))| |\alpha'(t)| \, dt.$$ <2>7. Since $|f(\alpha(t))| \le M$ for all $t \in [a, b]$: $$|I| \le M \int_a^b |\alpha'(t)| \, dt = M \cdot \operatorname{length}(\alpha).$$

<1>3. Part (c): Upper bound on the circle $C_R$: *Proof:* <2>1. For the circle $C_R = \{z \in \mathbb{C} \mid |z| = R\}$ with $R > 1$, parameterized by $\alpha(t) = R e^{it}$ for $t \in [-\pi, \pi]$ (or choosing the branch of the logarithm $\log z = \ln |z| + i \operatorname{Arg}(z)$ with $\operatorname{Arg}(z) \in (-\pi, \pi]$): <2>2. For any $z \in C_R$, $|z| = R > 1$, so: $$|\log z| = |\ln R + i \operatorname{Arg}(z)| \le \ln R + |\operatorname{Arg}(z)| \le \ln R + \pi.$$ (Alternatively, $|\log z| \le \sqrt{(\ln R)^2 + \pi^2}$). <2>3. The denominator satisfies $|z^2| = |z|^2 = R^2$.
<2>4. Thus the integrand is bounded on $C_R$ by: $$\left| \frac{\log z}{z^2} \right| \le \frac{\ln R + \pi}{R^2}.$$ <2>5. The arc length of the contour is $\operatorname{length}(C_R) = 2\pi R$.
<2>6. Applying the $ML$-inequality from Part (b): $$\left| \int_{C_R} \frac{\log z}{z^2} \, dz \right| \le \left( \frac{\ln R + \pi}{R^2} \right) (2\pi R) = \frac{2\pi(\ln R + \pi)}{R}.$$

<1>4. Conclusion: The complex line integral is well-defined, satisfies the $ML$-inequality, and $\left| \int_{C_R} \frac{\log z}{z^2} \, dz \right| \le \frac{2\pi \ln R + 2\pi^2}{R}$.
Q.E.D.
:::
