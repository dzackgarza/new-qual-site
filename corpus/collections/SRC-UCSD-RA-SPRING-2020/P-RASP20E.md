---
schema: qual/card@1
id: P-RASP20E
kind: problem
title: "Absolute convergence of Fourier series of C^1 function"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Problem 5 of the official UCSD Spring 2020 real-analysis qualifying exam, with the source torus normalization on [0,1].
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Let $f \in C^1(\mathbb{T})$.
Let $\hat{f}(k)$ ($k \in \mathbb{Z}$) be the Fourier coefficients of $f$.
Prove that
$$
\sum_{k=-\infty}^{\infty} |\hat{f}(k)| \leq \|f\|_{L^1(\mathbb{T})} + \frac{1}{\sqrt{2}\pi}\|f'\|_{L^2(\mathbb{T})} \sqrt{\sum_{k=1}^{\infty} \frac{1}{k^2}}.
$$
:::


::: solution
<1>1. Control the zero Fourier mode.
::: proof
With
\[
\widehat f(k)=\int_0^1 f(x)e^{-2\pi ikx}\,dx,
\]
we have
\[
|\widehat f(0)|
=\left|\int_0^1f(x)\,dx\right|
\le \|f\|_{L^1(\mathbb T)}.
\]
:::

<1>2. Express the nonzero Fourier coefficients through \(f'\).
::: proof
For \(k\ne0\), periodicity of \(f\) and integration by parts give
\[
\widehat{f'}(k)
=2\pi i k\,\widehat f(k).
\]
Hence
\[
|\widehat f(k)|
=\frac{|\widehat{f'}(k)|}{2\pi|k|}.
\]
Therefore, by Cauchy--Schwarz,
\[
\begin{aligned}
\sum_{k\ne0}|\widehat f(k)|
&\le \frac1{2\pi}
\left(\sum_{k\ne0}|\widehat{f'}(k)|^2\right)^{1/2}
\left(\sum_{k\ne0}\frac1{k^2}\right)^{1/2}\\
&=\frac1{2\pi}
\left(\sum_{k\ne0}|\widehat{f'}(k)|^2\right)^{1/2}
\sqrt{2\sum_{k=1}^\infty\frac1{k^2}}.
\end{aligned}
\]
By Parseval,
\[
\sum_{k\in\mathbb Z}|\widehat{f'}(k)|^2
=\|f'\|_2^2.
\]
Thus
\[
\sum_{k\ne0}|\widehat f(k)|
\le
\frac1{\sqrt2\,\pi}\|f'\|_2
\sqrt{\sum_{k=1}^\infty\frac1{k^2}}.
\]
:::

<1>3. Combine the estimates.
::: proof
Adding the zero mode from Step 1 yields
\[
\boxed{
\sum_{k=-\infty}^\infty|\widehat f(k)|
\le \|f\|_1
+\frac1{\sqrt2\,\pi}\|f'\|_2
\sqrt{\sum_{k=1}^\infty\frac1{k^2}}.}
\]
In particular the Fourier series is absolutely convergent.
:::
:::
