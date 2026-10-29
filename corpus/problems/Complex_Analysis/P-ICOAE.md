---
schema: qual/card@1
id: P-ICOAE
kind: problem
title: $\int_0^{2\pi}\frac{d\theta}{(a+b\cos\theta)^2}$ for $a>b>0$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Contour Integration
  - Integrals
  - Trigonometry
  - Poles
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: {.problem}
Suppose $a>b>0$ and calculate
$$
\int_0^{2\pi} {1 \over (a+b\cos(\theta))^2} \,d\theta
.$$
:::

::: {.solution}
Let $z_{1,2} = \dfrac{-a \pm \sqrt{a^2 - b^2}}{b}$ be the roots of $bz^2+2az+b$.

::: pf

::: {.pf-step #contour}
$\displaystyle\int_0^{2\pi} \frac{d\theta}{(a + b\cos\theta)^2} = \oint_{\abs z=1} g(z)\,dz$, where $g(z) = \dfrac{4z}{i b^2(z-z_1)^2(z-z_2)^2}$.

::: pf-proof
Substitute $z = e^{i\theta}$, so $d\theta = \frac{dz}{iz}$ and $a + b\cos\theta = \frac{bz^2+2az+b}{2z}$. Then the integrand becomes $\frac{4z^2}{(bz^2+2az+b)^2}\cdot\frac{1}{iz}$.
:::

:::

::: {.pf-step #roots}
$\abs{z_1}<1<\abs{z_2}$.

::: pf-proof
$z_1z_2=1$ and $z_2 < -a/b < -1$.
:::

:::

::: {.pf-step #residue}
$\operatorname{Res}(g, z_1) = \dfrac{a}{i(a^2 - b^2)^{3/2}}$.

::: pf-proof
At the double pole $z_1$,
$$
\operatorname{Res}(g,z_1) = \frac{4}{ib^2}\,\frac{d}{dz}\frac{z}{(z-z_2)^2}\bigg|_{z=z_1} = \frac{4}{ib^2}\,\frac{-(z_1+z_2)}{(z_1-z_2)^3}.
$$
With $z_1+z_2=-2a/b$ and $z_1-z_2 = 2\sqrt{a^2-b^2}/b$, this equals $\frac{4}{ib^2}\cdot\frac{2a/b}{8(a^2-b^2)^{3/2}/b^3} = \frac{a}{i(a^2-b^2)^{3/2}}$.
:::

:::

::: pf-step
$\displaystyle\int_0^{2\pi} \frac{d\theta}{(a + b\cos\theta)^2} = \boxed{\frac{2\pi a}{(a^2 - b^2)^{3/2}}}$.

::: pf-proof
By steps [](#contour){.pf-ref} and [](#roots){.pf-ref}, the only pole of $g$ inside the unit circle is $z_1$. The residue theorem and step [](#residue){.pf-ref} give $2\pi i\cdot\frac{a}{i(a^2-b^2)^{3/2}}$.
:::

:::

:::

:::
