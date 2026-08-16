---
schema: qual/card@1
id: P-AMD-OOYYQNH5
kind: problem
title: Use the Cauchy integral formula to prove the maximal principle for
classification:
  areas:
  - complex-analysis
  topics:
  - maximum-modulus-principle
  - cauchy-integral-formula
relations: []
review: draft
---

::: {.problem}
Use the Cauchy integral formula to prove the maximal principle for analytic functions.
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**Goal:** Let $\Omega \subset \mathbb{C}$ be a connected open set (domain) and let $f: \Omega \to \mathbb{C}$ be holomorphic.
Prove using the Cauchy integral formula that if there exists a point $z_0 \in \Omega$ such that $|f(z_0)| \geq |f(z)|$ for all $z \in \Omega$, then $f$ is constant on $\Omega$.

* * *

### Step 1: Mean Value Property via Cauchy Integral Formula

<1>1. **For any $z_0 \in \Omega$ and any $r > 0$ such that the closed disk $\overline{D}(z_0, r) \subset \Omega$, $f(z_0) = \frac{1}{2\pi} \int_0^{2\pi} f(z_0 + r e^{i\theta}) \, d\theta$.** <2>1. By the Cauchy integral formula, since $f$ is holomorphic on $\Omega$ and $\overline{D}(z_0, r) \subset \Omega$: $$f(z_0) = \frac{1}{2\pi i} \oint_{|z-z_0|=r} \frac{f(z)}{z-z_0} \, dz.$$ *Proof:* The boundary circle $\gamma(\theta) = z_0 + r e^{i\theta}$ ($\theta \in [0, 2\pi]$) is a simple closed positively oriented contour whose interior $D(z_0, r)$ contains $z_0$ and lies in $\Omega$.
<2>2. Parametrizing the contour by $z(\theta) = z_0 + r e^{i\theta}$ with $dz = i r e^{i\theta} d\theta$: $$f(z_0) = \frac{1}{2\pi i} \int_0^{2\pi} \frac{f(z_0 + r e^{i\theta})}{r e^{i\theta}} i r e^{i\theta} \, d\theta = \frac{1}{2\pi} \int_0^{2\pi} f(z_0 + r e^{i\theta}) \, d\theta.$$ *Proof:* Direct substitution of parameterization.
<2>3. Q.E.D.

* * *

### Step 2: Local Constancy at a Maximum Point

