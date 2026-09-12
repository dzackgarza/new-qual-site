---
schema: qual/card@1
id: P-RASP13F
kind: problem
title: "Solving -Delta u + u = f via Fourier transform and the heat kernel representation"
classification:
  areas:
  - real-analysis
  topics:
  - Fourier Transform
  - Partial Differential Equations
  - Heat Kernel
  - Distributions
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 6 of the official UCSD Spring 2013 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
The problem concerns finding an explicit solution to the equation $-\Delta u + u = f$ for $f \in C_c^\infty(\mathbb{R}^n)$, using the Fourier transform.

(a) Assume that the solution $u$ and all its first-order and second-order partial derivatives are in $L^1(\mathbb{R}^n) \cap L^2(\mathbb{R}^n)$.
Prove
$$
\hat{u}(z) = \frac{\hat{f}(z)}{1 + 4\pi^2 |z|^2}.
$$

(b) Prove, via the identity $(1 + 4\pi^2 |z|^2)^{-1} = \int_0^\infty e^{-t(1+4\pi^2|z|^2)} \, dt$, that
$$
u(x) = \int_0^\infty \frac{e^{-t}}{(4\pi t)^{n/2}} \int_{\mathbb{R}^n} e^{-\frac{|x-y|^2}{4t}} f(y) \, dm(y) \, dt.
$$
:::

::: solution
<1>1. Fourier transform the equation.
::: proof
Use the convention
\[
\widehat v(z)=\int_{\mathbb R^n}e^{-2\pi i x\cdot z}v(x)\,dx.
\]
Under the stated $L^1$ hypotheses on $u$ and its first and second derivatives,
\[
\widehat{\partial_j u}(z)=2\pi i z_j\widehat u(z),
\qquad
\widehat{\partial_j^2u}(z)=-4\pi^2z_j^2\widehat u(z).
\]
Therefore
\[
\widehat{-\Delta u+u}(z)
=\bigl(1+4\pi^2|z|^2\bigr)\widehat u(z).
\]
Since $-\Delta u+u=f$,
\[
\bigl(1+4\pi^2|z|^2\bigr)\widehat u(z)=\widehat f(z),
\]
and hence
\[
\boxed{\widehat u(z)=\frac{\widehat f(z)}{1+4\pi^2|z|^2}.}
\]
:::

<1>2. Express the multiplier by Gaussian multipliers.
::: proof
For every $z$,
\[
\frac1{1+4\pi^2|z|^2}
=\int_0^\infty e^{-t}e^{-4\pi^2t|z|^2}\,dt.
\]
Set
\[
H_t(x)=\frac1{(4\pi t)^{n/2}}e^{-|x|^2/(4t)}.
\]
Then $\|H_t\|_1=1$ and, for the same Fourier convention,
\[
\widehat{H_t}(z)=e^{-4\pi^2t|z|^2}.
\]
Thus
\[
e^{-4\pi^2t|z|^2}\widehat f(z)
=\widehat{H_t*f}(z).
\]
:::

<1>3. Integrate the heat kernels and invert the transform.
::: proof
Define
\[
v(x)=\int_0^\infty e^{-t}(H_t*f)(x)\,dt.
\]
Young's inequality gives
\[
\int_0^\infty e^{-t}\|H_t*f\|_1\,dt
\le \|f\|_1\int_0^\infty e^{-t}\,dt
=\|f\|_1.
\]
Hence $v\in L^1$, and Fubini permits taking its Fourier transform under the $t$-integral:
\[
\begin{aligned}
\widehat v(z)
&=\int_0^\infty e^{-t}\widehat{H_t*f}(z)\,dt\\
&=\widehat f(z)\int_0^\infty e^{-t}e^{-4\pi^2t|z|^2}\,dt\\
&=\frac{\widehat f(z)}{1+4\pi^2|z|^2}.
\end{aligned}
\]
By Step 1, $\widehat v=\widehat u$. Fourier-transform uniqueness on $L^1$ gives $u=v$ almost everywhere. Expanding the convolution yields
\[
\boxed{
u(x)=\int_0^\infty\frac{e^{-t}}{(4\pi t)^{n/2}}
\int_{\mathbb R^n}e^{-|x-y|^2/(4t)}f(y)\,dy\,dt.}
\]
The right-hand side is the natural continuous representative of the solution.
:::
:::
