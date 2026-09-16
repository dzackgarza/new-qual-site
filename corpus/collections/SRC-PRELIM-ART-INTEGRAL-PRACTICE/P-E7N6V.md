---
schema: qual/card@1
id: P-E7N6V
kind: problem
title: Infinite nested-radical antiderivative and several trigonometric definite integrals
classification:
  areas:
  - prelim
  topics:
  - Integrals
  - Improper Integrals
  - u-Substitution
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
Evaluate or justify the following:

1. For \(x>0\), the infinite nested radical
\[
R(x)=\sqrt{x\sqrt[3]{x\sqrt[4]{x\sqrt[5]{x\cdots}}}}
\]
and an antiderivative of \(R(x)\).
2. \(\displaystyle \int_0^1\frac{\sin(\log x)}{\log x}\,dx\).
3. \(\displaystyle \int_{-\infty}^{\infty}\frac{\sin^2x}{x^2}\,dx\).
4. \(\displaystyle \lim_{n\to\infty}\int_0^1\frac{x^n}{1+x}\,dx\).
5. \(\displaystyle \int_0^\infty \frac{\sin x}{x e^{\sqrt3x}}\,dx\).
6. \(\displaystyle \int_{-\infty}^{\infty}\frac{\cos x}{1+x^2}\,dx\).
7. \(\displaystyle \int\sqrt{\frac{1+x}{1-x}}\,dx\) for \(-1<x<1\).
:::

::: {.solution}
<1>1. Evaluate the infinite nested radical.
::: {.proof}
Truncate after the \(N\)-th root and write the result as \(R_N(x)=x^{a_{2,N}}\). If the exponent at the \(k\)-th level is \(a_{k,N}\), then
\[
a_{N,N}=\frac1N,
\qquad
a_{k,N}=\frac{1+a_{k+1,N}}k.
\]
Unrolling gives
\[
a_{2,N}=\frac1{2!}+\frac1{3!}+\cdots+\frac1{N!}.
\]
Hence
\[
a_{2,N}\longrightarrow e-2,
\]
so for \(x>0\),
\[
R(x)=x^{e-2}.
\]
Therefore
\[
\boxed{\int R(x)\,dx=\frac{x^{e-1}}{e-1}+C.}
\]
:::

<1>2. Evaluate the logarithmic sine integral.
::: {.proof}
Put \(t=-\log x\). Then \(x=e^{-t}\), \(dx=-e^{-t}dt\), and
\[
\int_0^1\frac{\sin(\log x)}{\log x}\,dx
=\int_0^\infty e^{-t}\frac{\sin t}{t}\,dt.
\]
For \(a>0\), define
\[
F(b)=\int_0^\infty e^{-at}\frac{\sin(bt)}t\,dt.
\]
Differentiation under the integral gives
\[
F'(b)=\int_0^\infty e^{-at}\cos(bt)\,dt=\frac{a}{a^2+b^2},
\]
and \(F(0)=0\). Thus \(F(b)=\arctan(b/a)\). Taking \(a=b=1\),
\[
\boxed{\int_0^1\frac{\sin(\log x)}{\log x}\,dx=\frac\pi4.}
\]
:::

<1>3. Evaluate the squared-sinc integral.
::: {.proof}
Use the Fourier transform \(\widehat f(\xi)=\int_{\mathbb R}f(t)e^{-it\xi}\,dt\). For \(f=\mathbf1_{[-1,1]}\),
\[
\widehat f(\xi)=\frac{2\sin\xi}{\xi}.
\]
Plancherel's theorem in this normalization gives
\[
\int_{\mathbb R}|\widehat f(\xi)|^2\,d\xi
=2\pi\int_{\mathbb R}|f(t)|^2\,dt=4\pi.
\]
Therefore
\[
4\int_{-\infty}^{\infty}\frac{\sin^2\xi}{\xi^2}\,d\xi=4\pi,
\]
so
\[
\boxed{\int_{-\infty}^{\infty}\frac{\sin^2x}{x^2}\,dx=\pi.}
\]
:::

<1>4. Pass the limit through the integral.
::: {.proof}
For \(x\in[0,1)\), \(x^n/(1+x)\to0\), while
\[
0\le\frac{x^n}{1+x}\le1.
\]
Dominated convergence therefore gives
\[
\boxed{\lim_{n\to\infty}\int_0^1\frac{x^n}{1+x}\,dx=0.}
\]
:::

<1>5. Evaluate the exponentially damped sine integral.
::: {.proof}
The calculation in Step 2 gives, for \(a>0\),
\[
\int_0^\infty e^{-ax}\frac{\sin x}{x}\,dx=\arctan\frac1a.
\]
With \(a=\sqrt3\),
\[
\boxed{\int_0^\infty\frac{\sin x}{xe^{\sqrt3x}}\,dx
=\arctan\frac1{\sqrt3}=\frac\pi6.}
\]
:::

<1>6. Evaluate the Cauchy-kernel cosine transform.
::: {.proof}
Integrate
\[
\frac{e^{iz}}{1+z^2}
\]
over the upper semicircle of radius \(R>1\). The only enclosed pole is \(z=i\), with residue
\[
\operatorname*{Res}_{z=i}\frac{e^{iz}}{1+z^2}
=\frac{e^{-1}}{2i}.
\]
The residue theorem gives a contour integral tending to \(\pi/e\). The semicircular contribution tends to \(0\): away from the endpoints the factor \(e^{-\operatorname{Im}z}\) gives exponential decay, and the two endpoint pieces are \(O(R^{-1})\). Hence
\[
\int_{-\infty}^{\infty}\frac{e^{ix}}{1+x^2}\,dx=\frac\pi e.
\]
Taking real parts yields
\[
\boxed{\int_{-\infty}^{\infty}\frac{\cos x}{1+x^2}\,dx=\frac\pi e.}
\]
:::

<1>7. Integrate the square-root quotient.
::: {.proof}
Put \(x=\cos\theta\), where \(0<\theta<\pi\). Then
\[
\sqrt{\frac{1+x}{1-x}}
=\sqrt{\frac{1+\cos\theta}{1-\cos\theta}}
=\cot\frac\theta2,
\qquad
dx=-\sin\theta\,d\theta.
\]
Thus
\[
\sqrt{\frac{1+x}{1-x}}\,dx
=-(1+\cos\theta)\,d\theta.
\]
Consequently
\[
\int\sqrt{\frac{1+x}{1-x}}\,dx
=-\theta-\sin\theta+C.
\]
Since \(-\arccos x=\arcsin x-\pi/2\) and \(\sin\theta=\sqrt{1-x^2}\), the constant absorbs \(-\pi/2\), giving
\[
\boxed{\int\sqrt{\frac{1+x}{1-x}}\,dx
=\arcsin x-\sqrt{1-x^2}+C.}
\]
:::
:::
