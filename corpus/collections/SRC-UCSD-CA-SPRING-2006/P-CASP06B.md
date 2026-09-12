---
schema: qual/card@1
id: P-CASP06B
kind: problem
title: "Subharmonic function growth estimate and Liouville-type theorem"
classification:
  areas:
  - complex-analysis
  topics:
  - Harmonic Functions
relations: []
review: draft
---

::: problem
Suppose that $u$ is a $C^2$ subharmonic function on the whole complex plane.

(a) Prove that for any positive $R_1$ and $R_2$ with $R_2 > R_1$, $$\int_0^{2\pi} \left(u(R_2 e^{i\theta}) - u(R_1 e^{i\theta})\right)d\theta \geq \int_{R_1 \leq |z| \leq R_2} \log\left(\frac{R_2}{|z|}\right) \Delta u \, dx\,dy.$$

(b) Show that if $u$ satisfies $\lim_{z \to \infty} \frac{u(z)}{\log|z|} = 0$, then $u$ must be a constant.
:::

::: solution
Let
\[
M(r)=\int_0^{2\pi}u(re^{i\theta})\,d\theta.
\]
Green's theorem gives
\[
rM'(r)=\int_{|z|\le r}\Delta u\,dA(z).
\]
Since $u$ is subharmonic, $\Delta u\ge0$. Therefore
\[
\begin{aligned}
M(R_2)-M(R_1)
&=\int_{R_1}^{R_2}\frac1r
   \left(\int_{|z|\le r}\Delta u(z)\,dA(z)\right)dr\\
&\ge
\int_{R_1\le |z|\le R_2}
\left(\int_{|z|}^{R_2}\frac{dr}{r}\right)
\Delta u(z)\,dA(z)\\
&=\int_{R_1\le |z|\le R_2}
\log\frac{R_2}{|z|}\,\Delta u(z)\,dA(z),
\end{aligned}
\]
which is (a).

For (b), fix $0<R_1<R$. Applying (a) with $R_2>T>R$ gives
\[
M(T)-M(R_1)
\ge \log(T/R)
\int_{R_1\le|z|\le R}\Delta u\,dA.
\]
The hypothesis implies $M(T)=o(\log T)$ as $T\to\infty$. Dividing by
$\log T$ and letting $T\to\infty$ yields
\[
\int_{R_1\le|z|\le R}\Delta u\,dA=0.
\]
Since $R_1,R$ are arbitrary and $\Delta u\ge0$ is continuous, we get
$\Delta u\equiv0$. Thus $u$ is harmonic on $\mathbb C$.

The same growth hypothesis gives $|u(z)|=o(\log|z|)$ at infinity. Standard
gradient estimates for harmonic functions on disks yield, for fixed $a$,
\[
|\nabla u(a)|
\le \frac{C}{R}\sup_{|z-a|\le R}|u(z)|
=o\!\left(\frac{\log R}{R}\right),
\]
as $R\to\infty$. Hence $\nabla u(a)=0$ for every $a$, so $u$ is constant.
:::
