---
schema: qual/card@1
id: E-4H3JY
kind: problem
title: A conformal map from $\DD$ onto $\HH$
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Fractional Linear Transformations
relations: []
review: draft
---

::: {.exercise}
Find a conformal map from $\DD$ to $\HH$.
:::

::: {.solution}
Let
$$
T(z)=i\frac{1+z}{1-z},\qquad S(w)=\frac{w-i}{w+i},
$$
so that $S$ is the Cayley map and $T=S^{-1}$ as fractional linear transformations.

::: pf

::: {.pf-step #into-H}
$T(\DD)\subseteq\HH$.

::: pf-proof
For $z\in\DD$,
$$
\Im T(z)=\Re \frac{1+z}{1-z}=\frac{1-\abs{z}^2}{\abs{1-z}^2}>0.
$$
:::

:::

::: {.pf-step #into-D}
$S(\HH)\subseteq\DD$.

::: pf-proof
For $\Im w>0$, the point $w$ is closer to $i$ than to $-i$, so $\abs{w-i}<\abs{w+i}$.
:::

:::

::: pf-step
$T:\DD\to\HH$ is a conformal bijection.

::: pf-proof
By steps [](#into-H){.pf-ref} and [](#into-D){.pf-ref}, $T|_\DD$ and $S|_\HH$ are mutually inverse holomorphic maps, so $T$ is biholomorphic onto $\HH$.
:::

:::

:::

:::
