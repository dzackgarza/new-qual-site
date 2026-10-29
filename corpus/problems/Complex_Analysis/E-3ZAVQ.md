---
schema: qual/card@1
id: E-3ZAVQ
kind: problem
title: $\int_\RR\frac{\sin x}{x}\,dx$ by an indented semicircle and Jordan's lemma
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Contour Integration
  - Integrals
relations: []
review: draft
---

::: {.exercise}
Compute
$$
\int_\RR \frac{\sin(x)}{x}\dx.
$$

:::

::: {.solution}
Let $f(z) \coloneqq e^{iz}/z$, and for $0<\varepsilon<R$ let

- $C_+ \coloneqq [\varepsilon, R]$ and $C_- \coloneqq [-R, -\varepsilon]$,
- $C_\varepsilon(t) \coloneqq \varepsilon e^{it}$ and $C_R(t) \coloneqq R e^{it}$ for $t\in [0, \pi]$,
- $\Gamma \coloneqq C_+ + C_R + C_- - C_\varepsilon$.

![](../../assets/Complex_Analysis/040_Residues/figures/2021-12-20_06-55-40.png)

Write $I$ for the requested integral, taken as the improper integral $\lim_{\varepsilon\to0,\,R\to\infty}\int_{\varepsilon\le\abs x\le R}\frac{\sin x}{x}\dx$.

::: pf

::: {.pf-step #real-part}
$I=\Im\lim_{\varepsilon\to0}\lim_{R\to\infty}\qty{\int_{C_+}+\int_{C_-}}f$.

::: pf-proof
On $C_+\cup C_-$ the imaginary part of $e^{ix}/x$ is $\sin(x)/x$.
:::

:::

::: {.pf-step #cauchy}
$\qty{\int_{C_+}+\int_{C_-}}f=\int_{C_\varepsilon}f-\int_{C_R}f$.

::: pf-proof
$f$ is holomorphic on a neighbourhood of $\Gamma$ and its interior, so $\int_\Gamma f=0$ by Cauchy's theorem.
:::

:::

::: {.pf-step #jordan}
$\int_{C_R}f\to0$ as $R\to\infty$.

::: pf-proof
The estimate $\pi R\sup_{C_R}\abs{1/z}=\pi$ does not tend to $0$, so the length bound alone fails.
Jordan's lemma gives $\int_0^\pi e^{-R\sin t}\,dt\le\pi/R$, hence $\abs{\int_{C_R}f}\le\int_0^\pi e^{-R\sin t}\,dt\le\pi/R$.
:::

:::

::: {.pf-step #small-arc}
$\int_{C_\varepsilon}f\to i\pi$ as $\varepsilon\to0$.

::: pf-proof
$f$ has a simple pole at $0$ with residue $1$, and $C_\varepsilon$ is a counterclockwise half-circle, so the fractional residue formula gives $i\pi\Res_{z=0}f=i\pi$.
:::

:::

::: pf-step
$I=\boxed{\pi}$.

::: pf-proof
By steps [](#real-part){.pf-ref}--[](#small-arc){.pf-ref}, $I=\Im(i\pi-0)=\pi$.
:::

:::

:::

:::
