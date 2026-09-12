---
schema: qual/card@1
id: P-RAF24F
kind: problem
title: Absolute summability of Fourier coefficients controlled by $L^1$ and $L^p$ derivative
classification:
  areas:
  - real-analysis
  topics:
  - Fourier Analysis
  - Integrals
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 6 of the official UCSD Fall 2024 real-analysis qualifying exam, using the standard Fourier-series convention \hat f(k)=\int_{\mathbb T}f(x)e^{-2\pi i kx}\,dx.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Show that for any $p > 1$, there is a constant $C_p < \infty$ such that
\[
\sum_{k=-\infty}^{\infty} |\hat{f}(k)| \le \|f\|_{L^1} + C_p \|f'\|_{L^p}
\quad\text{for each } f \in C^1(\mathbb{T}).
\]
:::

::: solution
<1>1. Separate the zero Fourier mode.
::: proof
For $k=0$,
\[
|\widehat f(0)|
=\left|\int_{\mathbb T}f(x)\,dx\right|
\le \|f\|_{L^1}.
\]
Thus it remains to control the sum over $k\ne0$.
:::

<1>2. Integrate by parts for the nonzero modes.
::: proof
Because $f\in C^1(\mathbb T)$ is periodic, integration by parts gives, for every $k\ne0$,
\[
\widehat{f'}(k)
=2\pi i k\,\widehat f(k).
\]
Hence
\[
|\widehat f(k)|
\le \frac1{2\pi|k|}\,|\widehat{f'}(k)|.
\]
Therefore
\[
\sum_{k\ne0}|\widehat f(k)|
\le \frac1{2\pi}
\sum_{k\ne0}\frac{|\widehat{f'}(k)|}{|k|}.
\]
:::

<1>3. Treat the range $1<p\le2$.
::: proof
Let $p'=p/(p-1)$. By Hölder's inequality for sequences,
\[
\sum_{k\ne0}\frac{|\widehat{f'}(k)|}{|k|}
\le
\left(\sum_{k\ne0}|k|^{-p}\right)^{1/p}
\left(\sum_{k\ne0}|\widehat{f'}(k)|^{p'}\right)^{1/p'}.
\]
Since $p>1$, the first series converges. By the Hausdorff--Young inequality,
\[
\|\widehat{f'}\|_{\ell^{p'}}
\le \|f'\|_{L^p}.
\]
Thus
\[
\sum_{k\ne0}|\widehat f(k)|
\le C_p\|f'\|_{L^p}.
\]
:::

<1>4. Treat the range $p\ge2$.
::: proof
Since $\mathbb T$ has finite measure,
\[
\|f'\|_{L^2}\le \|f'\|_{L^p}.
\]
By Cauchy--Schwarz and Plancherel,
\[
\begin{aligned}
\sum_{k\ne0}\frac{|\widehat{f'}(k)|}{|k|}
&\le
\left(\sum_{k\ne0}|k|^{-2}\right)^{1/2}
\left(\sum_{k\ne0}|\widehat{f'}(k)|^2\right)^{1/2}\\
&\le C\|f'\|_{L^2}
\le C\|f'\|_{L^p}.
\end{aligned}
\]
Hence the same estimate holds for every $p\ge2$.
:::

<1>5. Combine the estimates.
::: proof
Steps 1--4 give, for every $p>1$,
\[
\boxed{
\sum_{k\in\mathbb Z}|\widehat f(k)|
\le \|f\|_{L^1}+C_p\|f'\|_{L^p}.}
\]
The constant $C_p$ depends only on $p$ and the Fourier normalization.
:::
:::
