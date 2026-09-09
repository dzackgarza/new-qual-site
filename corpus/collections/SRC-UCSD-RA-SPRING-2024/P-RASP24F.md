---
schema: qual/card@1
id: P-RASP24F
kind: problem
title: "Fourier uncertainty principle for compactly supported L^2 functions"
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

::: problem
Let $f \in L^2(\mathbb{R}^n)$ be such that $f(x) = 0$ for a.e. $x \in \mathbb{R}^n \setminus A$, where $m(A) < \infty$.
Show that, for any measurable $E \subset \mathbb{R}^n$,
$$
\int_E |\hat{f}(\xi)|^2\,d\xi \leq m(A)\,m(E)\,\|f\|_{L^2}^2.
$$
:::

::: solution
Since $f=0$ almost everywhere outside $A$ and $m(A)<\infty$, Cauchy--Schwarz gives
\[
\|f\|_1
=\int_A|f(x)|\,dx
\le m(A)^{1/2}\|f\|_2.
\]
Thus $f\in L^1(\mathbb R^n)$, so its Fourier transform is defined pointwise by the Fourier integral. For every $\xi\in\mathbb R^n$,
\[
|\widehat f(\xi)|
\le \int_{\mathbb R^n}|f(x)|\,dx
=\|f\|_1
\le m(A)^{1/2}\|f\|_2.
\]
Therefore
\[
|\widehat f(\xi)|^2
\le m(A)\|f\|_2^2
\]
for every $\xi$. Integrating over the measurable set $E$ gives
\[
\int_E|\widehat f(\xi)|^2\,d\xi
\le m(E)m(A)\|f\|_2^2.
\]
Hence
\[
\boxed{
\int_E|\widehat f(\xi)|^2\,d\xi
\le m(A)m(E)\|f\|_{L^2}^2.}
\]
If $m(E)=\infty$, the same inequality is understood in the extended-real sense and is immediate from the pointwise bound.
:::
