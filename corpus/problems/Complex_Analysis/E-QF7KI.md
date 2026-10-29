---
schema: qual/card@1
id: E-QF7KI
kind: problem
title: Residues at infinity
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Contour Integration
  - Singularities
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.exercise}
Use residues at infinity to evaluate
$$
\int_{\abs{z}=1} \frac{1}{(z-2)(1+2 z)^{4}(1-3 z)^{7}} \dz.
$$
:::

::: {.solution}

Let $f(z) \coloneqq \frac{1}{(z-2)(1+2z)^4(1-3z)^7}$.
Its poles are $-1/2$ and $1/3$, inside $\abs{z}=1$, and $2$, outside.

::: pf

::: {.pf-step #sum-zero}
The residues of $f$ at $-1/2$, $1/3$, $2$ and $\infty$ sum to $0$.

::: pf-proof
For $R>2$, the residue theorem gives $\oint_{\abs{z}=R}f = 2\pi i\sum_{\text{finite poles}}\Res f$, and by definition $\Res_{z=\infty}f = -\frac{1}{2\pi i}\oint_{\abs{z}=R}f$.
:::

:::

::: {.pf-step #res-infinity}
$\Res_{z=\infty} f = 0$.

::: pf-proof
$\Res_{z=\infty} f = -\Res_{z=0}\frac{1}{z^2}f(1/z)$, and
$$
\frac{1}{z^2} f(1/z) = \frac{z^{10}}{(1-2z)(z+2)^4(z-3)^7}
$$
is holomorphic at $0$.
:::

:::

::: {.pf-step #res-two}
$\Res_{z=2} f = -\frac{1}{5^{11}}$.

::: pf-proof
$2$ is a simple pole, so $\Res_{z=2} f = \lim_{z \to 2} (z-2) f(z) = \frac{1}{5^4 \cdot (-5)^7} = -\frac{1}{5^{11}}$.
:::

:::

::: pf-step
$\displaystyle\oint_{\abs{z}=1} f(z)\,dz = \boxed{\frac{2\pi i}{5^{11}}}$.

::: pf-proof
By the residue theorem and steps [](#sum-zero){.pf-ref}, [](#res-infinity){.pf-ref} and [](#res-two){.pf-ref},
$$
\oint_{\abs{z}=1} f = 2\pi i\left(\Res_{z=-1/2}f + \Res_{z=1/3}f\right) = -2\pi i\left(\Res_{z=2}f + \Res_{z=\infty}f\right) = \frac{2\pi i}{5^{11}}.
$$
:::

:::

:::

:::
