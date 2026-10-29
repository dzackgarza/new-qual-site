---
schema: qual/card@1
id: E-JKROF
kind: problem
title: $\int_0^{2\pi}\frac{d\theta}{a+b\cos\theta}$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Contour Integration
  - Integrals
  - Trigonometry
relations: []
review: draft
audit:
- event: source-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: The source prints only the identity, with no instruction and no condition on a and b; the statement asks to show it for real a > |b|, where the integrand is continuous and the identity holds.
---

::: {.exercise}
For real numbers $a>\abs b$, show that
$$
\int_{0}^{2 \pi} \frac{d \theta}{a+b \cos \theta}=\frac{2 \pi}{\sqrt{a^{2}-b^{2}}}
.$$
:::

::: {.solution}
If $b=0$, the integral is $2\pi/a$ directly; assume $b\neq0$.
Let $r_\pm\coloneqq{-a\pm\sqrt{a^2-b^2}\over b}$, the roots of $z^2+{2a\over b}z+1$.

::: pf

::: {.pf-step #contour}
$I\coloneqq\int_0^{2\pi}{d\theta\over a+b\cos\theta}=-{2i\over b}\oint_{\abs z=1}{\dz\over(z-r_+)(z-r_-)}$.

::: pf-proof
Substitute $z=e^{i\theta}$, so $\cos\theta={1\over2}(z+z^{-1})$ and $d\theta={\dz\over iz}$:
$$
I=\oint_{\abs z=1}{\dz\over iz\qty{a+{b\over2}(z+z^{-1})}}=-i\oint_{\abs z=1}{\dz\over{b\over2}z^2+az+{b\over2}}=-{2i\over b}\oint_{\abs z=1}{\dz\over z^2+{2a\over b}z+1}
.$$
:::

:::

::: {.pf-step #inside}
$r_+\in\DD$ and $\abs{r_-}>1$.

::: pf-proof
Since $a>\abs b$, the roots are real and distinct, and $r_+r_-=1$.
If $b>0$, then $r_-<-a/b<-1$; if $b<0$, then $r_->a/\abs b>1$.
So $\abs{r_-}>1$ and $\abs{r_+}=1/\abs{r_-}<1$.
:::

:::

::: pf-qed
By steps [](#contour){.pf-ref} and [](#inside){.pf-ref}, the only pole inside the unit circle is the simple pole $r_+$, with residue ${1\over r_+-r_-}={b\over2\sqrt{a^2-b^2}}$, so the residue theorem gives
$$
I=2\pi i\cdot\qty{-{2i\over b}}\cdot{b\over2\sqrt{a^2-b^2}}={2\pi\over\sqrt{a^2-b^2}}
.$$
:::

:::

:::
