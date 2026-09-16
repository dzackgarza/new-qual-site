---
schema: qual/card@1
id: PR-PW4Z6
kind: proposition
title: Möbius map from the upper half-disc to the first quadrant
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
The map
$$
f\colon\ts{z\st\abs{z}<1,\ \Im z>0}\to\ts{w\st\Re w>0,\ \Im w>0},\qquad f(z)=\frac{1+z}{1-z},
$$
is a [[D-TM4TE|biholomorphism]] from the upper half-disc onto the first quadrant, with inverse $f^{-1}(w)=\frac{w-1}{w+1}$.
:::

::: {.proof}
For $z=x+iy$ with $x^2+y^2<1$ and $y>0$, multiplying numerator and denominator by $1-\bar z$ gives
$$
f(z)=\frac{(1+z)(1-\bar z)}{\abs{1-z}^2}=\frac{1-(x^2+y^2)}{(1-x)^2+y^2}+i\,\frac{2y}{(1-x)^2+y^2},
$$
and both parts are positive, so $f(z)$ lies in the first quadrant.

For $w=u+iv$ with $u,v>0$, the point $w$ is closer to $1$ than to $-1$ because $u>0$, so $\abs{\frac{w-1}{w+1}}<1$.
Moreover
$$
\frac{w-1}{w+1}=\frac{(u-1+iv)(u+1-iv)}{(u+1)^2+v^2}=\frac{u^2+v^2-1}{(u+1)^2+v^2}+i\,\frac{2v}{(u+1)^2+v^2},
$$
whose imaginary part is positive.
So $w\mapsto\frac{w-1}{w+1}$ maps the first quadrant into the upper half-disc, and solving $w=\frac{1+z}{1-z}$ for $z$ shows that the two maps are mutually inverse.
:::

::: {.remark}
On the upper unit semicircle, for $z=e^{i\theta}$ with $0<\theta<\pi$,
$$
f(e^{i\theta})=\frac{e^{-i\theta/2}+e^{i\theta/2}}{e^{-i\theta/2}-e^{i\theta/2}}=\frac{2\cos(\theta/2)}{-2i\sin(\theta/2)}=i\cot(\theta/2),
$$
so as $\theta$ increases from $0$ to $\pi$, $f(e^{i\theta})$ moves from $i\infty$ to $0$ along the positive imaginary axis.
As $x$ increases from $-1$ to $1$, $f(x)=\frac{1+x}{1-x}$ increases from $0$ to $\infty$ along the positive real axis, with $f(0)=1$.
:::
