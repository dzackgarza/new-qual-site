---
schema: qual/card@1
id: P-SWLWB
kind: problem
title: $\int_0^\infty\frac{dx}{(1+x^n)^2}$, $\int_0^\infty\frac{\cos x}{(x^2+a^2)^2}\,dx$,
  $\int_0^\pi\frac{d\theta}{a+\sin\theta}$, $\int_0^{\pi/2}\frac{d\theta}{a+\sin^2\theta}$,
  $\int_{|z|=2}\frac{dz}{(z^5-1)(z-3)}$, $\int_{-\infty}^{\infty}\frac{\sin(\pi a)\,e^{-ix\xi}}{\cosh(\pi
  x)+\cos(\pi a)}\,dx$, and $\int_{|z|=1}\cot^2 z\,dz$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Contour Integration
  - Integrals
  - Trigonometry
relations: []
review: draft
---

::: {.problem}
Compute the following integrals.

(i) $\displaystyle \int_0^\infty \frac{1}{(1 + x^n)^2} \, dx$, $n \geq 1$

(ii) $\displaystyle \int_0^\infty \frac{\cos x}{(x^2 + a^2)^2} \, dx$, $a \in \mathbb R$

(iii) $\displaystyle \int_0^\pi \frac{1}{a + \sin \theta} \, d \theta$, $a>1$

(iv) $\displaystyle \int_0^{\frac{\pi}{2}} \frac{d \theta}{a+ \sin ^2 \theta},$ $a >0$.

(v) $\displaystyle \int_{|z|=2} \frac{1}{(z^{5} -1) (z-3)} \, dz$

(vi) $\displaystyle \int_{- \infty}^{\infty} \frac{\sin \pi a}{\cosh \pi x + \cos \pi a} e^{- i x \xi} \, d x$, $0< a <1$, $\xi \in \mathbb R$

(vii) $\displaystyle \int_{|z| = 1} \cot^2 z \, dz$.
:::

::: {.solution}
We evaluate the seven integrals in order.

For **(i)**, first assume $n>1$ and put $u=x^n$. Then
\[
\int_0^\infty\frac{dx}{(1+x^n)^2}
=\frac1n\int_0^\infty\frac{u^{1/n-1}}{(1+u)^2}\,du
=\frac1n B\left(\frac1n,2-\frac1n\right).
\]
Using $B(p,q)=\Gamma(p)\Gamma(q)/\Gamma(p+q)$, the recurrence for $\Gamma$,
and Euler's reflection formula,
\[
\boxed{
\int_0^\infty\frac{dx}{(1+x^n)^2}
=\frac{\pi(n-1)}{n^2}\csc\frac\pi n,
\qquad n>1.}
\]
For $n=1$ the integral is directly
\[
\int_0^\infty\frac{dx}{(1+x)^2}=1.
\]

For **(ii)**, if $a=0$ the integral diverges at $0$. If $a\ne0$, put
$A=|a|$. The standard residue computation gives
\[
I(A):=\int_0^\infty\frac{\cos x}{x^2+A^2}\,dx
=\frac{\pi}{2A}e^{-A}.
\]
Differentiating with respect to $A$,
\[
I'(A)=-2A\int_0^\infty\frac{\cos x}{(x^2+A^2)^2}\,dx.
\]
Therefore
\[
\boxed{
\int_0^\infty\frac{\cos x}{(x^2+a^2)^2}\,dx
=\frac{\pi e^{-|a|}(|a|+1)}{4|a|^3},
\qquad a\ne0.}
\]

For **(iii)**, use $t=\tan(\theta/2)$. Then
$\sin\theta=2t/(1+t^2)$ and $d\theta=2\,dt/(1+t^2)$, so
\[
\int_0^\pi\frac{d\theta}{a+\sin\theta}
=2\int_0^\infty\frac{dt}{at^2+2t+a}.
\]
Writing $\Delta=a^2-1>0$ and completing the square gives
\[
\boxed{
\int_0^\pi\frac{d\theta}{a+\sin\theta}
=\frac{2}{\sqrt{a^2-1}}
\arctan\sqrt{a^2-1},
\qquad a>1.}
\]

For **(iv)**, set $t=\tan\theta$. Since
$\sin^2\theta=t^2/(1+t^2)$ and $d\theta=dt/(1+t^2)$,
\[
\int_0^{\pi/2}\frac{d\theta}{a+\sin^2\theta}
=\int_0^\infty\frac{dt}{a+(a+1)t^2}
=\boxed{\frac{\pi}{2\sqrt{a(a+1)}}}.
\]

For **(v)**, the contour $|z|=2$ encloses all five roots of $z^5-1$ and
excludes $z=3$. Since
\[
F(z)=\frac1{(z^5-1)(z-3)}=O(z^{-6}),
\]
the residue at infinity is $0$, so the sum of all finite residues is $0$.
The residue at $z=3$ is
\[
\operatorname{Res}(F;3)=\frac1{3^5-1}=\frac1{242}.
\]
Thus the sum of the residues inside $|z|=2$ is $-1/242$, and
\[
\boxed{
\int_{|z|=2}\frac{dz}{(z^5-1)(z-3)}
=-\frac{\pi i}{121}.}
\]

For **(vi)**, put $A=\pi a$ and scale $y=\pi x$. It is enough to evaluate
\[
J(k)=\int_{-\infty}^{\infty}
\frac{e^{-iky}}{\cosh y+\cos A}\,dy,
\qquad k=\frac\xi\pi.
\]
Assume first $k>0$ and integrate
\[
F(z)=\frac{e^{-ikz}}{\cosh z+\cos A}
\]
over the rectangle with vertices $-R,R,R-2\pi i,-R-2\pi i$, oriented
clockwise. The vertical sides vanish as $R\to\infty$. Because the denominator
is $2\pi i$-periodic, the lower horizontal side contributes
$-e^{-2\pi k}J(k)$. The poles in the strip $-2\pi<\Im z<0$ are
\[
z_1=-i(\pi-A),
\qquad
z_2=-i(\pi+A).
\]
Their residue sum is
\[
\frac{2i e^{-\pi k}\sinh(Ak)}{\sin A}.
\]
The clockwise residue theorem therefore gives
\[
(1-e^{-2\pi k})J(k)
=\frac{4\pi e^{-\pi k}\sinh(Ak)}{\sin A},
\]
and hence
\[
J(k)=\frac{2\pi}{\sin A}\frac{\sinh(Ak)}{\sinh(\pi k)}.
\]
The same formula holds for $k<0$ by evenness, and its limit at $k=0$ is
$2A/\sin A$. Restoring the scale and the factor $\sin(\pi a)$ gives
\[
\boxed{
\int_{-\infty}^{\infty}
\frac{\sin(\pi a)e^{-ix\xi}}{\cosh(\pi x)+\cos(\pi a)}\,dx
=\frac{2\sinh(a\xi)}{\sinh\xi}}
\]
for $\xi\ne0$, with limiting value $2a$ at $\xi=0$.

For **(vii)**, the only pole of $\cot^2z$ inside $|z|=1$ is at $0$. Since
\[
\cot z=\frac1z-\frac z3+O(z^3),
\]
we have
\[
\cot^2z=\frac1{z^2}-\frac23+O(z^2),
\]
whose residue at $0$ is $0$. Therefore
\[
\boxed{\int_{|z|=1}\cot^2z\,dz=0.}
\]
:::
