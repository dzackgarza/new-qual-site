---
schema: qual/card@1
id: T-WFXQP
kind: theorem
title: Residue at infinity
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Singularities
relations: []
review: draft
---

::: {.theorem}
Let $R>0$ and let $f$ be [[D-E7A5W|holomorphic]] on $\{z : \abs{z}>R\}$.
Define $g(z)\coloneqq-\dfrac{1}{z^2}f\Bigl(\dfrac1z\Bigr)$ for $0<\abs{z}<1/R$.
Then the residue of $f$ at $\infty$ is
$$
\Res_{z=\infty}f=\Res_{z=0}g=-\frac{1}{2\pi i}\int_{\abs{z}=\rho}f(z)\dz
$$
for every $\rho>R$, the circle $\abs{z}=\rho$ being oriented counterclockwise.
:::

::: {.remark}
Residues belong to the differential form $f(z)\dz$ rather than to the function $f$.
Under $w=1/z$ the form $f(z)\dz$ becomes $f(1/w)\,d(1/w)=-\frac{1}{w^2}f(1/w)\dw=g(w)\dw$, and the counterclockwise circle $\abs{z}=\rho$ becomes the clockwise circle $\abs{w}=1/\rho$, which accounts for the sign.
:::
