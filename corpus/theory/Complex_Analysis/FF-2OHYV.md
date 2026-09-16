---
schema: qual/card@1
id: FF-2OHYV
kind: fact
title: Rational parametrization of the unit circle
prompts:
- What is the standard rational parameterization of the circle in $\CC$?
classification:
  areas:
  - complex-analysis
  topics:
  - Trigonometry
  - Contour Integration
relations: []
review: draft
---

::: {.fact}
The map
$$
x\mapsto\frac{1-x^2}{1+x^2}+i\,\frac{2x}{1+x^2}=\frac{1+ix}{1-ix},\qquad x\in\RR,
$$
is a bijection from $\RR$ onto $S^1\setminus\{-1\}$.
Substituting $x=\tan t$ for $t\in\qty{-\frac{\pi}{2},\frac{\pi}{2}}$ gives
$$
F(t)\coloneqq\frac{1-x^2}{1+x^2}+i\,\frac{2x}{1+x^2}=\cos 2t+i\sin 2t=e^{2it}.
$$
:::

::: {.proof}
Since $(1+ix)(1-ix)=1+x^2$, we have $\frac{1+ix}{1-ix}=\frac{(1+ix)^2}{1+x^2}=\frac{1-x^2+2ix}{1+x^2}$, and its modulus is $\abs{1+ix}/\abs{1-ix}=1$.
For $t\in(-\pi/2,\pi/2)$ and $x=\tan t$, $1+x^2=\sec^2t$, so $\frac{1-x^2}{1+x^2}=\cos^2t-\sin^2t=\cos2t$ and $\frac{2x}{1+x^2}=2\sin t\cos t=\sin2t$.
As $t$ runs over $(-\pi/2,\pi/2)$, $x=\tan t$ runs bijectively over $\RR$ and $2t$ runs over $(-\pi,\pi)$, so $e^{2it}$ runs bijectively over $S^1\setminus\{-1\}$.
:::
