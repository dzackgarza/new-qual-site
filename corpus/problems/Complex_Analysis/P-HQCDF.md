---
schema: qual/card@1
id: P-HQCDF
kind: problem
title: $\int_0^\infty\frac{x^2}{(x^2+a^2)^2}\,dx$ for $a>0$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Contour Integration
  - Integrals
  - Poles
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

:::{.problem}
Let $a>0$ and calculate
\[
\int_0^\infty {x^2 \over (x^2 + a^2)^2} \, dx
.\]
:::

::: {.solution}
<1>1. The integrand is even, so $\int_0^\infty \frac{x^2}{(x^2 + a^2)^2}\,dx = \frac{1}{2}\int_{-\infty}^{\infty} \frac{x^2}{(x^2 + a^2)^2}\,dx$.
::: {.proof}
evenness.
:::

<1>2. Consider $f(z) = \frac{z^2}{(z^2 + a^2)^2} = \frac{z^2}{(z - ia)^2 (z + ia)^2}$.
::: {.proof}
definition.
:::

<1>3. $f$ has a double pole at $z = ia$ (in the upper half-plane) and a double pole at $z = -ia$ (in the lower half-plane).
::: {.proof}
factor the denominator.
:::

<1>4. Integrate over a semicircular contour in the upper half-plane; the integral over the arc tends to $0$ as the radius $\to \infty$.
::: {.proof}
$|f(z)| \le C/R^2$ on the arc of radius $R$, and the arc length is $\pi R$, so the arc integral is $O(1/R) \to 0$.
:::

<1>5. $\operatorname{Res}(f, ia) = \frac{1}{4ia}$.
::: {.proof}
computing the residue at the double pole $z = ia$: $\operatorname{Res} = \frac{d}{dz}\left[\frac{z^2}{(z + ia)^2}\right]_{z = ia} = \frac{1}{4ia}$.
:::

<1>6. By the residue theorem, $\int_{-\infty}^{\infty} f(x)\,dx = 2\pi i \cdot \frac{1}{4ia} = \frac{\pi}{2a}$.
::: {.proof}
<1>4 and <1>5.
:::

<1>7. Hence $\int_0^\infty \frac{x^2}{(x^2 + a^2)^2}\,dx = \frac{1}{2} \cdot \frac{\pi}{2a} = \frac{\pi}{4a}$.
::: {.proof}
<1>1 and <1>6.
:::

<1>8. Q.E.D.
::: {.proof}
<1>7.
:::
:::

