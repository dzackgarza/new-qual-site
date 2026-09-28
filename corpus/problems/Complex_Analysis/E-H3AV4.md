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
---

::: {.problem}
Let $\lambda = {1\over 2}\qty{1 + i \sqrt{3}}$ and find a map 
\[
R \da \ts{\abs{z - \lambda} < 1} \intersect \ts{\abs{z-\bar{\lambda}} < 1 } \too \DD
.\]
:::

::: {.solution}
Let $C_1=\theset{\abs{z-\lambda}=1}$ and $C_2=\theset{\abs{z-\bar\lambda}=1}$. Since $\abs\lambda=\abs{1-\lambda}=1$, both circles pass through $0$ and $1$, and $R$ is the lens between them:

![](../../assets/Complex_Analysis/999_Quals/figures/2021-12-29_19-19-01.png)

Send the vertices $0$ and $1$ of the lens to $0$ and $\infty$ with
\[
f(z) \da {z\over 1-z}
.\]

::: {.claim}
\[
f(R) = \ts{z\st -\theta_0 < \Arg(z) < \theta_0 },\qquad \theta_0 \da {\pi \over 6}
.\]

![](../../assets/Complex_Analysis/999_Quals/figures/2021-12-29_19-35-44.png)

The figure is labelled $z\mapsto{z\over z-1}$; the sector it shows is the image under $f(z)={z\over1-z}=-{z\over z-1}$.
:::

::: {.proof title="of claim"}
Since $C_1$ and $C_2$ pass through $0$ and $1$, their images pass through $f(0)=0$ and $f(1)=\infty$, so they are lines through the origin.

The point $z_0=i\sqrt3$ lies on $C_1$, since $\abs{i\sqrt3-\lambda}^2={1\over4}+{3\over4}=1$, and
\[
f(z_0) = {i\sqrt 3 \over 1-i\sqrt 3} = {i\sqrt3(1+i\sqrt3)\over4} = {1\over 4}\qty{-3+i\sqrt 3}
,\]
which has argument $5\pi/6$. So $f(C_1)$ is the line through $0$ in the directions $5\pi/6$ and $-\pi/6$.
Similarly $z_1=-i\sqrt3\in C_2$ and $f(z_1)={1\over4}\qty{-3-i\sqrt3}$, so $f(C_2)$ is the line through $0$ in the directions $-5\pi/6$ and $\pi/6$.

The two lines divide $\CC\setminus\theset{0}$ into four open sectors, and $f(R)$ is one of them, being connected with boundary in the two lines. Since ${1\over2}\in R$ and $f\qty{1\over2}=1$, $f(R)$ is the sector containing $1$, which is $\abs{\Arg z}<\pi/6$.
:::

From here we map to the disc in the following steps:

- $z\mapsto {z\over 1-z}$ sends $R$ to $\abs{\Arg(z)} < \theta_0$.
- $z\mapsto z^{\pi \over 2\theta_0}=z^3$ maps $\abs{\Arg(z)}<\theta_0$ onto $\abs{\Arg(z)} < {\pi \over 2}$, the right half-plane.
- $z\mapsto iz$ rotates the right half-plane onto $\HH$.
- $z\mapsto {z-i\over z+i}$ maps $\HH$ onto $\DD$.

The composite is
\[
F(z)={i\qty{z\over1-z}^3-i\over i\qty{z\over1-z}^3+i}={z^3-(1-z)^3\over z^3+(1-z)^3}
.\]
:::
