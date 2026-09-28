---
schema: qual/card@1
id: P-Y2YJL
kind: problem
title: Fresnel integrals $\int_0^\infty\sin(x^2)\,dx=\int_0^\infty\cos(x^2)\,dx=\frac{\sqrt{2\pi}}{4}$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Contour Integration
  - Integrals
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Show that
\[
\int_{0}^{\infty} \sin \left(x^{2}\right) d x=\int_{0}^{\infty} \cos \left(x^{2}\right) d x=\frac{\sqrt{2 \pi}}{4}
.\]

> Hint: integrate $e^{-x^2}$ over the following contour, using the fact that $\int_{-\infty}^{\infty} e^{-x^{2}} d x=\sqrt{\pi}$:


![Image](../../assets/Complex_Analysis/999_Quals/figures/2020-02-03-13%3A51.png)\
:::

::: {.solution}
For $R>0$, let $\Gamma_R$ be the boundary of the sector with vertices $0$, $R$, and $Re^{i\pi/4}$, traversed along $[0,R]$, then along the arc $\abs{z} = R$ from $R$ to $Re^{i\pi/4}$, then along the ray $\arg z = \pi/4$ back to $0$.

<1>1. $\displaystyle\int_{\Gamma_R} e^{-z^2}\, dz = 0$ for every $R>0$.

::: {.proof}
The function $e^{-z^2}$ is entire, so Cauchy's theorem applies.
:::

<1>2. $\displaystyle\int_0^R e^{-x^2}\, dx \to \frac{\sqrt{\pi}}{2}$ as $R \to \infty$.

::: {.proof}
The integrand is even, so $\int_0^\infty e^{-x^2}\, dx = \frac{1}{2}\int_{-\infty}^\infty e^{-x^2}\, dx = \frac{\sqrt\pi}{2}$.
:::

<1>3. The arc contribution $\int_{\text{arc}} e^{-z^2}\, dz$ tends to $0$ as $R \to \infty$.

::: {.proof}
On the arc $z = Re^{i\theta}$, $0 \leq \theta \leq \pi/4$, one has $\abs{e^{-z^2}} = e^{-R^2 \cos 2\theta}$. Since $\theta\mapsto\cos 2\theta$ is concave on $[0,\pi/4]$, it lies above its chord: $\cos 2\theta \geq 1 - 4\theta/\pi$. Hence
$$\abs{\int_{\text{arc}} e^{-z^2}\,dz} \leq R\int_0^{\pi/4} e^{-R^2(1-4\theta/\pi)}\, d\theta = \frac{\pi}{4R}\bigl(1-e^{-R^2}\bigr) \leq \frac{\pi}{4R}.$$
:::

<1>4. $\displaystyle\int_{\text{ray}} e^{-z^2}\, dz = -e^{i\pi/4}\int_0^R e^{-ir^2}\, dr$.

::: {.proof}
On the ray $z = re^{i\pi/4}$ one has $z^2 = ir^2$ and $dz = e^{i\pi/4}\, dr$. The ray is traversed from $R$ to $0$, so the integral is $\int_R^0 e^{-ir^2} e^{i\pi/4}\, dr$.
:::

<1>5. $\displaystyle\int_0^\infty e^{-ir^2}\, dr = e^{-i\pi/4}\frac{\sqrt\pi}{2}$.

::: {.proof}
By step <1>1, $\int_0^R e^{-x^2}\, dx + \int_{\text{arc}} e^{-z^2}\,dz + \int_{\text{ray}} e^{-z^2}\,dz = 0$. Letting $R\to\infty$ and using steps <1>2--<1>4 gives $\frac{\sqrt\pi}{2} - e^{i\pi/4}\int_0^\infty e^{-ir^2}\, dr = 0$.
:::

<1>6. $\displaystyle\int_0^\infty \cos(r^2)\, dr = \int_0^\infty \sin(r^2)\, dr = \boxed{\frac{\sqrt{2\pi}}{4}}$.

::: {.proof}
Since $e^{-ir^2}=\cos(r^2)-i\sin(r^2)$ and $e^{-i\pi/4} = \frac{\sqrt2}{2}(1 - i)$, step <1>5 gives
$$\int_0^\infty \cos(r^2)\, dr = \Re\int_0^\infty e^{-ir^2}\, dr = \frac{\sqrt2}{2}\cdot\frac{\sqrt\pi}{2},
\qquad
\int_0^\infty \sin(r^2)\, dr = -\Im\int_0^\infty e^{-ir^2}\, dr = \frac{\sqrt2}{2}\cdot\frac{\sqrt\pi}{2}.$$
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 proves both identities.
:::
:::
