---
schema: qual/card@1
id: P-HCAX5
kind: problem
title: Power series and radius of convergence of the tangent function
classification:
  areas:
  - complex-analysis
  topics:
  - Power Series
relations: []
review: draft
---

::: problem
a. Derive the power series of $\tan z$ at the origin.

b. Determine its radius of convergence.

c. Prove the location of the zeros of $\cos z$, and explain how they determine this radius.
:::

::: solution
Using the Bernoulli-number generating function
\[
\frac{t}{e^t-1}=\sum_{n=0}^{\infty}B_n\frac{t^n}{n!},
\]
one obtains
\[
\boxed{
\tan z
=\sum_{n=1}^{\infty}
(-1)^{n-1}
\frac{2^{2n}(2^{2n}-1)B_{2n}}{(2n)!}
z^{2n-1}.}
\]
Thus
\[
\tan z
=z+\frac{z^3}{3}+\frac{2z^5}{15}
+\frac{17z^7}{315}+\cdots.
\]
For example, the formula follows from
\[
\tan z=-i\frac{e^{2iz}-1}{e^{2iz}+1}
=-i+\frac{2i}{e^{2iz}+1}
\]
together with the Bernoulli expansion for $t/(e^t-1)$ applied after the standard identity
\[
\frac{2}{e^t+1}
=\frac{2}{e^t-1}-\frac{4}{e^{2t}-1}.
\]

To locate the singularities, write $z=x+iy$. If $\cos z=0$, then
\[
e^{iz}+e^{-iz}=0,
\qquad	ext{so}\qquad
e^{2iz}=-1.
\]
Taking absolute values gives $e^{-2y}=1$, hence $y=0$. Therefore
\[
e^{2ix}=-1,
\]
so
\[
\boxed{z=\frac\pi2+k\pi,
\qquad k\in\mathbb Z.}
\]
Conversely these points are plainly zeros of $\cos z$. They are simple because
\[
-\sin\left(\frac\pi2+k\pi\right)\ne0,
\]
and therefore they are simple poles of $\tan z$.

The nearest poles to the origin are at $\pm\pi/2$. Hence $\tan z$ is holomorphic on
\[
|z|<\frac\pi2,
\]
so its Taylor series at $0$ has radius at least $\pi/2$. It cannot have larger radius, because a larger Taylor disk would give a holomorphic continuation across $z=\pi/2$, where $\tan z$ has a genuine pole. Thus the radius of convergence is
\[
\boxed{R=\frac\pi2.}
\]
:::
