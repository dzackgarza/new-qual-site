---
schema: qual/card@1
id: PR-TQDIL
kind: proposition
title: Exponential map from a vertical half-strip to a half-disc
slogan: 'The exponential converts vertical height to radius and horizontal position to angle, sending the half-strip to the right half-disc.'
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
relations: []
review: draft
---

::: {.proposition}
The map
$$
F\colon\theset{z\st\abs{\Re z}<\tfrac\pi2,\ \Im z>0}\to\theset{w\st\abs{w}<1,\ \Re w>0},\qquad F(z)=e^{iz},
$$
is a [[D-TM4TE|biholomorphism]] from the vertical half-strip onto the right half-disc, with inverse $w\mapsto-i\Log w$, where $\Log$ is the [[D-4CSPM|principal branch]] of the logarithm.

This is the exponential correspondence of [@Ahl73, ch. 3, §4.1, The Use of Level Curves]: there $\zeta=e^z$ maps the strip $-\pi/2<\Im z<\pi/2$ onto $\Re\zeta>0$, with the lines $x=x_0$ going to circles about the origin and the lines $y=y_0$ to rays. The map above is that exponential read on the strip rotated by $\pi/2$ — writing $z_1=iz$ carries $\abs{\Re z}<\pi/2$, $\Im z>0$ onto $\Re z_1<0$, $\abs{\Im z_1}<\pi/2$ — so the image is the part of $\Re\zeta>0$ cut out by $\abs\zeta<1$, the right half-disc, and the inverse is the logarithm of that branch.
:::
