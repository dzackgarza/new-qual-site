---
schema: qual/card@1
id: P-FS6W6
kind: problem
title: A conformal map from $\DD$ to $\HH$
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Fractional Linear Transformations
relations: []
review: draft
---

::: {.problem}
Find a conformal map from $\DD$ to $\HH$.
:::

::: {.solution}
::: pf

::: {.pf-step #into}
The Cayley transform $F(z) = i\dfrac{1+z}{1-z}$ maps $\DD$ into $\HH$.

::: pf-proof
$F$ is a Möbius transformation with its only pole at $z=1\notin\DD$. For $\abs z<1$,
$$
\Im F(z) = \Re\frac{1+z}{1-z} = \Re\frac{(1+z)(1-\bar z)}{\abs{1-z}^2} = \frac{1-\abs z^2}{\abs{1-z}^2}>0.
$$
:::

:::

::: {.pf-step #inverse}
$G(w) = \dfrac{w-i}{w+i}$ maps $\HH$ into $\DD$, and $F\circ G = \id_{\HH}$, $G\circ F = \id_{\DD}$.

::: pf-proof
For $\Im w>0$, $w$ is closer to $i$ than to $-i$, so $\abs{w-i}<\abs{w+i}$ and $\abs{G(w)}<1$. Solving $w = i(1+z)/(1-z)$ for $z$ gives $z = (w-i)/(w+i)$, so $F$ and $G$ are inverse Möbius maps.
:::

:::

::: pf-step
$\boxed{F(z)=i\dfrac{1+z}{1-z}}$ is a conformal map from $\DD$ onto $\HH$.

::: pf-proof
By steps [](#into){.pf-ref} and [](#inverse){.pf-ref}, $F:\DD\to\HH$ is a holomorphic bijection with holomorphic inverse $G$.
:::

:::

:::

:::
