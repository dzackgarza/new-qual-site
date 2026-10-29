---
schema: qual/card@1
id: P-KUNLD
kind: problem
title: Tangent from polynomial long division
classification:
  areas:
  - complex-analysis
  topics:
  - Laurent Series
  - Power Series
  - Trigonometry
relations: []
review: draft
---

::: {.exercise}
Find a Laurent expansion about $z_0=0$ for $f(z) = \tan(z)$ by using polynomial long division on the series expansions for $\sin(z)$ and $\cos(z)$.
:::

::: {.solution}
Write $C(z) = 1 - \frac{z^2}{2} + \frac{z^4}{24} + O(z^6)$ and $S(z) = z - \frac{z^3}{6} + \frac{z^5}{120} + O(z^7)$ for the series of $\cos z$ and $\sin z$.
Since $\cos 0 \neq 0$, $\tan z = S/C$ is holomorphic at $0$, so its Laurent series is a Taylor series, convergent for $\abs{z} < \pi/2$; we divide $S$ by $C$ in increasing powers of $z$.

::: pf

::: {.pf-step #first}
$S = C\cdot z + \frac13 z^3 - \frac1{30}z^5 + O(z^7)$.

::: pf-proof
$C\cdot z = z - \frac{z^3}{2} + \frac{z^5}{24} + O(z^7)$, and $-\frac16 + \frac12 = \frac13$, $\frac1{120} - \frac1{24} = -\frac1{30}$.
:::

:::

::: {.pf-step #second}
$\frac13 z^3 - \frac1{30}z^5 = C\cdot\frac13 z^3 + \frac2{15}z^5 + O(z^7)$.

::: pf-proof
$C\cdot\frac13 z^3 = \frac13 z^3 - \frac16 z^5 + O(z^7)$, and $-\frac1{30} + \frac16 = \frac2{15}$.
:::

:::

::: {.pf-step #third}
$\frac2{15}z^5 = C\cdot\frac2{15}z^5 + O(z^7)$.

::: pf-proof
$C\cdot\frac2{15}z^5 = \frac2{15}z^5 + O(z^7)$.
:::

:::

::: pf-step
$$
\boxed{\tan z = z + \frac13 z^3 + \frac2{15}z^5 + O(z^7)}.
$$

::: pf-proof
Steps [](#first){.pf-ref}, [](#second){.pf-ref} and [](#third){.pf-ref} give $S = C\cdot\left(z + \frac13 z^3 + \frac2{15}z^5\right) + O(z^7)$; divide by $C$, which is a unit near $0$.
:::

:::

:::
:::
