---
schema: qual/card@1
id: E-H64WF
kind: problem
title: A fractional linear map sending $i\RR$ onto $\abs{z-\frac12}=\frac12$
classification:
  areas:
  - complex-analysis
  topics:
  - Fractional Linear Transformations
  - Conformal Maps
  - Trigonometry
relations: []
review: draft
---

::: {.exercise}
Find a conformal map that sends $i\RR$ to $\abs{z-{1\over 2}} = {1\over 2}$.
:::

::: {.hint}
With $x=\tan t$ for $t\in(-\pi/2,\pi/2)$, the double-angle formulas
$$
\sin(2t) = {2\tan t \over 1+\tan^2 t}, \qquad \cos(2t) = {1-\tan^2 t \over 1+\tan^2 t}
$$
parameterize a circle by a line; for instance $F(z)\coloneqq{i-z\over i+z}$ satisfies $F(x)=e^{2it}$ [@SS03, Chapter 8, Theorem 1.2].
:::

::: {.solution}
The line $i\RR$, traversed from $-i\infty$ through $0$ to $i\infty$, is to be mapped to the circle traversed from $0$ through $1$ back to $0$:

![The imaginary axis, parametrized by s = i omega, is mapped by w = 1/(s+1) onto the circle of radius 1/2 centred at 1/2, with 0 sent to 1, infinity sent to 0, and plus or minus 2i sent to points on the circle.](../../assets/Complex_Analysis/050_Conformal_Maps/figures/2021-12-18_22-01-30.png)

Let $R(z)\coloneqq{1\over z+1}$, the fractional linear transformation sending $0\mapsto1$, $\infty\mapsto0$ and $-1\mapsto\infty$.

::: pf

::: {.pf-step #circle}
$R$ maps $i\RR$ onto the circle $\abs{w-{1\over2}}={1\over2}$ minus the point $0=R(\infty)$.

::: pf-proof
Write $it$ with $t=\tan s$ and $s\in(-\pi/2,\pi/2)$. Then
$$
\begin{aligned}
R(it) &= {1\over 1+it} = {1-it\over 1+t^2} = {1\over 2} \qty{ 1 + {1-t^2\over 1+t^2} } - {i\over 2}\cdot{2t\over 1+t^2} \\
&= {1\over 2}\qty{1 + \cos(2s) - i\sin(2s)} = {1\over 2} + {1\over 2}e^{-2is}
,\end{aligned}
$$
and as $s$ ranges over $(-\pi/2,\pi/2)$ this covers the circle of radius $1/2$ about $1/2$ except the point $0$.
:::

:::

::: pf-step
$\boxed{z\mapsto{1\over1+z}}$ sends $i\RR\union\theset\infty$ onto $\abs{z-{1\over2}}={1\over2}$, with inverse $w\mapsto{1-w\over w}$.

::: pf-proof
Step [](#circle){.pf-ref} together with $R(\infty)=0$ gives the image, and solving $w={1\over1+z}$ gives $z={1-w\over w}$.
:::

:::

:::

:::
