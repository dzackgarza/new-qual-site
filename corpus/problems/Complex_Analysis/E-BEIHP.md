---
schema: qual/card@1
id: E-BEIHP
kind: problem
title: $\int_{-\pi}^{\pi}\frac{d\theta}{1+\sin^2\theta}$
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
  note: The source displays the integral with no instruction; the statement asks to compute it.
---

::: {.exercise}
Compute
$$
\int_{[-\pi, \pi]} \frac{1}{1 + \sin^2(\theta)} \dtheta.
$$
:::

::: {.solution}
Let $I$ be the integral and $g(z)\coloneqq\frac{4iz}{z^4-6z^2+1}$.

::: pf

::: {.pf-step #substitute}
$I=\oint_{\abs z=1}g(z)\dz$.

::: pf-proof
Set $z=e^{i\theta}$, so $\sin\theta = \frac{z-z^{-1}}{2i}$, $\sin^2\theta = -\frac{1}{4}(z^{-2}-2+z^2)$, and $\dtheta=\frac{\dz}{iz}$.
Then
$$
\frac{1}{1 + \sin^2\theta}\dtheta
= \frac{1}{1 - \frac{1}{4}(z^{-2} -2 + z^2)}\, \frac{\dz}{iz}
= \frac{4z}{i(6z^2-1-z^4)}\dz
= \frac{4iz}{z^4-6z^2+1}\dz.
$$
:::

:::

::: {.pf-step #poles}
The poles of $g$ in $\DD$ are $z_\pm\coloneqq\pm\sqrt{3-\sqrt 8}$, and both are simple.

::: pf-proof
With $w=z^2$, $w^2-6w+1=0$ gives $w=3\pm\sqrt8$, so the four zeros of the denominator are $\pm\sqrt{3\pm\sqrt8}$, all distinct.
Since $2<\sqrt8<3$, we have $0<3-\sqrt8<1<3+\sqrt8$.
:::

:::

::: {.pf-step #residues}
$\Res_{z=z_\pm}g=-\frac{i}{\sqrt8}$.

::: pf-proof
At a simple zero $z_0$ of the denominator,
$$
\Res_{z=z_0}g = \frac{4iz_0}{4z_0^3 - 12z_0} = \frac{i}{z_0^2 - 3},
$$
and $z_\pm^2-3=-\sqrt8$.
:::

:::

::: pf-step
$I=\boxed{\frac{4\pi}{\sqrt 8}=\sqrt2\,\pi}$.

::: pf-proof
By steps [](#substitute){.pf-ref}, [](#poles){.pf-ref}, and [](#residues){.pf-ref} and the residue theorem, $I = 2\pi i\cdot\qty{-\frac{2i}{\sqrt 8}} = \frac{4\pi}{\sqrt{8}}$.
:::

:::

:::

:::
