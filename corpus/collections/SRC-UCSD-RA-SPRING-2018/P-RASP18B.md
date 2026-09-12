---
schema: qual/card@1
id: P-RASP18B
kind: problem
title: "L^1 convergence from a.e. convergence with uniform L^2 bound"
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
  note: Checked against Problem 2 of the official UCSD Spring 2018 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Let $\{f_n\}_{n \geq 1}$ be a sequence of functions in $L^2([0,1], m)$ such that $\|f_n\|_2 \leq 1$ for all $n \geq 1$.
Assume that $\lim_{n \to \infty} f_n(x) = 0$ for almost every $x \in [0,1]$.

1. Show that $\lim_{n \to \infty} \|f_n\|_1 = 0$.

2. Give an example showing that we do not necessarily have $\lim_{n \to \infty} \|f_n\|_2 = 0$.
:::


::: solution
<1>1. Prove \(L^1\)-convergence.
::: proof
Fix \(\varepsilon>0\). By Egorov's theorem, since \([0,1]\) has finite measure and \(f_n\to0\) almost everywhere, there exists a measurable set \(E\subset[0,1]\) with
\[
m(E)<\frac{\varepsilon^2}{4}
\]
such that \(f_n\to0\) uniformly on \([0,1]\setminus E\). Hence for all sufficiently large \(n\),
\[
\sup_{[0,1]\setminus E}|f_n|<\frac\varepsilon2.
\]
Therefore
\[
\begin{aligned}
\|f_n\|_1
&\le \int_{[0,1]\setminus E}|f_n|+\int_E|f_n|\\
&\le \frac\varepsilon2
+ m(E)^{1/2}\|f_n\|_2\\
&<\frac\varepsilon2+\frac\varepsilon2=\varepsilon,
\end{aligned}
\]
where the second term uses Cauchy--Schwarz and \(\|f_n\|_2\le1\). Thus
\[
\boxed{\|f_n\|_1\to0.}
\]
:::

<1>2. Give a counterexample for \(L^2\)-convergence.
::: proof
Define
\[
f_n(x)=\sqrt n\,\mathbf1_{(0,1/n)}(x).
\]
For every \(x\in[0,1]\), \(f_n(x)\to0\). But
\[
\|f_n\|_2^2
=n\,m((0,1/n))=1.
\]
Hence
\[
\boxed{\|f_n\|_2=1\text{ for every }n,}
\]
so a.e. convergence together with a uniform \(L^2\) bound does not force \(L^2\)-norm convergence.
:::
:::
