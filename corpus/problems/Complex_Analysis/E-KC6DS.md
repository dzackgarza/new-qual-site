---
schema: qual/card@1
id: E-KC6DS
kind: problem
title: $\int_0^\infty\frac{\log x}{x^2+a^2}\,dx$
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
---

::: {.exercise}
Show that, for $a>0$,
$$
\int_0^\infty {\log(x) \over x^2+a^2}\dx = {\pi\log(a)\over 2a}
.$$

:::

::: {.solution}
Let $I$ be the integral, and let $f(z)\coloneqq\frac{\log z}{z^2+a^2}$ with the branch of $\log$ on $\CC\setminus(-i[0,\infty))$ with $\arg z\in(-\pi/2,3\pi/2)$, so that $\log(-t)=\log t+i\pi$ for $t>0$.
For $0<\varepsilon<a<R$ let $\Gamma$ be the indented semicircular contour: $[\varepsilon,R]$, the arc $C_R$ of radius $R$ from $R$ to $-R$ through $\HH$, $[-R,-\varepsilon]$, and the arc $C_\varepsilon$ of radius $\varepsilon$ from $-\varepsilon$ to $\varepsilon$ through $\HH$.
The only pole inside $\Gamma$ is $ia$.

![Indented semicircular contour](../../assets/Complex_Analysis/040_Residues/figures/2021-12-26_20-04-14.png)

::: pf

::: {.pf-step #residue}
$2\pi i\Res_{z=ia}f=\frac{\pi\log a}{a}+\frac{i\pi^2}{2a}$.

::: pf-proof
$\Res_{z=ia}f=\frac{\log(ia)}{2ia}=\frac{\log a+i\pi/2}{2ia}$; multiply by $2\pi i$.
:::

:::

::: {.pf-step #arcs}
$\int_{C_R}f\to0$ as $R\to\infty$ and $\int_{C_\varepsilon}f\to0$ as $\varepsilon\to0$.

::: pf-proof
On $\abs z=r$ in $\overline\HH$, $\abs{\log z}\le\abs{\log r}+\pi$. So $\abs{\int_{C_R}f}\le\pi R\frac{\log R+\pi}{R^2-a^2}\to0$, and $\abs{\int_{C_\varepsilon}f}\le\pi\varepsilon\frac{\abs{\log\varepsilon}+\pi}{a^2-\varepsilon^2}\to0$.
:::

:::

::: {.pf-step #negative-axis}
$\int_{-R}^{-\varepsilon}f(x)\,dx=\int_\varepsilon^R\frac{\log t}{t^2+a^2}\,dt+i\pi\int_\varepsilon^R\frac{dt}{t^2+a^2}$, and the right side tends to $I+\frac{i\pi^2}{2a}$.

::: pf-proof
Substitute $x=-t$ and use $\log(-t)=\log t+i\pi$ and $\int_0^\infty\frac{dt}{t^2+a^2}=\frac{\pi}{2a}$.
:::

:::

::: pf-step
$I=\frac{\pi\log a}{2a}$.

::: pf-proof
By the residue theorem and steps [](#arcs){.pf-ref} and [](#negative-axis){.pf-ref}, in the limit $2I+\frac{i\pi^2}{2a}=2\pi i\Res_{z=ia}f$. Step [](#residue){.pf-ref} gives $2I=\frac{\pi\log a}{a}$.
:::

:::

:::

:::
