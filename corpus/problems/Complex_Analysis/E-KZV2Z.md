---
schema: qual/card@1
id: E-KZV2Z
kind: problem
title: $\int_0^\infty\frac{dx}{x^2+3x+2}$ by a keyhole contour
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
- event: source-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: The source prints the integral over R, which diverges because x^2+3x+2 vanishes at -1 and -2. The solution computes the integral over (0, infinity), and the statement now asks for that integral.
---

::: {.exercise}
Compute
$$
I\coloneqq\int_0^\infty {1\over x^2 + 3x+ 2 }\dx
.$$

:::

::: {.solution}
Let $f(z)\coloneqq\frac{1}{(z+1)(z+2)}$, and let $\log$ be the branch on $\CC\setminus[0,\infty)$ with $\arg z\in(0,2\pi)$.
Since $f$ is not even, a semicircle does not reduce to $I$; we integrate $f(z)\log z$ over a keyhole contour $\Gamma$ around $[0,\infty)$: the upper edge from $\varepsilon$ to $R$, the circle $\abs z=R$ counterclockwise, the lower edge from $R$ to $\varepsilon$, and the circle $\abs z=\varepsilon$ clockwise, with $0<\varepsilon<1<2<R$.

![Keyhole contour](../../assets/Complex_Analysis/040_Residues/figures/2021-12-24_04-03-05.png)

::: pf

::: {.pf-step #edges}
As the edges approach the axis, their integrals sum to $-2\pi i\int_\varepsilon^Rf(t)\,dt$.

::: pf-proof
On the upper edge $\log z\to\log t$, and on the lower edge $\log z\to\log t+2\pi i$, traversed from $R$ to $\varepsilon$. The sum tends to $\int_\varepsilon^Rf(t)\log t\,dt-\int_\varepsilon^Rf(t)(\log t+2\pi i)\,dt$.
:::

:::

::: {.pf-step #circles}
The integrals over $\abs z=R$ and $\abs z=\varepsilon$ tend to $0$ as $R\to\infty$ and $\varepsilon\to0$.

::: pf-proof
On $\abs z=r$, $\abs{\log z}\le\abs{\log r}+2\pi$. For $r=R$, $\abs f\le\frac1{(R-1)(R-2)}$, so the integral is at most $2\pi R\frac{\log R+2\pi}{(R-1)(R-2)}\to0$. For $r=\varepsilon$, $\abs f\le\frac1{(1-\varepsilon)(2-\varepsilon)}$, so the integral is at most $2\pi\varepsilon\frac{\abs{\log\varepsilon}+2\pi}{(1-\varepsilon)(2-\varepsilon)}\to0$.
:::

:::

::: {.pf-step #residues}
The residues of $f(z)\log z$ sum to $-\ln2$.

::: pf-proof
At the simple poles, $\Res_{z=-1}=\frac{\log(-1)}{-1+2}=i\pi$ and $\Res_{z=-2}=\frac{\log(-2)}{-2+1}=-(\ln2+i\pi)$.
:::

:::

::: pf-step
$I=\boxed{\ln2}$.

::: pf-proof
By the residue theorem and steps [](#edges){.pf-ref}, [](#circles){.pf-ref} and [](#residues){.pf-ref}, $-2\pi iI=2\pi i(-\ln2)$.
:::

:::

:::

:::

::: {.remark}
Partial fractions confirm the value: $\int_0^\infty\qty{\frac1{x+1}-\frac1{x+2}}dx=\qty[\ln\frac{x+1}{x+2}]_0^\infty=\ln2$.
:::
