---
schema: qual/card@1
id: PR-PW4Z6
kind: proposition
title: Möbius map from the upper half-disc to the first quadrant
slogan: 'The Möbius map $(1+z)/(1-z)$ sends the upper half-disc biholomorphically onto the first quadrant.'
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
f\colon\theset{z\st\abs{z}<1,\ \Im z>0}\to\theset{w\st\Re w>0,\ \Im w>0},\qquad f(z)=\frac{1+z}{1-z},
$$
is a [[D-TM4TE|biholomorphism]] from the upper half-disc onto the first quadrant, with inverse $f^{-1}(w)=\frac{w-1}{w+1}$.
:::

::: {.remark}
On the upper unit semicircle, for $z=e^{i\theta}$ with $0<\theta<\pi$,
$$
f(e^{i\theta})=\frac{e^{-i\theta/2}+e^{i\theta/2}}{e^{-i\theta/2}-e^{i\theta/2}}=\frac{2\cos(\theta/2)}{-2i\sin(\theta/2)}=i\cot(\theta/2),
$$
so as $\theta$ increases from $0$ to $\pi$, $f(e^{i\theta})$ moves from $i\infty$ to $0$ along the positive imaginary axis.
As $x$ increases from $-1$ to $1$, $f(x)=\frac{1+x}{1-x}$ increases from $0$ to $\infty$ along the positive real axis, with $f(0)=1$.
:::
