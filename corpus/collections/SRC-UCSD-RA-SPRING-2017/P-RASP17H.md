---
schema: qual/card@1
id: P-RASP17H
kind: problem
title: "Smoothness of the Fourier transform of a compactly supported L^2 function; Arzela-Ascoli extraction"
classification:
  areas:
  - real-analysis
  topics:
  - Fourier Transform
  - L2 Spaces
  - Arzela-Ascoli Theorem
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Problem 8 of the official UCSD Spring 2017 real-analysis qualifying exam, using the source Fourier normalization (2pi)^(-1/2).
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Suppose that $f \in L^2(\mathbb{R}, m)$ is a function such that $f(x) = 0$ if $|x| \geq 1$.

1. Show $\hat{f} \in C^\infty(\mathbb{R}, \mathbb{C})$ and
$$
\sup_{k \in \mathbb{R}} |\hat{f}^{(\ell)}(k)| \leq \frac{1}{\sqrt{2\pi}} \sqrt{\frac{2}{2\ell + 1}} \|f\|_2 \quad \forall \ell = 0, 1, 2, \ldots
$$

2. Let $\{f_n\}_{n=1}^\infty \subset L^2(\mathbb{R}, m)$ satisfy $\|f_n\|_2 \leq 1$ and $f_n(x) = 0$ for $|x| \geq 1$.
   Show that for each $0 < M < \infty$ there exists $1 \leq n_1 < n_2 < n_3 < \ldots$ in $\mathbb{N}$ such that $\{\hat{f}_{n_k}\}_{k=1}^\infty$ is uniformly convergent on $[-M, M]$ to some $g \in C([-M, M], \mathbb{C})$.
:::


::: solution
<1>1. Differentiate the Fourier transform under the integral sign.
::: proof
With the source normalization,
\[
\widehat f(k)=\frac1{\sqrt{2\pi}}\int_{\mathbb R}f(x)e^{-ikx}\,dx.
\]
Since \(f\) vanishes outside \([-1,1]\), Cauchy--Schwarz gives \(f\in L^1\). More generally, for every integer \(\ell\ge0\),
\[
x^\ell f(x)\in L^1(\mathbb R).
\]
Therefore differentiation under the integral sign is justified for every order and yields
\[
\widehat f^{(\ell)}(k)
=\frac1{\sqrt{2\pi}}
\int_{-1}^1(-ix)^\ell f(x)e^{-ikx}\,dx.
\]
Hence \(\widehat f\in C^\infty(\mathbb R)\).
:::

<1>2. Prove the stated uniform derivative bound.
::: proof
By Cauchy--Schwarz,
\[
\begin{aligned}
|\widehat f^{(\ell)}(k)|
&\le \frac1{\sqrt{2\pi}}
\left(\int_{-1}^1|x|^{2\ell}\,dx\right)^{1/2}\|f\|_2\\
&=\frac1{\sqrt{2\pi}}
\sqrt{\frac{2}{2\ell+1}}\,\|f\|_2.
\end{aligned}
\]
The bound is independent of \(k\), so
\[
\boxed{
\sup_{k\in\mathbb R}|\widehat f^{(\ell)}(k)|
\le
\frac1{\sqrt{2\pi}}
\sqrt{\frac{2}{2\ell+1}}\,\|f\|_2.}
\]
:::

<1>3. Apply Arzelà--Ascoli to the sequence \((\widehat f_n)\).
::: proof
Assume \(\|f_n\|_2\le1\). Step 2 with \(\ell=0\) gives
\[
\sup_n\sup_{k\in\mathbb R}|\widehat f_n(k)|
\le \frac1{\sqrt\pi}.
\]
With \(\ell=1\),
\[
\sup_n\sup_{k\in\mathbb R}|\widehat f_n'(k)|
\le \frac1{\sqrt{3\pi}}.
\]
Thus for \(s,t\in[-M,M]\), the Mean Value Theorem gives
\[
|\widehat f_n(t)-\widehat f_n(s)|
\le \frac1{\sqrt{3\pi}}|t-s|.
\]
So \((\widehat f_n)\) is uniformly bounded and equicontinuous on the compact interval \([-M,M]\). By the Arzelà--Ascoli theorem there is a subsequence \((\widehat f_{n_k})\) converging uniformly on \([-M,M]\) to some continuous function
\[
g\in C([-M,M],\mathbb C).
\]
This is exactly the required conclusion.
:::
:::
