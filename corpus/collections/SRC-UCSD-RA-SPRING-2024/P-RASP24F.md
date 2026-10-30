---
schema: qual/card@1
id: P-RASP24F
kind: problem
title: 'Fourier uncertainty principle for $L^2$ functions supported on a set of finite measure'
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
  note: Checked against Problem 6 of the official UCSD Spring 2024 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Let $f \in L^2(\RR^n)$ be such that $f(x) = 0$ for a.e. $x \in \RR^n \setminus A$, where $m(A) < \infty$.
Show that, for any measurable $E \subset \RR^n$,
$$
\int_E \abs{\hat{f}(\xi)}^2\,d\xi \leq m(A)\,m(E)\,\norm{f}_{L^2}^2.
$$
:::

::: {.solution}
Since $f=0$ almost everywhere outside $A$ and $m(A)<\infty$, Cauchy--Schwarz gives
$$
\norm{f}_1
=\int_A\abs{f(x)}\,dx
\le m(A)^{1/2}\norm{f}_2.
$$
Thus $f\in L^1(\RR^n)$, so its Fourier transform is defined pointwise by the Fourier integral. For every $\xi\in\RR^n$,
$$
\abs{\widehat f(\xi)}
\le \int_{\RR^n}\abs{f(x)}\,dx
=\norm{f}_1
\le m(A)^{1/2}\norm{f}_2.
$$
Therefore
$$
\abs{\widehat f(\xi)}^2
\le m(A)\norm{f}_2^2
$$
for every $\xi$. Integrating over the measurable set $E$ gives
$$
\int_E\abs{\widehat f(\xi)}^2\,d\xi
\le m(E)m(A)\norm{f}_2^2.
$$
Hence
$$
\boxed{
\int_E\abs{\widehat f(\xi)}^2\,d\xi
\le m(A)m(E)\norm{f}_{L^2}^2.}
$$
If $m(E)=\infty$, the same inequality is understood in the extended-real sense and is immediate from the pointwise bound.
:::