<1>2. **If $|f(z_0)| = \max_{z \in \Omega} |f(z)|$, then $f(z) = f(z_0)$ for all $z$ in some disk $D(z_0, R) \subset \Omega$.** <2>1. If $f(z_0) = 0$, then $|f(z)| \leq |f(z_0)| = 0$ for all $z \in \Omega$, so $f(z) = 0$ everywhere on $\Omega$.
*Proof:* Modulus is non-negative, so $|f(z)| \leq 0 \implies f(z) = 0$.
<2>2. Now assume $M = |f(z_0)| > 0$.
Let $f(z_0) = M e^{i\alpha}$ for some $\alpha \in \mathbb{R}$.
Consider the rotated function $g(z) = e^{-i\alpha} f(z)$, which is holomorphic on $\Omega$ and satisfies $g(z_0) = M = |g(z_0)|$.
*Proof:* Multiplication by a constant unimodular factor preserves holomorphicity and modulus: $|g(z)| = |f(z)| \leq M$ for all $z \in \Omega$.
<2>3. Choose $R > 0$ such that $\overline{D}(z_0, R) \subset \Omega$.
For any $0 < r < R$, by <1>1: $$M = g(z_0) = \frac{1}{2\pi} \int_0^{2\pi} g(z_0 + r e^{i\theta}) \, d\theta.$$ *Proof:* Apply the mean value property to the holomorphic function $g$.
<2>4. Taking the real part of both sides: $$M = \frac{1}{2\pi} \int_0^{2\pi} \text{Re}(g(z_0 + r e^{i\theta})) \, d\theta \implies \frac{1}{2\pi} \int_0^{2\pi} \Big( M - \text{Re}(g(z_0 + r e^{i\theta})) \Big) \, d\theta = 0.$$ *Proof:* $\text{Re}(M) = M$ since $M \in \mathbb{R}$, and linearity of the integral.
<2>5. For every $\theta \in [0, 2\pi]$, $\text{Re}(g(z_0 + r e^{i\theta})) \leq |g(z_0 + r e^{i\theta})| \leq M$, which means the integrand $h(\theta) = M - \text{Re}(g(z_0 + r e^{i\theta}))$ is continuous and non-negative: $h(\theta) \geq 0$.
*Proof:* Real part is bounded by absolute value, and $|g(z)| \leq M$ by assumption.
<2>6. Since $h(\theta) \geq 0$ is continuous and $\int_0^{2\pi} h(\theta)\,d\theta = 0$, it follows that $h(\theta) = 0$ for all $\theta \in [0, 2\pi]$, hence $\text{Re}(g(z_0 + r e^{i\theta})) = M$ for all $\theta \in [0, 2\pi]$.
*Proof:* A non-negative continuous function with zero integral must be identically zero.
<2>7. Since $\text{Re}(g(z)) = M$ on the circle $|z-z_0|=r$ and $|g(z)| \leq M$, we have $M^2 \geq |g(z)|^2 = (\text{Re}(g(z)))^2 + (\text{Im}(g(z)))^2 = M^2 + (\text{Im}(g(z)))^2 \implies \text{Im}(g(z)) = 0$.
*Proof:* $(\text{Im}(g(z)))^2 \leq 0 \implies \text{Im}(g(z)) = 0$.
<2>8. Thus $g(z) = M + 0i = M$ for all $z$ on $|z-z_0|=r$.
Since $r \in (0, R)$ was arbitrary, $g(z) = M$ for all $z \in D(z_0, R)$, which implies $f(z) = M e^{i\alpha} = f(z_0)$ on $D(z_0, R)$.
*Proof:* Union of concentric circles $\{z : |z-z_0|=r\}$ for $r \in (0, R)$ together with the center $z_0$ is the disk $D(z_0, R)$.
<2>9. Q.E.D.

* * *

### Step 3: Global Constancy on the Connected Domain $\Omega$

<1>3. **$f$ is constant on the entire domain $\Omega$.** <2>1. Define the set $E = \{ z \in \Omega : f(z) = f(z_0) \}$.
*Proof:* Definition of fiber.
<2>2. $E$ is non-empty since $z_0 \in E$.
*Proof:* $f(z_0) = f(z_0)$.
<2>3. $E$ is closed in $\Omega$ by continuity of $f$: $E = (f - f(z_0))^{-1}(\{0\})$.
*Proof:* Preimage of the closed set $\{0\}$ under the continuous function $f - f(z_0)$.
<2>4. $E$ is open in $\Omega$: for any $w \in E$, $|f(w)| = |f(z_0)| = \max_{z \in \Omega} |f(z)|$, so by applying <1>2 at $w$, there exists a disk $D(w, r_w) \subset \Omega$ on which $f(z) = f(w) = f(z_0)$, which means $D(w, r_w) \subset E$.
*Proof:* Every point in $E$ is a local maximum for $|f|$, hence has an open neighborhood contained in $E$.
<2>5. Since $\Omega$ is connected, the only non-empty subset of $\Omega$ that is both open and closed in $\Omega$ is $\Omega$ itself.
Thus $E = \Omega$.
*Proof:* Definition of topological connectedness.
<2>6. Hence $f(z) = f(z_0)$ for all $z \in \Omega$, so $f$ is constant on $\Omega$.
*Proof:* Follows from $E = \Omega$.
<2>7. Q.E.D.
:::
