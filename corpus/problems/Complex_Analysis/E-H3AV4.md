---
schema: qual/card@1
id: E-H3AV4
kind: problem
title: A conformal map from the lens $\{|z-\lambda|<1\}\cap\{|z-\bar\lambda|<1\}$
  onto $\mathbb{D}$, for $\lambda=\frac12(1+i\sqrt{3})$
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Fractional Linear Transformations
relations: []
review: draft
audit:
- event: source-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: The source reads "find a map R -> D"; the statement asks for a conformal map onto D, without which a constant map answers it.
---

::: {.problem}
Let $\lambda = {1\over 2}\qty{1 + i \sqrt{3}}$ and find a conformal map of
$$
R \coloneqq \theset{\abs{z - \lambda} < 1} \intersect \theset{\abs{z-\bar{\lambda}} < 1 }
$$
onto $\DD$.
:::

::: {.solution}
Let $C_1=\theset{\abs{z-\lambda}=1}$ and $C_2=\theset{\abs{z-\bar\lambda}=1}$. Since $\abs\lambda=\abs{1-\lambda}=1$, both circles pass through $0$ and $1$, and $R$ is the lens between them:

![](../../assets/Complex_Analysis/999_Quals/figures/2021-12-29_19-19-01.png)

Let $f(z) \coloneqq {z\over 1-z}$, which sends the vertices $0$ and $1$ of the lens to $0$ and $\infty$.
The figure below is labelled $z\mapsto{z\over z-1}$; the sector it shows is the image under $f(z)={z\over1-z}=-{z\over z-1}$.

![](../../assets/Complex_Analysis/999_Quals/figures/2021-12-29_19-35-44.png)

::: pf

::: {.pf-step #sector}
$f(R) = \theset{w \st \abs{\Arg w} < \pi/6}$.

::: pf-proof
Since $C_1$ and $C_2$ pass through $0$ and $1$, their images pass through $f(0)=0$ and $f(1)=\infty$, so they are lines through the origin.

The point $z_0=i\sqrt3$ lies on $C_1$, since $\abs{i\sqrt3-\lambda}^2={1\over4}+{3\over4}=1$, and
$$
f(z_0) = {i\sqrt 3 \over 1-i\sqrt 3} = {i\sqrt3(1+i\sqrt3)\over4} = {1\over 4}\qty{-3+i\sqrt 3}
,$$
which has argument $5\pi/6$. So $f(C_1)$ is the line through $0$ in the directions $5\pi/6$ and $-\pi/6$.
Similarly $z_1=-i\sqrt3\in C_2$ and $f(z_1)={1\over4}\qty{-3-i\sqrt3}$, so $f(C_2)$ is the line through $0$ in the directions $-5\pi/6$ and $\pi/6$.

The two lines divide $\CC\setminus\theset{0}$ into four open sectors, and $f(R)$ is one of them, being connected with boundary in the two lines.
Since ${1\over2}\in R$ and $f\qty{1\over2}=1$, $f(R)$ is the sector containing $1$, which is $\abs{\Arg w}<\pi/6$.
:::

:::

::: pf-step
$\boxed{F(z)={z^3-(1-z)^3\over z^3+(1-z)^3}}$ maps $R$ conformally onto $\DD$.

::: pf-proof
$F$ is the composite of the following conformal bijections:

- $f$ maps $R$ onto $\abs{\Arg w}<\pi/6$, by step [](#sector){.pf-ref};

- $w\mapsto w^3$ maps $\abs{\Arg w}<\pi/6$ onto the right half-plane $\abs{\Arg w}<\pi/2$;

- $w\mapsto iw$ maps the right half-plane onto $\HH$;

- $w\mapsto {w-i\over w+i}$ maps $\HH$ onto $\DD$.

The composite is ${iw^3-i\over iw^3+i}={w^3-1\over w^3+1}$ with $w={z\over1-z}$, which equals $F(z)$.
:::

:::

:::

:::
