---
schema: qual/card@1
id: P-RAF04C
kind: problem
title: "Translation inner product of L^2 functions vanishes at infinity"
classification:
  areas:
  - real-analysis
  topics:
  - L2 Spaces
  - Translations
  - Dense Subsets
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 3 of the official UCSD Fall 2004 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Let $f$ and $g$ be two real $L^2(\mathbb{R}, m)$-functions.
Show
$$
\lim_{n \to \infty} \int_\mathbb{R} f(x) g(x-n) \, dx = 0.
$$

Hint: First prove the result holds if $g \in L^2(\mathbb{R}, m)$ is further assumed to have compact support.
:::

::: solution
<1>1. First assume that $g$ has compact support.
::: proof
Choose $M>0$ so that $g=0$ almost everywhere outside $[-M,M]$. Then
\[
\int_{\mathbb R}f(x)g(x-n)\,dx
=\int_{n-M}^{n+M}f(x)g(x-n)\,dx.
\]
By Cauchy--Schwarz and translation invariance of Lebesgue measure,
\[
\left|\int_{\mathbb R}f(x)g(x-n)\,dx\right|
\le
\left(\int_{n-M}^{n+M}|f(x)|^2\,dx\right)^{1/2}\|g\|_2.
\]
Since $f\in L^2(\mathbb R)$,
\[
\int_{n-M}^{n+M}|f(x)|^2\,dx
\le \int_{n-M}^{\infty}|f(x)|^2\,dx\longrightarrow0.
\]
Hence the desired limit is $0$ whenever $g$ has compact support.
:::

<1>2. Approximate an arbitrary $g\in L^2$ by compactly supported functions.
::: proof
Let
\[
g_R=g\,\mathbf1_{[-R,R]}.
\]
Then $g_R\to g$ in $L^2(\mathbb R)$. For every $n$,
\[
\begin{aligned}
\left|\int f(x)g(x-n)\,dx\right|
&\le
\left|\int f(x)g_R(x-n)\,dx\right|\\
&\qquad+
\left|\int f(x)(g-g_R)(x-n)\,dx\right|.
\end{aligned}
\]
The second term is bounded, uniformly in $n$, by
\[
\|f\|_2\,\|g-g_R\|_2.
\]
Given $\varepsilon>0$, choose $R$ so large that this bound is below $\varepsilon$. For that fixed $R$, Step 1 gives
\[
\int f(x)g_R(x-n)\,dx\longrightarrow0.
\]
Thus the limsup of the original correlations is at most $\varepsilon$. Since $\varepsilon$ is arbitrary,
\[
\boxed{
\lim_{n\to\infty}\int_{\mathbb R}f(x)g(x-n)\,dx=0.}
\]
:::
:::
