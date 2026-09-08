---
schema: qual/card@1
id: P-RAF07E
kind: problem
title: "Tempered distribution e^{iax} and its Fourier transform"
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
  date: 2026-09-08
  note: Checked against Problem 5 of the official UCSD Fall 2007 real-analysis qualifying exam. The solution uses the unitary Fourier normalization used elsewhere in the UCSD real-analysis corpus.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
For $a \in \mathbb{R}$, let $f_a$ be the function on $\mathbb{R}$ defined by $f_a(x) := e^{iax}$.

(a) Show that $f_a$ is a tempered distribution on $\mathbb{R}$.

(b) Find the Fourier transform of $f_a$.
:::


::: solution
<1>1. Show that $f_a$ defines a tempered distribution.
::: proof
For $\varphi\in\mathcal S(\mathbb R)$ define
\[
\langle T_a,\varphi\rangle
:=\int_{\mathbb R}e^{iax}\varphi(x)\,dx.
\]
Since $|e^{iax}|=1$,
\[
|\langle T_a,\varphi\rangle|
\le \int_{\mathbb R}|\varphi(x)|\,dx.
\]
For example,
\[
\int_{\mathbb R}|\varphi(x)|\,dx
\le
\left(\int_{\mathbb R}(1+x^2)^{-1}\,dx\right)
\sup_{x\in\mathbb R}(1+x^2)|\varphi(x)|.
\]
Thus $T_a$ is a continuous linear functional on the Schwartz space. Therefore $f_a=e^{iax}$ defines a tempered distribution.
:::

<1>2. Compute its Fourier transform.
::: proof
Use the UCSD unitary convention
\[
\widehat\varphi(\xi)
=\frac1{\sqrt{2\pi}}\int_{\mathbb R}e^{-ix\xi}\varphi(x)\,dx,
\]
with Fourier transform of tempered distributions defined by
\[
\langle\widehat T,\varphi\rangle
=\langle T,\widehat\varphi\rangle.
\]
Then for $\varphi\in\mathcal S(\mathbb R)$,
\[
\begin{aligned}
\langle\widehat{T_a},\varphi\rangle
&=\langle T_a,\widehat\varphi\rangle\\
&=\int_{\mathbb R}e^{iax}\widehat\varphi(x)\,dx.
\end{aligned}
\]
By Fourier inversion,
\[
\varphi(a)
=\frac1{\sqrt{2\pi}}
\int_{\mathbb R}e^{iax}\widehat\varphi(x)\,dx.
\]
Hence
\[
\langle\widehat{T_a},\varphi\rangle
=\sqrt{2\pi}\,\varphi(a)
=\langle\sqrt{2\pi}\,\delta_a,\varphi\rangle.
\]
Therefore
\[
\boxed{
\widehat{e^{iax}}=\sqrt{2\pi}\,\delta_a.}
\]
:::
:::
