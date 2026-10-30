---
schema: qual/card@1
id: P-RAF04C
kind: problem
title: 'Translation inner product of $L^2$ functions vanishes at infinity'
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

::: {.problem}
Let $f$ and $g$ be two real $L^2(\RR, m)$-functions.
Show
$$
\lim_{n \to \infty} \int_\RR f(x) g(x-n) \, dx = 0.
$$

Hint: First prove the result holds if $g \in L^2(\RR, m)$ is further assumed to have compact support. Under this assumption, notice that the following identity holds for sufficiently large $M$:
$$
\int_\RR f(x) g(x-n) \, dx = \int_\RR \left[f(x) 1_{[-M,M]}(x-n)\right] g(x-n) \, dx = \bigl(f(\cdot) 1_{[-M,M]}(\cdot - n),\, g(\cdot - n)\bigr).
$$
:::

::: {.solution}

::: pf

::: pf-step

First assume that $g$ has compact support.

::: pf-proof

Choose $M>0$ so that $g=0$ almost everywhere outside $[-M,M]$. Then
$$
\int_{\RR}f(x)g(x-n)\,dx
=\int_{n-M}^{n+M}f(x)g(x-n)\,dx.
$$
By Cauchy--Schwarz and translation invariance of Lebesgue measure,
$$
\abs{\int_{\RR}f(x)g(x-n)\,dx}
\le
\left(\int_{n-M}^{n+M}\abs{f(x)}^2\,dx\right)^{1/2}\norm{g}_2.
$$
Since $f\in L^2(\RR)$,
$$
\int_{n-M}^{n+M}\abs{f(x)}^2\,dx
\le \int_{n-M}^{\infty}\abs{f(x)}^2\,dx\longrightarrow0.
$$
Hence the desired limit is $0$ whenever $g$ has compact support.

:::

:::

::: pf-step

Approximate an arbitrary $g\in L^2$ by compactly supported functions.

::: pf-proof

Let
$$
g_R=g\,\mathbf1_{[-R,R]}.
$$
Then $g_R\to g$ in $L^2(\RR)$. For every $n$,
$$
\begin{aligned}
\abs{\int f(x)g(x-n)\,dx}
&\le
\abs{\int f(x)g_R(x-n)\,dx}\\
&\qquad+
\abs{\int f(x)(g-g_R)(x-n)\,dx}.
\end{aligned}
$$
The second term is bounded, uniformly in $n$, by
$$
\norm{f}_2\,\norm{g-g_R}_2.
$$
Given $\varepsilon>0$, choose $R$ so large that this bound is below $\varepsilon$. For that fixed $R$, Step 1 gives
$$
\int f(x)g_R(x-n)\,dx\longrightarrow0.
$$
Thus the limsup of the original correlations is at most $\varepsilon$. Since $\varepsilon$ is arbitrary,
$$
\boxed{
\lim_{n\to\infty}\int_{\RR}f(x)g(x-n)\,dx=0.}
$$

:::

:::

:::

:::
