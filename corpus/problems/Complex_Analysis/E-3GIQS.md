---
schema: qual/card@1
id: E-3GIQS
kind: problem
title: Mapping $\DD^c \cap \HH$ conformally onto $\HH$ with prescribed boundary values
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
Map $\DD^c \intersect \HH$ to $\HH$, sending

- $-1\to -1$

- $i\to 0$

- $1\to 1$

:::

::: {.solution}
Let $J$ be the Joukowski map
$$
J(z)=\frac{1}{2}\qty{z + z^{-1}}.
$$

![](../../assets/Complex_Analysis/050_Conformal_Maps/figures/2021-12-10_17-13-43.png)

::: pf

::: {.pf-step #upper}
$J$ maps $\theset{\abs z>1}\intersect\HH$ into $\HH$ and $\theset{\abs z>1}\setminus\overline{\HH}$ into the lower half-plane.

::: pf-proof
For $z=re^{i\theta}$ with $r>1$, $\Im J(z)=\frac12\qty{r-r^{-1}}\sin\theta$, which has the sign of $\sin\theta$; points of $\RR$ with $\abs z>1$ map into $\RR\setminus[-1,1]$.
:::

:::

::: {.pf-step #bijective}
$J$ maps $\theset{\abs z>1}$ bijectively and conformally onto $\CC\setminus[-1,1]$.

::: pf-proof
$J(z)=J(w)$ with $z\ne w$ forces $zw=1$, which is impossible when $\abs z,\abs w>1$, and $J'(z)=\frac12(1-z^{-2})\ne0$ there.
Given $c\in\CC\setminus[-1,1]$, the two roots of $z^2-2cz+1=0$ have product $1$ and neither lies on the unit circle, since $J$ maps the unit circle onto $[-1,1]$; so exactly one root has modulus greater than $1$.
:::

:::

::: pf-step
$J$ maps $\DD^c\intersect\HH$ conformally onto $\HH$ with $J(-1)=-1$, $J(i)=0$ and $J(1)=1$.

::: pf-proof
By steps [](#upper){.pf-ref} and [](#bijective){.pf-ref}, $J$ restricts to a conformal bijection of the open set $\theset{\abs z>1}\intersect\HH$ onto $\HH$.
The boundary values are direct computations: $J(\pm1)=\pm1$ and $J(i)=\frac12(i-i)=0$.
:::

:::

:::

:::
