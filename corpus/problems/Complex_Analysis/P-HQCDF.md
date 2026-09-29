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

::: {.problem}
Let $a>0$ and calculate
\[
\int_0^\infty {x^2 \over (x^2 + a^2)^2} \, dx
.\]
:::

::: {.solution}
::: pf

::: {.pf-step #even-integrand}
The integrand is even, so $\int_0^\infty \frac{x^2}{(x^2 + a^2)^2}\,dx = \frac{1}{2}\int_{-\infty}^{\infty} \frac{x^2}{(x^2 + a^2)^2}\,dx$.

::: pf-proof
evenness.
:::

:::

::: pf-step
Consider $f(z) = \frac{z^2}{(z^2 + a^2)^2} = \frac{z^2}{(z - ia)^2 (z + ia)^2}$.

::: pf-proof
definition.
:::

:::

::: pf-step
$f$ has a double pole at $z = ia$ (in the upper half-plane) and a double pole at $z = -ia$ (in the lower half-plane).

::: pf-proof
factor the denominator.
:::

:::

::: {.pf-step #arc-vanishes}
Integrate over a semicircular contour in the upper half-plane; the integral over the arc tends to $0$ as the radius $\to \infty$.

::: pf-proof
$|f(z)| \le C/R^2$ on the arc of radius $R$, and the arc length is $\pi R$, so the arc integral is $O(1/R) \to 0$.
:::

:::

::: {.pf-step #residue-at-ia}
$\operatorname{Res}(f, ia) = \frac{1}{4ia}$.

::: pf-proof
computing the residue at the double pole $z = ia$: $\operatorname{Res} = \frac{d}{dz}\left[\frac{z^2}{(z + ia)^2}\right]_{z = ia} = \frac{1}{4ia}$.
:::

:::

::: {.pf-step #line-integral-value}
By the residue theorem, $\int_{-\infty}^{\infty} f(x)\,dx = 2\pi i \cdot \frac{1}{4ia} = \frac{\pi}{2a}$.

::: pf-proof
Steps [](#arc-vanishes){.pf-ref} and [](#residue-at-ia){.pf-ref}.
:::

:::

::: {.pf-step #final-value}
Hence $\int_0^\infty \frac{x^2}{(x^2 + a^2)^2}\,dx = \frac{1}{2} \cdot \frac{\pi}{2a} = \frac{\pi}{4a}$.

::: pf-proof
Steps [](#even-integrand){.pf-ref} and [](#line-integral-value){.pf-ref}.
:::

:::

::: pf-qed
Step [](#final-value){.pf-ref}.
:::

:::

