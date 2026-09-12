---
schema: qual/card@1
id: P-RASP18A
kind: problem
title: "Limits of integrals involving rational functions with exponentials"
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
  note: Checked against Problem 1 of the official UCSD Spring 2018 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Compute the following two limits allowing for the values of $\pm\infty$:

(a) $\displaystyle\lim_{n \to \infty} \int_0^\infty \frac{x^n}{1 + x^{n+2}} e^{-x/n}\,dx$

(b) $\displaystyle\lim_{n \to \infty} \int_0^\infty \frac{x^n}{1 + x^{n+1}} e^{-x/n}\,dx$
:::


::: solution
<1>1. Evaluate part (a).
::: proof
For fixed \(x\ne1\),
\[
\frac{x^n}{1+x^{n+2}}e^{-x/n}
\longrightarrow
\begin{cases}
0,&0<x<1,\\
x^{-2},&x>1.
\end{cases}
\]
Also, for \(0<x<1\),
\[
0\le \frac{x^n}{1+x^{n+2}}e^{-x/n}\le1,
\]
while for \(x\ge1\),
\[
0\le \frac{x^n}{1+x^{n+2}}e^{-x/n}
\le \frac{x^n}{x^{n+2}}=x^{-2}.
\]
Thus the integrands are dominated by the integrable function
\[
\mathbf1_{(0,1)}+x^{-2}\mathbf1_{[1,\infty)}.
\]
The Dominated Convergence Theorem gives
\[
\boxed{
\lim_{n\to\infty}\int_0^\infty
\frac{x^n}{1+x^{n+2}}e^{-x/n}\,dx
=\int_1^\infty x^{-2}\,dx=1.}
\]
:::

<1>2. Evaluate part (b).
::: proof
The integrands are nonnegative. For every fixed \(x>1\),
\[
\frac{x^n}{1+x^{n+1}}e^{-x/n}
\longrightarrow \frac1x,
\]
while for \(0<x<1\) they tend to \(0\). Therefore Fatou's lemma gives
\[
\begin{aligned}
\liminf_{n\to\infty}
\int_0^\infty\frac{x^n}{1+x^{n+1}}e^{-x/n}\,dx
&\ge \int_1^\infty\frac{dx}{x}\\
&=+\infty.
\end{aligned}
\]
Hence
\[
\boxed{
\lim_{n\to\infty}
\int_0^\infty\frac{x^n}{1+x^{n+1}}e^{-x/n}\,dx
=+\infty.}
\]
:::
:::
