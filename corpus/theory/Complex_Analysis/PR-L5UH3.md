---
schema: qual/card@1
id: PR-L5UH3
kind: proposition
title: Biholomorphism from the right half-plane onto the unit disc
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Fractional Linear Transformations
relations: []
review: draft
---

::: {.proposition}
Let $\HH_R\coloneqq\ts{z\in\CC \st \Re z>0}$ be the right half-plane and $\DD\coloneqq\ts{w\in\CC \st \abs{w}<1}$ the unit disc.
The map
$$
\varphi\colon\HH_R\to\DD,\qquad \varphi(z)=\frac{1-z}{1+z},
$$
is a [[D-TM4TE|biholomorphism]], with inverse $\varphi^{-1}\colon\DD\to\HH_R$, $\varphi^{-1}(w)=\frac{1-w}{1+w}$.
:::

::: {.proof}
For $z\in\HH_R$ we have $1+z\neq0$, and
$$
\abs{1-z}^2-\abs{1+z}^2=-4\Re z<0,
$$
so $z$ is closer to $1$ than to $-1$ and $\abs{\varphi(z)}<1$.
Hence $\varphi$ is a [[D-E7A5W|holomorphic]] map $\HH_R\to\DD$.
The same map is the composite of the rotation $z\mapsto iz$, which maps $\HH_R$ onto the upper half-plane $\HH=\ts{u\in\CC\st\Im u>0}$, with the Cayley map $u\mapsto\frac{i-u}{i+u}$ from $\HH$ onto $\DD$:
$$
\frac{i-iz}{i+iz}=\frac{1-z}{1+z}.
$$

For $w\in\DD$ we have $w\neq-1$, so $\psi(w)\coloneqq\frac{1-w}{1+w}$ is holomorphic on $\DD$, and
$$
\Re\psi(w)=\frac{\Re\big((1-w)(1+\bar w)\big)}{\abs{1+w}^2}=\frac{1-\abs{w}^2}{\abs{1+w}^2}>0,
$$
so $\psi$ maps $\DD$ into $\HH_R$.
If $w=\varphi(z)$, then $w+wz=1-z$, so $z(1+w)=1-w$ and $z=\psi(w)$; thus $\psi\circ\varphi=\id_{\HH_R}$.
The same computation with the roles of $z$ and $w$ exchanged gives $\varphi\circ\psi=\id_{\DD}$.
:::

::: {.remark}
The formula $\frac{1-z}{1+z}$ also maps the imaginary axis into the unit circle: for $t\in\RR$, the numbers $1-it$ and $1+it$ are complex conjugates, so $\abs{\frac{1-it}{1+it}}=1$.
:::
