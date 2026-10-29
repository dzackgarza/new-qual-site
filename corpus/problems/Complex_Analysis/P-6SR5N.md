---
schema: qual/card@1
id: P-6SR5N
kind: problem
title: $\int_0^{2\pi}\frac{1}{a+\cos\theta}\,d\theta=\frac{2\pi}{\sqrt{a^2-1}}$ for
  $a>1$
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
---

::: {.problem}
Show
$$
\int_0^{2\pi} \frac{1}{a + \cos(\theta)} \dtheta = \frac{2\pi}{\sqrt{a^2-1}}, \qquad a> 1.
$$
:::

::: {.solution}
Let $r_1 = -a+\sqrt{a^2-1}$ and $r_2 = -a-\sqrt{a^2-1}$, the roots of $z^2+2az+1$.

::: pf

::: {.pf-step #substitute}
$\displaystyle\int_0^{2\pi} \frac{d\theta}{a + \cos\theta} = \frac{2}{i}\int_{\abs{z}=1} \frac{dz}{z^{2}+2az+1}$.

::: pf-proof
Put $z=e^{i\theta}$, so $\cos\theta = \frac12(z+z^{-1})$ and $d\theta = \frac{dz}{iz}$.
Then $\frac{1}{a+\frac12(z+z^{-1})}\cdot\frac{1}{iz} = \frac{2}{i(z^2+2az+1)}$.
:::

:::

::: {.pf-step #roots}
$r_1\in\DD$ and $\abs{r_2}>1$.

::: pf-proof
$r_1r_2=1$ and $r_2<-a<-1$, so $\abs{r_2}>1$ and $\abs{r_1}=1/\abs{r_2}<1$.
:::

:::

::: pf-step
$\displaystyle\int_0^{2\pi} \frac{d\theta}{a + \cos\theta} = \boxed{\frac{2\pi}{\sqrt{a^2-1}}}$.

::: pf-proof
By step [](#roots){.pf-ref}, the only pole of $\frac{1}{(z-r_1)(z-r_2)}$ inside the unit circle is the simple pole $r_1$, with residue $\frac{1}{r_1-r_2} = \frac{1}{2\sqrt{a^2-1}}$.
By step [](#substitute){.pf-ref} and the residue theorem the integral is $\frac{2}{i}\cdot 2\pi i\cdot\frac{1}{2\sqrt{a^2-1}} = \frac{2\pi}{\sqrt{a^2-1}}$.
:::

:::

:::

:::
