---
schema: qual/card@1
id: P-Y4TND
kind: problem
title: $\int_{-\infty}^{\infty}\frac{e^{ax}}{1+e^x}\,dx=\frac{\pi}{\sin\pi a}$ for $0<a<1$
classification:
  areas:
  - complex-analysis
  topics:
  - Contour Integration
relations: []
review: draft
---

::: {.problem}
Show that for $0<a<1$,
$$
\int_{-\infty}^{\infty}\frac{e^{ax}}{1+e^x}\,dx
=\frac{\pi}{\sin\pi a}.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #subst}
$\displaystyle\int_{-\infty}^{\infty}\frac{e^{ax}}{1+e^x}\,dx=\int_0^\infty \frac{t^{a-1}}{1+t}\,dt$.

::: pf-proof
Substitute $t=e^x$, so that $e^{ax}=t^a$ and $dx=dt/t$.
:::

:::

::: pf-step
$\displaystyle\int_0^\infty \frac{t^{a-1}}{1+t}\,dt=\frac{\pi}{\sin\pi a}$.

::: pf-proof
For $0<a<1$, Euler's beta integral gives
$$
\int_0^\infty \frac{t^{a-1}}{1+t}\,dt
=B(a,1-a)=\Gamma(a)\Gamma(1-a)
=\frac{\pi}{\sin\pi a},
$$
the last equality by Euler's reflection formula. With step [](#subst){.pf-ref} this proves the claim.
:::

:::

:::

:::
