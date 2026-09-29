---
schema: qual/card@1
id: P-J5JVJ
kind: problem
title: $\int_0^1\log(\sin\pi x)\,dx=-\log 2$
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
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: {.problem}
Show that
\[
\int_{0}^{1} \log (\sin \pi x) d x=-\log 2
.\]

> Hint: use the following contour.
> ![](../../assets/Complex_Analysis/999_Quals/figures/image_2020-06-17-21-52-40.png)
:::

::: {.solution}

::: pf

::: {.pf-step #rescale-to-0-pi}
$\int_0^1 \log(\sin \pi x)\,dx = \frac{1}{\pi}\int_0^{\pi} \log(\sin t)\,dt$.

::: pf-proof
Substitute $t = \pi x$.
:::

:::

::: {.pf-step #symmetric-about-half}
$\int_0^{\pi} \log(\sin t)\,dt = 2\int_0^{\pi/2} \log(\sin t)\,dt$.

::: pf-proof
The substitution $t\mapsto\pi-t$ maps $[\pi/2,\pi]$ onto $[0,\pi/2]$ and $\sin(\pi-t)=\sin t$.
:::

:::

::: {.pf-step #half-integral-value}
$\int_0^{\pi/2} \log(\sin t)\,dt = -\frac{\pi}{2}\log 2$.

::: pf-proof
Let $J=\int_0^{\pi/2} \log(\sin t)\,dt$, which converges because $\log(\sin t)\sim\log t$ as $t\to0^+$. The substitution $t \mapsto \pi/2 - t$ gives $J=\int_0^{\pi/2} \log(\cos t)\,dt$. Adding and using $\sin t\cos t = \frac12\sin 2t$,
$$2J = \int_0^{\pi/2} \log\left(\tfrac12\sin 2t\right)dt = -\frac{\pi}{2}\log 2 + \frac12\int_0^{\pi} \log(\sin u)\,du = -\frac{\pi}{2}\log 2 + J,$$
where the last equality is step [](#symmetric-about-half){.pf-ref}. Hence $J = -\frac{\pi}{2}\log 2$.
:::

:::

::: {.pf-step #full-integral-value}
$\int_0^{\pi} \log(\sin t)\,dt = -\pi \log 2$.

::: pf-proof
Steps [](#symmetric-about-half){.pf-ref} and [](#half-integral-value){.pf-ref} give $2 \cdot (-\frac{\pi}{2}\log 2)$.
:::

:::

::: {.pf-step #final-value}
$\int_0^1 \log(\sin \pi x)\,dx = \boxed{-\log 2}$.

::: pf-proof
Steps [](#rescale-to-0-pi){.pf-ref} and [](#full-integral-value){.pf-ref} give $\frac{1}{\pi}(-\pi \log 2)$.
:::

:::

::: pf-qed
Step [](#final-value){.pf-ref} is the required identity.
:::

:::
:::
