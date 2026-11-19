---
schema: qual/card@1
id: P-FBY23
kind: problem
title: 'Cauchy integral formula for $\oint_\gamma z^2/(z-i)\,dz$ on a circle about $i$'
classification:
  areas:
    - prelim
  topics:
    - Cauchy Integral Formula
    - Contour Integration
relations: []
review: draft
audit:
  - event: solution-written
    by: gpt-5.6-sol
    date: 2026-09-10
  - event: solution-written
    by: claude
    date: 2026-11-18
    note: >-
      Restructured as a Lamport proof of the card's own two-part solution, whose value -2 pi i and
      whose parametrisation are correct: with z = i + Re^{it} the integrand reduces to i(i +
      Re^{it})^2, and the expansion into real and imaginary parts was checked term by term.
      Repaired the part labels in the problem block to STYLE-05's '(a)' and '(b)', the printed
      text otherwise unchanged; no printed source line was changed. Not claimed: a retained
      solution set; the collection's provenance is the examination paper only.
---

::: {.problem}
(a) State the Cauchy integral formula and use it to evaluate the complex line integral: $\oint_\gamma z^2/(z-i)\, dz$, where $\gamma$ is a circle centered at $i$ and oriented counterclockwise.
(b) Use a parametrization of the path $\gamma$ to express the line integral explicitly in terms of real integrals, with limits of integration.
[You do not have to evaluate these real integrals.]
:::

::: {.solution}
The collection's `provenance` is the Fall 2002 examination paper `assets/attachments/grad_prelim_Fall02.pdf` and no solutions sheet accompanies it, so the argument below is the card's own. Throughout $\gamma$ is a circle about $i$ of radius $R > 0$, oriented counterclockwise, and $f(z) = z^{2}$.

::: pf

::: {.pf-step #cif}
(a) Cauchy integral formula: if $f$ is holomorphic on and inside a positively oriented simple closed contour $\gamma$, and $a$ lies inside $\gamma$, then $\oint_{\gamma}\frac{f(z)}{z-a}\,dz = 2\pi i\,f(a)$.

::: pf-proof
This is the statement asked for in part (a); it applies to $f$ holomorphic on a domain containing $\gamma$ and its interior, and to a point $a$ inside the contour.

:::

:::

::: {.pf-step #value}
(a) $\oint_{\gamma}\frac{z^{2}}{z-i}\,dz = \boxed{-2\pi i}$.

::: pf-proof
$f(z) = z^{2}$ is entire, so it is holomorphic on and inside $\gamma$; the centre $i$ lies inside the circle $\gamma$ about $i$. Step [](#cif){.pf-ref} then gives $\oint_{\gamma}\frac{z^{2}}{z-i}dz = 2\pi i\,f(i) = 2\pi i\cdot i^{2} = -2\pi i$. The value does not depend on $R$.

:::

:::

::: {.pf-step #parametrise}
(b) With $z(t) = i + Re^{it}$, $0 \le t \le 2\pi$, one has $dz = iRe^{it}dt$ and $z - i = Re^{it}$, so $\oint_{\gamma}\frac{z^{2}}{z-i}\,dz = \int_{0}^{2\pi} i\bigl(i + Re^{it}\bigr)^{2}dt$.

::: pf-proof
Substituting the parametrisation into the integrand gives $\frac{z(t)^{2}}{z(t)-i}\,z'(t) = \frac{(i+Re^{it})^{2}}{Re^{it}}\cdot iRe^{it} = i\bigl(i+Re^{it}\bigr)^{2}$; a continuous integrand on $[0,2\pi]$ is Riemann integrable, and the parametrisation traverses $\gamma$ once counterclockwise as $t$ runs from $0$ to $2\pi$.

:::

:::

::: {.pf-step #realform}
(b) Writing $e^{it} = \cos t + i\sin t$, the integrand's real and imaginary parts are $-2R\cos t\,(1 + R\sin t)$ and $R^{2}\cos^{2}t - (1+R\sin t)^{2}$, so the integral is $\int_{0}^{2\pi}\bigl[-2R\cos t\,(1+R\sin t) + i\bigl(R^{2}\cos^{2}t - (1+R\sin t)^{2}\bigr)\bigr]dt$.

::: pf-proof
Expand $i + Re^{it} = R\cos t + i(1 + R\sin t)$, so $\bigl(i+Re^{it}\bigr)^{2} = R^{2}\cos^{2}t - (1+R\sin t)^{2} + 2iR\cos t\,(1+R\sin t)$; multiplying by $i$ interchanges real and imaginary parts with a sign, giving the two displayed functions of $t$.

:::

:::

::: pf-step
The two parts are answered: (a) $\oint_{\gamma}\frac{z^{2}}{z-i}dz = -2\pi i$, and (b) $\int_{0}^{2\pi}\Bigl[-2R\cos t\,(1+R\sin t) + i\bigl(R^{2}\cos^{2}t - (1+R\sin t)^{2}\bigr)\Bigr]dt$, which is the same integral expressed as real integrals with limits $0$ and $2\pi$.

::: pf-proof
Step [](#value){.pf-ref} is part (a); steps [](#parametrise){.pf-ref} and [](#realform){.pf-ref} are part (b), which asks only for the expression and its limits, not for its evaluation. Separating the two real integrals gives $\int_{0}^{2\pi}-2R\cos t(1+R\sin t)\,dt + i\int_{0}^{2\pi}\bigl(R^{2}\cos^{2}t - (1+R\sin t)^{2}\bigr)dt$.

:::

:::

:::
:::
