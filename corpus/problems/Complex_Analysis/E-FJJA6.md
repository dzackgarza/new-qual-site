---
schema: qual/card@1
id: E-FJJA6
kind: problem
title: $\int_0^\infty\frac{\log x}{1+x^2}\,dx$
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
- event: statement-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: 'The source states $\int_0^\infty {\log(x) \over 1+x^2}\dx = 0$ with no request; the statement now asks to show it.'
---

::: {.exercise}
Show that
$$
I \coloneqq \int_0^\infty {\log(x) \over 1+x^2}\dx = 0.
$$
:::

::: {.solution}
Take the branch of $\log$ with cut along the ray $\theta = -\pi/2$, so that $\log(-x)=\log x+i\pi$ for $x>0$. Let $f(z) \coloneqq {\log(z) \over z^2 + 1}$, and integrate $f$ over the upper semicircle of radius $R$ indented at $0$ by a semicircle of radius $\varepsilon$, oriented counterclockwise:

![](../../assets/Complex_Analysis/040_Residues/figures/2021-12-22_05-21-05.png)

::: pf

::: {.pf-step #arcs}
The two arcs contribute $0$ as $R\to\infty$ and $\varepsilon\to0$.

::: pf-proof
The large arc contributes $O\qty{(\log R)/R}$ and the small arc $O\qty{\varepsilon\abs{\log\varepsilon}}$.
:::

:::

::: {.pf-step #axis}
As $R\to\infty$ and $\varepsilon\to0$, the real axis contributes $2I+\frac{i\pi^2}{2}$.

::: pf-proof
The segment $[\varepsilon,R]$ contributes $\int_\varepsilon^R f\to I$. On $[-R,-\varepsilon]$, substitute $t=-x$:
$$
\int_{-R}^{-\varepsilon} {\log(t) \over t^2 + 1}\dt
= \int_{\varepsilon}^{R} {\log(x) + i\pi \over x^2 + 1 }\dx
\longrightarrow I + i\pi \cdot {\pi \over 2},
$$
since $\int_0^\infty \frac{dx}{1+x^2}=\frac\pi2$.
:::

:::

::: {.pf-step #residue}
The contour integral equals $\frac{i\pi^2}{2}$.

::: pf-proof
The poles of $f$ are $\pm i$, and only $i$ lies inside the contour. It is simple, with
$$
\Res_{z=i} f = {\log(i) \over 2i} = {i\pi/2 \over 2i} = {\pi \over 4},
$$
so the residue theorem gives $2\pi i\cdot\frac\pi4=\frac{i\pi^2}{2}$.
:::

:::

::: pf-step
$I=0$.

::: pf-proof
By steps [](#arcs){.pf-ref}, [](#axis){.pf-ref} and [](#residue){.pf-ref}, $2I+\frac{i\pi^2}{2}=\frac{i\pi^2}{2}$.
:::

:::

:::

:::
