---
schema: qual/card@1
id: P-YDJE6
kind: problem
title: $\frac{1}{2\pi i}\int_{\abs{z}=2}\frac{z^n}{1-2z\cos\theta+z^2}\,dz=\frac{\sin(n\theta)}{\sin\theta}$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Contour Integration
  - Trigonometry
  - Poles
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
- event: source-corrected
  by: claude-opus-5-5
  date: 2026-10-29
  note: 'The card printed the denominator as 1 - 3z cos(theta) + z^2, for which the stated value is false; corrected to 1 - 2z cos(theta) + z^2, which the solution already used.'
---

::: {.problem}
Let $n\in \ZZ^{\geq 1}$ and $0<\theta<\pi$ and show that
$$
\frac{1}{2\pi i} \int_{\abs z = 2} \frac{z^n}{1 -2z\cos(\theta) + z^2} \,dz = \frac{\sin(n\theta)}{\sin(\theta)}.
$$
:::

::: {.solution}
Let $g(z)=\dfrac{z^n}{1-2z\cos\theta+z^2}$.

::: pf

::: {.pf-step #poles}
$g$ has simple poles at $e^{i\theta}$ and $e^{-i\theta}$, both in $\abs{z}<2$, and no other poles.

::: pf-proof
$z^2-2z\cos\theta+1=(z-e^{i\theta})(z-e^{-i\theta})$, the roots have modulus $1<2$, and they are distinct because $\sin\theta\ne0$ for $0<\theta<\pi$.
:::

:::

::: {.pf-step #residues}
$\Res(g,e^{i\theta})+\Res(g,e^{-i\theta})=\dfrac{\sin(n\theta)}{\sin\theta}$.

::: pf-proof
At simple poles,
$$
\Res(g,e^{i\theta})=\frac{e^{in\theta}}{e^{i\theta}-e^{-i\theta}}=\frac{e^{in\theta}}{2i\sin\theta},
\qquad
\Res(g,e^{-i\theta})=\frac{e^{-in\theta}}{e^{-i\theta}-e^{i\theta}}=-\frac{e^{-in\theta}}{2i\sin\theta},
$$
and the sum is $\dfrac{e^{in\theta}-e^{-in\theta}}{2i\sin\theta}=\dfrac{\sin(n\theta)}{\sin\theta}$.
:::

:::

::: pf-step
$\dfrac{1}{2\pi i}\displaystyle\int_{\abs{z}=2}g(z)\,dz=\dfrac{\sin(n\theta)}{\sin\theta}$.

::: pf-proof
By the residue theorem and steps [](#poles){.pf-ref} and [](#residues){.pf-ref}.
:::

:::

:::

:::
