---
schema: qual/card@1
id: E-SS3.EX-18
kind: problem
title: The Cauchy integral formula via homotopy
classification:
  areas:
    - complex-analysis
  topics: [Cauchy Integral Formula, Homotopy]
relations: []
review: draft
audit:
  - event: solution-written
    by: claude
    date: 2026-11-20
    note: >-
      Converted from prose to numbered steps under #2, six of them, each with its proof, and the
      citation moved to chapter, section and exercise number: Stein--Shakarchi, *Complex Analysis*,
      Chapter 3 §8 Exercise 18. The step that the prose compressed is the vanishing integral: the
      estimate $\abs{\int_{C_r}h}\le M\cdot2\pi r$ is written out with $M$ a bound for $h$ near $z$,
      and the fact that the integral is independent of $r$ is what lets it be $0$. The winding-number
      computation is a step of its own with the parametrization given. Not checked: no certificate,
      and homotopy invariance of contour integrals is cited rather than proved here.
  - event: solution-written
    by: gpt-5.6-sol
    date: 2026-09-11
---

::: {.exercise}
Give another proof of the Cauchy integral formula

$$
f(z) = \frac{1}{2\pi i}\int_{C} \frac{f(\zeta)}{\zeta - z}\,d\zeta
$$
using homotopy of curves.

[Hint: Deform the circle $C$ to a small circle centered at $z$, and note that the quotient $(f(\zeta) - f(z))/(\zeta - z)$ is bounded.]
:::

::: {.solution}
This is Stein--Shakarchi, *Complex Analysis*, Chapter 3 §8 Exercise 18, whose argument is reproduced in steps below and checked against the Cauchy integral formula it proves. Throughout $C$ is a positively oriented circle and $z$ lies in its interior.

::: pf

::: {.pf-step #split}
For $\zeta\ne z$, $\dfrac{f(\zeta)}{\zeta-z}=\dfrac{f(\zeta)-f(z)}{\zeta-z}+\dfrac{f(z)}{\zeta-z}$.

::: pf-proof
Subtract and add $f(z)$ in the numerator: $f(\zeta)=f(\zeta)-f(z)+f(z)$, and divide by $\zeta-z$.
:::

:::

::: {.pf-step #h}
The function $h(\zeta)=\dfrac{f(\zeta)-f(z)}{\zeta-z}$ for $\zeta\ne z$ and $h(z)=f'(z)$ is holomorphic on a neighbourhood of the region swept out by a homotopy shrinking $C$ to a small positively oriented circle $C_r$ about $z$.

::: pf-proof
The difference quotient of a holomorphic $f$ extends holomorphically across $z$ by its derivative, which is the definition of the removable singularity at $z$; outside $z$ the function is a quotient of holomorphic functions with nonvanishing denominator. The region swept out by the shrinking homotopy is a compact annulus-like neighbourhood of $z$ inside the disc bounded by $C$, on which $h$ is holomorphic.
:::

:::

::: {.pf-step #invariance}
$\displaystyle\int_Ch(\zeta)\,d\zeta=\int_{C_r}h(\zeta)\,d\zeta$ for $0<r$ small.

::: pf-proof
This is homotopy invariance of contour integrals of holomorphic functions: two closed curves that are homotopic through closed curves inside the domain of a holomorphic function have equal integrals, and a radial shrinking of $C$ to $C_r$ is such a homotopy inside the region of step [](#h){.pf-ref}.
:::

:::

::: {.pf-step #vanish}
$\displaystyle\int_C\frac{f(\zeta)-f(z)}{\zeta-z}\,d\zeta=0$.

::: pf-proof
By step [](#invariance){.pf-ref} the integral equals $\int_{C_r}h\,d\zeta$. The function $h$ is bounded near $z$, say by $M$ on a disc containing all the small circles, so $\abs{\int_{C_r}h\,d\zeta}\le M\cdot2\pi r$ by the standard estimate, and this tends to $0$ as $r\downarrow0$. The integral does not depend on $r$, so it is $0$.
:::

:::

::: {.pf-step #winding}
$\displaystyle\int_C\frac{d\zeta}{\zeta-z}=2\pi i$.

::: pf-proof
This is the winding-number computation for a positively oriented circle with $z$ in its interior: parametrizing $\zeta=z+re^{i\theta}$, $0\le\theta\le2\pi$, gives $\int_C d\zeta/(\zeta-z)=\int_0^{2\pi}i\,d\theta=2\pi i$, and the value is unchanged by deforming $C$ inside $\CC\setminus\{z\}$.
:::

:::

::: {.pf-step}
The Cauchy integral formula holds: $\displaystyle\int_C\frac{f(\zeta)}{\zeta-z}\,d\zeta=2\pi i\,f(z)$.

::: pf-proof
Integrate the identity of step [](#split){.pf-ref} over $C$: the first term vanishes by step [](#vanish){.pf-ref} and the second is $f(z)\int_Cd\zeta/(\zeta-z)=2\pi i f(z)$ by step [](#winding){.pf-ref}. This is the second proof of the Cauchy integral formula that the exercise asks for.
:::

:::

:::


:::
