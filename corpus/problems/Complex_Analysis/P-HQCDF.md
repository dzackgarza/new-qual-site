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
$$
\int_0^\infty {x^2 \over (x^2 + a^2)^2} \, dx
.$$
:::

::: {.solution}
Let $f(z) = \dfrac{z^2}{(z^2 + a^2)^2} = \dfrac{z^2}{(z - ia)^2 (z + ia)^2}$, which has double poles at $\pm ia$.

::: pf

::: {.pf-step #residue}
$\operatorname{Res}(f, ia) = \dfrac{1}{4ia}$.

::: pf-proof
At the double pole $ia$,
$$
\operatorname{Res}(f,ia) = \frac{d}{dz}\frac{z^2}{(z+ia)^2}\bigg|_{z=ia} = \frac{2iaz}{(z+ia)^3}\bigg|_{z=ia} = \frac{-2a^2}{-8ia^3} = \frac1{4ia}.
$$
:::

:::

::: {.pf-step #line}
$\displaystyle\int_{-\infty}^{\infty} f(x)\,dx = \frac{\pi}{2a}$.

::: pf-proof
Integrate $f$ over the boundary of the upper half-disk of radius $R>a$. The only enclosed pole is $ia$, so by step [](#residue){.pf-ref} the contour integral is $2\pi i\cdot\frac1{4ia} = \frac{\pi}{2a}$. On the arc $\abs{f(z)}\le R^2/(R^2-a^2)^2$, so the arc integral is at most $\pi R^3/(R^2-a^2)^2\to 0$ as $R\to\infty$.
:::

:::

::: pf-step
$\displaystyle\int_0^\infty \frac{x^2}{(x^2 + a^2)^2}\,dx = \boxed{\frac{\pi}{4a}}$.

::: pf-proof
The integrand is even, so the integral is half of the one in step [](#line){.pf-ref}.
:::

:::

:::

:::
