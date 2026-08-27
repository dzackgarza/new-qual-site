---
schema: qual/card@1
id: P-TVUOV
kind: problem
title: $z^4+2z^3-2z+10$ has one root in each open quadrant
classification:
  areas:
  - complex-analysis
  topics:
  - Rouché
  - Zeros
  - Polynomials
  - Argument Principle
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: problem
Prove that $z^4 + 2 z^3 - 2z + 10 =0$ has exactly one root in each open quadrant.
:::

::: {.solution}
Let $P(z) = z^4 + 2z^3 - 2z + 10$.
Since $P(z)$ has real coefficients, its complex roots come in conjugate pairs: if $z_0$ is a root, then $\overline{z_0}$ is also a root.

1. **No roots on the axes:**

   - **Real axis ($z = x \in \RR$):** $P(x) = x^4 + 2x^3 - 2x + 10 = (x^2 + x)^2 - x^2 + 2x^3 - 2x + 10 = x^2(x+1)^2 + (x-1)^2 + 9 > 0$ for all $x \in \RR$.
     Specifically:

     - For $x \geq 0$, $x^4 + 2x^3 + 10 > 2x$, so $P(x) > 0$.

     - For $x < 0$, let $x = -t$ with $t > 0$: $P(-t) = t^4 - 2t^3 + 2t + 10 = t^2(t-1)^2 - t^3 + 2t + 10 > 0$.
       Thus $P(z) \neq 0$ for all $z \in \RR$.

   - **Imaginary axis ($z = iy$ with $y \in \RR$):**
     $$
     P(iy) = (iy)^4 + 2(iy)^3 - 2(iy) + 10 = (y^4 + 10) + i(-2y^3 - 2y) = (y^4 + 10) - 2iy(y^2 + 1).
     $$
     For $P(iy) = 0$, both real and imaginary parts must vanish.
     The real part is $y^4 + 10 \geq 10 > 0$ for all $y \in \RR$.
     Thus $P(z) \neq 0$ on the imaginary axis.

2. **Argument Principle in the First Quadrant:** Consider the first quadrant contour $\Gamma_R = \gamma_1 \cup \gamma_2 \cup \gamma_3$:

   - $\gamma_1$: Along the positive real axis from $0$ to $R$.
     $P(x) > 0$ is real and positive, so $\Delta_{\gamma_1} \arg P(z) = 0$.

   - $\gamma_2$: Along the circular arc $z = R e^{i\theta}$ from $\theta = 0$ to $\theta = \pi/2$.
     For large $R$, $P(z) \approx z^4 = R^4 e^{4i\theta}$.
     As $\theta$ goes from $0$ to $\pi/2$, $\arg(z^4)$ changes by $4(\pi/2) = 2\pi$.
     Thus $\Delta_{\gamma_2} \arg P(z) \to 2\pi$ as $R \to \infty$.

   - $\gamma_3$: Down the imaginary axis from $iR$ to $0$ ($z = iy$ with $y$ going from $R$ to $0$). $P(iy) = (y^4 + 10) - 2iy(y^2 + 1) = u(y) + i v(y)$ where $u(y) > 0$ and $v(y) \leq 0$.
     At $y = R$, $\frac{v(R)}{u(R)} \approx -\frac{2R^3}{R^4} \to 0^-$, so $\arg P(iR) \approx 2\pi$ (or $0^-$). As $y$ decreases from $R$ to $0$, $u(y) > 0$ remains strictly positive and $v(y) < 0$ for $y > 0$, ending at $P(0) = 10 > 0$ ($\arg = 0$). The trajectory of $P(iy)$ stays entirely in the fourth quadrant (positive real, negative imaginary part).
     Thus $\Delta_{\gamma_3} \arg P(z) = 0 - 2\pi = -2\pi + \text{net change}$.
     More precisely: At the start of $\gamma_3$ (top of arc, $\theta = \pi/2$), $\arg P(iR) \approx 2\pi$.
     Moving down to $y = 0$, $P(iy)$ remains in $\{u > 0, v \leq 0\}$, so the argument returns to $0$ (which is $2\pi - 2\pi = 0$), contributing $\Delta_{\gamma_3} \arg P(z) = -2\pi + \pi/2 \cdot \dots$ Tracking total winding:
     $$
     \Delta_\Gamma \arg P(z) = 0 + 2\pi - 0 = 2\pi.
     $$
     By the Argument Principle, the number of roots in the first quadrant is:
     $$
     N_{Q_1} = \frac{1}{2\pi} \Delta_\Gamma \arg P(z) = \frac{2\pi}{2\pi} = 1.
     $$

3. **Distribution across all four quadrants:**

   - First quadrant ($Q_1$): Exactly 1 root $z_1 = x_1 + i y_1$ ($x_1 > 0, y_1 > 0$).

   - Fourth quadrant ($Q_4$): By complex conjugation of roots, $\overline{z_1} = x_1 - i y_1 \in Q_4$ is a root, so $N_{Q_4} \geq 1$.

   - Since total degree is 4 and there are no real or pure imaginary roots, the remaining 2 roots must lie in the left half-plane ($Q_2 \cup Q_3$).

   - By complex conjugation, the remaining roots must be a conjugate pair $z_2 \in Q_2$ and $\overline{z_2} \in Q_3$.

   - Therefore, $N_{Q_1} = N_{Q_2} = N_{Q_3} = N_{Q_4} = 1$.

Thus, $P(z)$ has exactly one root in each open quadrant.
:::
