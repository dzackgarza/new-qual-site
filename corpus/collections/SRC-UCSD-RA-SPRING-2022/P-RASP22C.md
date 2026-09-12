---
schema: qual/card@1
id: P-RASP22C
kind: problem
title: "Convergence of Laplace-type averaged functions"
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
  note: Checked against Problem 3 of the official UCSD Spring 2022 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Let $f \in L^1((0,\infty) \times \mathbb{R})$ and for $n \in \mathbb{N}$ define $g_n : \mathbb{R} \to \mathbb{R}$ by
$$
g_n(x) = \int_0^\infty e^{-\lambda} f(n\lambda, x)\,d\lambda.
$$
Prove that $g_n$ converges to $0$ almost everywhere and in $L^1(\mathbb{R})$.
:::


::: solution
Make the change of variables $t=n\lambda$. Then
\[
g_n(x)
=\frac1n\int_0^\infty e^{-t/n}f(t,x)\,dt.
\]
By Fubini--Tonelli, for almost every $x\in\mathbb R$ the function
\[
t\longmapsto f(t,x)
\]
belongs to $L^1(0,\infty)$. For every such $x$,
\[
|g_n(x)|
\le \frac1n\int_0^\infty|f(t,x)|\,dt
\longrightarrow0.
\]
Hence $g_n(x)\to0$ for almost every $x$.

For the $L^1$ convergence, Tonelli gives
\[
\begin{aligned}
\|g_n\|_{L^1(\mathbb R)}
&\le \frac1n\int_{\mathbb R}\int_0^\infty
 e^{-t/n}|f(t,x)|\,dt\,dx\\
&\le \frac1n\int_{\mathbb R}\int_0^\infty
 |f(t,x)|\,dt\,dx\\
&=\frac1n\|f\|_{L^1((0,\infty)\times\mathbb R)}.
\end{aligned}
\]
Therefore
\[
\boxed{\|g_n\|_1\to0},
\]
so $g_n\to0$ in $L^1(\mathbb R)$ as well as almost everywhere.
:::
