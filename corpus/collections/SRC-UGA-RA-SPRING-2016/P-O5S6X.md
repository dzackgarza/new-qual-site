---
schema: qual/card@1
id: P-O5S6X
kind: problem
title: The overlap $m(E\cap(E+x))$ is $L^1$, uniformly continuous, and vanishes at
  infinity
classification:
  areas:
  - real-analysis
  topics:
  - Convolution
  - Uniform Continuity
  - Measure Theory
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Spring 2016 Problem 4 in the preserved UGA source.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Corrected the translated tail set in the proof of vanishing at infinity.
---

::: problem
Let $E \subset \RR$ be measurable with $m(E) < \infty$.
Define
\[
f(x)=m(E \cap(E+x)).
\]

Show that

1. $f\in L^1(\RR)$.

2. $f$ is uniformly continuous.

3. $\lim _{|x| \to \infty} f(x) = 0$.

> Hint:
\[
\chi_{E \cap(E+x)}(y)=\chi_{E}(y) \chi_{E}(y-x)
\]
:::
::: solution
<1>1. Express the overlap as a convolution and prove integrability.
::: proof
Let $\widetilde\chi_E(u):=\chi_E(-u)$. The hint gives
\[
f(x)=\int_{\mathbb R}\chi_E(y)\chi_E(y-x)\,dy
=(\chi_E*\widetilde\chi_E)(x).
\]
Since $m(E)<\infty$, both factors lie in $L^1(\mathbb R)$. Tonelli gives
\[
\begin{aligned}
\int_{\mathbb R}f(x)\,dx
&=\int_{\mathbb R}\int_{\mathbb R}
\chi_E(y)\chi_E(y-x)\,dy\,dx\\
&=m(E)^2<\infty.
\end{aligned}
\]
Thus $f\in L^1(\mathbb R)$.
:::

<1>2. Prove uniform continuity.
::: proof
For $h\in\mathbb R$,
\[
\begin{aligned}
|f(x+h)-f(x)|
&\le \int_{\mathbb R}\chi_E(y)
|\widetilde\chi_E(x+h-y)-\widetilde\chi_E(x-y)|\,dy\\
&\le \|\tau_h\widetilde\chi_E-\widetilde\chi_E\|_1.
\end{aligned}
\]
Translations are continuous in $L^1$, so the right-hand side tends to $0$ as $h\to0$, independently of $x$. Hence $f$ is uniformly continuous.
:::

<1>3. Prove that $f(x)\to0$ as $|x|\to\infty$.
::: proof
Let $\varepsilon>0$. Choose $R>0$ such that
\[
m(E\setminus[-R,R])<\varepsilon.
\]
If $|x|>2R$ and $y\in E\cap(E+x)$, then $y\in E$ and $y-x\in E$. The two numbers $y$ and $y-x$ cannot both lie in $[-R,R]$, because then
\[
|x|=|y-(y-x)|\le2R.
\]
Therefore
\[
E\cap(E+x)
\subseteq
\bigl(E\setminus[-R,R]\bigr)
\cup
\bigl((E\setminus[-R,R])+x\bigr).
\]
By translation invariance,
\[
f(x)=m(E\cap(E+x))
\le 2m(E\setminus[-R,R])<2\varepsilon.
\]
Hence
\[
\boxed{\lim_{|x|\to\infty}f(x)=0.}
\]
:::
:::
