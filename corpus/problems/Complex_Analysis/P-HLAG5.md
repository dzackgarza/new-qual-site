---
schema: qual/card@1
id: P-HLAG5
kind: problem
title: Images of circles $|z|=r$ and rays $\arg z=\theta_0$ under $z+1/z$
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Geometry
relations: []
review: draft
---

::: {.problem}
Let $f(z)=z+1 / z$.
Describe the images of both the circle $|z|=r$ of radius $r(r \neq 0)$ and the ray $\arg z=\theta_{0}$ under $f$ in terms of well known curves.
:::

::: {.solution}
Write $z=re^{i\theta}$.

For the circle $|z|=r$,
\[
w=z+\frac1z
=\left(r+\frac1r\right)\cos\theta
+i\left(r-\frac1r\right)\sin\theta.
\]
Thus, for $r\ne1$, its image is the ellipse
\[
\boxed{
\frac{(\Re w)^2}{(r+r^{-1})^2}
+\frac{(\Im w)^2}{(r-r^{-1})^2}=1.}
\]
Its foci are at $\pm2$. When $r=1$, the ellipse degenerates to the segment
$[-2,2]$ on the real axis.

For the ray $\arg z=\theta_0$, write $z=\rho e^{i\theta_0}$ with $\rho>0$.
Then
\[
x=(\rho+\rho^{-1})\cos\theta_0,
\qquad
y=(\rho-\rho^{-1})\sin\theta_0.
\]
Since
\[
(\rho+\rho^{-1})^2-(\rho-\rho^{-1})^2=4,
\]
we obtain, when both sine and cosine are nonzero,
\[
\boxed{
\frac{x^2}{4\cos^2\theta_0}
-\frac{y^2}{4\sin^2\theta_0}=1.}
\]
Hence the image is one branch of a hyperbola with foci at $\pm2$.
For $\sin\theta_0=0$ it degenerates to a real ray outside $[-2,2]$; for
$\cos\theta_0=0$ it degenerates to the imaginary axis.
:::
