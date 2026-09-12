---
schema: qual/card@1
id: P-TLNGT
kind: problem
title: Residue evaluations of seven real and contour integrals
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Contour Integration
  - Integrals
relations: []
review: draft
---

::: problem
Compute the following integrals.

\(i\) $\displaystyle \int_0^\infty \frac{1}{(1 + x^n)^2} \, dx$, $n \geq 1$ (ii) $\displaystyle \int_0^\infty \frac{\cos x}{(x^2 + a^2)^2} \, dx$, $a \in \mathbb R$ (iii) $\displaystyle \int_0^\pi \frac{1}{a + \sin \theta} \, d \theta$, $a>1$

\(iv\) $\displaystyle \int_0^{\frac{\pi}{2}}
\frac{d \theta}{a+ \sin ^2 \theta},$ $a >0$.
(v) $\displaystyle \int_{|z|=2} \frac{1}{(z^{5} -1) (z-3)} \, dz$ (v) $\displaystyle \int_{- \infty}^{\infty} \frac{\sin \pi a}{\cosh \pi x + \cos \pi a} e^{- i x \xi} \, d x$, $0< a <1$, $\xi \in \mathbb R$ (vi) $\displaystyle \int_{|z| = 1} \cot^2 z \, dz$.
:::

::: solution
Reading the seven displayed integrals in order, their values are as follows.

For the first integral, when $n>1$ the substitution $u=x^n$ gives
\[
\int_0^\infty\frac{dx}{(1+x^n)^2}
=\frac1n B\left(\frac1n,2-\frac1n\right)
=\boxed{\frac{\pi(n-1)}{n^2}\csc\frac\pi n}.
\]
For $n=1$ its value is $1$.

For the second integral, if $a=0$ it diverges. For $a\ne0$, writing
$A=|a|$ and differentiating
\[
\int_0^\infty\frac{\cos x}{x^2+A^2}\,dx
=\frac{\pi}{2A}e^{-A}
\]
with respect to $A$ gives
\[
\boxed{
\int_0^\infty\frac{\cos x}{(x^2+a^2)^2}\,dx
=\frac{\pi e^{-|a|}(|a|+1)}{4|a|^3}.}
\]

For the third integral, $t=\tan(\theta/2)$ gives
\[
2\int_0^\infty\frac{dt}{at^2+2t+a},
\]
so for $a>1$,
\[
\boxed{
\int_0^\pi\frac{d\theta}{a+\sin\theta}
=\frac{2}{\sqrt{a^2-1}}\arctan\sqrt{a^2-1}.}
\]

For the fourth integral, $t=\tan\theta$ gives
\[
\boxed{
\int_0^{\pi/2}\frac{d\theta}{a+\sin^2\theta}
=\frac{\pi}{2\sqrt{a(a+1)}}.}
\]

For the fifth integral, all five roots of $z^5-1$ lie inside $|z|=2$, while
$z=3$ lies outside. Since the residue at infinity of
\[
F(z)=\frac1{(z^5-1)(z-3)}
\]
is zero and
\[
\operatorname{Res}(F;3)=\frac1{242},
\]
the sum of residues inside the contour is $-1/242$. Hence
\[
\boxed{
\int_{|z|=2}\frac{dz}{(z^5-1)(z-3)}=-\frac{\pi i}{121}.}
\]

For the sixth integral, a rectangular contour of height $2\pi i$ applied to
\[
\frac{e^{-ikz}}{\cosh z+\cos(\pi a)},
\qquad k=\frac\xi\pi,
\]
gives, for $\xi\ne0$,
\[
\boxed{
\int_{-\infty}^{\infty}
\frac{\sin(\pi a)e^{-ix\xi}}
{\cosh(\pi x)+\cos(\pi a)}\,dx
=\frac{2\sinh(a\xi)}{\sinh\xi}.}
\]
At $\xi=0$, the continuous limiting value is $2a$.

Finally,
\[
\cot z=\frac1z-\frac z3+O(z^3),
\]
so
\[
\cot^2z=\frac1{z^2}-\frac23+O(z^2).
\]
The only pole inside $|z|=1$ is $0$, and its residue is zero. Thus
\[
\boxed{\int_{|z|=1}\cot^2z\,dz=0.}
\]
:::
