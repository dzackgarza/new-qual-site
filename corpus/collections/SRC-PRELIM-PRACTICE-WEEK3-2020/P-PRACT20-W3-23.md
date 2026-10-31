---
schema: qual/card@1
id: P-PRACT20-W3-23
kind: problem
title: The Gaussian integral via polar coordinates
classification:
  areas:
  - prelim
  topics:
  - Multiple Integrals
  - Polar Coordinates
relations: []
review: draft
---

::: {.problem}
Let $D = \{ (x, y) \in \RR^{2} : x \geq 0, y \geq 0 \}$.

(a) Calculate $\displaystyle\iint_{D} e^{-(x^{2} + y^{2})}\, dx\, dy$.

(b) Use (a) to evaluate the Gaussian integral $\displaystyle\int_{-\infty}^{\infty} e^{-x^{2}}\, dx$.
:::

::: {.solution}
In polar coordinates,

$$
\iint_De^{-(x^2+y^2)}\,dx\,dy=\int_0^{\pi/2}\int_0^\infty e^{-r^2}r\,dr\,d\theta=\frac{\pi}{2}\left(-\frac12e^{-r^2}\evalfrom_{r=0}^{r\to\infty}\right)=\frac{\pi}{4}.
$$

The integrand is positive, so by Tonelli's theorem

$$
\iint_De^{-(x^2+y^2)}\,dx\,dy=\left(\int_0^\infty e^{-x^2}\,dx\right)\left(\int_0^\infty e^{-y^2}\,dy\right)=\left(\int_0^\infty e^{-x^2}\,dx\right)^2,
$$

so

$$
\int_0^\infty e^{-x^2}\,dx=\frac{\sqrt\pi}{2}\quad\text{and, since the integrand is even,}\quad\int_{-\infty}^{\infty}e^{-x^2}\,dx=\sqrt\pi.
$$
:::
