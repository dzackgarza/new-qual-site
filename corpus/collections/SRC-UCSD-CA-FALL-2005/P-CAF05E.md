---
schema: qual/card@1
id: P-CAF05E
kind: problem
title: "Evaluation of the sinc integral via residue calculus"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: problem
Use the method of residues to compute the integral $\int_0^{\infty} \frac{\sin x}{x}\,dx$.
Justify all your steps.

Hint: Integrate the function $\frac{e^{iz}}{z}$ on an appropriate closed curve.
:::

::: solution
For $0<\varepsilon<R$, integrate
\[
F(z)=\frac{e^{iz}}z
\]
over the boundary of the upper half-disk of radius $R$ with the small upper
half-disk of radius $\varepsilon$ about the origin removed. The contour consists
of the real intervals $[-R,-\varepsilon]$ and $[\varepsilon,R]$, the large
upper semicircle, and the small upper semicircle traversed clockwise. Since the
origin is excluded, $F$ is holomorphic inside the contour, so the total
integral is $0$.

On the large semicircle $z=Re^{i\theta}$,
\[
\left|\int \frac{e^{iz}}z\,dz\right|
\le \int_0^\pi e^{-R\sin\theta}\,d\theta.
\]
Using $\sin\theta\ge 2\theta/\pi$ on $[0,\pi/2]$ and symmetry, the right-hand
side is at most $\pi/R$, hence tends to $0$.

On the small clockwise semicircle $z=\varepsilon e^{i\theta}$,
$\theta$ decreases from $\pi$ to $0$, and
\[
\int \frac{e^{iz}}z\,dz
=i\int_\pi^0 e^{i\varepsilon e^{i\theta}}\,d\theta
\longrightarrow -i\pi.
\]
Consequently,
\[
\operatorname{PV}\int_{-\infty}^{\infty}\frac{e^{ix}}x\,dx=i\pi.
\]
The real part vanishes by oddness of $\cos x/x$, while
$\sin x/x$ is even. Hence
\[
2i\int_0^\infty\frac{\sin x}{x}\,dx=i\pi,
\]
so
\[
\boxed{\displaystyle
\int_0^\infty\frac{\sin x}{x}\,dx=\frac\pi2.}
\]
The improper integral converges, for example by Dirichlet's test.
:::
