---
schema: qual/card@1
id: E-Z4JCZ
kind: problem
title: $\int_0^{2\pi} d\theta/(1+a^2-2a\cos\theta)$ and the Poisson kernel
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Contour Integration
  - Integrals
  - Trigonometry
  - Harmonic Functions
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: 'Source printed the formula without saying what a is; for complex a the formula is false, so the statement now takes a real with |a| != 1 and asks to show the formula.'
---

::: {.exercise}
Let $a\in\RR$ with $\abs a\neq1$. Show that
$$
\int_{0}^{2 \pi} \frac{d \theta}{1+a^{2}-2 a \cos (\theta)}
= \begin{cases}\frac{2 \pi}{a^{2}-1} & \text { if }\abs a>1 \\ \frac{2 \pi}{1-a^{2}} & \text { if }\abs a<1.\end{cases}
$$
:::

::: {.solution}
Write $I$ for the integral.
If $a=0$, the integrand is $1$ and $I = 2\pi = \frac{2\pi}{1-a^2}$, so assume $a\neq0$.

::: pf

::: {.pf-step #contour}
$\displaystyle I = \frac ia\oint_{\abs z=1}\frac{dz}{(z-a)(z-a^{-1})}$.

::: pf-proof
Substitute $z = e^{i\theta}$, so $d\theta = \frac{dz}{iz}$ and $2\cos\theta = z + z^{-1}$.
Then $iz\qty(1+a^2 - a(z+z^{-1})) = -i\qty(az^2 - (1+a^2)z + a) = -ia(z-a)(z-a^{-1})$.
The integrand has no pole on $\abs z=1$ because $\abs a\neq1$.
:::

:::

::: pf-step
If $0<\abs a<1$, then $I = \boxed{\dfrac{2\pi}{1-a^2}}$.

::: pf-proof
Only the simple pole $a$ lies inside the circle, with residue $\frac{1}{a-a^{-1}}$.
By step [](#contour){.pf-ref} and the residue theorem, $I = \frac ia\cdot 2\pi i\cdot\frac{1}{a-a^{-1}} = \frac{-2\pi}{a^2-1}$.
:::

:::

::: pf-step
If $\abs a>1$, then $I = \boxed{\dfrac{2\pi}{a^2-1}}$.

::: pf-proof
Only the simple pole $a^{-1}$ lies inside the circle, with residue $\frac{1}{a^{-1}-a}$.
By step [](#contour){.pf-ref} and the residue theorem, $I = \frac ia\cdot2\pi i\cdot\frac{1}{a^{-1}-a} = \frac{-2\pi}{1-a^2}$.
:::

:::

:::

:::
