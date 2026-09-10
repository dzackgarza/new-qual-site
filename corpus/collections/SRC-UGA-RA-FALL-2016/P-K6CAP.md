---
schema: qual/card@1
id: P-K6CAP
kind: problem
title: $\lim_{n\to\infty}\int_{\RR}f(x)g(x+n)\,dx=0$ for $f,g\in L^2(\RR)$
classification:
  areas:
  - real-analysis
  topics:
  - L²
  - Small Tails
  - Convergence of Integrals
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Problem 6 of the official UGA August 2016 real-analysis qualifying exam; replaced the legacy tail estimate by a rigorous compact-support approximation argument.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

Let $f, g \in L^2(\RR)$. Show that
\[
\lim _{n \to \infty} \int _{\RR} f(x) g(x+n) \,dx = 0
\]

:::{.concept}
\envlist
- Cauchy Schwarz: $\norm{fg}_1 \leq \norm{f}_1 \norm{g}_1$.
- Small tails in $L^p$.
:::

::: solution

Let
\[
I_n:=\int_{\mathbb R} f(x)g(x+n)\,dx.
\]
Fix $\varepsilon>0$. Choose $h\in L^2(\mathbb R)$ with compact support such that
\[
\|g-h\|_2<\frac{\varepsilon}{2(1+\|f\|_2)}.
\]
Then, by Cauchy--Schwarz and translation invariance,
\[
\left|\int f(x)(g-h)(x+n)\,dx\right|
\le \|f\|_2\|g-h\|_2<\frac\varepsilon2.
\]

Choose $R>0$ so that $h=0$ a.e. outside $[-R,R]$. Then
\[
\int f(x)h(x+n)\,dx
=\int_{-n-R}^{-n+R}f(x)h(x+n)\,dx,
\]
so
\[
\left|\int f(x)h(x+n)\,dx\right|
\le \|h\|_2
\left(\int_{-n-R}^{-n+R}|f(x)|^2\,dx\right)^{1/2}.
\]
Since $f\in L^2(\mathbb R)$, its $L^2$ tails tend to zero, and therefore the last expression tends to $0$ as $n\to\infty$. For all sufficiently large $n$ it is below $\varepsilon/2$. Hence $|I_n|<\varepsilon$ eventually, proving
\[
\boxed{\lim_{n\to\infty}\int_{\mathbb R}f(x)g(x+n)\,dx=0.}
\]
:::
