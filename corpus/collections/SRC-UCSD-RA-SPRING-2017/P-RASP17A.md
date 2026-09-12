---
schema: qual/card@1
id: P-RASP17A
kind: problem
title: "Three limits via monotone and dominated convergence"
classification:
  areas:
  - real-analysis
  topics:
  - Monotone Convergence
  - Dominated Convergence
  - Oscillatory Integrals
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Problem 1 of the official UCSD Spring 2017 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
In each case below find $L$ (allowing for values of $\pm\infty$) and justify the calculations:

1. $L = \lim_{n \to \infty} \int_0^1 \frac{\min(nx, 1)}{x} \, dx$

2. $L = \lim_{n \to \infty} \int_1^\infty x^{-3/2} e^{inx} \, dx$

3. $L = \lim_{n \to \infty} \int_0^\infty e^{-n^2 x^2} \cos(e^{-n^2 x^2}) \, n^2 x \, dx$
:::


::: solution
<1>1. Evaluate the first limit.
::: proof
For \(n\ge1\),
\[
\frac{\min(nx,1)}x=
\begin{cases}
n,&0<x\le 1/n,\\
1/x,&1/n<x\le1.
\end{cases}
\]
Hence
\[
\int_0^1\frac{\min(nx,1)}x\,dx
=\int_0^{1/n}n\,dx+\int_{1/n}^1\frac{dx}{x}
=1+\log n.
\]
Therefore
\[
\boxed{L=+\infty.}
\]
:::

<1>2. Evaluate the oscillatory integral.
::: proof
Let \(u(x)=x^{-3/2}\). Then \(u'(x)=-\frac32x^{-5/2}\in L^1([1,\infty))\). Integration by parts gives, for \(R>1\),
\[
\int_1^R u(x)e^{inx}\,dx
=\left[\frac{u(x)e^{inx}}{in}\right]_1^R
-\frac1{in}\int_1^R u'(x)e^{inx}\,dx.
\]
Letting \(R\to\infty\), since \(u(R)\to0\),
\[
\left|\int_1^\infty x^{-3/2}e^{inx}\,dx\right|
\le \frac1n\left(1+\int_1^\infty|u'(x)|\,dx\right).
\]
The right side tends to \(0\). Thus
\[
\boxed{L=0.}
\]
:::

<1>3. Evaluate the third integral exactly.
::: proof
Put \(u=n^2x^2\). Then \(du=2n^2x\,dx\), so
\[
\begin{aligned}
\int_0^\infty e^{-n^2x^2}\cos(e^{-n^2x^2})n^2x\,dx
&=\frac12\int_0^\infty e^{-u}\cos(e^{-u})\,du.
\end{aligned}
\]
Now set \(y=e^{-u}\). Since \(du=-dy/y\),
\[
\frac12\int_0^\infty e^{-u}\cos(e^{-u})\,du
=\frac12\int_0^1\cos y\,dy
=\frac12\sin1.
\]
The expression is independent of \(n\), hence
\[
\boxed{L=\frac12\sin1.}
\]
:::
:::
