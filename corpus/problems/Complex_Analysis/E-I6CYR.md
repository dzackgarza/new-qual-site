---
schema: qual/card@1
id: E-I6CYR
kind: problem
title: $B(z,w)=\frac{\Gamma(z)\Gamma(w)}{\Gamma(z+w)}$
classification:
  areas:
  - complex-analysis
  topics:
  - Gamma Function
  - Integrals
  - Convolution
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: {.exercise}
Show that
\[
B(z, w) = {\Gamma(z) \Gamma(w) \over \Gamma(z+w)}
.\]

> Hint: find $\mcl(t^{z-1})$ and $\mcl(t^{z-1}\convolve t^{w-1})$.
:::

::: {.solution}
Let $\operatorname{Re}(z) > 0$ and $\operatorname{Re}(w) > 0$, let $s>0$, and define $f(t) = t^{z-1}$ and $g(t) = t^{w-1}$ for $t > 0$. Recall $B(z, w) = \int_0^1 u^{z-1} (1 - u)^{w-1}\,du$.

::: pf

::: {.pf-step #laplace-of-power}
$\mathcal{L}\{f\}(s) = \frac{\Gamma(z)}{s^z}$ and $\mathcal{L}\{g\}(s) = \frac{\Gamma(w)}{s^w}$.

::: pf-proof
Substituting $u = st$, so $t = u/s$ and $dt = du/s$,
$$\mathcal{L}\{f\}(s) = \int_0^\infty t^{z-1} e^{-st}\,dt = \int_0^\infty \left(\frac{u}{s}\right)^{z-1} e^{-u} \frac{du}{s} = \frac{1}{s^z} \int_0^\infty u^{z-1} e^{-u}\,du = \frac{\Gamma(z)}{s^z}.$$
The same computation with $w$ in place of $z$ gives $\mathcal{L}\{g\}$.
:::

:::

::: {.pf-step #convolution-value}
$(f * g)(x) = x^{z+w-1} B(z, w)$ for $x > 0$.

::: pf-proof
Substituting $t = xu$, so $dt = x\,du$,
$$(f * g)(x) = \int_0^x t^{z-1} (x - t)^{w-1}\,dt = \int_0^1 (xu)^{z-1} (x - xu)^{w-1} x\,du = x^{z+w-1} \int_0^1 u^{z-1} (1 - u)^{w-1}\,du.$$
:::

:::

::: {.pf-step #laplace-of-convolution}
$B(z, w) \frac{\Gamma(z+w)}{s^{z+w}} = \frac{\Gamma(z)\Gamma(w)}{s^{z+w}}$.

::: pf-proof
By step [](#convolution-value){.pf-ref} and step [](#laplace-of-power){.pf-ref} with $z+w$ in place of $z$,
$$\mathcal{L}\{f * g\}(s) = B(z, w) \int_0^\infty x^{z+w-1} e^{-sx}\,dx = B(z, w) \frac{\Gamma(z+w)}{s^{z+w}}.$$
By the convolution theorem for Laplace transforms and step [](#laplace-of-power){.pf-ref},
$$\mathcal{L}\{f * g\}(s) = \mathcal{L}\{f\}(s) \cdot \mathcal{L}\{g\}(s) = \frac{\Gamma(z)\Gamma(w)}{s^{z+w}}.$$
:::

:::

::: pf-qed
Multiply step [](#laplace-of-convolution){.pf-ref} by $s^{z+w}$ and divide by $\Gamma(z+w)$, which has no zeros.
:::

:::
