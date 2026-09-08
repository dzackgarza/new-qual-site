---
schema: qual/card@1
id: P-JHUSP08ANC
kind: problem
title: "Absolute convergence of the Fourier series of a C1 periodic function"
classification:
  areas:
  - real-analysis
  topics:
  - Fourier Series
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 3 of the JHU Analysis Qualifying Exam, Spring 2008, in the preserved exam collection.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Let $f$ be a continuously differentiable $2\pi$-periodic function on $\mathbb R$, with Fourier coefficients
\[
\widehat f(n)=\frac1{2\pi}\int_0^{2\pi}f(t)e^{-int}\,dt.
\]
Show that the Fourier series
\[
\sum_{n\in\mathbb Z}\widehat f(n)e^{int}
\]
is absolutely convergent for every $t$.
:::

::: {.solution}
Because $f$ is $2\pi$-periodic and $C^1$, integration by parts gives, for every $n\ne0$,
\[
\begin{aligned}
\widehat{f'}(n)
&=\frac1{2\pi}\int_0^{2\pi}f'(t)e^{-int}\,dt\\
&=\frac1{2\pi}\bigl[f(t)e^{-int}\bigr]_0^{2\pi}
+in\widehat f(n)\\
&=in\widehat f(n),
\end{aligned}
\]
since $f(2\pi)=f(0)$.

Now $f'\in L^2([0,2\pi])$. By Bessel's inequality,
\[
\sum_{n\in\mathbb Z}|\widehat{f'}(n)|^2<\infty.
\]
Hence
\[
\sum_{n\ne0}n^2|\widehat f(n)|^2<\infty.
\]
Therefore Cauchy--Schwarz yields
\[
\begin{aligned}
\sum_{n\ne0}|\widehat f(n)|
&=\sum_{n\ne0}\frac1{|n|}\,|n\widehat f(n)|\\
&\le
\left(\sum_{n\ne0}\frac1{n^2}\right)^{1/2}
\left(\sum_{n\ne0}n^2|\widehat f(n)|^2\right)^{1/2}
<\infty.
\end{aligned}
\]
Adding the single term $|\widehat f(0)|$ gives
\[
\sum_{n\in\mathbb Z}|\widehat f(n)|<\infty.
\]
Since $|e^{int}|=1$, for every $t$,
\[
\sum_{n\in\mathbb Z}|\widehat f(n)e^{int}|
=\sum_{n\in\mathbb Z}|\widehat f(n)|<\infty.
\]
Thus the Fourier series converges absolutely for every $t$.
:::
