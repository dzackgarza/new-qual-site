---
schema: qual/card@1
id: E-Z66NC
kind: problem
title: The integral of $1/(x\sqrt{x^2-1})$ over $[1,\infty)$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Contour Integration
  - Integrals
  - Complex Logarithm
relations: []
review: draft
---

::: {.exercise}
Show that
$$
\int_{1}^{\infty} \frac{dx}{x \sqrt{x^{2}-1}} = \frac{\pi}{2}.
$$
:::

::: {.solution}
On $\CC\setminus[-1,1]$ let $s(z) \coloneqq z\sqrt{1-1/z^2}$ with the principal square root; $1-1/z^2$ is a nonpositive real exactly when $z\in[-1,1]$, so $s$ is holomorphic there and $s(z)^2 = z^2-1$.

::: pf

::: {.pf-step #substitute}
$\displaystyle\int_1^\infty \frac{dx}{x\sqrt{x^2-1}} = \frac12\int_{-1}^1\frac{dt}{\sqrt{1-t^2}}$.

::: pf-proof
Substitute $x = 1/t$, so $dx = -dt/t^2$ and $x\sqrt{x^2-1} = \sqrt{1-t^2}/t^2$; this gives $\int_0^1 dt/\sqrt{1-t^2}$, and the integrand is even.
:::

:::

::: {.pf-step #banks}
For $-1<x<1$, $s(x+i0) = i\sqrt{1-x^2}$ and $s(x-i0) = -i\sqrt{1-x^2}$.

::: pf-proof
For $z = x\pm i\varepsilon$ with $x\neq0$, $1 - 1/z^2 = (1-1/x^2) \pm 2i\varepsilon/x^3 + O(\varepsilon^2)$, a point near the negative real axis on the side of sign $\pm\operatorname{sgn}x$.
So $\sqrt{1-1/z^2}\to \pm\operatorname{sgn}(x)\, i\sqrt{1/x^2-1}$, and multiplying by $x$ gives $\pm i\sqrt{1-x^2}$; the value at $x=0$ follows by continuity of the bank limits.
:::

:::

::: {.pf-step #circle}
For $R>1$, $\displaystyle\oint_{\abs{z}=R}\frac{dz}{s(z)} = 2\pi i$.

::: pf-proof
For $\abs{z}>1$, $\frac{1}{s(z)} = \frac1z\qty(1-z^{-2})^{-1/2} = \frac1z + O(z^{-3})$, whose Laurent coefficient of $z^{-1}$ is $1$.
:::

:::

::: {.pf-step #dogbone}
$\displaystyle 2i\int_{-1}^1\frac{dt}{\sqrt{1-t^2}} = 2\pi i$.

::: pf-proof
By Cauchy's theorem, the circle in step [](#circle){.pf-ref} may be deformed to the positively oriented boundary of an $\varepsilon$-neighbourhood of $[-1,1]$: the lower bank from $-1$ to $1$, the upper bank from $1$ to $-1$, and two circles of radius $\varepsilon$ about $\pm1$.
Near $\pm1$, $\abs{1/s(z)} = O(\abs{z\mp1}^{-1/2})$, so the small circles contribute $O(\varepsilon^{1/2})\to0$.
By step [](#banks){.pf-ref}, the banks contribute
$$
\int_{-1}^1\frac{dt}{-i\sqrt{1-t^2}} + \int_1^{-1}\frac{dt}{i\sqrt{1-t^2}} = 2i\int_{-1}^1\frac{dt}{\sqrt{1-t^2}}.
$$
:::

:::

::: pf-step
$\displaystyle\int_1^\infty\frac{dx}{x\sqrt{x^2-1}} = \boxed{\frac\pi2}$.

::: pf-proof
Step [](#dogbone){.pf-ref} gives $\int_{-1}^1 dt/\sqrt{1-t^2} = \pi$, and step [](#substitute){.pf-ref} halves it.
:::

:::

:::

:::
