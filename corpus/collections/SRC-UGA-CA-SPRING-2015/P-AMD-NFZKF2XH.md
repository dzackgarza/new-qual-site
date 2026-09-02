---
schema: qual/card@1
id: P-AMD-NFZKF2XH
kind: problem
title: Blaschke-factor integral identities and a half-disk conformal map
classification:
  areas:
  - complex-analysis
  topics:
  - Blaschke Factors
  - Conformal Maps
  - Integrals
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Let $\displaystyle{\psi_{\alpha}(z)=\frac{\alpha-z}{1-\bar{\alpha}z}}$ with $|\alpha|<1$ and ${\mathbb D}=\{z:\ |z|<1\}$.
Prove that

- $\displaystyle{\frac{1}{\pi}\iint_{{\mathbb D}} |\psi'_{\alpha}|^2 dx dy =1}$.

- Show that
  $$
  \frac{1}{\pi}\iint_{{\mathbb D}} |\psi'_{\alpha}| dx dy
  =\frac{1-|\alpha|^2}{|\alpha|^2}\log \frac{1}{1-|\alpha|^2}.
  $$

Prove that $\displaystyle{f(z)=-\frac{1}{2}\left(z+\frac{1}{z}\right)}$ is a conformal map from half disc $\{z=x+iy:\ |z|<1,\ y>0\}$ to upper half plane $\mathbb H=\{z=x+iy:\ y>0\}$.
:::

::: {.solution}
**Goal:**

1. For $\psi_\alpha(z) = \frac{\alpha - z}{1 - \bar{\alpha}z}$ with $|\alpha| < 1$, prove that $\frac{1}{\pi}\iint_{\mathbb{D}} |\psi_\alpha'(z)|^2 \,dx\,dy = 1$.

2. Prove that $\frac{1}{\pi}\iint_{\mathbb{D}} |\psi_\alpha'(z)| \,dx\,dy = \frac{1-|\alpha|^2}{|\alpha|^2}\log\left(\frac{1}{1-|\alpha|^2}\right)$ (for $\alpha \neq 0$, with limit $1$ as $\alpha \to 0$).

3. Prove that $f(z) = -\frac{1}{2}\left(z + \frac{1}{z}\right)$ is a conformal map from the upper half-disk $\mathbb{D}^+ = \{z = x+iy : |z| < 1, y > 0\}$ to the upper half-plane $\mathbb{H} = \{w = u+iv : v > 0\}$.

* * *

### Part 1: Area Integral of $|\psi_\alpha'(z)|^2$

<1>1. **$\psi_\alpha$ is a biholomorphic automorphism of the unit disk $\mathbb{D}$.** <2>1. $\psi_\alpha$ is a Möbius transformation with pole at $z = 1/\bar{\alpha}$.
Since $|\alpha| < 1$, $|1/\bar{\alpha}| > 1$, so $\psi_\alpha$ is holomorphic in a neighborhood of $\overline{\mathbb{D}}$.
*Proof:* Pole lies strictly outside the closed unit disk.
<2>2. For $|z| = 1$, $|\psi_\alpha(z)|^2 = \frac{|\alpha - z|^2}{|1 - \bar{\alpha}z|^2} = \frac{(\alpha - z)(\bar{\alpha} - \bar{z})}{(1 - \bar{\alpha}z)(1 - \alpha \bar{z})} = \frac{|\alpha|^2 - \alpha \bar{z} - \bar{\alpha}z + 1}{1 - \alpha \bar{z} - \bar{\alpha}z + |\alpha|^2|z|^2} = 1$ (since $|z|^2=1$). *Proof:* Algebraic calculation on the boundary circle $\partial \mathbb{D}$.
<2>3. $\psi_\alpha(\psi_\alpha(z)) = \frac{\alpha - \frac{\alpha-z}{1-\bar{\alpha}z}}{1 - \bar{\alpha}\frac{\alpha-z}{1-\bar{\alpha}z}} = \frac{\alpha(1-\bar{\alpha}z) - (\alpha-z)}{(1-\bar{\alpha}z) - \bar{\alpha}(\alpha-z)} = \frac{z(1-|\alpha|^2)}{1-|\alpha|^2} = z$.
*Proof:* $\psi_\alpha$ is its own inverse (an involution), hence a bijection of $\mathbb{D}$ onto $\mathbb{D}$.
<2>4. Q.E.D.

<1>2. **The Jacobian determinant of a holomorphic mapping $\psi(z) = u(x,y) + i v(x,y)$ is $|\psi'(z)|^2$.** <2>1. By the Cauchy-Riemann equations $u_x = v_y$ and $u_y = -v_x$, the Jacobian determinant is $J_\psi(x,y) = u_x v_y - u_y v_x = u_x^2 + v_x^2 = |u_x + i v_x|^2 = |\psi'(z)|^2$.
*Proof:* Standard real-differentiability computation for holomorphic functions.
<2>2. Q.E.D.

<1>3. **Compute $\frac{1}{\pi}\iint_{\mathbb{D}} |\psi_\alpha'(z)|^2 \,dx\,dy$.** <2>1. By the change of variables formula for 2D integrals under the diffeomorphism $\psi_\alpha: \mathbb{D} \to \mathbb{D}$: $$\iint_{\mathbb{D}} |\psi_\alpha'(z)|^2 \,dx\,dy = \iint_{\mathbb{D}} J_{\psi_\alpha}(x,y) \,dx\,dy = \text{Area}(\psi_\alpha(\mathbb{D})) = \text{Area}(\mathbb{D}) = \pi.$$ *Proof:* Change of variables theorem for planar integrals.
<2>2. Dividing both sides by $\pi$ yields $\frac{1}{\pi}\iint_{\mathbb{D}} |\psi_\alpha'(z)|^2 \,dx\,dy = \frac{\pi}{\pi} = 1$.
*Proof:* Follows from <2>1. <2>3. Q.E.D.

* * *

### Part 2: Area Integral of $|\psi_\alpha'(z)|$

<1>4. **Compute the derivative $\psi_\alpha'(z)$.** <2>1. By the quotient rule: $$\psi_\alpha'(z) = \frac{-(1-\bar{\alpha}z) - (\alpha-z)(-\bar{\alpha})}{(1-\bar{\alpha}z)^2} = \frac{-1 + \bar{\alpha}z + |\alpha|^2 - \bar{\alpha}z}{(1-\bar{\alpha}z)^2} = \frac{-(1-|\alpha|^2)}{(1-\bar{\alpha}z)^2}.$$ *Proof:* Direct differentiation.
<2>2. Therefore, $|\psi_\alpha'(z)| = \frac{1-|\alpha|^2}{|1-\bar{\alpha}z|^2}$.
*Proof:* Absolute value of <2>1. <2>3. Q.E.D.

<1>5. **Evaluate the integral in polar coordinates.** <2>1. Without loss of generality, assume $\alpha \neq 0$ (if $\alpha = 0$, $|\psi_0'(z)| = 1$, and $\frac{1}{\pi}\iint_{\mathbb{D}} 1\,dx\,dy = 1 = \lim_{\alpha\to 0} \frac{1-|\alpha|^2}{|\alpha|^2}\log\frac{1}{1-|\alpha|^2}$). Let $\alpha = a e^{i\phi}$ with $a = |\alpha| \in (0, 1)$.
By rotational invariance of the disk, substituting $z \mapsto e^{i\phi} z$ allows us to assume $\alpha = a \in (0,1)$ is real: $$\iint_{\mathbb{D}} \frac{1-a^2}{|1-a z|^2} \,dx\,dy = (1-a^2) \int_0^1 r \left( \int_0^{2\pi} \frac{d\theta}{|1 - a r e^{i\theta}|^2} \right) dr.$$ *Proof:* Polar coordinates $z = r e^{i\theta}$ and rotation invariance of the area element $dx\,dy = r\,dr\,d\theta$.
<2>2. For any $c \in (0, 1)$, $\frac{1}{2\pi}\int_0^{2\pi} \frac{d\theta}{|1 - c e^{i\theta}|^2} = \frac{1}{1-c^2}$.
*Proof:* Write $\frac{1}{1-c e^{i\theta}} = \sum_{k=0}^\infty c^k e^{ik\theta}$.
By Parseval's identity / orthogonality of $\{e^{ik\theta}\}_{k\in\mathbb{Z}}$, $\frac{1}{2\pi}\int_0^{2\pi} \left|\sum_{k=0}^\infty c^k e^{ik\theta}\right|^2 d\theta = \sum_{k=0}^\infty (c^k)^2 = \sum_{k=0}^\infty c^{2k} = \frac{1}{1-c^2}$.
<2>3. Setting $c = ar$ with $0 \leq ar < 1$, we get $\int_0^{2\pi} \frac{d\theta}{|1 - a r e^{i\theta}|^2} = \frac{2\pi}{1 - a^2 r^2}$.
*Proof:* Applied <2>2 with $c = ar$.
<2>4. Integrate with respect to $r$: $$\frac{1}{\pi}\iint_{\mathbb{D}} |\psi_a'(z)| \,dx\,dy = \frac{1-a^2}{\pi} \int_0^1 r \cdot \frac{2\pi}{1-a^2 r^2} \,dr = (1-a^2) \int_0^1 \frac{2r}{1-a^2 r^2} \,dr.$$ *Proof:* Substitution of <2>3 into <2>1. <2>5. Using the substitution $u = 1 - a^2 r^2$, $du = -2a^2 r\,dr$: $$\int_0^1 \frac{2r}{1-a^2 r^2} \,dr = \int_{1-a^2}^1 \frac{du}{a^2 u} = \frac{1}{a^2} [\log u]_{1-a^2}^1 = \frac{1}{a^2} \log\left(\frac{1}{1-a^2}\right).$$ *Proof:* Standard calculus integration.
<2>6. Multiplying by $(1-a^2)$ gives: $$\frac{1}{\pi}\iint_{\mathbb{D}} |\psi_\alpha'(z)| \,dx\,dy = \frac{1-a^2}{a^2}\log\left(\frac{1}{1-a^2}\right) = \frac{1-|\alpha|^2}{|\alpha|^2}\log\left(\frac{1}{1-|\alpha|^2}\right).$$ *Proof:* Combines <2>4 and <2>5. <2>7. Q.E.D.

* * *

### Part 3: Conformal Map $f(z) = -\frac{1}{2}\left(z + \frac{1}{z}\right)$ from $\mathbb{D}^+$ to $\mathbb{H}$

<1>6. **$f$ is holomorphic on $\mathbb{D}^+$ with non-vanishing derivative.** <2>1. $f(z) = -\frac{1}{2}(z + z^{-1})$ is rational with its only pole at $z=0 \notin \mathbb{D}^+$, hence holomorphic on $\mathbb{D}^+$.
*Proof:* $0 \notin \mathbb{D}^+$ since points in $\mathbb{D}^+$ have $y = \text{Im}(z) > 0$.
<2>2. $f'(z) = -\frac{1}{2}\left(1 - \frac{1}{z^2}\right) = \frac{1 - z^2}{2z^2}$.
*Proof:* Direct differentiation.
<2>3. $f'(z) = 0 \iff z^2 = 1 \iff z = \pm 1 \notin \mathbb{D}^+$.
Thus $f'(z) \neq 0$ for all $z \in \mathbb{D}^+$.
*Proof:* Points $\pm 1$ have $y=0$ and $|z|=1$, so they lie on the boundary, not in $\mathbb{D}^+$.
<2>4. Q.E.D.

<1>7. **$f$ maps $\mathbb{D}^+$ into the upper half-plane $\mathbb{H}$.** <2>1. For $z = r e^{i\theta} \in \mathbb{D}^+$ (so $0 < r < 1$ and $0 < \theta < \pi$): $$f(z) = -\frac{1}{2}\left(r e^{i\theta} + \frac{1}{r} e^{-i\theta}\right) = -\frac{1}{2}\left( r(\cos\theta + i\sin\theta) + \frac{1}{r}(\cos\theta - i\sin\theta) \right).$$ *Proof:* Euler's formula.
<2>2. The imaginary part is $\text{Im}(f(z)) = -\frac{1}{2}\left(r - \frac{1}{r}\right)\sin\theta = \frac{1}{2}\left(\frac{1}{r} - r\right)\sin\theta$.
*Proof:* Extracting the imaginary component.
<2>3. Since $0 < r < 1$, $\frac{1}{r} - r > 0$; and since $0 < \theta < \pi$, $\sin\theta > 0$.
Thus $\text{Im}(f(z)) > 0$, so $f(\mathbb{D}^+) \subseteq \mathbb{H}$.
*Proof:* Product of two strictly positive real numbers is strictly positive.
<2>4. Q.E.D.

<1>8. **$f: \mathbb{D}^+ \to \mathbb{H}$ is bijective.** <2>1. Let $w \in \mathbb{H}$ be given.
We solve $f(z) = w \iff -\frac{1}{2}(z + 1/z) = w \iff z^2 + 2w z + 1 = 0$.
*Proof:* Algebraic rearrangement.
<2>2. The two roots of this quadratic equation are $z_{1,2} = -w \pm \sqrt{w^2 - 1}$.
The product of the roots is $z_1 z_2 = 1$.
*Proof:* Vieta's formulas for $z^2 + 2wz + 1 = 0$.
<2>3. Since $w \in \mathbb{H}$, $w \notin [-1, 1]$, so $w^2 - 1 \neq 0$ and the two roots are distinct and neither has modulus $1$ (if $|z|=1$ with $z=e^{i\theta}$, then $-\frac{1}{2}(e^{i\theta}+e^{-i\theta}) = -\cos\theta \in [-1,1] \subset \mathbb{R}$, which has imaginary part $0$). *Proof:* Modulus 1 points map to the real interval $[-1, 1]$.
<2>4. Since $|z_1||z_2| = 1$ and $|z_1| \neq 1$, exactly one root has modulus strictly less than $1$ (say $|z_1| < 1$). *Proof:* If $|z_1| < 1$, then $|z_2| = 1/|z_1| > 1$.
<2>5. From <1>7.<2>2, $\text{Im}(w) = \frac{1}{2}(\frac{1}{|z_1|} - |z_1|)\sin(\arg z_1)$.
Since $\text{Im}(w) > 0$ and $\frac{1}{|z_1|} - |z_1| > 0$, we must have $\sin(\arg z_1) > 0$, which means $\arg(z_1) \in (0, \pi)$, so $z_1 \in \mathbb{D}^+$.
*Proof:* Sign of $\sin(\arg z_1)$ must match the sign of $\text{Im}(w)$.
<2>6. Thus, for each $w \in \mathbb{H}$, there is a unique $z \in \mathbb{D}^+$ such that $f(z) = w$.
*Proof:* Exactly one of the two quadratic roots lies in $\mathbb{D}^+$.
<2>7. Q.E.D.

<1>9. **Conclusion: $f$ is a conformal map (biholomorphism) from $\mathbb{D}^+$ to $\mathbb{H}$.** <2>1. By <1>6 and <1>8, $f$ is a holomorphic bijection from $\mathbb{D}^+$ to $\mathbb{H}$, hence a biholomorphism / conformal map.
*Proof:* A bijective holomorphic function between open domains in $\mathbb{C}$ has a holomorphic inverse.
<2>2. Q.E.D.
:::
